---
declaration: def
origin: cited
lean: FormalGroup.height
statement: formalized
---

# FormalGroup.height

The **height** of a formal group law `F` over a field `K` of characteristic `p`: `⊤` if
multiplication by `p` on `F` is zero, and otherwise the exponent `h` such that the first nonzero
term of `[p]_F(T)` has degree `p ^ h` (see `FormalGroup.height_eq_natCast_iff`).

```lean
FormalGroup.height.{u_1} {K : Type u_1} [Field K] (F : FormalGroup K) (p : ℕ) : ℕ∞
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FormalGroup.height`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Basic.html#FormalGroup.height).

## Sources

- [Tau Ceti documentation: `FormalGroup.height`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Basic.html#FormalGroup.height)
- [Source of `FormalGroup.height` in TauCeti/RingTheory/FormalGroup/Height/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/Height/Basic.lean#L202)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
