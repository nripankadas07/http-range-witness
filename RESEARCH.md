# Qualitative research — 12 October 2026

Observed 2026-10-12 06:35:23 UTC. Search queries: `http range parser sort:stars-desc; HTTP range sort:stars-desc`.

GitHub search requested star ordering through query qualifiers. Direct repository-search REST fetch was unsupported; connector results were noisy and some irrelevant matches were rejected. Established adjacent tools were added explicitly, with current repository metadata, README and three recent open issue/PR records inspected. Ranking is the highest-star relevant comparable among these found sources, not an exhaustive global ranking. Code inspected for one relevant comparable in each area; complete competitor installations and full feature inventories were not tested.

| Repository | Stars | Last pushed UTC | API license |
| --- | ---: | --- | --- |
| [curl/curl](https://github.com/curl/curl) | 43175 | 2026-10-12T05:55:30Z | NOASSERTION |
| [aria2/aria2](https://github.com/aria2/aria2) | 43059 | 2026-06-25T14:49:35Z | GPL-2.0 |
| [jshttp/range-parser](https://github.com/jshttp/range-parser) | 99 | 2026-06-25T20:56:12Z | MIT |

Highest-star relevant/adjacent source found in this inspected set: curl/curl.

curl transfers data across many protocols, aria2 supports segmented multi-source downloads, and range-parser supplies a Node library with malformed/unsatisfiable states and optional combining. This candidate explains a strict bounded subset of byte-range requests over a known nonempty representation, showing original order separately from unique coverage. It cannot transfer data or construct HTTP responses. The upstream merge-order PR is evidence of a live workflow, not proof of a current defect or unmet feature.

Installability, examples and support were assessed from current README/issue evidence. No measured time-to-result, reliability ranking, comparative speed or superiority claim is made. Our offline installed example passes; that establishes our behavior only. Specific demand remains inferred, as stated in README. All implementation code is original; no third-party source or prose was imported.

## Current evidence links

- curl/curl: [README](https://github.com/curl/curl/blob/master/README.md), observed blob `f8061f2edc0ba8067186a83d730c949cb6f224db`.
  - [PR](https://github.com/curl/curl/pull/23369) — imap: fail on multiple literals in custom FETCH response
  - [PR](https://github.com/curl/curl/pull/23368) — schannel: retain close_notify records across send retries
  - [PR](https://github.com/curl/curl/pull/23367) — test_06_eyeballs: silence Code Quality warning
- aria2/aria2: [README](https://github.com/aria2/aria2/blob/master/README.rst), observed blob `75559047dabff9cc609760551d49b342de504cd6`.
  - [issue](https://github.com/aria2/aria2/issues/2404) — Download status messages are not displayed in real time when output is redirected
  - [PR](https://github.com/aria2/aria2/pull/2403) — Add support for OpenSSL 4
  - [issue](https://github.com/aria2/aria2/issues/2402) — [SECURITY] Unauthenticated JSON-RPC → Arbitrary File Write → Remote Code Execution (Cron-based RCE)
- jshttp/range-parser: [README](https://github.com/jshttp/range-parser/blob/master/README.md), observed blob `5103c4b65244efbf563c8a247786246a14d4e057`.
  - [PR](https://github.com/jshttp/range-parser/pull/68) — fix: keep original order when a combined range is fully absorbed
  - [PR](https://github.com/jshttp/range-parser/pull/62) — Improve parsing performance
  - [PR](https://github.com/jshttp/range-parser/pull/61) — Refactor to TypeScript
