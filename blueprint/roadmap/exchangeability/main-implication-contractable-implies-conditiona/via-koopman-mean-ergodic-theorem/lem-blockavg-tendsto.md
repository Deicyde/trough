---
declaration: lemma
origin: cited
lean: Exchangeability.DeFinetti.ViaKoopman.blockAvg_tendsto_condExp
statement: formalized
---

# Block averages converge in $L^1$

For a shift-invariant measure, block averages converge *in $L^1$* to the conditional expectation given the shift-invariant $\sigma$-algebra: $\int |A_{m,n,k}(f) - \mathbb{E}[f \circ \pi_0 \mid \mathcal{I}]| \, d\mu \to 0$ as $n \to \infty$.

## Depends on

- [Block average](def-blockavg.md)
- [Birkhoff averages converge to condexp](thm-birkhoff-condexp.md)

## Lean

Stated as [`Exchangeability.DeFinetti.ViaKoopman.blockAvg_tendsto_condExp`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaKoopman.blockAvg_tendsto_condExp); the blueprint marks no proof of it as formalized.

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 460](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L460)
