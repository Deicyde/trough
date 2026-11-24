---
declaration: theorem
origin: cited
lean: Reduction.liftContext_completeness, Reduction.liftContext_perfectCompleteness
statement: formalized
---

# Completeness Preservation under Context Lifting

If a reduction is complete with error $\epsilon$ and the context lens is completeness-preserving, then the lifted reduction is complete with error $\epsilon$. The same holds for perfect completeness.

## Depends on

- [Completeness](../../definitions/part-01/def-completeness.md)
- [Reduction Context Lifting](def-reduction-lift-context.md)
- [Completeness-Preserving Context Lens](def-context-lens-is-complete.md)

## Lean

Stated as [`Reduction.liftContext_completeness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.liftContext_completeness), [`Reduction.liftContext_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Reduction.liftContext_perfectCompleteness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 405](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/composition.tex#L405)
