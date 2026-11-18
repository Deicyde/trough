---
declaration: theorem
origin: cited
lean: TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq
statement: formalized
proof: formalized
---

# Conjugacy of maximal tori

Any two maximal tori of a compact Lie group are conjugate.

```lean
TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] (I : ModelWithCorners ℝ E H) {G : Type u_3}
  [TopologicalSpace G] [ChartedSpace H G] [Group G] [FiniteDimensional ℝ E] [LieGroup I (↑⊤) G]
  [T2Space G] [CompactSpace G] {S T : Subgroup G} (hS : TauCeti.Lie.IsMaximalTorus S)
  (hT : TauCeti.Lie.IsMaximalTorus T) :
  ∃ g, Subgroup.map (MulEquiv.toMonoidHom (MulAut.conj g)) S = T
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The closed-subgroup theorem, with its model space](../../../geometry/part-02/lie/the-closed-subgroup-theorem-with-its-model-space.md)
- [Hadamard's identity in the algebra of smooth functions](../../../geometry/part-02/manifold/part-02/hadamards-identity-in-the-algebra-of-smooth-func.md)
- [Hadamard's lemma](../../../geometry/part-02/manifold/part-02/hadamards-lemma.md)
- [Hunt's lemma](../../../geometry/part-02/lie/hunts-lemma.md)
- [Kronecker's theorem in the Lie algebra](../../../geometry/part-02/lie/kroneckers-theorem-in-the-lie-algebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Torus/Conjugacy.html#TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Lie/Subgroup/Torus/Conjugacy.html#TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq)
- [Source of `TauCeti.Lie.IsMaximalTorus.exists_map_conj_eq` in TauCeti/Geometry/Lie/Subgroup/Torus/Conjugacy.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Lie/Subgroup/Torus/Conjugacy.lean#L136)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
