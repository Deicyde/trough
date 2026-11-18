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
- [Source of `TauCeti.NumberField.mem_ramifiedSupport_iff_exists` in TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Discriminant/RamifiedSupport/Basic.lean#L70)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/NumberFieldArithmetic/STATUS.md)
