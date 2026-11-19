---
declaration: def
origin: cited
lean: TauCeti.RationalFraction.completionLocEquiv
statement: formalized
---

# `A⟨f/g⟩` is the Huber rational localisation `A⟨T/g⟩`

**`A⟨f/g⟩` is the Huber rational localisation `A⟨T/g⟩`** for the numerators
`T = {g, f₁, …, fₘ}` ([Wedhorn, *Adic Spaces*][wedhorn_adic], Example 6.38): when `g, f₁, …, fₘ`
generate the unit ideal of the affinoid algebra `A`, the rational fraction algebra is isomorphic to
the completion of the localisation `S = A[1/g]` for its Huber topology. The isomorphism is the
structure map on `A` (`completionLocEquiv_algebraMap`), sends `fᵢ/g` to the fraction `fᵢ/g` of `S`
(`completionLocEquiv_ratio`; the inverse forms are `completionLocEquiv_symm_toCompletionLoc`,
`completionLocEquiv_symm_coe_divBy` and `completionLocEquiv_symm_coe`), and is a homeomorphism
(`continuous_completionLocEquiv` and `continuous_completionLocEquiv_symm`).

The standing hypothesis `hden` of the Huber construction always holds here, by
`TauCeti.Huber.PairOfDefinition.hasDenominatorPower_of_isOpen_span`, because the numerators span
the unit ideal; it is an argument because the topology of `A[1/g]` is stated in terms of it.

```lean
TauCeti.RationalFraction.completionLocEquiv.{u_1, u_2, u_4} {A : Type u_1} [NormedCommRing A]
  [IsUltrametricDist A] {m : ℕ} {g : A} {f : Fin m → A} {K : Type u_2} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] [NormedAlgebra K A] [CompleteSpace A]
  (hA : TauCeti.IsAffinoidAlgebra K A) (P : TauCeti.Huber.PairOfDefinition A) (S : Type u_4)
  [CommRing S] [Algebra A S] [IsLocalization.Away g S]
  (hden : P.HasDenominatorPower (insert g (Set.range f)) g S)
  (h : Ideal.span (insert g (Set.range f)) = ⊤) :
  TauCeti.RationalFraction g f ≃+* UniformSpace.Completion S
```

## Depends on

- [The rational fraction algebra `A⟨f/g⟩ = A⟨X₁, …, Xₘ⟩ ⧸ (g Xᵢ - fᵢ)`](the-rational-fraction-algebra-af-g-ax1-xm-g-xi-f.md)

## Proof depends on

- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [Strong noetherianness passes to an algebra topologically of finite type over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/strong-noetherianness-passes-to-an-algebra-topol.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RationalFraction.completionLocEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/RationalFraction.html#TauCeti.RationalFraction.completionLocEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.RationalFraction.completionLocEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/RationalFraction.html#TauCeti.RationalFraction.completionLocEquiv)
- [Source of `TauCeti.RationalFraction.completionLocEquiv` in TauCeti/RingTheory/Affinoid/RationalFraction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/RationalFraction.lean#L314)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
