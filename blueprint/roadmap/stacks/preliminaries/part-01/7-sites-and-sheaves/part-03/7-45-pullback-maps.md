---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.locallyQuasicoherentStructurePullbackMap, AlgebraicGeometry.Stack.quasicoherentRelativePullbackMap, CategoryTheory.Adjunction.relativePullback, CategoryTheory.Adjunction.relativePullbackMapOfHom, CategoryTheory.Presheaf.isTerminalConstPUnit, CategoryTheory.Presheaf.globalSections, Stacks.Sites.GlobalSectionsAsEqualizer.globalSectionsForkIsLimit, ToposBaseChange.main
statement: formalized
proof: formalized
---

# 7.45 Pullback maps

Section 7.45 of the Stacks Project, [Tag 06UM](https://stacks.math.columbia.edu/tag/06UM). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06UM, the section

[Tag 06UM](https://stacks.math.columbia.edu/tag/06UM) in the Stacks Project.

**`AlgebraicGeometry.Stack.locallyQuasicoherentStructurePullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean#L180). The attribute's comment: “the relative pullback map w\_*𝒪\_𝒲 ⟶ f\_*𝒪\_𝒬 at the structure sheaf of the middle stack of a factorization 𝒬 ⟶ 𝒲 ⟶ 𝒳 of algebraic stacks, on LQCoh^fbc, for direct images wStar, fStar and an adjunction adjPr with an identification cmp : prStar ⋙ wStar ≅ fStar”.

> **The relative pullback map on `LQCoh^fbc` at the structure sheaf.**  For a factorization
> `𝒬 --pr--> 𝒲 --w--> 𝒳` of 1-morphisms of algebraic stacks with direct images `wStar`, `fStar`
> on `LQCoh^fbc` identified by `cmp : pr_* ⋙ w_* ≅ f_*`, the relative pullback map at the
> structure sheaf of `𝒲`, followed by `f_*` of the identification `pr^*𝒪_𝒲 ≅ 𝒪_𝒬` of
> `AlgebraicGeometry.Stack.locallyQuasicoherentStructureSheafPullbackIso`:
>
> `w_*𝒪_𝒲 ⟶ f_*(pr^*𝒪_𝒲) ⟶ f_*𝒪_𝒬`.

```lean
def locallyQuasicoherentStructurePullbackMap :
    wStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒲.val.val.p 𝒲.val.property hincW).obj
        (FibredSite.quasicoherentTensorUnit B S hS 𝒲.val.val.p 𝒲.val.property)) ⟶
      fStar.obj ((quasicoherentToFlatBaseChange B E hE S hS
          𝒬.val.val.p 𝒬.val.property hincP).obj
        (FibredSite.quasicoherentTensorUnit B S hS 𝒬.val.val.p 𝒬.val.property))
```

**`AlgebraicGeometry.Stack.quasicoherentRelativePullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/QuasicoherentTensorPushforward.lean#L221). The attribute's comment: “the relative pullback map w\_\{QCoh,*}𝒪\_𝒲 ⟶ f\_\{QCoh,*}𝒪\_𝒬 in QCoh(𝒪\_𝒳), the coherator of Lemma 0778 applied to the map on LQCoh^fbc, over the same data of Proposition 0771 together with the coherator inputs hincX, hclosed, hpres, hls, hlsD, hwp, hsep of Lemma 0778”.

> **The relative pullback map in `QCoh(𝒪_𝒳)` at the structure sheaf.**  The coherator `Q` of
> **Lemma 0778** applied to
> `AlgebraicGeometry.Stack.locallyQuasicoherentStructurePullbackMap`.  Its source and target are
> the three-step composite `Q ∘ w_* ∘ i` of **Stacks 077A** at the structure sheaf, so this is a
> map
>
> `w_{QCoh, *}𝒪_𝒲 ⟶ f_{QCoh, *}𝒪_𝒬`
>
> in `QCoh(𝒪_𝒳)`.

```lean
def quasicoherentRelativePullbackMap :
    (flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed hpres
          hls hlsD hwp hsep).obj
        (wStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒲.val.val.p 𝒲.val.property
          hincW).obj (FibredSite.quasicoherentTensorUnit B S hS 𝒲.val.val.p 𝒲.val.property))) ⟶
      (flatBaseChangeQuasicoherator B E hE S hS 𝒳.val.val.p 𝒳.val.property hincX hclosed hpres
          hls hlsD hwp hsep).obj
        (fStar.obj ((quasicoherentToFlatBaseChange B E hE S hS 𝒬.val.val.p 𝒬.val.property
          hincP).obj (FibredSite.quasicoherentTensorUnit B S hS 𝒬.val.val.p 𝒬.val.property)))
```

