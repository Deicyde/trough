---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate
statement: formalized
proof: formalized
---

# The Tate algebra is faithfully flat over the Monsky–Washnitzer algebra

```lean
TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate.{u_1, u_2} {K : Type u_1} {σ : Type u_2}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] [Finite σ] :
  (TauCeti.Dagger.washnitzerAlgebra.toTate σ K).FaithfullyFlat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Monsky–Washnitzer algebras are noetherian](monsky-washnitzer-algebras-are-noetherian.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [Power-bounded elements of an affinoid algebra](../rigid-analytic-geometry/power-bounded-elements-of-an-affinoid-algebra.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/FaithfullyFlat.html#TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/FaithfullyFlat.html#TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate` in TauCeti/RingTheory/Dagger/FaithfullyFlat.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/FaithfullyFlat.lean#L204)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
