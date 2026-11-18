---
declaration: theorem
origin: cited
lean: TauCeti.FiniteEtaleScheme.nonempty_fiber_iso
statement: formalized
proof: formalized
---

# Any two geometric points of a connected scheme are joined by an étale path

their
geometric fibre functors on finite étale schemes are isomorphic. The geometric points may have
different separably closed fields.

```lean
TauCeti.FiniteEtaleScheme.nonempty_fiber_iso.{u} {S : AlgebraicGeometry.Scheme} {Ω : Type u}
  [Field Ω] [IsSepClosed Ω] [ConnectedSpace ↥S] {Ω' : Type u} [Field Ω'] [IsSepClosed Ω']
  (x : AlgebraicGeometry.Spec ↧Ω ⟶ S) (y : AlgebraicGeometry.Spec ↧Ω' ⟶ S) :
  Nonempty (TauCeti.FiniteEtaleScheme.fiber x ≅ TauCeti.FiniteEtaleScheme.fiber y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Finite étale schemes over a connected scheme form a Galois category](finite-etale-schemes-over-a-connected-scheme-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.nonempty_fiber_iso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.html#TauCeti.FiniteEtaleScheme.nonempty_fiber_iso).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.nonempty_fiber_iso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.html#TauCeti.FiniteEtaleScheme.nonempty_fiber_iso)
- [Source of `TauCeti.FiniteEtaleScheme.nonempty_fiber_iso` in TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/Galois/Category.lean#L119)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
