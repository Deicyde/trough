---
declaration: section
origin: cited
lean: Deformation.FormalObject, Deformation.FormalObject.Hom, Deformation.FormalObject.instCategory, Deformation.formalObjectProjection_isCofiberedInGroupoids, Deformation.FormalObject.projection, Deformation.filteredFormalObjectsEquivalence, Deformation.cofiberedCompletion_obj_equiv_formalObject, Deformation.restrictionCompletionEquivalence
statement: formalized
proof: formalized
---

# 90.7 Formal objects and completion categories

Section 90.7 of the Stacks Project, [Tag 06H2](https://stacks.math.columbia.edu/tag/06H2). 14 tags here are carried by 46 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06H3, a definition

[Tag 06H3](https://stacks.math.columbia.edu/tag/06H3) in the Stacks Project.

**`Deformation.FormalObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L312). The attribute's comment: “objects”. References: SGA 7 VI (1.15).

> A formal object of a category `F` over `𝒞_Λ` consists of a complete local algebra `R`,
> an object of `F` over each positive adic truncation of `R`, and transition maps lying over the
> quotient projections.

```lean
structure FormalObject {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
```

**`Deformation.FormalObject.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L334). The attribute's comment: “morphisms”.

> A morphism of formal objects is a morphism of their complete local bases together with a
> compatible family of morphisms over its maps on all adic truncations.

```lean
structure Hom (X Y : FormalObject p)
```

**`Deformation.FormalObject.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L397). The attribute's comment: “category structure”.

> Formal objects and their compatible families of morphisms form a category.

```lean
instance instCategory : Category (FormalObject p)
```

## Tag 06H4, a lemma

[Tag 06H4](https://stacks.math.columbia.edu/tag/06H4) in the Stacks Project.

**`Deformation.formalObjectProjection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L476). References: SGA 7 VI (1.15), “Â is cofibered over Ĉ\_\{Λ”.

> **Stacks Project, Tag 06H4.** The projection from the category of formal objects of a
> category cofibered in groupoids to the category of complete local algebras is cofibered in
> groupoids.

```lean
public theorem formalObjectProjection_isCofiberedInGroupoids
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p) :
    IsCofiberedInGroupoids (FormalObject.projection (p := p))
```

## Tag 06H5, a definition

[Tag 06H5](https://stacks.math.columbia.edu/tag/06H5) in the Stacks Project.

**`Deformation.FormalObject.projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L410). The attribute's comment: “the completion of a category cofibered in groupoids”.

> The canonical functor from formal objects to their underlying complete local algebras.

```lean
def projection : FormalObject p ⥤ CompleteLocalAlgCat.{u, v, w} Λ k
```

## Tag 06H6, a lemma

[Tag 06H6](https://stacks.math.columbia.edu/tag/06H6) in the Stacks Project.

**`Deformation.filteredFormalObjectsEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Filtration/Equivalence.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Filtration/Equivalence.lean#L655).

> A cofinal ideal filtration gives the same category of formal objects over `R` as the
> maximal-ideal filtration.

```lean
theorem filteredFormalObjectsEquivalence {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (R : CompleteLocalAlgCat.{u, v, w} Λ k) (I : IdealFiltration R)
    (hp : IsCofiberedInGroupoids p) :
    Nonempty
      (FilteredFormalObject p R I ≌
        (FormalObject.projection (p := p)).Fiber R)
```

## Tag 06H8, a remark

[Tag 06H8](https://stacks.math.columbia.edu/tag/06H8) in the Stacks Project.

**`Deformation.cofiberedCompletion_obj_equiv_formalObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean#L721). The attribute's comment: “the completion of a set-valued functor is the limit over the adic truncations”.

> A section of the completed cofibered set at `S` is a formal object of the
> category of elements of `F` whose base is `S`.

```lean
public noncomputable def cofiberedCompletion_obj_equiv_formalObject
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type (max v z))
    (S : CompleteLocalAlgCat.{u, v, w} Λ k) :
    (cofiberedCompletion.obj F).obj S ≃
      {X : FormalObject (CategoryOfElements.π F) // X.base = S}
```

## Tag 06SJ, a remark

[Tag 06SJ](https://stacks.math.columbia.edu/tag/06SJ) in the Stacks Project.

**`Deformation.restrictionCompletionEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/RestrictionEquivalence/Equivalence.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/RestrictionEquivalence/Equivalence.lean#L436). References: SGA 7 VI (1.15), “special case”.

> Restricting the category of formal objects of a category cofibered in groupoids back
> to Artinian local algebras gives a canonical equivalence with the original category.

```lean
public noncomputable def restrictionCompletionEquivalence
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p) : RestrictionCompletionEquivalence p
```

## Tag 06H9, a remark

[Tag 06H9](https://stacks.math.columbia.edu/tag/06H9) in the Stacks Project.

**`Deformation.completionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L703). The attribute's comment: “completion\_morphism”.

> **Stacks Project, Tag 06H9.** A functor over the category of Artinian local algebras
> induces a functor on formal objects by application at every level.

```lean
public def completionMap
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q)) :
    BasedFunctor
      (BasedCategory.ofFunctor (FormalObject.projection (p := p)))
      (BasedCategory.ofFunctor (FormalObject.projection (p := q)))
```

**`Deformation.completionMap_obj_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 742](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L742). The attribute's comment: “completion\_morphism”.

> The induced functor does not change the complete local algebra underlying a formal object.

```lean
public theorem completionMap_obj_base
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (X : FormalObject p) :
    ((completionMap φ).obj X).base = X.base
```

**`Deformation.completionMap_obj_level`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 749](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L749). The attribute's comment: “completion\_morphism”.

> On objects, the induced completion functor applies the original functor at every level.

```lean
public theorem completionMap_obj_level
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (X : FormalObject p) (n : ℕ) :
    ((completionMap φ).obj X).level n = φ.obj (X.level n)
```

**`Deformation.completionMap_obj_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L757). The attribute's comment: “completion\_morphism”.

> On objects, the induced completion functor applies the original functor to every transition
> map.

```lean
public theorem completionMap_obj_transition
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (X : FormalObject p) (n : ℕ) :
    ((completionMap φ).obj X).transition n =
      eqToHom (completionMap_obj_level φ X (n + 1)) ≫ φ.map (X.transition n) ≫
        eqToHom (completionMap_obj_level φ X n).symm
```

**`Deformation.completionMap_map_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 769](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L769). The attribute's comment: “completion\_morphism”.

