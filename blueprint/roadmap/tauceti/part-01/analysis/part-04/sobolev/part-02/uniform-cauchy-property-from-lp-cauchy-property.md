---
declaration: theorem
origin: cited
lean: TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub
statement: formalized
proof: formalized
---

# Uniform Cauchy property from `Lᵖ` Cauchy property and `W^{1,p}` bounds

Let `2 < p ≤ ∞`.
Let `f m` be locally `Lᵖ` on `Ω` with weak derivatives `D m` on `Ω` which are bounded in `Lᵖ(K)`
uniformly in `m` for every compact `K ⊆ Ω`, and suppose that `‖f m - f n‖_{Lᵖ(K)} → 0` as
`m, n → ∞` for every compact `K ⊆ Ω`. Then the precise representatives of the `f m` are uniformly
Cauchy on every compact subset of `Ω`. The proof applies the local Morrey sup bound
`TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le` to `f m - f n` on balls of a small
radius `r`: the derivative term is small for small `r`, and the `Lᵖ` term for large `m` and `n`.

```lean
TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {p : ENNReal}
  {Ω : TopologicalSpace.Opens ℂ} (hp : 2 < p) {f : ℕ → ℂ → F} {D : ℕ → ℂ → ℂ →L[ℝ] F}
  (hf : ∀ (m : ℕ), TauCeti.MemLpLoc p (↑Ω) (f m))
  (hD : ∀ (m : ℕ), TauCeti.HasWeakFDerivOn MeasureTheory.volume Ω (f m) (D m))
  (hDbdd :
    ∀ (K : Set ℂ),
      IsCompact K →
        K ⊆ ↑Ω →
          ∃ M, ∀ (m : ℕ), MeasureTheory.eLpNorm (D m) p (MeasureTheory.volume.restrict K) ≤ ↑M)
  (hfc :
    ∀ (K : Set ℂ),
      IsCompact K →
        K ⊆ ↑Ω →
          Filter.Tendsto
            (fun mn => MeasureTheory.eLpNorm (f mn.1 - f mn.2) p (MeasureTheory.volume.restrict K))
            (Filter.atTop ×ˢ Filter.atTop) (nhds 0))
  {K : Set ℂ} (hK : IsCompact K) (hKΩ : K ⊆ ↑Ω) :
  UniformCauchySeqOn
    (fun m => TauCeti.MeasureTheory.preciseRepresentative MeasureTheory.volume (f m)) Filter.atTop K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local Morrey inequality](../part-01/the-local-morrey-inequality.md)
- [The local Morrey sup bound](../part-01/the-local-morrey-sup-bound.md)
- [TauCeti.MemWkpLoc](../../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-memwkploc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Compactness/Uniform.html#TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Compactness/Uniform.html#TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub)
- [Source of `TauCeti.uniformCauchySeqOn_preciseRepresentative_of_tendsto_eLpNorm_sub` in TauCeti/Analysis/Sobolev/Local/Compactness/Uniform.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Local/Compactness/Uniform.lean#L96)
