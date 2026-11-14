---
declaration: lemma
origin: cited
lean: ProbabilityTheory.renyiDiv_zero
statement: formalized
proof: formalized
---

# renyiDiv_zero

For $\mu$ a sigma-finite measure and $\nu$ a finite measure

$$
R_0(\mu, \nu) = - \log(\nu\{x \mid \frac{d \mu}{d \nu}(x) > 0\}) \: .
$$

## Depends on

- [Rényi divergence](def-renyi.md)

## Proof depends on

- [Hellinger $\alpha$-divergence](../hellinger-alpha-divergences/def-hellingeralpha.md)

## Lean

Formalized as [`ProbabilityTheory.renyiDiv_zero`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.renyiDiv_zero).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/renyi_divergence.tex, line 23](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/renyi_divergence.tex#L23)
