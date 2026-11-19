---
declaration: def
origin: cited
lean: TauCeti.HasPropertyP
statement: formalized
---

# TauCeti.HasPropertyP

A knot `f : S¹ → X` has **Property P** when no nontrivial Dehn surgery on it is simply
connected: for every solid torus neighbourhood `Φ` of `f`, no Dehn filling of the knot exterior
along a slope other than the meridian of `Φ` is simply connected (Kirby's problem 1.15).

```lean
TauCeti.HasPropertyP {X : Type} [TopologicalSpace X] [T2Space X] (f : Circle → X) : Prop
```

## Depends on

- [The Hurewicz theorem](../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasPropertyP`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/NontrivialKnot.html#TauCeti.HasPropertyP).

## Sources

- [Tau Ceti documentation: `TauCeti.HasPropertyP`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/NontrivialKnot.html#TauCeti.HasPropertyP)
- [Source of `TauCeti.HasPropertyP` in TauCeti/LowDimTopology/DehnSurgery/NontrivialKnot.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LowDimTopology/DehnSurgery/NontrivialKnot.lean#L96)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricTopology/STATUS.md)
