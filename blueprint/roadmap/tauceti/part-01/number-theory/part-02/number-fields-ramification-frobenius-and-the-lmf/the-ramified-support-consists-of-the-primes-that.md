---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.mem_ramifiedSupport_iff_exists
statement: formalized
proof: formalized
---

# The ramified support consists of the primes that actually ramify

A prime lies in it
exactly when some prime of `𝓞 L` above it has ramification index greater than one.

```lean
TauCeti.NumberField.mem_ramifiedSupport_iff_exists.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L]
  {v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)} :
  v ∈ TauCeti.NumberField.ramifiedSupport K L ↔
    ∃ P, 1 < (↑P).ramificationIdx (NumberField.RingOfIntegers K)
```

## Depends on

- [TauCeti.relDiscr](tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.mem_ramifiedSupport_iff_exists`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Basic.html#TauCeti.NumberField.mem_ramifiedSupport_iff_exists).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.mem_ramifiedSupport_iff_exists`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Basic.html#TauCeti.NumberField.mem_ramifiedSupport_iff_exists)
- [Source of `TauCeti.NumberField.mem_ramifiedSupport_iff_exists` in TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Basic.lean#L70)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/NumberFieldArithmetic/STATUS.md)
