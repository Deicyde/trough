---
declaration: section
origin: cited
lean: Stacks.Cohomology.ModuleColimit.isIso_colimit_post_rightDerived_evaluation_of_isCompact, Stacks.Cohomology.Vanishing.isIso_colimit_post_Hfunctor_of_isCompact, Stacks.Cohomology.AbelianSheaf.preservesColimit_higherDirectImage_of_isBasis, Stacks.Cohomology.SpectralLimit.SpectralAbelianSheafSystem.nonempty_and_isIso_comparison, Stacks.Cohomology.SpectralLimit.SpectralAbelianSheafSystem.nonempty_and_isIso_comparison_global
statement: formalized
proof: formalized
---

# 20.19 Cohomology and colimits

Section 20.19 of the Stacks Project, [Tag 01FE](https://stacks.math.columbia.edu/tag/01FE). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01FF, a lemma

[Tag 01FF](https://stacks.math.columbia.edu/tag/01FF) in the Stacks Project.

**`Stacks.Cohomology.ModuleColimit.isIso_colimit_post_rightDerived_evaluation_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/CohomologyFilteredColimits.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TopDegreeBaseChange/CohomologyFilteredColimits.lean#L150).

> **[Stacks, Tag 01FF] at the module-valued spelling, in the tag's own shape.** Let `X` be a
> space with a basis of quasi-compact opens whose pairwise intersections are quasi-compact, let
> `O_X` be a sheaf of rings on `X` and let `U` be a quasi-compact open. Then for every filtered
> system `F` of `O_X`-modules and every degree `q` the canonical map
> `colimᵢ Hᑫ(U, Fᵢ) ⟶ Hᑫ(U, colimᵢ Fᵢ)` of `Γ(U, O_X)`-modules is an isomorphism.
>
> `Stacks.Cohomology.Vanishing.isIso_colimit_post_Hfunctor_of_isCompact` is the same statement
> for cohomology valued in abelian groups.

```lean
theorem isIso_colimit_post_rightDerived_evaluation_of_isCompact
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (hBasis : PrespectralSpace X) (hInter : QuasiSeparatedSpace X)
    (U : Opens X) (hU : IsCompact (U : Set X)) (q : ℕ)
    {I : Type u} [SmallCategory I] [IsFiltered I] (F : I ⥤ SheafOfModules.{u} R) :
    IsIso (colimit.post F ((_root_.SheafOfModules.evaluation R (op U)).rightDerived q))
```

**`Stacks.Cohomology.Vanishing.isIso_colimit_post_Hfunctor_of_isCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredColimits/CohomologyOverAQuasiCompactOpen.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/FilteredColimits/CohomologyOverAQuasiCompactOpen.lean#L318).

> **Stacks 01FF.**  Let `X` be a topological space with a basis of quasi-compact opens whose
> pairwise intersections are quasi-compact, let `O_X` be a sheaf of rings on `X` and let `U` be a
> quasi-compact open of `X`.  Then for every filtered system `F` of `O_X`-modules and every degree
> `q` the canonical map `colimᵢ Hᑫ(U, Fᵢ) ⟶ Hᑫ(U, colimᵢ Fᵢ)` is an isomorphism.
>
> The proof is the induction of the source on `q`, carried out for an arbitrary cohomological
> δ-functor in `CategoryTheory.DeltaFunctor.isIso_colimit_post_of_isIso_zero` and specialized to
> the cohomology δ-functor in
> `Stacks.Cohomology.Colimit.isIso_colimit_post_Hfunctor_of_preservesColimitsOfShape`.  Its two
> inputs are Stacks 009F for sheaves of modules
> (`Stacks.Cohomology.Sections.preservesColimitsOfShape_secF_of_isCompact`) and the vanishing
> `isZero_Hfunctor_succ_obj_colimit_of_injective` above.
>
> The hypotheses are exactly the tag's: sheafification of abelian presheaves on the site of opens,
> its characterization by local bijectivity, and enough injectives in `SheafOfModules.{u} R` are
> all instances at these universes, so none of them is assumed.

```lean
theorem isIso_colimit_post_Hfunctor_of_isCompact
    {X : Type u} [TopologicalSpace X]
    (R : Sheaf (Opens.grothendieckTopology X) RingCat.{u})
    (hBasis : PrespectralSpace X) (hInter : QuasiSeparatedSpace X)
    {I : Type u} [SmallCategory I] [IsFiltered I]
    (F : I ⥤ SheafOfModules.{u} R)
    (U : Opens X) (hU : IsCompact (U : Set X)) (q : ℕ) :
    IsIso (colimit.post F (Hfunctor R U q))
```

## Tag 0H7A, a lemma

[Tag 0H7A](https://stacks.math.columbia.edu/tag/0H7A) in the Stacks Project.

**`Stacks.Cohomology.AbelianSheaf.preservesColimit_higherDirectImage_of_isBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredColimits/AbelianHigherDirectImage.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/FilteredColimits/AbelianHigherDirectImage.lean#L111).

> **Stacks 0H7A.** If cohomology over the inverse images of the opens of a basis of `Y`
> commutes with a colimit of abelian sheaves on `X`, then so does the degree-`p` higher direct
> image along `f`.
>
> This is the local criterion of Stacks 0H7B for the morphism of sites given by the continuous
> functor `Opens.map f`, together with the observation that a basis of `Y` supplies, for every
> open `V`, a covering of `V` by members of the basis — which is what 0H7B asks for.

```lean
theorem preservesColimit_higherDirectImage_of_isBasis
    {I : Type v} [SmallCategory I] (f : X ⟶ Y)
    (F : I ⥤ X.Sheaf AddCommGrpCat.{v}) (p : ℕ)
    (h : Opens.IsBasis {V : Opens Y |
      PreservesColimit F (cohomologyOver ((Opens.map f).obj V) p)}) :
    PreservesColimit F (higherDirectImage f p)
```

## Tag 0A37, a lemma

[Tag 0A37](https://stacks.math.columbia.edu/tag/0A37) in the Stacks Project.

**`Stacks.Cohomology.SpectralLimit.SpectralAbelianSheafSystem.nonempty_and_isIso_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SpectralSpaceLimit/ComparisonInEveryDegree.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SpectralSpaceLimit/ComparisonInEveryDegree.lean#L270). The attribute's comment: “quasi-compact open: colim_{a : j → i} Hᵖ(f_a⁻¹(Uᵢ), 𝓕ⱼ) = Hᵖ(pᵢ⁻¹(Uᵢ), 𝓕) for every p ≥ 0”.

> **Stacks 0A37, over a quasi-compact open of a stage.**  For a cofiltered system of spectral
> spaces `Xⱼ` with spectral transition maps and abelian sheaves `𝓕ⱼ` with compatible `f`-maps, the
> limit `X = lim Xⱼ` with the sheaf `𝓕 = colim pⱼ⁻¹𝓕ⱼ` on it (a limiting cone `c` of the diagram
> of abelian sheafed spaces), a stage `i`, a quasi-compact open `Uᵢ ⊆ Xᵢ` and `p ≥ 0`, the
> cohomology cocone `colim_{a : j → i} Hᵖ(f_a⁻¹ Uᵢ, 𝓕ⱼ) ⟶ Hᵖ(pᵢ⁻¹ Uᵢ, 𝓕)` exists and its
> comparison out of the colimit is an isomorphism.

```lean
theorem nonempty_and_isIso_comparison (c : Cone S.E) (hc : IsLimit c) (i : J)
    (U : Opens (S.E.obj i)) (hU : IsCompact (U : Set (S.E.obj i))) (p : ℕ) :
    Nonempty (CohomologyCocone ((Over.forget i) ⋙ S.E) (c.whisker (Over.forget i))
      (S.stageOpenCone c i U) p) ∧
    ∀ D : CohomologyCocone ((Over.forget i) ⋙ S.E) (c.whisker (Over.forget i))
      (S.stageOpenCone c i U) p, IsIso D.comparison
```

**`Stacks.Cohomology.SpectralLimit.SpectralAbelianSheafSystem.nonempty_and_isIso_comparison_global`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SpectralSpaceLimit/ComparisonInEveryDegree.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SpectralSpaceLimit/ComparisonInEveryDegree.lean#L282). The attribute's comment: “in particular Hᵖ(X, 𝓕) = colim Hᵖ(Xᵢ, 𝓕ᵢ) for every p ≥ 0”.

> **Stacks 0A37, the global statement**: for a limiting cone `c` of the system and `p ≥ 0`, the
> cohomology cocone `colim Hᵖ(Xᵢ, 𝓕ᵢ) ⟶ Hᵖ(X, 𝓕)` exists and its comparison out of the colimit is
> an isomorphism, that is `Hᵖ(X, 𝓕) = colim Hᵖ(Xᵢ, 𝓕ᵢ)`.

```lean
theorem nonempty_and_isIso_comparison_global (c : Cone S.E) (hc : IsLimit c) (p : ℕ) :
    Nonempty (CohomologyCocone S.E c (S.globalOpenCone c) p) ∧
    ∀ D : CohomologyCocone S.E c (S.globalOpenCone c) p, IsIso D.comparison
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.19, Tag 01FE](https://stacks.math.columbia.edu/tag/01FE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