> The induced functor does not change the morphism of complete local algebras underlying a
> morphism of formal objects.

```lean
public theorem completionMap_map_base
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    {X Y : FormalObject p} (f : X ⟶ Y) :
    ((completionMap φ).map f).base =
      eqToHom (completionMap_obj_base φ X) ≫ f.base ≫
        eqToHom (completionMap_obj_base φ Y).symm
```

**`Deformation.completionMap_map_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 780](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L780). The attribute's comment: “completion\_morphism”.

> On morphisms, the induced completion functor applies the original functor to every level
> map.

```lean
public theorem completionMap_map_app
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    {X Y : FormalObject p} (f : X ⟶ Y) (n : ℕ) :
    ((completionMap φ).map f).app n =
      eqToHom (completionMap_obj_level φ X n) ≫ φ.map (f.app n) ≫
        eqToHom (completionMap_obj_level φ Y n).symm
```

**`Deformation.completionMap_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 804](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L804). The attribute's comment: “completion\_two\_functor”.

> **Stacks Project, Tag 06H9.** Completion takes the identity morphism of a category cofibered
> in groupoids to the identity morphism of its completion. Together with `completionMap_comp`,
> `completionNatTrans_id` and `completionNatTrans_comp` this is the statement that completion is a
> functor of two-categories; the equality is strict, not merely up to isomorphism.

