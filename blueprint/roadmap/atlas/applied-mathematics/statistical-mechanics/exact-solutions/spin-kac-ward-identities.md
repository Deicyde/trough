---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_decExternalStepWalk, StatMech.Onsager.ons_mvMonomialValue, StatMech.Onsager.ons_MvSeriesEvalSummable, StatMech.Onsager.ons_mvSeriesEvalNorm, StatMech.Onsager.ons_TorusEvenSubgraph, StatMech.Onsager.ons_DecoratedEvenSubgraph, StatMech.Onsager.ons_originalEdgesOfDecorated, StatMech.Onsager.ons_decIsExternal
statement: formalized
proof: formalized
---

# Spin Kac–Ward identities

71 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html).

## One-edge decorated walk along an external edge

The one-edge decorated walk along the external edge from `d` to its reverse.

Formalized by `StatMech.Onsager.ons_decExternalStepWalk`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleExponent.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleExponent.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-external-step-walk).

## Value of a monomial at weights

The value `∏_e w_e ^ {m e}` of the monomial with exponent `m` at weights `w`.

Formalized by `StatMech.Onsager.ons_mvMonomialValue`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEvalAlgebra.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEvalAlgebra.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-mv-monomial-value).

## Absolute summability of a power series evaluated at weights

Absolute summability of `∑_m coeff_m · w^m`.

Formalized by `StatMech.Onsager.ons_MvSeriesEvalSummable`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEvalAlgebra.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEvalAlgebra.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-mv-series-eval-summable).

## Sum of absolute values of an evaluated power series

The sum `∑_m ‖coeff_m · w^m‖` of absolute values.

Formalized by `StatMech.Onsager.ons_mvSeriesEvalNorm`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEvalAlgebra.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEvalAlgebra.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-mv-series-eval-norm).

## Even subgraphs of the L × L torus

Even subgraphs of the `L × L` torus.

Formalized by `StatMech.Onsager.ons_TorusEvenSubgraph`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-torus-even-subgraph).

## Even subgraphs of the decorated torus graph

Even subgraphs of the decorated graph of the torus.

Formalized by `StatMech.Onsager.ons_DecoratedEvenSubgraph`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-even-subgraph).

## Torus even subgraph of a decorated even subgraph

The torus even subgraph corresponding to a decorated even subgraph under the decoration
bijection.

Formalized by `StatMech.Onsager.ons_originalEdgesOfDecorated`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-original-edges-of-decorated).

## Externality of a decorated edge

An edge of the decorated graph is external if it joins a dart to its reverse.

Formalized by `StatMech.Onsager.ons_decIsExternal`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-is-external).

## External edges of a decorated edge set

The external edges of a decorated edge set.

Formalized by `StatMech.Onsager.ons_decoratedExternalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-external-edges).

## Projection of a decorated edge to the torus

The projection of a decorated edge to the torus, taking each dart to its starting site.

Formalized by `StatMech.Onsager.ons_decEdgeProjection`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-edge-projection).

## Spin weight of a decorated even subgraph

The weight `χ_{a,b}(hom F) x^|F|` of the torus even subgraph `F` corresponding to a decorated
even subgraph.

Formalized by `StatMech.Onsager.ons_decoratedSpinWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-spin-weight).

## External edges used by a decorated walk

The external edges used by a walk in the decorated graph.

Formalized by `StatMech.Onsager.ons_walkExternalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-walk-external-edges).

## Torus edges underlying a decorated walk

The torus edges underlying the external edges of a decorated walk.

Formalized by `StatMech.Onsager.ons_walkOriginalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationSum.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-walk-original-edges).

## Decorated edges as formal-series variables

Decorated edges, used as the variables of the formal series.

Formalized by `StatMech.Onsager.ons_DecEdge`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-edge).

## Exponent of a Kac-Ward transition

The exponent of a transition: one for the external edge at `d₁` and one for each internal edge
on the path at the site of `d₂`.

