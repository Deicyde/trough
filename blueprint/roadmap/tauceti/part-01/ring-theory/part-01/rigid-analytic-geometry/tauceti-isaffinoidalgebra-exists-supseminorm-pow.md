---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm
statement: formalized
proof: formalized
---

# TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm

A single positive exponent, depending only on the affinoid algebra, sends every
supremum seminorm into the value group of the base field (with zero included).

```lean
TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm.{u_1, u_2} {K : Type u_1}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A]
  [Algebra K A] (hA : TauCeti.IsAffinoidAlgebra K A) :
  ∃ m, 1 ≤ m ∧ ∀ (f : A), ∃ c, TauCeti.supSeminorm K f ^ m = ‖c‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Affinoid Noether normalisation](affinoid-noether-normalisation.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Maximum modulus principle for Tate algebras](../restricted-power-series-and-tate-algebras/maximum-modulus-principle-for-tate-algebras.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [Tate algebras are unique factorisation domains](../restricted-power-series-and-tate-algebras/tate-algebras-are-unique-factorisation-domains.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/ValueGroup.html#TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/ValueGroup.html#TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm)
- [Source of `TauCeti.IsAffinoidAlgebra.exists_supSeminorm_pow_eq_norm` in TauCeti/RingTheory/Affinoid/ValueGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/ValueGroup.lean#L77)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
