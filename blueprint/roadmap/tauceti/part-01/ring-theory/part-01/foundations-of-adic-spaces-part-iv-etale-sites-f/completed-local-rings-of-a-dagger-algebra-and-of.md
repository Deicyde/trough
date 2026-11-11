---
declaration: def
origin: cited
lean: TauCeti.Dagger.adicCompletionAlgEquiv
statement: formalized
---

# Completed local rings of a dagger algebra and of its completion agree

For an ideal `J` of
`A` whose radical is maximal, for instance a maximal ideal, the completion map `τ` induces an
isomorphism of the `J`-adic completion of `A` with the `J Â`-adic completion of `Â`.

```lean
TauCeti.Dagger.adicCompletionAlgEquiv.{u_1, u_2} (K : Type u_1) [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A] [Algebra K A]
  [TauCeti.Dagger.IsDaggerAlgebra K A] (J : Ideal A) [J.radical.IsMaximal] :
  AdicCompletion J A ≃ₐ[K]
    AdicCompletion (Ideal.map (TauCeti.Dagger.toCompletion K A) J) (TauCeti.Dagger.completion K A)
```

## Depends on

- [TauCeti.Dagger.completion](tauceti-dagger-completion.md)
- [TauCeti.Dagger.IsDaggerAlgebra](tauceti-dagger-isdaggeralgebra.md)

## Proof depends on

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/part-01/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Monsky–Washnitzer algebras are noetherian](monsky-washnitzer-algebras-are-noetherian.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/part-01/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [The supremum seminorm is the spectral value of the minimal polynomial](../rigid-analytic-geometry/the-supremum-seminorm-is-the-spectral-value-of-t.md)
- [Tate algebras are unique factorisation domains](../restricted-power-series-and-tate-algebras/part-01/tate-algebras-are-unique-factorisation-domains.md)
- [TauCeti.Dagger.faithfullyFlat_toCompletion](tauceti-dagger-faithfullyflat-tocompletion.md)
- [TauCeti.IsAffinoidAlgebra.continuous_algHom](../rigid-analytic-geometry/tauceti-isaffinoidalgebra-continuous-alghom.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/part-01/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.MvPowerSeries.supSeminorm_eq_norm](../restricted-power-series-and-tate-algebras/part-01/tauceti-mvpowerseries-supseminorm-eq-norm.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/part-01/tauceti-powerseries-ismuldistinguished.md)
- [TauCeti.supSeminorm](../rigid-analytic-geometry/tauceti-supseminorm.md)
- [The Weierstrass division estimate for a multiplicatively distinguished divisor](../restricted-power-series-and-tate-algebras/part-01/the-weierstrass-division-estimate-for-a-multipli.md)
- [The Weierstrass division identity](../power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.adicCompletionAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.html#TauCeti.Dagger.adicCompletionAlgEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.adicCompletionAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.html#TauCeti.Dagger.adicCompletionAlgEquiv)
- [Source of `TauCeti.Dagger.adicCompletionAlgEquiv` in TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.lean#L219)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
