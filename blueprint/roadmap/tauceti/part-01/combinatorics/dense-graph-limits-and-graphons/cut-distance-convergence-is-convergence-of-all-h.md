---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto
statement: formalized
proof: formalized
---

# Cut-distance convergence is convergence of all homomorphism densities

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

- [A measurable function on a product factors through Boolean coordinates](a-measurable-function-on-a-product-factors-throu.md)
- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [Hoeffding's lemma, oscillation form](../../probability/moments/part-01/hoeffdings-lemma-oscillation-form.md)
- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr](tauceti-densegraphlimits-graphon-unitintervalrep.md)
- [TauCeti.Probability.empiricalFiniteMeasure](../../probability/random-matrices/tauceti-probability-empiricalfinitemeasure.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.html#TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto)
- [Source of `TauCeti.DenseGraphLimits.tendsto_cutDist_iff_forall_homDensity_tendsto` in TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Convergence.lean#L152)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/DenseGraphLimits/STATUS.md)
