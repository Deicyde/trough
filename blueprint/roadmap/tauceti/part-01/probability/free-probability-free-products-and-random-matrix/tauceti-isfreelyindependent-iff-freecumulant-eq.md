---
declaration: theorem
origin: cited
lean: TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero

*Free cumulants detect freeness*: for a normalised `φ`, the subalgebras `B i` are freely
independent exactly when every mixed free cumulant `κ_n(a₁, …, aₙ)`, with letters
`aₖ ∈ B (ℓ k)` whose labels are not all equal, vanishes.

```lean
TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  {ι : Type u_3} [CommRing R] [Semiring A] [Algebra R A] {φ : A →ₗ[R] R} {B : ι → Subalgebra R A}
  (hφ : φ 1 = 1) :
  TauCeti.IsFreelyIndependent φ B ↔
    ∀ (n : ℕ) (a : Fin n → A) (ℓ : Fin n → ι),
      (∀ (k : Fin n), a k ∈ B (ℓ k)) →
        ∀ (k k' : Fin n), ℓ k ≠ ℓ k' → TauCeti.freeCumulant (⇑φ) a Finset.univ = 0
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Proof depends on

- [TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant](tauceti-apply-prod-offn-eq-sum-prod-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Free.html#TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Free.html#TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero)
- [Source of `TauCeti.isFreelyIndependent_iff_freeCumulant_eq_zero` in TauCeti/Probability/FreeProbability/Cumulant/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Cumulant/Free.lean#L219)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
