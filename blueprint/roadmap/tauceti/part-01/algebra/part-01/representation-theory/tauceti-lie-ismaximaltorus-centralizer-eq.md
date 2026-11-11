---
declaration: theorem
origin: cited
lean: TauCeti.Lie.IsMaximalTorus.centralizer_eq
statement: formalized
proof: formalized
---

# TauCeti.Lie.IsMaximalTorus.centralizer_eq

A maximal torus of a compact connected finite-dimensional real Lie group is its own
centralizer.

```lean
TauCeti.Lie.IsMaximalTorus.centralizer_eq.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  (I : ModelWithCorners ℝ E H) {G : Type u_3} [TopologicalSpace G] [ChartedSpace H G] [Group G]
  [LieGroup I (↑⊤) G] [CompactSpace G] [ConnectedSpace G] {T : Subgroup G}
  (hT : TauCeti.Lie.IsMaximalTorus T) : Subgroup.centralizer ↑T = T
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
- [The Koszul formula](../../../geometry/part-02/manifold/part-02/the-koszul-formula.md)
- [Kronecker's theorem in the Lie algebra](../../../geometry/part-02/lie/kroneckers-theorem-in-the-lie-algebra.md)
- [TauCeti.Manifold.riemannianExp](../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Lie.IsMaximalTorus.centralizer_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Torus/Centralizer.html#TauCeti.Lie.IsMaximalTorus.centralizer_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Lie.IsMaximalTorus.centralizer_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Torus/Centralizer.html#TauCeti.Lie.IsMaximalTorus.centralizer_eq)
- [Source of `TauCeti.Lie.IsMaximalTorus.centralizer_eq` in TauCeti/Geometry/Lie/Subgroup/Torus/Centralizer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Lie/Subgroup/Torus/Centralizer.lean#L41)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)
