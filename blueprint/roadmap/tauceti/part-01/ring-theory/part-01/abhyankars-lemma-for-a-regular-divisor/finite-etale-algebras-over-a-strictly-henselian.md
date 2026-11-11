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

## Proof depends on

- [TauCeti.IsFiniteEtaleSplit](../analytic-adic-geometry-for-diamonds/tauceti-isfiniteetalesplit.md)
- [TauCeti.IsFiniteEtaleSplit.of_henselianLocalRing](../analytic-adic-geometry-for-diamonds/tauceti-isfiniteetalesplit-of-henselianlocalring.md)

## Lean

Formalized in Tau Ceti as [`Algebra.IsFiniteSplit.of_henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Etale.html#Algebra.IsFiniteSplit.of_henselianLocalRing).

## Sources

- [Tau Ceti documentation: `Algebra.IsFiniteSplit.of_henselianLocalRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/Etale.html#Algebra.IsFiniteSplit.of_henselianLocalRing)
- [Source of `Algebra.IsFiniteSplit.of_henselianLocalRing` in TauCeti/RingTheory/Henselian/Etale.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Henselian/Etale.lean#L156)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