Formalized by `StatMech.Onsager.ons_decTransitionExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-transition-exponent).

## Scalar of a Kac-Ward transition

The scalar of a transition: its boundary phase times its turn weight, or `0` if `d₂` does not
start at the head of `d₁`.

Formalized by `StatMech.Onsager.ons_decTransitionScalar`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-transition-scalar).

## Monomial of a Kac-Ward transition

The monomial of the transition from `d₁` to `d₂`.

Formalized by `StatMech.Onsager.ons_decFormalTransition`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-transition).

## Exponent of a closed Kac-Ward walk

The exponent of a closed walk: the sum of the exponents of its transitions.

Formalized by `StatMech.Onsager.ons_decLoopExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-loop-exponent).

## Scalar of a closed Kac-Ward walk

The scalar of a closed walk: the product of the scalars of its transitions.

Formalized by `StatMech.Onsager.ons_decLoopScalar`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-loop-scalar).

## Total degree of an exponent

The total degree `∑ m e` of an exponent; this is `Finsupp.degree`.

Formalized by `StatMech.Onsager.ons_finsuppTotalDegree`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-finsupp-total-degree).

## Total degree of an exponent agrees with Mathlib's degree

`ons_finsuppTotalDegree` agrees with Mathlib's `Finsupp.degree`.

Formalized by `StatMech.Onsager.ons_finsuppTotalDegree_eq_degree`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-finsupp-total-degree-eq-degree).

## Coefficient of the formal Kac-Ward logarithm

The coefficient of `x^m` in the formal logarithm: minus one half of the sum over closed walks of
length `r + 1 ≤ deg m` with exponent `m` of their scalars divided by `r + 1`.

Formalized by `StatMech.Onsager.ons_decFormalLogCoeff`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-log-coeff).

## Formal logarithm of the Kac-Ward root

The formal logarithm of the Kac-Ward root.

Formalized by `StatMech.Onsager.ons_decFormalLog`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-log).

## Formal Kac-Ward root

The formal Kac-Ward root: the formal exponential of `ons_decFormalLog`.

Formalized by `StatMech.Onsager.ons_decFormalRoot`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-root).

## Squarefree exponent of a set of variables

The squarefree exponent `∑_{e ∈ S} single e 1` of a set of variables.

Formalized by `StatMech.Onsager.ons_finsetExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-finset-exponent).

## Decorated spin polynomial

The decorated spin polynomial `∑_D χ_{a,b}(hom D) ∏_{e ∈ D} x_e` over decorated even subgraphs.

Formalized by `StatMech.Onsager.ons_decoratedSpinPolynomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-spin-polynomial).

## Evaluation of a multivariate power series at weights

Evaluation of a multivariate formal power series at weights, as the sum
`∑_m coeff_m · weight^m`.

Formalized by `StatMech.Onsager.ons_mvSeriesEval`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-mv-series-eval).

## Formal Kac-Ward identity on the torus

The formal Kac-Ward identity on the `L × L` torus: for every spin structure, the formal Kac-Ward
root equals the decorated spin polynomial.

Formalized by `StatMech.Onsager.ons_decoratedFormalKacWardIdentity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalSeries.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-formal-kac-ward-identity).

## Closed-walk weight through a dart but not its reverse

The total decorated-weight Kac-Ward weight of closed walks of length `n + 1` visiting `e` but
not its reverse.

Formalized by `StatMech.Onsager.ons_decPhaseBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-phase-bucket-e).

## Closed-walk weight avoiding a dart and its reverse

The total decorated-weight Kac-Ward weight of closed walks of length `n + 1` visiting neither
`e` nor its reverse.

