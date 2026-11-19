---
declaration: theorem
origin: cited
lean: KummerCriterion.bernoulli_div_self_abs_lower_bound
statement: formalized
proof: formalized
---

# bernoulli-growth-bound

For every $k \ge 1$,

$$
\left|\frac{B_{2k}}{2k}\right|
\ \ge\ \frac{(2k-1)!}{2^{2k-1}\,\pi^{2k}}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Euler's formula gives

$$
\zeta(2k) \;=\; (-1)^{k+1}\,\frac{B_{2k}\,(2\pi)^{2k}}{2\,(2k)!},
$$

and $\zeta(2k) \ge 1$, so $|B_{2k}| \ge 2\,(2k)!/(2\pi)^{2k}$. Dividing by $2k$ yields the claim.

## Lean

Formalized as [`KummerCriterion.bernoulli_div_self_abs_lower_bound`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.bernoulli_div_self_abs_lower_bound).

## Sources

- [Kummer's criterion blueprint: subsections/irregular-primes-carlitz.tex, line 117](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/irregular-primes-carlitz.tex#L117)
