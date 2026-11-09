---
declaration: theorem
origin: cited
lean: TauCeti.fixedField_evenAutSubgroup, TauCeti.fixingSubgroup_discrField
statement: formalized
proof: formalized
---

# The comparison theorem (`TauCeti.fixedField_evenAutSubgroup`)

In a Galois splitting extension, and away from characteristic `2`,
the discriminant field of a separable polynomial is the field fixed by the automorphisms
acting on the roots by an even permutation.

```lean
TauCeti.fixedField_evenAutSubgroup.{u, v} {F : Type u} [Field F] {E : Type v} [Field E]
  [Algebra F E] {f : Polynomial F} [Fact (Polynomial.map (algebraMap F E) f).Splits] [IsGalois F E]
  (hsep : f.Separable) (hchar : ringChar F ≠ 2) :
  IntermediateField.fixedField (TauCeti.evenAutSubgroup f E) = TauCeti.discrField f E
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Polynomial.Gal.sign](../galois-groups-of-polynomials/polynomial-gal-sign.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.fixedField_evenAutSubgroup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Discriminant/Field.html#TauCeti.fixedField_evenAutSubgroup).

## Other forms

**The comparison theorem, from the other side.** Formalized in Tau Ceti as [`TauCeti.fixingSubgroup_discrField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Discriminant/Field.html#TauCeti.fixingSubgroup_discrField).

```lean
TauCeti.fixingSubgroup_discrField.{u, v} {F : Type u} [Field F] {E : Type v} [Field E] [Algebra F E]
  {f : Polynomial F} [Fact (Polynomial.map (algebraMap F E) f).Splits] (hsep : f.Separable)
  (hchar : ringChar F ≠ 2) : (TauCeti.discrField f E).fixingSubgroup = TauCeti.evenAutSubgroup f E
```

## Sources

- [Tau Ceti documentation: `TauCeti.fixedField_evenAutSubgroup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Discriminant/Field.html#TauCeti.fixedField_evenAutSubgroup)
- [Source of `TauCeti.fixedField_evenAutSubgroup` in TauCeti/FieldTheory/GaloisGroups/Discriminant/Field.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisGroups/Discriminant/Field.lean#L327)
