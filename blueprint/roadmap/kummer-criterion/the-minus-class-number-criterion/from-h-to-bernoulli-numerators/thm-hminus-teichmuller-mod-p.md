---
declaration: theorem
origin: cited
lean: KummerCriterion.hMinus_formula_teichmuller_mod_p
statement: formalized
proof: formalized
---

# hminus-teichmuller-mod-p

There exists $z\in\mathbb{Z}_p$ such that, inside $\mathbb{Q}_p$,

$$
h^-(K)
=
\prod_{\substack{j\lt p-2\\ j\ \mathrm{odd}}}
\left(-\frac12 B_{1,\omega^j}\right)
+ pz .
$$

## Depends on

- [hminus-formula](../the-relative-class-number-formula/thm-hminus-formula.md)
- [teichmuller](../characters-and-bernoulli-factors/def-teichmuller.md)

## Proof

Starting from [Theorem hminus-formula](../the-relative-class-number-formula/thm-hminus-formula.md), index the odd characters modulo $p$ as $\omega^j$ with $j$ odd, $1 \le j \le p-2$. The boundary exponent $j = p-2$ plays a special role: the combination of the prefactor $2p$ with the boundary factor $-\tfrac12 B_{1,\omega^{p-2}}$ is a $p$-adic integer congruent to $1$ modulo $p$, so it can be absorbed into the error term $pz$, leaving the product over odd $j < p-2$.

## Lean

Formalized as [`KummerCriterion.hMinus_formula_teichmuller_mod_p`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.hMinus_formula_teichmuller_mod_p).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 235](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L235)
