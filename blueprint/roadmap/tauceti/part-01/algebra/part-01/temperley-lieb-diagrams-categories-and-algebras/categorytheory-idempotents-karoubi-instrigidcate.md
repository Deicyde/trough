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
- [Source of `CategoryTheory.Idempotents.Karoubi.instRigidCategory` in TauCeti/CategoryTheory/Monoidal/Envelope/Karoubi/Rigid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Envelope/Karoubi/Rigid.lean#L183)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TemperleyLieb/STATUS.md)
