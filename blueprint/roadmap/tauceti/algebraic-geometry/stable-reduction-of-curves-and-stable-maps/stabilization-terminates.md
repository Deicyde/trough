---
declaration: theorem
origin: cited
lean: TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable
statement: formalized
proof: formalized
---

# Stabilization terminates

In the stable range `2g - 2 + n > 0`, iterating stabilization
steps from any graph reaches a stable graph, of the same arithmetic genus by
`TauCeti.DualGraph.arithmeticGenus_eq_of_reflTransGen`. Termination holds because every step
removes a vertex.

```lean
TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable.{u, v} {ι : Type v}
  (G : TauCeti.DualGraph ι) [Fintype ι]
  (hrange : 0 < 2 * ↑G.arithmeticGenus - 2 + ↑(Fintype.card ι)) :
  ∃ H, Relation.ReflTransGen TauCeti.DualGraph.StabilizationStep G H ∧ H.IsStable
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Contraction.html#TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable).

## Sources

- [Tau Ceti documentation: `TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/DualGraph/Contraction.html#TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable)
- [Source of `TauCeti.DualGraph.exists_reflTransGen_stabilizationStep_isStable` in TauCeti/AlgebraicGeometry/Curves/DualGraph/Contraction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/DualGraph/Contraction.lean#L949)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
