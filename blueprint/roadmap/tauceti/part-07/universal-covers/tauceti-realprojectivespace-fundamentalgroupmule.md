---
declaration: def
origin: cited
lean: TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt
statement: formalized
---

# TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt

**The fundamental group of real projective space `RPⁿ` (for `2 ≤ n`) is isomorphic to `ℤˣ`
for any basepoint `x`**: `FundamentalGroup (RealProjectiveSpace n) x ≃* ℤˣ`.

```lean
TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt (n : ℕ) (hn : 2 ≤ n)
  (x : TauCeti.RealProjectiveSpace n) : FundamentalGroup (TauCeti.RealProjectiveSpace n) x ≃* ℤˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.simplyConnectedSpace\_sphere](tauceti-simplyconnectedspace-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.html#TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt).

## Sources

- [Tau Ceti documentation: `TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.html#TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt)
- [Source of `TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt` in TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.lean#L135)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/UniversalCovers/STATUS.md)
