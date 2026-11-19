---
declaration: definition
origin: cited
lean: OpenSmoothEmbedding.transfer, OneJetSec.localize, RelMfld.localize
statement: formalized
---

# transfer_map

Given manifolds $M$, $X$, $N$ and $Y$ and smooth open embeddings $g : Y → N$ and $h : X → M$ we get a transfer map $ψ_{g, h} : J^1(X, Y) → J^1(M, N)$ defined by

$$
ψ_{g, h}(x, y, φ) = (h(x), g(y), T_yg ∘ φ ∘ (T_xh)⁻¹)
$$

and an operator on sections which sends $\mathcal{F} : M → J^1(M, N)$ to $Ψ_{g, h}\mathcal{F} : X → J^1(X, Y)$ defined when $\operatorname{bs}\mathcal{F}(h(X)) ⊂ g(Y)$ by

$$
Ψ_{g, h}\mathcal{F}(x) = (x, g⁻¹ ∘ \operatorname{bs}\mathcal{F} ∘ h(x), (T_{g⁻¹ ∘ \operatorname{bs}\mathcal{F} ∘ h(x)}g)⁻¹ ∘ \mathcal{F}(h(x))_φ ∘ T_xh).
$$

Given a relation $\mathcal{R} ⊂ J^1(M, N)$, the induced relation in $J^1(X, Y)$ is $ψ_{g, h}⁻¹\mathcal{R}$.

## Depends on

- [one_jet_space](../preliminaries/def-one-jet-space.md)

## Lean

Formalized as [`OpenSmoothEmbedding.transfer`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OpenSmoothEmbedding.transfer), [`OneJetSec.localize`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/OneJetSec.localize), [`RelMfld.localize`](https://leanprover-community.github.io/sphere-eversion/docs/find/#doc/RelMfld.localize).

## Sources

- [Sphere eversion blueprint: global_convex_integration.tex, line 412](https://github.com/leanprover-community/sphere-eversion/blob/33ab3d626854a0f0f04ed5772e3102d652e96475/blueprint/src/global_convex_integration.tex#L412)
