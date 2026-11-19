---
declaration: def
origin: cited
lean: BialgHom.normalizerQuotientCentralizerEquiv
statement: formalized
---

# BialgHom.normalizerQuotientCentralizerEquiv

The rational normalizer modulo the rational centralizer is the Weyl group.

```lean
BialgHom.normalizerQuotientCentralizerEquiv.{u, v, w} {R : Type u} {H : Type v} {X : Type w}
  [CommRing R] [CommRing H] [HopfAlgebra R H] [CommGroup X] [ConnectedSpace (PrimeSpectrum R)]
  (π : H →ₐc[R] MonoidAlgebra R X) (hπ : Function.Surjective ⇑π) :
  ↥(π.normalizerPoints hπ) ⧸ (π.centralizerPointsSubgroup ↧R).subgroupOf (π.normalizerPoints hπ) ≃*
    ↥(π.weylGroup hπ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`BialgHom.normalizerQuotientCentralizerEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/WeylGroup.html#BialgHom.normalizerQuotientCentralizerEquiv).

## Sources

- [Tau Ceti documentation: `BialgHom.normalizerQuotientCentralizerEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/WeylGroup.html#BialgHom.normalizerQuotientCentralizerEquiv)
- [Source of `BialgHom.normalizerQuotientCentralizerEquiv` in TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/WeylGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/WeylGroup.lean#L104)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
