---
declaration: theorem
origin: cited
lean: TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le
statement: formalized
proof: formalized
---

# The graded Nakayama lemma for generators

If a set `s` of homogeneous elements of positive
degree generates the irrelevant ideal `A₊` of an `ℕ`-graded commutative semiring modulo `A₊²`, then
`s` generates the semiring as an algebra over its degree-zero part.

```lean
TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le.{u_1, u_2} {A : Type u_1} {σ : Type u_2}
  [CommSemiring A] [SetLike σ A] [AddSubmonoidClass σ A] (𝒜 : ℕ → σ) [GradedRing 𝒜] {s : Set A}
  (hs : ∀ x ∈ s, ∃ i, 0 < i ∧ x ∈ 𝒜 i)
  (h :
    (HomogeneousIdeal.irrelevant 𝒜).toIdeal ≤
      Ideal.span s ⊔ (HomogeneousIdeal.irrelevant 𝒜).toIdeal ^ 2) :
  Algebra.adjoin (↥(𝒜 0)) s = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Nakayama.html#TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le).

## Sources

- [Tau Ceti documentation: `TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/GradedAlgebra/Nakayama.html#TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le)
- [Source of `TauCeti.GradedAlgebra.adjoin_eq_top_of_irrelevant_le` in TauCeti/RingTheory/GradedAlgebra/Nakayama.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/GradedAlgebra/Nakayama.lean#L57)
