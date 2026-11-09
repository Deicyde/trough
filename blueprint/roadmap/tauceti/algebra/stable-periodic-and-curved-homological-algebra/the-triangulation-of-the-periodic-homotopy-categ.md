---
declaration: theorem
origin: cited
lean: TauCeti.PeriodicComplex.mem_distTriang_iff
statement: formalized
proof: formalized
---

# The triangulation of the periodic homotopy category is the mapping-cone triangulation

A triangle is distinguished exactly when it is isomorphic to the image of a mapping-cone triangle
`X ⟶ Y ⟶ cone(f) ⟶ X⟦1⟧` of periodic complexes, whose last map is minus the cone projection.

```lean
TauCeti.PeriodicComplex.mem_distTriang_iff.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] {n : ℕ}
  (T : CategoryTheory.Pretriangulated.Triangle (HomotopyCategory C (ComplexShape.up (ZMod n)))) :
  T ∈ CategoryTheory.Pretriangulated.distinguishedTriangles ↔
    ∃ X Y f, Nonempty (T ≅ TauCeti.PeriodicComplex.mappingConeTriangle f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Happel's theorem](happels-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PeriodicComplex.mem_distTriang_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Periodic/Triangulated.html#TauCeti.PeriodicComplex.mem_distTriang_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.PeriodicComplex.mem_distTriang_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Periodic/Triangulated.html#TauCeti.PeriodicComplex.mem_distTriang_iff)
- [Source of `TauCeti.PeriodicComplex.mem_distTriang_iff` in TauCeti/Algebra/Homology/Periodic/Triangulated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/Periodic/Triangulated.lean#L194)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
