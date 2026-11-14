---
declaration: definition
origin: cited
lean: Verifier.Extractor.Straightline.IsMonotone
statement: formalized
---

# Monotone Straightline Extractor

A straightline extractor is **monotone** if, whenever the prover's and verifier's query logs are extended (as sublists), the probability that it returns a valid input witness does not decrease.

## Depends on

- [Straightline Extractor](../part-01/def-straightline-extractor.md)

## Lean

Formalized as [`Verifier.Extractor.Straightline.IsMonotone`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.Extractor.Straightline.IsMonotone).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 503](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L503)
