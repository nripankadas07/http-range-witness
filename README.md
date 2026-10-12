# http-range-witness

Public alpha prepared on 12 October 2026. **Remote verification pending; not yet a verified launch.**
Original Python implementation, MIT, zero runtime dependencies. AI-assisted development.

HTTP storage maintainer inspecting captured Range requests. Explain suffix, open-ended and overlapping ranges and transfer amplification for a known representation size.

Bounded byte-range planner with per-member reasons, original request order and separate coalesced coverage.

## Install and first useful result

Python 3.10+ (only Linux Python 3.12.14 tested in this preparation). Build requires setuptools 61+ and wheel already available; install into a fresh venv uses only the generated wheel. Run source tests with your build interpreter:

```sh
python -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse .
python -m venv .venv
.venv/bin/python -m pip install --no-index --no-deps wheelhouse/*.whl
.venv/bin/http-range-witness example.json
python -m unittest -v
```

The included synthetic input documents the exact normalized JSON schema.
Output is deterministic JSON; malformed inputs exit 2. Inputs are limited to 1 MiB.
No network connections, credential reads or writes to input files occur.
Hostnames, identifiers, paths and selected SSH values may be disclosed in output.
Review exported inputs and outputs before sharing. Use synthetic examples for reports.

## Scope and limits

Nonempty representations only; no HTTP server, If-Range, encoding negotiation or multipart responses.

Specific demand: Inferred; range-parser's API and merge-order report establish an existing workflow, not missing competitor behavior.
Discovery: HTTP range debugging and download fixture examples.
Portfolio distinction: No owned tool plans byte-range coverage; cache-header-contract concerns caching policy.
See RESEARCH.md and the bundled research record for alternatives and incomplete research coverage.
No competitor absence, performance superiority or customer-adoption claim.

## Acceptance criteria

- Correct inclusive endpoints, clamping and nonzero suffixes.
- Reject malformed or reversed ranges distinctly from unsatisfiable members.
- Count repeated transfer bytes separately from unique covered bytes.

## Support and contribution

Report a reproducible synthetic input, expected result, actual output and Python version.
Keep changes bounded and run the unit suite and clean installed example.
Do not submit private host configuration, production metric labels or credentials.
Security reports should omit secrets; this offline diagnostic is not a security boundary.
The source distribution is the supported install path; no registry release is claimed.
