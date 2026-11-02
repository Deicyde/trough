---
declaration: lemma
origin: cited
lean: NumberField.AdeleRing.DivisionAlgebra.Aux.antidiag_mem_C
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.DivisionAlgebra.Aux.antidiag\_mem\_C

For every $\beta\in D_{\mathbb{A}}^{(1)}$, there exists $b\in D^\times$ and $\nu\in D_{\mathbb{A}}^{(1)}$ such that $\beta=b\nu$ and $(\nu,\nu^{-1})\in C.$

## Depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.C](numberfield-adelering-divisionalgebra-aux-c.md)

## Proof depends on

- [NumberField.AdeleRing.DivisionAlgebra.Aux.E](numberfield-adelering-divisionalgebra-aux-e.md)
- [NumberField.AdeleRing.DivisionAlgebra.Aux.X\_meets\_kernel](numberfield-adelering-divisionalgebra-aux-x-meet.md)
- [NumberField.AdeleRing.DivisionAlgebra.Aux.X\_meets\_kernel'](numberfield-adelering-divisionalgebra-aux-x-meet-2.md)

## Proof

By lemma [NumberField.AdeleRing.DivisionAlgebra.Aux.X\_meets\_kernel](numberfield-adelering-divisionalgebra-aux-x-meet.md), $\beta X\cap D^\times\not=\emptyset$, and lemma [NumberField.AdeleRing.DivisionAlgebra.Aux.X\_meets\_kernel'](numberfield-adelering-divisionalgebra-aux-x-meet-2.md), $X\beta^{-1}\cap D^\times\not=\emptyset$, so we can write $\beta x_1=b_1$ and $x_2\beta^{-1}=b_2$ with $b_i\in D^\times$ and $x_i\in X$. Note that $\beta\in D_{\mathbb{A}}^{(1)}$ and $b_i\in D^{\times}\subseteq D_{\mathbb{A}}^{(1)}$ by corollary [NumberField.AdeleRing.units\_mem\_ringHaarCharacter\_ker](../../miniproject-haar-characters/adeles/numberfield-adelering-units-mem-ringhaarcharacte.md), so $x_i\in D_{\mathbb{A}}^{(1)}$ as well. In particular $x_i\in D_{\mathbb{A}}^\times$ so $x_1^{-1}$ makes sense.

Multiplying the equations defining the $x_i$ and $b_i$ we deduce that $x_2x_1=b_2b_1\in Y\cap D^\times=T$ (recall that $Y=X.X$ and $T=Y\cap D^\times$ is finite); call this element $t$. Then $x_1^{-1}=t^{-1}x_2\in T^{-1}.X$, and $x_1\in X$, so if we set $\nu=x_1^{-1}\in D_{\mathbb{A}}^{(1)}$ and $b=b_1\in D^\times$ then we have $\beta=b\nu$ and $(\nu,\nu^{-1})\in C := (T^{-1}.X)\times X$. We are done!

## Lean

Formalized as [`NumberField.AdeleRing.DivisionAlgebra.Aux.antidiag_mem_C`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.DivisionAlgebra.Aux.antidiag_mem_C).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 268](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L268)
