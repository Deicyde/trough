---
declaration: theorem
origin: cited
lean: Reduction.seqCompose_completeness_of_pure
statement: formalized
---

# General Completeness Preservation

Let $R_0, \ldots, R_{k-1}$ be a finite chain with compatible consecutive relations. Every prover has pure output and every verifier is pure and total. For each $i$ and each $s \in \Sigma$, assume $R_i$ is complete with error $\epsilon_i$ from the deterministic initial state $s$. Then the chain is complete from any initial distribution $\mu$, with error $\sum_{i=0}^{k-1} \epsilon_i$.

## Depends on

- [Completeness](../../definitions/part-01/def-completeness.md)
- [General Reduction Composition](def-reduction-compose.md)
- [Completeness Preservation under Append](thm-completeness-append.md)

## Lean

Stated as [`Reduction.seqCompose_completeness_of_pure`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.seqCompose_completeness_of_pure); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 208](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L208)
