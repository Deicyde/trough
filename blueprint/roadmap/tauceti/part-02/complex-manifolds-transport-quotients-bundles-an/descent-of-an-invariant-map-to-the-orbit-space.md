---
declaration: def
origin: cited
lean: TauCeti.MulAction.orbitRelQuotientLift
statement: formalized
---

# Descent of an invariant map to the orbit space

A map `f : X → Y` that is invariant under
the action of `G` factors through the orbit projection `X → MulAction.orbitRel.Quotient G X`.

```lean
TauCeti.MulAction.orbitRelQuotientLift.{u_1, u_2, u_3} {G : Type u_1} {X : Type u_2} [Group G]
  [MulAction G X] {Y : Type u_3} (f : X → Y) (hf : ∀ (g : G) (x : X), f (g • x) = f x) :
  MulAction.orbitRel.Quotient G X → Y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MulAction.orbitRelQuotientLift`](https://taucetiproject.org/docs/TauCeti/Algebra/GroupAction/OrbitRelQuotient.html#TauCeti.MulAction.orbitRelQuotientLift).

## Sources

- [Tau Ceti documentation: `TauCeti.MulAction.orbitRelQuotientLift`](https://taucetiproject.org/docs/TauCeti/Algebra/GroupAction/OrbitRelQuotient.html#TauCeti.MulAction.orbitRelQuotientLift)
- [Source of `TauCeti.MulAction.orbitRelQuotientLift` in TauCeti/Algebra/GroupAction/OrbitRelQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/GroupAction/OrbitRelQuotient.lean#L816)
- [Tau Ceti roadmap status: Complex manifolds: transport, quotients, bundles, and gluing](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexManifolds/STATUS.md)
