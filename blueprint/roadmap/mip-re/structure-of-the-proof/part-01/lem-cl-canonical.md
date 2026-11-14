---
declaration: lemma
origin: cited
lean: MIPRE.CL.finrank_perp, MIPRE.CL.perp_perp, MIPRE.CL.isCompl_canonCompl, MIPRE.CL.card_pivots, MIPRE.CL.ker_canonLin, MIPRE.CL.range_canonLin, MIPRE.CL.ker_lperp
statement: formalized
proof: formalized
---

# The two complements

With the notation of Definition [Orthogonal and canonical complements](def-cl-canonical.md):

1. ($\texttt{lem:perp\_perp}$) $\dim S + \dim S^\perp = \dim V$ and $(S^\perp)^\perp = S$, over every field;
2. ($\texttt{lem:canonical-complement}$) $S$ and its canonical complement are complementary subspaces, and the pivot set has $\dim S$ elements;
3. the canonical linear map with kernel $S$ has kernel exactly $S$ and range the canonical complement;
4. ($\texttt{lem:L\_perp\_perp}$) $\ker(L^\perp) = (\ker L)^\perp$.

## Depends on

- [Orthogonal and canonical complements](def-cl-canonical.md)

## Proof

Item 1 is Mathlib's, for a nondegenerate reflexive bilinear form, once the dot product is shown to be one. For item 2, let $0 \neq x \in S$ lie in the canonical complement and let $j$ be the least index with $x_j \neq 0$; then $x$ witnesses $S \cap \mathrm{span}\{\hat e_i : i \geq j+1\} < S \cap \mathrm{span}\{\hat e_i : i \geq j\}$, so $j$ is a pivot, so $x_j = 0$ — a contradiction. The pivot count is an induction on $j$ along $u_j + \#\{\text{pivots} < j\} = \dim S$, using that $u_j \leq u_{j+1} + 1$ because the $j$-th coordinate is a linear functional on $S \cap \mathrm{span}\{\hat e_i : i \geq j\}$ with kernel the next term. Codisjointness then follows by counting dimensions, the complement having $n - \#J$. Items 3 and 4 are then Mathlib's projector along a direct sum decomposition.

## Lean

Formalized as [`MIPRE.CL.finrank_perp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.finrank_perp), [`MIPRE.CL.perp_perp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.perp_perp), [`MIPRE.CL.isCompl_canonCompl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.isCompl_canonCompl), [`MIPRE.CL.card_pivots`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.card_pivots), [`MIPRE.CL.ker_canonLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.ker_canonLin), [`MIPRE.CL.range_canonLin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.range_canonLin), [`MIPRE.CL.ker_lperp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.ker_lperp).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 117](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L117)
