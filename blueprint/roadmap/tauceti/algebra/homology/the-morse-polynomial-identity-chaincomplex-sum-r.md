---
declaration: theorem
origin: cited
lean: ChainComplex.sum_range_monomial_finrank_X_eq, TauCeti.exists_sum_range_monomial_eq_add_mul
statement: formalized
proof: formalized
---

# The Morse polynomial identity (`ChainComplex.sum_range_monomial_finrank_X_eq`)

If the terms of `K` through degree `n` are
finite-dimensional and the differential `Kₙ₊₁ ⟶ Kₙ` vanishes, then in `ℕ[X]`
`∑ᵢ₌₀ⁿ cᵢ Xⁱ = ∑ᵢ₌₀ⁿ bᵢ Xⁱ + (1 + X) Q`, where `cᵢ` is the dimension of `Kᵢ`, `bᵢ` that of
`Hᵢ(K)`, and `Q = ∑ᵢ₌₀ⁿ⁻¹ qᵢ Xⁱ` with `qᵢ` the rank of `Kᵢ₊₁ ⟶ Kᵢ`: the coefficient of `Xⁱ` in
`Q` is that rank for `i < n` and zero otherwise.

```lean
ChainComplex.sum_range_monomial_finrank_X_eq.{u, v} {k : Type u} [DivisionRing k]
  (K : ChainComplex (ModuleCat k) ℕ) {n : ℕ} (hfinite : ∀ i ≤ n, Module.Finite k ↑(K.X i))
  (hn : K.d (n + 1) n = 0) :
  ∑ i ∈ Finset.range (n + 1), (Polynomial.monomial i) (Module.finrank k ↑(K.X i)) =
    ∑ i ∈ Finset.range (n + 1),
        (Polynomial.monomial i) (Module.finrank k ↑(HomologicalComplex.homology K i)) +
      (1 + Polynomial.X) *
        ∑ i ∈ Finset.range n,
          (Polynomial.monomial i) (Module.finrank k ↥(ModuleCat.Hom.hom (K.d (i + 1) i)).range)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The truncated Morse polynomial identity](the-truncated-morse-polynomial-identity.md)

## Lean

Formalized in Tau Ceti as [`ChainComplex.sum_range_monomial_finrank_X_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#ChainComplex.sum_range_monomial_finrank_X_eq).

## Other forms

**The Morse polynomial identity from the strong inequalities.** Formalized in Tau Ceti as [`TauCeti.exists_sum_range_monomial_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#TauCeti.exists_sum_range_monomial_eq_add_mul).

```lean
TauCeti.exists_sum_range_monomial_eq_add_mul {b c : ℕ → ℕ} {n : ℕ}
  (hstrong :
    ∀ m < n,
      ∑ i ∈ Finset.range (m + 1), (-1) ^ (m - i) * ↑(b i) ≤
        ∑ i ∈ Finset.range (m + 1), (-1) ^ (m - i) * ↑(c i))
  (heuler :
    ∑ i ∈ Finset.range (n + 1), (-1) ^ i * ↑(b i) = ∑ i ∈ Finset.range (n + 1), (-1) ^ i * ↑(c i)) :
  ∃ Q,
    ∑ i ∈ Finset.range (n + 1), (Polynomial.monomial i) (c i) =
        ∑ i ∈ Finset.range (n + 1), (Polynomial.monomial i) (b i) + (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          ↑(Q.coeff i) =
            ∑ j ∈ Finset.range (i + 1), (-1) ^ (i - j) * ↑(c j) -
              ∑ j ∈ Finset.range (i + 1), (-1) ^ (i - j) * ↑(b j)) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

## Sources

- [Tau Ceti documentation: `ChainComplex.sum_range_monomial_finrank_X_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#ChainComplex.sum_range_monomial_finrank_X_eq)
- [Source of `ChainComplex.sum_range_monomial_finrank_X_eq` in TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.lean#L203)
