---
declaration: theorem
origin: cited
lean: KummerCriterion.not_dvd_cyclotomicUnitIndex_of_bernoulli_nonzero
statement: formalized
proof: formalized
---

# bernoulli-nonzero-index

Let $p$ be an odd prime. Suppose that

$$
\forall j,\ 1\le j,\ 2j\le p-3,\quad
p\nmid\operatorname{num}(B_{2j}).
$$

Then

$$
p\nmid[(\mathcal O_{K^+})^\times:C^+].
$$

## Depends on

- [kummer-log-det-bernoulli](../../cyclotomic-units-and-kummer-logarithms/the-kummer-logarithm-matrix/thm-kummer-log-det-bernoulli.md)
- [kummer-log-det-saturation](../../cyclotomic-units-and-kummer-logarithms/the-kummer-logarithm-matrix/thm-kummer-log-det-saturation.md)
- [not-dvd-index-of-pSaturated](../../cyclotomic-units-and-kummer-logarithms/exact-p-saturation/thm-not-dvd-index-of-psaturated.md)

## Proof

If $p=3$, Kummer's range is empty, $K^+ = \mathbb{Q}$, the group $C^+$ is the full unit group $\{\pm1\}$, and the index is $1$. For $p\ge5$, [Theorem kummer-log-det-bernoulli](../../cyclotomic-units-and-kummer-logarithms/the-kummer-logarithm-matrix/thm-kummer-log-det-bernoulli.md) identifies the Bernoulli nonvanishing hypothesis with the nonvanishing of the Kummer logarithm determinant. By [Theorem kummer-log-det-saturation](../../cyclotomic-units-and-kummer-logarithms/the-kummer-logarithm-matrix/thm-kummer-log-det-saturation.md), the subgroup $C^+$ is then $p$-saturated in the full unit group, and [Theorem not-dvd-index-of-pSaturated](../../cyclotomic-units-and-kummer-logarithms/exact-p-saturation/thm-not-dvd-index-of-psaturated.md) concludes that the index is prime to $p$.

## Lean

Formalized as [`KummerCriterion.not_dvd_cyclotomicUnitIndex_of_bernoulli_nonzero`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.not_dvd_cyclotomicUnitIndex_of_bernoulli_nonzero).

## Sources

- [Kummer's criterion blueprint: subsections/final.tex, line 13](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/final.tex#L13)
