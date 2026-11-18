---
declaration: theorem
origin: cited
lean: TauCeti.IsConvexPolyhedron.finite_setOf_isExposed
statement: formalized
proof: formalized
---

# TauCeti.IsConvexPolyhedron.finite_setOf_isExposed

A convex polyhedron has finitely many exposed subsets, hence finitely many faces.

```lean
TauCeti.IsConvexPolyhedron.finite_setOf_isExposed.{u_1} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℝ V] [TopologicalSpace V] {P : Set V} (hP : TauCeti.IsConvexPolyhedron P) :
  {F | IsExposed ℝ P F}.Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsConvexPolyhedron.finite_setOf_isExposed`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Polyhedron/Face.html#TauCeti.IsConvexPolyhedron.finite_setOf_isExposed).

## Sources

- [Tau Ceti documentation: `TauCeti.IsConvexPolyhedron.finite_setOf_isExposed`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Polyhedron/Face.html#TauCeti.IsConvexPolyhedron.finite_setOf_isExposed)
- [Source of `TauCeti.IsConvexPolyhedron.finite_setOf_isExposed` in TauCeti/Analysis/Convex/Polyhedron/Face.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/Polyhedron/Face.lean#L189)
- [Tau Ceti roadmap status: Scattering diagrams, wall crossing and theta functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ScatteringDiagrams/STATUS.md)
