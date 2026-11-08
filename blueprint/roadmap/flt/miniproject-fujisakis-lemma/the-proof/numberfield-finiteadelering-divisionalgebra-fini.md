---
declaration: theorem
origin: cited
lean: NumberField.FiniteAdeleRing.DivisionAlgebra.finiteDoubleCoset
statement: formalized
proof: formalized
---

# NumberField.FiniteAdeleRing.DivisionAlgebra.finiteDoubleCoset

If $U$ is an open subgroup of $(D\otimes_K \mathbb{A}_K^\infty)^\times$ then the double coset space $D^\times\backslash(D\otimes_K \mathbb{A}_K^\infty)^\times/U$ is finite.

## Depends on

- [NumberField.FiniteAdeleRing.DivisionAlgebra.units_cocompact](numberfield-finiteadelering-divisionalgebra-unit.md)

## Proof

The double cosets give a disjoint open cover of $(D\otimes_K \mathbb{A}_K^\infty)$ which descends to a disjoint open cover of the quotient space $D^\times\backslash(D\otimes_K \mathbb{A}_K^\infty)^\times$. However this space is compact by theorem [NumberField.FiniteAdeleRing.DivisionAlgebra.units_cocompact](numberfield-finiteadelering-divisionalgebra-unit.md).

## Lean

Formalized as [`NumberField.FiniteAdeleRing.DivisionAlgebra.finiteDoubleCoset`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.FiniteAdeleRing.DivisionAlgebra.finiteDoubleCoset).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 350](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L350)
