---
declaration: theorem
origin: cited
lean: TauCeti.exists_cover_of_fderiv_eq_zero
statement: formalized
proof: formalized
---

# The Morse criticality lemma

The set on which a `C^(k+1)` map into a finite-dimensional
real normed space is critical, in the sense that its derivative vanishes, is covered by a
countable set and countably many bounded pieces, on each of which the map has a uniform
`o(‖y - x‖ ^ (k + 1))` modulus.  Neither the set nor the pieces are assumed measurable.

```lean
TauCeti.exists_cover_of_fderiv_eq_zero.{u_1} {n k : ℕ} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] (A : Set (Fin n → ℝ)) {f : (Fin n → ℝ) → F}
  (hf : ContDiff ℝ (↑k + 1) f) (hA : ∀ x ∈ A, fderiv ℝ f x = 0) :
  ∃ A₀ P,
    A₀.Countable ∧
      P.Countable ∧
        A ⊆ A₀ ∪ ⋃₀ P ∧
          ∀ S ∈ P,
            Bornology.IsBounded S ∧
              ∀ (ε : ℝ),
                0 < ε →
                  ∃ δ, 0 < δ ∧ ∀ x ∈ S, ∀ y ∈ S, ‖y - x‖ < δ → ‖f y - f x‖ ≤ ε * ‖y - x‖ ^ (k + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_cover_of_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/MorseVanishing/Basic.html#TauCeti.exists_cover_of_fderiv_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_cover_of_fderiv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Sard/MorseVanishing/Basic.html#TauCeti.exists_cover_of_fderiv_eq_zero)
- [Source of `TauCeti.exists_cover_of_fderiv_eq_zero` in TauCeti/Analysis/Calculus/Sard/MorseVanishing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Sard/MorseVanishing/Basic.lean#L391)
