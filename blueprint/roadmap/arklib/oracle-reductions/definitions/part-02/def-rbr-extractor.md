---
declaration: definition
origin: cited
lean: Extractor.RoundByRound
statement: formalized
---

# Round-by-Round Extractor

Given intermediate witness types $W_0, \ldots, W_n$, a **round-by-round extractor** extracts the input witness backward from the output witness, one round at a time. It consists of three functions, each also given the input statement $x_{\text{in}}$:

- $\mathsf{extractOut}$ maps a full transcript and an output witness to an intermediate witness in $W_n$;
- $\mathsf{extractMid}$, for each round $m < n$, maps the transcript up to round $m+1$ and an intermediate witness in $W_{m+1}$ to one in $W_m$;
- $\mathsf{extractIn}$ maps an intermediate witness in $W_0$ to an input witness.

The extractor reads no query log.

## Depends on

- [Protocol Transcript](../part-01/def-transcript.md)

## Lean

Formalized as [`Extractor.RoundByRound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Extractor.RoundByRound).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 513](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L513)
