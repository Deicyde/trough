---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.LocalIsometry.intertwine, MIPRE.BipartiteModel.LocalIsometry.bornProb_withState, MIPRE.BipartiteModel.LocalIsometry.stateSqNorm_withState, MIPRE.BipartiteModel.LocalIsometry.bornProb_of_W_ψ, MIPRE.BipartiteModel.LocalIsometry.stateSqNorm_of_W_ψ, MIPRE.BipartiteModel.LocalIsometry.swap_stateSqNorm_of_W_ψ, MIPRE.BipartiteModel.LocalIsometry.xSqNorm_of_W_ψ, MIPRE.BipartiteModel.LocalIsometry.comp_W_ψ, MIPRE.BipartiteModel.LocalIsometry.isPVMIn_transportA, MIPRE.BipartiteModel.LocalIsometry.isPVMIn_transportB, MIPRE.BipartiteModel.LocalIsometry.intertwine_transportOpA, MIPRE.BipartiteModel.LocalIsometry.povmValue_transport, MIPRE.BipartiteModel.LocalIsometry.povmValue_pushforward
statement: formalized
proof: formalized
---

# Local isometries carry the Born rule

Let $W, \Phi$ be a local isometry from $M$ to $M'$. On the transported state $W\psi$, the Born probability of $(\Phi_A(a), \Phi_B(b))$ in $M'^{W\psi}$ is that of $(a, b)$ in $M$, and so is every squared state norm and cross-party deviation; when $W\psi$ is the state of $M'$ these hold in $M'$. A transported projective measurement is projective, intertwined with the original by $W$, so a strategy and its transport have the same value on the transported state; when both homomorphisms are unital and $W$ carries the state to the state, the images of a POVM strategy have its value in $M'$.

## Depends on

- [Local isometries of bipartite models](def-local-isometry.md)
- [Nonlocal game](../../foundations/part-01/def-game.md)

## Proof

Every quantity is a quadratic form of a product of represented operators on the state, and intertwining moves $W$ past each factor; $W$ preserves inner products. The transported effects are the images of orthogonal projections summing to $\Phi_A({I})$, completed by the orthogonal projection ${I} - \Phi_A({I})$, and the complement annihilates the image of $W$.

## Lean

Formalized as [`MIPRE.BipartiteModel.LocalIsometry.intertwine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.intertwine), [`MIPRE.BipartiteModel.LocalIsometry.bornProb_withState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.bornProb_withState), [`MIPRE.BipartiteModel.LocalIsometry.stateSqNorm_withState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.stateSqNorm_withState), [`MIPRE.BipartiteModel.LocalIsometry.bornProb_of_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.bornProb_of_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.stateSqNorm_of_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.stateSqNorm_of_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.swap_stateSqNorm_of_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.swap_stateSqNorm_of_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.xSqNorm_of_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.xSqNorm_of_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.comp_W_ψ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.comp_W_ψ), [`MIPRE.BipartiteModel.LocalIsometry.isPVMIn_transportA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.isPVMIn_transportA), [`MIPRE.BipartiteModel.LocalIsometry.isPVMIn_transportB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.isPVMIn_transportB), [`MIPRE.BipartiteModel.LocalIsometry.intertwine_transportOpA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.intertwine_transportOpA), [`MIPRE.BipartiteModel.LocalIsometry.povmValue_transport`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.povmValue_transport), [`MIPRE.BipartiteModel.LocalIsometry.povmValue_pushforward`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.LocalIsometry.povmValue_pushforward).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1819](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1819)
