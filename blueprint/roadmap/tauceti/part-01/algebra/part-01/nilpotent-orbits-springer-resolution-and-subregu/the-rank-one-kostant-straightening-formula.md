---
declaration: theorem
origin: cited
lean: TauCeti.Sl2.dividedPower_e_mul_dividedPower_f
statement: formalized
proof: formalized
---

# The rank-one Kostant straightening formula

If `H`, `E`, and `F` satisfy the `sl₂`
commutator relations in an associative `ℚ`-algebra, then the product of a raising divided power
and a lowering divided power is an integral sum in PBW order `F`, `H`, `E`.

The argument of the Cartan binomial is written as `H - (m + n) + 2 * k`; the natural numbers are
coerced to the algebra, so this is the standard coefficient `(H - m - n + 2k choose k)`.

```lean
TauCeti.Sl2.dividedPower_e_mul_dividedPower_f.{u} {A : Type u} [Ring A] [Algebra ℚ A] {H E F : A}
  (hef : E * F - F * E = H) (hhe : H * E - E * H = 2 • E) (hhf : H * F - F * H = -(2 • F))
  (m n : ℕ) :
  TauCeti.Associative.dividedPower m E * TauCeti.Associative.dividedPower n F =
    ∑ k ∈ Finset.range (min m n + 1),
      TauCeti.Associative.dividedPower (n - k) F * Ring.choose (H - ↑(m + n) + ↑(2 * k)) k *
        TauCeti.Associative.dividedPower (m - k) E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Sl2.dividedPower_e_mul_dividedPower_f`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Straightening.html#TauCeti.Sl2.dividedPower_e_mul_dividedPower_f).

## Sources

- [Tau Ceti documentation: `TauCeti.Sl2.dividedPower_e_mul_dividedPower_f`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/Straightening.html#TauCeti.Sl2.dividedPower_e_mul_dividedPower_f)
- [Source of `TauCeti.Sl2.dividedPower_e_mul_dividedPower_f` in TauCeti/Algebra/Lie/Sl2/Straightening.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Sl2/Straightening.lean#L271)
