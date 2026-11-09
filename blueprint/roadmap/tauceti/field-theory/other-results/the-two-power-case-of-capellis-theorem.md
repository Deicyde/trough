---
declaration: theorem
origin: cited
lean: TauCeti.X_pow_two_pow_sub_C_irreducible
statement: formalized
proof: formalized
---

# The two-power case of Capelli's theorem

Over any field `K`, if `a` is not a square
in `K` and, when `k ≥ 2`, `a` is not of the form `-4b⁴`, then `X^(2ᵏ) - a` is irreducible.
The second condition cannot be dropped: `X⁴ + 4` is reducible over `ℚ`.

```lean
TauCeti.X_pow_two_pow_sub_C_irreducible.{u_1} {K : Type u_1} [Field K] (k : ℕ) {a : K}
  (ha : ∀ (b : K), b ^ 2 ≠ a) (ha' : 2 ≤ k → ∀ (b : K), -4 * b ^ 4 ≠ a) :
  Irreducible (Polynomial.X ^ 2 ^ k - Polynomial.C a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.X_pow_two_pow_sub_C_irreducible`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Kummer/Capelli.html#TauCeti.X_pow_two_pow_sub_C_irreducible).

## Sources

- [Tau Ceti documentation: `TauCeti.X_pow_two_pow_sub_C_irreducible`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Kummer/Capelli.html#TauCeti.X_pow_two_pow_sub_C_irreducible)
- [Source of `TauCeti.X_pow_two_pow_sub_C_irreducible` in TauCeti/FieldTheory/Kummer/Capelli.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/Kummer/Capelli.lean#L106)
