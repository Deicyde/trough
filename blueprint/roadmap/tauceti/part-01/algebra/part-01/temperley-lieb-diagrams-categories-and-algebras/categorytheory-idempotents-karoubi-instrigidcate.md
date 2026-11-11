---
declaration: instance
origin: cited
lean: CategoryTheory.Idempotents.Karoubi.instRigidCategory
statement: formalized
---

# CategoryTheory.Idempotents.Karoubi.instRigidCategory

The idempotent completion of a rigid monoidal category is rigid.

```lean
CategoryTheory.Idempotents.Karoubi.instRigidCategory.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.RigidCategory C] :
  CategoryTheory.RigidCategory (CategoryTheory.Idempotents.Karoubi C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Idempotents.Karoubi.instRigidCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Karoubi/Rigid.html#CategoryTheory.Idempotents.Karoubi.instRigidCategory).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Idempotents.Karoubi.instRigidCategory`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Envelope/Karoubi/Rigid.html#CategoryTheory.Idempotents.Karoubi.instRigidCategory)
- [Source of `CategoryTheory.Idempotents.Karoubi.instRigidCategory` in TauCeti/CategoryTheory/Monoidal/Envelope/Karoubi/Rigid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Envelope/Karoubi/Rigid.lean#L183)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
