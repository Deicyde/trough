---
declaration: theorem
origin: cited
lean: InfModel.Finite.two_variable_laws
statement: formalized
proof: formalized
---

# Austin's finite model theorem

Any law with at most two variables has a non-trivial finite model.

## Depends on

- [Models](../../basic-theory-of-magmas/models-def.md)

## Proof

If neither side of the law is a single variable then the zero law $x \diamond y = 0$ will work, so one can assume the law takes the form $x = f(x,y)$. Consider a finite field $F$ with the operation $x \diamond y := ax+by$ for some coefficients $a,b \in F$. Then the law becomes a pair of equations $P(a,b)=0$, $Q(a,b)=1$ in the coefficients for some polynomials $P,Q$ with integer coefficients, which one can verify to not divide each other (they have the same degree, and do not have the same set of non-zero monomials). From Bezout's theorem, this equation has a solution in some field, and hence by the Lefschetz principle it has a solution in a finite field.

## Lean

Formalized as [`InfModel.Finite.two_variable_laws`](https://teorth.github.io/equational_theories/docs/find/#doc/InfModel.Finite.two_variable_laws).

## Sources

- [Equational Theories blueprint: chapter/infinite_models.tex, line 81](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_models.tex#L81)
