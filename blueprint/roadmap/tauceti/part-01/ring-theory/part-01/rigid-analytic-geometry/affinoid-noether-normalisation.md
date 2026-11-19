---
declaration: theorem
origin: cited
lean: TauCeti.IsAffinoidAlgebra.exists_finite_injective
statement: formalized
proof: formalized
---

# Affinoid Noether normalisation

Every nonzero affinoid algebra over a complete
ultrametric field is finite over an injectively embedded finite-variable Tate algebra.
Finiteness uses the algebra structure induced by the displayed map.

```lean
TauCeti.IsAffinoidAlgebra.exists_finite_injective.{u, u_1} {K : Type u} [NormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {A : Type u_1} [CommRing A] [Algebra K A] [Nontrivial A]
  (hA : TauCeti.IsAffinoidAlgebra K A) : ∃ n g, Function.Injective ⇑g ∧ g.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAffinoidAlgebra.exists_finite_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/NoetherNormalization.html#TauCeti.IsAffinoidAlgebra.exists_finite_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.IsAffinoidAlgebra.exists_finite_injective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/NoetherNormalization.html#TauCeti.IsAffinoidAlgebra.exists_finite_injective)
- [Source of `TauCeti.IsAffinoidAlgebra.exists_finite_injective` in TauCeti/RingTheory/Affinoid/NoetherNormalization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/NoetherNormalization.lean#L160)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
