---
declaration: theorem
origin: cited
lean: TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one, TauCeti.Place.differentExponent_eq_finsum_card_ramificationGroup_sub_one
statement: formalized
proof: formalized
---

# Hilbert's different formula

**Hilbert's different formula** (Stichtenoth, Theorem 3.8.7), with the sum cut off at an
index `N` from which the ramification groups are trivial:
`d(P ∣ P ∩ F) = ∑_{i < N} (|G_i(P)| - 1)`, when the residue extension is separable.

```lean
TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one.{u, v, v'} {k : Type u}
  (F : Type v) {F' : Type v'} [Field k] [Field F] [Field F'] [Algebra k F] [Algebra k F']
  [Algebra F F'] [IsScalarTower k F F'] [FiniteDimensional F F'] [IsGalois F F']
  (P : TauCeti.Place k F')
  [Algebra.IsSeparable (TauCeti.Place.restrict k F P).ResidueField P.ResidueField] {N : ℕ}
  (hN : TauCeti.Place.ramificationGroup F P N = ⊥) :
  TauCeti.Place.differentExponent k F P =
    ∑ i ∈ Finset.range N, (Nat.card ↥(TauCeti.Place.ramificationGroup F P i) - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental identity](the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Galois correspondence for the inertia field](the-galois-correspondence-for-the-inertia-field.md)
- [Hilbert's counting identity](../../../ring-theory/part-01/local-ring/hilberts-counting-identity.md)
- [The residue action, on residues (Stichtenoth, Theorem 3.8.2)](the-residue-action-on-residues-stichtenoth-theor.md)
- [The weak approximation theorem](the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hilbert.html#TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one).

## Other forms

**Hilbert's different formula (Stichtenoth, Theorem 3.8.7).** Formalized in Tau Ceti as [`TauCeti.Place.differentExponent_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hilbert.html#TauCeti.Place.differentExponent_eq_finsum_card_ramificationGroup_sub_one).

```lean
TauCeti.Place.differentExponent_eq_finsum_card_ramificationGroup_sub_one.{u, v, v'} {k : Type u}
  (F : Type v) {F' : Type v'} [Field k] [Field F] [Field F'] [Algebra k F] [Algebra k F']
  [Algebra F F'] [IsScalarTower k F F'] [FiniteDimensional F F'] [IsGalois F F']
  (P : TauCeti.Place k F')
  [Algebra.IsSeparable (TauCeti.Place.restrict k F P).ResidueField P.ResidueField] :
  TauCeti.Place.differentExponent k F P =
    ∑ᶠ (i : ℕ), (Nat.card ↥(TauCeti.Place.ramificationGroup F P i) - 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Different/Hilbert.html#TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one)
- [Source of `TauCeti.Place.differentExponent_eq_sum_range_card_ramificationGroup_sub_one` in TauCeti/FieldTheory/FunctionField/Different/Hilbert.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Different/Hilbert.lean#L203)
