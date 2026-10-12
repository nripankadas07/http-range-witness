import json, os, pathlib, subprocess, sys, tempfile, unittest
from http_range_witness.core import run

CASES = [({'size': 100, 'range': 'bytes=0-9'}, {'coverage': [[0, 9]], 'unique_bytes': 10}), ({'size': 100, 'range': 'bytes=90-999'}, {'coverage': [[90, 99]], 'unique_bytes': 10}), ({'size': 100, 'range': 'bytes=95-'}, {'coverage': [[95, 99]]}), ({'size': 100, 'range': 'bytes=-5'}, {'coverage': [[95, 99]]}), ({'size': 100, 'range': 'bytes=-500'}, {'coverage': [[0, 99]]}), ({'size': 100, 'range': 'bytes=0-9,5-14'}, {'requested_bytes': 20, 'unique_bytes': 15, 'repeated_bytes': 5}), ({'size': 100, 'range': 'bytes=100-,-0'}, {'satisfiable': False, 'coverage': []}), ({'size': 100, 'range': 'bytes=50-59,0-9'}, 'order'), ({'size': 100, 'range': 'bytes=10-2'}, 'error'), ({'size': 100, 'range': 'items=0-9'}, 'error'), ({'size': 0, 'range': 'bytes=-5'}, 'error'), ({'size': True, 'range': 'bytes=0-1'}, 'error')]

class ContractTests(unittest.TestCase):
    def test_unit_case_insensitive(self):
        expected = run({"size": 100, "range": "bytes=0-9,-5"})
        for unit in ("BYTES", "Bytes", "bYtEs"):
            with self.subTest(unit=unit):
                self.assertEqual(run({"size": 100, "range": unit + "=0-9,-5"}), expected)

    def test_cli_demo(self):
        r=subprocess.run([sys.executable,"-c","from http_range_witness.cli import main; raise SystemExit(main())","example.json"],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIsInstance(json.loads(r.stdout),dict)

    def test_cli_malformed(self):
        with tempfile.TemporaryDirectory() as d:
            path=pathlib.Path(d)/"bad.json";path.write_text("[broken")
            r=subprocess.run([sys.executable,"-c","from http_range_witness.cli import main; raise SystemExit(main())",str(path)],text=True,capture_output=True)
            self.assertEqual(r.returncode,2)
            self.assertEqual(r.stdout,"")
            self.assertIn("input error",r.stderr)

def make_case(data,expected):
    def test(self):
        before=json.dumps(data,sort_keys=True)
        if expected=="error":
            with self.assertRaises(ValueError): run(data)
        else:
            result=run(data)
            if expected=="opaque":
                self.assertEqual(set(result["paths"]),{"d","d/new","other"})
                self.assertEqual(result["whiteouts"][0]["removed"],["d/a"])
            elif expected=="order":
                self.assertEqual([r["start"] for r in result["requests"]],[50,0])
                self.assertEqual(result["coverage"],[[0,9],[50,59]])
            else:
                for key,value in expected.items(): self.assertEqual(result[key],value)
        self.assertEqual(json.dumps(data,sort_keys=True),before,"input mutated")
    return test
for i,(data,expected) in enumerate(CASES):
    setattr(ContractTests,"test_contract_%02d"%i,make_case(data,expected))

if __name__=="__main__": unittest.main()
