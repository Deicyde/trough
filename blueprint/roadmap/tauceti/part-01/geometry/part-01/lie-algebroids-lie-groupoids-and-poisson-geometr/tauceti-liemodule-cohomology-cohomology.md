---
declaration: abbrev
origin: cited
lean: TauCeti.LieModule.Cohomology.cohomology
statement: formalized
---

# TauCeti.LieModule.Cohomology.cohomology

The `n`-th Lie algebra cohomology of `L` with coefficients in `M`, the homology of the
Chevalley–Eilenberg complex in degree `n`.

```lean
TauCeti.LieModule.Cohomology.cohomology.{u_1, u_2, u_3} (R : Type u_1) [CommRing R] (L : Type u_2)
  [LieRing L] [LieAlgebra R L] (M : Type u_3) [AddCommGroup M] [_root_.Module R M]
  [LieRingModule L M] [LieModule R L M] (n : ℕ) : ModuleCat R
```

## Depends on

- [TauCeti.LieModule.Cohomology.cochainComplex](tauceti-liemodule-cohomology-cochaincomplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.cohomology`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.cohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.cohomology`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.cohomology)
- [Source of `TauCeti.LieModule.Cohomology.cohomology` in TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean#L299)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
