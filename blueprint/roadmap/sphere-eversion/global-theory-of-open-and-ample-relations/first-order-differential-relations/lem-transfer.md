---
declaration: lemma
origin: cited
lean: OneJetSec.localize, isHolonomicAt_localize_iff, OneJetSec.localize_mem_iff
statement: formalized
proof: formalized
---

# transfer

In the situation of the previous definition, given a section $\mathcal{F} : M → J^1(M, N)$:

- $Ψ_{g, h}(\mathcal{F})$ is a smooth section of $J^1(X, Y)$.
- $\mathcal{F}$ is holonomic on $s ⊂ h(X) ∩ \operatorname{bs}\mathcal{F}⁻¹(g(Y))$ if and only if $Ψ_{g, h}(\mathcal{F})$ is holonomic on $h⁻¹(s)$.
- $\mathcal{F}$ is a formal solution of $\mathcal{R}$ on $h(X) ∩ \operatorname{bs}\mathcal{F}⁻¹(g(Y)$ if and only if $Ψ_{g, h}(\mathcal{F})$ is a formal solution of the induced relation $Ψ_{g, h}⁻¹\mathcal{R}$.

## Depends on

- [transfer_map](def-transfer-map.md)
- [holonomic_section](../preliminaries/def-holonomic-section.md)
- [formal_sol](def-formal-sol.md)

## Proof depends on

- [one_jet_section](../preliminaries/lem-one-jet-section.md)

## Proof

The first point is clear by composition. In order to prove the second point while keeping notations under control, we set $f(x) = g⁻¹ ∘ \operatorname{bs}\mathcal{F} ∘ h$. Using this notation $Ψ_{g, h}\mathcal{F}(x) = (x, f(x), (T_{f(x)}g)⁻¹ ∘ \mathcal{F}(h(x))_φ ∘ T_xh)$. We have

$$
\begin{aligned}
T_x f &= T_{\operatorname{bs}\mathcal{F} ∘ h(x)}(g⁻¹) ∘ T_{h(x)}\operatorname{bs}\mathcal{F} ∘ T_x h\\
&= \left(T_{f(x)}g\right)⁻¹ ∘ T_{h(x)}\operatorname{bs}\mathcal{F} ∘ T_x h
\end{aligned}
$$

hence $Ψ_{g, h}\mathcal{F}$ is holonomic at $x$ if and only if $\left(T_{f(x)}g\right)⁻¹ ∘ \mathcal{F}(h(x))_φ ∘ T_xh = \left(T_{f(x)}g\right)⁻¹ ∘ T_{h(x)}\operatorname{bs}\mathcal{F} ∘ T_x h$ and this is equivalent to $\mathcal{F}(h(x))_φ = T_{h(x)}\operatorname{bs}\mathcal{F}$ which is the holonomy condition for $\mathcal{F}$ at $h(x)$.

The third point is a direct consequence of the easy formula $ψ_{g, h} ∘ Ψ_{g, h}(\mathcal{F}) = F ∘ h$.

## Lean

Formalized as [`OneJetSec.localize`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OneJetSec.localize), [`isHolonomicAt_localize_iff`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/isHolonomicAt_localize_iff), [`OneJetSec.localize_mem_iff`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OneJetSec.localize_mem_iff).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 435](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L435)
