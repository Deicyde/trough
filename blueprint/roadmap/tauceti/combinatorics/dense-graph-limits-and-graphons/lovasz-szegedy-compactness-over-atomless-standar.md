---
declaration: theorem
origin: cited
lean: TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace
statement: formalized
proof: formalized
---

# Lovász--Szegedy compactness over atomless standard Borel carriers

The cut-distance
quotient of graphons on a standard Borel space with an atomless probability measure is a compact
metric space, being isometric to `GraphonSpaceI`.

```lean
TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace.{u_1} {Ω : Type u_1} [MeasurableSpace Ω]
  [StandardBorelSpace Ω] {μ : MeasureTheory.Measure Ω} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.NullSingletonClass μ] : CompactSpace (TauCeti.DenseGraphLimits.GraphonSpace Ω μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Frieze--Kannan weak regularity](frieze-kannan-weak-regularity.md)
- [TauCeti.DenseGraphLimits.cutDist](tauceti-densegraphlimits-cutdist.md)
- [TauCeti.DenseGraphLimits.cutDist_triangle](tauceti-densegraphlimits-cutdist-triangle.md)
- [TauCeti.DenseGraphLimits.Graphon.unitIntervalRepr](tauceti-densegraphlimits-graphon-unitintervalrep.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Compact.html#TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace`](https://taucetiproject.org/docs/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Compact.html#TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace)
- [Source of `TauCeti.DenseGraphLimits.GraphonSpace.instCompactSpace` in TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Compact.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/DenseGraphLimits/GraphonSpace/Compact.lean#L62)
- [Tau Ceti roadmap status: Dense graph limits and graphons](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/DenseGraphLimits/STATUS.md)
