---
declaration: section
origin: cited
lean: CategoryTheory.Sheaf.exists_over_equiv_sheaf, MorphismOfTopoi.sheafOverLocalization, MorphismOfTopoi.sheafOverLocalization_inverseImage_obj, MorphismOfTopoi.sheafOverLocalizationShriek, MorphismOfTopoi.sheafOverLocalization_isLocalization, CategoryTheory.homPushforwardEquivRightInverse, CategoryTheory.Presheaf.IsSheaf.app_fibers_inv_comp_unitInv, CategoryTheory.Presheaf.IsSheaf.app_fibers_inv_comp_homEquiv_shriek
statement: formalized
proof: formalized
---

# 7.30 Localization of topoi

Section 7.30 of the Stacks Project, [Tag 04GY](https://stacks.math.columbia.edu/tag/04GY). 7 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04GZ, a lemma

[Tag 04GZ](https://stacks.math.columbia.edu/tag/04GZ) in the Stacks Project.

**`CategoryTheory.Sheaf.exists_over_equiv_sheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean#L59). The attribute's comment: “the category Sh(C)/F is a topos: it is equivalent to Sh(C/F), sheaves on the site of pairs (U, s) with s ∈ F(U)”.

> **Stacks 04GZ: `Sh(C)/F` is a topos.** For a sheaf `F` on a site `(C, J)`, the slice
> `Sh(C)/F` is equivalent to the category of sheaves of sets on a site, namely the site `C/F` of
> `sheafOverEquivalence`.

```lean
theorem _root_.CategoryTheory.Sheaf.exists_over_equiv_sheaf (F : Sheaf J (Type u)) :
    ∃ (D : Type u) (_ : SmallCategory D) (K : GrothendieckTopology D),
      Nonempty (Over F ≌ Sheaf K (Type u))
```

**`MorphismOfTopoi.sheafOverLocalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean#L92). The attribute's comment: “the canonical morphism of topoi j\_F : Sh(C)/F → Sh(C), with j\_F^\{-1} = toOver F and j\_\{F,*} its right adjoint, constructed through Sh(C)/F ≌ Sh(C/F)”.

> **Stacks 04GZ.** Let `(C, J)` be a site and `F` a sheaf on it. The localization morphism
> `j_F : Sh(C)/F ⟶ Sh(C)` is the morphism of topoi with inverse image `j_F⁻¹ = toOver F`, i.e.
> `H ↦ (H × F ⟶ F)`, and pushforward `j_{F,*} = overLocalizationPushforward J F`, its right
> adjoint.

```lean
noncomputable def sheafOverLocalization (F : Sheaf J (Type u)) :
    MorphismOfTopoi (Over F) (Sheaf J (Type u))
```

**`MorphismOfTopoi.sheafOverLocalization_inverseImage_obj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean#L99). The attribute's comment: “(1): the functor j\_F^\{-1} is H ↦ H × F / F”.

> **Stacks 04GZ (1).** The inverse image of `j_F : Sh(C)/F ⟶ Sh(C)` is
> `H ↦ (H × F ⟶ F)`.

```lean
lemma sheafOverLocalization_inverseImage_obj (F H : Sheaf J (Type u)) :
    (sheafOverLocalization J F).inverseImage.obj H = Over.mk (snd H F)
```

**`MorphismOfTopoi.sheafOverLocalizationShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean#L106). The attribute's comment: “(2): the functor j\_\{F!} is the forgetful functor G/F ↦ G”.

> **Stacks 04GZ (2).** The functor `j_{F!}` of `j_F : Sh(C)/F ⟶ Sh(C)` is the forgetful functor
> `(G ⟶ F) ↦ G`: it is left adjoint to `j_F⁻¹`.

```lean
noncomputable def sheafOverLocalizationShriek (F : Sheaf J (Type u)) :
    Over.forget F ⊣ (sheafOverLocalization J F).inverseImage
```

**`MorphismOfTopoi.sheafOverLocalization_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/ToposLocalizationSheaf.lean#L115). The attribute's comment: “j\_F is a localization: the triple of adjoints j\_\{F!} ⊣ j\_F^\{-1} ⊣ j\_\{F,*}, with j\_\{F!} the forgetful functor and j\_F^\{-1} = H ↦ H × F / F”.

> **Stacks 04GZ: `j_F` is a localization.** The triple of adjoints
> `j_{F!} ⊣ j_F⁻¹ ⊣ j_{F,*}` of `j_F : Sh(C)/F ⟶ Sh(C)`, with `j_{F!} = Over.forget F` and
> `j_F⁻¹ = toOver F`, as in Section 7.25 (tag 00XZ).

```lean
theorem sheafOverLocalization_isLocalization (F : Sheaf J (Type u)) :
    Nonempty (Over.forget F ⊣ (sheafOverLocalization J F).inverseImage) ∧
      Nonempty ((sheafOverLocalization J F).inverseImage ⊣
        (sheafOverLocalization J F).pushforward) ∧
      (sheafOverLocalization J F).inverseImage = toOver F
```

## Tag 04H0, a lemma

[Tag 04H0](https://stacks.math.columbia.edu/tag/04H0) in the Stacks Project.

**`CategoryTheory.homPushforwardEquivRightInverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/OverHomEquiv.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/OverHomEquiv.lean#L93).

> **Stacks 04H0.** Let `E` be a topos, `F` an object of `E` and `j_{F,*} = p` a pushforward
> for the localization `j_F : E/F ⟶ E`, i.e. a right adjoint of `j_F⁻¹ = toOver F`.  For an object
> `φ : G ⟶ F` of `E/F` and any object `A` of `E`, the maps `A ⟶ j_{F,*}(G/F)` are in bijection
> with the morphisms `α : F|_A ⟶ G|_A` of `E/A` that are right inverse to `φ|_A`, restriction to
> `A` being `(-)|_A = j_A⁻¹ = toOver A`.
>
> Taking `A = h_U^#` and using `Γ(U, -) = Hom(h_U^#, -)` this is Stacks 04H0: the sections of
> `j_{F,*}(G/F)` over `U` are the right inverses of `φ|_U`.  The proof follows the Stacks one: the
> adjunction defining `p` identifies `Hom(A, j_{F,*}(G/F))` with the fibre of `φ ∘ (-)` over the
> projection `A ⊗ F ⟶ F`, and interchanging the two factors turns that fibre into the set of right
> inverses of `φ|_A`.
>
> Two things are *not* covered: the bijection is stated pointwise in `A`, its naturality in `A`
> (which is what makes the right-inverse description a description of the sheaf rather than of its
> individual section sets) being left implicit; and `F|_A` is read in the slice `E/A`, whereas
> Stacks reads it in `Sh(C/U)` via the equivalence `Sh(C/U) ≃ Sh(C)/h_U^#` of Stacks 00Y1, which
> is not yet available.

```lean
def homPushforwardEquivRightInverse [BraidedCategory E] {p : Over F ⥤ E} (adj : toOver F ⊣ p)
    (φ : G ⟶ F) (A : E) :
    (A ⟶ p.obj (Over.mk φ)) ≃
      { α : (toOver A).obj F ⟶ (toOver A).obj G // α ≫ (toOver A).map φ = 𝟙 _ }
```

## Tag 0791, a lemma

[Tag 0791](https://stacks.math.columbia.edu/tag/0791) in the Stacks Project.

**`CategoryTheory.Presheaf.IsSheaf.app_fibers_inv_comp_unitInv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/LocalizationOfTopoi.lean, line 881](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/LocalizationOfTopoi.lean#L881). The attribute's comment: “the fibre identification of `j_!j^{-1}G` is evaluation of the counit of `j_!`”.

> **Stacks 0791: the fibre identification of `j_!j^{-1}G` is evaluation of the shriek counit.**
> Write `E` for the equivalence of `sheafEquivalenceCostructuredArrowYoneda` and
> `T = E(j^{-1}G)` for the object of `Sh(C)/F` whose source is `j_!j^{-1}G`. The equivalence
> identifies the fibre sheaf of `T` with `j^{-1}G`: on underlying presheaves the fibre sheaf of `T`
> is `(U, s) ↦ {t ∈ T.left(U) | T.hom(t) = s}` by the `fibers` field, and `E.inverse (E T) ≅ T` by
> the unit. This says that the identification sends a section `t` of `j_!j^{-1}G` over `U` lying in
> the fibre over `s ∈ F(U)` to its image under the counit of `j_! ⊣ j^{-1}`, a section of `G` over
> `U`.
>
> This is the statement connecting the package's two descriptions of `E`. A comparison built from
> the *fibre* field — such as Stacks 04J4's identification of the inverse image of a relocalization
> with a base change — and one built from the *counit* of `j_!` — such as Stacks 04IE's
> identification of the inverse image of a localization with a product — are otherwise assertions
> about data that nothing relates, even though both come from the same `E`. Both sides here are
> morphisms out of the fibre presheaf of `T`, so comparing them needs no further transport.

```lean
theorem Presheaf.IsSheaf.app_fibers_inv_comp_unitInv {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {F : Cᵒᵖ ⥤ Type v} (hF : Presheaf.IsSheaf J F)
    [(CostructuredArrow.proj yoneda F).IsContinuous
      ((CostructuredArrow.proj yoneda F).restrictedTopology J) J]
    (G : Sheaf J (Type v)) (X : CostructuredArrow yoneda F)
    (p : OverArrows (hF.sheafEquivalenceCostructuredArrowYoneda.equivalence.functor.obj
        (((CostructuredArrow.proj yoneda F).sheafPushforwardContinuous (Type v)
          ((CostructuredArrow.proj yoneda F).restrictedTopology J) J).obj G)).hom.hom X.hom) :
    (hF.sheafEquivalenceCostructuredArrowYoneda.fibers.inv.app
          (hF.sheafEquivalenceCostructuredArrowYoneda.equivalence.functor.obj
            (((CostructuredArrow.proj yoneda F).sheafPushforwardContinuous (Type v)
              ((CostructuredArrow.proj yoneda F).restrictedTopology J) J).obj G)) ≫
        (hF.sheafEquivalenceCostructuredArrowYoneda.equivalence.unitInv.app
            (((CostructuredArrow.proj yoneda F).sheafPushforwardContinuous (Type v)
              ((CostructuredArrow.proj yoneda F).restrictedTopology J) J).obj G)).hom).app
        (op X) p =
      (hF.sheafEquivalenceCostructuredArrowYoneda.shriek.counit.app G).hom.app (op X.left)
        p.val
```

**`CategoryTheory.Presheaf.IsSheaf.app_fibers_inv_comp_homEquiv_shriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/LocalizationOfTopoi.lean, line 916](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/LocalizationOfTopoi.lean#L916). The attribute's comment: “transposing across `j_! ⊣ j^{-1}` is evaluation on fibres”.

> **Stacks 0791: transposing across `j_! ⊣ j^{-1}` is evaluation on fibres.** Let `T` be an
> object of `Sh(C)/F` and `β : T.left ⟶ G` a morphism of sheaves on `C`. Reading `β` as a morphism
> out of `j_!` of the fibre sheaf of `T` — which is what precomposing with the counit of the
> equivalence does — and transposing it across `j_! ⊣ j^{-1}` gives a morphism from the fibre sheaf
> of `T` to `j^{-1}G`. This says that that morphism sends a section `t` of `T.left` over `U` lying
> in the fibre over `s ∈ F(U)` to `β(t)`.
>
> This is the general form of `app_fibers_inv_comp_unitInv`, which is the case
> `T = E(j^{-1}G)`, `β` the counit; it is what a comparison built from the `fibers` field has to be
> fed through in order to be compared with one built from the counit of `j_!`, since the underlying
> sheaf `T.left` of an object in the image of `E` has no description other than by its fibres.
> Everything in `j_!`'s adjunction cancels against the equivalence, so the content is exactly the
> fibre hom bijection of the source's proof.

```lean
theorem Presheaf.IsSheaf.app_fibers_inv_comp_homEquiv_shriek {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} {F : Cᵒᵖ ⥤ Type v} (hF : Presheaf.IsSheaf J F)
    [(CostructuredArrow.proj yoneda F).IsContinuous
      ((CostructuredArrow.proj yoneda F).restrictedTopology J) J]
    (T : Over (⟨F, hF⟩ : Sheaf J (Type v))) (G : Sheaf J (Type v)) (β : T.left ⟶ G)
    (X : CostructuredArrow yoneda F) (p : OverArrows T.hom.hom X.hom) :
    (hF.sheafEquivalenceCostructuredArrowYoneda.fibers.inv.app T ≫
        (hF.sheafEquivalenceCostructuredArrowYoneda.shriek.homEquiv
            (hF.sheafEquivalenceCostructuredArrowYoneda.equivalence.inverse.obj T) G
            ((Over.forget (⟨F, hF⟩ : Sheaf J (Type v))).map
              (hF.sheafEquivalenceCostructuredArrowYoneda.equivalence.counit.app T) ≫
                β)).hom).app
        (op X) p =
      β.hom.app (op X.left) p.val
```

**`CategoryTheory.Presheaf.IsSheaf.exists_sheafEquivalence_costructuredArrow_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/LocalizationOfTopoi.lean, line 956](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/LocalizationOfTopoi.lean#L956). The attribute's comment: “Sheaves on the site `C/F` of pairs `(U, s)` with `s ∈ F(U)`, whose coverings are those of `C`: `C/F` is a site, `j` is continuous and cocontinuous, the canonical equivalence `PSh(C)/F ≌ PSh(C/F)` matches sheaves with sheaves, and it restricts to an equivalence `Sh(C/F) ≌ Sh(C)/F` carrying `j_!` to `Over.forget`, i.e. turning `j` into `j_F`.”. References: SGA 4 III (5.2), “special case”.

> **Stacks 0791.** Let `(C, J)` be a site and let `F` be a sheaf of sets on `C`. Let
> `C/F = CostructuredArrow yoneda F` be the category of pairs `(U, s)` with `s ∈ F(U)`, with its
> projection `j = CostructuredArrow.proj yoneda F` to `C`, and declare a family
> `{(U_i, s_i) ⟶ (U, s)}` to be a covering when `{U_i ⟶ U}` is a covering of `C`, i.e. give `C/F`
> the topology `j.restrictedTopology J` generated by those families. Then:
>
> 1. `C/F` is a site with exactly those coverings: a sieve of `(U, s)` is covering for
>    `j.restrictedTopology J` if and only if its image under `j` is a covering sieve of `U`;
> 2. the canonical equivalence `Over F ≌ PSh(C/F)` of `overEquivPresheafCostructuredArrow` matches
>    sheaves with sheaves: for an object `φ : G ⟶ F` of `PSh(C)/F`, the presheaf
>    `(U, s) ↦ {t ∈ G(U) | φ(t) = s}` on `C/F` is a sheaf if and only if `G` is a sheaf on `C`;
> 3. `j` is continuous and cocontinuous, so that it induces a morphism of topoi
>    `j : Sh(C/F) ⟶ Sh(C)` with `j^{-1}` restriction (Stacks 00XR); and
> 4. there is an equivalence `E : Sh(C/F) ≌ Sh(C)/F`, namely the restriction of that canonical
>    equivalence — `E.inverse` is `(G, φ) ↦ ((U, s) ↦ {t ∈ G(U) | φ(t) = s})` on underlying
>    presheaves — for which `E.functor` followed by `Over.forget` is left adjoint to `j^{-1}`, that
>    is, is `j_!`. Since `Over.forget` is the `j_{F!}` of Stacks 04GZ, this is the assertion that
>    `E` turns `j` into the localization morphism `j_F`.

```lean
public theorem Presheaf.IsSheaf.exists_sheafEquivalence_costructuredArrow_yoneda {C : Type u}
    [Category.{v} C] {J : GrothendieckTopology C} {F : Cᵒᵖ ⥤ Type v} (hF : Presheaf.IsSheaf J F) :
    (∀ (X : CostructuredArrow yoneda F) (S : Sieve X),
        S ∈ (CostructuredArrow.proj yoneda F).restrictedTopology J X ↔
          Sieve.functorPushforward (CostructuredArrow.proj yoneda F) S ∈ J X.left) ∧
      (∀ T : Over F,
        Presheaf.IsSheaf ((CostructuredArrow.proj yoneda F).restrictedTopology J)
            ((overEquivPresheafCostructuredArrow F).functor.obj T) ↔
          Presheaf.IsSheaf J T.left) ∧
      ∃ (_ :
        (CostructuredArrow.proj yoneda F).IsContinuous
          ((CostructuredArrow.proj yoneda F).restrictedTopology J) J)
        (_ :
        (CostructuredArrow.proj yoneda F).IsCocontinuous
          ((CostructuredArrow.proj yoneda F).restrictedTopology J) J)
        (E :
        Sheaf ((CostructuredArrow.proj yoneda F).restrictedTopology J) (Type v) ≌
          Over (⟨F, hF⟩ : Sheaf J (Type v))),
        Nonempty
            (E.inverse ⋙
                sheafToPresheaf ((CostructuredArrow.proj yoneda F).restrictedTopology J) (Type v) ≅
              Over.post (X := (⟨F, hF⟩ : Sheaf J (Type v))) (sheafToPresheaf J (Type v)) ⋙
                (overEquivPresheafCostructuredArrow F).functor) ∧
          Nonempty
            (E.functor ⋙ Over.forget (⟨F, hF⟩ : Sheaf J (Type v)) ⊣
              (CostructuredArrow.proj yoneda F).sheafPushforwardContinuous (Type v)
                ((CostructuredArrow.proj yoneda F).restrictedTopology J) J)
```

## Tag 04IP, a definition

[Tag 04IP](https://stacks.math.columbia.edu/tag/04IP) in the Stacks Project.

**`localizationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationMorphism.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/LocalizationMorphism.lean#L46). The attribute's comment: “(2): the localization morphism j\_F : Sh(C)/F → Sh(C)”.

> **Stacks 04IP (2).** The *localization morphism* of the topos `Sh(C, J)` at a sheaf `F` is the
> morphism of topoi `j_F : Sh(C, J)/F ⟶ Sh(C, J)` of Stacks 04GZ: its inverse image `j_F⁻¹` is
> `H ↦ (H × F ⟶ F)`, which is left exact, and its pushforward `j_{F,*}` is the right adjoint of
> `j_F⁻¹` given by sections over `F`. Its source is `toposLocalization J F`, the localization of the
> topos `Sh(C, J)` at `F` (Stacks 04IP (1)).

```lean
noncomputable def localizationMorphism (F : Sheaf J (Type (max u v))) :
    MorphismOfTopoi (toposLocalization J F) (Sheaf J (Type (max u v)))
```

**`toposLocalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/ToposLocalizationMorphism.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/ToposLocalizationMorphism.lean#L39). The attribute's comment: “(1): the localization Sh(C)/F of the topos Sh(C) at F”. References: SGA 4 IV (5.1).

> The localization of the topos of sheaves `Sh(C, J)` at a sheaf `F` is the
> slice (over) category `Sh(C, J) / F`. Objects are pairs `(G, φ)` where `G` is a
> sheaf on `C` and `φ : G ⟶ F` is a morphism of sheaves, and morphisms are
> commuting triangles over `F`.

```lean
abbrev toposLocalization (F : Sheaf J (Type (max u v)))
```

## Tag 04IQ, a lemma

[Tag 04IQ](https://stacks.math.columbia.edu/tag/04IQ) in the Stacks Project.

**`CategoryTheory.OverShriek.sheafFunctorToOverCompForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/ToposComparison.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/ToposComparison.lean#L90). The attribute's comment: “j\_\{F!} = j\_\{U!} for F = h\_U^#: the lower shrieks agree”.

> **Stacks 04IQ**, on lower shrieks: `j_{F!} ∘ Φ_U = j_{U!}` for `F = h_U^#`.
>
> The lower shriek of the localization morphism `j_F` of Stacks 04GZ is the forgetful functor
> `Over.forget F` (`MorphismOfTopoi.overLocalizationShriek`), so this says that the sheaf underlying
> `Φ_U G` is `j_{U!}G`.

```lean
def sheafFunctorToOverCompForgetIso :
    sheafFunctorToOver (U := U) J ⋙
        Over.forget ((presheafToSheaf J (Type v)).obj (yoneda.obj U)) ≅
      (Over.forget U).sheafPullback (Type v) (J.over U) J
```

**`CategoryTheory.OverShriek.overPullbackCompSheafFunctorToOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/ToposComparison.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/ToposComparison.lean#L110). The attribute's comment: “j\_F^\{-1} = j\_U^\{-1} for F = h\_U^#: the inverse images agree”.

> **Stacks 04IQ**, on inverse images: `j_F^{-1} = j_U^{-1}` for `F = h_U^#`, i.e.
> `j_U^{-1} ⋙ Φ_U ≅ toOver F`.

```lean
def overPullbackCompSheafFunctorToOverIso :
    J.overPullback (Type v) U ⋙ sheafFunctorToOver (U := U) J ≅
      toOver ((presheafToSheaf J (Type v)).obj (yoneda.obj U))
```

**`CategoryTheory.OverShriek.sheafFunctorToOverCompPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/ToposComparison.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/ToposComparison.lean#L206). The attribute's comment: “j\_\{F,*} = j\_\{U,*} for F = h\_U^#: the pushforwards agree”.

> **Stacks 04IQ**, on pushforwards: `j_{F,*} = j_{U,*}` for `F = h_U^#`, i.e.
> `Φ_U ⋙ j_{F,*} ≅ j_{U,*}`.
>
> Both pushforwards are taken as data, as in `MorphismOfTopoi.overLocalization` and Stacks 04H0 and
> 04IR: `p` is a right adjoint of `j_F^{-1} = toOver F` and `q` a right adjoint of `j_U^{-1}`.

```lean
def sheafFunctorToOverCompPushforwardIso
    {p : Over ((presheafToSheaf J (Type v)).obj (yoneda.obj U)) ⥤ Sheaf J (Type v)}
    (adjp : toOver ((presheafToSheaf J (Type v)).obj (yoneda.obj U)) ⊣ p)
    {q : Sheaf (J.over U) (Type v) ⥤ Sheaf J (Type v)}
    (adjq : J.overPullback (Type v) U ⊣ q) :
    sheafFunctorToOver (U := U) J ⋙ p ≅ q
```

## Tag 04IR, a lemma

[Tag 04IR](https://stacks.math.columbia.edu/tag/04IR) in the Stacks Project.

**`CategoryTheory.starIteratedSliceForwardIsoPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/IteratedSlice.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/IteratedSlice.lean#L58). The attribute's comment: “j = j\_\{G/F} and j^\{-1}(H → F) = (H ×\_F G → G)”. References: SGA 7 VII (2.0), “partial”.

> Let `s : G ⟶ F` be a morphism of a topos `E` and write `G/F` for the corresponding object of
> the slice topos `E/F`.  Localizing `E/F` at `G/F` produces the morphism of topoi whose inverse
> image is `Over.star (Over.mk s)`; transporting it along the iterated slice equivalence
> `(E/F)/(G/F) ≌ E/G` identifies it with base change along `s`:
> ```
> j⁻¹(H ⟶ F) = (H ×_F G ⟶ G).
> ```
> Together with `map_eq_forget_iteratedSlice` (Stacks 03EH), which identifies the corresponding
> lower shriek with `Over.map s`, this is the assertion that `j` is the localization of `E/F` at
> `G/F`.

```lean
noncomputable def starIteratedSliceForwardIsoPullback [HasPullbacks E] :
    Over.star (Over.mk s) ⋙ (Over.mk s).iteratedSliceForward ≅ Over.pullback s
```

**`CategoryTheory.pushforwardIsoCompPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/SliceTopos/IteratedSlice.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/SliceTopos/IteratedSlice.lean#L72). The attribute's comment: “j\_\{G,*} = j\_\{F,*} ∘ j\_*”.

> The pushforwards of the localizations satisfy `j_{G,*} = j_{F,*} ∘ j_*`.
>
> The inverse images satisfy `j_G⁻¹ = j⁻¹ ∘ j_F⁻¹`, which is `Over.starPullbackIsoStar`; passing
> to right adjoints turns this into the stated identity between the pushforwards.  The three
> pushforwards are given as data, since a general category with pullbacks and binary products
> need not have them (in a topos they exist, by Stacks 04GZ).

```lean
noncomputable def pushforwardIsoCompPushforward [HasPullbacks E] [HasBinaryProducts E]
    {pF : Over F ⥤ E} {pG : Over G ⥤ E} {p : Over G ⥤ Over F}
    (adjF : Over.star F ⊣ pF) (adjG : Over.star G ⊣ pG) (adj : Over.pullback s ⊣ p) :
    pG ≅ p ⋙ pF
```

## Tag 04IS, a lemma

[Tag 04IS](https://stacks.math.columbia.edu/tag/04IS) in the Stacks Project.

**`CategoryTheory.OverShriek.relocalizeToposInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizeTopos.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizeTopos.lean#L80). The attribute's comment: “the inverse images of the two relocalizations agree, via 00Y1”.

> **Stacks 04IS**, on inverse images.  Under the identification of Stacks 00Y1, used in the
> forward direction `Φ_U = sheafFunctorToOver J`, the inverse image `j^{-1}` of the relocalization
> functor `j = Over.map f` of diagram (04IK) is the inverse image
> `Over.star (h_V^#/h_U^#) ⋙ iteratedSliceForward` of the localization of the topos `Sh(C)/h_U^#` at
> the object `h_V^#/h_U^#` of Stacks 04IR.
>
> This is Stacks' proof: by Stacks 04IL the left-hand side is base change along `h_f^#`, and by
> Stacks 04IR so is the right-hand side.

```lean
def relocalizeToposInverseImageIso :
    (Over.map f).sheafPushforwardContinuous (Type v) (J.over V) (J.over U) ⋙
        sheafFunctorToOver (U := V) J ≅
      sheafFunctorToOver (U := U) J ⋙
        Over.star (Over.mk ((presheafToSheaf J (Type v)).map (yoneda.map f))) ⋙
          (Over.mk ((presheafToSheaf J (Type v)).map (yoneda.map f))).iteratedSliceForward
```

**`CategoryTheory.OverShriek.relocalizeToposShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/RelocalizeTopos.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/RelocalizeTopos.lean#L101). The attribute's comment: “the lower shrieks of the two relocalizations agree, via 00Y1”.

> **Stacks 04IS**, on lower shrieks.  Under the identification of Stacks 00Y1, used in the
> forward direction `Φ_U = sheafFunctorToOver J`, the lower shriek `j_!` of the relocalization
> functor `j = Over.map f` of diagram (04IK) is the lower shriek
> `iteratedSliceBackward ⋙ Over.forget (h_V^#/h_U^#)` of the localization of the topos `Sh(C)/h_U^#`
> at the object `h_V^#/h_U^#` of Stacks 04IR.
>
> By Stacks 04IL the left-hand side is postcomposition with `h_f^#`, and by
> `Over.iteratedSliceBackward_forget` — the identity underlying Stacks 04IR's description of `j_!` —
> so is the right-hand side.

```lean
def relocalizeToposShriekIso :
    (Over.map f).sheafPullback (Type v) (J.over V) (J.over U) ⋙ sheafFunctorToOver (U := U) J ≅
      sheafFunctorToOver (U := V) J ⋙
        (Over.mk ((presheafToSheaf J (Type v)).map (yoneda.map f))).iteratedSliceBackward ⋙
          Over.forget (Over.mk ((presheafToSheaf J (Type v)).map (yoneda.map f)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.30, Tag 04GY](https://stacks.math.columbia.edu/tag/04GY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
