---
declaration: theorem
origin: cited
lean: TopCat.Presheaf.isIso_fiberStalkMap
statement: formalized
proof: formalized
---

# TopCat.Presheaf.isIso_fiberStalkMap

For a closed map `f` from a Hausdorff space with finite fiber over `y`, the canonical map from
the stalk at `y` of the direct image of a sheaf to the product of the stalks over the fiber is an
isomorphism. This applies to proper maps with finite fibers, by `IsProperMap.isClosedMap`.

```lean
TopCat.Presheaf.isIso_fiberStalkMap.{v, u, u_1} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Limits.HasColimits C] [CategoryTheory.Limits.HasProducts C] {X Y : TopCat}
  {FC : C → C → Type u_1} {CC : C → Type v} [(X Y : C) → FunLike (FC X Y) (CC X) (CC Y)]
  [instCC : CategoryTheory.ConcreteCategory C FC]
  [CategoryTheory.Limits.PreservesFilteredColimits (CategoryTheory.forget C)]
  [CategoryTheory.Limits.HasLimits C]
  [CategoryTheory.Limits.PreservesLimits (CategoryTheory.forget C)]
  [(CategoryTheory.forget C).ReflectsIsomorphisms] [T2Space ↑X] (F : TopCat.Sheaf C X) {f : X ⟶ Y}
  (hf : IsClosedMap ⇑(CategoryTheory.ConcreteCategory.hom f)) {y : ↑Y}
  (hfin : (⇑(CategoryTheory.ConcreteCategory.hom f) ⁻¹' {y}).Finite) :
  CategoryTheory.IsIso (TopCat.Presheaf.fiberStalkMap C f F.presheaf y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.Presheaf.isIso_fiberStalkMap`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/FiberStalk.html#TopCat.Presheaf.isIso_fiberStalkMap).

## Sources

- [Tau Ceti documentation: `TopCat.Presheaf.isIso_fiberStalkMap`](https://taucetiproject.org/docs/TauCeti/Topology/Sheaves/FiberStalk.html#TopCat.Presheaf.isIso_fiberStalkMap)
- [Source of `TopCat.Presheaf.isIso_fiberStalkMap` in TauCeti/Topology/Sheaves/FiberStalk.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Sheaves/FiberStalk.lean#L253)
- [Tau Ceti roadmap status: Topological sheaf cohomology and native comparison maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TopologicalSheafCohomology/STATUS.md)
