---
declaration: theorem
origin: cited
lean: TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra
statement: formalized
proof: formalized
---

# The adic spectrum of a classical affinoid algebra is an affinoid adic space

Let `K` be a
complete nonarchimedean field with a nontrivial absolute value and `B` a quotient of a Tate algebra
`K⟨X₁, …, Xₙ⟩`, carrying a complete ultrametric algebra norm, for instance the quotient Gauss norm.
Then for any pair of definition `P` of `B` and any plus ring `B⁺` of power-bounded elements
containing its ring of definition, such as `B°`, `Spa(B, B⁺)` is an affinoid adic space.

```lean
TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra.{u, u_1}
  {K : Type u_1} [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {B : Type u}
  [NormedCommRing B] [NormedAlgebra K B] [IsUltrametricDist B] [CompleteSpace B]
  (P : TauCeti.Huber.PairOfDefinition B) {Bplus : Subring B} (hB : TauCeti.IsAffinoidAlgebra K B)
  (hP : P.ringOfDefinition ≤ Bplus)
  (hBplus : ∀ ⦃b : B⦄, b ∈ Bplus → TauCeti.Huber.IsPowerBounded b) :
  (TauCeti.ValuationSpectrum.presentationLimitPreAdicSpace P Bplus hBplus hP).isAdic
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](adic-spaces-wedhorn-definition-8-22.md)

## Proof depends on

- [A finite module over a complete noetherian Tate ring has a strict finite presentation](a-finite-module-over-a-complete-noetherian-tate.md)
- [A rational localisation of a strongly noetherian Tate ring is strongly noetherian](a-rational-localisation-of-a-strongly-noetherian.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Henkel's open mapping theorem](../../../part-02/topology/algebra/part-01/henkels-open-mapping-theorem.md)
- [Henkel's theorem in quotient form](../../../part-02/topology/algebra/part-01/henkels-theorem-in-quotient-form.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The open mapping theorem over a Tate ring](the-open-mapping-theorem-over-a-tate-ring.md)
- [Strong noetherianness passes to an algebra topologically of finite type over a Tate ring](strong-noetherianness-passes-to-an-algebra-topol.md)
- [TauCeti.IsNormMulUnit](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../../ring-theory/part-01/restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../ring-theory/part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.html#TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.html#TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra)
- [Source of `TauCeti.ValuationSpectrum.isAdic_presentationLimitPreAdicSpace_of_isAffinoidAlgebra` in TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/AdicSpace/PreAdicSpace/StronglyNoetherian.lean#L110)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/AdicSpaces/STATUS.md)
