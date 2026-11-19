---
declaration: definition
origin: cited
lean: ConNF.InflexiblePath
statement: formalized
---

# inflexible path

Let $\alpha$ be a proper type index. Suppose that we have model data for all type indices $\beta \leq \alpha$ and position functions for $\mathsf{Tang}_\beta$ for all $\beta < \alpha$. For any type index $\beta \leq \alpha$, a *inflexible $\beta$-path* is a tuple $I = (\gamma, \delta, \varepsilon, A)$ where $\delta, \varepsilon < \gamma$ are distinct, the index $\varepsilon$ is proper, and $A : \beta \rightsquigarrow \gamma$. We will write $\gamma_I, \delta_I, \varepsilon_I, A_I$ for its fields. Inflexible paths have a coderivative operation, given by $(\gamma, \delta, \varepsilon, A)^B = (\gamma, \delta, \varepsilon, A^B)$.

## Depends on

- [fuzz maps](prop-fuzz.md)

## Lean

Formalized as [`ConNF.InflexiblePath`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.InflexiblePath).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 394](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L394)
