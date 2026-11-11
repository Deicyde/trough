---
declaration: theorem
origin: cited
lean: TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor, TauCeti.fusionCoeff_dual_left, TauCeti.fusionCoeff_dual_right, TauCeti.fusionCoeff_eq_simpleMultiplicities_tensor_rightDual
statement: formalized
proof: formalized
---

# Frobenius reciprocity in multiplicity form

`N_{S T}^U` is the multiplicity of `T` in
`Sᘁ ⊗ U`, coming from `(Sᘁ ⊗ U ⟶ T) ≃ (U ⟶ S ⊗ T)`.

```lean
TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor.{w', v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.RigidCategory C] (k : Type w') [Field k]
  [IsAlgClosed k] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  (S T U : TauCeti.SimpleClasses C) :
  TauCeti.fusionCoeff k S T U =
    (TauCeti.simpleMultiplicities (CategoryTheory.MonoidalCategoryStruct.tensorObj S.reprᘁ U.repr))
      T
```

## Depends on

- [TauCeti.fusionCoeff](../pivotal-and-spherical-categories/tauceti-fusioncoeff.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Rigid.html#TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor).

## Other forms

**Frobenius reciprocity for fusion coefficients.** Formalized in Tau Ceti as [`TauCeti.fusionCoeff_dual_left`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Rigid.html#TauCeti.fusionCoeff_dual_left).

```lean
TauCeti.fusionCoeff_dual_left.{w', v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.RigidCategory C] (k : Type w') [Field k]
  [IsAlgClosed k] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  (S T U : TauCeti.SimpleClasses C) : TauCeti.fusionCoeff k S.dual T U = TauCeti.fusionCoeff k S U T
```

**Frobenius reciprocity for fusion coefficients.** Formalized in Tau Ceti as [`TauCeti.fusionCoeff_dual_right`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Rigid.html#TauCeti.fusionCoeff_dual_right).

```lean
TauCeti.fusionCoeff_dual_right.{w', v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.RigidCategory C] (k : Type w') [Field k]
  [IsAlgClosed k] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  (S T U : TauCeti.SimpleClasses C) : TauCeti.fusionCoeff k S T.dual U = TauCeti.fusionCoeff k U T S
```

**Frobenius reciprocity in multiplicity form.** Formalized in Tau Ceti as [`TauCeti.fusionCoeff_eq_simpleMultiplicities_tensor_rightDual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Rigid.html#TauCeti.fusionCoeff_eq_simpleMultiplicities_tensor_rightDual).

```lean
TauCeti.fusionCoeff_eq_simpleMultiplicities_tensor_rightDual.{w', v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] [CategoryTheory.RigidCategory C] (k : Type w') [Field k]
  [IsAlgClosed k] [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  (S T U : TauCeti.SimpleClasses C) :
  TauCeti.fusionCoeff k S T U =
    (TauCeti.simpleMultiplicities (CategoryTheory.MonoidalCategoryStruct.tensorObj U.repr T.reprᘁ))
      S
```

## Sources

- [Tau Ceti documentation: `TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/Rigid.html#TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor)
- [Source of `TauCeti.fusionCoeff_eq_simpleMultiplicities_rightDual_tensor` in TauCeti/CategoryTheory/Semisimple/Rigid.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Semisimple/Rigid.lean#L217)
