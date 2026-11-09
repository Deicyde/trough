---
declaration: theorem
origin: cited
lean: SumOfSetsInSeveralDimensions.card_add_sum_min_le_card_add_of_finrank_span_sub_eq, SumOfSetsInSeveralDimensions.card_add_mul_card_le_card_add_add_of_le_finrank_span_sub, SumOfSetsInSeveralDimensions.sInf_card_add_eq_add_sum_min, SumOfSetsInSeveralDimensions.freimanDim_le_two_mul_sub_one_of_card_add_le
statement: formalized
proof: formalized
---

# Sum of sets in several dimensions

> Proves Ruzsa's lower bound for sumsets in R^D. If A and B are finite with B nonempty, |B| ≤ |A| and A + B of affine dimension d, then |A + B| ≥ |A| + Σ\_{t=1}^{|B|-1} min(d, |A| - t), and this bound is attained in R^d whenever d ≥ 1 and |A| ≥ d + 1, so it is the exact minimum. Derives the asymmetric form of Freiman's lemma, |A + B| ≥ |A| + d|B| - d(d+1)/2. Defines the Freiman dimension of a finite subset of a commutative monoid, transfers the bound to sets with a Freiman model in R^r, and shows that a set X with |X + X| ≤ κ|X| has Freiman dimension at most 2κ - 1 and at most κ - 1 + κ(2κ - 1)/|X|.

*Quoted from the card [LeanPool/projects/sum-of-sets-in-several-dimensions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sum-of-sets-in-several-dimensions.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`SumOfSetsInSeveralDimensions.card_add_sum_min_le_card_add_of_finrank_span_sub_eq`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/LowerBound.html#SumOfSetsInSeveralDimensions.card_add_sum_min_le_card_add_of_finrank_span_sub_eq) (theorem; a main declaration), declared in [LeanPool/SumOfSetsInSeveralDimensions/LowerBound.lean, line 107](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/LowerBound.lean#L107): “For finite A, B ⊆ R^D with B nonempty and |B| ≤ |A|, if the differences of A + B span a space of dimension d, then |A| + Σ\_{t=1}^{|B|-1} min(d, |A| - t) ≤ |A + B|.” Its source, as the card gives it: “Theorem 1.”
- [`SumOfSetsInSeveralDimensions.card_add_mul_card_le_card_add_add_of_le_finrank_span_sub`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/ClosedForm.html#SumOfSetsInSeveralDimensions.card_add_mul_card_le_card_add_add_of_le_finrank_span_sub) (theorem; a main declaration), declared in [LeanPool/SumOfSetsInSeveralDimensions/ClosedForm.lean, line 88](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/ClosedForm.lean#L88): “For finite A, B ⊆ R^D with B nonempty and |B| ≤ |A|, and every d at most the dimension of the span of the differences of A + B, |A| + d|B| ≤ |A + B| + d(d+1)/2.” Its source, as the card gives it: “Corollary 1.1.”
- [`SumOfSetsInSeveralDimensions.sInf_card_add_eq_add_sum_min`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/MinCardAdd.html#SumOfSetsInSeveralDimensions.sInf_card_add_eq_add_sum_min) (theorem; a main declaration), declared in [LeanPool/SumOfSetsInSeveralDimensions/MinCardAdd.lean, line 94](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/MinCardAdd.lean#L94): “For d ≥ 1, 1 ≤ m ≤ n and n ≥ d + 1, the least size of A + B over A, B ⊆ R^d with |A| = m, |B| = n and A + B of affine dimension d is n + Σ\_{j=1}^{m-1} min(d, n - j).” Its source, as the card gives it: “Theorem 2, F_d(m, n) = G_d(m, n).”
- [`SumOfSetsInSeveralDimensions.sInf_card_add_of_finrank_span_sub_right_eq_add_sum_min`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/MinCardAdd.html#SumOfSetsInSeveralDimensions.sInf_card_add_of_finrank_span_sub_right_eq_add_sum_min) (theorem), declared in [LeanPool/SumOfSetsInSeveralDimensions/MinCardAdd.lean, line 103](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/MinCardAdd.lean#L103): “The same minimum n + Σ\_{j=1}^{m-1} min(d, n - j) holds when only B is required to have affine dimension d.” Its source, as the card gives it: “Theorem 2, F'\_d(m, n) = G_d(m, n).”
- [`SumOfSetsInSeveralDimensions.freimanDim_le_two_mul_sub_one_of_card_add_le`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.html#SumOfSetsInSeveralDimensions.freimanDim_le_two_mul_sub_one_of_card_add_le) (theorem; a main declaration), declared in [LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.lean, line 277](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.lean#L277): “A nonempty finite subset X of a cancellative commutative monoid with |X + X| ≤ κ|X|, for a real κ, has Freiman dimension at most 2κ - 1.”
- [`SumOfSetsInSeveralDimensions.freimanDim_le_sub_one_add_mul_div_card_of_card_add_le`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.html#SumOfSetsInSeveralDimensions.freimanDim_le_sub_one_add_mul_div_card_of_card_add_le) (theorem), declared in [LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.lean, line 313](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.lean#L313): “Under the same hypotheses, the Freiman dimension of X is at most κ - 1 + κ(2κ - 1)/|X|.”
- [`SumOfSetsInSeveralDimensions.card_add_sum_min_le_of_freimanDim_union`](https://leanpool.github.io/lean-pool/LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.html#SumOfSetsInSeveralDimensions.card_add_sum_min_le_of_freimanDim_union) (theorem), declared in [LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.lean, line 251](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions/FreimanDimensionSumsetBounds.lean#L251): “Ruzsa's lower bound holds for finite A, B in a commutative monoid with B nonempty and |B| ≤ |A|, with d replaced by r - 1, where r ≥ 1 is the Freiman dimension of A ∪ B.”

## Project

- Authors: Gabriel Dahia.
- Source: *Sum of sets in several dimensions* by Imre Z. Ruzsa, [doi:10.1007/BF01302969](https://doi.org/10.1007/BF01302969).
- Project repository: [gdahia/SumOfSetsInSeveralDimensions](https://github.com/gdahia/SumOfSetsInSeveralDimensions), at commit [bd2694b8](https://github.com/gdahia/SumOfSetsInSeveralDimensions/tree/bd2694b89fbe18ee5c4365a6330eba36d9f7ed8e).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11P70, 11B13, 11B75.
- In Lean Pool: [LeanPool/SumOfSetsInSeveralDimensions](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions), from the card [LeanPool/projects/sum-of-sets-in-several-dimensions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sum-of-sets-in-several-dimensions.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sum-of-sets-in-several-dimensions.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sum-of-sets-in-several-dimensions.yaml)
- [Lean Pool at 2b205bf9: LeanPool/SumOfSetsInSeveralDimensions](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/SumOfSetsInSeveralDimensions)
