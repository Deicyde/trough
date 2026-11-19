---
declaration: theorem
origin: cited
lean: KummerCriterion.p_dvd_hMinus_iff_p_dvd_some_bernoulli
statement: formalized
proof: formalized
---

# hminus-bernoulli-final

For $p$ odd,

$$
p\mid h^-(K)
\quad\Longleftrightarrow\quad
\exists k,\ 1\le k,\ 2k\le p-3,\quad
p\mid\operatorname{num}(B_{2k}).
$$

## Depends on

- [hminus-bernoulli-mod-p](thm-hminus-bernoulli-mod-p.md)
- [padic-bernoulli-factor](../characters-and-bernoulli-factors/lem-padic-bernoulli-factor.md)
- [odd-index-to-k](lem-odd-index-to-k.md)

## Proof

By [Theorem hminus-bernoulli-mod-p](thm-hminus-bernoulli-mod-p.md), $h^-$ is congruent modulo $p$ to the finite product of the $p$-adic integers $-\tfrac12 B_{j+1}/(j+1)$ over odd $j < p-2$. The factor $-\tfrac12$ and the denominator $j+1$ are $p$-adic units in this range, so by [Lemma padic-bernoulli-factor](../characters-and-bernoulli-factors/lem-padic-bernoulli-factor.md) each factor is a non-unit exactly when $p$ divides $\operatorname{num}(B_{j+1})$. A product of $p$-adic integers lies in $p\mathbb{Z}_p$ exactly when one of the factors does, so $p \mid h^-$ holds precisely when some numerator in the range is divisible by $p$. Finally [Lemma odd-index-to-k](lem-odd-index-to-k.md) converts the odd index $j$ into the classical range $1\le k$, $2k\le p-3$ with $2k = j+1$.

## Lean

Formalized as [`KummerCriterion.p_dvd_hMinus_iff_p_dvd_some_bernoulli`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.p_dvd_hMinus_iff_p_dvd_some_bernoulli).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 295](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L295)
