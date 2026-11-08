---
declaration: theorem
origin: cited
lean: TauCeti.iterate_frobeniusSchurRotate_eq_id, TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one
statement: formalized
proof: formalized
---

# Ng–Schauenburg

the `(n + 1)`-st iterate of `E_V^{(n+1)}` is the identity.

```lean
TauCeti.iterate_frobeniusSchurRotate_eq_id.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C]
  (V : C) (n : ℕ) : (TauCeti.frobeniusSchurRotate V n)^[n + 1] = id
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.iterate_frobeniusSchurRotate_eq_id`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.html#TauCeti.iterate_frobeniusSchurRotate_eq_id).

## Other forms

**Ng–Schauenburg trichotomy.** Formalized in Tau Ceti as [`TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Simple.html#TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one).

```lean
TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.Preadditive C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C] [CategoryTheory.Limits.HasKernels C]
  (k : Type w) [Field k] [IsAlgClosed k] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalLinear k C] (V : C) [CategoryTheory.Simple V]
  [FiniteDimensional k (V ⟶ V)] [CategoryTheory.Simple Vᘁ] :
  TauCeti.frobeniusSchurIndicator k V 2 = 1 ∨
    TauCeti.frobeniusSchurIndicator k V 2 = 0 ∨ TauCeti.frobeniusSchurIndicator k V 2 = -1
```

## Sources

- [Tau Ceti documentation: `TauCeti.iterate_frobeniusSchurRotate_eq_id`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.html#TauCeti.iterate_frobeniusSchurRotate_eq_id)
- [Source of `TauCeti.iterate_frobeniusSchurRotate_eq_id` in TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Basic.lean#L229)
