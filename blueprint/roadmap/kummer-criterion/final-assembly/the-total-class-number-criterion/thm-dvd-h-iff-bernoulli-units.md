---
declaration: theorem
origin: cited
lean: KummerCriterion.dvd_h_iff_exists_dvd_bernoulli_units
statement: formalized
proof: formalized
---

# dvd-h-iff-bernoulli-units

For an odd prime $p$ and the $p$th cyclotomic field $K$,

$$
p\mid h(K)
\quad\Longleftrightarrow\quad
\exists k,\ 1\le k,\ 2k\le p-3,\quad
p\mid\operatorname{num}(B_{2k}).
$$

## Depends on

- [dvd-h-iff-dvd-hminus-from-plus-to-minus](../../class-numbers-of-the-cyclotomic-cm-field/the-relative-class-number/thm-dvd-h-iff-dvd-hminus-from-plus-to-minus.md)
- [hplus-to-hminus-units](../the-implication-from-h-to-h/thm-hplus-to-hminus-units.md)
- [hminus-bernoulli-final](../../the-minus-class-number-criterion/from-h-to-bernoulli-numerators/thm-hminus-bernoulli-final.md)

## Proof

The implication $p\mid h^+(K)\Rightarrow p\mid h^-(K)$ is [Theorem hplus-to-hminus-units](../the-implication-from-h-to-h/thm-hplus-to-hminus-units.md); feeding it to [Theorem dvd-h-iff-dvd-hminus-from-plus-to-minus](../../class-numbers-of-the-cyclotomic-cm-field/the-relative-class-number/thm-dvd-h-iff-dvd-hminus-from-plus-to-minus.md) converts $p\mid h(K)$ into $p\mid h^-(K)$. The minus class-number criterion ([Theorem hminus-bernoulli-final](../../the-minus-class-number-criterion/from-h-to-bernoulli-numerators/thm-hminus-bernoulli-final.md)) rewrites the latter as the existence of a Bernoulli numerator in Kummer's range divisible by $p$.

## Lean

Formalized as [`KummerCriterion.dvd_h_iff_exists_dvd_bernoulli_units`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.dvd_h_iff_exists_dvd_bernoulli_units).

## Sources

- [Kummer's criterion blueprint: subsections/final.tex, line 70](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/final.tex#L70)
