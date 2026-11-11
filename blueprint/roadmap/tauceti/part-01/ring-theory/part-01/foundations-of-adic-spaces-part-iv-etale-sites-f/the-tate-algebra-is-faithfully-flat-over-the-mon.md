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

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Monsky–Washnitzer algebras are noetherian](monsky-washnitzer-algebras-are-noetherian.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [The supremum seminorm is the spectral value of the minimal polynomial](../rigid-analytic-geometry/the-supremum-seminorm-is-the-spectral-value-of-t.md)
- [Tate algebras are unique factorisation domains](../restricted-power-series-and-tate-algebras/part-01/tate-algebras-are-unique-factorisation-domains.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](../rigid-analytic-geometry/tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.MvPowerSeries.supSeminorm_eq_norm](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-supseminorm-eq-norm.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [TauCeti.supSeminorm](../rigid-analytic-geometry/tauceti-supseminorm.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/FaithfullyFlat.html#TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/FaithfullyFlat.html#TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.faithfullyFlat_toTate` in TauCeti/RingTheory/Dagger/FaithfullyFlat.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/FaithfullyFlat.lean#L204)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
