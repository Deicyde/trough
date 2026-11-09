---
declaration: theorem
origin: cited
lean: Finset.two_mul_sum_range_choose_add_sum_sum_tsub
statement: formalized
proof: formalized
---

# The Conway–Sloane exponent identity

Twice `∑_{j < max k} binom(Nⱼ + 1, 2)`, where
`Nⱼ = #{i ∈ s | j < kᵢ}`, plus `∑_{i, i' ∈ s} (k_{i'} - kᵢ)` (truncated subtraction) is
`(#s + 1) ∑_{i ∈ s} kᵢ`. The first sum is the exponent of `p` in the local density of the
diagonal Jordan form `diag(uᵢ pᵏⁱ)` at an odd prime, the second is the exponent of `√p` in the
cross terms of its Conway–Sloane `p`-mass.

```lean
Finset.two_mul_sum_range_choose_add_sum_sum_tsub.{u_1} {ι : Type u_1} (s : Finset ι) (k : ι → ℕ) :
  2 * ∑ j ∈ Finset.range (s.sup k), ({i ∈ s | j < k i}.card + 1).choose 2 +
      ∑ i ∈ s, ∑ i' ∈ s, (k i' - k i) =
    (s.card + 1) * ∑ i ∈ s, k i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Finset.two_mul_sum_range_choose_add_sum_sum_tsub`](https://taucetiproject.org/docs/TauCeti/Algebra/BigOperators/Finset/LayerCake.html#Finset.two_mul_sum_range_choose_add_sum_sum_tsub).

## Sources

- [Tau Ceti documentation: `Finset.two_mul_sum_range_choose_add_sum_sum_tsub`](https://taucetiproject.org/docs/TauCeti/Algebra/BigOperators/Finset/LayerCake.html#Finset.two_mul_sum_range_choose_add_sum_sum_tsub)
- [Source of `Finset.two_mul_sum_range_choose_add_sum_sum_tsub` in TauCeti/Algebra/BigOperators/Finset/LayerCake.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/BigOperators/Finset/LayerCake.lean#L72)
