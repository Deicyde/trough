---
declaration: theorem
origin: cited
lean: TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv
statement: formalized
proof: formalized
---

# The image of the cyclotomic character is an invariant of the field

An isomorphism of fields
induces an isomorphism of absolute Galois groups, and the cyclotomic character of the target is the
character of the source read through it (`TauCeti.localCyclotomicCharacter_map`); hence the two
characters have the same image in `ℤ_pˣ`.

```lean
TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv.{u_1, u_2} (p : ℕ) [Fact (Nat.Prime p)]
  {K : Type u_1} [Field K] {K' : Type u_2} [Field K'] (e : K ≃+* K') :
  (TauCeti.localCyclotomicCharacter p K).range = (TauCeti.localCyclotomicCharacter p K').range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv)
- [Source of `TauCeti.range_localCyclotomicCharacter_eq_of_ringEquiv` in TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean#L104)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
