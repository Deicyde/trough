---
declaration: theorem
origin: cited
lean: NumberField.InfinitePlace.Completion.baseChangeEquiv
statement: formalized
---

# NumberField.InfinitePlace.Completion.baseChangeEquiv

Let $v$ be an infinite place of $K$. There is a natural $L$-algebra homeomorphism $L\otimes_K K_v \cong_L \prod_{w\mid v}L_w$, whose restriction to $1\otimes_K K_v$ corresponds to the map in [Definition NumberField.InfinitePlace.Completion.piExtension](numberfield-infiniteplace-completion-piextension.md).

## Depends on

- [NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md)
- [NumberField.InfinitePlace.Completion.baseChange\_surjective](numberfield-infiniteplace-completion-basechange-2.md)
- [NumberField.InfinitePlace.Completion.baseChange\_injective](numberfield-infiniteplace-completion-basechange-3.md)
- [NumberField.InfinitePlace.Completion.instIsModuleTopologyValEqComapAlgebraMap\_fLT](numberfield-infiniteplace-completion-instismodul.md)

## Proof

The map in [Definition NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md) is an $L$-algebra isomorphism by Theorem [Theorem NumberField.InfinitePlace.Completion.baseChange\_surjective](numberfield-infiniteplace-completion-basechange-2.md) and Theorem [Theorem NumberField.InfinitePlace.Completion.baseChange\_injective](numberfield-infiniteplace-completion-basechange-3.md). Every $K_v$-algebra isomorphism between two $K_v$-module topological spaces is a homeomorphism. Since the $L$-algebra isomorphism of Definition [Definition NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md) can equivalently be viewed as a $K_v$-algebra isomorphism, it is also a homeomorphism.

## Lean

Formalized as [`NumberField.InfinitePlace.Completion.baseChangeEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfinitePlace.Completion.baseChangeEquiv).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 811](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L811)
