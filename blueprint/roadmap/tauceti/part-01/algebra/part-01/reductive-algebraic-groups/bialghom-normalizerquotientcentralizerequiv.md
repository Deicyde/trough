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
- [Source of `BialgHom.normalizerQuotientCentralizerEquiv` in TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/WeylGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/DiagonalizableGroup/Normalizer/WeylGroup.lean#L104)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
