---
declaration: instance
origin: cited
lean: TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor
statement: formalized
---

# TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor

The block swap of `FiniteBijection` acts on `X^∧(k + l)` as the swap of the two smash factors
`X^∧k ∧ X^∧l`, so the symmetric sequence of smash powers is a braided monoidal functor.

```lean
TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor.{u} {X : TauCeti.PointedSSet} :
  X.smashPowFunctor.Braided
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/Pointed/Smash/Power.html#TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor).

## Sources

- [Tau Ceti documentation: `TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/SimplicialSet/Pointed/Smash/Power.html#TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor)
- [Source of `TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor` in TauCeti/AlgebraicTopology/SimplicialSet/Pointed/Smash/Power.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/SimplicialSet/Pointed/Smash/Power.lean#L629)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