Formalized by `StatMech.Onsager.ons_decPhaseBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-phase-bucket-n).

## Masked closed-walk weight through a dart but not its reverse

As `ons_decPhaseBucketE`, with the darts of `forbidden` masked.

Formalized by `StatMech.Onsager.ons_decMaskPhaseBucketE`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-mask-phase-bucket-e).

## Masked closed-walk weight avoiding a dart and its reverse

As `ons_decPhaseBucketN`, with the darts of `forbidden` masked.

Formalized by `StatMech.Onsager.ons_decMaskPhaseBucketN`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-mask-phase-bucket-n).

## Decorated weights with one edge weight scaled by t

Decorated weights with the weight of `edge` multiplied by `t`.

Formalized by `StatMech.Onsager.ons_scaleDecEdgeWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationExternalDeletion.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-scale-dec-edge-weight).

## Log-coefficient polynomial over the cycles of a decomposition

The polynomial `∑_C log-coefficient(C) x^{E(C)}` over the cycles `C` of a fixed decomposition of
an even subgraph.

Formalized by `StatMech.Onsager.ons_decComponentSeries`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalCoefficient.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalCoefficient.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-component-series).

## Squarefree exponent

An exponent is squarefree if every variable occurs with exponent at most `1`.

Formalized by `StatMech.Onsager.ons_IsSquarefreeExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalCoefficient.lean, line 982](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalCoefficient.lean#L982). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-is-squarefree-exponent).

## Formal-logarithm term from closed walks of given length and exponent

The term of the evaluated formal logarithm from closed walks of length `r + 1` with exponent
`m`, divided by `r + 1` and multiplied by `w^m`.

Formalized by `StatMech.Onsager.ons_decFormalBucketTerm`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEval.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalEval.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-bucket-term).

## External part of a loop exponent

The external part of a loop exponent: one for the external edge at each dart of the loop.

Formalized by `StatMech.Onsager.ons_decLoopExternalExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-loop-external-exponent).

## Internal part of a loop exponent

The internal part of a loop exponent: the internal edges on the paths between consecutive ports.

Formalized by `StatMech.Onsager.ons_decLoopInternalExponent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-loop-internal-exponent).

## Kac-Ward loops with a given squarefree exponent and nonzero scalar

The closed Kac-Ward walks of length `n` with exponent the squarefree exponent of `S` and nonzero
scalar.

Formalized by `StatMech.Onsager.ons_decSquarefreeLoopFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-squarefree-loop-finset).

## Darts of a loop with their reverses

The darts of a loop together with their reverses.

Formalized by `StatMech.Onsager.ons_decLoopRootFinset`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-loop-root-finset).

## Rotations of a loop and of its reversal

The `2n` rotations of a loop and of its reversal, indexed by `Fin n ⊕ Fin n`.

Formalized by `StatMech.Onsager.ons_decLoopOrientation`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean, line 573](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationLoopClassification.lean#L573). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-loop-orientation).

## Column-scaled augmented Kac-Ward matrix

The augmented matrix with blocks `Λ₀`, `t U`, `V` and `0` (scaling on the column factor).

Formalized by `StatMech.Onsager.ons_decMiddleAugmentedCol`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleAffine.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleAffine.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-middle-augmented-col).

## Row weights of the column-scaled augmented matrix

Row weights of the column-scaled augmented matrix.

Formalized by `StatMech.Onsager.ons_decMiddleColRowWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleAffine.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleAffine.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-middle-col-row-weight).

## Column weights of the column-scaled augmented matrix

Column weights of the column-scaled augmented matrix.

Formalized by `StatMech.Onsager.ons_decMiddleColColWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleAffine.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationMiddleAffine.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-middle-col-col-weight).

## Vanishing of repeated-edge coefficients of the formal Kac-Ward root

On every `L × L` torus with `L > 2` and for every spin structure, the coefficient of the formal
Kac-Ward root at any exponent that uses some decorated edge at least twice is zero.

Formalized by `StatMech.Onsager.ons_DecFormalRepeatedEdgeVanishes`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationRepeatedEdge.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationRepeatedEdge.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-repeated-edge-vanishes).

## Edge-weighted spin weight of a decorated even subgraph

