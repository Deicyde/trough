---
declaration: section
origin: cited
lean: Stacks.Blowup.strictTransformSheaf, Stacks.Blowup.strictTransformIdeal, Stacks.Blowup.strictTransform, Stacks.Blowup.ideal_strictTransformIdeal, Stacks.Blowup.isQuasicoherent_strictTransformSheaf, Stacks.StrictTransform.sheaf, Stacks.StrictTransform.ideal, Stacks.StrictTransform.scheme
statement: formalized
proof: formalized
---

# 31.34 Strict transform

Section 31.34 of the Stacks Project, [Tag 080C](https://stacks.math.columbia.edu/tag/080C). 7 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 080D, a definition

[Tag 080D](https://stacks.math.columbia.edu/tag/080D) in the Stacks Project.

**`Stacks.Blowup.strictTransformSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransform.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransform.lean#L164). The attribute's comment: “strict transform of a module”.

> The strict transform of an `𝒪_X`-module `ℱ` along the blowup of the base in `ℐ`: the
> quotient of the pullback of `ℱ` to `X ×_S S'` by the submodule of sections supported on the
> inverse image of the exceptional divisor.

```lean
abbrev strictTransformSheaf (ℱ : X.Modules) : (blowUpPullback f ℐ).Modules
```

**`Stacks.Blowup.strictTransformIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransform.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransform.lean#L172). The attribute's comment: “ideal of the strict transform of a scheme”.

> The quasi-coherent ideal of sections of `𝒪_{X ×_S S'}` supported on the inverse image of
> the exceptional divisor, assembled from its modules of sections over the affine opens of
> `X ×_S S'`.

```lean
def strictTransformIdeal : (blowUpPullback f ℐ).IdealSheafData
```

**`Stacks.Blowup.strictTransform`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransform.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransform.lean#L210). The attribute's comment: “strict transform of a scheme”.

> The strict transform of `X` along the blowup of the base in `ℐ`: the closed subscheme of
> `X ×_S S'` cut out by the ideal of sections supported on the inverse image of the exceptional
> divisor.

```lean
abbrev strictTransform : Scheme.{u}
```

**`Stacks.Blowup.ideal_strictTransformIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformRetrocompact.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformRetrocompact.lean#L130). The attribute's comment: “the defining ideal of the strict transform of a scheme, with no hypothesis”.

> **Stacks Project, Tag 080D, part (2).** On an affine open, the defining ideal of the strict
> transform of `X` consists of exactly the sections of `𝒪_{X ×_S S'}` supported on `pr_{S'}⁻¹ E`.
> This is `Stacks.Blowup.ideal_strictTransformIdeal_of_quasiCompact` with its retrocompactness
> hypothesis discharged, so it is the equality that tag 080D's definition asserts.

```lean
theorem ideal_strictTransformIdeal (U : (blowUpPullback f ℐ).affineOpens) :
    (strictTransformIdeal f ℐ).ideal U =
      (SheafOfModules.supportedSectionsSubmodule (exceptionalPullbackSet f ℐ)
        (SheafOfModules.unit (blowUpPullback f ℐ).ringCatSheaf)).toSubmodule.obj
          (Opposite.op U.1)
```

**`Stacks.Blowup.isQuasicoherent_strictTransformSheaf`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformRetrocompact.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/StrictTransformRetrocompact.lean#L142). The attribute's comment: “the strict transform of a quasi-coherent module is quasi-coherent”.

> **Stacks Project, Tag 080D, part (1).** The strict transform of a quasi-coherent module is
> quasi-coherent on `X ×_S S'`, with no hypothesis. Recorded as an instance because the strict
> transform of a strict transform is formed by instance search on the quasi-coherence of the
> first.

```lean
instance isQuasicoherent_strictTransformSheaf (ℱ : X.Modules) [ℱ.IsQuasicoherent] :
    (strictTransformSheaf f ℐ ℱ).IsQuasicoherent
```

**`Stacks.StrictTransform.sheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/Basic.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/Basic.lean#L256). The attribute's comment: “strict transform of a module”.

> **Stacks Project, Tag 080D (1).** The strict transform of a sheaf of `𝒪_X`-modules `F`: the
> quotient of `pr_X^* F` by the submodule of sections supported on `pr_{S'}^{-1}(Supp E)`.

```lean
public abbrev sheaf (F : X.Modules) : (baseChange f b).Modules
```

**`Stacks.StrictTransform.ideal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/Basic.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/Basic.lean#L297). The attribute's comment: “ideal of the strict transform of a scheme”.

> The quasi-coherent ideal of sections of `𝒪_{X ×_S S'}` supported on
> `pr_{S'}^{-1}(Supp E)`, assembled from its values on affine opens.

```lean
public def ideal : (baseChange f b).IdealSheafData
```

**`Stacks.StrictTransform.scheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/Basic.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/Basic.lean#L305). The attribute's comment: “strict transform of a scheme”. References: SGA 7 X (2.4), “more general”.

> **Stacks Project, Tag 080D (2).** The strict transform of `X`: the closed subscheme of
> `X ×_S S'` cut out by the ideal of sections supported on `pr_{S'}^{-1}(Supp E)`.

```lean
public abbrev scheme : Scheme.{u}
```

## Tag 080E, a lemma

[Tag 080E](https://stacks.math.columbia.edu/tag/080E) in the Stacks Project.

**`AlgebraicGeometry.strictTransformBlowUpIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/InverseImageCentre.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/InverseImageCentre.lean#L255). The attribute's comment: “scheme”. References: SGA 5 VII (9.5), “First clause only”.

> The strict transform of `X` under the blowup of `S` in `ℐ` is the blowup of `X` in the
> inverse image of `ℐ`, canonically as `X`-schemes.

```lean
def strictTransformBlowUpIso :
    Over.mk ((Stacks.StrictTransform.ideal f (blowUpToBase ℐ) (exceptionalIdeal ℐ)).subschemeι ≫
      pullback.fst f (blowUpToBase ℐ)) ≅ Over.mk (blowUpToBase (ℐ.comap f))
```

**`AlgebraicGeometry.strictTransformSheafBlowUpIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/InverseImageCentre.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/InverseImageCentre.lean#L530). The attribute's comment: “sheaf”.

> For a sheaf of `𝒪_X`-modules `F`, the strict
> transform of `F` under the blowup of `S` in `ℐ` is canonically the direct image, along the closed
> immersion `X' ⟶ X ×_S S'` of part (1), of the strict transform of `F` relative to the blowup of
> `X` in the inverse image `ℐ·𝒪_X`. The sheaf `F` is not assumed quasi-coherent.

```lean
def strictTransformSheafBlowUpIso (F : X.Modules) :
    sheaf f (blowUpToBase ℐ) (exceptionalIdeal ℐ) F ≅
      (Scheme.Modules.pushforward (strictTransformBlowUpι f ℐ)).obj
        (sheaf (𝟙 X) (blowUpToBase (ℐ.comap f)) (exceptionalIdeal (ℐ.comap f)) F)
```

## Tag 080F, a lemma

[Tag 080F](https://stacks.math.columbia.edu/tag/080F) in the Stacks Project.

**`AlgebraicGeometry.strictTransformIdeal_eq_bot_of_flat_at_exceptional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/Flat.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/Flat.lean#L220). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 080F (1).** If `X` is flat over `S` at every point lying over the
> centre of the blowup, then the strict transform of `X` is the whole base change `X ×_S S'`: the
> ideal cutting it out is zero.

```lean
public theorem strictTransformIdeal_eq_bot_of_flat_at_exceptional
    {X S : Scheme.{u}} (f : X ⟶ S) (I : S.IdealSheafData)
    (hflat : ∀ x : X, f x ∈ I.support → IsFlatAt f.toLRSHom.toShHom x) :
    Stacks.StrictTransform.ideal f (blowUpToBase I) (exceptionalIdeal I) = ⊥
```

**`AlgebraicGeometry.isIso_strictTransformSheaf_quotient_of_flat_at_exceptional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/Flat.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/Flat.lean#L242). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 080F (2).** If a quasi-coherent `𝒪_X`-module `F` is flat over `S` at
> every point lying over the centre of the blowup, then the canonical quotient map from `pr_X^* F`
> onto the strict transform of `F` is an isomorphism.

```lean
public theorem isIso_strictTransformSheaf_quotient_of_flat_at_exceptional
    {X S : Scheme.{u}} (f : X ⟶ S) (I : S.IdealSheafData) (F : X.Modules) [F.IsQuasicoherent]
    (hflat : ∀ x : X, f x ∈ I.support → IsFlatOverAt f.toLRSHom.toShHom F x) :
    IsIso (Stacks.StrictTransform.π f (blowUpToBase I) (exceptionalIdeal I) F)
```

## Tag 080G, a lemma

[Tag 080G](https://stacks.math.columbia.edu/tag/080G) in the Stacks Project.

**`AlgebraicGeometry.strictTransformSheafPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/AffinePushforward.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/AffinePushforward.lean#L379).

> **Stacks Project, Tag 080G.** Let `b : S' ⟶ S` be the blowup of `S` in a closed subscheme
> cut out by the quasi-coherent ideal sheaf `I`, let `g : X ⟶ Y` be an affine morphism of schemes
> over `S`, let `F` be a quasi-coherent `𝒪_X`-module and let `g' : X ×_S S' ⟶ Y ×_S S'` be the
> base change of `g`. Then `g'_*` of the strict transform of `F` relative to `b` is the strict
> transform of `g_* F`.

```lean
def strictTransformSheafPushforwardIso {X Y S : Scheme.{u}}
    (g : X ⟶ Y) (f : Y ⟶ S) (I : S.IdealSheafData)
    (F : X.Modules) [IsAffineHom g] [F.IsQuasicoherent] :
    let g' : Stacks.StrictTransform.baseChange (g ≫ f) (blowUpToBase I) ⟶
        Stacks.StrictTransform.baseChange f (blowUpToBase I) :=
      pullback.lift
        (pullback.fst (g ≫ f) (blowUpToBase I) ≫ g)
        (pullback.snd (g ≫ f) (blowUpToBase I))
        (by rw [Category.assoc]; exact pullback.condition)
    (Scheme.Modules.pushforward g').obj
        (Stacks.StrictTransform.sheaf (g ≫ f) (blowUpToBase I) (exceptionalIdeal I) F) ≅
      Stacks.StrictTransform.sheaf f (blowUpToBase I) (exceptionalIdeal I)
        ((Scheme.Modules.pushforward g).obj F)
```

## Tag 080H, a lemma

[Tag 080H](https://stacks.math.columbia.edu/tag/080H) in the Stacks Project.

**`AlgebraicGeometry.blowUpProductIso_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/CartierProduct.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/CartierProduct.lean#L205). The attribute's comment: “part (1): isomorphism of blowups”.

> **Stacks Project, Tag 080H**, part (1). Let `D` be an effective Cartier divisor on `S` and
> let `I` be any quasi-coherent ideal sheaf. The blowup of `S` in `I * D` is the blowup of `S` in
> `I`, as `S`-schemes.

```lean
theorem blowUpProductIso_exists {S : Scheme.{u}} (I D : S.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) :
    Nonempty (Over.mk (blowUpToBase I) ≅ Over.mk (blowUpToBase (I * D)))
```

**`Stacks.StrictTransform.exists_baseChange_iso_sheaf_iso_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/DifferentCentres.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/DifferentCentres.lean#L391). The attribute's comment: “part (2): strict transforms of modules”.

> **[Stacks, Tag 080H] part (2).** Let `D` be an effective Cartier divisor on `S` and let `F`
> be a sheaf of `𝒪_X`-modules with no nonzero local sections supported in `f^{-1}D`. Given an
> isomorphism `e` of the blowup of `S` in `I` with the blowup of `S` in `I * D` over `S` — part (1)
> of the tag — the induced isomorphism of the two base changes, specified by both its projections,
> carries the strict transform of `F` for the centre `I * D` to the strict transform for the centre
> `I`.
>
> Part (1) of the tag, which supplies `e`, is not in the repository; see the implementation notes
> of this file. Everything else here is unconditional, [Stacks, Tag 02OS] part (1) being the
> instance `AlgebraicGeometry.isIso_blowUpToBase_restrict_compl_support`.
>
> The hypothesis `_hD` that `D` is an effective Cartier divisor is the tag's, and is retained so
> that the statement is the tag's; it is used only through `e`, which part (1) deduces from it, so
> the conclusion in fact holds for any `D` admitting such an `e`.

```lean
public theorem exists_baseChange_iso_sheaf_iso_mul (f : X ⟶ S) (I D : S.IdealSheafData)
    (_hD : Stacks.Divisors.IsEffectiveCartierDivisor D) (F : X.Modules)
    (hF : ∀ (U : X.Opens) (s : Γ(F, U)),
      s ∈ (supportedSectionsSubmodule (f.base ⁻¹' D.supportSet) F).toSubmodule.obj (op U) →
        s = 0)
    (e : Over.mk (AlgebraicGeometry.blowUpToBase I) ≅
      Over.mk (AlgebraicGeometry.blowUpToBase (I * D))) :
    ∃ g : baseChange f (AlgebraicGeometry.blowUpToBase I) ≅
        baseChange f (AlgebraicGeometry.blowUpToBase (I * D)),
      (g.hom ≫ pullback.fst f (AlgebraicGeometry.blowUpToBase (I * D)) =
        pullback.fst f (AlgebraicGeometry.blowUpToBase I)) ∧
      (g.hom ≫ pullback.snd f (AlgebraicGeometry.blowUpToBase (I * D)) =
        pullback.snd f (AlgebraicGeometry.blowUpToBase I) ≫ e.hom.left) ∧
      Nonempty ((Scheme.Modules.pullback g.hom).obj
        (sheaf f (AlgebraicGeometry.blowUpToBase (I * D))
          (AlgebraicGeometry.exceptionalIdeal (I * D)) F) ≅
        sheaf f (AlgebraicGeometry.blowUpToBase I)
          (AlgebraicGeometry.exceptionalIdeal I) F)
```

## Tag 080I, a lemma

[Tag 080I](https://stacks.math.columbia.edu/tag/080I) in the Stacks Project.

**`Stacks.StrictTransform.strictTransformSheaf_comp_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/CompositionBlowUp.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/CompositionBlowUp.lean#L191). The attribute's comment: “part (1): strict transform of a module”.

> **[Stacks, Tag 080I] part (1).** For `b` the blowup of `S` in `I`, `c` the blowup of the
> blowup in `J`, and `d` the blowup of `S` in a third centre `K` whose support is
> `Supp I ∪ b(Supp J)`, the iterated strict transform of `F` agrees with the strict transform in
> the composite centre, compatibly with both projections and with the quotient maps.
>
> This is `Stacks.StrictTransform.exists_baseChange_iso_sheaf_iso_comp_blowUp` with its one
> hypothesis `hQJ` discharged by
> `Stacks.StrictTransform.supportedSections_sheaf_blowUp_union_eq_zero`, applied on the first base
> change over the first blowup with centre `J` and divisor `AlgebraicGeometry.exceptionalIdeal I`,
> whose own hypothesis is the defining property
> `Stacks.StrictTransform.supportedSections_sheaf_eq_zero` of the first strict transform.
> Unconditional.

```lean
public theorem strictTransformSheaf_comp_blowUp (f : X ⟶ S) (I K : S.IdealSheafData)
    (J : (AlgebraicGeometry.blowUp I).IdealSheafData)
    (hK : K.supportSet = I.supportSet ∪
      (AlgebraicGeometry.blowUpToBase I).base '' J.supportSet)
    (e : Over.mk (AlgebraicGeometry.blowUpToBase J ≫ AlgebraicGeometry.blowUpToBase I) ≅
      Over.mk (AlgebraicGeometry.blowUpToBase K))
    (F : X.Modules) :
    let b := AlgebraicGeometry.blowUpToBase I
    let f₁ : baseChange f b ⟶ AlgebraicGeometry.blowUp I := pullback.snd f b
    let c := AlgebraicGeometry.blowUpToBase J
    let d := AlgebraicGeometry.blowUpToBase K
    let pK := pullback.fst f d
    let pI := pullback.fst f b
    let pJ := pullback.fst f₁ c
    let FK := (Scheme.Modules.pullback pK).obj F
    let FI := (Scheme.Modules.pullback pI).obj F
    let QK := sheaf f d (AlgebraicGeometry.exceptionalIdeal K) F
    let QI := sheaf f b (AlgebraicGeometry.exceptionalIdeal I) F
    let QJ := sheaf f₁ c (AlgebraicGeometry.exceptionalIdeal J) QI
    ∃ (g : baseChange f₁ c ≅ baseChange f d) (hg : g.hom ≫ pK = pJ ≫ pI),
      (g.hom ≫ pullback.snd f d = pullback.snd f₁ c ≫ e.hom.left) ∧
      ∃ s : (Scheme.Modules.pullback g.hom).obj QK ≅ QJ,
        let t : (Scheme.Modules.pullback g.hom).obj FK ≅ (Scheme.Modules.pullback pJ).obj FI :=
          ((Scheme.Modules.pullbackComp g.hom pK).app F) ≪≫
            ((Scheme.Modules.pullbackCongr hg).app F) ≪≫
            ((Scheme.Modules.pullbackComp pJ pI).symm.app F)
        let qK : FK ⟶ QK := π f d (AlgebraicGeometry.exceptionalIdeal K) F
        let qI : FI ⟶ QI := π f b (AlgebraicGeometry.exceptionalIdeal I) F
        let qJ : (Scheme.Modules.pullback pJ).obj QI ⟶ QJ :=
          π f₁ c (AlgebraicGeometry.exceptionalIdeal J) QI
        (Scheme.Modules.pullback g.hom).map qK ≫ s.hom =
          t.hom ≫ (Scheme.Modules.pullback pJ).map qI ≫ qJ
```

**`Stacks.StrictTransform.strictTransform_comp_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/CompositionScheme.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/CompositionScheme.lean#L322). The attribute's comment: “part (2): strict transform of a scheme”.

> **[Stacks, Tag 080I] part (2).** For `b` the blowup of `S` in `I`, `c` the blowup of the
> blowup in `J`, and `d` the blowup of `S` in a third centre `K` whose support is
> `Supp I ∪ b(Supp J)`, the strict transform along `c` of the strict transform of `X` along `b`
> agrees with the strict transform of `X` along `d`, compatibly with both projections.
>
> Unconditional: the support identity is
> `Stacks.StrictTransform.iso_preimage_exceptionalPreimage_blowUp` and the open immersion away from
> the second exceptional divisor is
> `Stacks.StrictTransform.isOpenImmersion_exceptionalComplement_ι_comp_fst`, both of which are
> theorems now that [Stacks, Tag 02OS] part (1) is the instance
> `AlgebraicGeometry.isIso_blowUpToBase_restrict_compl_support`.

```lean
public theorem strictTransform_comp_blowUp (f : X ⟶ S) (I K : S.IdealSheafData)
    (J : (AlgebraicGeometry.blowUp I).IdealSheafData)
    (hK : K.supportSet = I.supportSet ∪
      (AlgebraicGeometry.blowUpToBase I).base '' J.supportSet)
    (e : Over.mk (AlgebraicGeometry.blowUpToBase J ≫ AlgebraicGeometry.blowUpToBase I) ≅
      Over.mk (AlgebraicGeometry.blowUpToBase K)) :
    let X₁ := scheme f (AlgebraicGeometry.blowUpToBase I) (AlgebraicGeometry.exceptionalIdeal I)
    let f₁ : X₁ ⟶ AlgebraicGeometry.blowUp I :=
      (ideal f (AlgebraicGeometry.blowUpToBase I)
          (AlgebraicGeometry.exceptionalIdeal I)).subschemeι ≫
        pullback.snd f (AlgebraicGeometry.blowUpToBase I)
    ∃ g : scheme f₁ (AlgebraicGeometry.blowUpToBase J) (AlgebraicGeometry.exceptionalIdeal J) ≅
        scheme f (AlgebraicGeometry.blowUpToBase K) (AlgebraicGeometry.exceptionalIdeal K),
      (g.hom ≫ (ideal f (AlgebraicGeometry.blowUpToBase K)
            (AlgebraicGeometry.exceptionalIdeal K)).subschemeι ≫
          pullback.fst f (AlgebraicGeometry.blowUpToBase K) =
        (ideal f₁ (AlgebraicGeometry.blowUpToBase J)
            (AlgebraicGeometry.exceptionalIdeal J)).subschemeι ≫
          pullback.fst f₁ (AlgebraicGeometry.blowUpToBase J) ≫
          (ideal f (AlgebraicGeometry.blowUpToBase I)
            (AlgebraicGeometry.exceptionalIdeal I)).subschemeι ≫
          pullback.fst f (AlgebraicGeometry.blowUpToBase I)) ∧
      (g.hom ≫ (ideal f (AlgebraicGeometry.blowUpToBase K)
            (AlgebraicGeometry.exceptionalIdeal K)).subschemeι ≫
          pullback.snd f (AlgebraicGeometry.blowUpToBase K) =
        (ideal f₁ (AlgebraicGeometry.blowUpToBase J)
            (AlgebraicGeometry.exceptionalIdeal J)).subschemeι ≫
          pullback.snd f₁ (AlgebraicGeometry.blowUpToBase J) ≫ e.hom.left)
```

## Tag 080W, a lemma

[Tag 080W](https://stacks.math.columbia.edu/tag/080W) in the Stacks Project.

**`AlgebraicGeometry.strictTransformSheaf_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/ShortExact.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/ShortExact.lean#L590).

> **Stacks Project, Tag 080W.** A short exact sequence of quasi-coherent `𝒪_X`-modules which
> remains short exact after every base change of the base scheme `S` has short exact strict
> transforms along the blowup of `S` in any quasi-coherent ideal, with the three maps determined
> by the quotient maps onto the strict transforms.

```lean
public theorem strictTransformSheaf_shortExact {X S : Scheme.{u}} (f : X ⟶ S)
    (I : S.IdealSheafData) (C : ShortComplex X.Modules)
    [C.X₁.IsQuasicoherent] [C.X₂.IsQuasicoherent] [C.X₃.IsQuasicoherent]
    (hC : ∀ {T : Scheme.{u}} (g : T ⟶ S),
      (C.map (Scheme.Modules.pullback (pullback.fst f g))).ShortExact) :
    let b := blowUpToBase I
    let E := exceptionalIdeal I
    let p := pullback.fst f b
    let F₁ := (Scheme.Modules.pullback p).obj C.X₁
    let F₂ := (Scheme.Modules.pullback p).obj C.X₂
    let F₃ := (Scheme.Modules.pullback p).obj C.X₃
    let q₁ : F₁ ⟶ Stacks.StrictTransform.sheaf f b E C.X₁ := Stacks.StrictTransform.π f b E C.X₁
    let q₂ : F₂ ⟶ Stacks.StrictTransform.sheaf f b E C.X₂ := Stacks.StrictTransform.π f b E C.X₂
    let q₃ : F₃ ⟶ Stacks.StrictTransform.sheaf f b E C.X₃ := Stacks.StrictTransform.π f b E C.X₃
    ∃ (f' : Stacks.StrictTransform.sheaf f b E C.X₁ ⟶ Stacks.StrictTransform.sheaf f b E C.X₂)
      (g' : Stacks.StrictTransform.sheaf f b E C.X₂ ⟶ Stacks.StrictTransform.sheaf f b E C.X₃)
      (w : f' ≫ g' = 0),
      (ShortComplex.mk f' g' w).ShortExact ∧
        (q₁ ≫ f' = (Scheme.Modules.pullback p).map C.f ≫ q₂) ∧
        (q₂ ≫ g' = (Scheme.Modules.pullback p).map C.g ≫ q₃)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.34, Tag 080C](https://stacks.math.columbia.edu/tag/080C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
