---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone, TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_sum_sublevelPair
statement: formalized
proof: formalized
---

# The strong Morse inequalities of a filtration

Let `A 0 ⊆ A 1 ⊆ ⋯ ⊆ A (N + 1)` be
subspaces of a space such that every step `Hᵢ(A (j + 1), A j)`, `j ≤ N`, is finite-dimensional in
every degree, and write `Sₙ(P) = dim Hₙ(P) - dim Hₙ₋₁(P) + ⋯ ± dim H₀(P)`. Then
`Sₙ(A (N + 1), A 0) ≤ Sₙ(A 1, A 0) + ⋯ + Sₙ(A (N + 1), A N)`.

```lean
TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone.{w, u_1}
  {Y : TopCat} {A : ℕ → Set ↑Y} (hA : Monotone A) {k : Type u_1} [DivisionRing k] (V : ModuleCat k)
  {N : ℕ}
  (hfin : ∀ j ≤ N, ∀ (i : ℕ), Module.Finite k ↑((TopPair.ofInclusion ⋯).singularHomology V i))
  (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i)) ≤
    ∑ j ∈ Finset.range (N + 1),
      ∑ i ∈ Finset.range (n + 1),
        (-1) ^ (n - i) * ↑(Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone).

## Other forms

**The strong Morse inequalities of a sublevel filtration.** Formalized in Tau Ceti as [`TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_sum_sublevelPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Sublevel.html#TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_sum_sublevelPair).

```lean
TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_sum_sublevelPair.{u, u_1, u_2}
  {X : Type u} [TopologicalSpace X] {β : Type u_1} [Preorder β] {f : X → β} {s : ℕ → β}
  (hs : Monotone s) {N : ℕ} (hs₀ : ∀ (x : X), s 0 < f x) (hsN : ∀ (x : X), f x ≤ s (N + 1))
  {k : Type u_2} [DivisionRing k] (V : ModuleCat k)
  (hfin : ∀ j ≤ N, ∀ (i : ℕ), Module.Finite k ↑((TauCeti.sublevelPair f ⋯).singularHomology V i))
  (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) *
        ↑(Module.finrank k
            ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj V).obj ↧X)) ≤
    ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) *
        ↑(∑ j ∈ Finset.range (N + 1),
            Module.finrank k ↑((TauCeti.sublevelPair f ⋯).singularHomology V i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone)
- [Source of `TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_ofInclusion_le_of_monotone` in TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.lean#L387)
