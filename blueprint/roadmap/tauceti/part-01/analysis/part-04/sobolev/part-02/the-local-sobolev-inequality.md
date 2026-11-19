---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one
statement: formalized
proof: formalized
---

# The local Sobolev inequality

Let `1 ≤ q ≤ s < ∞` with `1/q - 1/s ≤ 1/2`, and let `V` have
compact closure inside the open set `W ⊆ ℂ`. There is a constant `C` such that every
`u : ℂ → F` satisfies `‖u‖_{L^s(V)} ≤ C ‖u‖_{W^{1,q}(W)}`. The case `1/s = 1/q - 1/2` is the
critical Sobolev embedding for `q < 2`; for `q ≥ 2` every finite `s ≥ q` is allowed.

```lean
TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {q s : NNReal} {W : TopologicalSpace.Opens ℂ} {V : Set ℂ}
  [FiniteDimensional ℝ F] (hq : 1 ≤ q) (hqs : q ≤ s) (hgap : (↑q)⁻¹ - (↑s)⁻¹ ≤ 2⁻¹)
  (hVc : IsCompact (closure V)) (hVW : closure V ⊆ ↑W) :
  ∃ C,
    ∀ (u : ℂ → F),
      MeasureTheory.eLpNorm u (↑s) (MeasureTheory.volume.restrict V) ≤
        ↑C * TauCeti.eLpNormWkp (↑q) (↑W) 1 u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The interior Sobolev inequality](../part-01/the-interior-sobolev-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/SobolevEmbedding.html#TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/SobolevEmbedding.html#TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one)
- [Source of `TauCeti.exists_eLpNorm_le_mul_eLpNormWkp_one` in TauCeti/Analysis/Sobolev/Local/SobolevEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Local/SobolevEmbedding.lean#L137)
