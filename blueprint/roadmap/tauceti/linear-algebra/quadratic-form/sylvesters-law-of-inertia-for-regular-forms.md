---
declaration: theorem
origin: cited
lean: QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq, QuadraticForm.equivalent_iff_finrank_eq_and_sigPos_eq_and_sigNeg_eq, TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq
statement: formalized
proof: formalized
---

# Sylvester's law of inertia for regular forms

two nondegenerate real quadratic forms are
isometric exactly when their signatures agree.

```lean
QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq.{u_1, u_2} {M : Type u_1} {M' : Type u_2}
  [AddCommGroup M] [_root_.Module ℝ M] [AddCommGroup M'] [_root_.Module ℝ M']
  [FiniteDimensional ℝ M] [FiniteDimensional ℝ M'] {Q : QuadraticForm ℝ M} {Q' : QuadraticForm ℝ M'}
  (hQ : QuadraticMap.Nondegenerate) (hQ' : QuadraticMap.Nondegenerate) :
  QuadraticMap.Equivalent Q Q' ↔ sigPos Q = sigPos Q' ∧ sigNeg Q = sigNeg Q'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Real.html#QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq).

## Other forms

**Sylvester's law of inertia, classification form.** Formalized in Tau Ceti as [`QuadraticForm.equivalent_iff_finrank_eq_and_sigPos_eq_and_sigNeg_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Real.html#QuadraticForm.equivalent_iff_finrank_eq_and_sigPos_eq_and_sigNeg_eq).

```lean
QuadraticForm.equivalent_iff_finrank_eq_and_sigPos_eq_and_sigNeg_eq.{u_1, u_2} {M : Type u_1}
  {M' : Type u_2} [AddCommGroup M] [_root_.Module ℝ M] [AddCommGroup M'] [_root_.Module ℝ M']
  [FiniteDimensional ℝ M] [FiniteDimensional ℝ M'] (Q : QuadraticForm ℝ M)
  (Q' : QuadraticForm ℝ M') :
  QuadraticMap.Equivalent Q Q' ↔
    Module.finrank ℝ M = Module.finrank ℝ M' ∧ sigPos Q = sigPos Q' ∧ sigNeg Q = sigNeg Q'
```

**Sylvester's law of inertia for isometry classes.** Formalized in Tau Ceti as [`TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Signature.html#TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq).

```lean
TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq.{u_1} {K : Type u_1} [Field K]
  [LinearOrder K] [IsStrictOrderedRing K] [Invertible 2] [IsRealClosed K]
  {x y : TauCeti.RegularFormClass K} : x = y ↔ x.rank = y.rank ∧ x.signature = y.signature
```

## Sources

- [Tau Ceti documentation: `QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Real.html#QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq)
- [Source of `QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq` in TauCeti/LinearAlgebra/QuadraticForm/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/QuadraticForm/Real.lean#L279)
