---
declaration: def
origin: cited
lean: CategoryTheory.Functor.mapDoubleRightDualNatIso
statement: formalized
---

# CategoryTheory.Functor.mapDoubleRightDualNatIso

The bidual comparisons of a strong monoidal functor `F` between right rigid categories, as a
natural isomorphism `doubleRightDualFunctor C ⋙ F ≅ F ⋙ doubleRightDualFunctor D`.

```lean
CategoryTheory.Functor.mapDoubleRightDualNatIso.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.MonoidalCategory C] {D : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.RightRigidCategory C] [CategoryTheory.RightRigidCategory D]
  (F : CategoryTheory.Functor C D) [F.Monoidal] :
  (TauCeti.doubleRightDualFunctor C).comp F ≅ F.comp (TauCeti.doubleRightDualFunctor D)
```

## Depends on

- [CategoryTheory.Functor.mapDoubleRightDualIso](categorytheory-functor-mapdoublerightdualiso.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.mapDoubleRightDualNatIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Functor.html#CategoryTheory.Functor.mapDoubleRightDualNatIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.mapDoubleRightDualNatIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Functor.html#CategoryTheory.Functor.mapDoubleRightDualNatIso)
- [Source of `CategoryTheory.Functor.mapDoubleRightDualNatIso` in TauCeti/CategoryTheory/Monoidal/Rigid/Functor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Rigid/Functor.lean#L488)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
