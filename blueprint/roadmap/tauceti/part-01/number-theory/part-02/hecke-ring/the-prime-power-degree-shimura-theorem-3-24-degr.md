---
declaration: theorem
origin: cited
lean: HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow
statement: formalized
proof: formalized
---

# The prime-power degree (Shimura, Theorem 3.24, degree count)

for prime `p` and
`k ≥ 1`, a divisibility chain `a` of ratio `a₁ / a₀ = pᵏ` has `deg T(a₀, a₁) = pᵏ⁻¹ (p + 1)`.
The archetype is `a = (pⁱ, pⁱ⁺ᵏ)`.

```lean
HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow (p : ℕ) (hp : Nat.Prime p) (a : Fin 2 → ℕ)
  (hdiv : HeckeRing.GLn.IsDvdChain a) (k : ℕ) (hk : 0 < k) (h_ratio : a 1 / a 0 = p ^ k) :
  (HeckeRing.GLn.diagCoset a).degree = p ^ (k - 1) * (p + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GL2/DiagonalCosetDegree.html#HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/HeckeRing/GL2/DiagonalCosetDegree.html#HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow)
- [Source of `HeckeRing.GL2.degree_diagCoset_of_ratio_eq_prime_pow` in TauCeti/NumberTheory/HeckeRing/GL2/DiagonalCosetDegree.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/HeckeRing/GL2/DiagonalCosetDegree.lean#L178)
