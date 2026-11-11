---
declaration: theorem
origin: cited
lean: PeriodPair.derivWeierstrassP_add
statement: formalized
proof: formalized
---

# The addition theorem for `℘'`

If `z, w ∉ Λ` and `℘(z) ≠ ℘(w)`, then
`℘'(z + w) = -m (℘(z + w) - ℘(z)) - ℘'(z)` with `m = (℘'(z) - ℘'(w)) / (℘(z) - ℘(w))`: the points
`(℘(z), ℘'(z))`, `(℘(w), ℘'(w))` and `(℘(z + w), -℘'(z + w))` lie on a line of slope `m`.

```lean
PeriodPair.derivWeierstrassP_add (L : PeriodPair) {z w : ℂ} (hz : z ∉ L.lattice)
  (hw : w ∉ L.lattice) (h : L.weierstrassP z ≠ L.weierstrassP w) :
  L.derivWeierstrassP (z + w) =
    -((L.derivWeierstrassP z - L.derivWeierstrassP w) / (L.weierstrassP z - L.weierstrassP w)) *
        (L.weierstrassP (z + w) - L.weierstrassP z) -
      L.derivWeierstrassP z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The addition theorem for `℘`](the-addition-theorem-for-2.md)

## Lean

Formalized in Tau Ceti as [`PeriodPair.derivWeierstrassP_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.html#PeriodPair.derivWeierstrassP_add).

## Sources

- [Tau Ceti documentation: `PeriodPair.derivWeierstrassP_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.html#PeriodPair.derivWeierstrassP_add)
- [Source of `PeriodPair.derivWeierstrassP_add` in TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.lean#L305)
