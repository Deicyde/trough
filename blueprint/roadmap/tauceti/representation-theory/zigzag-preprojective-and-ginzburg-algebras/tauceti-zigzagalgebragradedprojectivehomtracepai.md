---
declaration: theorem
origin: cited
lean: TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair
statement: formalized
proof: formalized
---

# TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair

Complementary shifted Hom spaces of actual componentwise vertex projectives are in perfect
trace pairing over every commutative coefficient ring.

```lean
TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair.{u, w} (k : Type w) [CommRing k]
  {V : Type u} [Finite V] (G : SimpleGraph V) (i j : V) (s : ℤ) :
  (TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing k G i j s).IsPerfPair
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/Hom.html#TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/Hom.html#TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair)
- [Source of `TauCeti.zigzagAlgebraGradedProjectiveHomTracePairing_isPerfPair` in TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/Hom.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Componentwise/Hom.lean#L169)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
