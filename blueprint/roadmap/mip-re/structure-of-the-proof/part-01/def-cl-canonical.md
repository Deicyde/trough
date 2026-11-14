---
declaration: definition
origin: cited
lean: MIPRE.CL.coordSub, MIPRE.CL.dotForm, MIPRE.CL.perp, MIPRE.CL.mem_perp, MIPRE.CL.tail, MIPRE.CL.dimTail, MIPRE.CL.pivots, MIPRE.CL.mem_pivots, MIPRE.CL.canonCompl, MIPRE.CL.canonLin, MIPRE.CL.lperp, MIPRE.CL.sub_canonLin_mem
statement: formalized
---

# Orthogonal and canonical complements

Let $V = \mathbb{F}^n$ with its standard basis. Two complements of a subspace $S \leq V$ are needed, and they are different.

The *orthogonal complement* $S^\perp = \{u : u \cdot v = 0 \text{ for all } v \in S\}$ for the standard dot product. Over a finite field it need *not* be a complement of $S$: $\mathrm{span}\{(1,1)\}$ over $\mathbb{F}_2$ is orthogonal to itself.

The *canonical complement*, which is one. Write $u_j = \dim\bigl(S \cap \mathrm{span}\{\hat e_i : i \geq j\}\bigr)$; the *pivot set* of $S$ is $J = \{j : u_{j+1} < u_j\}$, and the canonical complement of $S$ is $\mathrm{span}\{\hat e_j : j \notin J\}$. The *canonical linear map with kernel $S$* is the projector onto the canonical complement parallel to $S$. Finally, for a linear map $L$, $L^\perp$ is the canonical linear map with kernel $(\ker L)^\perp$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.CL.coordSub`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.coordSub), [`MIPRE.CL.dotForm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.dotForm), [`MIPRE.CL.perp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.perp), [`MIPRE.CL.mem_perp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.mem_perp), [`MIPRE.CL.tail`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.tail), [`MIPRE.CL.dimTail`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.dimTail), [`MIPRE.CL.pivots`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.pivots), [`MIPRE.CL.mem_pivots`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.mem_pivots), [`MIPRE.CL.canonCompl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.canonCompl), [`MIPRE.CL.canonLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.canonLin), [`MIPRE.CL.lperp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.lperp), [`MIPRE.CL.sub_canonLin_mem`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.sub_canonLin_mem).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 75](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L75)
