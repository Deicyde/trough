---
declaration: lemma
origin: cited
lean: NumberField.AdeleRing.DivisionAlgebra.Aux.T_finite
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.DivisionAlgebra.Aux.T_finite

$T$ is finite.

## Depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.T](numberfield-adelering-divisionalgebra-aux-t.md)

## Proof depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.Y_compact](numberfield-adelering-divisionalgebra-aux-y-comp.md)

## Proof

It suffices to prove that $Y\cap D$ is finite. But $D\subseteq D_{\mathbb{A}}$ is a discrete additive subgroup, and hence closed. And $Y\subseteq D_{\mathbb{A}}$ is compact. So $D\cap Y$ is compact and discrete, so finite.

## Lean

Formalized as [`NumberField.AdeleRing.DivisionAlgebra.Aux.T_finite`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.DivisionAlgebra.Aux.T_finite).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 228](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L228)
