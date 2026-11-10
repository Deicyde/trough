---
declaration: section
origin: cited
lean: CategoryTheory.Functor.category, AlgebraicGeometry.BigFppfOver.presheafAdjunction, AlgebraicGeometry.BigFppfOver.presheafPushforwardObjObjIsoLimit, CategoryTheory.Functor.ranOpCompIso, CategoryTheory.Functor.homEquiv_comp_ranOpCompIso_hom_app, CategoryTheory.Functor.whiskeringLeft_obj_comp, CategoryTheory.CatFiberedInGroupoids.isIso_underlyingNatTrans_app, CategoryTheory.CatFiberedInGroupoids.pullbackIso
statement: formalized
proof: formalized
---

# 96.3 Presheaves

Section 96.3 of the Stacks Project, [Tag 06TI](https://stacks.math.columbia.edu/tag/06TI). 4 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06TJ, a definition

[Tag 06TJ](https://stacks.math.columbia.edu/tag/06TJ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.category#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch96.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch96.lean#L15) (StacksFrontier): “(1), (2) and PSh(X): presheaves on the underlying category of X, the functor category Xᵒᵖ ⥤ Type (morphisms are natural transformations)”. References: SGA 4 I (1.1.1).

## Tag 06TK, an equation

[Tag 06TK](https://stacks.math.columbia.edu/tag/06TK) in the Stacks Project.

**`AlgebraicGeometry.BigFppfOver.presheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean#L77). The attribute's comment: “presheaf pullback f^p, pushforward {}_pf, and the adjunction f^p ⊣ {}_pf”.

> **Stacks 06TK**, the pullback and pushforward of presheaves and their adjointness. For a
> 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big fppf category of `S`, the
> pullback `G^p : PSh(𝒴) ⥤ PSh(𝒳)` of presheaves of sets is precomposition with `G.op`, so that
> `G^p 𝒢 (x) = 𝒢 (G x)` by definition, and the pushforward `{}_pG : PSh(𝒳) ⥤ PSh(𝒴)` is the right
> Kan extension along `G.op`; `G^p` is left adjoint to `{}_pG`.

```lean
noncomputable def presheafAdjunction :
    (Functor.whiskeringLeft _ _ (Type max v w t)).obj (CatFiberedInGroupoids.homFunctor G).op ⊣
      (CatFiberedInGroupoids.homFunctor G).op.ran
```

**`AlgebraicGeometry.BigFppfOver.presheafPushforwardObjObjIsoLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AssociatedMorphismOfTopoi.lean#L87). The attribute's comment: “the formula ({}_pf F)(y) = lim_{f(x) -> y} F(x) for the pushforward”.

> **Stacks 06TK**, the formula `({}_pG ℱ)(y) = lim_{G(x) → y} ℱ(x)` for the pushforward of a
> presheaf of sets `ℱ` on `𝒳` along a 1-morphism `G : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over
> the big fppf category of `S`, at an object `y` of `𝒴`: the limit is indexed by the pairs of an
> object `x` of `𝒳` and a morphism `G(x) → y`.

```lean
noncomputable def presheafPushforwardObjObjIsoLimit (ℱ : 𝒳.val.objᵒᵖ ⥤ Type (max v w t))
    (y : 𝒴.val.obj) :
    ((CatFiberedInGroupoids.homFunctor G).op.ran.obj ℱ).obj (Opposite.op y) ≅
      Limits.limit (StructuredArrow.proj (Opposite.op y) (CatFiberedInGroupoids.homFunctor G).op ⋙
        ℱ)
```

## Tag 06TL, a lemma

[Tag 06TL](https://stacks.math.columbia.edu/tag/06TL) in the Stacks Project.

**`CategoryTheory.Functor.ranOpCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafComp.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafComp.lean#L188). The attribute's comment: “the canonical isomorphism of pushforwards”.

> **Stacks 06TL**: the canonical isomorphism `{}_p(g ∘ f) ≅ {}_pg ∘ {}_pf` of functors
> `PSh(𝒳) ⥤ PSh(𝒵)`, namely the comparison of the two right adjoints `{}_p(g ∘ f)` and
> `{}_pg ∘ {}_pf` of `(g ∘ f)^p = f^p ∘ g^p`.

```lean
noncomputable def ranOpCompIso : (f ⋙ g).op.ran (H := A) ≅ f.op.ran ⋙ g.op.ran
```

**`CategoryTheory.Functor.homEquiv_comp_ranOpCompIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafComp.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafComp.lean#L196). The attribute's comment: “compatibility of the canonical isomorphism with adjointness”.

> **Stacks 06TL**: the isomorphism `{}_p(g ∘ f) ≅ {}_pg ∘ {}_pf` is compatible with adjointness
> of `(f^p, {}_pf)`, `(g^p, {}_pg)` and `((g ∘ f)^p, {}_p(g ∘ f))`: the square of hom-set bijections
> `Mor(f^p g^p K, F) = Mor(g^p K, {}_pf F) = Mor(K, {}_pg {}_pf F)` and
> `Mor((g ∘ f)^p K, F) = Mor(K, {}_p(g ∘ f) F)` commutes.

```lean
theorem homEquiv_comp_ranOpCompIso_hom_app (K : Zᵒᵖ ⥤ A) (F : Xᵒᵖ ⥤ A)
    (α : (f ⋙ g).op ⋙ K ⟶ F) :
    ((f ⋙ g).op.ranAdjunction A).homEquiv K F α ≫ (ranOpCompIso A f g).hom.app F =
      (ranCompAdjunction A f.op g.op).homEquiv K F α
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.whiskeringLeft_obj_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.whiskeringLeft_obj_comp#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafComp.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/PresheafComp.lean#L208) (StacksFrontier): “pullback of presheaves along a composite: `(g ∘ f)^p = f^p ∘ g^p`, at `F = f.op`, `G = g.op`”.

## Tag 06TM, a lemma

[Tag 06TM](https://stacks.math.columbia.edu/tag/06TM) in the Stacks Project.

**`CategoryTheory.CatFiberedInGroupoids.isIso_underlyingNatTrans_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L109). The attribute's comment: “invertibility of the two-morphism”.

> **Stacks 06TM.** Every component of a two-morphism of categories fibred in groupoids lies
> over an identity, hence is invertible.

```lean
theorem isIso_underlyingNatTrans_app {f g : 𝒳 ⟶ 𝒴} (t : f ⟶ g) (x : 𝒳.based.obj) :
    IsIso (t.hom.toNatTrans.app x)
```

**`CategoryTheory.CatFiberedInGroupoids.pullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L145). The attribute's comment: “canonical isomorphism on restriction functors”.

> **Stacks 06TM.** Pullback of presheaves along the isomorphism of functors underlying a
> two-morphism, contravariant in the two-morphism.

```lean
noncomputable def pullbackIso :
    (whiskeringLeft 𝒳.based.objᵒᵖ 𝒴.based.objᵒᵖ A).obj
        (homFunctorOp g) ≅
      (whiskeringLeft 𝒳.based.objᵒᵖ 𝒴.based.objᵒᵖ A).obj
        (homFunctorOp f)
```

**`CategoryTheory.CatFiberedInGroupoids.pullbackIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L155). The attribute's comment: “pointwise description of restriction”.

> **Stacks 06TM.** On a presheaf and an object, the restriction comparison is evaluation on
> the component of the given two-morphism.

```lean
theorem pullbackIso_hom_app (P : 𝒴.based.objᵒᵖ ⥤ A) (x : 𝒳.based.obj) :
    ((pullbackIso A t).hom.app P).app (Opposite.op x) =
      P.map (t.hom.toNatTrans.app x).op
```

**`CategoryTheory.CatFiberedInGroupoids.pullbackIso_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L163). The attribute's comment: “vertical composition on restriction”.

> **Stacks 06TM.** Vertical composition of two-morphisms becomes composition of the induced
> restriction isomorphisms, in reverse order.

```lean
theorem pullbackIso_trans {h : 𝒳 ⟶ 𝒴} (s : g ⟶ h) :
    pullbackIso A (t ≫ s) = pullbackIso A s ≪≫ pullbackIso A t
```

**`CategoryTheory.CatFiberedInGroupoids.pullbackIso_hcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L176). The attribute's comment: “horizontal composition on restriction”.

> **Stacks 06TM.** The restriction comparison for a horizontal composite acts pointwise by
> the two component maps, in the contravariant order.

```lean
theorem pullbackIso_hcomp {𝒵 : CatFiberedInGroupoids.{v₀, v₁, u₀, u₁} B}
    {h k : 𝒴 ⟶ 𝒵} (s : h ⟶ k) (P : 𝒵.based.objᵒᵖ ⥤ A) (x : 𝒳.based.obj) :
    ((pullbackIso (f := f ≫ h) (g := g ≫ k) A
      (Bicategory.whiskerRight t h ≫ Bicategory.whiskerLeft g s)).hom.app P).app
        (Opposite.op x) =
      P.map (s.hom.toNatTrans.app ((CatFiberedInGroupoids.homFunctor g).obj x)).op ≫
        P.map ((CatFiberedInGroupoids.homFunctor h).map (t.hom.toNatTrans.app x)).op
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L225). The attribute's comment: “canonical isomorphism on right adjoints”.

> **Stacks 06TM.** Direct image of presheaves along the isomorphism of functors underlying a
> two-morphism, obtained as the adjoint mate of the pullback isomorphism.

```lean
noncomputable def pushforwardIso :
    (homFunctorOp f).ran (H := A) ≅
      (homFunctorOp g).ran (H := A)
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L234). The attribute's comment: “compatibility with adjunction”.

> **Stacks 06TM.** The direct-image comparison is the mate of the restriction comparison,
> expressing compatibility with both adjunctions.

```lean
theorem pushforwardIso_hom :
    (pushforwardIso A t).hom =
      conjugateEquiv ((homFunctorOp f).ranAdjunction A)
        ((homFunctorOp g).ranAdjunction A)
        (pullbackIso A t).hom
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIso_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L243). The attribute's comment: “vertical composition on right adjoints”.

