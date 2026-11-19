---
declaration: def
origin: cited
lean: TauCeti.PDCode.khovanovBracketMappingConeIso
statement: formalized
---

# The skein mapping cone of the unnormalized Khovanov complex

For a crossing `c` of a
planar code `D`, the mapping cone of the cochain map `⟦D_A⟧ʲ ⟶ ⟦D_B⟧ʲ⁻¹` induced by the saddle
map `TauCeti.PDCode.resolveCrossingSaddle` is the degree-`j` component of the unnormalized
Khovanov complex `⟦D⟧` shifted by one, where `D_A` and `D_B` are the resolutions of `D` at `c`.
A vertex of `⟦D_A⟧` is sent to the vertex over it in `⟦D⟧`
(`TauCeti.PDCode.inl_v_khovanovBracketMappingConeIso_hom_f`), and a vertex `S` of `⟦D_B⟧` to the
vertex over it with the sign `-(-1) ^ #{a ∈ S | a.castSucc < c}`
(`TauCeti.PDCode.inr_f_khovanovBracketMappingConeIso_hom_f`).

```lean
TauCeti.PDCode.khovanovBracketMappingConeIso.{u} {n : ℕ} (D : TauCeti.PDCode (n + 1))
  (c : Fin (n + 1)) (hD : D.IsPlanar) (R : Type u) [CommRing R] (j : ℤ) :
  CochainComplex.mappingCone
      (CategoryTheory.NatTrans.cubeComplexMap (D.resolveCrossingSaddle c hD R j)) ≅
    D.khovanovBracket hD R j⟦1⟧
```

## Depends on

- [The cube complex is a mapping cone](the-cube-complex-is-a-mapping-cone.md)
- [Reordering the indices of a cube complex](reordering-the-indices-of-a-cube-complex.md)

## Proof depends on

- [The Euler bound for a pair of permutations](../../group-theory/permutations/the-euler-bound-for-a-pair-of-permutations.md)
- [Euler's formula for a PD-code](../other-results/eulers-formula-for-a-pd-code.md)
- [Every edge of the cube of resolutions of a planar code is a merge or a split](every-edge-of-the-cube-of-resolutions-of-a-plana.md)
- [The faces of the cube of resolutions commute](the-faces-of-the-cube-of-resolutions-commute.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.khovanovBracketMappingConeIso`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/Skein.html#TauCeti.PDCode.khovanovBracketMappingConeIso).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.khovanovBracketMappingConeIso`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/Skein.html#TauCeti.PDCode.khovanovBracketMappingConeIso)
- [Source of `TauCeti.PDCode.khovanovBracketMappingConeIso` in TauCeti/KnotTheory/Khovanov/Resolution/Skein.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Khovanov/Resolution/Skein.lean#L172)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
