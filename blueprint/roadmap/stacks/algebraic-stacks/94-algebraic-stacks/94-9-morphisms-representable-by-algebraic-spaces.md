---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces, AlgebraicGeometry.Stack.exists_algebraicSpace_over_baseChange, AlgebraicGeometry.Stack.baseChangeSpace, AlgebraicGeometry.Stack.nonempty_equivalenceOver_baseChangeSpace, AlgebraicGeometry.Stack.baseChangeStructureMap, AlgebraicGeometry.isRepresentableByAlgebraicSpaces_iff_associatedMap, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_iff_of_equivalences, AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_isRepresentableByAlgebraicSpace
statement: formalized
proof: formalized
---

# 94.9 Morphisms representable by algebraic spaces

Section 94.9 of the Stacks Project, [Tag 04SX](https://stacks.math.columbia.edu/tag/04SX). 12 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02ZW, a definition

[Tag 02ZW](https://stacks.math.columbia.edu/tag/02ZW) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Representability.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Representability.lean#L80).

> **Stacks 02ZW.** A 1-morphism of categories over the big fppf site of `S` is *representable
> by algebraic spaces* if, for every scheme `U` over `S` and every scheme-valued point
> `y : (Sch/U)_{fppf} ⟶ 𝒴` of its target, the first projection of the 2-fibre product
> `(Sch/U)_{fppf} ×_𝒴 𝒳 ⟶ (Sch/U)_{fppf}` is equivalent, over the big fppf site of `U`, to the
> category of elements of the sheaf of points of an algebraic space over `U`.

```lean
abbrev IsRepresentableByAlgebraicSpaces
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : BasedCategory.{v₁, w₁} (BigFppfOver B S hS)}
    {𝒴 : BasedCategory.{v₂, w₂} (BigFppfOver B S hS)}
    (f : 𝒳 ⥤ᵇ 𝒴) : Prop
```

## Tag 0402, an equation

[Tag 0402](https://stacks.math.columbia.edu/tag/0402) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_algebraicSpace_over_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicSpace.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeAlgebraicSpace.lean#L43).

> The algebraic space representing the 2-fibre product of a 1-morphism representable by
> algebraic spaces with a scheme-valued point `y` of its target, viewed over the original base,
> comes with its canonical morphism to `U`. The representing equivalence is over the big fppf
> category of `U`.

```lean
theorem exists_algebraicSpace_over_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (hf : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (U : BigFppfOver B S hS)
    (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
    (hy : y ⋙ 𝒴.val.p = Over.map U.hom) :
    ∃ (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F)
      (Fy : SpacesOverSmallerBase B U.left.1 S U.left.2 hS U.hom),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
          (CatFiberedInGroupoids.homFunctor f))
        (presheafOfCategories (F ⋙ typeToCat)).p) ∧
      Fy = (spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩ ∧
      ∃ (ι : Fy.1.left ≅ (OverShriek.relocalizePresheafFunctor U.hom).obj F),
        ∀ (W : BigFppfOver B S hS) (s : Fy.1.left.obj (op W)),
          (Fy.1.hom.app (op W) s).left = (ι.hom.app (op W) s).1.1
```

**`AlgebraicGeometry.Stack.baseChangeSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeSpace.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeSpace.lean#L99). The attribute's comment: “the representing algebraic space F\_y”.

> **Stacks 0402.** The algebraic space `F_y` over `U` representing the 2-fibre product
> `(Sch/U)_fppf ×_{y, 𝒴} 𝒳` of a 1-morphism `f` representable by algebraic spaces along a point
> `y` of its target over `U`.
>
> This is a choice of representative; see the implementation notes.

```lean
noncomputable def baseChangeSpace : AlgebraicSpaces B U.left.1 U.left.2
```

**`AlgebraicGeometry.Stack.nonempty_equivalenceOver_baseChangeSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeSpace.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeSpace.lean#L106). The attribute's comment: “F\_y represents the 2-fibre product”.

> **Stacks 0402, the squiggly arrow.** The category of elements of
> `AlgebraicGeometry.Stack.baseChangeSpace` is equivalent, over the big fppf site of `U`, to the
> first projection of the 2-fibre product `(Sch/U)_fppf ×_{y, 𝒴} 𝒳`.

```lean
theorem nonempty_equivalenceOver_baseChangeSpace :
    Nonempty (StacksRepresentableCFG.EquivalenceOver
      (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.p 𝒴.p y f.toFunctor)
      (presheafOfCategories ((baseChangeSpace B S hS f hf U y hy).1 ⋙ typeToCat)).p)
```

**`AlgebraicGeometry.Stack.baseChangeStructureMap`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeSpace.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeSpace.lean#L124). The attribute's comment: “the structure morphism f\_y”.

> **Stacks 0402.** The structure morphism `f_y : F_y ⟶ U` of the display, as a morphism of
> algebraic spaces over `S` from `AlgebraicGeometry.Stack.baseChangeSpace` to the representable
> algebraic space of `U`.

```lean
noncomputable abbrev baseChangeStructureMap :
    (⟨(baseChangeSpaceOverBase B S hS f hf U y hy).1.left,
      (baseChangeSpaceOverBase B S hS f hf U y hy).property⟩ : AlgebraicSpaces B S hS) ⟶
      (schemeSpace (Over.mk U.hom) :
        AlgebraicSpaces B S hS)
```

## Tag 02ZY, a lemma

[Tag 02ZY](https://stacks.math.columbia.edu/tag/02ZY) in the Stacks Project.

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_iff_associatedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/MorphismRepresentableBySpaces/Criterion.lean, line 756](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/MorphismRepresentableBySpaces/Criterion.lean#L756).

> **Stacks 02ZY.** A morphism of categories fibred in groupoids is representable by
> algebraic spaces if and only if its functors on fibres are faithful and, for every
> object of the target over a scheme, the associated presheaf of pairs is an
> algebraic space over that scheme.

```lean
public theorem isRepresentableByAlgebraicSpaces_iff_associatedMap
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (AlgebraicGeometry.BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (c : 𝒴.val.p.ChoiceOfPullbacks) :
    AlgebraicGeometry.IsRepresentableByAlgebraicSpaces B S hS f.hom ↔
      ((∀ U : AlgebraicGeometry.BigFppfOver B S hS,
        (Stacks.RepresentableMorphism.inducedFiberFunctor 𝒳.val.p 𝒴.val.p
          (CatFiberedInGroupoids.homFunctor f)
          (CatFiberedInGroupoids.homFunctor_comp_p f) U).Faithful) ∧
        (∀ (U : AlgebraicGeometry.BigFppfOver B S hS) (y : 𝒴.val.p.Fiber U),
          IsAlgebraicSpacePairIsoClassPresheaf B S hS f c U y))
```

## Tag 0457, a lemma

[Tag 0457](https://stacks.math.columbia.edu/tag/0457) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_iff_of_equivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentabilityInvariance.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentabilityInvariance.lean#L93).

> Representability by algebraic spaces of a morphism of categories fibred in groupoids is
> invariant under horizontal equivalences in a 2-commutative square.

```lean
theorem isRepresentableByAlgebraicSpaces_iff_of_equivalences
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳' : CatFiberedInGroupoids.{u, v₁, u + 1, w₁}
      (BigFppfOver B S hS)}
    {𝒳 : CatFiberedInGroupoids.{u, v₂, u + 1, w₂}
      (BigFppfOver B S hS)}
    {𝒴' : CatFiberedInGroupoids.{u, v₃, u + 1, w₃}
      (BigFppfOver B S hS)}
    {𝒴 : CatFiberedInGroupoids.{u, v₄, u + 1, w₄}
      (BigFppfOver B S hS)}
    (f' : 𝒳'.val ⥤ᵇ 𝒴'.val) (f : 𝒳.val ⥤ᵇ 𝒴.val)
    (a : 𝒳'.val ⥤ᵇ 𝒳.val) (b : 𝒴'.val ⥤ᵇ 𝒴.val)
    (α : BasedFunctor.comp a f ≅ BasedFunctor.comp f' b)
    [Functor.IsEquivalence a.toFunctor]
    [Functor.IsEquivalence b.toFunctor] :
    IsRepresentableByAlgebraicSpaces B S hS f ↔
      IsRepresentableByAlgebraicSpaces B S hS f'
```

## Tag 02ZZ, a lemma

[Tag 02ZZ](https://stacks.math.columbia.edu/tag/02ZZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_of_isRepresentableByAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicSpaceStack.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicSpaceStack.lean#L213).

> **Stacks 02ZZ.** A 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` whose source and target are both representable by algebraic spaces over `S` is representable
> by algebraic spaces.
>
> Both source and target are transported to categories of elements, where
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_fibredCategory` applies: the source by
> `AlgebraicGeometry.Stack.nonempty_equivalenceOver_fst_of_equivalence_source`, the target by
> Stacks 0457.

```lean
theorem isRepresentableByAlgebraicSpaces_of_isRepresentableByAlgebraicSpace
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : IsRepresentableByAlgebraicSpace B S hS 𝒳)
    (h𝒴 : IsRepresentableByAlgebraicSpace B S hS 𝒴) :
    IsRepresentableByAlgebraicSpaces B S hS f.hom
```

## Tag 0458, a lemma

[Tag 0458](https://stacks.math.columbia.edu/tag/0458) in the Stacks Project.

**`AlgebraicGeometry.Stack.associatedMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresheafFibredCategory.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresheafFibredCategory.lean#L65). The attribute's comment: “associated morphism”.

> The 1-morphism of categories fibred in groupoids induced by a map `a` of set-valued
> presheaves, together with its value on objects: it sends `(U, x)` to `(U, a_U(x))`.

```lean
def associatedMap
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) :
    {f : fibredCategory B S hS F ⟶ fibredCategory B S hS G //
      ∀ x : (fibredCategory B S hS F).val.obj,
      HEq ((CatFiberedInGroupoids.homFunctor f).obj x).fiber
          (Discrete.mk (a.app (Opposite.op x.base)
            (Discrete.as (show Discrete (F.obj (Opposite.op x.base)) from x.fiber))))}
```

**`AlgebraicGeometry.Stack.associatedMap_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresheafFibredCategory.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresheafFibredCategory.lean#L99). The attribute's comment: “the associated morphism on objects”.

> The 1-morphism attached to a map `a : F ⟶ G` of set-valued presheaves sends the pair
> `(U, x)` to the pair `(U, a_U(x))`.

```lean
theorem associatedMap_obj
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G)
    (x : (fibredCategory B S hS F).val.obj) :
    (associatedMap B S hS a).1.hom.obj x =
      ⟨x.base, Discrete.mk (a.app (Opposite.op x.base) x.fiber.as)⟩
```

**`AlgebraicGeometry.Stack.associatedMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresheafFibredCategory.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresheafFibredCategory.lean#L174). The attribute's comment: “functoriality of the associated morphism”.

> The 1-morphism attached to a composite of maps of presheaves is the composite of the two
> attached 1-morphisms.

```lean
theorem associatedMap_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (b : G ⟶ H) :
    (associatedMap B S hS (a ≫ b)).1 =
      (associatedMap B S hS a).1 ≫ (associatedMap B S hS b).1
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_iff_associatedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresheafRepresentability.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresheafRepresentability.lean#L146). The attribute's comment: “representability equivalence”.

> **Stacks 0458**, representability equivalence. A map `a : F ⟶ G` of set-valued presheaves on
> the big fppf site of `S` is representable by algebraic spaces exactly when the 1-morphism of
> categories fibred in groupoids it induces, `AlgebraicGeometry.Stack.associatedMap`, is.
>
> A scheme-valued point of the category of elements of `G` over a scheme `U` over `S` and a section
> of `G` over `U` naming the same family of elements have the same base change of `a`: the presheaf
> representing the base change of the 1-morphism along the point is the fibre of `a` over the
> section, and the relocalization of that fibre along the structure morphism of `U` is the base
> change of `a` along the section.

```lean
theorem isRepresentableByAlgebraicSpaces_iff_associatedMap
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) :
    Space.IsRepresentableByAlgebraicSpaces B S hS a ↔
      IsRepresentableByAlgebraicSpaces B S hS (associatedMap B S hS a).1.hom
```

## Tag 04SY, a lemma

[Tag 04SY](https://stacks.math.columbia.edu/tag/04SY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isoClassMap_isRepresentableByAlgebraicSpaces_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SetoidRepresentability.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SetoidRepresentability.lean#L256).

> For categories fibred in setoids, representability by algebraic spaces of
> the induced map of isomorphism-class presheaves is equivalent to
> representability of the original morphism.

```lean
public theorem isoClassMap_isRepresentableByAlgebraicSpaces_iff
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInSetoids.{u, v, u + 1, u}
      (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (a : 𝒳.val.p.isoClassPresheaf ⟶ 𝒴.val.p.isoClassPresheaf)
    (ha : ∀ (U : BigFppfOver B S hS) (x : 𝒳.val.p.Fiber U),
      a.app (Opposite.op U) (Functor.isoClassMk 𝒳.val.p x) =
        Functor.isoClassMk 𝒴.val.p
          ((Functor.Fiber.mapOfComp 𝒳.val.p 𝒴.val.p
            (CatFiberedInGroupoids.homFunctor f)
            (CatFiberedInGroupoids.homFunctor_comp_p f) U).obj x)) :
    AlgebraicGeometry.Space.IsRepresentableByAlgebraicSpaces B S hS
        a ↔
      AlgebraicGeometry.Stack.IsRepresentableByAlgebraicSpaces B S hS
        (CatFiberedInSetoids.inclusion.map f).hom
```

## Tag 0302, a lemma

[Tag 0302](https://stacks.math.columbia.edu/tag/0302) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_twoFibreProductFst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean#L91).

> If `f : 𝒳 ⟶ 𝒴` is a 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` which is representable by algebraic spaces and `g : 𝒵 ⟶ 𝒴` is any 1-morphism, then the base
> change `𝒵 ×_{g, 𝒴, f} 𝒳 ⟶ 𝒵` is representable by algebraic spaces. No relation is assumed
> between the universes of the three categories.

```lean
theorem isRepresentableByAlgebraicSpaces_twoFibreProductFst
    (𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS))
    (𝒵 : CatFiberedInGroupoids.{u, v₁, u + 1, w₁} (BigFppfOver B S hS))
    (𝒳 : CatFiberedInGroupoids.{u, v₂, u + 1, w₂} (BigFppfOver B S hS))
    (g : 𝒵.val ⥤ᵇ 𝒴.val) (f : 𝒳.val ⥤ᵇ 𝒴.val)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f) :
    IsRepresentableByAlgebraicSpaces B S hS (twoFibreProductFst B S hS 𝒴 𝒵 𝒳 g f)
```

## Tag 0300, a lemma

[Tag 0300](https://stacks.math.columbia.edu/tag/0300) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/BaseChangeRepresentableBySpace.lean#L110).

> Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of categories fibred in groupoids over the big fppf site of
> `S` which is representable by algebraic spaces, let `g : 𝒵 ⟶ 𝒴` be any 1-morphism, and assume
> `𝒵` is represented by an algebraic space over `S`. Then the 2-fibre product `𝒵 ×_𝒴 𝒳` is
> represented by an algebraic space over `S`.

```lean
theorem isRepresentableByAlgebraicSpace_twoFibreProduct
    (𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS))
    (𝒵 : CatFiberedInGroupoids.{u, v₁, u + 1, w₁} (BigFppfOver B S hS))
    (𝒳 : CatFiberedInGroupoids.{u, v₂, u + 1, w₂} (BigFppfOver B S hS))
    (g : 𝒵.val ⥤ᵇ 𝒴.val) (f : 𝒳.val ⥤ᵇ 𝒴.val)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f)
    (h𝒵 : IsRepresentableByAlgebraicSpace B S hS 𝒵) :
    IsRepresentableByAlgebraicSpace B S hS (twoFibreProduct B S hS 𝒴 𝒵 𝒳 g f)
```

## Tag 0301, a lemma

[Tag 0301](https://stacks.math.columbia.edu/tag/0301) in the Stacks Project.

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentabilityComp.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentabilityComp.lean#L332).

> The composition of two morphisms representable by algebraic spaces is
> representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w}
      (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom) :
    IsRepresentableByAlgebraicSpaces B S hS (f ≫ g).hom
```

## Tag 0303, a lemma

[Tag 0303](https://stacks.math.columbia.edu/tag/0303) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_productMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProductMorphism.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProductMorphism.lean#L360).

> **Stacks 0303.** The product `f₁ × f₂` of two 1-morphisms of categories fibred in groupoids
> over the big fppf site of `S`, each representable by algebraic spaces, is representable by
> algebraic spaces.
>
> It factors as `(id_{𝒴₁} × f₂) ∘ (f₁ × id_{𝒳₂})`, each factor is representable by
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_productMap_id_left` resp.
> `…_id_right`, and the composite is representable by Stacks 0301.

```lean
theorem isRepresentableByAlgebraicSpaces_productMap (f₁ : 𝒳₁ ⟶ 𝒴₁) (f₂ : 𝒳₂ ⟶ 𝒴₂)
    (hf₁ : IsRepresentableByAlgebraicSpaces B S hS f₁.hom)
    (hf₂ : IsRepresentableByAlgebraicSpaces B S hS f₂.hom) :
    IsRepresentableByAlgebraicSpaces B S hS (productMap f₁ f₂).hom
```

## Tag 0CKY, a lemma

[Tag 0CKY](https://stacks.math.columbia.edu/tag/0CKY) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStack_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismStack.lean, line 842](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableMorphismStack.lean#L842).

> **Stacks 0CKY.** Let `𝒳 ⟶ 𝒵` and `𝒴 ⟶ 𝒵` be 1-morphisms of categories fibred in groupoids
> over the big fppf site of `S`. If `𝒳 ⟶ 𝒵` is representable by algebraic spaces and `𝒴` is a
> stack in groupoids, then the 2-fibre product `𝒳 ×_𝒵 𝒴` is a stack in groupoids.

```lean
theorem isStack_of_isTwoFibreProduct
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (AlgebraicGeometry.BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒵) (g : 𝒴 ⟶ 𝒵)
    (P : Bicategory.TwoCommSq f g)
    (hP : Bicategory.IsTwoFibreProduct P)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (h𝒴 : 𝒴.val.p.IsStack (AlgebraicGeometry.BigFppfOver.topology B S hS)) :
    P.pt.val.p.IsStack (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.9, Tag 04SX](https://stacks.math.columbia.edu/tag/04SX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