> **Stacks 06TM.** Vertical composition of two-morphisms becomes composition of the
> corresponding direct-image isomorphisms.

```lean
theorem pushforwardIso_trans {h : 𝒳 ⟶ 𝒴} (s : g ⟶ h)
    [∀ (F : 𝒳.based.objᵒᵖ ⥤ A),
      (homFunctorOp h).HasRightKanExtension F] :
    pushforwardIso A (t ≫ s) = pushforwardIso A t ≪≫ pushforwardIso A s
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIso_hcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Presheaves.lean#L256). The attribute's comment: “horizontal composition on right adjoints”.

> **Stacks 06TM.** The direct-image comparison for a horizontal composite, after identifying
> direct images of composites with successive direct images, is the horizontal composite of the
> two direct-image comparisons.

```lean
theorem pushforwardIso_hcomp {𝒵 : CatFiberedInGroupoids.{v₀, v₁, u₀, u₁} B}
    {h k : 𝒴 ⟶ 𝒵} (s : h ⟶ k)
    [∀ (P : 𝒴.based.objᵒᵖ ⥤ A),
      (homFunctorOp h).HasRightKanExtension P]
    [∀ (P : 𝒴.based.objᵒᵖ ⥤ A),
      (homFunctorOp k).HasRightKanExtension P]
    [∀ (F : 𝒳.based.objᵒᵖ ⥤ A),
      (homFunctorOp (f ≫ h)).HasRightKanExtension F]
    [∀ (F : 𝒳.based.objᵒᵖ ⥤ A),
      (homFunctorOp (g ≫ k)).HasRightKanExtension F]
    [∀ (F : 𝒳.based.objᵒᵖ ⥤ A),
      ((homFunctorOp f) ⋙
        (homFunctorOp h)).HasRightKanExtension F]
    [∀ (F : 𝒳.based.objᵒᵖ ⥤ A),
      ((homFunctorOp g) ⋙
        (homFunctorOp k)).HasRightKanExtension F] :
    pushforwardIso A (Bicategory.whiskerRight t h ≫ Bicategory.whiskerLeft g s) ≪≫
        ranCompIso (homFunctorOp g)
          (homFunctorOp k) A =
      ranCompIso (homFunctorOp f)
          (homFunctorOp h) A ≪≫
        Functor.isoWhiskerRight (pushforwardIso A t)
          ((homFunctorOp h).ran (H := A)) ≪≫
        Functor.isoWhiskerLeft ((homFunctorOp g).ran (H := A))
        (pushforwardIso A s)
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIsoOfSets`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean#L77). The attribute's comment: “canonical isomorphism of direct images of presheaves of sets”.

> **Stacks 06TM.** The canonical isomorphism `{}_pt : {}_pf ≅ {}_pg` of direct images of
> presheaves of sets induced by a two-morphism `t : f ⟶ g`, namely the mate of the restriction
> comparison `t^p : g^p ≅ f^p` for the adjunctions `(f^p, {}_pf)` and `(g^p, {}_pg)`. The direct
> images exist by instance search: Mathlib's pointwise right Kan extension, computed by limits in
> `Type (max u₁ v₁ w)`.

```lean
noncomputable def pushforwardIsoOfSets :
    (homFunctorOp f).ran (H := Type (max u₁ v₁ w)) ≅ (homFunctorOp g).ran
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIsoOfSets_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean#L85). The attribute's comment: “compatibility with adjointness, for presheaves of sets”.

