---
declaration: def
origin: cited
lean: TauCeti.FiniteEtaleScheme.fiber
statement: formalized
---

# TauCeti.FiniteEtaleScheme.fiber

The geometric fibre functor at a geometric point `x : Spec Ω ⟶ S`, for `Ω` separably
closed: a finite étale `S`-scheme `X` goes to the finite set classifying `X ×_S Spec Ω`.

```lean
TauCeti.FiniteEtaleScheme.fiber.{u} {S : AlgebraicGeometry.Scheme} {Ω : Type u} [Field Ω]
  [IsSepClosed Ω] (x : AlgebraicGeometry.Spec ↧Ω ⟶ S) :
  CategoryTheory.Functor (TauCeti.FiniteEtaleScheme S) FintypeCat
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.fiber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Fiber.html#TauCeti.FiniteEtaleScheme.fiber).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.fiber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Fiber.html#TauCeti.FiniteEtaleScheme.fiber)
- [Source of `TauCeti.FiniteEtaleScheme.fiber` in TauCeti/AlgebraicGeometry/FiniteEtale/Fiber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/FiniteEtale/Fiber.lean#L145)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
