---
declaration: theorem
origin: cited
lean: TauCeti.LieModule.Cohomology.d₂₃_twoCochainEquiv
statement: formalized
proof: formalized
---

# TauCeti.LieModule.Cohomology.d₂₃_twoCochainEquiv

In degree two, the differential is Mathlib's `d₂₃`, which takes values in all trilinear
maps.

```lean
TauCeti.LieModule.Cohomology.d₂₃_twoCochainEquiv.{u_1, u_2, u_3} {R : Type u_1} [CommRing R]
  {L : Type u_2} [LieRing L] [LieAlgebra R L] {M : Type u_3} [AddCommGroup M] [_root_.Module R M]
  [LieRingModule L M] [LieModule R L M] (ω : L [⋀^Fin 2]→ₗ[R] M) (x y z : L) :
  ((((LieModule.Cohomology.d₂₃ R L M) ((TauCeti.LieModule.Cohomology.twoCochainEquiv R L M) ω)) x)
        y)
      z =
    ((TauCeti.LieModule.Cohomology.d R L M 2) ω) ![x, y, z]
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Chevalley–Eilenberg formula for the differential of a cochain of positive degree](the-chevalley-eilenberg-formula-for-the-differen.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.d₂₃_twoCochainEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.d%E2%82%82%E2%82%83_twoCochainEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.d₂₃_twoCochainEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.d%E2%82%82%E2%82%83_twoCochainEquiv)
- [Source of `TauCeti.LieModule.Cohomology.d₂₃_twoCochainEquiv` in TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean#L379)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
