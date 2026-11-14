---
declaration: theorem
origin: cited
lean: KummerCriterion.bernoulli_nonzero_of_not_dvd_hMinus
statement: formalized
proof: formalized
---

# hminus-nondiv-to-bernoulli-nondiv

If $p\nmid h^-(K)$, then for every $k$ with $1\le k$ and $2k\le p-3$,

$$
p\nmid\operatorname{num}(B_{2k}).
$$

## Depends on

- [hminus-bernoulli-final](thm-hminus-bernoulli-final.md)

## Proof

Contrapositive of one direction of [Theorem hminus-bernoulli-final](thm-hminus-bernoulli-final.md): a numerator divisible by $p$ in the range would force $p\mid h^-(K)$.

## Lean

Formalized as [`KummerCriterion.bernoulli_nonzero_of_not_dvd_hMinus`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.bernoulli_nonzero_of_not_dvd_hMinus).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 320](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L320)
