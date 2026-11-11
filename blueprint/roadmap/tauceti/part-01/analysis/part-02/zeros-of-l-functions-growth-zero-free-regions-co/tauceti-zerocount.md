---
declaration: def
origin: cited
lean: TauCeti.zeroCount
statement: formalized
---

# TauCeti.zeroCount

The sum of positive divisor multiplicities in `R`; poles and infinite order contribute zero.
On infinite support this takes the default value zero.

```lean
TauCeti.zeroCount.{u_1, u_2} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2}
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] (f : 𝕜 → E) (U R : Set 𝕜) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zeroCount`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Basic.html#TauCeti.zeroCount).

## Sources

- [Tau Ceti documentation: `TauCeti.zeroCount`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Basic.html#TauCeti.zeroCount)
- [Source of `TauCeti.zeroCount` in TauCeti/Analysis/Meromorphic/Counting/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Meromorphic/Counting/Basic.lean#L38)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
