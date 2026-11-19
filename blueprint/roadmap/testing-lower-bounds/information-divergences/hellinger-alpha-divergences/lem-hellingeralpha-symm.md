---
declaration: lemma
origin: cited
lean: ProbabilityTheory.hellingerDiv_symm
statement: formalized
proof: formalized
---

# hellingerAlpha_symm

For $\alpha \in (0, 1)$ and finite measures $\mu, \nu$, $(1 - \alpha) \operatorname{H}_\alpha(\mu, \nu) = \alpha \operatorname{H}_{1 - \alpha}(\nu, \mu)$.

## Depends on

- [Hellinger $\alpha$-divergence](def-hellingeralpha.md)

## Proof depends on

- [integral_rpow_rnDeriv_symm](lem-integral-rpow-rnderiv-symm.md)

## Proof

Use Lemma [integral_rpow_rnDeriv_symm](lem-integral-rpow-rnderiv-symm.md).

## Lean

Formalized as [`ProbabilityTheory.hellingerDiv_symm`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.hellingerDiv_symm).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/hellinger_alpha.tex, line 79](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/hellinger_alpha.tex#L79)
