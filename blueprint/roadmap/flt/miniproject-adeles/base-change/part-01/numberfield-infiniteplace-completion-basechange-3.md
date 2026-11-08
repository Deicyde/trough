---
declaration: theorem
origin: cited
lean: NumberField.InfinitePlace.Completion.baseChange_injective
statement: formalized
---

# NumberField.InfinitePlace.Completion.baseChange_injective

For a fixed infinite place $v$ of $K$, the map $L\otimes_K K_v \to\prod_{w\mid v}L_w$ is injective.

## Depends on

Its statement uses no other node that has an article here.

## Proof

The $L$-algebra map $L\otimes_K K_v \to\prod_{w\mid v}L_w$ can equivalently be thought of as $K_v$-linear, which is injective, because it is surjective by Theorem [NumberField.InfinitePlace.Completion.baseChange_surjective](numberfield-infiniteplace-completion-basechange-2.md), and both side have the same $K_v$-dimension by Theorem [NumberField.InfinitePlace.Completion.finrank_pi_eq_finrank_tensorProduct](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L726).

## Lean

Stated as [`NumberField.InfinitePlace.Completion.baseChange_injective`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfinitePlace.Completion.baseChange_injective); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 778](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L778)
