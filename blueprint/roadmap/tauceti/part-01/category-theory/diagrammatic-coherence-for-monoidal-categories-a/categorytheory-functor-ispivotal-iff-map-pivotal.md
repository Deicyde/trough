---
declaration: theorem
origin: cited
lean: CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom
statement: formalized
proof: formalized
---

# CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom

A monoidal functor is pivotal if and only if it carries `φ_X` to `φ_{F X}` along the bidual
comparison `κ_X : F.obj Xᘁᘁ ≅ (F.obj X)ᘁᘁ`, that is, `F.map φ_X ≫ κ_X = φ_{F X}` for every `X`.

```lean
CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom.{v_1, u_1,
    v_2, u_2}
  {C : Type u_1} [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.MonoidalCategory C]
  {D : Type u_2} [CategoryTheory.Category.{v_2, u_2} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C] [CategoryTheory.RigidCategory D]
  [TauCeti.PivotalCategory D] {F : CategoryTheory.Functor C D} [F.Monoidal] :
  F.IsPivotal ↔
    ∀ (X : C),
      CategoryTheory.CategoryStruct.comp (F.map (TauCeti.pivotalIsoApp X).hom)
          (F.mapDoubleRightDualIso X).hom =
        (TauCeti.pivotalIsoApp (F.obj X)).hom
```

## Depends on

- [CategoryTheory.Functor.mapDoubleRightDualIso](categorytheory-functor-mapdoublerightdualiso.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.html#CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.html#CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom)
- [Source of `CategoryTheory.Functor.isPivotal_iff_map_pivotalIsoApp_hom_comp_mapDoubleRightDualIso_hom` in TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Pivotal/Functor/Basic.lean#L101)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
