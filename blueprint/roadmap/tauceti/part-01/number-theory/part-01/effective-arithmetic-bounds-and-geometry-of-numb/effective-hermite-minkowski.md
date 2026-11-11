---
declaration: theorem
origin: cited
lean: NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le
statement: formalized
proof: formalized
---

# Effective Hermite--Minkowski

Inside a fixed extension `A / ℚ`, the number of number fields
`K` (finite extensions of `ℚ`) with `|discr K| ≤ N` is at most
`(2 * coeffBoundOfDiscrBdd N + 1) ^ (rankOfDiscrBdd N + 1) * rankOfDiscrBdd N`, an explicit function
of `N` alone. This upgrades Mathlib's `NumberField.finite_of_discr_bdd` from finiteness to an
explicit count.

```lean
NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le.{u_1} (A : Type u_1) [Field A]
  [CharZero A] (N : ℕ) :
  {K | |NumberField.discr ↥↑K| ≤ ↑N}.ncard ≤
    (2 * NumberField.coeffBoundOfDiscrBdd N + 1) ^
        (NumberField.hermiteTheorem.rankOfDiscrBdd N + 1) *
      NumberField.hermiteTheorem.rankOfDiscrBdd N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.html#NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le).

## Sources

- [Tau Ceti documentation: `NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.html#NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le)
- [Source of `NumberField.ncard_setOf_finiteDimensional_abs_discr_le_le` in TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/EffectiveBounds/HermiteCount/Basic.lean#L167)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/EffectiveBounds/STATUS.md)
