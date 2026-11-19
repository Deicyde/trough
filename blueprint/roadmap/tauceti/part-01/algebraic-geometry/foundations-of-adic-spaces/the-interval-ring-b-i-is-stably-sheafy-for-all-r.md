---
declaration: theorem
origin: cited
lean: TauCeti.WittVector.isStablySheafyRing_intervalRing
statement: formalized
proof: formalized
---

# The interval ring `B^I` is stably sheafy for all radii `0 < ρ₁ ≤ ρ₂ < 1`

every complete
Hausdorff Huber ring topologically of finite type over `B^I` is sheafy. The ring `B^I` is a
complete Hausdorff Tate ring that is strongly noetherian by Kedlaya's Theorem 4.10
(`TauCeti.WittVector.isStronglyNoetherian_intervalRing`), so this is Wedhorn's Corollary 8.35
(`TauCeti.Huber.isStablySheafyRing_of_isStronglyNoetherian`). In particular `B^I` is sheafy
(`TauCeti.Huber.IsStablySheafyRing.isSheafyRing`).

```lean
TauCeti.WittVector.isStablySheafyRing_intervalRing.{u, w, u_1} (p : ℕ) [Fact (Nat.Prime p)]
  {O : Type u} [CommRing O] {ϖ : O} {K : Type u_1} [Field K] [Algebra O K] {v : Valuation K NNReal}
  [CharP O p] [PerfectRing O p] (hv : v.Integers O) (hϖ : ϖ ≠ 0) (hϖ' : v ((algebraMap O K) ϖ) < 1)
  {ρ₁ ρ₂ : NNReal} (hρ₁ : ρ₁ ∈ Set.Ioo 0 1) (hρ₂ : ρ₂ ∈ Set.Ioo 0 1) (hρ : ρ₁ ≤ ρ₂) :
  TauCeti.Huber.IsStablySheafyRing (TauCeti.WittVector.IntervalRing p hv hϖ hϖ' hρ₁ hρ₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A finite module over a complete noetherian Tate ring has a strict finite presentation](a-finite-module-over-a-complete-noetherian-tate.md)
- [A rational localisation of a strongly noetherian Tate ring is strongly noetherian](a-rational-localisation-of-a-strongly-noetherian.md)
- [Henkel's open mapping theorem](../../../part-02/topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [Henkel's theorem in quotient form](../../../part-02/topology/algebra/part-01/henkels-theorem-in-quotient-form.md)
- [The interval ring `B^I` is strongly noetherian](the-interval-ring-b-i-is-strongly-noetherian.md)
- [The open mapping theorem over a Tate ring](the-open-mapping-theorem-over-a-tate-ring.md)
- [Strong noetherianness passes to an algebra topologically of finite type over a Tate ring](strong-noetherianness-passes-to-an-algebra-topol.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.WittVector.isStablySheafyRing_intervalRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/IntervalChart.html#TauCeti.WittVector.isStablySheafyRing_intervalRing).

## Sources

- [Tau Ceti documentation: `TauCeti.WittVector.isStablySheafyRing_intervalRing`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/IntervalChart.html#TauCeti.WittVector.isStablySheafyRing_intervalRing)
- [Source of `TauCeti.WittVector.isStablySheafyRing_intervalRing` in TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/IntervalChart.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/IntervalChart.lean#L170)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
