---
declaration: definition
origin: cited
lean: Context.Lens.IsComplete
statement: formalized
---

# Completeness-Preserving Context Lens

A context lens preserves completeness if projection maps the outer input relation into the inner input relation, and lifting maps every compatible pair of a valid outer input and a valid inner output into the outer output relation.

## Depends on

- [Context Lens](def-context-lens.md)

## Lean

Formalized as [`Context.Lens.IsComplete`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Context.Lens.IsComplete).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 362](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L362)
