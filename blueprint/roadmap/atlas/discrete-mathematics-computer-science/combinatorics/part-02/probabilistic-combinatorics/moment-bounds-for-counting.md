---
declaration: section
origin: cited
lean: Matrix.sum_weights_shared_endpoint_le, Matrix.sum_mul_mul_kernel_le, Matrix.sum_ordered_nat_int_kernel_le, Finset.card_filter_mul_sq_le_sum_sq, Finset.card_filter_mul_sq_le_of_moments, Finset.card_filter_mul_sq_le_sum_sq_univ, Finset.card_filter_mul_sq_le_of_moments_univ
statement: formalized
proof: formalized
---

# Moment bounds for counting

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html).

## Bound on the weight of pairs sharing an endpoint with a fixed pair

Pairs sharing an endpoint with a fixed pair have total weight at most `4 * P`.
Loops are permitted. Symmetry bounds the two column fibers by the same row bound.

Formalized by `Matrix.sum_weights_shared_endpoint_le`, a theorem declared in [MathlibExt/Combinatorics/WeightedEdgeKernel.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/WeightedEdgeKernel.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#sum-weights-shared-endpoint-le).

## Weighted quadratic sum bound for a shared-endpoint kernel

A kernel vanishing on pairs with no common endpoint has weighted quadratic sum at most
`4 * P * totalWeight * m`. Neither nonnegativity nor symmetry of the kernel is required;
diagonal weights are permitted, and no separate nonnegativity assumption on `P` is needed.

Formalized by `Matrix.sum_mul_mul_kernel_le`, a theorem declared in [MathlibExt/Combinatorics/WeightedEdgeKernel.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/WeightedEdgeKernel.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#sum-mul-mul-kernel-le).

## Shared-endpoint kernel bound with hypotheses on distinct pairs

The `Variance.StHence` bound with the kernel hypothesis restricted to distinct pairs:
natural weights on `Fin g`, integer kernel, and row sums over erased diagonals.
Diagonal weights and kernel entries outside the distinct-pair domain are arbitrary.
The four inequalities in `h0` are precisely the negation of the source `Meets` disjunction.
The proof zeroes diagonal weights and masks the kernel outside the distinct-pair domain;
it does not extend a signed sum by adding unmasked terms.

Formalized by `Matrix.sum_ordered_nat_int_kernel_le`, a theorem declared in [MathlibExt/Combinatorics/WeightedEdgeKernel.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/WeightedEdgeKernel.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#sum-ordered-nat-int-kernel-le).

## Chebyshev-type count bound from the sum of squares

The number of points where a function is at least a nonnegative threshold,
times the threshold squared, is at most the sum of squares.

Formalized by `Finset.card_filter_mul_sq_le_sum_sq`, a theorem declared in [MathlibExt/Data/Finset/MomentBounds.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/MomentBounds.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#card-filter-mul-sq-le-sum-sq).

## Count bound from first and second moments

A denominator-cleared finite count bound from first and second moments.

Neither the finite set nor `A`, `t`, or `s` is required to be nonzero.

Formalized by `Finset.card_filter_mul_sq_le_of_moments`, a theorem declared in [MathlibExt/Data/Finset/MomentBounds.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/MomentBounds.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#card-filter-mul-sq-le-of-moments).

## Sum-of-squares count bound over the whole type

`card_filter_mul_sq_le_sum_sq` specialized to the universal finset.

Formalized by `Finset.card_filter_mul_sq_le_sum_sq_univ`, a theorem declared in [MathlibExt/Data/Finset/MomentBounds.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/MomentBounds.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#card-filter-mul-sq-le-sum-sq-univ).

## Moment count bound over the whole type

`card_filter_mul_sq_le_of_moments` specialized to the universal finset.

Formalized by `Finset.card_filter_mul_sq_le_of_moments_univ`, a theorem declared in [MathlibExt/Data/Finset/MomentBounds.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/MomentBounds.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html#card-filter-mul-sq-le-of-moments-univ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moment bounds for counting](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/moment-bounds-for-counting)
