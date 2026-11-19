---
declaration: theorem
origin: cited
lean: Reduction.append_perfectCompleteness_of_pure_verifiers
statement: formalized
---

# Perfect Completeness Preservation under Append

Under the pure-verifier and execution hypotheses of Theorem [Completeness Preservation under Append](thm-completeness-append.md), suppose $R_1$ is perfectly complete from $\mu$ and $R_2$ is perfectly complete from every deterministic shared state. Then $R_1.\mathsf{append}\ R_2$ is perfectly complete from $\mu$.

## Depends on

- [Perfect Completeness](../../definitions/part-01/def-perfect-completeness.md)
- [Reduction Append](def-reduction-append.md)
- [Completeness Preservation under Append](thm-completeness-append.md)

## Lean

Stated as [`Reduction.append_perfectCompleteness_of_pure_verifiers`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.append_perfectCompleteness_of_pure_verifiers); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 146](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L146)
