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
- [Source of `TauCeti.FixedPoints.etale_subalgebra` in TauCeti/RingTheory/Etale/Equalizer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Etale/Equalizer.lean#L308)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
