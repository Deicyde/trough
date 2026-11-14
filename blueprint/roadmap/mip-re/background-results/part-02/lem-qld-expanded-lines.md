---
declaration: lemma
origin: cited
lean: MIPRE.QLD.lineCoeffs, MIPRE.QLD.eval_lineCoeffs, MIPRE.QLD.dotF_indVec, MIPRE.QLD.padLine, MIPRE.QLD.linePoly_eval_eq_range, MIPRE.QLD.eval_padLine, MIPRE.QLD.rdLine, MIPRE.QLD.synLinePOVM, MIPRE.QLD.synLinePOVM_map_eval, MIPRE.QLD.lineAnsPOVM, MIPRE.QLD.hatLinePOVM, MIPRE.QLD.isPVM_hatLinePOVM, MIPRE.QLD.hatLinePOVM_map_eval, MIPRE.QLD.sum_xSqNorm_hatLinePOVM_le, MIPRE.QLD.hatLinePOVM_consistency, MIPRE.QLD.Content.omega_pt, MIPRE.QLD.sum_xSqNorm_hatLine_point_le, MIPRE.QLD.rep_add_lineParam_smul, MIPRE.QLD.abaseOf, MIPRE.QLD.ddirOf, MIPRE.QLD.dbaseOf, MIPRE.QLD.d_le_mul, MIPRE.QLD.m_le_mul, MIPRE.QLD.hsub_aline, MIPRE.QLD.hsub_dline, MIPRE.QLD.hatLinePOVM_point_consistency, MIPRE.QLD.expanded_lines_aline, MIPRE.QLD.expanded_lines_dline, MIPRE.QLD.isPVM_synPOVM, MIPRE.QLD.kronIn, MIPRE.QLD.kronIn_op, MIPRE.QLD.isPVMIn_kronIn, MIPRE.QLD.kronIn_congr, MIPRE.QLD.kronIn_map, MIPRE.QLD.isPVM_synLinePOVM
statement: formalized
proof: formalized
---

# Expanded line measurements

Let $d \geq 1$ and let $|\hat\psi\rangle$ be as in Lemma [Expanded point observables commute](lem-qld-expanded-commutation.md). For each $W \in \{X, Z\}$ and each line type — axis-parallel or diagonal — write $\ell$ for the line the verifier's content presents on the $W$ side, and let

$$
\widehat{M}^{(\mathtt{Line}, W), \ell}_f
\;=\; \sum_{f' + f'' = f} M^{(\mathtt{Line}, W), \ell}_{f'} \otimes \tau^{W, \ell}_{f''}
$$

be the convolution of the strategy's line measurement with the ancilla measurement that reports the restriction to $\ell$ of the low-degree encoding of its outcome (Definition [Restriction to a line](../../structure-of-the-proof/part-07/def-line-restriction.md)), the outcomes being the polynomials of degree at most $md$ on $\ell$. Then, on average over the verifier's content — which is the line–point distribution, the line and the point being read off the same sample:

1. (**Self-consistency**) $\widehat{M}^{(\mathtt{Line}, W), \ell}_f \otimes {I} \;\simeq_{172\varepsilon}\; {I} \otimes \widehat{M}^{(\mathtt{Line}, W), \ell}_f$;
2. (**Consistency with the expanded point measurements**) $\widehat{M}^{(\mathtt{Point}, W), u}_a \otimes {I} \;\simeq_{172\varepsilon}\; {I} \otimes \widehat{M}^{(\mathtt{Line}, W), \ell}_{[\mathrm{eval}_u(\cdot) = a]}$, where $u$ is the point of the same content and $\mathrm{eval}_u$ evaluates a polynomial on $\ell$ at the parameter of $u$.

Moreover $\{\widehat{M}^{(\mathtt{Line}, W), \ell}_f\}_f$ is *projective* whenever the strategy's own line measurement is, as it is for a strategy of a bipartite model (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)). The Lean proves the two items for a strategy in any bipartite model, with no projectivity, on its register model (Definition [The register model](../../downstream-results/part-03/def-register-model.md)); the statement above is its tensor-product instance.

## Depends on

- [Win implications](lem-qld-win.md)
- [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)
- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)
- [Restriction to a line](../../structure-of-the-proof/part-07/def-line-restriction.md)
- [Seeded CL low individual degree test](../part-01/def-lidt-cl.md)
- [The order of a matrix algebra over an ordered $*$-ring](../../downstream-results/part-03/def-block-order.md)

## Proof depends on

- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)
- [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md)
- [The ancilla extension](../../downstream-results/part-02/lem-ancilla-extension.md)

## Proof

