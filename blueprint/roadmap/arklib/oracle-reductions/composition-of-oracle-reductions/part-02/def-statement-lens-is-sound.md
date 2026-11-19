---
declaration: definition
origin: cited
lean: Statement.Lens.IsSound
statement: formalized
---

# Soundness-Preserving Statement Lens

A statement lens preserves soundness if projection maps statements outside the outer input language to statements outside the inner input language, and lifting maps an outer input outside its language together with a compatible inner output outside its language to an outer output outside its language. The same condition serves ordinary and round-by-round soundness.

## Depends on

- [Statement Lens](../part-01/def-statement-lens.md)

## Lean

Formalized as [`Statement.Lens.IsSound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Statement.Lens.IsSound).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 372](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L372)