```lean
public theorem completionMap_id :
    completionMap (BasedFunctor.id (BasedCategory.ofFunctor p)) =
      BasedFunctor.id (BasedCategory.ofFunctor (FormalObject.projection (p := p)))
```

**`Deformation.completionMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L814). The attribute's comment: “completion\_two\_functor”.

> **Stacks Project, Tag 06H9.** Completion takes a composite of morphisms of categories
> cofibered in groupoids to the composite of the completions. Together with `completionMap_id`,
> `completionNatTrans_id` and `completionNatTrans_comp` this is the statement that completion is a
> functor of two-categories; the equality is strict, not merely up to isomorphism.

```lean
public theorem completionMap_comp {H : Type uH} [Category.{vH} H]
    {r : H ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (ψ : BasedFunctor (BasedCategory.ofFunctor q) (BasedCategory.ofFunctor r)) :
    completionMap (φ.comp ψ) = (completionMap φ).comp (completionMap ψ)
```

**`Deformation.completionNatTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 839](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L839). The attribute's comment: “completion\_two\_morphism”.

> **Stacks Project, Tag 06H9.** The natural transformation induced levelwise on formal
> objects by a two-morphism over the Artinian base.

```lean
public def completionNatTrans
    {φ ψ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q)}
    (t : BasedNatTrans φ ψ) :
    BasedNatTrans (completionMap φ) (completionMap ψ)
```

**`Deformation.completionNatTrans_app_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 963](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L963). The attribute's comment: “completion\_two\_morphism”.

> The induced component is the identity on the complete local algebra.

```lean
public theorem completionNatTrans_app_base
    {φ ψ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q)}
    (t : BasedNatTrans φ ψ) (X : FormalObject p) :
    ((completionNatTrans t).toNatTrans.app X).base =
      eqToHom (completionMap_obj_base φ X) ≫
        eqToHom (completionMap_obj_base ψ X).symm
```

**`Deformation.completionNatTrans_app_level`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 973](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L973). The attribute's comment: “completion\_two\_morphism”.

> At every Artinian quotient, the induced component is the original two-morphism.

```lean
public theorem completionNatTrans_app_level
    {φ ψ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q)}
    (t : BasedNatTrans φ ψ) (X : FormalObject p) (n : ℕ) :
    ((completionNatTrans t).toNatTrans.app X).app n =
      eqToHom (completionMap_obj_level φ X n) ≫
        t.toNatTrans.app (X.level n) ≫
          eqToHom (completionMap_obj_level ψ X n).symm
```

**`Deformation.completionNatTrans_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 986](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L986). The attribute's comment: “completion\_two\_functor”.

> **Stacks Project, Tag 06H9.** Levelwise completion takes an identity two-morphism to an
> identity. This is half of the statement that completion is a functor of two-categories on
> two-morphisms.

```lean
public theorem completionNatTrans_id
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q)) :
    completionNatTrans (𝟙 φ) = 𝟙 (completionMap φ)
```

**`Deformation.completionNatTrans_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Basic.lean, line 1003](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Basic.lean#L1003). The attribute's comment: “completion\_two\_functor”.

> **Stacks Project, Tag 06H9.** Levelwise completion is compatible with composition of
> two-morphisms. This is the other half of the statement that completion is a functor of
> two-categories on two-morphisms.

```lean
public theorem completionNatTrans_comp
    {φ ψ χ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q)}
    (t : φ ⟶ ψ) (s : ψ ⟶ χ) :
    completionNatTrans (t ≫ s) =
      BasedNatTrans.comp (completionNatTrans t) (completionNatTrans s)
```

## Tag 06HA, a remark

[Tag 06HA](https://stacks.math.columbia.edu/tag/06HA) in the Stacks Project.

**`Deformation.completionHomEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/HomEquivalenceMain.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/HomEquivalenceMain.lean#L45). The attribute's comment: “hom\_equivalence”.

