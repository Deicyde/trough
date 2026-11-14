---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.bernoulliFactor_ne_zero_iff_not_dvd_bernoulli_num
statement: formalized
proof: formalized
---

# bernoulliFactor-num

The diagonal Bernoulli factor attached to $j$ is nonzero in $\mathbb{F}_p$ exactly when

$$
p\nmid\operatorname{num}(B_{2j}).
$$

## Depends on

- [padic-bernoulli-factor](../../the-minus-class-number-criterion/characters-and-bernoulli-factors/lem-padic-bernoulli-factor.md)

## Proof

The factor is the reduction modulo $p$ of a $p$-integral rational expression which is a $p$-adic unit multiple of $B_{2j}/2j$; in the range $2j \le p-3$, both $2j$ and the denominator of $B_{2j}$ are prime to $p$ ([Lemma padic-bernoulli-factor](../../the-minus-class-number-criterion/characters-and-bernoulli-factors/lem-padic-bernoulli-factor.md)). So the reduction vanishes exactly when $p$ divides the numerator of $B_{2j}$.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.bernoulliFactor_ne_zero_iff_not_dvd_bernoulli_num`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.bernoulliFactor_ne_zero_iff_not_dvd_bernoulli_num).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 274](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L274)
