---
declaration: lemma
origin: cited
lean: NumberField.AdeleRing.DivisionAlgebra.Aux.X_meets_kernel'
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.DivisionAlgebra.Aux.X\_meets\_kernel'

Similarly, if $\beta\in D_{\mathbb{A}}^{(1)}$ then $X\beta^{-1}\cap D^\times\not=\emptyset$.

## Depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.X](numberfield-adelering-divisionalgebra-aux-x.md)

## Proof depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.E](numberfield-adelering-divisionalgebra-aux-e.md)

## Proof

Indeed, $\beta^{-1}\in D_{\mathbb{A}}^{(1)}$, and so left multiplication by $\beta^{-1}$ doesn't change Haar measure on $D_{\mathbb{A}}$, so neither does right multiplication (by theorem addHaarScalarFactor.left\_mul\_eq\_right\_mul). So the same argument works: $E\beta^{-1}\to D\backslash D_{\mathbb{A}}$ is not injective so choose $e_1\beta^{-1}\not=e_2\beta^{-1}$ with difference $b\in D$ and then $(e_1-e_2)\beta^{-1}\in D-{0}=D^\times$.

## Lean

Formalized as [`NumberField.AdeleRing.DivisionAlgebra.Aux.X_meets_kernel'`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.DivisionAlgebra.Aux.X_meets_kernel').

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 199](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L199)
