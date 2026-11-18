---
declaration: abbrev
origin: cited
lean: TauCeti.LaurentTriangulatedK0
statement: formalized
---

# Graded triangulated `K₀` over the Laurent coefficient ring

The underlying group is the
triangulated Grothendieck group of `C`, and the Laurent variable `q` acts by the automorphism
`[M] ↦ [M{1}]` induced by the grading shift `e`.  Use
`TauCeti.LaurentTriangulatedK0.ofTriangulatedK0` to move between the two views.

```lean
TauCeti.LaurentTriangulatedK0.{w, v, u} (C : Type u) [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.HasShift C ℤ] [∀ (n : ℤ), (CategoryTheory.shiftFunctor C n).Additive]
  [CategoryTheory.Pretriangulated C] [CategoryTheory.EssentiallySmall.{w, v, u} C] (e : C ≌ C)
  [e.functor.CommShift ℤ] [e.functor.IsTriangulated] : Type w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentTriangulatedK0`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Triangulated.html#TauCeti.LaurentTriangulatedK0).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentTriangulatedK0`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Triangulated.html#TauCeti.LaurentTriangulatedK0)
- [Source of `TauCeti.LaurentTriangulatedK0` in TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Triangulated.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/GrothendieckGroup/Laurent/Triangulated.lean#L89)
- [Tau Ceti roadmap status: Grothendieck groups, Cartan maps, and Euler forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GrothendieckEulerForms/STATUS.md)
