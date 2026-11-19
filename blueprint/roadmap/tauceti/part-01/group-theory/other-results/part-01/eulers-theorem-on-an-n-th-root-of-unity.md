---
declaration: theorem
origin: cited
lean: TauCeti.pow_pow_totient_eq_self
statement: formalized
proof: formalized
---

# Euler's theorem on an `n`-th root of unity

if `x ^ n = 1` in a monoid and `q` is prime to
`n`, then `x ^ q ^ φ(n) = x`, since `q ^ φ(n) ≡ 1 [MOD n]`.

```lean
TauCeti.pow_pow_totient_eq_self.{u_1} {M : Type u_1} [Monoid M] {q n : ℕ} (hq : q.Coprime n) {x : M}
  (hx : x ^ n = 1) : x ^ q ^ n.totient = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.pow_pow_totient_eq_self`](https://taucetiproject.org/docs/TauCeti/GroupTheory/OrderOfElement/Basic.html#TauCeti.pow_pow_totient_eq_self).

## Sources

- [Tau Ceti documentation: `TauCeti.pow_pow_totient_eq_self`](https://taucetiproject.org/docs/TauCeti/GroupTheory/OrderOfElement/Basic.html#TauCeti.pow_pow_totient_eq_self)
- [Source of `TauCeti.pow_pow_totient_eq_self` in TauCeti/GroupTheory/OrderOfElement/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/OrderOfElement/Basic.lean#L171)
