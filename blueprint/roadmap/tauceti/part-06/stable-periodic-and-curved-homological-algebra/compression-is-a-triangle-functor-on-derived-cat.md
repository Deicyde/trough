---
declaration: theorem
origin: cited
lean: TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor
statement: formalized
proof: formalized
---

# Compression is a triangle functor on derived categories

```lean
TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor.{w, v, u}
  {C : Type u} [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] (n : ℕ)
  [HasDerivedCategory C] : (TauCeti.PeriodicComplex.derivedCompressionFunctor n).IsTriangulated
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Happel's theorem](happels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Periodic/Compression/Derived.html#TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Periodic/Compression/Derived.html#TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor)
- [Source of `TauCeti.PeriodicComplex.instIsTriangulatedBoundedDerivedCategoryDerivedCompressionFunctor` in TauCeti/Algebra/Homology/Periodic/Compression/Derived.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/Periodic/Compression/Derived.lean#L133)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