Everything is exact except the strategy's own error, and the two items come out of the same three inputs as Lemma [Expanded point measurements are self-consistent](lem-qld-expanded-consistency.md).

Projectivity is two closure properties and no computation: a product of projective measurements is projective, and so is any coarse-graining of one — because the elements of a projective measurement are mutually orthogonal, a sum of them over a level set is idempotent. The convolution is a coarse-graining of a product, so it is projective.

For item 1, the agreement probability of the product measurement on the expanded state factorizes (Definition [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)); the ancilla factor is *exactly one*, the level-set projectors of the basis measurement being perfectly self-consistent across the two halves of $|\textsc{EPR}_q\rangle^{\otimes M}$ (Definition [The maximally entangled state of the Weyl system](../../foundations/part-02/def-weyl-epr.md)); the convolution can only increase agreement; and what remains is item 1 of Lemma [Win implications](lem-qld-win.md) at the line type's self-loop. One conversion from agreement to distance gives $2 \cdot 86\varepsilon$.

For item 2 the ancilla contributes an identity rather than an estimate: relabelling a line outcome of the ancilla by its value at the point *is* the ancilla's point measurement at that point. Both are coarse-grainings of the same eigenbasis measurement, and the two labels agree because evaluating the restriction of $g_h$ to $\ell$ at the parameter of $u$ is evaluating $g_h$ at $u$ (Definition [Restriction to a line](../../structure-of-the-proof/part-07/def-line-restriction.md)), $u$ lying on $\ell$ at that parameter. So the two players' measurements are convolutions of their own factors with *one* ancilla measurement, the factorization applies again, the ancilla factor is again exactly one, and what remains is item 2a or 2b of Lemma [Win implications](lem-qld-win.md) — the line answer evaluated at the sampled point against the point answer — at $2 \cdot 86 \varepsilon$.

## Lean

Formalized as [`MIPRE.QLD.lineCoeffs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.lineCoeffs), [`MIPRE.QLD.eval_lineCoeffs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.eval_lineCoeffs), [`MIPRE.QLD.dotF_indVec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.dotF_indVec), [`MIPRE.QLD.padLine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.padLine), [`MIPRE.QLD.linePoly_eval_eq_range`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.linePoly_eval_eq_range), [`MIPRE.QLD.eval_padLine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.eval_padLine), [`MIPRE.QLD.rdLine`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.rdLine), [`MIPRE.QLD.synLinePOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.synLinePOVM), [`MIPRE.QLD.synLinePOVM_map_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.synLinePOVM_map_eval), [`MIPRE.QLD.lineAnsPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.lineAnsPOVM), [`MIPRE.QLD.hatLinePOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatLinePOVM), [`MIPRE.QLD.isPVM_hatLinePOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVM_hatLinePOVM), [`MIPRE.QLD.hatLinePOVM_map_eval`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatLinePOVM_map_eval), [`MIPRE.QLD.sum_xSqNorm_hatLinePOVM_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_xSqNorm_hatLinePOVM_le), [`MIPRE.QLD.hatLinePOVM_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatLinePOVM_consistency), [`MIPRE.QLD.Content.omega_pt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.Content.omega_pt), [`MIPRE.QLD.sum_xSqNorm_hatLine_point_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.sum_xSqNorm_hatLine_point_le), [`MIPRE.QLD.rep_add_lineParam_smul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.rep_add_lineParam_smul), [`MIPRE.QLD.abaseOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.abaseOf), [`MIPRE.QLD.ddirOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.ddirOf), [`MIPRE.QLD.dbaseOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.dbaseOf), [`MIPRE.QLD.d_le_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.d_le_mul), [`MIPRE.QLD.m_le_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.m_le_mul), [`MIPRE.QLD.hsub_aline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hsub_aline), [`MIPRE.QLD.hsub_dline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hsub_dline), [`MIPRE.QLD.hatLinePOVM_point_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.hatLinePOVM_point_consistency), [`MIPRE.QLD.expanded_lines_aline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.expanded_lines_aline), [`MIPRE.QLD.expanded_lines_dline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.expanded_lines_dline), [`MIPRE.QLD.isPVM_synPOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVM_synPOVM), [`MIPRE.QLD.kronIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.kronIn), [`MIPRE.QLD.kronIn_op`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.kronIn_op), [`MIPRE.QLD.isPVMIn_kronIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVMIn_kronIn), [`MIPRE.QLD.kronIn_congr`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.kronIn_congr), [`MIPRE.QLD.kronIn_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.kronIn_map), [`MIPRE.QLD.isPVM_synLinePOVM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.QLD.isPVM_synLinePOVM).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 2632](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L2632)