> **Stacks Project, Tag 06HA (hom equivalence).** Completion and restriction
> induce quasi-inverse equivalences on hom categories, with the forward and
> backward formulas specified above.

```lean
public noncomputable def completionHomEquivalence
    (hp : IsCofiberedInGroupoids p)
    (hq : IsCofiberedInGroupoids q) :
    CompletionHomEquivalence p q hp hq
```

**`Deformation.completionUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Unit.lean, line 512](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Unit.lean#L512). The attribute's comment: “unit”.

> **Stacks Project, Tag 06HA (unit).** Chosen pushforwards along all adic quotient maps
> assemble canonically into a morphism from a category cofibered in groupoids to the category
> of formal objects of its restriction.  It sends an object to its tower of chosen
> pushforwards, with the induced transition maps.

```lean
public noncomputable def completionUnit
    {G : Type uG} [Category.{vG} G]
    (p : G ⥤ CompleteLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p) :
    CompletionUnit p (adicPushforwardChoice p hp)
```

## Tag 06HB, a remark

[Tag 06HB](https://stacks.math.columbia.edu/tag/06HB) in the Stacks Project.

**`Deformation.cofiberedCompletion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean#L78). The attribute's comment: “completion functor”.

> Completion of a cofibered set, viewed as a covariant set-valued functor.
> Its sections over a complete local algebra are the compatible families of values
> on the Artinian truncations.

```lean
public noncomputable def cofiberedCompletion :
    (ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type (max v z)) ⥤
      (CompleteLocalAlgCat.{u, v, w} Λ k ⥤ Type (max v z))
```

**`Deformation.cofiberedCompletionAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean#L616). The attribute's comment: “functorial hom bijection”.

> Completion is right adjoint to restriction; its hom equivalence is the
> functorial bijection from maps out of a restriction to maps into a completion.

```lean
public noncomputable def cofiberedCompletionAdjunction :
    (Functor.whiskeringLeft
      (ArtinianLocalAlgCat.{u, v, w} Λ k)
      (CompleteLocalAlgCat.{u, v, w} Λ k)
      (Type (max v z))).obj
      (artinianToComplete (Λ := Λ) (k := k)) ⊣
      cofiberedCompletion (Λ := Λ) (k := k)
```

**`Deformation.cofiberedCompletion_isRightKanExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean#L686). The attribute's comment: “canonical completion”.

> Completion is the right Kan extension of a set-valued functor along the
> inclusion of Artinian local algebras, with the comparison supplied by the
> adjunction counit.

```lean
public theorem cofiberedCompletion_isRightKanExtension
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type (max v z)) :
    (cofiberedCompletion (Λ := Λ) (k := k) |>.obj F).IsRightKanExtension
      ((cofiberedCompletionAdjunction (Λ := Λ) (k := k)).counit.app F)
```

