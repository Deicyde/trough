---
declaration: definition
origin: cited
lean: ConNF.Params
statement: formalized
---

# model parameters

A collection of *model parameters* is a tuple $(\lambda, {\lt _\lambda}, \kappa, \mu)$ such that

- ${<} = {\lt _\lambda}$ is a well-order on $\lambda$, and under this ordering, $\lambda$ has no maximal element (so $\operatorname{\mathsf{ot}}(\lambda)$ is a limit ordinal);

- $\#\kappa$ is uncountable and regular;

- $\#\mu$ is a strong limit, and satisfies

    $$
    \#\kappa < \#\mu;\quad \#\kappa \leq \operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu));\quad \operatorname{\mathsf{ot}}(\lambda) \leq \operatorname{\mathsf{ord}}(\operatorname{\mathsf{cof}}(\operatorname{\mathsf{ord}}(\#\mu)))
    $$

    so in particular, $\operatorname{\mathsf{ot}}(\lambda) \leq \operatorname{\mathsf{ord}}(\#\mu)$. Note that the inequalities in $\kappa$ are inequalities of cardinals; the inequality in $\lambda$ is an inequality of ordinals.

Given a collection of model parameters, we define

- canonical well-orders on $\kappa$ and $\mu$ such that $\operatorname{\mathsf{ot}}(\kappa) = \operatorname{\mathsf{ord}}(\#\kappa)$ and $\operatorname{\mathsf{ot}}(\mu) = \operatorname{\mathsf{ord}}(\#\mu)$; and
- a canonical left-cancellative additive monoid on $\kappa$, obtained by passing through the equivalence $\kappa \simeq \{ o : \mathsf{Ord} \mid o < \operatorname{\mathsf{ord}}(\#\kappa) \}$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ConNF.Params`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Params).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 20](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L20)
