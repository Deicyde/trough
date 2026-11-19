---
declaration: def
origin: cited
lean: TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph
statement: formalized
---

# TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph

For a maximal torus `T` of a compact connected Lie group `G`, the orbit space of the normalizer
on `T` is homeomorphic to the space of conjugacy classes of `G`, through the inclusion of `T`.

```lean
TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] (I : ModelWithCorners ℝ E H) {G : Type u_3} [TopologicalSpace G]
  [ChartedSpace H G] [Group G] [LieGroup I (↑⊤) G] [CompactSpace G] [ConnectedSpace G]
  {T : Subgroup G} (hT : TauCeti.Lie.IsMaximalTorus T) :
  MulAction.orbitRel.Quotient ↥(Subgroup.normalizer ↑T) ↥T ≃ₜ
    MulAction.orbitRel.Quotient (ConjAct G) G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The closed-subgroup theorem, with its model space](../../../geometry/part-02/lie/the-closed-subgroup-theorem-with-its-model-space.md)
- [Conjugacy of maximal tori](conjugacy-of-maximal-tori.md)
- [The Gauss lemma](../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/the-gauss-lemma.md)
- [Hadamard's identity in the algebra of smooth functions](../../../geometry/part-02/manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../../../geometry/part-02/manifold/part-02/hadamards-lemma.md)
- [Hunt's lemma](../../../geometry/part-02/lie/hunts-lemma.md)
- [The inverse function theorem for manifolds](../../../geometry/part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)
- [Kronecker's theorem in the Lie algebra](../../../geometry/part-02/lie/kroneckers-theorem-in-the-lie-algebra.md)
- [TauCeti.Manifold.riemannianExp](../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Weyl/ConjugacyClasses.html#TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Weyl/ConjugacyClasses.html#TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph)
- [Source of `TauCeti.Lie.IsMaximalTorus.normalizerOrbitHomeomorph` in TauCeti/Geometry/Lie/Subgroup/Weyl/ConjugacyClasses.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Lie/Subgroup/Weyl/ConjugacyClasses.lean#L90)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
