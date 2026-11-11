---
declaration: theorem
origin: cited
lean: TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment
statement: formalized
proof: formalized
---

# TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment

The free cumulant of a word is the sum over the noncrossing partitions `π` of its block
moments weighted by the Möbius function, `κ_s(a) = ∑_{π ∈ NC(s)} μ(π, 1_s) φ_π(a)`.

```lean
TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  {α : Type u_3} [LinearOrder α] [CommRing R] [Monoid A] (φ : A → R) (a : α → A) (s : Finset α) :
  TauCeti.freeCumulant φ a s = ∑ π, (IncidenceAlgebra.mu R) π ⊤ * TauCeti.partitionMoment φ a ↑π
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment).

## Sources

- [Tau Ceti documentation: `TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment)
- [Source of `TauCeti.freeCumulant_eq_sum_mu_mul_partitionMoment` in TauCeti/Probability/FreeProbability/Cumulant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/FreeProbability/Cumulant/Basic.lean#L213)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeProbability/STATUS.md)
