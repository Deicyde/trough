---
declaration: theorem
origin: cited
lean: TauCeti.SchemeAction.exists_isClosed_orbit
statement: formalized
proof: formalized
---

# Existence of closed orbits

A nonempty scheme of finite type over an algebraically closed
field, acted on by a group scheme of finite type, contains the closed orbit of a rational
point.

```lean
TauCeti.SchemeAction.exists_isClosed_orbit.{u} {k : Type u} [Field k] [IsAlgClosed k]
  (G : CategoryTheory.Over (AlgebraicGeometry.Spec ↧k))
  {X : CategoryTheory.Over (AlgebraicGeometry.Spec ↧k)} [CategoryTheory.GrpObj G]
  [CategoryTheory.ModObj G X] [AlgebraicGeometry.LocallyOfFiniteType G.hom] [CompactSpace ↥G.left]
  [AlgebraicGeometry.LocallyOfFiniteType X.hom] [CompactSpace ↥X.left] [Nonempty ↥X.left] :
  ∃ y, IsClosed (TauCeti.SchemeAction.orbit G y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SchemeAction.exists_isClosed_orbit`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupAction/ClosedOrbit.html#TauCeti.SchemeAction.exists_isClosed_orbit).

## Sources

- [Tau Ceti documentation: `TauCeti.SchemeAction.exists_isClosed_orbit`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/GroupAction/ClosedOrbit.html#TauCeti.SchemeAction.exists_isClosed_orbit)
- [Source of `TauCeti.SchemeAction.exists_isClosed_orbit` in TauCeti/AlgebraicGeometry/GroupAction/ClosedOrbit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/GroupAction/ClosedOrbit.lean#L175)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
