---
declaration: theorem
origin: cited
lean: TauCeti.WittVector.isStronglyNoetherian_intervalRing
statement: formalized
proof: formalized
---

# The interval ring `B^I` is strongly noetherian

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

## Proof depends on

- [Kedlaya's estimate (4.9.1) in the normalisation `λ_ρ(p) = ρ`](../../ring-theory/part-02/other-results/part-02/kedlayas-estimate-4-9-1-in-the-normalisation-p.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WittVector.isStronglyNoetherian_intervalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.html#TauCeti.WittVector.isStronglyNoetherian_intervalRing).

## Sources

- [Tau Ceti documentation: `TauCeti.WittVector.isStronglyNoetherian_intervalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.html#TauCeti.WittVector.isStronglyNoetherian_intervalRing)
- [Source of `TauCeti.WittVector.isStronglyNoetherian_intervalRing` in TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/WittVector/IntervalRing/StronglyNoetherian.lean#L423)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
