---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFiltered_and_nonempty_isColimit_coherentSubobjectCocone, AlgebraicGeometry.Space.isFilteredColimit_isFinitePresentation_of_isAffineHom, AlgebraicGeometry.Space.exists_isFiltered_isColimit_isFinitePresentation_of_isAffineHom_of_isNoetherian
statement: formalized
proof: formalized
---

# 69.15 Limits of coherent modules

Section 69.15 of the Stacks Project, [Tag 07UU](https://stacks.math.columbia.edu/tag/07UU). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07UV, a lemma

[Tag 07UV](https://stacks.math.columbia.edu/tag/07UV) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiltered_and_nonempty_isColimit_coherentSubobjectCocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubmoduleColimitNoetherian.lean, line 846](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSubmoduleColimitNoetherian.lean#L846).

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

**`AlgebraicGeometry.Space.isFilteredColimit_isFinitePresentation_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationColimitAffineOverNoetherian.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationColimitAffineOverNoetherian.lean#L188). The attribute's comment: “granted five general cited inputs: hNoeth (the Noetherian case, Stacks 07UV with 07UB), hpush (Stacks 08AI), hpull (Stacks 03LU, 05VR), hepi (Stacks 03LX, step 3) and hqcqs”.

> **Stacks 07UW.**  Let `f : X ⟶ Y` be an affine morphism of algebraic spaces over a scheme `S`
> with `Y` Noetherian.  Then every quasi-coherent `𝒪_X`-module is a filtered colimit of
> `𝒪_X`-modules of finite presentation.
>
> No clause of the tag's conclusion is dropped or weakened, and the tag's own hypotheses — `f`
> affine, `Y` Noetherian, the module quasi-coherent — are the hypotheses here.  What is granted
> beyond them are the five general cited inputs `hNoeth`, `hpush`, `hpull`, `hepi` and `hqcqs`,
> each quantified over its own algebraic spaces, morphisms and modules and none of them mentioning
> `f`, `X`, `Y` or `F`; see the module docstring for what each one is and for which tag it stands
> in.  In particular `hNoeth` is the assertion for a *Noetherian* space, namely Stacks 07UV with
> Stacks 07UB, which the source quotes here and which is not the conclusion below: `X` is affine
> over a Noetherian space, not Noetherian, and the transfer along `f` is the content of the tag.
>
> Everything else in the source's proof is discharged: the pullback of the presentation and the
> quotient presentation of an arbitrary quasi-coherent module
> (`AlgebraicGeometry.Space.exists_epi_isColimit_isFinitePresentation_of_isAffineHom`), the
> identification of `F` as a cokernel of a map between two such colimits, Stacks 07U7 on `X`, and
> the formal passage from that cokernel to the filtered colimit of the cokernels of the
> representing maps.

```lean
theorem isFilteredColimit_isFinitePresentation_of_isAffineHom
    (hNoeth : ∀ Z : AlgebraicSpaces B S hS, IsNoetherian B S hS hZ Z.1 →
      ∀ N : Modules.{u, u} B S hS Z.1 Z.2, N.IsQuasicoherentOnSite →
        ∃ (I : Type u) (inst : SmallCategory I),
          let _ := inst
          ∃ (_ : IsFiltered I) (D : I ⥤ Modules.{u, u} B S hS Z.1 Z.2)
            (φ : D ⟶ (Functor.const I).obj N),
            (∀ i, (D.obj i).IsFinitePresentation) ∧ Nonempty (IsColimit (Cocone.mk N φ)))
    (hpush : ∀ (Z W : AlgebraicSpaces B S hS) (g : Z ⟶ W), IsAffineHom B S hS g.hom →
      ∀ N : Modules.{u, u} B S hS Z.1 Z.2, N.IsQuasicoherentOnSite →
        ((modulePushforward B S hS g).obj N).IsQuasicoherentOnSite)
    (hpull : ∀ (Z W : AlgebraicSpaces B S hS) (g : Z ⟶ W) (N : Modules.{u, u} B S hS W.1 W.2),
      (N.IsQuasicoherentOnSite → ((modulePullback B S hS g).obj N).IsQuasicoherentOnSite) ∧
        (N.IsFinitePresentation → ((modulePullback B S hS g).obj N).IsFinitePresentation))
    (hepi : ∀ (Z W : AlgebraicSpaces B S hS) (g : Z ⟶ W), IsAffineHom B S hS g.hom →
      ∀ N : Modules.{u, u} B S hS Z.1 Z.2, N.IsQuasicoherentOnSite →
        Epi ((modulePullbackAdjunction B S hS g).counit.app N))
    (hqcqs : ∀ (Z W : AlgebraicSpaces B S hS) (g : Z ⟶ W), IsAffineHom B S hS g.hom →
      IsNoetherian B S hS hZ W.1 →
        IsQuasiCompactSpace B S hS Z.1 ∧ IsAbsolutelyQuasiSeparated B S hS hZ Z.1)
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (hY : IsNoetherian B S hS hZ Y.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite) :
    ∃ (K : Type (u + 1)) (inst : Category.{u} K),
      let _ := inst
      ∃ (_ : IsFiltered K) (D : K ⥤ Modules.{u, u} B S hS X.1 X.2)
        (φ : D ⟶ (Functor.const K).obj F),
        (∀ k, (D.obj k).IsFinitePresentation) ∧ Nonempty (IsColimit (Cocone.mk F φ))
```

**`AlgebraicGeometry.Space.exists_isFiltered_isColimit_isFinitePresentation_of_isAffineHom_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationColimitAffineOverNoetherianUnconditional.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationColimitAffineOverNoetherianUnconditional.lean#L209). The attribute's comment: “every quasi-coherent 𝒪_X-module is a filtered colimit of finitely presented 𝒪_X-modules, for f : X ⟶ Y affine with Y Noetherian”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