**`Deformation.cofiberedCompletion_obj_equiv_formalObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean#L721). The attribute's comment: “formal-object description”.

> A section of the completed cofibered set at `S` is a formal object of the
> category of elements of `F` whose base is `S`.

```lean
public noncomputable def cofiberedCompletion_obj_equiv_formalObject
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type (max v z))
    (S : CompleteLocalAlgCat.{u, v, w} Λ k) :
    (cofiberedCompletion.obj F).obj S ≃
      {X : FormalObject (CategoryOfElements.π F) // X.base = S}
```

**`Deformation.cofiberedCompletion_restriction_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean, line 731](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/Groupoid/CofiberedCompletion.lean#L731). The attribute's comment: “counit isomorphism”.

> The canonical map from the restriction of a completion to the original
> cofibered set is an isomorphism.

```lean
public theorem cofiberedCompletion_restriction_isIso
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type (max v z)) :
    IsIso ((cofiberedCompletionAdjunction (Λ := Λ) (k := k)).counit.app F)
```

## Tag 06HE, a remark

[Tag 06HE](https://stacks.math.columbia.edu/tag/06HE) in the Stacks Project.

**`Deformation.coyonedaIsoAdicCompletion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Completion.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Completion.lean#L380). The attribute's comment: “representable\_completion”. References: SGA 3 XI (3.3), “representable, affine”.

> The covariant functor represented by `R` is canonically the adic completion
> of its restriction to Artinian local algebras.

```lean
public noncomputable def coyonedaIsoAdicCompletion
    (R : CompleteLocalAlgCat.{u, v, w} Λ k) :
    coyoneda.obj (Opposite.op R) ≅
      adicCompletion (artinianToComplete ⋙
        coyoneda.obj (Opposite.op R))
```

**`Deformation.coyonedaIsoAdicCompletion_hom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Completion.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Completion.lean#L399). The attribute's comment: “representable\_completion”.

> At level `n`, the canonical isomorphism sends `f : R ⟶ S` to the composite
> of `f` with the quotient homomorphism `S → S / m_S ^ (n + 1)`.

```lean
public theorem coyonedaIsoAdicCompletion_hom_apply
    (R S : CompleteLocalAlgCat.{u, v, w} Λ k) (f : R ⟶ S) (n : ℕ) :
    (((coyonedaIsoAdicCompletion R).hom.app S f).value n).hom =
      (Ideal.Quotient.mkₐ Λ (AdicTruncation.ideal S n)).comp f.hom
```

**`Deformation.adicCompletionRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Completion.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Completion.lean#L814). The attribute's comment: “continuous\_functor\_completion”.

> A limit-preserving functor on complete local algebras is canonically the
> completion of its restriction to Artinian local algebras.

```lean
public noncomputable def adicCompletionRestrictionIso
    (G : CompleteLocalAlgCat.{u, v, w} Λ k ⥤ Type v)
    [PreservesLimits G] :
    G ≅ adicCompletion (artinianToComplete ⋙ G)
```

**`Deformation.adicCompletionRestrictionIso_hom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Completion.lean, line 843](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Completion.lean#L843). The attribute's comment: “continuous\_functor\_completion”.

> The canonical isomorphism sends a value to its image on each adic quotient.
> The formula is independent of the chosen morphism representing that quotient.

```lean
public theorem adicCompletionRestrictionIso_hom_apply
    (G : CompleteLocalAlgCat.{u, v, w} Λ k ⥤ Type v)
    [PreservesLimits G]
    (S : CompleteLocalAlgCat.{u, v, w} Λ k) (x : G.obj S) (n : ℕ)
    (q : S ⟶ artinianToComplete.obj (AdicTruncation.obj S n))
    (hq : q.hom = Ideal.Quotient.mkₐ Λ (AdicTruncation.ideal S n)) :
    ((adicCompletionRestrictionIso G).hom.app S x).value n = G.map q x
```

## Tag 06HC, a remark

[Tag 06HC](https://stacks.math.columbia.edu/tag/06HC) in the Stacks Project.

**`Deformation.associatedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/Associated.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/Associated.lean#L358). The attribute's comment: “associated\_morphism\_of\_formal\_object”. References: SGA 7 VI (2.2(d)), “construction of ξ^#”.

> **Stacks Project, Tag 06HC.** After choosing pushforwards, a formal object `ξ` over `R`
> determines a morphism from the restriction of the cofibered set represented by `R` to `F`.
> On an Artinian point `α : R → A`, it is the pushforward of the level indexed by the
> least nilpotence exponent of the maximal ideal of `A`, minus one.

```lean
public noncomputable def associatedMorphism
    (hp : IsCofiberedInGroupoids p) (ξ : FormalObject p)
    (pushforwards : ChosenPushforwards p) : AssociatedMorphism ξ pushforwards
```

**`Deformation.formalObjectsYonedaEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L385). The attribute's comment: “formal\_objects\_yoneda\_equivalence”.

> Morphisms over the Artinian base from the restriction of the functor represented by `R`
> to a category cofibered in groupoids form a category equivalent to the category of formal
> objects over `R`, with the quasi-inverse `Ψ ∘ ι`. The forward direction is the equivalence
> constructed in Tag 06SK by `representableMorphismFormalObjectEquivalence`, so it carries that
> construction's explicit description at the Artinian quotient points of `R` and its
> factorization through `Φ` followed by 2-Yoneda evaluation.

```lean
public noncomputable def formalObjectsYonedaEquivalence
    (hp : IsCofiberedInGroupoids p)
    (R : CompleteLocalAlgCat.{u, v, w} Λ k)
    (P : ChosenCompletePushforwards (FormalObject.projection (p := p))) :
    BasedFunctor
        (BasedCategory.ofFunctor (Functor.Elements.π (restrictedCoyoneda R)))
        (BasedCategory.ofFunctor p) ≌
      (FormalObject.projection (p := p)).Fiber R
```

**`Deformation.formalObjectsYonedaEquivalence_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L401). The attribute's comment: “formal\_objects\_yoneda\_equivalence”.

> The forward direction of the Yoneda equivalence is the equivalence constructed in Tag
> 06SK. Its `levelIso` and `transition_comm` give the explicit description sending `φ` to the
> formal object `(R, φ(R → R/𝔪_R^n), φ(f_n))`, and its `completionComparison` exhibits it as
> `Φ` followed by 2-Yoneda evaluation.

```lean
public theorem formalObjectsYonedaEquivalence_functor
    (hp : IsCofiberedInGroupoids p)
    (R : CompleteLocalAlgCat.{u, v, w} Λ k)
    (P : ChosenCompletePushforwards (FormalObject.projection (p := p))) :
    (formalObjectsYonedaEquivalence hp R P).functor =
      (representableMorphismFormalObjectEquivalence p hp R).equivalence.functor
```

**`Deformation.formalObjectsYonedaEquivalence_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L411). The attribute's comment: “formal\_objects\_yoneda\_equivalence”.

> The quasi-inverse of the Yoneda equivalence is the composite `Ψ ∘ ι` specified in the
> source.

```lean
public theorem formalObjectsYonedaEquivalence_inverse
    (hp : IsCofiberedInGroupoids p)
    (R : CompleteLocalAlgCat.{u, v, w} Λ k)
    (P : ChosenCompletePushforwards (FormalObject.projection (p := p))) :
    (formalObjectsYonedaEquivalence hp R P).inverse = iotaCompPsi hp R P
```

**`Deformation.associatedMorphism_maps_to_canonicalEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L665). The attribute's comment: “formal\_objects\_yoneda\_equivalence”.

> The explicit morphism `ξ̲` associated to a formal object `ξ` maps to `ξ` under the Yoneda
> equivalence: evaluating the equivalence constructed in Tag 06SK on
> `associatedMorphism hp ξ pushforwards` returns `ξ`, up to an isomorphism over its complete
> local base.

```lean
public theorem associatedMorphism_maps_to_canonicalEquivalence
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : IsCofiberedInGroupoids p)
    (ξ : FormalObject p)
    (pushforwards : ChosenPushforwards p) :
    Nonempty
      ((representableMorphismFormalObjectEquivalence p hp ξ.base).equivalence.functor.obj
        (associatedMorphism hp ξ pushforwards).toBasedFunctor ≅
          (Functor.Fiber.mk rfl : (FormalObject.projection (p := p)).Fiber ξ.base))
