---
declaration: theorem
origin: cited
lean: ConNF.StrAction.freedomOfAction
statement: formalized
proof: formalized
---

# freedom of action for actions

Every coherent action approximates some allowable permutation.

## Depends on

Its statement uses no other node that has an article here.

## Proof depends on

- [exists_flexApprox](prop-exists-flexapprox.md)
- [approximates_of_flexApprox](prop-approximates-of-flexapprox.md)
- [freedom of action](../proving-freedom-of-action/thm-strapprox-foa.md)

## Proof

Let $\xi$ be a coherent $\beta$-action, and let $\psi$ be a flexible approximation for it, which exists by [Proposition exists_flexApprox](prop-exists-flexapprox.md). Then apply [freedom of action](../proving-freedom-of-action/thm-strapprox-foa.md) (freedom of action) to $\psi$ to obtain a $\beta$-allowable permutation $\rho$ that $\psi$ exactly approximates. Finally, appeal to [Proposition approximates_of_flexApprox](prop-approximates-of-flexapprox.md) to conclude that $\xi$ approximates $\rho$.

## Lean

Formalized as [`ConNF.StrAction.freedomOfAction`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrAction.freedomOfAction).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 665](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L665)