> **Stacks 06TM.** The isomorphism `{}_pt` of direct images of presheaves of sets is
> compatible with adjointness of `(f^p, {}_pf)` and `(g^p, {}_pg)`: it is the conjugate of
> `t^p : g^p ≅ f^p` for the two adjunctions.

```lean
theorem pushforwardIsoOfSets_hom :
    (pushforwardIsoOfSets.{w} t).hom =
      conjugateEquiv ((homFunctorOp f).ranAdjunction (Type (max u₁ v₁ w)))
        ((homFunctorOp g).ranAdjunction (Type (max u₁ v₁ w)))
        (pullbackIso (Type (max u₁ v₁ w)) t).hom
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIsoOfSets_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean#L95). The attribute's comment: “vertical composition on direct images of presheaves of sets”.

> **Stacks 06TM.** Vertical composition of two-morphisms becomes composition of the induced
> isomorphisms of direct images of presheaves of sets.

```lean
theorem pushforwardIsoOfSets_trans {h : 𝒳 ⟶ 𝒴} (s : g ⟶ h) :
    pushforwardIsoOfSets.{w} (t ≫ s) = pushforwardIsoOfSets.{w} t ≪≫ pushforwardIsoOfSets s
```

**`CategoryTheory.CatFiberedInGroupoids.pushforwardIsoOfSets_hcomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/PresheavesOfSets.lean#L103). The attribute's comment: “horizontal composition on direct images of presheaves of sets”.

> **Stacks 06TM.** The isomorphism of direct images of presheaves of sets induced by a
> horizontal composite of two-morphisms, after identifying direct images along composites with
> successive direct images, is the horizontal composite of the two induced isomorphisms.

```lean
theorem pushforwardIsoOfSets_hcomp {𝒵 : CatFiberedInGroupoids.{v₀, v₁, u₀, u₁} B}
    {h k : 𝒴 ⟶ 𝒵} (s : h ⟶ k) :
    pushforwardIsoOfSets.{w} (Bicategory.whiskerRight t h ≫ Bicategory.whiskerLeft g s) ≪≫
        ranCompIso (homFunctorOp g) (homFunctorOp k) (Type (max u₁ v₁ w)) =
      ranCompIso (homFunctorOp f) (homFunctorOp h) (Type (max u₁ v₁ w)) ≪≫
        isoWhiskerRight (pushforwardIsoOfSets.{w} t)
          ((homFunctorOp h).ran (H := Type (max u₁ v₁ w))) ≪≫
        isoWhiskerLeft ((homFunctorOp g).ran (H := Type (max u₁ v₁ w)))
          (pushforwardIsoOfSets.{w} s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.3, Tag 06TI](https://stacks.math.columbia.edu/tag/06TI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