**`CategoryTheory.Adjunction.relativePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePullbackMap.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativePullbackMap.lean#L89). The attribute's comment: “the relative pullback map g\_*ℱ ⟶ h\_*f^\{-1}ℱ of a commutative triangle of morphisms of topoi, stated for an adjunction f^\{-1} ⊣ f\_*, two direct images and an isomorphism f\_* ⋙ g\_* ≅ h\_* in place of the source's equality of functors”.

> **The relative pullback map of a commutative triangle.**  For an adjunction
> `f^{-1} ⊣ f_*` and direct images `g_*`, `h_*` to a third category identified by
> `c : f_* ⋙ g_* ≅ h_*`, the map
>
> `g_*ℱ ⟶ h_*f^{-1}ℱ`
>
> is `g_*` applied to the unit `ℱ ⟶ f_*f^{-1}ℱ`, followed by `c` at `f^{-1}ℱ`.

```lean
def relativePullback : gstar ⟶ finv ⋙ hstar
```

**`CategoryTheory.Adjunction.relativePullbackMapOfHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePullbackMap.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RelativePullbackMap.lean#L111). The attribute's comment: “the variant g\_*ℱ ⟶ h\_*𝒢 of the relative pullback map attached to a morphism f^\{-1}ℱ ⟶ 𝒢”.

> **The relative pullback map attached to a morphism `f^{-1}ℱ ⟶ 𝒢`.**  The pullback map
> `g_*ℱ ⟶ h_*f^{-1}ℱ` followed by `h_*φ`.

```lean
def relativePullbackMapOfHom (F : 𝒞) {G : 𝒟} (φ : finv.obj F ⟶ G) :
    gstar.obj F ⟶ hstar.obj G
```

## Tag 06UN, a definition

[Tag 06UN](https://stacks.math.columbia.edu/tag/06UN) in the Stacks Project.

**`CategoryTheory.Presheaf.isTerminalConstPUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/GlobalSections.lean#L38).

> The presheaf constant at a singleton is the final object of the category of presheaves
> on `C`.

```lean
def isTerminalConstPUnit :
    IsTerminal ((Functor.const Cᵒᵖ).obj (PUnit.{w + 1}))
```

**`CategoryTheory.Presheaf.globalSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/GlobalSections.lean#L45).

> The *global sections* of a presheaf of sets `F` on `C`: the set
> `Γ(C, F) = Mor_{PSh(C)}(*, F)` of morphisms of presheaves from the final presheaf `*` to `F`.

```lean
abbrev globalSections (F : Cᵒᵖ ⥤ Type w) : Type _
```

## Tag 0792, a lemma

[Tag 0792](https://stacks.math.columbia.edu/tag/0792) in the Stacks Project.

**`Stacks.Sites.GlobalSectionsAsEqualizer.globalSectionsForkIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections/AsEqualizer.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/GlobalSections/AsEqualizer.lean#L186).

> **Stacks Tag 0792**: `Γ(C, F)` is the equalizer of `a^*, b^*`.

```lean
noncomputable def globalSectionsForkIsLimit {V U : C} (a b : V ⟶ U)
    (h : IsColimit (Cofork.ofπ (shYonedaTerminal J U) (shYoneda_fork_commutes J a b)))
    (F : Sheaf J (Type u)) :
    IsLimit (Fork.ofι (evalAt J F U) (evalAt_eq J a b F))
```

## Tag 0F6X, a remark

[Tag 0F6X](https://stacks.math.columbia.edu/tag/0F6X) in the Stacks Project.

**`ToposBaseChange.main`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/GlobalSections/BaseChangeComposition.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/GlobalSections/BaseChangeComposition.lean#L111). References: SGA 4 XII (4.4), “more general”.

> **Tag 0F6X (vertical composition of base change maps).** The base change map
> `\beta_rect` of the outer rectangle equals the pasted composite obtained from
> `\beta_bot` and `\beta_top`, namely the horizontal composite of natural
> transformations
> ```
>   m^{-1} \circ g_* \circ f_*
>     --> g'_* \circ l^{-1} \circ f_*     (β_bot whiskered by f_* on the right)
>     --> g'_* \circ f'_* \circ k^{-1}    (β_top whiskered by g'_* on the left)
> ```
> In Mathlib's notation this two-step whiskered composite is exactly
> `(βtop).hComp (βbot)` (the horizontal composition of the two `TwoSquare`s).

```lean
theorem main :
    βrect adjf adjf' adjg adjg' χtop χbot
      = (βtop adjf adjf' χtop).hComp (βbot adjg adjg' χbot)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.45, Tag 06UM](https://stacks.math.columbia.edu/tag/06UM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
