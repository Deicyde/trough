---
declaration: theorem
origin: cited
lean: TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff
statement: formalized
proof: formalized
---

# The ray class number equals the product of the class number, the number of residue units and the number of sign patterns exactly when every integer unit is congruent to one modulo `𝔪`

Otherwise it is smaller by a factor of the index of the units congruent to one.

```lean
TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (𝔪 : TauCeti.GlobalNumberFields.Modulus K) :
  Nat.card (TauCeti.GlobalNumberFields.RayClassGroup 𝔪) =
      Nat.card (ClassGroup (NumberField.RingOfIntegers K)) *
        (Nat.card (NumberField.RingOfIntegers K ⧸ 𝔪.finitePart)ˣ * 2 ^ 𝔪.infinitePart.card) ↔
    TauCeti.GlobalNumberFields.unitsCongruenceSubgroup 𝔪 = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/RayClass/ClassNumber.html#TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/RayClass/ClassNumber.html#TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff)
- [Source of `TauCeti.GlobalNumberFields.card_rayClassGroup_eq_iff` in TauCeti/NumberTheory/NumberField/Global/RayClass/ClassNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Global/RayClass/ClassNumber.lean#L138)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/GlobalNumberFields/STATUS.md)