The edge-weighted spin weight `χ_{a,b}(hom F) ∏_{e ∈ F} w_e` of the torus even subgraph `F`
corresponding to a decorated even subgraph.

Formalized by `StatMech.Onsager.ons_decoratedWeightedSpinWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWeighted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationWeighted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-weighted-spin-weight).

## Decorated even subgraphs containing a given external edge

Decorated even subgraphs that contain the external edge at `d`.

Formalized by `StatMech.Onsager.ons_DecoratedContainingEdge`, an abbreviation declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-containing-edge).

## Split of a decorated even subgraph into a rooted cycle and remainder

A split of a decorated even subgraph containing the external edge at `d` into a simple cycle
rooted at `d` (starting along that edge) and an even remainder disjoint from the cycle.

Formalized by `StatMech.Onsager.ons_DecoratedEdgeSplit`, a structure declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-edge-split).

## Chosen split of a decorated even subgraph at an external edge

A chosen split of a decorated even subgraph at the external edge of `d`.

Formalized by `StatMech.Onsager.ons_decoratedEdgeSplit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-edge-split-2).

## Cycle removal identity for decorated even subgraphs

The cycle removal identity: the Kac-Ward root with `d` and its reverse masked, times the total
first-return weight at `d`, equals the sum over decorated even subgraphs through `d` of the
first-return weight of the split-off cycle times the spin weight of the remainder.

Formalized by `StatMech.Onsager.ons_decoratedCycleRemovalIdentity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationCycleRemoval.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-decorated-cycle-removal-identity).

## Degree-$n$ part of a power series evaluated at a point

The sum of the terms of total degree `n` of a series evaluated at `w`.

Formalized by `StatMech.Onsager.ons_degreeFiberCoeff`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/MvSeriesAnalyticUniqueness.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/MvSeriesAnalyticUniqueness.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-degree-fiber-coeff).

## Sum of absolute values of the degree-$n$ terms at a point

The sum of the absolute values of the terms of total degree `n` evaluated at `w`.

Formalized by `StatMech.Onsager.ons_degreeFiberNorm`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/MvSeriesAnalyticUniqueness.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/MvSeriesAnalyticUniqueness.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-degree-fiber-norm).

## Homogeneous degree-$n$ part of a power series as a polynomial

The homogeneous degree-`n` part of a series as a polynomial (finitely many variables).

Formalized by `StatMech.Onsager.ons_degreeFiberPolynomial`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/MvSeriesAnalyticUniqueness.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/MvSeriesAnalyticUniqueness.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-degree-fiber-polynomial).

## Spin-character sums squared as twisted determinants at activity $x$

For every spin structure `(a, b)`, the square of the spin-character sum equals the twisted
Kac-Ward determinant `det (1 - Λ_{ab})` at activity `x`.

Formalized by `StatMech.Onsager.ons_spinCoefficientIdentity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCoefficientTarget.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCoefficientTarget.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-coefficient-identity).

## Sector weight of a homology class as a polynomial

The sector weight of the homology class `h` as a real polynomial in `x`.

Formalized by `StatMech.Onsager.ons_sectorPoly`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-sector-poly).

## Signed sector polynomial with the $(1,1)$ sector negated

The signed sector sum `ons_spin00` as a polynomial.

Formalized by `StatMech.Onsager.ons_spinPoly00`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-poly00).

## Signed sector polynomial with the $(1,0)$ sector negated

The signed sector sum `ons_spin10` as a polynomial.

Formalized by `StatMech.Onsager.ons_spinPoly10`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-poly10).

## Signed sector polynomial with the $(0,1)$ sector negated

The signed sector sum `ons_spin01` as a polynomial.

Formalized by `StatMech.Onsager.ons_spinPoly01`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-poly01).

## Signed sector polynomial with only the $(0,0)$ sector positive

The signed sector sum `ons_spin11` as a polynomial.

Formalized by `StatMech.Onsager.ons_spinPoly11`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-poly11).

## Sector determinant as a function of $x$

