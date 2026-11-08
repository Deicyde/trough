---
declaration: def
origin: cited
lean: TauCeti.cyclicTwoCohomPolynomialEquiv
statement: formalized
---

# TauCeti.cyclicTwoCohomPolynomialEquiv

The canonical graded mod-two cohomology algebra of an order-two discrete group is a
polynomial algebra, with `X` sent to its nontrivial character in degree one.

```lean
TauCeti.cyclicTwoCohomPolynomialEquiv.{u} (G : Type u) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [DiscreteTopology G] (hG : Nat.card G = 2) :
  Polynomial (ZMod 2) ≃ₐ[ZMod 2] TauCeti.gradedCohomF2 G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The index-two corestriction--cup sequence is exact in every degree](the-index-two-corestriction-cup-sequence-is-exac.md)
- [Shapiro's lemma in degree one](../homological/shapiros-lemma-in-degree-one.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicTwoCohomPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/TrivialF2/CyclicTwo.html#TauCeti.cyclicTwoCohomPolynomialEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicTwoCohomPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/TrivialF2/CyclicTwo.html#TauCeti.cyclicTwoCohomPolynomialEquiv)
- [Source of `TauCeti.cyclicTwoCohomPolynomialEquiv` in TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/TrivialF2/CyclicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/TrivialF2/CyclicTwo.lean#L205)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
