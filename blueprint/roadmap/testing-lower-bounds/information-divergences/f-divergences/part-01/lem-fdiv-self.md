---
declaration: lemma
origin: cited
lean: ProbabilityTheory.fDiv_self
statement: formalized
proof: formalized
---

# fDiv_self

If $f(1) = 0$ then $D_{f}(\mu, \mu) = 0$.

## Depends on

- [f-divergence](def-fdiv.md)

## Proof

$\frac{d \mu}{d \mu}(x) = 1$ almost everywhere and $f(1) = 0$.

## Lean

Formalized as [`ProbabilityTheory.fDiv_self`](https://RemyDegenne.github.io/testing-lower-bounds/docs/find/#doc/ProbabilityTheory.fDiv_self).

## Sources

- [Lower bounds for hypothesis testing blueprint: sections/f_divergence.tex, line 51](https://github.com/RemyDegenne/testing-lower-bounds/blob/6c303c98977be5a81e5a659823d83038d48a9a04/blueprint/src/sections/f_divergence.tex#L51)
