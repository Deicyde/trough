---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_eq_zero_iff
statement: formalized
proof: formalized
---

# fDiv_eq_zero_iff

Let $\mu, \nu$ be two finite measures. Assume that $f$ is strictly convex on $(0, +\infty)$ and $f(1) = 0$. Then $D_f(\mu, \nu) = 0$ if and only if $\mu = \nu$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof depends on

- [fDiv_self](lem-fdiv-self.md)

## Proof

If $\mu = \nu$ then $D_f(\mu, \nu) = 0$ by Lemma [fDiv_self](lem-fdiv-self.md). For the other direction, since $f \ge 0$ is strictly convex with $f(1) = 0$, $f(x) = 0$ only for $x = 1$, and $f'(\infty) > 0$ (since $f(2) \le 2 f'(\infty)$ and $f(2) > 0$). $D_f(\mu, \nu) = 0$ then implies $\mu_{\perp \nu}(\mathcal X) = 0$, hence $\mu \ll \nu$, and $f(\frac{d\mu}{d\nu}) = 0$ $\nu$-almost everywhere, hence $\frac{d\mu}{d\nu} = 1$ $\nu$-almost everywhere.

## Lean

Formalized as [`ProbabilityTheory.fDiv_eq_zero_iff`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_eq_zero_iff).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 64](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L64)
