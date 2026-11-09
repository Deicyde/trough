---
declaration: theorem
origin: cited
lean: TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty
statement: formalized
proof: formalized
---

# The tame different theorem fails at infinity

the different exponent `d` is at least the
ramification index `e`, so `e ≠ d + 1`, unlike at every tame place.

```lean
TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty.{u_1}
  {k : Type u_1} [Field k] {p m : ℕ} [Fact (Nat.Prime p)] [CharP k p] [hm : Fact ¬p ∣ m]
  {P : TauCeti.Place k (TauCeti.ArtinSchreierMonomial.FunctionField k p m)}
  (hP : TauCeti.Place.restrict k (RatFunc k) P = TauCeti.Place.infty k) :
  TauCeti.Place.ramificationIdx (RatFunc k) P ≤ TauCeti.Place.differentExponent k (RatFunc k) P
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, the tame case, as an exponent](../../../ring-theory/part-02/other-results/part-01/dedekinds-different-theorem-the-tame-case-as-an.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ArtinSchreier/Monomial.html#TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty).

## Sources

- [Tau Ceti documentation: `TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/ArtinSchreier/Monomial.html#TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty)
- [Source of `TauCeti.ArtinSchreierMonomial.ramificationIdx_le_differentExponent_of_restrict_eq_infty` in TauCeti/FieldTheory/FunctionField/ArtinSchreier/Monomial.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/ArtinSchreier/Monomial.lean#L231)
