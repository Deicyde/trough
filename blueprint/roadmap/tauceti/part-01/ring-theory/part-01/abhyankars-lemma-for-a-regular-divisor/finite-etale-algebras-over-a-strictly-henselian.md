---
declaration: theorem
origin: cited
lean: Algebra.IsFiniteSplit.of_henselianLocalRing
statement: formalized
proof: formalized
---

# Finite étale algebras over a strictly Henselian local ring split

over a Henselian local
ring `R` with separably closed residue field, every finite étale `R`-algebra is `R`-isomorphic to
a finite product `Fin n → R` of copies of `R`.

```lean
Algebra.IsFiniteSplit.of_henselianLocalRing.{u, u_1} (R : Type u) [CommRing R]
  [HenselianLocalRing R] [IsSepClosed (IsLocalRing.ResidueField R)] (T : Type u_1) [CommRing T]
  [Algebra R T] [Algebra.Etale R T] [Module.Finite R T] : Algebra.IsFiniteSplit R T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Algebra.IsFiniteSplit.of_henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Etale.html#Algebra.IsFiniteSplit.of_henselianLocalRing).

## Sources

- [Tau Ceti documentation: `Algebra.IsFiniteSplit.of_henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Etale.html#Algebra.IsFiniteSplit.of_henselianLocalRing)
- [Source of `Algebra.IsFiniteSplit.of_henselianLocalRing` in TauCeti/RingTheory/Henselian/Etale.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Henselian/Etale.lean#L156)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
