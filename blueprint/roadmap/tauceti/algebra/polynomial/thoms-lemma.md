---
declaration: theorem
origin: cited
lean: Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo, Polynomial.preimage_thomEncoding_subsingleton_or_eq_Ioo
statement: formalized
proof: formalized
---

# Thom's lemma

For any signs `σ k` prescribed for the derivatives of every order of `p`,
including order zero, the set of points where `p` realizes them is empty, a single point, or an
open interval with endpoints `a ∈ WithBot R` and `b ∈ WithTop R`.

```lean
Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo.{u_1} {R : Type u_1} [Field R]
  [LinearOrder R] [IsStrictOrderedRing R] [IsRealClosed R] (p : Polynomial R) (σ : ℕ → SignType) :
  (p.derivativeSign ⁻¹' {σ}).Subsingleton ∨ ∃ a b, p.derivativeSign ⁻¹' {σ} = {x | a < ↑x ∧ ↑x < b}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Thom/Interval.html#Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo).

## Other forms

**Thom's lemma for finite Thom encodings.** Formalized in Tau Ceti as [`Polynomial.preimage_thomEncoding_subsingleton_or_eq_Ioo`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Thom/Interval.html#Polynomial.preimage_thomEncoding_subsingleton_or_eq_Ioo).

```lean
Polynomial.preimage_thomEncoding_subsingleton_or_eq_Ioo.{u_1} {R : Type u_1} [Field R]
  [LinearOrder R] [IsStrictOrderedRing R] [IsRealClosed R] (p : Polynomial R)
  (τ : Fin p.natDegree → SignType) :
  (p.thomEncoding ⁻¹' {τ}).Subsingleton ∨ ∃ a b, p.thomEncoding ⁻¹' {τ} = {x | a < ↑x ∧ ↑x < b}
```

## Sources

- [Tau Ceti documentation: `Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Thom/Interval.html#Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo)
- [Source of `Polynomial.preimage_derivativeSign_subsingleton_or_eq_Ioo` in TauCeti/Algebra/Polynomial/Thom/Interval.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Polynomial/Thom/Interval.lean#L63)
