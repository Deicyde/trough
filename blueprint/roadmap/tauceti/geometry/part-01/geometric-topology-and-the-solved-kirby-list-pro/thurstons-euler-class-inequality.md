---
declaration: def
origin: cited
lean: TauCeti.ThurstonEulerClassInequality
statement: formalized
---

# Thurston's Euler class inequality

on a closed orientable hyperbolic `3`-manifold `M`,
that is a compact connected orientable smooth `3`-manifold without boundary admitting a complete
Riemannian metric of constant curvature `-1`, every Euler class of a smooth taut codimension-one
foliation satisfies the Euler class inequality.

```lean
TauCeti.ThurstonEulerClassInequality : Prop
```

## Depends on

- [TauCeti.Foliation.eulerClass](tauceti-foliation-eulerclass.md)

## Proof depends on

- [The Koszul formula](../manifold/part-02/the-koszul-formula.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ThurstonEulerClassInequality`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Foliation/EulerClass.html#TauCeti.ThurstonEulerClassInequality).

## Sources

- [Tau Ceti documentation: `TauCeti.ThurstonEulerClassInequality`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Foliation/EulerClass.html#TauCeti.ThurstonEulerClassInequality)
- [Source of `TauCeti.ThurstonEulerClassInequality` in TauCeti/Geometry/Manifold/Foliation/EulerClass.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Foliation/EulerClass.lean#L326)
- [Tau Ceti roadmap status: Geometric topology and the solved Kirby-list problems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeometricTopology/STATUS.md)
