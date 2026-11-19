---
declaration: theorem
origin: cited
lean: TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le
statement: formalized
proof: formalized
---

# The resonant estimate (Bahouri–Chemin–Danchin, Theorem 2.85)

Let `0 < α + β` and let `N`
be a gap. There is `C ≥ 0`, depending only on `φ`, `N`, `α` and `β`, with the following property
for all exponents `1 ≤ p₁, p₂, r, q, q₁ ≤ ∞` with `1/r = 1/p₁ + 1/p₂`. If `u ∈ B^α_{p₁,q₁}` and
`v ∈ B^β_{p₂,q}`, then the resonant part `R(u, v) = ∑ⱼ Δⱼ u · ∑_{|k - j| ≤ N} Δₖ v` converges in
the tempered distributions to an element of `B^{α+β}_{r,q}` of norm at most `C ‖u‖ ‖v‖`.

```lean
TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] [CompleteSpace F]
  (φ : ContDiffBump 0) {α β : ℝ} (hαβ : 0 < α + β) (N : ℕ) :
  ∃ C,
    0 ≤ C ∧
      ∀ {p₁ p₂ r q q₁ : ENNReal} [inst : Fact (1 ≤ p₁)] [inst_1 : Fact (1 ≤ p₂)]
        [inst_2 : Fact (1 ≤ r)] [inst_3 : Fact (1 ≤ q)] [inst_4 : Fact (1 ≤ q₁)]
        [inst_5 : p₁.HolderTriple p₂ r] (u : TauCeti.BesovSpace ℂ φ α p₁ q₁)
        (v : TauCeti.BesovSpace F φ β p₂ q),
        ∃ w,
          HasSum
              (fun j =>
                MeasureTheory.Lp.toTemperedDistribution
                  (u.block j • ∑ k ∈ Finset.Icc (j - N) (j + N), v.block k))
              w.toDistr ∧
            ‖w‖ ≤ C * ‖u‖ * ‖v‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Young's convolution inequality](../../part-03/convolution/youngs-convolution-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.html#TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le).

## Sources

- [Tau Ceti documentation: `TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.html#TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le)
- [Source of `TauCeti.BesovSpace.exists_hasSum_block_smul_sum_block_and_norm_le` in TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/FunctionalSpaces/BesovSpace/Paraproduct.lean#L616)
