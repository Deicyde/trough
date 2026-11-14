---
declaration: theorem
origin: cited
lean: RandomQuery.oracleVerifier_rbrKnowledgeSoundness_of_distanceLE
statement: formalized
---

# RandomQuery Knowledge Soundness from Distance

If the oracle interface on $M$ has oracle distance at most $d$, then the RandomQuery oracle reduction satisfies round-by-round knowledge soundness with error $\frac{d}{|\mathsf{Query}|}$.

## Depends on

- [RandomQuery Oracle Reduction](def-randomquery-oracle-reduction.md)
- [Oracle Distance](def-oracle-distance.md)

## Lean

Stated as [`RandomQuery.oracleVerifier_rbrKnowledgeSoundness_of_distanceLE`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RandomQuery.oracleVerifier_rbrKnowledgeSoundness_of_distanceLE); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 170](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L170)
