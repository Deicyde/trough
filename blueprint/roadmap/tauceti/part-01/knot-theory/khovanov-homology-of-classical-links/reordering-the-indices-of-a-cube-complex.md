---
declaration: def
origin: cited
lean: CategoryTheory.Functor.cubeComplexReindexIso
statement: formalized
---

# Reordering the indices of a cube complex

For an equivalence `e : ι ≃ κ` of finite
linearly ordered types and vertex isomorphisms `α S : F(S) ≅ G(e(S))` commuting with the edge
maps, the cube complexes of `F` and `G` are isomorphic. On the vertex `F(S)` the isomorphism is
`α S` multiplied by the inversion sign `(-1) ^ #(S.inversions e)` of `e` on `S`
(`Functor.ι_cubeComplexReindexIso_hom_f`); these signs absorb the change in the edge signs.

```lean
CategoryTheory.Functor.cubeComplexReindexIso.{w, w', v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] {ι : Type w} [LinearOrder ι] {κ : Type w'} [LinearOrder κ]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasFiniteBiproducts C] [Fintype ι]
  [Fintype κ] (F : CategoryTheory.Functor (Finset ι) C) {G : CategoryTheory.Functor (Finset κ) C}
  (e : ι ≃ κ) (α : (S : Finset ι) → F.obj S ≅ G.obj (Finset.map e.toEmbedding S))
  (hα : F.IsCubeReindexCompatible G e α) : F.cubeComplex ≅ G.cubeComplex
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.cubeComplexReindexIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/Reindex.html#CategoryTheory.Functor.cubeComplexReindexIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.cubeComplexReindexIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/Reindex.html#CategoryTheory.Functor.cubeComplexReindexIso)
- [Source of `CategoryTheory.Functor.cubeComplexReindexIso` in TauCeti/Algebra/Homology/Cube/Reindex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/Cube/Reindex.lean#L216)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
