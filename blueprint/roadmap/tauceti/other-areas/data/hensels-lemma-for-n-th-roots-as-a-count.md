---
declaration: theorem
origin: cited
lean: ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots
statement: formalized
proof: formalized
---

# Hensel's lemma for `n`-th roots, as a count

For `n` coprime to the prime `p`, an integer
`a` prime to `p` and `k ≠ 0`, reduction modulo `p` is a bijection from the `n`-th roots of `a`
modulo `p ^ k` to those modulo `p`; so there are equally many.

```lean
ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots {p n k : ℕ} [Fact (Nat.Prime p)]
  (hn : n.Coprime p) (hk : k ≠ 0) {a : ℤ} (ha : ↑a ≠ 0) :
  Nat.card { x // x ^ n = ↑a } = Nat.card { x // x ^ n = ↑a }
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/PrincipalUnits.html#ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots).

## Sources

- [Tau Ceti documentation: `ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/PrincipalUnits.html#ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots)
- [Source of `ZMod.natCard_nthRoots_prime_pow_eq_natCard_nthRoots` in TauCeti/Data/ZMod/PrincipalUnits.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Data/ZMod/PrincipalUnits.lean#L96)
