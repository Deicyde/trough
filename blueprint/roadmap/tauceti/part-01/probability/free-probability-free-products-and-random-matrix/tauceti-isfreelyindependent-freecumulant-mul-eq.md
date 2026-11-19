---
declaration: theorem
origin: cited
lean: TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant
statement: formalized
proof: formalized
---

# TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant

*Free cumulants of products of free families*: if the letters of `a` and `b` lie in two
distinct members `B i`, `B j` of a free family of subalgebras, for a normalised `φ`, then
`κ_s(a_{x₁} b_{x₁}, …, a_{xₙ} b_{xₙ}) = ∑_{π ∈ NC(s)} κ_π(a) κ_{K(π)}(b)` for
`s = {x₁ < ⋯ < xₙ}`, where `K(π)` is the Kreweras complement of `π`.

```lean
TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant.{u_1,
    u_2, u_3, u_4}
  {R : Type u_1} {A : Type u_2} {ι : Type u_3} {α : Type u_4} [CommRing R] [Semiring A]
  [Algebra R A] [LinearOrder α] {φ : A →ₗ[R] R} {B : ι → Subalgebra R A} {s : Finset α}
  (h : TauCeti.IsFreelyIndependent φ B) (hφ : φ 1 = 1) {i j : ι} (hij : i ≠ j) {a b : α → A}
  (ha : ∀ x ∈ s, a x ∈ B i) (hb : ∀ x ∈ s, b x ∈ B j) :
  TauCeti.freeCumulant (⇑φ) (fun x => a x * b x) s =
    ∑ π, TauCeti.partitionCumulant (⇑φ) a π * TauCeti.partitionCumulant (⇑φ) b π.kreweras
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Kreweras.html#TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Kreweras.html#TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant)
- [Source of `TauCeti.IsFreelyIndependent.freeCumulant_mul_eq_sum_partitionCumulant_mul_partitionCumulant` in TauCeti/Probability/FreeProbability/Cumulant/Kreweras.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Cumulant/Kreweras.lean#L179)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
