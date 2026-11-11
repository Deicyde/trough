---
declaration: theorem
origin: cited
lean: PeriodPair.weierstrassP_add
statement: formalized
proof: formalized
---

# The addition theorem for `℘`

If `z, w ∉ Λ` and `℘(z) ≠ ℘(w)`, then
`℘(z + w) = ((℘'(z) - ℘'(w)) / (℘(z) - ℘(w)))² / 4 - ℘(z) - ℘(w)`.

```lean
PeriodPair.weierstrassP_add (L : PeriodPair) {z w : ℂ} (hz : z ∉ L.lattice) (hw : w ∉ L.lattice)
  (h : L.weierstrassP z ≠ L.weierstrassP w) :
  L.weierstrassP (z + w) =
    ((L.derivWeierstrassP z - L.derivWeierstrassP w) / (L.weierstrassP z - L.weierstrassP w)) ^ 2 /
          4 -
        L.weierstrassP z -
      L.weierstrassP w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PeriodPair.weierstrassP_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.html#PeriodPair.weierstrassP_add).

## Sources

- [Tau Ceti documentation: `PeriodPair.weierstrassP_add`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.html#PeriodPair.weierstrassP_add)
- [Source of `PeriodPair.weierstrassP_add` in TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Elliptic/AdditionTheorem.lean#L296)
