---
declaration: abbrev
origin: cited
lean: TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory
statement: formalized
---

# TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory

The **absolute derived category** of curved right modules: the Verdier quotient of the
curved homotopy category by the absolutely acyclic objects.

```lean
TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory.{u} (R : Type u) {A : Type u} [CommRing R]
  [Ring A] [Algebra R A] {𝒜 : ℤ → Submodule R A} [GradedAlgebra 𝒜] {d : A →ₗ[R] A} {w : A}
  (h : TauCeti.IsCurvedDGAlgebra 𝒜 d w) : Type (u + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Happel's theorem](happels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Curved/Module/Right/SecondKind.html#TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory).

## Sources

- [Tau Ceti documentation: `TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Curved/Module/Right/SecondKind.html#TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory)
- [Source of `TauCeti.CurvedDGRightModuleCat.AbsoluteDerivedCategory` in TauCeti/Algebra/Homology/Curved/Module/Right/SecondKind.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/Curved/Module/Right/SecondKind.lean#L71)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
