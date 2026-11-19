---
declaration: definition
origin: cited
lean: Fri.Spec.Extractor.extract, Fri.Spec.Extractor.extractProgram, Fri.Spec.Extractor.extractHistory, Fri.Spec.Extractor.extractHistory_eq_profile
statement: formalized
---

# fri-measured-extractor

The named straightline extractor reads only the transcript prefix preceding the query-vector challenge. It first rejects if the final polynomial has degree at least $d$, before coefficient, domain, challenge, or word accesses. Otherwise it scans every initial-domain position in order and applies the actual local checks. It counts all accepting positions and caches the first $M$ nodes and initial-word values. Fewer than $M$ acceptances yield failure. Otherwise it interpolates these cached samples and returns the polynomial if its degree is less than $M$. Its public result is the literal first projection of this measured program.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Fri.Spec.Extractor.extract`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.extract), [`Fri.Spec.Extractor.extractProgram`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.extractProgram), [`Fri.Spec.Extractor.extractHistory`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.extractHistory), [`Fri.Spec.Extractor.extractHistory_eq_profile`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.extractHistory_eq_profile).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 141](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L141)
