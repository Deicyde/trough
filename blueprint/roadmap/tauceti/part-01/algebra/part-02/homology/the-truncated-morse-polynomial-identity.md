---
declaration: theorem
origin: cited
lean: ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq
statement: formalized
proof: formalized
---

# The truncated Morse polynomial identity

If the terms of `K` through degree `n` are
finite-dimensional, then in `ℕ[X]`
`∑ᵢ₌₀ⁿ cᵢ Xⁱ + qₙ Xⁿ⁺¹ = ∑ᵢ₌₀ⁿ bᵢ Xⁱ + (1 + X) ∑ᵢ₌₀ⁿ qᵢ Xⁱ`, where `cᵢ` is the dimension of `Kᵢ`,
`bᵢ` that of `Hᵢ(K)` and `qᵢ` the rank of `Kᵢ₊₁ ⟶ Kᵢ`.

```lean
ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq.{u, v} {k : Type u} [DivisionRing k]
  (K : ChainComplex (ModuleCat k) ℕ) (n : ℕ) (hfinite : ∀ i ≤ n, Module.Finite k ↑(K.X i)) :
  ∑ i ∈ Finset.range (n + 1), (Polynomial.monomial i) (Module.finrank k ↑(K.X i)) +
      (Polynomial.monomial (n + 1)) (Module.finrank k ↥(ModuleCat.Hom.hom (K.d (n + 1) n)).range) =
    ∑ i ∈ Finset.range (n + 1),
        (Polynomial.monomial i) (Module.finrank k ↑(HomologicalComplex.homology K i)) +
      (1 + Polynomial.X) *
        ∑ i ∈ Finset.range (n + 1),
          (Polynomial.monomial i) (Module.finrank k ↥(ModuleCat.Hom.hom (K.d (i + 1) i)).range)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq).

## Sources

- [Tau Ceti documentation: `ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq)
- [Source of `ChainComplex.sum_range_monomial_finrank_X_add_monomial_eq` in TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.lean#L186)
