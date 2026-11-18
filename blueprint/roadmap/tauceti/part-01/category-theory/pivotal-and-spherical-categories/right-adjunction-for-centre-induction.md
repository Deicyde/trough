---
declaration: def
origin: cited
lean: CategoryTheory.Center.forgetInductionAdjunction
statement: formalized
---

# Right adjunction for centre induction

`Center.forget C ⊣ Center.induction k C`. This holds
for any rigid `k`-linear finite semisimple abelian monoidal category over an algebraically closed
field with finitely many simple classes and finite-dimensional Hom spaces, without assuming
simplicity of the tensor unit or a pivotal structure.

```lean
CategoryTheory.Center.forgetInductionAdjunction.{w, v, u} (k : Type w) [Field k] [IsAlgClosed k]
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.Linear k C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.MonoidalLinear k C]
  [CategoryTheory.RightRigidCategory C] [TauCeti.IsFiniteSemisimpleCategory C]
  [Fintype (TauCeti.SimpleClasses C)] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [CategoryTheory.LeftRigidCategory C] :
  CategoryTheory.Center.forget C ⊣ CategoryTheory.Center.induction k C
```

## Depends on

- [CategoryTheory.Center.induction](categorytheory-center-induction.md)
- [Module.Basis.homDual](module-basis-homdual.md)

## Proof depends on

- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Center.forgetInductionAdjunction`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Center/Induction/Adjunction.html#CategoryTheory.Center.forgetInductionAdjunction).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Center.forgetInductionAdjunction`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Center/Induction/Adjunction.html#CategoryTheory.Center.forgetInductionAdjunction)
- [Source of `CategoryTheory.Center.forgetInductionAdjunction` in TauCeti/CategoryTheory/Monoidal/Center/Induction/Adjunction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Center/Induction/Adjunction.lean#L388)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
