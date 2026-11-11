---
declaration: theorem
origin: cited
lean: QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq, QuadraticForm.equivalent_iff_finrank_eq_and_sigPos_eq_and_sigNeg_eq, QuadraticForm.sigNeg_eq_finrank_of_isCompl_of_negDef, QuadraticForm.sigPos_eq_finrank_of_isCompl_of_posDef, TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq
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

**Sylvester's law of inertia for a definite splitting.** Formalized in Tau Ceti as [`QuadraticForm.sigNeg_eq_finrank_of_isCompl_of_negDef`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Signature.html#QuadraticForm.sigNeg_eq_finrank_of_isCompl_of_negDef).

```lean
QuadraticForm.sigNeg_eq_finrank_of_isCompl_of_negDef.{u_1, u_2} {K : Type u_1} {M : Type u_2}
  [Field K] [LinearOrder K] [IsStrictOrderedRing K] [AddCommGroup M] [_root_.Module K M]
  [FiniteDimensional K M] (Q : QuadraticForm K M) {A B : Subspace K M} (hAB : IsCompl A B)
  (hA : (QuadraticMap.restrict (-Q) A).PosDef) (hB : ∀ x ∈ B, 0 ≤ Q x) :
  sigNeg Q = Module.finrank K ↥A
```

**Sylvester's law of inertia for a definite splitting.** Formalized in Tau Ceti as [`QuadraticForm.sigPos_eq_finrank_of_isCompl_of_posDef`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Signature.html#QuadraticForm.sigPos_eq_finrank_of_isCompl_of_posDef).

```lean
QuadraticForm.sigPos_eq_finrank_of_isCompl_of_posDef.{u_1, u_2} {K : Type u_1} {M : Type u_2}
  [Field K] [LinearOrder K] [AddCommGroup M] [_root_.Module K M] [FiniteDimensional K M]
  (Q : QuadraticForm K M) {A B : Subspace K M} (hAB : IsCompl A B)
  (hA : (QuadraticMap.restrict Q A).PosDef) (hB : ∀ x ∈ B, Q x ≤ 0) : sigPos Q = Module.finrank K ↥A
```

**Sylvester's law of inertia for isometry classes.** Formalized in Tau Ceti as [`TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Witt/Signature.html#TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq).

```lean
TauCeti.RegularFormClass.eq_iff_rank_eq_and_signature_eq.{u_1} {K : Type u_1} [Field K]
  [LinearOrder K] [IsStrictOrderedRing K] [Invertible 2] [IsRealClosed K]
  {x y : TauCeti.RegularFormClass K} : x = y ↔ x.rank = y.rank ∧ x.signature = y.signature
```

## Sources

- [Tau Ceti documentation: `QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/QuadraticForm/Real.html#QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq)
- [Source of `QuadraticForm.equivalent_iff_sigPos_eq_and_sigNeg_eq` in TauCeti/LinearAlgebra/QuadraticForm/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/QuadraticForm/Real.lean#L281)
