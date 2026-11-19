---
declaration: theorem
origin: cited
lean: TauCeti.divisor_divisorProductOne
statement: formalized
proof: formalized
---

# TauCeti.divisor_divisorProductOne

For an entire function nonzero at zero, the product has exactly its native divisor.

```lean
TauCeti.divisor_divisorProductOne {f : ℂ → ℂ} (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0)
  (hsum : Summable fun ρ => ↑((MeromorphicOn.divisor f Set.univ) ↑ρ).toNat * ‖(↑ρ)⁻¹‖ ^ 2) :
  MeromorphicOn.divisor (TauCeti.divisorProductOne f) Set.univ = MeromorphicOn.divisor f Set.univ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.divisor_divisorProductOne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CanonicalProduct/Divisor.html#TauCeti.divisor_divisorProductOne).

## Sources

- [Tau Ceti documentation: `TauCeti.divisor_divisorProductOne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CanonicalProduct/Divisor.html#TauCeti.divisor_divisorProductOne)
- [Source of `TauCeti.divisor_divisorProductOne` in TauCeti/Analysis/Complex/CanonicalProduct/Divisor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/CanonicalProduct/Divisor.lean#L211)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
