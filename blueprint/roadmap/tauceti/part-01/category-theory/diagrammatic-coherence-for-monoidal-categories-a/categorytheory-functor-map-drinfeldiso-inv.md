---
declaration: theorem
origin: cited
lean: CategoryTheory.Functor.map_drinfeldIso_inv
statement: formalized
proof: formalized
---

# CategoryTheory.Functor.map_drinfeldIso_inv

A braided functor carries the inverse Drinfeld isomorphism of `X` to that of `F.obj X`, after
the bidual comparison: `F.map u_X⁻¹ = κ_X ≫ u_{F X}⁻¹`.

```lean
CategoryTheory.Functor.map_drinfeldIso_inv.{v_1, u_1, v_2, u_2} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.MonoidalCategory C] {D : Type u_2}
  [CategoryTheory.Category.{v_2, u_2} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.BraidedCategory C] [CategoryTheory.RightRigidCategory C]
  [CategoryTheory.BraidedCategory D] [CategoryTheory.RightRigidCategory D]
  (F : CategoryTheory.Functor C D) [F.Braided] (X : C) :
  F.map (TauCeti.drinfeldIso X).inv =
    CategoryTheory.CategoryStruct.comp (F.mapDoubleRightDualIso X).hom
      (TauCeti.drinfeldIso (F.obj X)).inv
```

## Depends on

- [CategoryTheory.Functor.mapDoubleRightDualIso](categorytheory-functor-mapdoublerightdualiso.md)

## Proof depends on

- [CategoryTheory.Functor.map_drinfeldIso_hom_comp_mapDoubleRightDualIso_hom](categorytheory-functor-map-drinfeldiso-hom-comp.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.map_drinfeldIso_inv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.html#CategoryTheory.Functor.map_drinfeldIso_inv).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.map_drinfeldIso_inv`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.html#CategoryTheory.Functor.map_drinfeldIso_inv)
- [Source of `CategoryTheory.Functor.map_drinfeldIso_inv` in TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.lean#L204)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
