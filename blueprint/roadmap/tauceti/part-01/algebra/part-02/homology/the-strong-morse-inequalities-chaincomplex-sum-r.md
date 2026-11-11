---
declaration: theorem
origin: cited
lean: ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le
statement: formalized
proof: formalized
---

# The strong Morse inequalities (`ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le`)

If the terms of `K` through degree `n` are
finite-dimensional, then `bₙ - bₙ₋₁ + ⋯ ± b₀ ≤ cₙ - cₙ₋₁ + ⋯ ± c₀`, where `bᵢ` is the dimension
of `Hᵢ(K)` and `cᵢ` that of `Kᵢ`.  The difference of the two sides is the rank of `Kₙ₊₁ ⟶ Kₙ`.

```lean
ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le.{u, v} {k : Type u} [DivisionRing k]
  (K : ChainComplex (ModuleCat k) ℕ) (n : ℕ) (hfinite : ∀ i ≤ n, Module.Finite k ↑(K.X i)) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(Module.finrank k ↑(HomologicalComplex.homology K i)) ≤
    ∑ i ∈ Finset.range (n + 1), (-1) ^ (n - i) * ↑(Module.finrank k ↑(K.X i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le).

## Sources

- [Tau Ceti documentation: `ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.html#ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le)
- [Source of `ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le` in TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/EulerCharacteristic/MorseInequalities.lean#L171)
