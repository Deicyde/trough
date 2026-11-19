---
declaration: definition
origin: cited
lean: Extractor.Lens.IsKnowledgeSound
statement: formalized
---

# Knowledge-Soundness-Preserving Extractor Lens

An extractor lens preserves knowledge soundness if it satisfies two conditions.

- *Lift:* if the projected outer input statement and an extracted inner input witness lie in the inner input relation, then the lifted outer input witness lies in the outer input relation.
- *Project, or shortcut:* if a lifted output statement and an outer output witness lie in the outer output relation, then either the projected output witness and the inner output statement lie in the inner output relation, or every inner input witness lifts to a valid outer input witness.

The shortcut covers lenses whose outer output already certifies the outer input. Both conditions also take a compatibility predicate on witnesses; the lifting theorems use the trivial one.

## Depends on

- [Extractor Lens](def-extractor-lens.md)

## Lean

Formalized as [`Extractor.Lens.IsKnowledgeSound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Extractor.Lens.IsKnowledgeSound).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 383](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L383)
