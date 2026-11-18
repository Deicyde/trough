---
declaration: def
origin: cited
lean: TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv
statement: formalized
---

# The node ring is `ℂ{x, y}/(xy)`

Restriction to the two coordinate axes identifies the
quotient of the ring of holomorphic germs at the origin of `ℂ²` by `xy` with the ring of pairs of
branch germs with equal values at the node.

```lean
TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv :
  ↑((TauCeti.holomorphicStructureSheaf (modelWithCornersSelf ℂ (ℂ × ℂ)) (ℂ × ℂ)).presheaf.stalk
          (0, 0)) ⧸
      Ideal.span
        {TauCeti.holomorphicStructureSheaf.planeFstCoordinate *
            TauCeti.holomorphicStructureSheaf.planeSndCoordinate} ≃+*
    ↥(TauCeti.holomorphicStructureSheaf.nodeLocalRing (modelWithCornersSelf ℂ ℂ)
        (modelWithCornersSelf ℂ ℂ) 0 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's lemma along a graph](../../../../analysis/part-03/analytic/hadamards-lemma-along-a-graph.md)
- [Osgood's lemma](../../complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/PlaneNode.html#TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/StructureSheaf/PlaneNode.html#TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv)
- [Source of `TauCeti.holomorphicStructureSheaf.nodeLocalRing.planeNodeEquiv` in TauCeti/Geometry/Manifold/Complex/StructureSheaf/PlaneNode.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Complex/StructureSheaf/PlaneNode.lean#L220)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
