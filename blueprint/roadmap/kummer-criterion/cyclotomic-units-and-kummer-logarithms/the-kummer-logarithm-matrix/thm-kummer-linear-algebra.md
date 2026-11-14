---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.exponents_modP_eq_zero_of_kummerLogMatrix_relation
statement: formalized
proof: formalized
---

# kummer-linear-algebra

If $\det M\ne0$ and $Me=0$, then $e = 0$ in $\mathbb{F}_p^{\,r}$.

## Depends on

- [concreteKummerLogMatrix](def-concretekummerlogmatrix.md)

## Proof

Over the field $\mathbb{F}_p$, a square matrix with nonzero determinant is invertible, so its kernel is trivial.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.exponents_modP_eq_zero_of_kummerLogMatrix_relation`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.exponents_modP_eq_zero_of_kummerLogMatrix_relation).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 345](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L345)
