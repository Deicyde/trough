---
declaration: lemma
origin: cited
lean: NumberField.AdeleRing.DivisionAlgebra.Aux.X_meets_kernel
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.DivisionAlgebra.Aux.X\_meets\_kernel

If $\beta\in D_{\mathbb{A}}^{(1)}$ then $\beta X\cap D^\times\not=\emptyset$.

## Depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.X](numberfield-adelering-divisionalgebra-aux-x.md)
- [NumberField.AdeleRing.DivisionAlgebra.Aux.E](numberfield-adelering-divisionalgebra-aux-e.md)

## Proof

Indeed by lemma [Lemma NumberField.AdeleRing.DivisionAlgebra.Aux.existsE](numberfield-adelering-divisionalgebra-aux-exists.md), the map $\beta E\to D\backslash D_{\mathbb{A}}$ isn't injective, so there are distinct $\beta e_1,\beta e_2\in \beta E$ with $e_i\in E$ and $\beta e_1-\beta e_2=b\in D$. Now $b\not=0$ and $D$ is a division algebra, so $b\in D^\times$. And $e_1-e_2\in X$ so $b=\beta(e_1-e_2)\in \beta X$, so we're done.

## Lean

Formalized as [`NumberField.AdeleRing.DivisionAlgebra.Aux.X_meets_kernel`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.DivisionAlgebra.Aux.X_meets_kernel).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 179](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L179)
