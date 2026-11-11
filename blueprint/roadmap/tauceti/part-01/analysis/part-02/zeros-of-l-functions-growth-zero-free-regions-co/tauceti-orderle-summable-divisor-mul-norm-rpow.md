---
declaration: theorem
origin: cited
lean: TauCeti.OrderLE.summable_divisor_mul_norm_rpow
statement: formalized
proof: formalized
---

# TauCeti.OrderLE.summable_divisor_mul_norm_rpow

The reciprocal `p`th powers of the zeros of an entire function of order at most `A`
are summable with their divisor multiplicities for every `p > A`, provided the function
is nonzero at the origin.

```lean
TauCeti.OrderLE.summable_divisor_mul_norm_rpow {f : ℂ → ℂ} {A p : ℝ} (h : TauCeti.OrderLE f A)
  (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (hAp : A < p) :
  Summable fun ρ => ↑((MeromorphicOn.divisor f Set.univ) ↑ρ) * ‖↑ρ‖ ^ (-p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's theorem for functions of negative order](../complex/part-02/liouvilles-theorem-for-functions-of-negative-ord.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrderLE.summable_divisor_mul_norm_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder/Zero/Summability.html#TauCeti.OrderLE.summable_divisor_mul_norm_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.OrderLE.summable_divisor_mul_norm_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder/Zero/Summability.html#TauCeti.OrderLE.summable_divisor_mul_norm_rpow)
- [Source of `TauCeti.OrderLE.summable_divisor_mul_norm_rpow` in TauCeti/Analysis/Complex/GrowthOrder/Zero/Summability.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/GrowthOrder/Zero/Summability.lean#L39)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
