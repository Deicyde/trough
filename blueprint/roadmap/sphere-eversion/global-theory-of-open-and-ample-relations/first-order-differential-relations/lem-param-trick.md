---
declaration: lemma
origin: cited
lean: FamilyOneJetSec.isHolonomicAt_uncurry, FamilyOneJetSec.uncurry_mem_relativize
statement: formalized
proof: formalized
---

# param_trick

In the above setup, we have:

- $\bar F$ is holonomic at $(x, p)$ if and only if $F_p$ is holonomic at $x$.
- $F$ is a family of formal solutions of some $\mathcal{R} ⊂ J^1(X, Y)$ if and only if $\bar F$ is a formal solution of $\mathcal{R}^P := Ψ^{-1}(\mathcal{R})$.

## Depends on

- [holonomic_section](../preliminaries/def-holonomic-section.md)
- [formal_sol](def-formal-sol.md)

## Proof

For the first part, the derivative of $\bar F$ is $∂f/∂x(x, p) ⊕ ∂f/∂p(x, p)$, which is equal to $\bar F_φ$ iff $∂f/∂x(x, p) = f_φ$.

The second part follows from $Ψ ∘ \bar F(x,p)=F_p(x)$.

## Lean

Formalized as [`FamilyOneJetSec.isHolonomicAt_uncurry`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/FamilyOneJetSec.isHolonomicAt_uncurry), [`FamilyOneJetSec.uncurry_mem_relativize`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/FamilyOneJetSec.uncurry_mem_relativize).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 496](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L496)
