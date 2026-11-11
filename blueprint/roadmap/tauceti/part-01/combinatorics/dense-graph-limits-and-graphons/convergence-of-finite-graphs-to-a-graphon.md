---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto
statement: formalized
proof: formalized
---

# Convergence of finite graphs to a graphon

A family of finite graphs `Gᵢ` on nonempty
vertex sets, indexed by any type and taken along any filter, converges to a graphon `W`, on any
probability carrier, in the cut distance of their step graphons if and only if every finite
homomorphism density `t(F, Gᵢ)` converges to `t(F, W)`. Graph sequences are the case of `atTop`
on `ℕ`.

```lean
TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto.{u_1,
    u_2}
  {Ω : Type u_1} [MeasurableSpace Ω] {μ : MeasureTheory.Measure Ω}
  [MeasureTheory.IsProbabilityMeasure μ] {ι : Type u_2} {l : Filter ι} {mι : ι → ℕ}
  (hm : ∀ (i : ι), 0 < mι i) (G : (i : ι) → SimpleGraph (Fin (mι i)))
  (W : TauCeti.DenseGraphLimits.Graphon Ω μ) :
  Filter.Tendsto
      (fun i =>
        TauCeti.DenseGraphLimits.cutDist (TauCeti.DenseGraphLimits.finiteGraphGraphon (G i)) W)
      l (nhds 0) ↔
    ∀ (n : ℕ) (F : SimpleGraph (Fin n)) [inst : DecidableRel F.Adj],
      Filter.Tendsto (fun i => TauCeti.DenseGraphLimits.homDensityFin F (G i)) l
        (nhds (TauCeti.DenseGraphLimits.homDensity F W))
```

## Depends on

- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)

## Proof depends on

- [Cut-distance convergence is convergence of all homomorphism densities](cut-distance-convergence-is-convergence-of-all-h.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto)
- [Source of `TauCeti.DenseGraphLimits.tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_tendsto` in TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean#L230)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/DenseGraphLimits/STATUS.md)
