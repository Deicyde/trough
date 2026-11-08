---
declaration: theorem
origin: cited
lean: TauCeti.Sturm.sum_sign_Icc, TauCeti.Sturm.sum_sign, TauCeti.Sturm.sum_sign_Ioc, TauCeti.Sturm.sum_sign_Ico, Polynomial.tarskiQuery_eq_signVariationsAtBot_sub_signVariationsAtTop, TauCeti.Sturm.sum_sign_Ioo
statement: formalized
proof: formalized
---

# Sturm–Tarski on `[a, b]`

The contributions of both closed endpoints are added
explicitly to the open-interval formula. For `a = b` this is the contribution of a point.

```lean
TauCeti.Sturm.sum_sign_Icc.{u_1} {R : Type u_1} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  [IsRealClosed R] {p f : Polynomial R} {cs : List (Polynomial R)}
  (h : TauCeti.Sturm.IsSignedRemainderSeq (p :: cs))
  (hseed : TauCeti.Sturm.IsTarskiSeed p f (cs.head?.getD 0)) {a b : R} (hab : a ≤ b) :
  ((↑(TauCeti.Sturm.signVariationsRight (p :: cs) a) -
          ↑(TauCeti.Sturm.signVariationsLeft (p :: cs) b) +
        if Polynomial.eval a p = 0 then ↑(SignType.sign (Polynomial.eval a f)) else 0) +
      if Polynomial.eval b p = 0 then ↑(SignType.sign (Polynomial.eval b f)) else 0) =
    ∑ r ∈ p.roots.toFinset with a ≤ r ∧ r ≤ b, ↑(SignType.sign (Polynomial.eval r f))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Sturm.sum_sign_Icc`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/OneSided.html#TauCeti.Sturm.sum_sign_Icc).

## Other forms

**Sturm–Tarski.** Formalized in Tau Ceti as [`TauCeti.Sturm.sum_sign`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/Tarski.html#TauCeti.Sturm.sum_sign).

```lean
TauCeti.Sturm.sum_sign.{u_1} {R : Type u_1} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  [IsRealClosed R] {p f : Polynomial R} {cs : List (Polynomial R)}
  (h : TauCeti.Sturm.IsSignedRemainderSeq (p :: cs))
  (hseed : TauCeti.Sturm.IsTarskiSeed p f (cs.head?.getD 0)) {a b : R} (hab : a < b)
  (ha : Polynomial.eval a p ≠ 0) (hb : Polynomial.eval b p ≠ 0) :
  ↑(TauCeti.Sturm.signVariationsAt (p :: cs) a) - ↑(TauCeti.Sturm.signVariationsAt (p :: cs) b) =
    ∑ r ∈ p.roots.toFinset with a < r ∧ r < b, ↑(SignType.sign (Polynomial.eval r f))
```

**Sturm–Tarski on `(a, b]`.** Formalized in Tau Ceti as [`TauCeti.Sturm.sum_sign_Ioc`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/OneSided.html#TauCeti.Sturm.sum_sign_Ioc).

```lean
TauCeti.Sturm.sum_sign_Ioc.{u_1} {R : Type u_1} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  [IsRealClosed R] {p f : Polynomial R} {cs : List (Polynomial R)}
  (h : TauCeti.Sturm.IsSignedRemainderSeq (p :: cs))
  (hseed : TauCeti.Sturm.IsTarskiSeed p f (cs.head?.getD 0)) {a b : R} (hab : a ≤ b) :
  (↑(TauCeti.Sturm.signVariationsRight (p :: cs) a) -
        ↑(TauCeti.Sturm.signVariationsLeft (p :: cs) b) +
      if Polynomial.eval b p = 0 then ↑(SignType.sign (Polynomial.eval b f)) else 0) =
    ∑ r ∈ p.roots.toFinset with a < r ∧ r ≤ b, ↑(SignType.sign (Polynomial.eval r f))
```

**Sturm–Tarski on `[a, b)`.** Formalized in Tau Ceti as [`TauCeti.Sturm.sum_sign_Ico`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/OneSided.html#TauCeti.Sturm.sum_sign_Ico).

```lean
TauCeti.Sturm.sum_sign_Ico.{u_1} {R : Type u_1} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  [IsRealClosed R] {p f : Polynomial R} {cs : List (Polynomial R)}
  (h : TauCeti.Sturm.IsSignedRemainderSeq (p :: cs))
  (hseed : TauCeti.Sturm.IsTarskiSeed p f (cs.head?.getD 0)) {a b : R} (hab : a ≤ b) :
  (↑(TauCeti.Sturm.signVariationsRight (p :: cs) a) -
        ↑(TauCeti.Sturm.signVariationsLeft (p :: cs) b) +
      if Polynomial.eval a p = 0 then ↑(SignType.sign (Polynomial.eval a f)) else 0) =
    ∑ r ∈ p.roots.toFinset with a ≤ r ∧ r < b, ↑(SignType.sign (Polynomial.eval r f))
```

**Sturm–Tarski on the whole line.** Formalized in Tau Ceti as [`Polynomial.tarskiQuery_eq_signVariationsAtBot_sub_signVariationsAtTop`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/CauchyIndex/Sequence.html#Polynomial.tarskiQuery_eq_signVariationsAtBot_sub_signVariationsAtTop).

```lean
Polynomial.tarskiQuery_eq_signVariationsAtBot_sub_signVariationsAtTop.{u_1} {R : Type u_1} [Field R]
  [LinearOrder R] [IsStrictOrderedRing R] [IsRealClosed R] (p q : Polynomial R) :
  p.tarskiQuery q =
    ↑(TauCeti.Sturm.signVariationsAtBot (p.sturmSeq (Polynomial.derivative p * q))) -
      ↑(TauCeti.Sturm.signVariationsAtTop (p.sturmSeq (Polynomial.derivative p * q)))
```

**Sturm–Tarski with one-sided endpoints.** Formalized in Tau Ceti as [`TauCeti.Sturm.sum_sign_Ioo`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/OneSided.html#TauCeti.Sturm.sum_sign_Ioo).

```lean
TauCeti.Sturm.sum_sign_Ioo.{u_1} {R : Type u_1} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
  [IsRealClosed R] {p f : Polynomial R} {cs : List (Polynomial R)}
  (h : TauCeti.Sturm.IsSignedRemainderSeq (p :: cs))
  (hseed : TauCeti.Sturm.IsTarskiSeed p f (cs.head?.getD 0)) {a b : R} (hab : a < b) :
  ↑(TauCeti.Sturm.signVariationsRight (p :: cs) a) -
      ↑(TauCeti.Sturm.signVariationsLeft (p :: cs) b) =
    ∑ r ∈ p.roots.toFinset with a < r ∧ r < b, ↑(SignType.sign (Polynomial.eval r f))
```

## Sources

- [Tau Ceti documentation: `TauCeti.Sturm.sum_sign_Icc`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Sturm/OneSided.html#TauCeti.Sturm.sum_sign_Icc)
- [Source of `TauCeti.Sturm.sum_sign_Icc` in TauCeti/Algebra/Polynomial/Sturm/OneSided.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Polynomial/Sturm/OneSided.lean#L368)
