---
declaration: proposition
origin: cited
lean: ConNF.StrApprox.addFlexible
statement: formalized
proof: formalized
---

# adding flexible litters

Let $\psi$ be a coherent $\beta$-approximation, and let $L$ be $A$-flexible. Then there is a coherent extension $\chi \geq \psi$ with $L \in \operatorname{\mathsf{coim}} \chi_A^{\mathcal L}$.

## Depends on

- [Inflexible](../structural-approximations/def-inflexible.md)
- [StrApprox](../structural-approximations/def-strapprox.md)

## Proof depends on

- [adding orbits coherently](../structural-approximations/prop-strapprox-addorbit.md)

## Proof

Define $L' : \mathbb Z \to {\mathcal L}$ by $L'(n) = L$, then appeal to [adding orbits coherently](../structural-approximations/prop-strapprox-addorbit.md) to obtain $\chi \geq \psi$. All we must do is check that $\psi$ is coherent at $(L, L)$, which is trivial.

## Lean

Formalized as [`ConNF.StrApprox.addFlexible`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.addFlexible).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 307](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L307)
