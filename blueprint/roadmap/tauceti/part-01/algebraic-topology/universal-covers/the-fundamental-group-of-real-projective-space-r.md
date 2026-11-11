---
declaration: def
origin: cited
lean: TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt
statement: formalized
---

# The fundamental group of real projective space `RPⁿ` (for `2 ≤ n`) is isomorphic to `ℤˣ` for any basepoint `x`

`FundamentalGroup (RealProjectiveSpace n) x ≃* ℤˣ`.

```lean
TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt (n : ℕ) (hn : 2 ≤ n)
  (x : TauCeti.RealProjectiveSpace n) : FundamentalGroup (TauCeti.RealProjectiveSpace n) x ≃* ℤˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.simplyConnectedSpace_sphere](tauceti-simplyconnectedspace-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.html#TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt).

## Sources

- [Tau Ceti documentation: `TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.html#TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt)
- [Source of `TauCeti.RealProjectiveSpace.fundamentalGroupMulEquivAt` in TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/UniversalCover/RealProjective/FundamentalGroup/Basic.lean#L135)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/UniversalCovers/STATUS.md)
