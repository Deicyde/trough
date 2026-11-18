---
declaration: def
origin: cited
lean: CategoryTheory.Functor.cubeComplexMappingConeIso
statement: formalized
---

# The cube complex is a mapping cone

For a cube `F` indexed by `WithBot ι`, the mapping
cone of the cochain map from the totalization of the `0`-face to that of the `1`-face induced by
the edges in the direction of `⊥` is isomorphic to the cube complex of `F` shifted by one. A
vertex of the `0`-face is sent to the same vertex of `F`
(`Functor.inl_v_cubeComplexMappingConeIso_hom_f`), and a vertex of the `1`-face to the negative
of the same vertex of `F` (`Functor.inr_f_cubeComplexMappingConeIso_hom_f`).

```lean
CategoryTheory.Functor.cubeComplexMappingConeIso.{w, v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasFiniteBiproducts C] {ι : Type w} [Fintype ι] [LinearOrder ι]
  (F : CategoryTheory.Functor (Finset (WithBot ι)) C) :
  CochainComplex.mappingCone (CategoryTheory.NatTrans.cubeComplexMap F.cubeFaceMap) ≅
    F.cubeComplex⟦1⟧
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.cubeComplexMappingConeIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/MappingCone.html#CategoryTheory.Functor.cubeComplexMappingConeIso).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.cubeComplexMappingConeIso`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/MappingCone.html#CategoryTheory.Functor.cubeComplexMappingConeIso)
- [Source of `CategoryTheory.Functor.cubeComplexMappingConeIso` in TauCeti/Algebra/Homology/Cube/MappingCone.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/Cube/MappingCone.lean#L382)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
