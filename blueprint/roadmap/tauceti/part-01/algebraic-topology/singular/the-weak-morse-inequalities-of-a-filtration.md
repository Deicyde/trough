---
declaration: theorem
origin: cited
lean: TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone, TauCeti.finrank_singularHomology_le_sum_sublevelPair
statement: formalized
proof: formalized
---

# The weak Morse inequalities of a filtration

If `A 0 ⊆ A 1 ⊆ ⋯ ⊆ A (N + 1)` and every step
`Hᵢ(A (j + 1), A j)`, `j ≤ N`, is finite-dimensional, then `dim Hᵢ(A (N + 1), A 0)` is at most
the sum of the dimensions of the steps.

```lean
TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone.{w, u_1} {Y : TopCat}
  {A : ℕ → Set ↑Y} (hA : Monotone A) {k : Type u_1} [DivisionRing k] (V : ModuleCat k) {N : ℕ}
  (i : ℕ) (hfin : ∀ j ≤ N, Module.Finite k ↑((TopPair.ofInclusion ⋯).singularHomology V i)) :
  Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i) ≤
    ∑ j ∈ Finset.range (N + 1), Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone).

## Other forms

**The weak Morse inequalities of a sublevel filtration.** Formalized in Tau Ceti as [`TauCeti.finrank_singularHomology_le_sum_sublevelPair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Sublevel.html#TauCeti.finrank_singularHomology_le_sum_sublevelPair).

```lean
TauCeti.finrank_singularHomology_le_sum_sublevelPair.{u, u_1, u_2} {X : Type u} [TopologicalSpace X]
  {β : Type u_1} [Preorder β] {f : X → β} {s : ℕ → β} (hs : Monotone s) {N : ℕ}
  (hs₀ : ∀ (x : X), s 0 < f x) (hsN : ∀ (x : X), f x ≤ s (N + 1)) {k : Type u_2} [DivisionRing k]
  (V : ModuleCat k) (i : ℕ)
  (hfin : ∀ j ≤ N, Module.Finite k ↑((TauCeti.sublevelPair f ⋯).singularHomology V i)) :
  Module.finrank k ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj V).obj ↧X) ≤
    ∑ j ∈ Finset.range (N + 1), Module.finrank k ↑((TauCeti.sublevelPair f ⋯).singularHomology V i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone)
- [Source of `TauCeti.finrank_singularHomology_ofInclusion_le_sum_of_monotone` in TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.lean#L364)
