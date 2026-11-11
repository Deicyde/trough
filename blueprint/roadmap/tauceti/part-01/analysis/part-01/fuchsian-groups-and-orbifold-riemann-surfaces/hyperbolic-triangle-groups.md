---
declaration: theorem
origin: cited
lean: TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup
statement: formalized
proof: formalized
---

# Hyperbolic triangle groups

For a hyperbolic typed triple `p`, `q`, `r` of elliptic orders
and cusps, some hyperbolic triangle has the corresponding angles, and its triangle group, generated
by products of reflections in its sides, is a cofinite Fuchsian group isomorphic to the abstract
triangle group `Δ(p, q, r)`.

```lean
TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup {p q r : TauCeti.TriangleOrder}
  (h : p.IsHyperbolic q r) :
  ∃ P,
    P.interiorAngle 0 = p.angle ∧
      P.interiorAngle 1 = q.angle ∧
        P.interiorAngle 2 = r.angle ∧
          P.triangleGroup.IsCofinite ∧
            Nonempty (TauCeti.TriangleGroup p.order q.order r.order ≃* ↥P.triangleGroup)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The angle condition of Poincaré's theorem](../../part-02/complex/part-01/the-angle-condition-of-poincares-theorem.md)
- [The cusp condition of Poincaré's theorem](../../part-02/complex/part-01/the-cusp-condition-of-poincares-theorem.md)
- [The Gauss–Bonnet formula](../../part-02/complex/part-01/the-gauss-bonnet-formula.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Poincaré's presentation theorem](../../part-02/complex/part-03/poincares-presentation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/TriangleOrder/Group.html#TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/TriangleOrder/Group.html#TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup)
- [Source of `TauCeti.TriangleOrder.IsHyperbolic.exists_isCofinite_triangleGroup` in TauCeti/Analysis/Complex/Fuchsian/TriangleOrder/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/TriangleOrder/Group.lean#L465)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
