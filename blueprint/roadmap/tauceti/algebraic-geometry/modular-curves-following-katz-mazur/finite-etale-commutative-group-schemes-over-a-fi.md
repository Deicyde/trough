---
declaration: def
origin: cited
lean: TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp
statement: formalized
---

# Finite étale commutative group schemes over a field are finite Galois modules

Commutative group objects in finite étale `K`-schemes are equivalent to commutative group objects
in finite continuous `Gal(Ω/K)`-sets, that is, to finite abelian groups with a continuous action
of `Gal(Ω/K)` by group automorphisms.

```lean
TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp.{u} (K Ω : Type u) [Field K] [Field Ω]
  [Algebra K Ω] [IsSepClosed Ω] [IsGalois K Ω] :
  CategoryTheory.CommGrp (TauCeti.FiniteEtaleScheme (AlgebraicGeometry.Spec ↧K)) ≌
    CategoryTheory.CommGrp (ContAction FintypeCat Gal(Ω/K))
```

## Depends on

- [Galois theory for finite étale schemes over a field](galois-theory-for-finite-etale-schemes-over-a-fi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.html#TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.html#TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp)
- [Source of `TauCeti.FiniteEtaleScheme.galoisEquivalenceCommGrp` in TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Basic.lean#L196)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
