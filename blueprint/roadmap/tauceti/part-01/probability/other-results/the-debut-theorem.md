---
declaration: theorem
origin: cited
lean: MeasurableSet.isStoppingTime_debut
statement: formalized
proof: formalized
---

# The debut theorem

For standard Borel time with measurable open sets and a
first-countable order topology, a right-continuous filtration with complete trims of an
s-finite measure `P` makes every progressive set's debut a stopping time. In particular,
`ℱ.IsComplete P` supplies the required trim completeness. No graph point or section is asserted.

```lean
MeasurableSet.isStoppingTime_debut.{u_1, u_2} {ι : Type u_1} {Ω : Type u_2}
  [ConditionallyCompleteLinearOrderBot ι] [TopologicalSpace ι] [MeasurableSpace ι]
  [OpensMeasurableSpace ι] [StandardBorelSpace ι] {mΩ : MeasurableSpace Ω}
  {ℱ : MeasureTheory.Filtration ι mΩ} {s : Set (ι × Ω)} [OrderTopology ι] [FirstCountableTopology ι]
  (hs : MeasurableSet s) (P : MeasureTheory.Measure Ω) [MeasureTheory.SFinite P]
  [ℱ.IsRightContinuous] [∀ (t : ι), (P.trim ⋯).IsComplete] :
  MeasureTheory.IsStoppingTime ℱ (TauCeti.debut s)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A measurable function on a product factors through Boolean coordinates](../../combinatorics/dense-graph-limits-and-graphons/a-measurable-function-on-a-product-factors-throu.md)
- [Lusin's universal-measurability theorem](../../measure-theory/measurable-space/lusins-universal-measurability-theorem.md)

## Lean

Formalized in Tau Ceti as [`MeasurableSet.isStoppingTime_debut`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Debut.html#MeasurableSet.isStoppingTime_debut).

## Sources

- [Tau Ceti documentation: `MeasurableSet.isStoppingTime_debut`](https://taucetiproject.org/docs/TauCeti/Probability/Process/Debut.html#MeasurableSet.isStoppingTime_debut)
- [Source of `MeasurableSet.isStoppingTime_debut` in TauCeti/Probability/Process/Debut.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Process/Debut.lean#L185)
