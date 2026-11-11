---
declaration: def
origin: cited
lean: CategoryTheory.Functor.mapDoubleRightDualIso
statement: formalized
---

# CategoryTheory.Functor.mapDoubleRightDualIso

The bidual comparison `κ_X : F.obj Xᘁᘁ ≅ (F.obj X)ᘁᘁ` of a strong monoidal functor between
right rigid categories: the comparison `δ_{Xᘁ} : F.obj Xᘁᘁ ≅ (F.obj Xᘁ)ᘁ`, followed by the
inverse of the right dual `(δ_X)ᘁ : (F.obj X)ᘁᘁ ≅ (F.obj Xᘁ)ᘁ` of `δ_X : F.obj Xᘁ ≅ (F.obj X)ᘁ`.

```lean
CategoryTheory.Functor.mapDoubleRightDualIso.{v₁, v₂, u₁, u₂} {C : Type u₁}
  [CategoryTheory.Category.{v₁, u₁} C] [CategoryTheory.MonoidalCategory C] {D : Type u₂}
  [CategoryTheory.Category.{v₂, u₂} D] [CategoryTheory.MonoidalCategory D]
  [CategoryTheory.RightRigidCategory C] [CategoryTheory.RightRigidCategory D]
  (F : CategoryTheory.Functor C D) [F.Monoidal] (X : C) : F.obj Xᘁᘁ ≅ (F.obj X)ᘁᘁ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.mapDoubleRightDualIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Functor.html#CategoryTheory.Functor.mapDoubleRightDualIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.mapDoubleRightDualIso`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Rigid/Functor.html#CategoryTheory.Functor.mapDoubleRightDualIso)
- [Source of `CategoryTheory.Functor.mapDoubleRightDualIso` in TauCeti/CategoryTheory/Monoidal/Rigid/Functor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Rigid/Functor.lean#L408)
- [Tau Ceti roadmap status: Diagrammatic coherence for monoidal categories and duality](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiagrammaticCoherence/STATUS.md)
