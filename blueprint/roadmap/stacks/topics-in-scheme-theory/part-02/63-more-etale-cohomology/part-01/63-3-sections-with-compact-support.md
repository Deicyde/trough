---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.properSupportSections, AlgebraicGeometry.SmallEtale.properSupportSections_restrict, AlgebraicGeometry.SmallEtale.properSupportSections_descend, AlgebraicGeometry.SmallEtale.fShriekSubsheaf, AlgebraicGeometry.SmallEtale.mem_range_fShriekSubsheaf_arrow_iff, AlgebraicGeometry.SmallEtale.abelianExtensionByZeroToPushforward_range_eq_fShriekSubsheaf, AlgebraicGeometry.SmallEtale.properSupportIsoPushforward, AlgebraicGeometry.SmallEtale.fShriekSubsheaf_arrow_isIso
statement: formalized
proof: formalized
---

# 63.3 Sections with compact support

Section 63.3 of the Stacks Project, [Tag 0F4W](https://stacks.math.columbia.edu/tag/0F4W). 17 tags here are carried by 44 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F4X, a lemma

[Tag 0F4X](https://stacks.math.columbia.edu/tag/0F4X) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean#L152). The attribute's comment: “the proper support condition”.

> **Stacks 0F4X.** The condition that a section of the small-étale direct image of `F` over an
> étale test object `V ⟶ Y` has proper support over `V`: its support in `X ×_Y V` is proper over
> `V`.

```lean
public def properSupportSections (V : SmallEtale B Y.obj Y.property)
    (s : F.obj.obj (op ((smallEtaleBaseChange B f).obj V))) : Prop
```

**`AlgebraicGeometry.SmallEtale.properSupportSections_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean#L211). The attribute's comment: “stability under restriction”.

> **Stacks 0F4X.** The proper-support condition is stable under restriction along an arrow of
> the small étale site of `Y`.

```lean
public theorem properSupportSections_restrict [LocallyOfFiniteType (B.inclusion.map f)]
    (U V : SmallEtale B Y.obj Y.property) (a : V ⟶ U)
    (s : F.obj.obj (op ((smallEtaleBaseChange B f).obj U)))
    (hs : properSupportSections B f F U s) :
    properSupportSections B f F V (F.obj.map ((smallEtaleBaseChange B f).map a).op s)
```

**`AlgebraicGeometry.SmallEtale.properSupportSections_descend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean#L251). The attribute's comment: “locality of the proper support condition”.

> **Stacks 0F4X.** The proper-support condition is local for the fpqc topology on the test
> object.

```lean
public theorem properSupportSections_descend [LocallyOfFiniteType (B.inclusion.map f)]
    (V : SmallEtale B Y.obj Y.property)
    (s : F.obj.obj (op ((smallEtaleBaseChange B f).obj V)))
    {ι : Type w} (W : ι → SmallEtale B Y.obj Y.property) (a : ∀ i, W i ⟶ V)
    (hcover : Presieve.ofArrows
      (fun i => (SmallEtale.toScheme B Y.obj Y.property).obj (W i))
      (fun i => (SmallEtale.toScheme B Y.obj Y.property).map (a i)) ∈
        Scheme.fpqcPrecoverage ((SmallEtale.toScheme B Y.obj Y.property).obj V))
    (hloc : ∀ i, properSupportSections B f F (W i)
      (F.obj.map ((smallEtaleBaseChange B f).map (a i)).op s)) :
    properSupportSections B f F V s
```

**`AlgebraicGeometry.SmallEtale.fShriekSubsheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean#L477). References: SGA 4 XVII (6.3.16), “f\_! as subsheaf of f\_*”; SGA 4 XVII (6.1.2), “abelian sheaves”.

> **Stacks 0F4X.** The abelian subsheaf `f_! F` of the small-étale direct image `f_* F`
> consisting exactly of the sections whose support is proper over the étale base, bundled with the
> sectionwise description of its image.

```lean
public def fShriekSubsheaf [LocallyOfFiniteType (B.inclusion.map f)] :
    {G : MonoOver ((smallEtaleBaseChange B f).sheafPushforwardContinuous
        AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
          (SmallEtale.topology B X.obj X.property) |>.obj F) //
      ∀ (V : SmallEtale B Y.obj Y.property)
        (s : ((smallEtaleBaseChange B f).sheafPushforwardContinuous
          AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
            (SmallEtale.topology B X.obj X.property)).obj F |>.obj.obj (op V)),
          s ∈ Set.range (G.arrow.hom.app (op V)) ↔
            properSupportSections B f F V s}
```

**`AlgebraicGeometry.SmallEtale.mem_range_fShriekSubsheaf_arrow_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean#L511). The attribute's comment: “the sectionwise characterization”.

> **Stacks 0F4X.** The sections of `f_! F` over an étale test object are exactly the sections
> of `f_* F` whose support is proper over that object.

```lean
public theorem mem_range_fShriekSubsheaf_arrow_iff [LocallyOfFiniteType (B.inclusion.map f)]
    (V : SmallEtale B Y.obj Y.property)
    (s : (directImageSheaf B f F).obj.obj (op V)) :
    s ∈ Set.range ((fShriekSubsheaf B f F).val.arrow.hom.app (op V)) ↔
      properSupportSections B f F V s
```

## Tag 0F4Y, a lemma

[Tag 0F4Y](https://stacks.math.columbia.edu/tag/0F4Y) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.abelianExtensionByZeroToPushforward_range_eq_fShriekSubsheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekExtensionByZero.lean, line 945](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekExtensionByZero.lean#L945).

> **Stacks 0F4Y.** For a separated étale morphism, the image of extension by zero in the
> direct image is precisely the proper-support subsheaf.

```lean
public theorem abelianExtensionByZeroToPushforward_range_eq_fShriekSubsheaf
    (B : BigEtaleSite.{u}) (X : Scheme.{u}) (hX : B.Contains X) (U : SmallEtale B X hX)
    [IsSeparated (B.inclusion.map U.obj.hom)]
    (F : Sheaf (SmallEtale.topology B U.obj.left.1 U.obj.left.property) AddCommGrpCat.{u + 1})
    (V : SmallEtale B X hX) :
    Set.range (((abelianExtensionByZeroToPushforward B X hX U).app F).hom.app (op V)) =
      Set.range (((fShriekSubsheaf B U.obj.hom F).val.arrow).hom.app (op V))
```

## Tag 0F4Z, a definition

[Tag 0F4Z](https://stacks.math.columbia.edu/tag/0F4Z) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekSubsheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekSubsheaf.lean#L477). The attribute's comment: “the subsheaf f\_! F of f\_* F, the direct image with compact support”. References: SGA 4 XVII (6.3.16), “f\_! as subsheaf of f\_*”; SGA 4 XVII (6.1.2), “abelian sheaves”.

> **Stacks 0F4X.** The abelian subsheaf `f_! F` of the small-étale direct image `f_* F`
> consisting exactly of the sections whose support is proper over the étale base, bundled with the
> sectionwise description of its image.

```lean
public def fShriekSubsheaf [LocallyOfFiniteType (B.inclusion.map f)] :
    {G : MonoOver ((smallEtaleBaseChange B f).sheafPushforwardContinuous
        AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
          (SmallEtale.topology B X.obj X.property) |>.obj F) //
      ∀ (V : SmallEtale B Y.obj Y.property)
        (s : ((smallEtaleBaseChange B f).sheafPushforwardContinuous
          AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
            (SmallEtale.topology B X.obj X.property)).obj F |>.obj.obj (op V)),
          s ∈ Set.range (G.arrow.hom.app (op V)) ↔
            properSupportSections B f F V s}
```

## Tag 0F51, a lemma

[Tag 0F51](https://stacks.math.columbia.edu/tag/0F51) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportIsoPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L185). The attribute's comment: “natural isomorphism f\_! ≅ f\_* for proper f”.

> For a proper morphism the proper-support direct image is the ordinary
> direct image, naturally in the abelian étale sheaf.

```lean
public def properSupportIsoPushforward [IsProper (B.inclusion.map g)] :
    properSupportFunctor.{u, v} B g ≅ etalePushforward.{u, v} B g
```

**`AlgebraicGeometry.SmallEtale.fShriekSubsheaf_arrow_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekProper.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekProper.lean#L76).

> **Stacks 0F51.** For a proper morphism, the canonical inclusion of the proper-support
> direct image `f_! F` into the ordinary direct image `f_* F` is an isomorphism.

```lean
public theorem fShriekSubsheaf_arrow_isIso [IsProper (B.inclusion.map f)] :
    IsIso ((fShriekSubsheaf B f F).val.arrow)
```

## Tag 0F53, a remark

[Tag 0F53](https://stacks.math.columbia.edu/tag/0F53) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean#L65). The attribute's comment: “open\_inclusion\_compatibility: induced maps”.

> The induced map on proper-support direct images, characterized by its
> inclusion into ordinary direct image.

```lean
public noncomputable def fShriekMap
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F H : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (φ : F ⟶ H) :
    let G := (SmallEtale.fShriekSubsheaf B f F).val
    let K := (SmallEtale.fShriekSubsheaf B f H).val
    let push := (smallEtaleBaseChange B f).sheafPushforwardContinuous AddCommGrpCat.{v}
      (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B X.obj X.property)
    {m : G.obj.left ⟶ K.obj.left // m ≫ K.arrow = G.arrow ≫ push.map φ}
```

**`AlgebraicGeometry.SmallEtale.fShriekMap_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean#L219). The attribute's comment: “open\_inclusion\_compatibility: identity”.

> The proper-support direct image takes identity morphisms to identities.

```lean
public theorem fShriekMap_id
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    (fShriekMap B f F F (𝟙 F)).val = 𝟙 _
```

**`AlgebraicGeometry.SmallEtale.fShriekMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean#L236). The attribute's comment: “open\_inclusion\_compatibility: composition”.

> The proper-support direct image respects composition of sheaf morphisms.

```lean
public theorem fShriekMap_comp
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F H K : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (φ : F ⟶ H) (ψ : H ⟶ K) :
    (fShriekMap B f F K (φ ≫ ψ)).val =
      (fShriekMap B f F H φ).val ≫ (fShriekMap B f H K ψ).val
```

**`AlgebraicGeometry.SmallEtale.openInclusionShriekMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekFunctorial.lean#L647). The attribute's comment: “open\_inclusion\_compatibility”.

> Extension by zero from an open subscheme is natural in the abelian sheaf.

```lean
public theorem openInclusionShriekMap_naturality
    (B : BigEtaleSite.{u}) {X' X Y : B.Scheme}
    (j : X' ⟶ X) (f : X ⟶ Y)
    [IsOpenImmersion (B.inclusion.map j)]
    [IsSeparated (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F H : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (φ : F ⟶ H) :
    letI : LocallyOfFiniteType (B.inclusion.map (j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map j ≫ B.inclusion.map f)
      infer_instance
    let pull := (smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)
    (fShriekMap B (j ≫ f) (pull.obj F) (pull.obj H) (pull.map φ)).val ≫
      (openInclusionShriekMap B j f H).val =
        (openInclusionShriekMap B j f F).val ≫
        (fShriekMap B f F H φ).val
```

**`AlgebraicGeometry.SmallEtale.openInclusionShriekMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusion/ShriekMap.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusion/ShriekMap.lean#L524). The attribute's comment: “open\_inclusion\_mono”.

> The canonical injection from the proper-support direct image on an open
> subscheme, with its sectionwise extension-by-zero characterization.

```lean
public noncomputable def openInclusionShriekMap
    (B : BigEtaleSite.{u}) {X' X Y : B.Scheme}
    (j : X' ⟶ X) (f : X ⟶ Y)
    [IsOpenImmersion (B.inclusion.map j)]
    [IsSeparated (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    letI : LocallyOfFiniteType (B.inclusion.map (j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map j ≫ B.inclusion.map f)
      infer_instance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    let G' := (SmallEtale.fShriekSubsheaf B (j ≫ f) F').val
    let G := (SmallEtale.fShriekSubsheaf B f F).val
    {α : G'.obj.left ⟶ G.obj.left //
      Mono α ∧
      ∀ (V : SmallEtale B Y.obj Y.property) (a : G'.obj.left.obj.obj (op V)),
        let W := (smallEtaleBaseChange B f).obj V
        let e := (smallEtaleBaseChange_compIso B X' X Y j f).val
        let s := G.arrow.hom.app (op V) (α.hom.app (op V) a)
        let s' := G'.arrow.hom.app (op V) a
        let s'W := F'.obj.map (e.hom.app V).op s'
        (F'.obj.map (e.hom.app V).op s' =
          (((smallEtaleBaseChange B j).sheafAdjunctionContinuous AddCommGrpCat.{v}
            (SmallEtale.topology B X.obj X.property)
            (SmallEtale.topology B X'.obj X'.property)).unit.app F).hom.app (op W) s) ∧
        (SmallEtale.supportSection B X.obj X.property F W s =
          (B.inclusion.map (pullback.fst W.obj.hom j)).base ''
            SmallEtale.supportSection B X'.obj X'.property F'
              ((smallEtaleBaseChange B j).obj W) s'W)}
```

**`AlgebraicGeometry.SmallEtale.openInclusionShriekCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusionComp.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusionComp.lean#L383). The attribute's comment: “open\_inclusion\_trans”.

> **Stacks 0F53.** Restricting an abelian sheaf to a nested open subscheme in two steps or in
> one gives canonically isomorphic proper-support direct images.

```lean
public noncomputable def openInclusionShriekCompIso
    (B : BigEtaleSite.{u}) {X'' X' X Y : B.Scheme}
    (i : X'' ⟶ X') (j : X' ⟶ X) (f : X ⟶ Y)
    [IsOpenImmersion (B.inclusion.map i)]
    [IsOpenImmersion (B.inclusion.map j)]
    [IsSeparated (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    letI : IsOpenImmersion (B.inclusion.map (i ≫ j)) := by
      change IsOpenImmersion (B.inclusion.map i ≫ B.inclusion.map j)
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map j ≫ B.inclusion.map f)
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (i ≫ j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map i ≫ B.inclusion.map (j ≫ f))
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map ((i ≫ j) ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map (i ≫ j) ≫ B.inclusion.map f)
      infer_instance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    let F'' := ((smallEtaleBaseChange B i).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X'.obj X'.property)
      (SmallEtale.topology B X''.obj X''.property)).obj F'
    let Fd := ((smallEtaleBaseChange B (i ≫ j)).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X''.obj X''.property)).obj F
    (fShriekSubsheaf B (i ≫ j ≫ f) F'').val.obj.left ≅
      (fShriekSubsheaf B ((i ≫ j) ≫ f) Fd).val.obj.left
```

**`AlgebraicGeometry.SmallEtale.openInclusionShriekCompIso_ambient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusionComp.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusionComp.lean#L419). The attribute's comment: “open\_inclusion\_trans”.

> **Stacks 0F53.** The comparison of proper-support direct images is the comparison of
> restrictions, read inside the ordinary direct images.

```lean
public theorem openInclusionShriekCompIso_ambient
    (B : BigEtaleSite.{u}) {X'' X' X Y : B.Scheme}
    (i : X'' ⟶ X') (j : X' ⟶ X) (f : X ⟶ Y)
    [IsOpenImmersion (B.inclusion.map i)]
    [IsOpenImmersion (B.inclusion.map j)]
    [IsSeparated (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    letI : IsOpenImmersion (B.inclusion.map (i ≫ j)) := by
      change IsOpenImmersion (B.inclusion.map i ≫ B.inclusion.map j)
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map j ≫ B.inclusion.map f)
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (i ≫ j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map i ≫ B.inclusion.map (j ≫ f))
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map ((i ≫ j) ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map (i ≫ j) ≫ B.inclusion.map f)
      infer_instance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    let F'' := ((smallEtaleBaseChange B i).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X'.obj X'.property)
      (SmallEtale.topology B X''.obj X''.property)).obj F'
    let Fd := ((smallEtaleBaseChange B (i ≫ j)).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X''.obj X''.property)).obj F
    let Pi := (smallEtaleBaseChange B (i ≫ j ≫ f)).sheafPushforwardContinuous
      AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B X''.obj X''.property)
    let Pd := (smallEtaleBaseChange B ((i ≫ j) ≫ f)).sheafPushforwardContinuous
      AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B X''.obj X''.property)
    let restrictionIso := (smallEtaleSheafPullbackCompIso B X'' X' X i j
      AddCommGrpCat.{v}).app F
    let pushforwardIso : Pi ≅ Pd :=
      eqToIso (congrArg (fun g : X'' ⟶ Y =>
        (smallEtaleBaseChange B g).sheafPushforwardContinuous
          AddCommGrpCat.{v} (SmallEtale.topology B Y.obj Y.property)
          (SmallEtale.topology B X''.obj X''.property))
        (Category.assoc i j f).symm)
    (openInclusionShriekCompIso B i j f F).hom ≫
        (fShriekSubsheaf B ((i ≫ j) ≫ f) Fd).val.arrow =
      (fShriekSubsheaf B (i ≫ j ≫ f) F'').val.arrow ≫
        (Pi.mapIso restrictionIso ≪≫ pushforwardIso.app Fd).hom
```

**`AlgebraicGeometry.SmallEtale.openInclusionShriekMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusionComp.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenInclusionComp.lean#L478). The attribute's comment: “open\_inclusion\_trans”.

> **Stacks 0F53.** Extension by zero is transitive: for nested open subschemes
> `X'' ⟶ X' ⟶ X` of the source of a separated morphism locally of finite type, the canonical map
> from the proper-support direct image on `X''` is the composite of the two successive canonical
> maps, once the two proper-support direct images on `X''` are identified.

```lean
public theorem openInclusionShriekMap_comp
    (B : BigEtaleSite.{u}) {X'' X' X Y : B.Scheme}
    (i : X'' ⟶ X') (j : X' ⟶ X) (f : X ⟶ Y)
    [IsOpenImmersion (B.inclusion.map i)]
    [IsOpenImmersion (B.inclusion.map j)]
    [IsSeparated (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map f)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    letI : IsOpenImmersion (B.inclusion.map (i ≫ j)) := by
      change IsOpenImmersion (B.inclusion.map i ≫ B.inclusion.map j)
      infer_instance
    letI : IsSeparated (B.inclusion.map (j ≫ f)) := by
      change IsSeparated (B.inclusion.map j ≫ B.inclusion.map f)
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map j ≫ B.inclusion.map f)
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (i ≫ j ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map i ≫ B.inclusion.map (j ≫ f))
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map ((i ≫ j) ≫ f)) := by
      change LocallyOfFiniteType (B.inclusion.map (i ≫ j) ≫ B.inclusion.map f)
      infer_instance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    (openInclusionShriekCompIso B i j f F).hom ≫
        (openInclusionShriekMap B (i ≫ j) f F).val =
      (openInclusionShriekMap B i (j ≫ f) F').val ≫
        (openInclusionShriekMap B j f F).val
```

## Tag 0F52, a lemma

[Tag 0F52](https://stacks.math.columbia.edu/tag/0F52) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.compactificationProperSupportIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L224). The attribute's comment: “natural isomorphism of proper-support functors”.

> The canonical comparison `f_! ⟶ f̄_! ∘ j_!` of proper-support direct
> images through a compactification `j : X ⟶ X̄` of `X` over `Y`, as a natural isomorphism of
> functors on abelian étale sheaves.

```lean
public def compactificationProperSupportIso
    [LocallyOfFiniteType (B.inclusion.map U.obj.hom)] :
    properSupportFunctor.{u, u + 1} B (U.obj.hom ≫ fbar) ≅
      abelianExtensionByZero B Xbar.obj Xbar.property U ⋙
        properSupportFunctor.{u, u + 1} B fbar
```

**`AlgebraicGeometry.SmallEtale.fShriekFunctorIsoCompactification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/DerivedLowerShriekQuasiFinite.lean#L243). The attribute's comment: “f\_! = f̄\_* ∘ j\_!”.

> `f_! = f̄_* ∘ j_!`: the direct image with compact support along
> `f = j ≫ f̄`, for `j : X ⟶ X̄` an open immersion and `f̄ : X̄ ⟶ Y` proper, is extension by zero
> along `j` followed by the ordinary direct image along `f̄`.

```lean
public def fShriekFunctorIsoCompactification
    [LocallyQuasiFinite (B.inclusion.map fbar)] :
    fShriekFunctor.{u, u} B (U.obj.hom ≫ fbar) ≅
      abelianExtensionByZero B Xbar.obj Xbar.property U ⋙
        etalePushforward.{u, u + 1} B fbar
```

**`AlgebraicGeometry.SmallEtale.compactificationFShriekMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean#L322). The attribute's comment: “canonical comparison”.

> **Stacks 0F52.** The canonical map `f_! F ⟶ f̄_!(j_! F)` for an open immersion `j : X ⟶ X̄`
> with `f = j ≫ f̄`: the extension-by-zero unit, which identifies `F` with the restriction of
> `j_! F`, followed by the open-inclusion comparison of Stacks 0F53. The subtype records that
> factorisation, which is what pins the map down.

```lean
public noncomputable def compactificationFShriekMap :
    letI : IsSeparated (B.inclusion.map fbar) := inferInstance
    letI : LocallyOfFiniteType (B.inclusion.map fbar) := inferInstance
    letI : LocallyOfFiniteType (B.inclusion.map (U.obj.hom ≫ fbar)) := by
      change LocallyOfFiniteType (B.inclusion.map U.obj.hom ≫ B.inclusion.map fbar)
      infer_instance
    let Fbar := (abelianExtensionByZero B Xbar.obj Xbar.property U).obj F
    let pull := (smallEtaleBaseChange B U.obj.hom).sheafPullback AddCommGrpCat.{u + 1}
      (SmallEtale.topology B Xbar.obj Xbar.property)
      (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
    let push := (smallEtaleBaseChange B (U.obj.hom ≫ fbar)).sheafPushforwardContinuous
      AddCommGrpCat.{u + 1} (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
    let Gsrc := (fShriekSubsheaf B (U.obj.hom ≫ fbar) F).val
    let Gpull := (fShriekSubsheaf B (U.obj.hom ≫ fbar) (pull.obj Fbar)).val
    let Gtgt := (fShriekSubsheaf B fbar Fbar).val
    {α : Gsrc.obj.left ⟶ Gtgt.obj.left //
      ∃ i : Gsrc.obj.left ≅ Gpull.obj.left,
        let unit := (abelianExtensionByZeroAdjunction B Xbar.obj Xbar.property U).unit.app F
        let e := unit ≫ (openRestrictionIso.{u, u} B U.obj.hom).hom.app Fbar
        (i.hom ≫ Gpull.arrow = Gsrc.arrow ≫ push.map e) ∧
        (α = i.hom ≫ (openInclusionShriekMap B U.obj.hom fbar Fbar).val)}
```

**`AlgebraicGeometry.SmallEtale.compactificationFShriekMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean#L521). The attribute's comment: “isomorphism”.

> **Stacks 0F52.** The canonical compactification comparison is an isomorphism.

```lean
public theorem compactificationFShriekMap_isIso :
    IsIso (compactificationFShriekMap B fbar U F).val
```

**`AlgebraicGeometry.SmallEtale.compactificationFShriekMap_to_pushforward_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean#L581). The attribute's comment: “ordinary direct image”.

> **Stacks 0F52.** Since the compactification is proper, the same canonical map identifies
> `f_! F` with the ordinary direct image `f̄_*(j_! F)`.

```lean
public theorem compactificationFShriekMap_to_pushforward_isIso :
    letI : LocallyOfFiniteType (B.inclusion.map fbar) := inferInstance
    let Fbar := (abelianExtensionByZero B Xbar.obj Xbar.property U).obj F
    IsIso ((compactificationFShriekMap B fbar U F).val ≫
      (fShriekSubsheaf B fbar Fbar).val.arrow)
```

**`AlgebraicGeometry.SmallEtale.compactificationFShriekMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean, line 597](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactification.lean#L597). The attribute's comment: “naturality and functor comparison”.

> **Stacks 0F52.** The compactification comparison commutes with morphisms of abelian étale
> sheaves, hence identifies the two direct-image functors naturally.

```lean
public theorem compactificationFShriekMap_naturality
    (H : Sheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property) AddCommGrpCat.{u + 1})
    (phi : F ⟶ H) :
    letI : IsSeparated (B.inclusion.map fbar) := inferInstance
    letI : LocallyOfFiniteType (B.inclusion.map fbar) := inferInstance
    letI : LocallyOfFiniteType (B.inclusion.map (U.obj.hom ≫ fbar)) := by
      change LocallyOfFiniteType (B.inclusion.map U.obj.hom ≫ B.inclusion.map fbar)
      infer_instance
    let ext := abelianExtensionByZero B Xbar.obj Xbar.property U
    let push := (smallEtaleBaseChange B (U.obj.hom ≫ fbar)).sheafPushforwardContinuous
      AddCommGrpCat.{u + 1} (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
    let pushbar := (smallEtaleBaseChange B fbar).sheafPushforwardContinuous
      AddCommGrpCat.{u + 1} (SmallEtale.topology B Y.obj Y.property)
      (SmallEtale.topology B Xbar.obj Xbar.property)
    let GF := (fShriekSubsheaf B (U.obj.hom ≫ fbar) F).val
    let GH := (fShriekSubsheaf B (U.obj.hom ≫ fbar) H).val
    let GbarF := (fShriekSubsheaf B fbar (ext.obj F)).val
    let GbarH := (fShriekSubsheaf B fbar (ext.obj H)).val
    ∀ (a : GF.obj.left ⟶ GH.obj.left) (b : GbarF.obj.left ⟶ GbarH.obj.left),
      (a ≫ GH.arrow = GF.arrow ≫ push.map phi) →
      (b ≫ GbarH.arrow = GbarF.arrow ≫ pushbar.map (ext.map phi)) →
      (a ≫ (compactificationFShriekMap B fbar U H).val =
        (compactificationFShriekMap B fbar U F).val ≫ b)
```

## Tag 0F72, a definition

[Tag 0F72](https://stacks.math.columbia.edu/tag/0F72) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupport.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupport.lean#L62).

> **Stacks 0F72.** The subgroup of global sections of an abelian sheaf on the small étale
> site whose support is proper over the base field.

```lean
public def compactlySupportedSections :
    AddSubgroup (F.obj.obj (op (SmallEtale.final B X hX)))
```

## Tag 0F73, a lemma

[Tag 0F73](https://stacks.math.columbia.edu/tag/0F73) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections_eq_top_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekProper.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekProper.lean#L101).

> **Stacks 0F73.** On a scheme proper over a field, every global section of an abelian sheaf
> on the small étale site has compact support.

```lean
public theorem compactlySupportedSections_eq_top_of_isProper :
    compactlySupportedSections k X f B hX F = ⊤
```

## Tag 0F74, a remark

[Tag 0F74](https://stacks.math.columbia.edu/tag/0F74) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections_openInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean, line 474](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean#L474). The attribute's comment: “canonical injection”.

> **Stacks 0F74.** Extension by zero gives a canonical injection on compactly supported
> sections along an open immersion, characterised by the restriction of its value back to the
> open subscheme and by the equality of supports.

```lean
public noncomputable def compactlySupportedSections_openInclusion {X' X : B.Scheme}
    (j : X' ⟶ X) (f : X.obj ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f]
    [IsOpenImmersion (B.inclusion.map j)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    letI : LocallyOfFiniteType (B.inclusion.map j ≫ f) := inferInstance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    {φ : compactlySupportedSections k X'.obj (B.inclusion.map j ≫ f) B X'.property F' →+
        compactlySupportedSections k X.obj f B X.property F //
      Function.Injective φ ∧
      ∀ s, (F'.obj.map ((SmallEtale.finalIsTerminal B X'.obj X'.property).from
            ((smallEtaleBaseChange B j).obj (SmallEtale.final B X.obj X.property))).op s.1 =
          (((smallEtaleBaseChange B j).sheafAdjunctionContinuous AddCommGrpCat.{v}
            (SmallEtale.topology B X.obj X.property)
            (SmallEtale.topology B X'.obj X'.property)).unit.app F).hom.app
              (op (SmallEtale.final B X.obj X.property)) (φ s).1) ∧
        (supportSection B X.obj X.property F (SmallEtale.final B X.obj X.property) (φ s).1 =
          (B.inclusion.map j).base ''
            supportSection B X'.obj X'.property F'
              (SmallEtale.final B X'.obj X'.property) s.1)}
```

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections_openInclusion_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean#L508). The attribute's comment: “precosheaf identity”.

> **Stacks 0F74.** For the identity open immersion extension by zero is surjective on
> compactly supported sections, hence an isomorphism: the unit of the restriction adjunction
> along an identity is an isomorphism, and the characterising restriction equation identifies the
> injection with it.

```lean
public theorem compactlySupportedSections_openInclusion_id (X : B.Scheme)
    (f : X.obj ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    Function.Surjective (compactlySupportedSections_openInclusion k B (𝟙 X) f F).1
```

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections_openInclusion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean, line 632](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean#L632). The attribute's comment: “precosheaf composition”.

> **Stacks 0F74.** Extension by zero on compactly supported sections is transitive for
> composable open immersions, once the two restrictions of the sheaf to the smallest open
> subscheme are identified by the canonical comparison of inverse images.

```lean
public theorem compactlySupportedSections_openInclusion_comp {X'' X' X : B.Scheme}
    (i : X'' ⟶ X') (j : X' ⟶ X) (f : X.obj ⟶ Spec (.of k))
    [IsSeparated f] [LocallyOfFiniteType f]
    [IsOpenImmersion (B.inclusion.map i)] [IsOpenImmersion (B.inclusion.map j)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v}) :
    letI : IsOpenImmersion (B.inclusion.map (i ≫ j)) := by
      change IsOpenImmersion (B.inclusion.map i ≫ B.inclusion.map j)
      infer_instance
    letI : IsSeparated (B.inclusion.map j ≫ f) := by infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map j ≫ f) := by infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map i ≫ (B.inclusion.map j ≫ f)) := by
      infer_instance
    letI : LocallyOfFiniteType (B.inclusion.map (i ≫ j) ≫ f) := by
      change LocallyOfFiniteType (B.inclusion.map i ≫ B.inclusion.map j ≫ f)
      infer_instance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    let F'' := ((smallEtaleBaseChange B i).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X'.obj X'.property)
      (SmallEtale.topology B X''.obj X''.property)).obj F'
    let Fd := ((smallEtaleBaseChange B (i ≫ j)).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X''.obj X''.property)).obj F
    ∀ (s : compactlySupportedSections k X''.obj (B.inclusion.map i ≫ (B.inclusion.map j ≫ f))
        B X''.property F''),
      ∃ (t : compactlySupportedSections k X''.obj (B.inclusion.map (i ≫ j) ≫ f) B X''.property
        Fd),
        (((smallEtaleSheafPullbackCompIso B X'' X' X i j AddCommGrpCat.{v}).app F).hom.hom.app
            (op (SmallEtale.final B X''.obj X''.property)) s.1 = t.1) ∧
        ((compactlySupportedSections_openInclusion k B j f F).1
          ((compactlySupportedSections_openInclusion k B i (B.inclusion.map j ≫ f) F').1 s) =
          (compactlySupportedSections_openInclusion k B (i ≫ j) f F).1 t)
```

**`AlgebraicGeometry.SmallEtale.exists_compactlySupportedSections_openInclusion_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean, line 906](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean#L906). The attribute's comment: “cosheaf, image of the canonical injection”.

> **Stacks 0F74.** A compactly supported section of `F` is the extension by zero of a
> compactly supported section on an open subscheme exactly when its support lies in that open
> subscheme: this identifies the image of the canonical injection.

```lean
public theorem exists_compactlySupportedSections_openInclusion_eq {X' X : B.Scheme}
    (j : X' ⟶ X) (f : X.obj ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f]
    [IsOpenImmersion (B.inclusion.map j)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (t : compactlySupportedSections k X.obj f B X.property F) :
    letI : LocallyOfFiniteType (B.inclusion.map j ≫ f) := inferInstance
    let F' := ((smallEtaleBaseChange B j).sheafPullback AddCommGrpCat.{v}
      (SmallEtale.topology B X.obj X.property)
      (SmallEtale.topology B X'.obj X'.property)).obj F
    (∃ s : compactlySupportedSections k X'.obj (B.inclusion.map j ≫ f) B X'.property F',
        (compactlySupportedSections_openInclusion k B j f F).1 s = t) ↔
      supportSection B X.obj X.property F (SmallEtale.final B X.obj X.property) t.1 ⊆
        Set.range (B.inclusion.map j).base
```

**`AlgebraicGeometry.SmallEtale.exists_compactlySupportedSections_openInclusion_inter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean, line 987](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean#L987). The attribute's comment: “cosheaf, Mayer–Vietoris”.

> **Stacks 0F74.** Mayer–Vietoris for compactly supported sections: two compactly supported
> sections on open subschemes with the same extension by zero both come from a compactly
> supported section on the intersection of the two open subschemes, an open subscheme `X₀` whose
> image is the intersection of the two images — for instance their fibre product, by
> `AlgebraicGeometry.SmallEtale.range_pullback_fst_comp`.

```lean
public theorem exists_compactlySupportedSections_openInclusion_inter {X₀ X₁ X₂ X : B.Scheme}
    (j₀ : X₀ ⟶ X) (j₁ : X₁ ⟶ X) (j₂ : X₂ ⟶ X) (f : X.obj ⟶ Spec (.of k))
    [IsSeparated f] [LocallyOfFiniteType f] [IsOpenImmersion (B.inclusion.map j₀)]
    [IsOpenImmersion (B.inclusion.map j₁)] [IsOpenImmersion (B.inclusion.map j₂)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (h₀ : Set.range (B.inclusion.map j₀).base =
      Set.range (B.inclusion.map j₁).base ∩ Set.range (B.inclusion.map j₂).base) :
    ∀ (s₁ : compactlySupportedSections k X₁.obj (B.inclusion.map j₁ ≫ f) B X₁.property
        (((smallEtaleBaseChange B j₁).sheafPullback AddCommGrpCat.{v}
          (SmallEtale.topology B X.obj X.property)
          (SmallEtale.topology B X₁.obj X₁.property)).obj F))
      (s₂ : compactlySupportedSections k X₂.obj (B.inclusion.map j₂ ≫ f) B X₂.property
        (((smallEtaleBaseChange B j₂).sheafPullback AddCommGrpCat.{v}
          (SmallEtale.topology B X.obj X.property)
          (SmallEtale.topology B X₂.obj X₂.property)).obj F)),
      (compactlySupportedSections_openInclusion k B j₁ f F).1 s₁ =
          (compactlySupportedSections_openInclusion k B j₂ f F).1 s₂ →
        ∃ s₀ : compactlySupportedSections k X₀.obj (B.inclusion.map j₀ ≫ f) B X₀.property
            (((smallEtaleBaseChange B j₀).sheafPullback AddCommGrpCat.{v}
              (SmallEtale.topology B X.obj X.property)
              (SmallEtale.topology B X₀.obj X₀.property)).obj F),
          (compactlySupportedSections_openInclusion k B j₀ f F).1 s₀ =
            (compactlySupportedSections_openInclusion k B j₁ f F).1 s₁
```

**`AlgebraicGeometry.SmallEtale.exists_compactlySupportedSections_openInclusion_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean, line 1116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpen.lean#L1116). The attribute's comment: “cosheaf, gluing”.

> **Stacks 0F74.** Gluing for compactly supported sections: a compactly supported section
> whose support is the union of two disjoint closed subsets, one inside each of two open
> subschemes, is the sum of the extensions by zero of compactly supported sections on those two
> open subschemes.

```lean
public theorem exists_compactlySupportedSections_openInclusion_add {X₁ X₂ X : B.Scheme}
    (j₁ : X₁ ⟶ X) (j₂ : X₂ ⟶ X) (f : X.obj ⟶ Spec (.of k))
    [IsSeparated f] [LocallyOfFiniteType f]
    [IsOpenImmersion (B.inclusion.map j₁)] [IsOpenImmersion (B.inclusion.map j₂)]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v})
    (t : compactlySupportedSections k X.obj f B X.property F)
    (Z₁ Z₂ : Set ((SmallEtale.toScheme B X.obj X.property).obj
      (SmallEtale.final B X.obj X.property)))
    (hZ₁ : IsClosed Z₁) (hZ₂ : IsClosed Z₂) (hdisj : Disjoint Z₁ Z₂)
    (hsupp : supportSection B X.obj X.property F (SmallEtale.final B X.obj X.property) t.1 =
      Z₁ ∪ Z₂)
    (h₁ : Z₁ ⊆ Set.range (B.inclusion.map j₁).base)
    (h₂ : Z₂ ⊆ Set.range (B.inclusion.map j₂).base) :
    ∃ (s₁ : compactlySupportedSections k X₁.obj (B.inclusion.map j₁ ≫ f) B X₁.property
        (((smallEtaleBaseChange B j₁).sheafPullback AddCommGrpCat.{v}
          (SmallEtale.topology B X.obj X.property)
          (SmallEtale.topology B X₁.obj X₁.property)).obj F))
      (s₂ : compactlySupportedSections k X₂.obj (B.inclusion.map j₂ ≫ f) B X₂.property
        (((smallEtaleBaseChange B j₂).sheafPullback AddCommGrpCat.{v}
          (SmallEtale.topology B X.obj X.property)
          (SmallEtale.topology B X₂.obj X₂.property)).obj F)),
      (compactlySupportedSections_openInclusion k B j₁ f F).1 s₁ +
        (compactlySupportedSections_openInclusion k B j₂ f F).1 s₂ = t
```

**`AlgebraicGeometry.SmallEtale.exists_zariskiCovering_not_surjective_compactlySupportedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpenNotCosheaf.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportOpenNotCosheaf.lean#L178). The attribute's comment: “the cosheaf condition is false in the literal sense: a Zariski covering of ℙ¹\_k by two opens on which the sum map H^0\_c(U₁) ⊕ H^0\_c(U₂) → H^0\_c(ℙ¹\_k, 𝔾\_a) is not surjective”.

> **Stacks 0F74, the cosheaf condition fails for an actual Zariski covering.** For every field
> `k` and every big étale site containing the projective line `ℙ¹_k`, the scheme `ℙ¹_k`, separated
> and of finite type (indeed proper) over `k`, has a Zariski covering by two open subschemes — the
> complements of the zero and of the infinity section — and an abelian sheaf on its small étale
> site — the additive group `𝔾_a` — such that the sum of the extension-by-zero maps
> `H^0_c(U₁) ⊕ H^0_c(U₂) → H^0_c(ℙ¹_k)` is not surjective. So `H^0_c` is not a cosheaf on the
> Zariski site in the literal sense; it is a precosheaf with injective transition maps, see
> `AlgebraicGeometry.SmallEtale.compactlySupportedSections_openInclusion`.

```lean
public theorem exists_zariskiCovering_not_surjective_compactlySupportedSections
    (hP : B.Contains (Stacks.Chow.relativeProjectiveLine (Spec (.of k)))) :
    ∃ (X X₁ X₂ : B.Scheme) (j₁ : X₁ ⟶ X) (j₂ : X₂ ⟶ X) (f : X.obj ⟶ Spec (.of k))
      (_ : IsProper f) (_ : IsOpenImmersion (B.inclusion.map j₁))
      (_ : IsOpenImmersion (B.inclusion.map j₂)),
      Set.range (B.inclusion.map j₁).base ∪ Set.range (B.inclusion.map j₂).base = Set.univ ∧
      ∃ F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u},
        ¬ Function.Surjective
          ((compactlySupportedSections_openInclusion k B j₁ f F).1.coprod
            (compactlySupportedSections_openInclusion k B j₂ f F).1)
```

## Tag 0F75, a lemma

[Tag 0F75](https://stacks.math.columbia.edu/tag/0F75) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections_extensionByZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportCompactification.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportCompactification.lean#L373). The attribute's comment: “canonical isomorphism”.

> **Stacks 0F75.** For an open immersion `j : X ⟶ X̄` with `X̄` proper over a field `k`, the
> compactly supported global sections of an abelian sheaf `F` on the small étale site of `X` are
> canonically the compactly supported global sections of its extension by zero `j_! F` on `X̄`.

```lean
public noncomputable def compactlySupportedSections_extensionByZero :
    compactlySupportedSections k U.obj.left.obj (B.inclusion.map U.obj.hom ≫ fbar) B
        U.obj.left.property F ≃+
      compactlySupportedSections k Xbar.obj fbar B Xbar.property
        ((abelianExtensionByZero B Xbar.obj Xbar.property U).obj F)
```

**`AlgebraicGeometry.SmallEtale.compactlySupportedSections_extensionByZero_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportCompactification.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekCompactSupportCompactification.lean#L386). The attribute's comment: “restriction characterization”.

> **Stacks 0F75.** The canonical equivalence is determined by the fact that restriction of the
> extended section to the open subscheme is the original section, identified through the
> extension-by-zero adjunction unit.

```lean
public theorem compactlySupportedSections_extensionByZero_restrict
    (s : compactlySupportedSections k U.obj.left.obj (B.inclusion.map U.obj.hom ≫ fbar) B
      U.obj.left.property F) :
    ((abelianExtensionByZeroAdjunction B Xbar.obj Xbar.property U).unit.app F).hom.app
        (op (SmallEtale.final B U.obj.left.obj U.obj.left.property)) s.1 =
      ((abelianExtensionByZero B Xbar.obj Xbar.property U).obj F).obj.map
        ((SmallEtale.finalIsTerminal B Xbar.obj Xbar.property).from U).op
        (compactlySupportedSections_extensionByZero k B Xbar fbar U F s).1
```

## Tag 0F76, a lemma

[Tag 0F76](https://stacks.math.columbia.edu/tag/0F76) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.fShriekStalkEquivCompactSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekGeometricStalkIso.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekGeometricStalkIso.lean#L83).

> **Stacks 0F76.** Let `f : X ⟶ Y` be separated and locally of finite type, `F` an abelian
> sheaf on `X_étale` and `ȳ : Spec k ⟶ Y` a geometric point. There is a canonical isomorphism
> `(f_!F)_ȳ ≅ H⁰_c(X_ȳ, F|_{X_ȳ})` between the stalk at `ȳ` of the direct image with compact
> support (Stacks 0F4X) and the compactly supported sections (Stacks 0F72) of the inverse image of
> `F` on the geometric fibre `X_ȳ = X ×_Y Spec k` over `k`. It sends the germ of a section over an
> étale neighbourhood `(V, v̄)` to its pullback along `X_ȳ ⟶ X_V`
> (`AlgebraicGeometry.SmallEtale.fShriekStalkEquivCompactSections_apply_germ`).

```lean
def fShriekStalkEquivCompactSections :
    ↥(etaleStalk B Y.obj Y.property y (fShriekSubsheaf B f F).val.obj.left.obj) ≃+
      geometricFibreCompactSections B f y hy F
```

**`AlgebraicGeometry.SmallEtale.fShriekStalkEquivCompactSections_apply_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekGeometricStalkIso.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekGeometricStalkIso.lean#L104). The attribute's comment: “the isomorphism pulls a section on an étale neighbourhood back to the fibre”.

> **Stacks 0F76, the isomorphism on germs.** Let `(V, v̄)` be an étale neighbourhood of `ȳ`
> and `s` a section of `f_!F` over `V`, that is a section of `F` over `X_V` with support proper over
> `V`. Let `h : X_ȳ ⟶ X_ȳ ×_X X_V` be a morphism over `X_ȳ` whose composite to `V` is
> `X_ȳ ⟶ Spec k ⟶ V`. Then the isomorphism sends the germ of `s` at `ȳ` to the pullback of `s`
> along `h`. Such an `h` exists and is unique, `AlgebraicGeometry.SmallEtale.geometricFibreLift`;
> this is the canonical map `c_ȳ` of the source.

```lean
theorem fShriekStalkEquivCompactSections_apply_germ
    (N : (geometricPointFiber B Y.obj Y.property y).Elements)
    (s : (fShriekSubsheaf B f F).val.obj.left.obj.obj (op N.1))
    (h : final B (geometricFibreObj B f y hy).obj (geometricFibreObj B f y hy).property ⟶
      (smallEtaleBaseChange B (geometricFibreProj B f y hy)).obj
        ((smallEtaleBaseChange B f).obj N.1))
    (hh : (h.hom.left ≫ baseChangeObjProjection B (geometricFibreProj B f y hy)
        ((smallEtaleBaseChange B f).obj N.1)) ≫ pullback.fst N.1.obj.hom f =
      geometricFibreStruct B f y hy ≫ neighborhoodPointHom B y hy N) :
    (fShriekStalkEquivCompactSections B f F y hy
        (etaleGerm B Y.obj Y.property y _ N.1 N.2 s) : geometricFibreSections B f y hy F) =
      pullbackSectionAlongHom B (geometricFibreProj B f y hy) AddCommGrpCat.{max (u + 1) v} F
        ((smallEtaleBaseChange B f).obj N.1) _ h
        ((fShriekSubsheaf B f F).val.arrow.hom.app (op N.1) s)
```

## Tag 0F55, a lemma

[Tag 0F55](https://stacks.math.columbia.edu/tag/0F55) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekProperBaseChange.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekProperBaseChange.lean#L80).

> **Stacks 0F55.** For a cartesian square of a big étale site with horizontal morphisms
> `p : X' ⟶ X`, `g : Y' ⟶ Y` and vertical morphisms `f : X ⟶ Y` separated and locally of finite
> type and `f' : X' ⟶ Y'`, there is an isomorphism `g⁻¹f_!F ≅ f'_!(p⁻¹F)`, natural in the abelian
> sheaf `F` on the small étale site of `X`. Its component at `F` is the base-change map
> `AlgebraicGeometry.SmallEtale.properSupportBaseChange`, the restriction of the pullback map
> `g⁻¹f_*F ⟶ f'_*(p⁻¹F)` (`AlgebraicGeometry.SmallEtale.properSupportBaseChange_comp_arrow`), so
> the isomorphism is the identification `f'_!(p⁻¹F) = g⁻¹f_!F` of the source inside
> `f'_*(p⁻¹F)`. The hypotheses on `f'` are read off the square.

```lean
public def properSupportBaseChangeIso :
    letI := locallyOfFiniteType_of_isPullback B p f' f g sq
    properSupportFunctor B f ⋙ abPullback.{u, v} B g ≅
      abPullback.{u, v} B p ⋙ properSupportFunctor B f'
```

## Tag 0F50, a lemma

[Tag 0F50](https://stacks.math.columbia.edu/tag/0F50) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportFunctor_compIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekComposition.lean, line 1044](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekComposition.lean#L1044).

> The canonical comparison is natural in the abelian étale sheaf.

```lean
public noncomputable def properSupportFunctor_compIso
    [IsSeparated (B.inclusion.map f)] [IsSeparated (B.inclusion.map g)] :
    letI : LocallyOfFiniteType (B.inclusion.map (f ≫ g)) :=
      by rw [Functor.map_comp]; infer_instance
    { e : properSupportFunctor B f ⋙ properSupportFunctor B g ≅
          properSupportFunctor B (f ≫ g) //
      ∀ F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v},
        e.app F = (properSupportSheaf_compIso B f g F).val }
```

## Tag 0F77, a remark

[Tag 0F77](https://stacks.math.columbia.edu/tag/0F77) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportFunctor_compIso_assoc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekAssociativity.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekAssociativity.lean#L262). The attribute's comment: “composition\_coherence”.

> Canonical proper-support direct-image comparisons are associative.

```lean
public theorem properSupportFunctor_compIso_assoc
    (B : BigEtaleSite.{u}) {X Y Z T : B.Scheme}
    (f : X ⟶ Y) (g : Y ⟶ Z) (h : Z ⟶ T)
    [LocallyOfFiniteType (B.inclusion.map f)]
    [LocallyOfFiniteType (B.inclusion.map g)]
    [LocallyOfFiniteType (B.inclusion.map h)]
    [IsSeparated (B.inclusion.map f)]
    [IsSeparated (B.inclusion.map g)]
    [IsSeparated (B.inclusion.map h)] :
    letI := locallyOfFiniteType_map_comp B f g
    letI := locallyOfFiniteType_map_comp B g h
    letI := locallyOfFiniteType_map_comp B (f ≫ g) h
    letI := locallyOfFiniteType_map_comp B f (g ≫ h)
    letI := isSeparated_map_comp B f g
    letI := isSeparated_map_comp B g h
    let fBang := SmallEtale.properSupportFunctor.{u, v} B f
    let gBang := SmallEtale.properSupportFunctor.{u, v} B g
    let hBang := SmallEtale.properSupportFunctor.{u, v} B h
    (Functor.isoWhiskerRight
        (SmallEtale.properSupportFunctor_compIso.{u, v} B f g).val hBang ≪≫
      (SmallEtale.properSupportFunctor_compIso.{u, v} B (f ≫ g) h).val) =
    (Functor.associator fBang gBang hBang ≪≫
      Functor.isoWhiskerLeft fBang
        (SmallEtale.properSupportFunctor_compIso.{u, v} B g h).val ≪≫
      (SmallEtale.properSupportFunctor_compIso.{u, v} B f (g ≫ h)).val ≪≫
      eqToIso (by
        have heq : f ≫ (g ≫ h) = (f ≫ g) ≫ h := (Category.assoc f g h).symm
        cases heq
        rfl))
```

**`AlgebraicGeometry.SmallEtale.properSupportBaseChange_compIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperSupportBaseChangeComposition.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ProperSupportBaseChangeComposition.lean#L302). The attribute's comment: “part (2): compatibility of the base change maps of 0F55 with the composition isomorphisms of 0F50”.

> **Stacks, Remark 0F77, part (2).** Let
> ```
> X' --c--> X
> |f'       |f
> v         v
> Y' --b--> Y
> |g'       |g
> v         v
> Z' --a--> Z
> ```
> be two cartesian squares of a big étale site, with `f` and `g` separated and locally of finite
> type. Then the square
> ```
> a⁻¹ (g ∘ f)_! ------------------------------> (g' ∘ f')_! c⁻¹
>      |                                               |
> a⁻¹ g_! f_! ------> g'_! b⁻¹ f_! ------> g'_! f'_! c⁻¹
> ```
> of abelian sheaves on the small étale site of `Z'` commutes, where the horizontal arrows are the
> base change maps of Stacks 0F55 (`AlgebraicGeometry.SmallEtale.properSupportBaseChange`) for the
> rectangle, for the lower square at `f_! F`, and `g'_!` of that for the upper square, and the
> vertical arrows are the composition isomorphisms of Stacks 0F50
> (`AlgebraicGeometry.SmallEtale.properSupportFunctor_compIso`).

```lean
theorem properSupportBaseChange_compIso (sq₁ : IsPullback c f' f b)
    (sq₂ : IsPullback b g' g a)
    [LocallyOfFiniteType (B.inclusion.map f)] [LocallyOfFiniteType (B.inclusion.map g)]
    [IsSeparated (B.inclusion.map f)] [IsSeparated (B.inclusion.map g)]
    (F : AbelianSheaf.{u, v} B X) :
    letI : LocallyOfFiniteType (B.inclusion.map f') :=
      MorphismProperty.of_isPullback (sq₁.map B.inclusion) inferInstance
    letI : LocallyOfFiniteType (B.inclusion.map g') :=
      MorphismProperty.of_isPullback (sq₂.map B.inclusion) inferInstance
    letI : IsSeparated (B.inclusion.map f') :=
      MorphismProperty.of_isPullback (sq₁.map B.inclusion) inferInstance
    letI : IsSeparated (B.inclusion.map g') :=
      MorphismProperty.of_isPullback (sq₂.map B.inclusion) inferInstance
    letI := locallyOfFiniteType_map_comp B f g
    letI := locallyOfFiniteType_map_comp B f' g'
    properSupportBaseChange.{u, v} B c (f' ≫ g') (f ≫ g) a (sq₁.paste_vert sq₂) F ≫
        (properSupportFunctor_compIso B f' g').val.inv.app ((abPullback.{u, v} B c).obj F) =
      (abPullback.{u, v} B a).map ((properSupportFunctor_compIso B f g).val.inv.app F) ≫
        properSupportBaseChange.{u, v} B b g' g a sq₂ ((properSupportFunctor B f).obj F) ≫
        (properSupportFunctor B g').map (properSupportBaseChange.{u, v} B c f' f b sq₁ F)
```

## Tag 0F54, a lemma

[Tag 0F54](https://stacks.math.columbia.edu/tag/0F54) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportFunctor_isColimit_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCover.lean, line 1117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekOpenCover.lean#L1117).

> **Stacks 0F54.** Let `f : X ⟶ Y` be separated and locally of finite type, and let the
> `X_i = U i` form an open covering of `X` that is directed: any two members lie in a third.
> Writing `f_i` for the restriction of `f` to `X_i`, the proper-support direct image is the
> colimit `f_! F = colim_i f_{i,!}(F|_{X_i})` functorially in the abelian sheaf `F`, along the
> canonical extension-by-zero maps: there is a directed diagram of functors whose value at `i` is
> `F ↦ f_{i,!}(F|_{X_i})` and a colimit cocone on it, in the category of functors from abelian
> sheaves on `X` to abelian sheaves on `Y`, whose vertex is the functor `f_!` and whose legs are,
> at every sheaf `F`, the canonical maps `f_{i,!}(F|_{X_i}) ⟶ f_! F`.

```lean
public theorem properSupportFunctor_isColimit_openCover [IsDirected ι (· ≤ ·)]
    (hcover : ∀ x : X.obj, ∃ i, x ∈ Set.range (B.inclusion.map (j.app i)).base) :
    ∃ (D : ι ⥤ (Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{v} ⥤
        Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{v}))
      (c : Cocone D) (hpt : c.pt = properSupportFunctor B f),
      (∀ i,
        let ji : U.obj i ⟶ X := j.app i
        letI : IsOpenImmersion (B.inclusion.map ji) := hopen i
        letI : LocallyOfFiniteType (B.inclusion.map (ji ≫ f)) := by
          change LocallyOfFiniteType (B.inclusion.map ji ≫ B.inclusion.map f)
          infer_instance
        let res := (smallEtaleBaseChange B ji).sheafPullback AddCommGrpCat.{v}
          (SmallEtale.topology B X.obj X.property)
          (SmallEtale.topology B (U.obj i).obj (U.obj i).property)
        ∃ (hi : D.obj i = res ⋙ properSupportFunctor B (ji ≫ f)),
          ∀ F, (c.ι.app i ≫ eqToHom hpt).app F =
            (eqToHom hi).app F ≫ (openInclusionShriekMap B ji f F).val) ∧
        Nonempty (IsColimit c)
```

## Tag 0F56, a lemma

[Tag 0F56](https://stacks.math.columbia.edu/tag/0F56) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportFunctor_preservesColimitsOfShape_discrete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FShriekDirectSums.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FShriekDirectSums.lean#L445).

> **Stacks 0F56.** Let `f : X ⟶ Y` be a morphism of schemes which is separated and locally of
> finite type. Then the proper-support direct image `f_!` of abelian sheaves on the small étale
> sites commutes with direct sums: it preserves colimits indexed by any discrete category, so it
> carries a direct sum of an arbitrarily indexed family of abelian sheaves on the small étale
> site of `X` to the direct sum of their proper-support direct images.

```lean
public theorem properSupportFunctor_preservesColimitsOfShape_discrete
    (B : BigEtaleSite.{u}) {X Y : B.Scheme} (f : X ⟶ Y)
    [IsSeparated (B.inclusion.map f)] [LocallyOfFiniteType (B.inclusion.map f)]
    (ι : Type w) :
    PreservesColimitsOfShape (Discrete ι) (properSupportFunctor.{u, v} B f)
```

## Tag 0F57, a lemma

[Tag 0F57](https://stacks.math.columbia.edu/tag/0F57) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properSupportStalkFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperSupportStalk.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ProperSupportStalk.lean#L64). The attribute's comment: “part (1)”.

> **Stacks 0F57, part (1).** For a separated locally quasi-finite morphism `f : X ⟶ Y` and a
> geometric point `ȳ` of `Y`, the stalk at `ȳ` of the proper-support direct image `f_!F` is the
> direct sum of the stalks of `F` at the geometric points `x̄` of `X` with `f(x̄) = ȳ`,
> functorially in the abelian étale sheaf `F`.

```lean
public def properSupportStalkFunctorIso (s : GeometricPoint Y.obj) :
    properSupportFunctor.{u, max (u + 1) v} B f ⋙
        (geometricPointSitePoint B Y.obj Y.property s).sheafFiber
          (A := AddCommGrpCat.{max (u + 1) v}) ≅
      Adjunction.sigmaFamily (fun x : GeometricFiberPoint B f s =>
        (geometricPointSitePoint B X.obj X.property (x.toGeometricPoint B f s)).sheafFiber
          (A := AddCommGrpCat.{max (u + 1) v}))
```

**`AlgebraicGeometry.SmallEtale.properSupportFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperSupportStalk.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/ProperSupportStalk.lean#L77). The attribute's comment: “part (2)”. References: SGA 4 XVII (6.1.4), “more general”.

> **Stacks 0F57, part (2).** For a separated locally quasi-finite morphism the proper-support
> direct image `f_!` on abelian étale sheaves is an exact functor.

```lean
public theorem properSupportFunctor_exact :
    exactFunctor _ _ (properSupportFunctor.{u, max (u + 1) v} B f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.3, Tag 0F4W](https://stacks.math.columbia.edu/tag/0F4W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
