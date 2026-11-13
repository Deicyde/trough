---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFiltered_and_nonempty_isColimit_coherentSubobjectCocone, AlgebraicGeometry.Space.exists_isFiltered_isColimit_isFinitePresentation_of_isAffineHom_of_isNoetherian
statement: formalized
proof: formalized
---

# 69.15 Limits of coherent modules

Section 69.15 of the Stacks Project, [Tag 07UU](https://stacks.math.columbia.edu/tag/07UU). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07UV, a lemma

[Tag 07UV](https://stacks.math.columbia.edu/tag/07UV) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiltered_and_nonempty_isColimit_coherentSubobjectCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubmoduleColimitNoetherian.lean, line 841](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubmoduleColimitNoetherian.lean#L841).

> Let `X` be a Noetherian algebraic space over a scheme `S`.  Every quasi-coherent
> `𝒪_X`-module `F` is the filtered colimit of its coherent submodules: the coherent submodules of `F`
> form a filtered category, and the cocone of their inclusions into `F` is a colimit cocone.

```lean
theorem isFiltered_and_nonempty_isColimit_coherentSubobjectCocone
    (terminal_mem : B.Contains (⊤_ Scheme.{u})) (noetherian : IsNoetherian B S hS terminal_mem X)
    (F : Modules.{u, u} B S hS X hX) [hFq : F.IsQuasicoherentOnSite] :
    IsFiltered (CoherentSubobject B S hS X hX F) ∧
      Nonempty (IsColimit (coherentSubobjectCocone B S hS X hX F))
```

## Tag 07UW, a lemma

[Tag 07UW](https://stacks.math.columbia.edu/tag/07UW) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isFiltered_isColimit_isFinitePresentation_of_isAffineHom_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationColimitAffineOverNoetherianUnconditional.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationColimitAffineOverNoetherianUnconditional.lean#L209). The attribute's comment: “for an affine morphism f : X ⟶ Y of algebraic spaces over S with Y Noetherian, every quasi-coherent 𝒪\_X-module is a filtered colimit of finitely presented 𝒪\_X-modules”.

> **Stacks 07UW.**  Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over a scheme
> `S` with `Y` Noetherian.  Then every quasi-coherent `𝒪_X`-module is a filtered colimit of
> `𝒪_X`-modules of finite presentation.
>
> This is `AlgebraicGeometry.Space.isFilteredColimit_isFinitePresentation_of_isAffineHom` with its
> five inputs proved: the Noetherian case
> (`AlgebraicGeometry.Space.exists_isFiltered_isColimit_isFinitePresentation_of_isNoetherian`),
> Stacks 07U8 for the direct image, Stacks 03GA and 03DO (7) for the pullback, the surjectivity of
> the counit (`AlgebraicGeometry.Space.epi_modulePullbackAdjunction_counit_app_of_isAffineHom`) and
> the quasi-compactness and quasi-separatedness of `X`
> (`AlgebraicGeometry.Space.isQuasiCompactSpace_and_isAbsolutelyQuasiSeparated_of_isAffineHom`).
>
> The index category is the category of triples `(i, j, α)` that the source's proof constructs,
> whose objects carry a morphism of `𝒪_X`-modules, and so lives in `Type (u + 1)` with Hom-types in
> `Type u`.

```lean
theorem exists_isFiltered_isColimit_isFinitePresentation_of_isAffineHom_of_isNoetherian
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (hY : IsNoetherian B S hS hZ Y.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    ∃ (K : Type (u + 1)) (inst : Category.{u} K),
      let _ := inst
      ∃ (_ : IsFiltered K) (D : K ⥤ Modules.{u, u} B S hS X.1 X.2)
        (φ : D ⟶ (Functor.const K).obj F),
        (∀ k, (D.obj k).IsFinitePresentation) ∧ Nonempty (IsColimit (Cocone.mk F φ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.15, Tag 07UU](https://stacks.math.columbia.edu/tag/07UU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
