---
declaration: theorem
origin: cited
lean: TauCeti.FixedPoints.etale_subalgebra
statement: formalized
proof: formalized
---

# The invariants of a finite étale algebra under a finite monoid of algebra endomorphisms form an étale algebra

```lean
TauCeti.FixedPoints.etale_subalgebra.{u, u_1} {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
  (G : Type u_1) [Monoid G] [MulSemiringAction G S] [SMulCommClass G R S] [Algebra.Etale R S]
  [Module.Finite R S] [Finite G] : Algebra.Etale R ↥(FixedPoints.subalgebra R S G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FixedPoints.etale_subalgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Equalizer.html#TauCeti.FixedPoints.etale_subalgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.FixedPoints.etale_subalgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Equalizer.html#TauCeti.FixedPoints.etale_subalgebra)
- [Source of `TauCeti.FixedPoints.etale_subalgebra` in TauCeti/RingTheory/Etale/Equalizer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Etale/Equalizer.lean#L308)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
