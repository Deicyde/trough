---
declaration: def
origin: cited
lean: TauCeti.FiniteEtaleScheme.galoisEquivalence
statement: formalized
---

# Galois theory for finite étale schemes over a field

For a separable closure `Ω` of `K`,
finite étale `K`-schemes are equivalent to finite sets with a continuous action of `Gal(Ω/K)`.
A finite étale scheme `Spec A` goes to the set of `Ω`-valued points of `A`
(`specCompGaloisEquivalenceFunctorIso`).

```lean
TauCeti.FiniteEtaleScheme.galoisEquivalence.{u} (K Ω : Type u) [Field K] [Field Ω] [Algebra K Ω]
  [IsSepClosed Ω] [IsGalois K Ω] :
  TauCeti.FiniteEtaleScheme (AlgebraicGeometry.Spec ↧K) ≌ ContAction FintypeCat Gal(Ω/K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.galoisEquivalence`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.html#TauCeti.FiniteEtaleScheme.galoisEquivalence).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.galoisEquivalence`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.html#TauCeti.FiniteEtaleScheme.galoisEquivalence)
- [Source of `TauCeti.FiniteEtaleScheme.galoisEquivalence` in TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.lean#L91)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