The sector determinant as a function of `x`: the product over shifted momenta of
`(1 + x²)² - 2x(1 - x²)(cos k₁ + cos k₂)`.

Formalized by `StatMech.Onsager.ons_spinDetX`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-det-x).

## Sector determinant as a real polynomial

The sector determinant as a real polynomial in `x`.

Formalized by `StatMech.Onsager.ons_spinDetPoly`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-det-poly).

## Four spin Kac-Ward identities on the torus at activity $x$

The four spin Kac-Ward identities `spin_{ab}(x)² = det_{ab}(x)` on the `L × L` torus at activity
`x`.

Formalized by `StatMech.Onsager.ons_spinKacWardAt`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinPolynomial.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-kac-ward-at).

## Weighted character sum over even subgraphs containing an edge

The part of the edge-weighted character sum coming from even subgraphs that contain `edge`.

Formalized by `StatMech.Onsager.ons_weightedSpinEdgeCoefficient`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedAffine.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedAffine.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-weighted-spin-edge-coefficient).

## Edge weights restricted to a set of edges

The edge weights restricted to `S`: equal to `weight` on `S` and `0` elsewhere.

Formalized by `StatMech.Onsager.ons_restrictEdgeWeight`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCoefficientInduction.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCoefficientInduction.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-restrict-edge-weight).

## Edge coefficient identity on the $L \times L$ torus

The edge coefficient identity on the `L × L` torus: for small weights, the part of the
edge-weighted character sum from even subgraphs through the edge of `e` equals minus the Kac-Ward
root with `e` and its reverse masked, times the total first-return weight at `e`.

Formalized by `StatMech.Onsager.ons_weightedEdgeCoefficientIdentity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCoefficientInduction.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinCoefficientInduction.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-weighted-edge-coefficient-identity).

## Edge-weighted spin-character sum over even subgraphs

The edge-weighted spin-character sum `∑_F χ_{a,b}(hom F) ∏_{e ∈ F} w_e` over even subgraphs of
the torus.

Formalized by `StatMech.Onsager.ons_weightedSpinCharacterSum`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedTarget.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedTarget.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-weighted-spin-character-sum).

## Edge-weighted root identity on the torus

The edge-weighted root identity on the `L × L` torus: for every spin structure and every edge
weight bounded by `q` below Sherman's radius, the walk-series square root of the twisted
edge-weighted Kac-Ward determinant equals the edge-weighted character sum.

Formalized by `StatMech.Onsager.ons_weightedRootIdentity`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedTarget.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedTarget.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-weighted-root-identity).

## Sherman's radius for $L > 2$, with value 1 otherwise

Sherman's radius for `L > 2`, and `1` otherwise.

Formalized by `StatMech.Onsager.ons_spinShermanRadius`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedTarget.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/SpinWeightedTarget.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-spin-sherman-radius).

## Second-difference factor for a monomial of degree k

The factor `2^k - 2 + 0^k` by which a second difference multiplies a monomial of degree `k` in
one variable.

Formalized by `StatMech.Onsager.ons_secondDifferenceFactor`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalMultiaffine.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalMultiaffine.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-second-difference-factor).

## Second difference of a formal series in one variable

The second difference of a formal series in the variable `edge`: the coefficient at `m` is
multiplied by `2^{m edge} - 2 + 0^{m edge}`.

Formalized by `StatMech.Onsager.ons_decFormalSecondDifference`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalMultiaffine.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalMultiaffine.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-dec-formal-second-difference).

## Onsager's formula

**Onsager's formula** for the zero-field square-lattice Ising model, in the form
`torus pressure → ons_pressure β` for `β ≥ 0` (L. Onsager, *Crystal statistics. I*, 1944). See
`main_free_energy` for the explicit integral.

Formalized by `StatMech.Onsager.ons_free_energy`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalMultiaffine.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/DecorationFormalMultiaffine.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html#ons-free-energy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spin Kac–Ward identities](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/spin-kac-ward-identities)
