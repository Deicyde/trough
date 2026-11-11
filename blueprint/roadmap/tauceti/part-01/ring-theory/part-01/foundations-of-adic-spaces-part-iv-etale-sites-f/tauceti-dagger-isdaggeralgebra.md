---
declaration: class
origin: cited
lean: TauCeti.Dagger.IsDaggerAlgebra
statement: formalized
---

# TauCeti.Dagger.IsDaggerAlgebra

A `K`-**dagger algebra** is a commutative `K`-algebra which is a quotient of the
Monsky–Washnitzer algebra `W_n = K⟨X₁, …, Xₙ⟩†` for some `n`.

```lean
TauCeti.Dagger.IsDaggerAlgebra.{u_1, u_2} (K : Type u_1) [NormedField K] [IsUltrametricDist K]
  (A : Type u_2) [CommRing A] [Algebra K A] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.IsDaggerAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra.html#TauCeti.Dagger.IsDaggerAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.IsDaggerAlgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra.html#TauCeti.Dagger.IsDaggerAlgebra)
- [Source of `TauCeti.Dagger.IsDaggerAlgebra` in TauCeti/RingTheory/Dagger/DaggerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Dagger/DaggerAlgebra.lean#L63)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
