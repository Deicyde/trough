---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsPrCompact.finrank_ker_pow
statement: formalized
proof: formalized
---

# ContinuousLinearMap.IsPrCompact.finrank_ker_pow

Over a complete ultrametric field, a good Fredholm zero of order `h` on a module
with property (Pr) has stabilized generalized eigenspaces of dimension `h`.

```lean
ContinuousLinearMap.IsPrCompact.finrank_ker_pow.{u_1, u_2} {K : Type u_1} {M : Type u_2}
  [NontriviallyNormedField K] [IsUltrametricDist K] [CompleteSpace K] [SeminormedAddCommGroup M]
  [_root_.Module K M] [ContinuousConstSMul K M] {u : M →L[K] M} {a : K} {h n : ℕ}
  (hu : u.IsPrCompact) (hH : u.charPowerSeries.IsGoodZero a h) (hn : h ≤ n) :
  Module.finrank K ↥(↑((1 - a • u) ^ n)).ker = h
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [Constant rank of the Riesz summand](constant-rank-of-the-riesz-summand.md)
- [The Riesz identity at a good zero](the-riesz-identity-at-a-good-zero.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsPrCompact.finrank_ker_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/PrModule.html#ContinuousLinearMap.IsPrCompact.finrank_ker_pow).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsPrCompact.finrank_ker_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/PrModule.html#ContinuousLinearMap.IsPrCompact.finrank_ker_pow)
- [Source of `ContinuousLinearMap.IsPrCompact.finrank_ker_pow` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/PrModule.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Nonarchimedean/RieszProjection/PrModule.lean#L191)
- [Tau Ceti roadmap status: Compact operators and nonarchimedean Fredholm theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CompactOperators/STATUS.md)