```

**`Deformation.psiIotaIsoAssociatedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 700](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L700). The attribute's comment: “formal\_objects\_yoneda\_equivalence”.

> The explicit `Ψ(ι(ξ))` is isomorphic, over the Artinian base, to the morphism `ξ̲`
> associated to `ξ` using any chosen pushforwards in the original category.

```lean
public noncomputable def psiIotaIsoAssociatedMorphism
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : IsCofiberedInGroupoids p)
    (ξ : FormalObject p)
    (pushforwards : ChosenPushforwards p)
    (P : ChosenCompletePushforwards (FormalObject.projection (p := p))) :
    (psi hp ξ.base).obj ((iota ξ.base P).obj
        (Functor.Fiber.mk rfl : (FormalObject.projection (p := p)).Fiber ξ.base)) ≅
      (associatedMorphism hp ξ pushforwards).toBasedFunctor
```

**`Deformation.iotaIsoCompletionAssociatedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 719](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L719). The attribute's comment: “formal\_objects\_yoneda\_equivalence”.

> Under the canonical represented-completion identification, `ι(ξ)` is the completion of the
> associated morphism `ξ̲`: `Φ` is the unit followed by levelwise completion, as in 06HA.

```lean
public noncomputable def iotaIsoCompletionAssociatedMorphism
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : IsCofiberedInGroupoids p)
    (ξ : FormalObject p)
    (pushforwards : ChosenPushforwards p)
    (P : ChosenCompletePushforwards (FormalObject.projection (p := p))) :
    (iota ξ.base P).obj
        (Functor.Fiber.mk rfl : (FormalObject.projection (p := p)).Fiber ξ.base) ≅
      (unitBasedFunctor (representedProjection ξ.base)
        (representedProjection_cofibered ξ.base)).comp
          (completionMap
            ((extendRepresentedHom p ξ.base).obj
              (associatedMorphism hp ξ pushforwards).toBasedFunctor))
