---
declaration: theorem
origin: cited
lean: TauCeti.natCard_le_eighty_four_mul_genus_sub_one, TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_not_dvd, TauCeti.card_algEquiv_le_eighty_four_mul_genus_sub_one_of_charZero, TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_charZero
statement: formalized
proof: formalized
---

# The Hurwitz bound (Stichtenoth, Exercise 3.18)

a finite group `G` of automorphisms of a
function field of genus `g ≥ 2`, every place of which is tame over the fixed field, has order at
most `84 (g - 1)`.

```lean
TauCeti.natCard_le_eighty_four_mul_genus_sub_one.{u, v} {k : Type u} {F : Type v} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  (G : Subgroup Gal(F/k)) [Finite ↥G] (hgenus : 2 ≤ TauCeti.genus k F)
  (htame :
    ∀ (P : TauCeti.Place k F), TauCeti.Place.IsTame k (↥(IntermediateField.fixedField G)) P) :
  Nat.card ↥G ≤ 84 * (TauCeti.genus k F - 1)
```

## Depends on

- [Artin's theorem](../../galois/artins-theorem.md)

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental identity](the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The weak approximation theorem](the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.natCard_le_eighty_four_mul_genus_sub_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.html#TauCeti.natCard_le_eighty_four_mul_genus_sub_one).

## Other forms

**The Hurwitz bound for a group of order prime to the characteristic (Stichtenoth, Exercise 3.18).** Formalized in Tau Ceti as [`TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_not_dvd`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.html#TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_not_dvd).

```lean
TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_not_dvd.{u, v} {k : Type u} {F : Type v}
  [Field k] [Field F] [Algebra k F] [PerfectField k] (p : ℕ) [CharP k p]
  (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F) (G : Subgroup Gal(F/k))
  [Finite ↥G] (hgenus : 2 ≤ TauCeti.genus k F) (hp : ¬p ∣ Nat.card ↥G) :
  Nat.card ↥G ≤ 84 * (TauCeti.genus k F - 1)
```

**The Hurwitz bound for the whole automorphism group.** Formalized in Tau Ceti as [`TauCeti.card_algEquiv_le_eighty_four_mul_genus_sub_one_of_charZero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.html#TauCeti.card_algEquiv_le_eighty_four_mul_genus_sub_one_of_charZero).

```lean
TauCeti.card_algEquiv_le_eighty_four_mul_genus_sub_one_of_charZero.{u, v} {k : Type u} {F : Type v}
  [Field k] [Field F] [Algebra k F] [CharZero k] [Finite Gal(F/k)]
  (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  (hgenus : 2 ≤ TauCeti.genus k F) : Nat.card Gal(F/k) ≤ 84 * (TauCeti.genus k F - 1)
```

**The Hurwitz bound in characteristic zero (Stichtenoth, Exercise 3.18).** Formalized in Tau Ceti as [`TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_charZero`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.html#TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_charZero).

```lean
TauCeti.natCard_le_eighty_four_mul_genus_sub_one_of_charZero.{u, v} {k : Type u} {F : Type v}
  [Field k] [Field F] [Algebra k F] [CharZero k] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) (G : Subgroup Gal(F/k)) [Finite ↥G]
  (hgenus : 2 ≤ TauCeti.genus k F) : Nat.card ↥G ≤ 84 * (TauCeti.genus k F - 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.natCard_le_eighty_four_mul_genus_sub_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.html#TauCeti.natCard_le_eighty_four_mul_genus_sub_one)
- [Source of `TauCeti.natCard_le_eighty_four_mul_genus_sub_one` in TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Automorphism/HurwitzBound.lean#L80)
