---
declaration: theorem
origin: cited
lean: TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one
statement: formalized
proof: formalized
---

# Ng–Schauenburg trichotomy

for a simple object `V` (with `Vᘁ` simple and `V ⟶ V`
finite-dimensional over an algebraically closed field `k`), the second Frobenius–Schur indicator
takes values in `{1, 0, -1}`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ng–Schauenburg](ng-schauenburg.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Simple.html#TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one).

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Simple.html#TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one)
- [Source of `TauCeti.frobeniusSchurIndicator_two_eq_one_or_eq_zero_or_eq_neg_one` in TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Simple.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/FrobeniusSchur/Simple.lean#L113)
