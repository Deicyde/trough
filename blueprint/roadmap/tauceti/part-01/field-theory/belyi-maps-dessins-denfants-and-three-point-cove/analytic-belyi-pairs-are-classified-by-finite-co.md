---
declaration: def
origin: cited
lean: TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass
statement: formalized
---

# Analytic Belyi pairs are classified by finite covers of the thrice-punctured sphere

Restricting the Belyi map over `ℂ ∖ {0, 1}` and filling the punctures are inverse bijections between
isomorphism classes of analytic Belyi pairs of degree `n` and isomorphism classes of connected
degree-`n` covers of `ℂ ∖ {0, 1}`.

```lean
TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass (n : ℕ) :
  Quotient (TauCeti.AnalyticBelyiPair.isoSetoid n) ≃
    TauCeti.ConnectedCoverClass TauCeti.ThricePuncturedSphere.basePt n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic inverse function theorem](../../analysis/part-03/analytic/the-analytic-inverse-function-theorem.md)
- [The identity theorem for Riemann surfaces](../../analysis/part-03/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../algebraic-topology/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The open mapping theorem](../../analysis/part-03/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Riemann's removable singularity theorem on complex curves](../../geometry/part-02/manifold/part-04/riemanns-removable-singularity-theorem-on-comple.md)
- [Rouché's theorem for a disc, classical form](../../analysis/part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [TauCeti.CoveringSpace](../../algebraic-topology/universal-covers/tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.html#TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.html#TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass)
- [Source of `TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.lean#L284)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BelyiMaps/STATUS.md)
