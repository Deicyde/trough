---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.isStandardVCovering_limit_iff', AlgebraicGeometry.isStandardVCovering_of_exists_isPHCovering_limit, AlgebraicGeometry.exists_isPHCovering_limit_of_exists_isHCovering_limit, AlgebraicGeometry.isStandardVCovering_limit_tfae_unconditional, AlgebraicGeometry.isStandardVCovering_limit_equivalences, AlgebraicGeometry.isVSheaf_of_isSheafFor_vCovering_of_isLimitPreserving, AlgebraicGeometry.ExtendingFunctors.isVSheafOver_of_isSheafFor_vCovering_of_isLimitPreserving, AlgebraicGeometry.ExtendingFunctors.exists_unique_isHSheaf_isVSheaf_extension
statement: formalized
proof: formalized
---

# 61.10 The V topology and the pro-h topology

Section 61.10 of the Stacks Project, [Tag 0EVM](https://stacks.math.columbia.edu/tag/0EVM). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EVN, a lemma

[Tag 0EVN](https://stacks.math.columbia.edu/tag/0EVN) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.isStandardVCovering_limit_iff'`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/VTopologyLimits.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/VTopologyLimits.lean#L621).

> A morphism from a cofiltered limit of affine schemes over an affine base is a
> standard V covering if and only if all stage morphisms are standard V coverings.

```lean
public lemma isStandardVCovering_limit_iff'
    {I : Type u} [Category.{u} I] [IsCofiltered I]
    {Y : Scheme.{u}} [IsAffine Y]
    (D : I ⥤ Scheme.{u}) [∀ i, IsAffine (D.obj i)]
    (t : D ⟶ (Functor.const I).obj Y)
    (c : Cone D) (hc : IsLimit c)
    (f : c.pt ⟶ Y)
    (hf : c.π ≫ t = (Functor.const I).map f) :
    (letI : IsAffine c.pt := Scheme.isAffine_of_isLimit c hc
     AlgebraicGeometry.IsStandardVCovering (fun _ : Unit ↦ c.pt) (fun _ ↦ f)) ↔
      ∀ i : I,
        (letI : IsAffine (((Functor.const I).obj Y).obj i) := by
           change IsAffine Y
           infer_instance
         AlgebraicGeometry.IsStandardVCovering (fun _ : Unit ↦ D.obj i)
           (fun _ ↦ t.app i))
```

## Tag 0EVP, a lemma

[Tag 0EVP](https://stacks.math.columbia.edu/tag/0EVP) in the Stacks Project.

**`AlgebraicGeometry.isStandardVCovering_of_exists_isPHCovering_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimits.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimits.lean#L218). The attribute's comment: “(2) implies (1)”.

> A morphism of affine schemes which is a directed inverse limit over the base of affine ph
> coverings is a standard V covering.

```lean
theorem isStandardVCovering_of_exists_isPHCovering_limit
    {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (f : X ⟶ Y)
    (h : ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
        (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
        (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
        (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
        (_ : IsLimit (Cone.mk X p))
        (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
      (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
        (∀ i, IsAffine (D.obj i)) ∧
        (∀ i, IsPHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i))) :
    IsStandardVCovering (fun _ : Unit ↦ X) (fun _ ↦ f)
```

**`AlgebraicGeometry.exists_isPHCovering_limit_of_exists_isHCovering_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimits.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimits.lean#L248). The attribute's comment: “(3) implies (2)”.

> A presentation of a morphism of affine schemes as a directed inverse limit over the base of
> affine h coverings is one by affine ph coverings.

```lean
theorem exists_isPHCovering_limit_of_exists_isHCovering_limit
    {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (f : X ⟶ Y)
    (h : ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
        (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
        (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
        (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
        (_ : IsLimit (Cone.mk X p))
        (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
      (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
        (∀ i, IsAffine (D.obj i)) ∧
        (∀ i, IsHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i))) :
    ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
      (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
      (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
      (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
      (_ : IsLimit (Cone.mk X p))
      (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
      (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
        (∀ i, IsAffine (D.obj i)) ∧
        (∀ i, IsPHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i))
```

**`AlgebraicGeometry.isStandardVCovering_limit_tfae_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimits.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimits.lean#L277). The attribute's comment: “(1) implies (3); the other two implications are stated without the hard direction of Stacks 0ETR and tagged separately”.

> A morphism of affine schemes is a standard V covering exactly when it is a directed inverse
> limit over the base of affine ph coverings, and exactly when it is such a limit of affine h
> coverings.

```lean
theorem isStandardVCovering_limit_tfae_unconditional
    {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (f : X ⟶ Y) :
    List.TFAE [
      IsStandardVCovering (fun _ : Unit ↦ X) (fun _ ↦ f),
      (∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
          (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
          (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
          (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
          (_ : IsLimit (Cone.mk X p))
          (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
        (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
          (∀ i, IsAffine (D.obj i)) ∧
          (∀ i, IsPHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i))),
      (∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
          (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
          (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
          (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
          (_ : IsLimit (Cone.mk X p))
          (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
        (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
          (∀ i, IsAffine (D.obj i)) ∧
          (∀ i, IsHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i)))]
```

**`AlgebraicGeometry.isStandardVCovering_limit_equivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimitsIff.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/StandardVCoveringLimitsIff.lean#L40).

> **Stacks 0EVP.** Let `f : X ⟶ Y` be a morphism of affine schemes. Then `f` is a standard V
> covering if and only if `X` is the limit of a directed inverse system of affine schemes `Xᵢ` over
> `Y` with each `Xᵢ ⟶ Y` a ph covering, and that holds if and only if `X` is such a limit with each
> `Xᵢ ⟶ Y` an h covering.

```lean
theorem isStandardVCovering_limit_equivalences {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y]
    (f : X ⟶ Y) :
    (IsStandardVCovering (fun _ : Unit ↦ X) (fun _ ↦ f) ↔
      ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
          (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
          (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
          (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
          (_ : IsLimit (Cone.mk X p))
          (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
        (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
          (∀ i, IsAffine (D.obj i)) ∧
          (∀ i, IsPHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i))) ∧
    ((∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
          (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
          (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
          (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
          (_ : IsLimit (Cone.mk X p))
          (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
        (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
          (∀ i, IsAffine (D.obj i)) ∧
          (∀ i, IsPHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i))) ↔
      ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I)
          (_ : IsDirectedOrder I) (D : Iᵒᵖ ⥤ Scheme.{u})
          (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
          (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
          (_ : IsLimit (Cone.mk X p))
          (_ : IsColimit ((Scheme.Γ ⋙ forget CommRingCat).mapCocone (Cone.mk X p).op)),
        (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
          (∀ i, IsAffine (D.obj i)) ∧
          (∀ i, IsHCovering (fun _ : Unit ↦ D.obj i) (fun _ ↦ t.app i)))
```

## Tag 0EVQ, a lemma

[Tag 0EVQ](https://stacks.math.columbia.edu/tag/0EVQ) in the Stacks Project.

**`AlgebraicGeometry.isVSheaf_of_isSheafFor_vCovering_of_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/VTopologySheafCriterion.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/VTopologySheafCriterion.lean#L491).

> **Stacks 0EVQ.** A presheaf of sets on schemes which satisfies the sheaf condition for
> every h covering and which is limit preserving in the sense of Stacks 05LX over every base
> satisfies the sheaf condition for every V covering.
>
> An h covering is a family of morphisms locally of finite presentation satisfying one of the
> two equivalent conditions of Stacks 0ETR, and the condition used here is the second: being a V
> covering. The equivalence with the first condition, being a ph covering, is Stacks 0ETR, which
> rests on `AlgebraicGeometry.StandardVCoveringHasPHRefinement` and so on the Raynaud-Gruson
> flattening theorem; with the first condition in place of the second the statement below would
> have to carry that hypothesis, since the predicate cannot be named this far up the import
> graph.

```lean
theorem isVSheaf_of_isSheafFor_vCovering_of_isLimitPreserving (F : Scheme.{u}ᵒᵖ ⥤ Type w)
    (hH : ∀ (T : Scheme.{u}) (I : Type (max u v)) (X : I → Scheme.{u}) (g : ∀ i, X i ⟶ T),
      (∀ i, LocallyOfFinitePresentation (g i)) → IsVCovering X g →
        (Presieve.ofArrows X g).IsSheafFor F)
    (hLP : ∀ Y : Scheme.{u}, Scheme.IsLimitPreserving Y ((Over.forget Y).op ⋙ F)) :
    IsVSheaf.{u, max u v, w} F
```

**`AlgebraicGeometry.ExtendingFunctors.isVSheafOver_of_isSheafFor_vCovering_of_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/VTopologySheafCriterionOver.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/VTopologySheafCriterionOver.lean#L124). The attribute's comment: “the relative form, for a contravariant functor on the category of all schemes over `S`, which is how the source states it. The sheaf property for the h topology is read, as in the absolute case, through the second of the two equivalent conditions of Stacks 0ETR: the hypothesis is the sheaf condition for the families which are locally of finite presentation and are V coverings. Stacks 0ETR, `AlgebraicGeometry.isPHCovering_iff_isVCovering`, is what identifies that hypothesis with the ph reading fixed by `AlgebraicGeometry.IsHCovering`; it is proved in this library, further down the import graph than this file”.

> A functor on the schemes over `S` which satisfies the sheaf condition for every h covering
> of `Sch/S` and which is limit preserving in the sense of Stacks 05LX satisfies the sheaf condition
> for every V covering of `Sch/S`.
>
> The h coverings are taken in the form of the second of the two equivalent conditions of
> Stacks 0ETR: the hypothesis `hH` is the sheaf condition for the families of morphisms which are
> locally of finite presentation and are V coverings.

```lean
theorem isVSheafOver_of_isSheafFor_vCovering_of_isLimitPreserving (F : (Over S)ᵒᵖ ⥤ Type w)
    (hH : ∀ (T : Over S) (I : Type (max u v)) (X : I → Over S) (g : ∀ i, X i ⟶ T),
      (∀ i, LocallyOfFinitePresentation (g i).left) → IsVCoveringOver g →
        (Presieve.ofArrows X g).IsSheafFor F)
    (hLP : Scheme.IsLimitPreserving S F) :
    IsVSheafOver.{w, u, max u v} F
```

## Tag 0EVR, a remark

[Tag 0EVR](https://stacks.math.columbia.edu/tag/0EVR) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.exists_unique_isHSheaf_isVSheaf_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/HSheafExtensionVSheaf.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/HSheafExtensionVSheaf.lean#L400). The attribute's comment: “the whole of the remark: the extension of an h sheaf on the big h category over `S` which carries a directed inverse limit of affine objects to a filtered colimit, together with its uniqueness and every property the remark asserts of it. The extension is an h sheaf on all schemes over `S`, is limit preserving in the sense of Stacks 05LX, satisfies the sheaf property for the V topology, restricts to the given functor, and is the only functor which is an h sheaf, is limit preserving and restricts to it, up to isomorphism”.

> **Stacks 0EVR.** Let `S` be a scheme, let `P` be a full subcategory of `Sch/S` satisfying
> conditions (1) and (2) of Stacks 0EUW and let `F : Pᵒᵖ ⥤ Set` be an h sheaf whose values on a
> directed inverse limit of affine objects form the filtered colimit of its values on the system.
> Then `F` extends to a contravariant functor `F'` on all schemes over `S` which satisfies the
> sheaf property for the h topology, is limit preserving in the sense of Stacks 05LX and satisfies
> the sheaf property for the V topology, and any functor on `Sch/S` which is an h sheaf, is limit
> preserving and restricts to `F` is isomorphic to `F'`.
>
> This is the whole of the remark, the V clause included.  Properties (a) and (b) of the extension
> are Stacks 0EV3, `isHSheaf_extension` and `isLimitPreserving_extension`; the
> uniqueness is Stacks 0EUW, `exists_unique_extension`; and the V sheaf property is
> Stacks 0EVQ read through Stacks 0ETR, by
> `isVSheafOver_of_isHSheaf_of_preservesAffineLimits`.

```lean
theorem exists_unique_isHSheaf_isVSheaf_extension
    (P : ObjectProperty (Over S))
    (hP1 : HasAffineOpens P) (hP2 : HasFinitePresentationAffines P)
    (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1)))
    (hF : IsHCoveringSheafOnSubcategory.{max w (u + 1), u, u} P F)
    (hbF : PreservesAffineLimitsOnSubcategory P F) :
    ∃ (F' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1))) (_ : IsHSheaf.{max w (u + 1), u, v} F')
      (_ : PreservesAffineLimits F') (_ : IsVSheafOver.{max w (u + 1), u, v} F')
      (_ : P.ι.op ⋙ F' ≅ F),
      ∀ F'' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1)), IsHSheaf.{max w (u + 1), u, u} F'' →
        PreservesAffineLimits F'' → (P.ι.op ⋙ F'' ≅ F) → Nonempty (F' ≅ F'')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.10, Tag 0EVM](https://stacks.math.columbia.edu/tag/0EVM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
