---
declaration: theorem
origin: cited
lean: IntermediateField.finiteDimensional_fixedField, IntermediateField.isGalois_fixedField
statement: formalized
proof: formalized
---

# Artin's theorem

`M` is finite over the field fixed by a finite group of automorphisms.

Mathlib has this for `FixedPoints.subfield H M`; the fixed field of the Galois correspondence is
the same subfield, and this is the instance on that form, with no hypothesis on `M / K`.

```lean
IntermediateField.finiteDimensional_fixedField.{u_1, u_2} {K : Type u_1} {M : Type u_2} [Field K]
  [Field M] [Algebra K M] (H : Subgroup Gal(M/K)) [Finite ↥H] :
  FiniteDimensional (↥(IntermediateField.fixedField H)) M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IntermediateField.finiteDimensional_fixedField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/FixedField.html#IntermediateField.finiteDimensional_fixedField).

## Other forms

**Artin's theorem.** Formalized in Tau Ceti as [`IntermediateField.isGalois_fixedField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/FixedField.html#IntermediateField.isGalois_fixedField).

```lean
IntermediateField.isGalois_fixedField.{u_1, u_2} {K : Type u_1} {M : Type u_2} [Field K] [Field M]
  [Algebra K M] (H : Subgroup Gal(M/K)) [Finite ↥H] : IsGalois (↥(IntermediateField.fixedField H)) M
```

## Sources

- [Tau Ceti documentation: `IntermediateField.finiteDimensional_fixedField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/FixedField.html#IntermediateField.finiteDimensional_fixedField)
- [Source of `IntermediateField.finiteDimensional_fixedField` in TauCeti/FieldTheory/Galois/FixedField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/Galois/FixedField.lean#L171)
