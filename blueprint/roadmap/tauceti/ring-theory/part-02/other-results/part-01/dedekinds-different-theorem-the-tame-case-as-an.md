---
declaration: theorem
origin: cited
lean: TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff, TauCeti.pow_dvd_differentIdeal_iff_of_isCoprime, TauCeti.ramificationIdx_sub_one_le_multiplicity_differentIdeal, TauCeti.pow_ramificationIdx_dvd_differentIdeal_iff, TauCeti.ramificationIdx_le_multiplicity_differentIdeal_iff
statement: formalized
proof: formalized
---

# Dedekind's different theorem, the tame case, as an exponent

the multiplicity of `P` in
the different ideal is exactly `e(P ∣ p) - 1` when the residue extension is separable and
`e(P ∣ p)` is nonzero in the residue field `A ⧸ p`.

```lean
TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff.{u_1, u_2} (A : Type u_1)
  {B : Type u_2} [CommRing A] [CommRing B] [Algebra A B] [IsDedekindDomain A] [IsDedekindDomain B]
  [Module.IsTorsionFree A B] [Module.Finite A B]
  [Algebra.IsSeparable (FractionRing A) (FractionRing B)] {p : Ideal A} [p.IsMaximal] (hp : p ≠ ⊥)
  (P : Ideal B) [P.IsMaximal] [P.LiesOver p] :
  multiplicity P (differentIdeal A B) = P.ramificationIdx A - 1 ↔
    Algebra.IsSeparable (A ⧸ p) (B ⧸ P) ∧ ↑(P.ramificationIdx A) ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Different.html#TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff).

## Other forms

**Dedekind's different theorem at a prime power with a coprime complement.** Formalized in Tau Ceti as [`TauCeti.pow_dvd_differentIdeal_iff_of_isCoprime`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Different.html#TauCeti.pow_dvd_differentIdeal_iff_of_isCoprime).

```lean
TauCeti.pow_dvd_differentIdeal_iff_of_isCoprime.{u_1, u_2} (A : Type u_1) {B : Type u_2}
  [CommRing A] [CommRing B] [Algebra A B] [IsDedekindDomain A] [IsDedekindDomain B]
  [Module.IsTorsionFree A B] [Module.Finite A B]
  [Algebra.IsSeparable (FractionRing A) (FractionRing B)] {p : Ideal A} [p.IsMaximal] (hp : p ≠ ⊥)
  (P Q : Ideal B) [P.IsMaximal] [P.LiesOver p] {e : ℕ} (hPQ : IsCoprime (P ^ e) Q)
  (hmul : P ^ e * Q = Ideal.map (algebraMap A B) p) :
  P ^ e ∣ differentIdeal A B ↔ ¬Algebra.IsSeparable (A ⧸ p) (B ⧸ P) ∨ ↑e = 0
```

**Dedekind's different theorem, first part, as a bound on the exponent.** Formalized in Tau Ceti as [`TauCeti.ramificationIdx_sub_one_le_multiplicity_differentIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Different/Basic.html#TauCeti.ramificationIdx_sub_one_le_multiplicity_differentIdeal).

```lean
TauCeti.ramificationIdx_sub_one_le_multiplicity_differentIdeal.{u_1, u_2} (A : Type u_1)
  {B : Type u_2} [CommRing A] [CommRing B] [Algebra A B] [IsDedekindDomain A] [IsDedekindDomain B]
  [Module.IsTorsionFree A B] [Module.Finite A B]
  [Algebra.IsSeparable (FractionRing A) (FractionRing B)] {p : Ideal A} [p.IsMaximal] (hp : p ≠ ⊥)
  (P : Ideal B) [P.IsPrime] [P.LiesOver p] :
  P.ramificationIdx A - 1 ≤ multiplicity P (differentIdeal A B)
```

**Dedekind's different theorem, second part (Stichtenoth, Theorem 3.5.1(b) and Corollary 3.5.5).** Formalized in Tau Ceti as [`TauCeti.pow_ramificationIdx_dvd_differentIdeal_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Different.html#TauCeti.pow_ramificationIdx_dvd_differentIdeal_iff).

```lean
TauCeti.pow_ramificationIdx_dvd_differentIdeal_iff.{u_1, u_2} (A : Type u_1) {B : Type u_2}
  [CommRing A] [CommRing B] [Algebra A B] [IsDedekindDomain A] [IsDedekindDomain B]
  [Module.IsTorsionFree A B] [Module.Finite A B]
  [Algebra.IsSeparable (FractionRing A) (FractionRing B)] {p : Ideal A} [p.IsMaximal] (hp : p ≠ ⊥)
  (P : Ideal B) [P.IsMaximal] [P.LiesOver p] :
  P ^ P.ramificationIdx A ∣ differentIdeal A B ↔
    ¬Algebra.IsSeparable (A ⧸ p) (B ⧸ P) ∨ ↑(P.ramificationIdx A) = 0
```

**Dedekind's different theorem, second part, as a bound on the exponent.** Formalized in Tau Ceti as [`TauCeti.ramificationIdx_le_multiplicity_differentIdeal_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Different.html#TauCeti.ramificationIdx_le_multiplicity_differentIdeal_iff).

```lean
TauCeti.ramificationIdx_le_multiplicity_differentIdeal_iff.{u_1, u_2} (A : Type u_1) {B : Type u_2}
  [CommRing A] [CommRing B] [Algebra A B] [IsDedekindDomain A] [IsDedekindDomain B]
  [Module.IsTorsionFree A B] [Module.Finite A B]
  [Algebra.IsSeparable (FractionRing A) (FractionRing B)] {p : Ideal A} [p.IsMaximal] (hp : p ≠ ⊥)
  (P : Ideal B) [P.IsMaximal] [P.LiesOver p] :
  P.ramificationIdx A ≤ multiplicity P (differentIdeal A B) ↔
    ¬Algebra.IsSeparable (A ⧸ p) (B ⧸ P) ∨ ↑(P.ramificationIdx A) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/DedekindDomain/Different.html#TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff)
- [Source of `TauCeti.multiplicity_differentIdeal_eq_ramificationIdx_sub_one_iff` in TauCeti/RingTheory/DedekindDomain/Different.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/DedekindDomain/Different.lean#L162)
