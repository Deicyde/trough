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

- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Kedlaya's Hilbert basis theorem for restricted power series](../restricted-power-series-and-tate-algebras/kedlayas-hilbert-basis-theorem-for-restricted-po.md)
- [Monsky–Washnitzer algebras are noetherian](monsky-washnitzer-algebras-are-noetherian.md)
- [Neumann series criterion (`MvPowerSeries.isNormMulUnit_of_norm_sub_C_lt`)](../restricted-power-series-and-tate-algebras/neumann-series-criterion-mvpowerseries-isnormmul.md)
- [The open mapping theorem over a Tate ring](../../../algebraic-geometry/foundations-of-adic-spaces/the-open-mapping-theorem-over-a-tate-ring.md)
- [Power-bounded elements of an affinoid algebra](../rigid-analytic-geometry/power-bounded-elements-of-an-affinoid-algebra.md)
- [TauCeti.Dagger.faithfullyFlat_toCompletion](tauceti-dagger-faithfullyflat-tocompletion.md)
- [TauCeti.IsNormMulUnit](../restricted-power-series-and-tate-algebras/tauceti-isnormmulunit.md)
- [TauCeti.MvPowerSeries.IsRestrictedFamily](../restricted-power-series-and-tate-algebras/tauceti-mvpowerseries-isrestrictedfamily.md)
- [TauCeti.PowerSeries.IsMulDistinguished](../restricted-power-series-and-tate-algebras/tauceti-powerseries-ismuldistinguished.md)
- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../restricted-power-series-and-tate-algebras/the-weierstrass-division-estimate-bosch-guntzer.md)
- [The Weierstrass division identity](../../part-02/power-series/the-weierstrass-division-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.adicCompletionAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.html#TauCeti.Dagger.adicCompletionAlgEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.adicCompletionAlgEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.html#TauCeti.Dagger.adicCompletionAlgEquiv)
- [Source of `TauCeti.Dagger.adicCompletionAlgEquiv` in TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.lean#L218)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
