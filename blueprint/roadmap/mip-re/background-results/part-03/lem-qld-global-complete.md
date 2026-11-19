---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.expandIdx, MIPRE.LIDT.expandIdx_apply_idx, MIPRE.LIDT.expandIdx_apply_of_not, MIPRE.LIDT.prod_pow_expandIdx, MIPRE.LIDT.LowIndDegPoly.blockPoly, MIPRE.LIDT.LowIndDegPoly.eval_blockPoly, MIPRE.QLD.isLinAB_of_isGood, MIPRE.QLD.notMem_xSet_iff, MIPRE.QLD.notMem_zSet_iff, MIPRE.QLD.not_depOutside_gA_of_isGood, MIPRE.QLD.not_depOutside_gB_of_isGood, MIPRE.QLD.gX, MIPRE.QLD.gZ, MIPRE.QLD.eval_gX, MIPRE.QLD.eval_gZ, MIPRE.QLD.pairOf, MIPRE.QLD.pairOf_of_isGood, MIPRE.QLD.pairMeas, MIPRE.QLD.pairMeas_mats, MIPRE.QLD.isPVM_pairMeas, MIPRE.QLD.evalMarg_pairMeas, MIPRE.QLD.inconsistency_map_eq
statement: formalized
proof: formalized
---

# Completing the pair measurement projectively

Relabel each good outcome $g = \alpha g_X(x) + \beta g_Z(z)$ of the global measurement by the pair $(g_X, g_Z)$ of polynomials of individual degree at most $d$ on $\mathbb{F}_q^m$, and every other outcome by the fixed pair $(0, 0)$. The result is a complete projective measurement of pairs, and the operator it assigns to $(0, 0)$ beyond the good outcomes with that pair is the paper's complement $R$, of weight at most $\delta_G$ by Lemma [Separating the two point variables](lem-qld-global-separate.md). Consequently each consistency estimate stated for the good outcomes holds for the completed measurement with its error increased by $\delta_G$. The Lean proves it for a global measurement in any bipartite model.

## Depends on

- [Separating the two point variables](lem-qld-global-separate.md)

## Proof

The relabelling is a map on outcomes, so the completed measurement is the coarse-graining of the global measurement by it; a coarse-graining of a projective measurement is projective, and complete because the original is. The pair of a good outcome is read off its two coefficient polynomials: $g_X$ is the coefficient of $\alpha$, which reads only the $x$ block, viewed as a polynomial in $m$ variables, and $g_Z$ the coefficient of $\beta$ on the $z$ block (`blockPoly`, whose defining property is that a coefficient vector supported on a block evaluates through that block). Nothing is lost: for a good outcome $g_X(x) = g_1(u)$ and $g_Z(z) = g_2(u)$ at every padded point $u$.

## Lean

Formalized as [`MIPRE.LIDT.expandIdx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.expandIdx), [`MIPRE.LIDT.expandIdx_apply_idx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.expandIdx_apply_idx), [`MIPRE.LIDT.expandIdx_apply_of_not`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.expandIdx_apply_of_not), [`MIPRE.LIDT.prod_pow_expandIdx`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.prod_pow_expandIdx), [`MIPRE.LIDT.LowIndDegPoly.blockPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.blockPoly), [`MIPRE.LIDT.LowIndDegPoly.eval_blockPoly`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.LowIndDegPoly.eval_blockPoly), [`MIPRE.QLD.isLinAB_of_isGood`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isLinAB_of_isGood), [`MIPRE.QLD.notMem_xSet_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.notMem_xSet_iff), [`MIPRE.QLD.notMem_zSet_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.notMem_zSet_iff), [`MIPRE.QLD.not_depOutside_gA_of_isGood`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.not_depOutside_gA_of_isGood), [`MIPRE.QLD.not_depOutside_gB_of_isGood`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.not_depOutside_gB_of_isGood), [`MIPRE.QLD.gX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.gX), [`MIPRE.QLD.gZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.gZ), [`MIPRE.QLD.eval_gX`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.eval_gX), [`MIPRE.QLD.eval_gZ`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.eval_gZ), [`MIPRE.QLD.pairOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.pairOf), [`MIPRE.QLD.pairOf_of_isGood`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.pairOf_of_isGood), [`MIPRE.QLD.pairMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.pairMeas), [`MIPRE.QLD.pairMeas_mats`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.pairMeas_mats), [`MIPRE.QLD.isPVM_pairMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVM_pairMeas), [`MIPRE.QLD.evalMarg_pairMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.evalMarg_pairMeas), [`MIPRE.QLD.inconsistency_map_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.inconsistency_map_eq).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 4426](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L4426)
