---
declaration: theorem
origin: cited
lean: FormalGroup.exists_order_nsmulSeries_eq_pow
statement: formalized
proof: formalized
---

# The `p`-series has order a power of `p`

in characteristic `p`: if `p` is a prime with
`p = 0` in `R` and `F` is commutative, then either `[p]_F = 0` or the first nonzero term of
`[p]_F` has degree `p ^ h` for some `h ≥ 1`.

```lean
FormalGroup.exists_order_nsmulSeries_eq_pow.{u_1} {R : Type u_1} [CommRing R] (F : FormalGroup R)
  [F.IsComm] {p : ℕ} (hp : Nat.Prime p) (hpR : ↑p = 0) (h0 : F.nsmulSeries p ≠ 0) :
  ∃ h, h ≠ 0 ∧ (F.nsmulSeries p).order = ↑(p ^ h)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`FormalGroup.exists_order_nsmulSeries_eq_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Basic.html#FormalGroup.exists_order_nsmulSeries_eq_pow).

## Sources

- [Tau Ceti documentation: `FormalGroup.exists_order_nsmulSeries_eq_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Height/Basic.html#FormalGroup.exists_order_nsmulSeries_eq_pow)
- [Source of `FormalGroup.exists_order_nsmulSeries_eq_pow` in TauCeti/RingTheory/FormalGroup/Height/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/Height/Basic.lean#L182)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
