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
- [Source of `TauCeti.Dagger.IsDaggerAlgebra` in TauCeti/RingTheory/Dagger/DaggerAlgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/DaggerAlgebra.lean#L63)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
