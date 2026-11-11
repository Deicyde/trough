---
declaration: def
origin: cited
lean: ZMod.unitsEquivPi
statement: formalized
---

# The Chinese remainder theorem for units

`(ℤ/n)ˣ` is the product of the unit groups
modulo the prime powers exactly dividing `n`.

```lean
ZMod.unitsEquivPi {n : ℕ} (hn : n ≠ 0) :
  (ZMod n)ˣ ≃* ((p : ↥n.primeFactors) → (ZMod (↑p ^ n.factorization ↑p))ˣ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZMod.unitsEquivPi`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/Divisibility.html#ZMod.unitsEquivPi).

## Sources

- [Tau Ceti documentation: `ZMod.unitsEquivPi`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/Divisibility.html#ZMod.unitsEquivPi)
- [Source of `ZMod.unitsEquivPi` in TauCeti/Data/ZMod/Divisibility.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/ZMod/Divisibility.lean#L193)