```

Declarations registered for the tag:

- [`representableMorphismFormalObjectEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=representableMorphismFormalObjectEquivalence#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/YonedaEquivalence.lean#L419) (StacksFrontier): “formal\_objects\_yoneda\_equivalence”.

## Tag 06SK, an equation

[Tag 06SK](https://stacks.math.columbia.edu/tag/06SK) in the Stacks Project.

**`Deformation.representableMorphismFormalObjectEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/RepresentableMorphism/FormalObjectEquivalence.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/RepresentableMorphism/FormalObjectEquivalence.lean#L70).

> Morphisms from the restriction of the functor represented by `R` to a category
> cofibered in groupoids are canonically equivalent to formal objects over `R`.

```lean
public noncomputable def representableMorphismFormalObjectEquivalence
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (R : CompleteLocalAlgCat.{u, v, w} Λ k) :
    RepresentableMorphismFormalObjectEquivalence p R
```

## Tag 06SL, a remark

[Tag 06SL](https://stacks.math.columbia.edu/tag/06SL) in the Stacks Project.

**`Deformation.associatedMorphism_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/AssociatedMorphismMap.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/AssociatedMorphismMap.lean#L193). The attribute's comment: “existence and component square”.

> A morphism of formal objects gives the canonical 2-cell between the
> associated morphisms of restricted representable categories. Its component
> at an Artinian point is characterized by the square with the corresponding
> level map of formal objects.

```lean
public theorem associatedMorphism_map
    (hp : IsCofiberedInGroupoids p)
    {ξ η : FormalObject p} (a : ξ ⟶ η)
    (pushforwards : ChosenPushforwards p) :
    let f := restrictedRepresentableMap a.base
    let X := associatedMorphism hp ξ pushforwards
    let Y := associatedMorphism hp η pushforwards
    ∃ τ : BasedFunctor.comp f X.toBasedFunctor ≅ Y.toBasedFunctor,
      ∀ α, ∃ h : X.level (f.obj α) = Y.level α,
        X.pointInclusion (f.obj α) ≫ τ.hom.app α =
          a.app (X.level (f.obj α)) ≫
            eqToHom (congrArg η.level h) ≫ Y.pointInclusion α
```

**`Deformation.associatedMorphism_map_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/AssociatedMorphismMap.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/AssociatedMorphismMap.lean#L413). The attribute's comment: “uniqueness”.

> The commuting square with the level map determines the canonical
> Yoneda 2-cell uniquely.

```lean
public theorem associatedMorphism_map_unique
    (hp : IsCofiberedInGroupoids p)
    {ξ η : FormalObject p} (a : ξ ⟶ η)
    (pushforwards : ChosenPushforwards p) :
    let f := restrictedRepresentableMap a.base
    let X := associatedMorphism hp ξ pushforwards
    let Y := associatedMorphism hp η pushforwards
    ∀ (τ σ : BasedFunctor.comp f X.toBasedFunctor ≅ Y.toBasedFunctor),
      (∀ α, ∃ h : X.level (f.obj α) = Y.level α,
        X.pointInclusion (f.obj α) ≫ τ.hom.app α =
          a.app (X.level (f.obj α)) ≫
            eqToHom (congrArg η.level h) ≫ Y.pointInclusion α) →
      (∀ α, ∃ h : X.level (f.obj α) = Y.level α,
        X.pointInclusion (f.obj α) ≫ σ.hom.app α =
          a.app (X.level (f.obj α)) ≫
            eqToHom (congrArg η.level h) ≫ Y.pointInclusion α) →
      τ = σ
```

## Tag 06HD, a remark

[Tag 06HD](https://stacks.math.columbia.edu/tag/06HD) in the Stacks Project.

**`Deformation.ProrepresentableMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean#L82). The attribute's comment: “the data equivalent to a formal object”.

> **Stacks 06HD.** A prorepresentable functor on `𝒞_Λ` together with a morphism from its
> category of elements to a category cofibered over `𝒞_Λ`. This is the data Stacks 06HD
> exhibits as equivalent to a formal object.

```lean
structure ProrepresentableMorphism (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
```

**`Deformation.ProrepresentableMorphism.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean#L107). The attribute's comment: “morphisms of the data”.

> **Stacks 06HD.** A morphism of prorepresentable pairs: a natural transformation of the
> functors in the Yoneda direction, together with a morphism over `𝒞_Λ` from the restriction of
> the source's morphism along it to the target's morphism.

```lean
structure Hom {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (X Y : ProrepresentableMorphism p)
```

**`Deformation.restrictedCoyonedaMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean#L149). The attribute's comment: “Yoneda for the restricted representable functors”.

> **Stacks 06HD.** Yoneda for `𝒞_Λ`: precomposition is a bijection from maps `R ⟶ S` of
> complete local algebras onto natural transformations of the restricted representable functors
> in the opposite direction. The inverse reads off the compatible system of quotient points
> determined by a natural transformation and uses the completion description of Stacks 06HE.

```lean
theorem restrictedCoyonedaMap_bijective (R S : CompleteLocalAlgCat.{u, v, w} Λ k) :
    Function.Bijective (restrictedCoyonedaMap (R := R) (S := S))
```

**`Deformation.formalObjectsProrepresentableMorphismEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/ProrepresentableMorphism.lean#L422). The attribute's comment: “the equivalence with formal objects”.

> **Stacks 06HD.** Spelling out Stacks 06HC: the prorepresentable pairs over `p` carry a
> category structure whose morphisms are `ProrepresentableMorphism.Hom`, and the category of
> formal objects of `p` is equivalent to it. The hom equivalence is for the total categories, so
> it pins down the morphisms between pairs with *different* prorepresentable functors, not only
> those over a fixed one.

```lean
theorem formalObjectsProrepresentableMorphismEquivalence
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (hp : IsCofiberedInGroupoids p) :
    ∃ c : Category (ProrepresentableMorphism p),
      letI := c
      c.Hom = (fun X Y => ProrepresentableMorphism.Hom X Y) ∧
      Nonempty (FormalObject p ≌ ProrepresentableMorphism p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.7, Tag 06H2](https://stacks.math.columbia.edu/tag/06H2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
