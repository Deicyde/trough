---
declaration: theorem
origin: cited
lean: TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone, Monotone.exists_sum_range_monomial_sum_finrank_singularHomology_ofInclusion_eq_add_mul, TauCeti.exists_sum_range_monomial_sum_sublevelPair_eq_add_mul
statement: formalized
proof: formalized
---

# The Morse polynomial identity of a filtration

Let `A 0 ⊆ A 1 ⊆ ⋯ ⊆ A (N + 1)` be
subspaces of a space such that every step `Hᵢ(A (j + 1), A j)`, `j ≤ N`, is finite-dimensional in
every degree and no step has homology in degree `n + 1`. Write `bᵢ = dim Hᵢ(A (N + 1), A 0)` and
`cᵢ = ∑ⱼ dim Hᵢ(A (j + 1), A j)`. Then `∑ᵢ₌₀ⁿ cᵢ tⁱ = ∑ᵢ₌₀ⁿ bᵢ tⁱ + (1 + t) Q(t)` for a
polynomial `Q` with natural number coefficients. For `i < n` the coefficient of `tⁱ` in `Q` is the
sum over `j < N` of the ranks of the connecting maps
`Hᵢ₊₁(A (j + 2), A (j + 1)) ⟶ Hᵢ(A (j + 1), A 0)` of the triples `(A (j + 2), A (j + 1), A 0)`, and
for `i ≥ n` it is zero.

```lean
TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone.{w, u_1}
  {Y : TopCat} {A : ℕ → Set ↑Y} (hA : Monotone A) {k : Type u_1} [DivisionRing k] (V : ModuleCat k)
  {N : ℕ}
  (hfin : ∀ j ≤ N, ∀ (i : ℕ), Module.Finite k ↑((TopPair.ofInclusion ⋯).singularHomology V i))
  {n : ℕ}
  (hzero :
    ∀ j ≤ N, CategoryTheory.Limits.IsZero ((TopPair.ofInclusion ⋯).singularHomology V (n + 1))) :
  ∃ Q,
    ∑ i ∈ Finset.range (n + 1),
          (Polynomial.monomial i)
            (∑ j ∈ Finset.range (N + 1),
              Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i)) =
        ∑ i ∈ Finset.range (n + 1),
            (Polynomial.monomial i)
              (Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i)) +
          (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          Q.coeff i =
            ∑ j ∈ Finset.range N,
              Module.finrank k
                ↥(ModuleCat.Hom.hom
                      ((TauCeti.TopTriple.ofInclusions ⋯ ⋯).singularHomologyδ V (i + 1) i
                        ⋯)).range) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse polynomial identity (`ChainComplex.sum_range_monomial_finrank_X_eq`)](../../algebra/part-02/homology/the-morse-polynomial-identity-chaincomplex-sum-r.md)
- [The strong Morse inequalities of a filtration](the-strong-morse-inequalities-of-a-filtration.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone).

## Other forms

**The Morse polynomial identity along a filtration.** Formalized in Tau Ceti as [`Monotone.exists_sum_range_monomial_sum_finrank_singularHomology_ofInclusion_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#Monotone.exists_sum_range_monomial_sum_finrank_singularHomology_ofInclusion_eq_add_mul).

```lean
Monotone.exists_sum_range_monomial_sum_finrank_singularHomology_ofInclusion_eq_add_mul.{w, u_1}
  {Y : TopCat} {X : ℤ → Set ↑Y} (hX : Monotone X) {k : Type u_1} [DivisionRing k] (V : ModuleCat k)
  {a b : ℤ} (hab : a ≤ b) {n : ℕ}
  (h :
    ∀ q ∈ Finset.Ico a b, ∀ i ≤ n, Module.Finite k ↑((TopPair.ofInclusion ⋯).singularHomology V i))
  (hn :
    ∀ q ∈ Finset.Ico a b,
      CategoryTheory.Limits.IsZero ((TopPair.ofInclusion ⋯).singularHomology V (n + 1))) :
  ∃ Q,
    ∑ i ∈ Finset.range (n + 1),
          (Polynomial.monomial i)
            (∑ q ∈ Finset.Ico a b,
              Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i)) =
        ∑ i ∈ Finset.range (n + 1),
            (Polynomial.monomial i)
              (Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V i)) +
          (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          ↑(Q.coeff i) =
            ∑ j ∈ Finset.range (i + 1),
                (-1) ^ (i - j) *
                  ∑ q ∈ Finset.Ico a b,
                    ↑(Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V j)) -
              ∑ j ∈ Finset.range (i + 1),
                (-1) ^ (i - j) *
                  ↑(Module.finrank k ↑((TopPair.ofInclusion ⋯).singularHomology V j))) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

**The Morse polynomial identity of a sublevel filtration.** Formalized in Tau Ceti as [`TauCeti.exists_sum_range_monomial_sum_sublevelPair_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Sublevel.html#TauCeti.exists_sum_range_monomial_sum_sublevelPair_eq_add_mul).

```lean
TauCeti.exists_sum_range_monomial_sum_sublevelPair_eq_add_mul.{u, u_1, u_2} {X : Type u}
  [TopologicalSpace X] {β : Type u_1} [Preorder β] {f : X → β} {s : ℕ → β} (hs : Monotone s) {N : ℕ}
  (hs₀ : ∀ (x : X), s 0 < f x) (hsN : ∀ (x : X), f x ≤ s (N + 1)) {k : Type u_2} [DivisionRing k]
  (V : ModuleCat k)
  (hfin : ∀ j ≤ N, ∀ (i : ℕ), Module.Finite k ↑((TauCeti.sublevelPair f ⋯).singularHomology V i))
  {n : ℕ}
  (hzero :
    ∀ j ≤ N, CategoryTheory.Limits.IsZero ((TauCeti.sublevelPair f ⋯).singularHomology V (n + 1))) :
  ∃ Q,
    ∑ i ∈ Finset.range (n + 1),
          (Polynomial.monomial i)
            (∑ j ∈ Finset.range (N + 1),
              Module.finrank k ↑((TauCeti.sublevelPair f ⋯).singularHomology V i)) =
        ∑ i ∈ Finset.range (n + 1),
            (Polynomial.monomial i)
              (Module.finrank k
                ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj V).obj ↧X)) +
          (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          Q.coeff i =
            ∑ j ∈ Finset.range N,
              Module.finrank k
                ↥(ModuleCat.Hom.hom
                      ((TauCeti.TopTriple.ofInclusions ⋯ ⋯).singularHomologyδ V (i + 1) i
                        ⋯)).range) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.html#TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone)
- [Source of `TauCeti.exists_sum_range_monomial_singularHomology_ofInclusion_eq_add_mul_of_monotone` in TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/FilteredSpace/Finrank.lean#L444)
