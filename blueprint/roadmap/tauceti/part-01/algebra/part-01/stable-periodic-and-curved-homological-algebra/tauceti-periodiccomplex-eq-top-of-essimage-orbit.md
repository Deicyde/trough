---
declaration: theorem
origin: cited
lean: TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le
statement: formalized
proof: formalized
---

# TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le

The essential image of the derived orbit functor generates the periodic derived category
under shifts and cones alone. No closure under retracts is required.

```lean
TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] {n : ℕ} [NeZero n]
  [HasDerivedCategory C] [CategoryTheory.EnoughProjectives C] (d : ℕ)
  (hd : ∀ (X : C), CategoryTheory.HasProjectiveDimensionLT X d)
  (P : CategoryTheory.ObjectProperty (TauCeti.PeriodicComplex.DerivedCategory C n))
  [P.IsTriangulated] [P.IsClosedUnderIsomorphisms]
  (hP : (TauCeti.PeriodicComplex.orbitDerivedCompressionFunctor n).essImage ≤ P) : P = ⊤
```

## Depends on

- [TauCeti.OrbitCategory.lift](tauceti-orbitcategory-lift.md)

## Proof depends on

- [Happel's theorem](happels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Periodic/Compression/Generation.html#TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Periodic/Compression/Generation.html#TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le)
- [Source of `TauCeti.PeriodicComplex.eq_top_of_essImage_orbitDerivedCompressionFunctor_le` in TauCeti/Algebra/Homology/Periodic/Compression/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/Periodic/Compression/Generation.lean#L107)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
