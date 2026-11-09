---
declaration: theorem
origin: cited
lean: QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq
statement: formalized
proof: formalized
---

# Sylvester's law of inertia at a real place

Two regular quadratic forms become isometric
at a real place exactly when their signatures there agree.

```lean
QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq.{u, v, v'} {K : Type u} [Field K]
  {V : Type v} [AddCommGroup V] [_root_.Module K V] {W : Type v'} [AddCommGroup W]
  [_root_.Module K W] {Q : QuadraticForm K V} {R : QuadraticForm K W} [FiniteDimensional K V]
  [FiniteDimensional K W] (hQ : QuadraticMap.Nondegenerate) (hR : QuadraticMap.Nondegenerate)
  (w : { w // w.IsReal }) :
  QuadraticMap.Equivalent (Q.atRealPlace w) (R.atRealPlace w) ↔
    Q.realSignature w = R.realSignature w
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sylvester's law of inertia for regular forms](../../../linear-algebra/quadratic-form/sylvesters-law-of-inertia-for-regular-forms.md)

## Lean

Formalized in Tau Ceti as [`QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Signature.html#QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq).

## Sources

- [Tau Ceti documentation: `QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Signature.html#QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq)
- [Source of `QuadraticForm.equivalent_atRealPlace_iff_realSignature_eq` in TauCeti/NumberTheory/QuadraticForm/Global/Signature.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/Signature.lean#L340)
