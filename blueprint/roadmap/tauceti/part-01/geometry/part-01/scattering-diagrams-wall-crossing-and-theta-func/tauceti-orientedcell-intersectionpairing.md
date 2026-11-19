---
declaration: def
origin: cited
lean: TauCeti.OrientedCell.intersectionPairing
statement: formalized
---

# TauCeti.OrientedCell.intersectionPairing

The intersection pairing of the affine test simplex with vertices `v` with finite formal sums
of oriented cells: the sum of the coefficients weighted by the local intersection indices.

```lean
TauCeti.OrientedCell.intersectionPairing.{u_1, u_2, u_3, u_4} {N : Type u_1} {V : Type u_2}
  [AddCommGroup N] [NormedAddCommGroup V] [NormedSpace ℝ V] {i : N →+ V}
  {h : TauCeti.Toric.IsIntegralLattice i} {k : ℕ} {R : Type u_3} [Ring R] {E : Type u_4}
  [AddCommGroup E] [_root_.Module R E] (v : Fin (k + 1) → V) :
  (TauCeti.OrientedCell h k →₀ E) →ₗ[R] E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrientedCell.intersectionPairing`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/PolyhedralCochain/Pairing.html#TauCeti.OrientedCell.intersectionPairing).

## Sources

- [Tau Ceti documentation: `TauCeti.OrientedCell.intersectionPairing`](https://taucetiproject.org/docs/TauCeti/Geometry/Convex/PolyhedralCochain/Pairing.html#TauCeti.OrientedCell.intersectionPairing)
- [Source of `TauCeti.OrientedCell.intersectionPairing` in TauCeti/Geometry/Convex/PolyhedralCochain/Pairing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Convex/PolyhedralCochain/Pairing.lean#L531)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
