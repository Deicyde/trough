---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto
statement: formalized
proof: formalized
---

# TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto

**Cut-distance convergence is convergence of all homomorphism densities**, for graphons on
arbitrary, possibly different, probability carriers, indexed by any type and taken along any
filter: `δ□(Wᵢ, W) → 0` if and only if `t(F, Wᵢ) → t(F, W)` for every finite simple graph `F`.
Sequences are the case of `atTop` on `ℕ`.

```lean
TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto.{u_1, u_3, u_4}
  {Ω' : Type u_1} [MeasurableSpace Ω'] {μ' : MeasureTheory.Measure Ω'}
  [MeasureTheory.IsProbabilityMeasure μ'] {ι : Type u_3} {l : Filter ι} {Ωι : ι → Type u_4}
  [(i : ι) → MeasurableSpace (Ωι i)] {μι : (i : ι) → MeasureTheory.Measure (Ωι i)}
  [∀ (i : ι), MeasureTheory.IsProbabilityMeasure (μι i)]
  (Ws : (i : ι) → TauCeti.DenseGraphLimits.Graphon (Ωι i) (μι i))
  (W : TauCeti.DenseGraphLimits.Graphon Ω' μ') :
  Filter.Tendsto (fun i => TauCeti.DenseGraphLimits.cutDist (Ws i) W) l (nhds 0) ↔
    ∀ (n : ℕ) (F : SimpleGraph (Fin n)) [inst : DecidableRel F.Adj],
      Filter.Tendsto (fun i => TauCeti.DenseGraphLimits.homDensity F (Ws i)) l
        (nhds (TauCeti.DenseGraphLimits.homDensity F W))
```

## Depends on

- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)

## Proof depends on

- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr](tauceti-densegraphlimits-graphon-unitintervalrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto)
- [Source of `TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto` in TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean#L152)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
