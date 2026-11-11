---
declaration: theorem
origin: cited
lean: TopCat.singularCohomologyPairMayerVietorisδ_singularCup
statement: formalized
proof: formalized
---

# The Mayer–Vietoris connecting morphism commutes with cup products

Let `U` and `V` be open
subsets covering `X`, and let `A ⊆ U` and `B ⊆ V` be open in `A ∪ B`. For `a ∈ Hᵖ(U ∩ V)` and
`b ∈ H^q(U ∪ V, A ∪ B)`, the connecting morphism of the Mayer–Vietoris sequence of the pairs
`(U, A)` and `(V, B)` sends `a ⌣ b|_{(U ∩ V, A ∩ B)}` to `δ a ⌣ b`, where `δ` is the connecting
morphism of the absolute Mayer–Vietoris sequence of the cover `{U, V}` and `δ a` is restricted from
`X` to `U ∪ V`.

```lean
TopCat.singularCohomologyPairMayerVietorisδ_singularCup.{w, v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.Limits.HasCoproducts C] [CategoryTheory.MonoidalCategory C]
  [CategoryTheory.MonoidalPreadditive C] {R S T M N L : C} (k : Type u_1) [CommRing k]
  [CategoryTheory.Linear k C] [CategoryTheory.MonoidalLinear k C] {X : TopCat} {U V : Set ↑X}
  (hU : IsOpen U) (hV : IsOpen V) (hUV : U ∪ V = Set.univ) {A B : Set ↑X} (hAU : A ⊆ U)
  (hBV : B ⊆ V) (hA : IsOpen (Subtype.val ⁻¹' A)) (hB : IsOpen (Subtype.val ⁻¹' B))
  (u : T ⟶ CategoryTheory.MonoidalCategoryStruct.tensorObj R S)
  (μ : CategoryTheory.MonoidalCategoryStruct.tensorObj M N ⟶ L) {p q n p' m : ℕ} (h : p + q = n)
  (hp : p + 1 = p') (hm : n + 1 = m) (h' : p' + q = m)
  (a : ↑(TopCat.singularCohomology R k M (↧↑(U ∩ V)) p))
  (b : ↑((TopPair.ofInclusion ⋯).singularCohomology S k N q)) :
  (CategoryTheory.ConcreteCategory.hom
        (TopCat.singularCohomologyPairMayerVietorisδ T k L hAU hBV ⋯ ⋯ hA hB n m hm))
      (((TopPair.singularCup k (TopPair.ofInclusion ⋯) u μ p q n h) a)
        ((CategoryTheory.ConcreteCategory.hom
            (TopPair.singularCohomologyMap (TopCat.interToUnionMap hAU hBV) q))
          b)) =
    ((TopPair.singularCup k (TopPair.ofInclusion ⋯) u μ p' q m h')
        ((CategoryTheory.ConcreteCategory.hom
            (TopCat.singularCohomologyMap (TopCat.ofHom (ContinuousMap.subtypeVal (U ∪ V))) p'))
          ((CategoryTheory.ConcreteCategory.hom
              (TopCat.singularCohomologyMayerVietorisδ R k M hU hV hUV p p' hp))
            a)))
      b
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TopCat.singularCohomologyPairMayerVietorisδ_singularCup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Cup.html#TopCat.singularCohomologyPairMayerVietoris%CE%B4_singularCup).

## Sources

- [Tau Ceti documentation: `TopCat.singularCohomologyPairMayerVietorisδ_singularCup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Cup.html#TopCat.singularCohomologyPairMayerVietoris%CE%B4_singularCup)
- [Source of `TopCat.singularCohomologyPairMayerVietorisδ_singularCup` in TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Cup.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/MayerVietoris/Cup.lean#L494)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
