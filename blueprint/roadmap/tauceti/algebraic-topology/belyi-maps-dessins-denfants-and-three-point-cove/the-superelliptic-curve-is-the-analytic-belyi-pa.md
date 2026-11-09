---
declaration: theorem
origin: cited
lean: TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff
statement: formalized
proof: formalized
---

# The superelliptic curve is the analytic Belyi pair of the torus triple

an analytic Belyi
pair is isomorphic to the superelliptic curve exactly when its monodromy triple is isomorphic to
`TauCeti.PermutationTriple.torusTriple`, for any numbering of its fibre over `1/2`.

```lean
TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff {P : TauCeti.AnalyticBelyiPair}
  (ν : ↑(P.restrict ⁻¹' {TauCeti.ThricePuncturedSphere.basePt}) ≃ Fin 4) :
  Nonempty (P.Iso TauCeti.AnalyticBelyiPair.superelliptic) ↔
    TauCeti.PermutationTriple.IsoClass.mk (⋯.monodromyTriple ν) =
      TauCeti.PermutationTriple.IsoClass.mk TauCeti.PermutationTriple.torusTriple
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Analytic Belyi pairs are classified by finite covers of the thrice-punctured sphere](analytic-belyi-pairs-are-classified-by-finite-co.md)
- [The analytic implicit root theorem](../../analysis/part-01/analytic/the-analytic-implicit-root-theorem.md)
- [The analytic inverse function theorem](../../analysis/part-01/analytic/the-analytic-inverse-function-theorem.md)
- [Connected covers of `ℂ ∖ {0, 1}` of degree `n` up to isomorphism are classified by the isomorphism classes of connected triples of degree `n`](connected-covers-of-c-0-1-of-degree-n-up-to-isom.md)
- [The identity theorem for Riemann surfaces](../../analysis/part-02/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [The open mapping theorem](../../analysis/part-02/complex/part-02/the-open-mapping-theorem.md)
- [Osgood's lemma](../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Riemann's removable singularity theorem on complex curves](../../geometry/part-01/manifold/part-02/riemanns-removable-singularity-theorem-on-comple.md)
- [Rouché's theorem for a disc, classical form](../../analysis/part-01/conformal-mapping-and-the-geometric-theory-of-ho/part-02/rouches-theorem-for-a-disc-classical-form.md)
- [TauCeti.CoveringSpace](../universal-covers/tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.html#TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.html#TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff)
- [Source of `TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.lean#L248)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
