---
declaration: def
origin: cited
lean: CategoryTheory.Center.induction
statement: formalized
---

# CategoryTheory.Center.induction

The **induction functor** `C ⥤ Center C` of a fusion category `C`: it sends `X` to
`⨁ S, S ⊗ X ⊗ Sᘁ`, summed over the simple classes `S`, with the half-braiding
`inductionHalfBraiding` built from dual bases of the spaces `S ⟶ Y ⊗ T`.

```lean
CategoryTheory.Center.induction.{w, v, u} (k : Type w) [Field k] [IsAlgClosed k] (C : Type u)
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.MonoidalLinear k C] [CategoryTheory.RightRigidCategory C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [Fintype (TauCeti.SimpleClasses C)] [CategoryTheory.LeftRigidCategory C] :
  CategoryTheory.Functor C (CategoryTheory.Center C)
```

## Depends on

- [Module.Basis.homDual](module-basis-homdual.md)

## Proof depends on

- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Center.induction`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Center/Induction/Basic.html#CategoryTheory.Center.induction).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Center.induction`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Center/Induction/Basic.html#CategoryTheory.Center.induction)
- [Source of `CategoryTheory.Center.induction` in TauCeti/CategoryTheory/Monoidal/Center/Induction/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Center/Induction/Basic.lean#L464)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
