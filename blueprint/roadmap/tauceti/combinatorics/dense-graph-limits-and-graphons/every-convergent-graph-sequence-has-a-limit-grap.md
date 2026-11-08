---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq
statement: formalized
proof: formalized
---

# Every convergent graph sequence has a limit graphon

**Every convergent graph sequence has a limit graphon** (Lovász--Szegedy), on every atomless
standard Borel carrier `(Ω, μ)`, such as the unit interval. A sequence of finite graphs on nonempty
vertex sets converges in the cut distance of step graphons to some graphon on `(Ω, μ)` if and only
if every finite homomorphism density `t(F, Gₙ)` is a Cauchy, hence convergent, sequence.

```lean
TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq.{u_1}
  {Ω : Type u_1} [MeasurableSpace Ω] (μ : MeasureTheory.Measure Ω)
  [MeasureTheory.IsProbabilityMeasure μ] {m : ℕ → ℕ} [StandardBorelSpace Ω]
  [MeasureTheory.NullSingletonClass μ] (hm : ∀ (n : ℕ), 0 < m n)
  (G : (n : ℕ) → SimpleGraph (Fin (m n))) :
  (∃ W,
      Filter.Tendsto
        (fun n =>
          TauCeti.DenseGraphLimits.cutDist (TauCeti.DenseGraphLimits.finiteGraphGraphon (G n)) W)
        Filter.atTop (nhds 0)) ↔
    ∀ (n : ℕ) (F : SimpleGraph (Fin n)) [DecidableRel F.Adj],
      CauchySeq fun k => TauCeti.DenseGraphLimits.homDensityFin F (G k)
```

## Depends on

- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)

## Proof depends on

- [Cut-distance convergence is convergence of all homomorphism densities](cut-distance-convergence-is-convergence-of-all-h.md)
- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr](tauceti-densegraphlimits-graphon-unitintervalrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq)
- [Source of `TauCeti.DenseGraphLimits.exists_graphon_tendsto_cutDist_finiteGraphGraphon_iff_forall_homDensityFin_cauchySeq` in TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean#L256)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
