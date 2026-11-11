---
declaration: structure
origin: cited
lean: TauCeti.Dagger.FringePresentation
statement: formalized
---

# TauCeti.Dagger.FringePresentation

A **fringe presentation** of a `K`-algebra `A`: relations `f₁, …, f_r` in `n` variables, all
restricted at one radius `ρ₀ > 1`, together with an isomorphism from the quotient of the
Monsky–Washnitzer algebra `W_n` by the ideal they generate onto `A`.

```lean
TauCeti.Dagger.FringePresentation.{u_1, u_2} (K : Type u_1) [NormedField K] [IsUltrametricDist K]
  (A : Type u_2) [CommRing A] [Algebra K A] : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.FringePresentation`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/FringePresentation/Basic.html#TauCeti.Dagger.FringePresentation).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.FringePresentation`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/FringePresentation/Basic.html#TauCeti.Dagger.FringePresentation)
- [Source of `TauCeti.Dagger.FringePresentation` in TauCeti/RingTheory/Dagger/FringePresentation/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/FringePresentation/Basic.lean#L86)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
