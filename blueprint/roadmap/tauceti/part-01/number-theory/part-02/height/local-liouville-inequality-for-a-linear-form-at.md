---
declaration: theorem
origin: cited
lean: NumberField.FinitePlace.iSup_mul_iSup_le, NumberField.InfinitePlace.iSup_mul_iSup_pow_mult_le
statement: formalized
proof: formalized
---

# Local Liouville inequality for a linear form at a finite place

The constant
`card ι ^ [K : ℚ]` remains present, since the global height still uses the infinite places.

```lean
NumberField.FinitePlace.iSup_mul_iSup_le.{u_1, u_2} {K : Type u_1} {ι : Type u_2} [Field K]
  [NumberField K] [Fintype ι] (v : NumberField.FinitePlace K) (a x : ι → K)
  (hz : ∑ i, a i * x i ≠ 0) :
  (⨆ i, v (a i)) * ⨆ i, v (x i) ≤
    ↑(Fintype.card ι) ^ Module.finrank ℚ K * (Height.mulHeight a * Height.mulHeight x) *
      v (∑ i, a i * x i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.FinitePlace.iSup_mul_iSup_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/LinearForm.html#NumberField.FinitePlace.iSup_mul_iSup_le).

## Other forms

**Local Liouville inequality for a linear form at an infinite place.** Formalized in Tau Ceti as [`NumberField.InfinitePlace.iSup_mul_iSup_pow_mult_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/LinearForm.html#NumberField.InfinitePlace.iSup_mul_iSup_pow_mult_le).

```lean
NumberField.InfinitePlace.iSup_mul_iSup_pow_mult_le.{u_1, u_2} {K : Type u_1} {ι : Type u_2}
  [Field K] [NumberField K] [Fintype ι] (v : NumberField.InfinitePlace K) (a x : ι → K)
  (hz : ∑ i, a i * x i ≠ 0) :
  ((⨆ i, v (a i)) * ⨆ i, v (x i)) ^ v.mult ≤
    ↑(Fintype.card ι) ^ Module.finrank ℚ K * (Height.mulHeight a * Height.mulHeight x) *
      v (∑ i, a i * x i) ^ v.mult
```

## Sources

- [Tau Ceti documentation: `NumberField.FinitePlace.iSup_mul_iSup_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/LinearForm.html#NumberField.FinitePlace.iSup_mul_iSup_le)
- [Source of `NumberField.FinitePlace.iSup_mul_iSup_le` in TauCeti/NumberTheory/Height/LinearForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Height/LinearForm.lean#L266)
