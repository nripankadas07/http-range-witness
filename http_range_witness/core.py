import re

def run(data):
    size, header = data.get("size"), data.get("range")
    if type(size) is not int or not 0<size<=2**63-1 or not isinstance(header,str) or len(header)>4096:
        raise ValueError("positive bounded representation size and Range string required")
    if header[:6].lower() != "bytes=":
        raise ValueError("only bytes unit supported")
    fields=header[6:].split(",")
    if not 1<=len(fields)<=32:
        raise ValueError("at most 32 ranges")
    requests=[]
    for field in fields:
        m=re.fullmatch(r"([0-9]*)-([0-9]*)",field.strip())
        if not m or not any(m.groups()) or any(len(x)>19 for x in m.groups()):
            raise ValueError("malformed byte range")
        first,last=m.groups()
        if first:
            start=int(first)
            finish=int(last) if last else size-1
            if last and finish<start:
                raise ValueError("reversed range")
            reason="starts_beyond_representation" if start>=size else None
            finish=min(finish,size-1)
        else:
            suffix=int(last)
            reason="zero_suffix" if suffix==0 else None
            start=max(0,size-suffix)
            finish=size-1
        requests.append({"field":field.strip(),"start":start if reason is None else None,"end":finish if reason is None else None,"reason":reason})
    accepted=[(x["start"],x["end"]) for x in requests if x["reason"] is None]
    merged=[]
    for start,end in sorted(accepted):
        if merged and start<=merged[-1][1]+1:
            merged[-1][1]=max(merged[-1][1],end)
        else:
            merged.append([start,end])
    requested=sum(b-a+1 for a,b in accepted)
    covered=sum(b-a+1 for a,b in merged)
    return {"satisfiable":bool(accepted),"requests":requests,"coverage":merged,"requested_bytes":requested,"unique_bytes":covered,"repeated_bytes":requested-covered}
