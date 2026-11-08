---
declaration: theorem
origin: cited
lean: TauCeti.Huber.IsHuberRing.subring
statement: formalized
proof: formalized
---

# Wedhorn Corollary 6.4(2)

An open subring of a Huber ring, with the subspace topology, is
a Huber ring.

```lean
TauCeti.Huber.IsHuberRing.subring.{u_2} {A : Type u_2} [CommRing A] [TopologicalSpace A]
  [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] {C : Subring A} (hC : IsOpen ↑C) :
  TauCeti.Huber.IsHuberRing ↥C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsHuberRing.subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/RingOfDefinition.html#TauCeti.Huber.IsHuberRing.subring).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsHuberRing.subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/RingOfDefinition.html#TauCeti.Huber.IsHuberRing.subring)
- [Source of `TauCeti.Huber.IsHuberRing.subring` in TauCeti/RingTheory/Huber/RingOfDefinition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/RingOfDefinition.lean#L723)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
