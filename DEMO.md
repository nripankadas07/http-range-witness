# Synthetic demo

Use the installed command with `example.json`; the expected deterministic output is:

```json
{
  "coverage": [
    [
      0,
      14
    ],
    [
      95,
      99
    ]
  ],
  "repeated_bytes": 5,
  "requested_bytes": 25,
  "requests": [
    {
      "end": 9,
      "field": "0-9",
      "reason": null,
      "start": 0
    },
    {
      "end": 14,
      "field": "5-14",
      "reason": null,
      "start": 5
    },
    {
      "end": 99,
      "field": "-5",
      "reason": null,
      "start": 95
    },
    {
      "end": null,
      "field": "150-",
      "reason": "starts_beyond_representation",
      "start": null
    }
  ],
  "satisfiable": true,
  "unique_bytes": 20
}
```

This proves the documented example only, not production efficacy or adoption.
