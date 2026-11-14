---
declaration: definition
origin: cited
lean: MIPRE.Tailored.Halting.SearchSpec, MIPRE.Tailored.Halting.vof, MIPRE.Tailored.Halting.C
statement: formalized
---

# The search program's specification

Let $C = \max\{C_0, 2\}$. A program $\mathcal{S}'$ *meets the search specification* when, on the description of every $\lambda$-bounded tailored verifier $(\mathcal{S}^\lambda, \mathcal{L}^\lambda, \mathcal{P})$, it halts exactly when $\mathrm{val}^*$ of that verifier at the level $C$ exceeds $\frac12$.

## Depends on

- [Tailored gap compression, value form; II:1852](def-tailored-compression.md)

## Lean

Formalized as [`MIPRE.Tailored.Halting.SearchSpec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.SearchSpec), [`MIPRE.Tailored.Halting.vof`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.vof), [`MIPRE.Tailored.Halting.C`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Halting.C).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 659](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L659)
