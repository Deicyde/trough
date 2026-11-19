---
declaration: theorem
origin: cited
lean: TauCeti.logDeriv_divisorProductOne
statement: formalized
proof: formalized
---

# TauCeti.logDeriv_divisorProductOne

The logarithmic derivative of the native divisor product is its paired divisor series.

```lean
TauCeti.logDeriv_divisorProductOne {f : ℂ → ℂ} (h0 : 0 ∉ (MeromorphicOn.divisor f Set.univ).support)
  (hsum : Summable fun ρ => ↑((MeromorphicOn.divisor f Set.univ) ↑ρ).toNat * ‖(↑ρ)⁻¹‖ ^ 2) {z : ℂ}
  (hz : z ∉ (MeromorphicOn.divisor f Set.univ).support) :
  logDeriv (TauCeti.divisorProductOne f) z =
    ∑' (ρ : ↑(MeromorphicOn.divisor f Set.univ).support),
      ↑((MeromorphicOn.divisor f Set.univ) ↑ρ).toNat * (1 / (z - ↑ρ) + 1 / ↑ρ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.logDeriv_divisorProductOne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CanonicalProduct/Divisor.html#TauCeti.logDeriv_divisorProductOne).

## Sources

- [Tau Ceti documentation: `TauCeti.logDeriv_divisorProductOne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CanonicalProduct/Divisor.html#TauCeti.logDeriv_divisorProductOne)
- [Source of `TauCeti.logDeriv_divisorProductOne` in TauCeti/Analysis/Complex/CanonicalProduct/Divisor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/CanonicalProduct/Divisor.lean#L261)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
