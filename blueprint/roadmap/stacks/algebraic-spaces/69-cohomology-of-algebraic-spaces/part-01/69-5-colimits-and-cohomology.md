---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIso_colimit_post_rightDerived_globalSections, AlgebraicGeometry.Space.isIso_colimit_post_rightDerived_smallEtaleAbelianPushforward, AlgebraicGeometry.Space.preservesColimitsOfShape_coyoneda_of_isFinitePresentation
statement: formalized
proof: formalized
---

# 69.5 Colimits and cohomology

Section 69.5 of the Stacks Project, [Tag 073D](https://stacks.math.columbia.edu/tag/073D). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 073E, a lemma

[Tag 073E](https://stacks.math.columbia.edu/tag/073E) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_colimit_post_rightDerived_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleCohomologyFilteredColimits.lean, line 715](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleCohomologyFilteredColimits.lean#L715). References: SGA 4 VII (3.3).

> **Stacks 073E.** On a quasi-compact and quasi-separated algebraic space,
> the canonical map from a filtered colimit of étale cohomology groups to the
> étale cohomology of the filtered colimit is an isomorphism.

```lean
theorem isIso_colimit_post_rightDerived_globalSections
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (p : ℕ) {I : Type w} [SmallCategory I] [IsFiltered I]
    [HasColimitsOfShape I Ab.{u + 1}]
    (F : I ⥤ Sheaf (SmallEtale.topology B S hS X) (Ab.{u + 1})) :
    IsIso (colimit.post F
      ((Sheaf.Γ (SmallEtale.topology B S hS X)
        (Ab.{u + 1})).rightDerived p))
```

## Tag 07U6, a lemma

[Tag 07U6](https://stacks.math.columbia.edu/tag/07U6) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_colimit_post_rightDerived_smallEtaleAbelianPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleCohomologyFilteredColimits.lean, line 892](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleCohomologyFilteredColimits.lean#L892). References: SGA 4 VI (5.1), “étale alg. spaces”.

> **Stacks 07U6.** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over `S`. For every degree `p` and every filtered diagram `F` of abelian
> sheaves on the small étale site of `X`, the canonical map from the colimit of the degree-`p`
> higher direct images to the degree-`p` higher direct image of the colimit is an isomorphism:
> `R^p f_* (colim F_i) = colim R^p f_* F_i`.
>
> The direct image is the direct image of abelian sheaves along the morphism of small étale topoi
> of Stacks 03G2, part (3). It is transported, along the comparison equivalence of Stacks 03G1 at
> abelian coefficients, to the direct image along the base-change morphism of *sites* of
> Stacks 03G2, part (1), where the statement is
> `AlgebraicGeometry.Space.isIso_colimit_post_rightDerived_spacesPushforward`.

```lean
theorem isIso_colimit_post_rightDerived_smallEtaleAbelianPushforward
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hqc : IsQuasiCompact B S hS f.hom) (hqs : IsQuasiSeparated B S hS f.hom)
    (p : ℕ) {I : Type w} [SmallCategory I] [IsFiltered I]
    [HasColimitsOfShape I Ab.{u + 1}]
    (F : I ⥤ Sheaf (SmallEtale.topology B S hS X.obj) Ab.{u + 1}) :
    IsIso (colimit.post F
      ((abelianPushforward (SmallEtale.topology B S hS X.obj)
        (smallToposMorphism B S hS f)).rightDerived p))
```

## Tag 07U7, a lemma

[Tag 07U7](https://stacks.math.columbia.edu/tag/07U7) in the Stacks Project.

**`AlgebraicGeometry.Space.preservesColimitsOfShape_coyoneda_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModelCoveringSet.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleModelCoveringSet.lean#L408).

> Let `X` be a quasi-compact and quasi-separated algebraic space over a scheme `S`, let `G` be
> an `𝒪_X`-module of finite presentation and let `λ ↦ F_λ` be a filtered system of `𝒪_X`-modules.
> Then
>
> `colim_λ Hom_X(G, F_λ) = Hom_X(G, colim_λ F_λ)`,
>
> here in the form that `Hom_X(G, -)` preserves colimits of the given filtered shape, which says
> exactly that the canonical comparison map out of any such colimit is a bijection. The module
> universe is the universe `u` of the schemes.

```lean
theorem preservesColimitsOfShape_coyoneda_of_isFinitePresentation
    (hqc : IsQuasiCompactSpace B S hS F) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ F)
    (G : Modules.{u, u} B S hS F hF) [G.IsFinitePresentation]
    (K : Type u) [Category.{u} K] [IsFiltered K] :
    PreservesColimitsOfShape K (coyoneda.obj (Opposite.op G))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.5, Tag 073D](https://stacks.math.columbia.edu/tag/073D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
