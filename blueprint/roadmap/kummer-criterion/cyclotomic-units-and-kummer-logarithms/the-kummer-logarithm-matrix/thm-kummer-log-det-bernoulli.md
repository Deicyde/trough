---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.kummerLogMatrix_det_ne_zero_iff_bernoulli_nonzero
statement: formalized
proof: formalized
---

# kummer-log-det-bernoulli

The Kummer logarithm determinant is nonzero precisely when no Bernoulli numerator in Kummer's range is divisible by $p$:

$$
\det M\ne0
\Longleftrightarrow
\forall j,\ 1\le j,\ 2j\le p-3,\quad
p\nmid\operatorname{num}(B_{2j}).
$$

## Depends on

- [kummer-det-bernoulli-factor](thm-kummer-det-bernoulli-factor.md)
- [bernoulliFactor-num](thm-bernoullifactor-num.md)

## Proof

[Theorem kummer-det-bernoulli-factor](thm-kummer-det-bernoulli-factor.md) reduces the determinant condition to the nonvanishing of every diagonal Bernoulli factor, and [Theorem bernoulliFactor-num](thm-bernoullifactor-num.md) translates each of those conditions into nondivisibility of the corresponding numerator. The finite index set of the matrix is identified with the classical range $1\le j$, $2j\le p-3$.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.kummerLogMatrix_det_ne_zero_iff_bernoulli_nonzero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.kummerLogMatrix_det_ne_zero_iff_bernoulli_nonzero).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 291](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L291)
