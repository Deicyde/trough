---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredGapCompression
statement: formalized
---

# Tailored gap compression, value form; II:1852

A *tailored gap compression* at level $\ell$ is a polynomial-time procedure that maps a tailored verifier and $\lambda$ to a tailored verifier whose sampler and answer-length calculator depend on $\lambda$ only, the calculator halting on every question of the sampler, with running times, dimension and lengths at most a polynomial in $n + \lambda$, such that for every $\lambda$-bounded input and every $n \geq C_0$: a perfect ZPC strategy for $\mathsf{V}_{2^n}$ gives one for $\mathsf{V}'_n$; and $\mathrm{val}^*(\mathsf{V}_{2^n}) \leq \frac12$ implies $\mathrm{val}^*(\mathsf{V}'_n) \leq \frac12$.

## Depends on

- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredGapCompression`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGapCompression).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 561](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L561)
