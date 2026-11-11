---
declaration: theorem
origin: cited
lean: MeasurableSet.measurableEmbedding_domRestrict_fst
statement: formalized
proof: formalized
---

# Lusin–Souslin for vertical sections

If a measurable subset `G` of a product of standard
Borel spaces has at most one point above each `x`, its projection `G → X` is a measurable
embedding.

```lean
MeasurableSet.measurableEmbedding_domRestrict_fst.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [MeasurableSpace X] [StandardBorelSpace X] [MeasurableSpace Y] [StandardBorelSpace Y]
  {G : Set (X × Y)} (hG : MeasurableSet G) (hinj : Set.InjOn Prod.fst G) :
  MeasurableEmbedding (G.domRestrict Prod.fst)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasurableSet.measurableEmbedding_domRestrict_fst`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#MeasurableSet.measurableEmbedding_domRestrict_fst).

## Sources

- [Tau Ceti documentation: `MeasurableSet.measurableEmbedding_domRestrict_fst`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Graph.html#MeasurableSet.measurableEmbedding_domRestrict_fst)
- [Source of `MeasurableSet.measurableEmbedding_domRestrict_fst` in TauCeti/MeasureTheory/Constructions/Polish/Graph.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Constructions/Polish/Graph.lean#L83)
