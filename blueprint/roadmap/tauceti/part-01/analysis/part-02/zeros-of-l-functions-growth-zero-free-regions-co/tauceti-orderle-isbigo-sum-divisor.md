---
declaration: theorem
origin: cited
lean: TauCeti.OrderLE.isBigO_sum_divisor
statement: formalized
proof: formalized
---

# TauCeti.OrderLE.isBigO_sum_divisor

The zero count, with multiplicity, of an entire function of order at most `A`
is `O(R ^ B)` for every `B > A`, provided the function is nonzero at the origin.

```lean
TauCeti.OrderLE.isBigO_sum_divisor {f : ℂ → ℂ} {A B : ℝ} (h : TauCeti.OrderLE f A)
  (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (hAB : A < B) :
  (fun R => ↑(∑ᶠ (z : ℂ), (MeromorphicOn.divisor f (Metric.closedBall 0 R)) z)) =O[Filter.atTop]
    fun R => R ^ B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Liouville's theorem for functions of negative order](../complex/part-02/liouvilles-theorem-for-functions-of-negative-ord.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OrderLE.isBigO_sum_divisor`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder/Zero/Count.html#TauCeti.OrderLE.isBigO_sum_divisor).

## Sources

- [Tau Ceti documentation: `TauCeti.OrderLE.isBigO_sum_divisor`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/GrowthOrder/Zero/Count.html#TauCeti.OrderLE.isBigO_sum_divisor)
- [Source of `TauCeti.OrderLE.isBigO_sum_divisor` in TauCeti/Analysis/Complex/GrowthOrder/Zero/Count.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/GrowthOrder/Zero/Count.lean#L111)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
