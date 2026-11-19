---
declaration: theorem
origin: cited
lean: ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le, TauCeti.CompactChartAtlas.CkHolderSpace.norm_chartIteratedFDeriv_sub_le
statement: formalized
proof: formalized
---

# Hölder estimate

On a map whose coordinate derivative is Hölder, the Hölder seminorm
bounds the oscillation of the `k`th coordinate derivative on `K`.

```lean
ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {F : Type u_5} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {n : WithTop ℕ∞}
  [IsManifold I n M] {x : M} {K : Set ↑(extChartAt I x).target} {k : ℕ} {hk : ↑k ≤ n} {α : NNReal}
  {f : ContMDiffMap I (modelWithCornersSelf 𝕜 F) M F n}
  (hf : ContMDiffMap.MemChartHolder x K k hk α f) {z w : ↑(extChartAt I x).target} (hz : z ∈ K)
  (hw : w ∈ K) :
  ‖(f.chartIteratedFDeriv x k hk) z - (f.chartIteratedFDeriv x k hk) w‖ ≤
    ↑(ContMDiffMap.chartHolderNorm x K k hk α f) * dist z w ^ ↑α
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Chart/Holder.html#ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le).

## Other forms

**Hölder estimate.** Formalized in Tau Ceti as [`TauCeti.CompactChartAtlas.CkHolderSpace.norm_chartIteratedFDeriv_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Chart/Holder.html#TauCeti.CompactChartAtlas.CkHolderSpace.norm_chartIteratedFDeriv_sub_le).

```lean
TauCeti.CompactChartAtlas.CkHolderSpace.norm_chartIteratedFDeriv_sub_le.{u_1, u_2, u_3, u_4, u_5}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_4}
  [TopologicalSpace M] [ChartedSpace H M] {A : TauCeti.CompactChartAtlas I M} {k : ℕ} {α : NNReal}
  {F : Type u_5} [NormedAddCommGroup F] [NormedSpace 𝕜 F] [IsManifold I (↑k) M]
  (f : A.CkHolderSpace k α F) (i : A.ι) {z w : ↑(extChartAt I (A.center i)).target}
  (hz : z ∈ A.piece i) (hw : w ∈ A.piece i) :
  ‖(((TauCeti.CompactChartAtlas.CkHolderSpace.toContMDiffMap A k α F) f).chartIteratedFDeriv
            (A.center i) k ⋯)
          z -
        (((TauCeti.CompactChartAtlas.CkHolderSpace.toContMDiffMap A k α F) f).chartIteratedFDeriv
            (A.center i) k ⋯)
          w‖ ≤
    ‖f‖ * dist z w ^ ↑α
```

## Sources

- [Tau Ceti documentation: `ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ContMDiffMap/Chart/Holder.html#ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le)
- [Source of `ContMDiffMap.MemChartHolder.norm_chartIteratedFDeriv_sub_le` in TauCeti/Geometry/Manifold/ContMDiffMap/Chart/Holder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/ContMDiffMap/Chart/Holder.lean#L185)
