---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_comp, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_one, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_zero, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_smul, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.norm_prodMap, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.ker_prodMap, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.range_prodMap, MathlibExt.Analysis.Normed.Operator.DirectSumOperators.isUnit_prodMap_iff
statement: formalized
proof: formalized
---

# Direct sums of operators

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html).

## Composition of direct sum operators is componentwise

Composing direct sums is componentwise.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_comp`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#prod-map-comp).

## Direct sum of identity operators is the identity

The identity direct sum is the identity.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_one`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#prod-map-one).

## Direct sum of zero operators is zero

The zero direct sum is zero.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#prod-map-zero).

## Scalar multiplication of a direct sum operator

Scaling a direct sum scales both summands by the same factor.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.prodMap_smul`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#prod-map-smul).

## Operator norm of a direct sum is the maximum of the norms

The operator norm of a direct sum is the maximum of the operator norms.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.norm_prodMap`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#norm-prod-map).

## Kernel of a direct sum operator

The kernel of a direct sum is the product of the kernels.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.ker_prodMap`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#ker-prod-map).

## Range of a direct sum operator

The range of a direct sum is the product of the ranges.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.range_prodMap`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#range-prod-map).

## Invertibility of a direct sum operator

A direct sum is a unit iff both summands are units.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.isUnit_prodMap_iff`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#is-unit-prod-map-iff).

## Spectrum of a direct sum operator is the union of spectra

The spectrum of a direct sum is the union of the spectra.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.spectrum_prodMap`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#spectrum-prod-map).

## Resolvent set of a direct sum operator

The resolvent set of a direct sum is the intersection of the resolvent sets.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.resolventSet_prodMap`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#resolvent-set-prod-map).

## Compactness of a direct sum operator

A direct sum is compact iff both summands are compact.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.isCompactOperator_prodMap_iff`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#is-compact-operator-prod-map-iff).

## Fredholmness of a direct sum operator

A direct sum is Fredholm iff both summands are Fredholm.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.isFredholm_prodMap_iff`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#is-fredholm-prod-map-iff).

## Fredholm index of a direct sum is additive

The Fredholm index of a direct sum is the sum of the Fredholm indices.

Formalized by `MathlibExt.Analysis.Normed.Operator.DirectSumOperators.index_prodMap`, a theorem declared in [MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Operator/DirectSumOperators.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html#index-prod-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Direct sums of operators](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/bounded-operators/direct-sums-of-operators)
