---
declaration: theorem
origin: cited
lean: TauCeti.WittVector.isStronglyNoetherian_intervalRing
statement: formalized
proof: formalized
---

# TauCeti.WittVector.isStronglyNoetherian_intervalRing

**The interval ring `B^I` is strongly noetherian** (Kedlaya, Theorem 4.10 and Remark 4.11),
for all radii `ρ₁ ≤ ρ₂`: each completed Huber algebra `B^I⟨X₁, …, Xₙ⟩` is the Gauss-normed ring
`B^I{X₁, …, Xₙ}` of unit-radius restricted series, which is noetherian by
`TauCeti.WittVector.isNoetherianRing_isRestricted_subring_intervalRing`.

```lean
TauCeti.WittVector.isStronglyNoetherian_intervalRing.{u_1, u_2} (p : ℕ) [Fact (Nat.Prime p)]
  {K : Type u_1} {O : Type u_2} [Field K] [CommRing O] [Algebra O K] [CharP O p] [PerfectRing O p]
  {v : Valuation K NNReal} {ϖ : O} (hv : v.Integers O) (hϖ : ϖ ≠ 0)
  (hϖ' : v ((algebraMap O K) ϖ) < 1) {ρ₁ ρ₂ : NNReal} (hρ₁ : ρ₁ ∈ Set.Ioo 0 1)
  (hρ₂ : ρ₂ ∈ Set.Ioo 0 1) (hρ : ρ₁ ≤ ρ₂) :
  TauCeti.Huber.IsStronglyNoetherian (TauCeti.WittVector.IntervalRing p hv hϖ hϖ' hρ₁ hρ₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WittVector.isStronglyNoetherian_intervalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.html#TauCeti.WittVector.isStronglyNoetherian_intervalRing).

## Sources

- [Tau Ceti documentation: `TauCeti.WittVector.isStronglyNoetherian_intervalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.html#TauCeti.WittVector.isStronglyNoetherian_intervalRing)
- [Source of `TauCeti.WittVector.isStronglyNoetherian_intervalRing` in TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.lean#L370)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
