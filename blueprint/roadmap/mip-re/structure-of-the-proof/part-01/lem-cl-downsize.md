---
declaration: lemma
origin: cited
lean: MIPRE.CL.downsizeEquiv, MIPRE.CL.CLFun.downsize, MIPRE.CL.CLFun.eval_downsize, MIPRE.CL.CLFun.eval_truncate_downsize, MIPRE.CL.CLFun.factorOfPrefix_downsize, MIPRE.CL.CLFun.mapOfPrefix_downsize, MIPRE.CL.CLFun.ExactlyOn.downsize, MIPRE.CL.IsCLFun.downsize, MIPRE.CL.clDist_downsize, MIPRE.CL.CLFun.reindex, MIPRE.CL.IsCLFun.reindex
statement: formalized
proof: formalized
---

# Downsizing

Let $\mathbb{F}$ be a finite field, $\mathbb{K}$ a subfield, and $e_1, \ldots, e_t$ a basis of $\mathbb{F}$ over $\mathbb{K}$; let $\kappa : \mathbb{F}^n \to \mathbb{K}^{nt}$ be the $\mathbb{K}$-linear bijection reading off the coordinates of each entry in this basis. If $L$ is an $\ell$-level CL function on $V = \mathbb{F}^n$, then $L^\kappa = \kappa \circ L \circ \kappa^{-1}$ is an $\ell$-level CL function on $\mathbb{K}^{nt}$, whose decomposition data are the downsized data of $L$: for $j \in \{1, \ldots, \ell\}$ and $u \in L_{\lt j}(V)$,

$$
L^\kappa_{\le j} = \kappa \circ L_{\le j} \circ \kappa^{-1}, \qquad
V^\kappa_{j,\, \kappa(u)} = \kappa(V_{j,u}), \qquad
L^\kappa_{j,\, \kappa(u)} = \kappa \circ L_{j,u} \circ \kappa^{-1},
$$

where $\kappa(V_{j,u})$ is the register subspace of $\mathbb{K}^{nt}$ on the coordinates $(i, k)$ with $i$ a coordinate of $V_{j,u}$. Exactness is preserved, and the CL distribution of $(L^\kappa, R^\kappa)$ is the image under $\kappa$ of that of $(L, R)$.

## Depends on

- [Conditionally linear function](def-cl-function.md)
- [Structure of a CL function](lem-cl-structure.md)

## Proof

`lem:cl-downsize` and `lem:downsize-cl-dist` of `linear.tex`, by induction on the level; the one fact used is that $\kappa$ commutes with the coordinate projections onto register subspaces (`lem:downsize_subspace` of `preliminaries.tex`, in the register case).

## Lean

Formalized as [`MIPRE.CL.downsizeEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.downsizeEquiv), [`MIPRE.CL.CLFun.downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.downsize), [`MIPRE.CL.CLFun.eval_downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_downsize), [`MIPRE.CL.CLFun.eval_truncate_downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_truncate_downsize), [`MIPRE.CL.CLFun.factorOfPrefix_downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.factorOfPrefix_downsize), [`MIPRE.CL.CLFun.mapOfPrefix_downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.mapOfPrefix_downsize), [`MIPRE.CL.CLFun.ExactlyOn.downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ExactlyOn.downsize), [`MIPRE.CL.IsCLFun.downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.downsize), [`MIPRE.CL.clDist_downsize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.clDist_downsize), [`MIPRE.CL.CLFun.reindex`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.reindex), [`MIPRE.CL.IsCLFun.reindex`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.reindex).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 243](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L243)
