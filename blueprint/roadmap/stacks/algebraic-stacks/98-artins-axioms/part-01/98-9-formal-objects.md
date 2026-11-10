---
declaration: section
origin: cited
lean: Deformation.Artin.FormalObject.mapFunctor, Deformation.Artin.FormalObject, Deformation.Artin.FormalObject.Hom, Deformation.Artin.FormalObject.exists_predeformationFormalObject, Deformation.Artin.exists_formalObject_lift, Deformation.Artin.approximationFunctorData, Deformation.Artin.FormalObject.IsEffective, Deformation.Artin.isEquivalence_approximationFunctor_algebraicStacks
statement: formalized
proof: formalized
---

# 98.9 Formal objects

Section 98.9 of the Stacks Project, [Tag 07X3](https://stacks.math.columbia.edu/tag/07X3). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07X3, the section

[Tag 07X3](https://stacks.math.columbia.edu/tag/07X3) in the Stacks Project.

**`Deformation.Artin.FormalObject.mapFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L49). The attribute's comment: “a 1-morphism induces a functor between categories of formal objects”.

> The functor between categories of formal objects induced by a `1`-morphism of categories
> fibred in groupoids: every level and every level map is pushed forward.

```lean
def FormalObject.mapFunctor : FormalObject B S hS 𝒳.val.p ⥤ FormalObject B S hS 𝒴.val.p
```

Declarations registered for the tag:

- [`Deformation.Artin.FormalObject`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L147), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L61) (StacksFrontier): “formal objects”.
- [`Deformation.Artin.FormalObject.Hom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L170), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L62) (StacksFrontier): “morphisms of formal objects”.
- [`Deformation.Artin.FormalObject.exists_predeformationFormalObject`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/Predeformation.lean#L326), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L63) (StacksFrontier): “the formal object of a predeformation category”.
- [`Deformation.Artin.exists_formalObject_lift`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/SmoothLift.lean#L249), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L65) (StacksFrontier): “lifting formal objects along a formally smooth 1-morphism”.
- [`Deformation.Artin.approximationFunctorData`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L1049), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L67) (StacksFrontier): “the functor to formal objects”.
- [`Deformation.Artin.FormalObject.IsEffective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L1253), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L68) (StacksFrontier): “effective formal objects”.
- [`Deformation.Artin.isEquivalence_approximationFunctor_algebraicStacks`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/ApproximationEssSurj.lean#L265), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Artin/FormalObjectsSection.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObjectsSection.lean#L69) (StacksFrontier): “for an algebraic stack every formal object is effective”.

## Tag 07X4, a definition

[Tag 07X4](https://stacks.math.columbia.edu/tag/07X4) in the Stacks Project.

**`Deformation.Artin.FormalObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L147). The attribute's comment: “formal objects”.

> A formal object of a category over the big fppf site of `S`.

```lean
public structure FormalObject {F : Type v} [Category.{w} F]
    (p : F ⥤ BigFppfOver B S hS)
```

**`Deformation.Artin.FormalObject.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L170). The attribute's comment: “morphisms”.

> A compatible family of morphisms between formal objects.

```lean
public structure Hom (X Y : FormalObject B S hS p)
```

**`Deformation.Artin.FormalObject.Hom.baseMapData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L214). The attribute's comment: “the induced map of complete bases”.

> A compatible family induces a unique map between its complete local bases.

```lean
public noncomputable def Hom.baseMapData {X Y : FormalObject B S hS p} (f : Hom X Y) :
    {a : Spec (.of X.base.R) ⟶ Spec (.of Y.base.R) //
      f.IsBaseMap a ∧ ∀ b, f.IsBaseMap b → b = a}
```

## Tag 0CXH, a remark

[Tag 0CXH](https://stacks.math.columbia.edu/tag/0CXH) in the Stacks Project.

**`Deformation.Artin.FormalObject.exists_predeformationFormalObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/Predeformation.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/Predeformation.lean#L326).

> A formal object of a category over the big fppf site of `S` gives a formal object of
> the predeformation category of its closed fibre, with the same levels, the same transition
> maps and the same complete local base.

```lean
theorem FormalObject.exists_predeformationFormalObject
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : Type v} [Category.{w} F]
    (p : F ⥤ BigFppfOver B S hS)
    (ξ : FormalObject B S hS p)
    (Λ : Type u) [CommRing Λ] [Algebra Λ ξ.base.R]
    (iΛ : Spec (.of Λ) ⟶ S)
    (hR : Spec.map (CommRingCat.ofHom (algebraMap Λ ξ.base.R)) ≫ iΛ =
      ξ.base.toS) :
    let R := ξ.base.R
    letI : CommRing R := ξ.base.commRing
    letI : IsLocalRing R := ξ.base.localRing
    let k := ResidueField R
    letI : Field k := ResidueField.field R
    letI : Algebra Λ k := ResidueField.algebra R
    let q : F ⥤ Over S := p ⋙ Over.post B.inclusion
    ∃ hx₀ : q.obj (ξ.level 0) = Over.mk
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ),
      let C := predeformationCategory iΛ q (ξ.level 0) hx₀
      letI : Category C.carrier := C.category
      ∃ η : Deformation.FormalObject C.projection,
        η.base = ξ.completeLocalBase Λ ∧
          (∀ n, (C.objects (η.level n)).point = ξ.level n) ∧
          (∀ n, HEq (C.objects (η.level n)).arrow
            (FormalObject.closedPointArrow ξ n)) ∧
          (∀ n, HEq (C.morphisms (η.level (n + 1)) (η.level n)
            (η.transition n)).arrow (ξ.transition n))
```

## Tag 07X5, a lemma

[Tag 07X5](https://stacks.math.columbia.edu/tag/07X5) in the Stacks Project.

**`Deformation.Artin.exists_formalObject_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/SmoothLift.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/SmoothLift.lean#L249).

> If `F : 𝒳 ⟶ 𝒴` is formally smooth on objects, every formal object `η` of `𝒴` whose
> closed-point level lifts to `𝒳` is, up to isomorphism, the image of a formal object of `𝒳` over
> the same complete local base and with the given closed-point lift.

```lean
public theorem exists_formalObject_lift
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p)
    (η : FormalObject B S hS 𝒴.val.p)
    (ξ₀ : 𝒳.val.p.Fiber (truncationOver B S hS η.base η.contains 0))
    (hξ₀ : (Functor.Fiber.mapOfComp 𝒳.val.p 𝒴.val.p (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
      (truncationOver B S hS η.base η.contains 0)).obj ξ₀ ≅
        ⟨η.level 0, η.level_eq 0⟩) :
    ∃ ξ : FormalObject B S hS 𝒳.val.p,
      ξ.base = η.base ∧ ξ.level 0 = ξ₀.1 ∧
        Nonempty (FormalObject.map B S hS 𝒳 𝒴 p ξ ≅ η)
```

## Tag 07X6, an equation

[Tag 07X6](https://stacks.math.columbia.edu/tag/07X6) in the Stacks Project.

**`Deformation.Artin.approximationFunctorData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject.lean, line 1049](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L1049).

> The canonical functor taking an object over a complete local ring to its
> compatible system of restrictions to the infinitesimal thickenings.

```lean
public noncomputable def approximationFunctorData
    (hp : p.IsFiberedInGroupoids) :
    {G : CompleteLocalObjects B S hS p ⥤ FormalObject B S hS p //
      IsApproximationFunctor B S hS p G}
```

## Tag 07X7, a definition

[Tag 07X7](https://stacks.math.columbia.edu/tag/07X7) in the Stacks Project.

**`Deformation.Artin.FormalObject.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject.lean, line 1253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject.lean#L1253).

> A formal object is effective if it comes, up to isomorphism, from an
> object over its complete local base by approximation.

```lean
public abbrev IsEffective (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {F : Type v} [Category.{w} F]
    (p : F ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids)
    (ξ : FormalObject B S hS p) : Prop
```

## Tag 07X8, a lemma

[Tag 07X8](https://stacks.math.columbia.edu/tag/07X8) in the Stacks Project.

**`Deformation.Artin.isEquivalence_approximationFunctor_algebraicStacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/ApproximationEssSurj.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/ApproximationEssSurj.lean#L265).

> **Stacks 07X8.** Let `𝒳` be an algebraic stack over a scheme `S`. The functor (Stacks 07X6)
> from objects of `𝒳` over spectra of Noetherian complete local `S`-algebras with residue field of
> finite type over `S` (and morphisms inducing local homomorphisms) to formal objects of `𝒳`,
> which restricts an object to the infinitesimal thickenings of the closed point, is an
> equivalence: full and faithful (`Deformation.Artin.full_approximationFunctor_algebraicStacks`,
> `Deformation.Artin.faithful_approximationFunctor_algebraicStacks`) and essentially surjective
> (`Deformation.Artin.essSurj_approximationFunctor_algebraicStacks`). The scheme `S` is not
> assumed locally Noetherian.

```lean
theorem isEquivalence_approximationFunctor_algebraicStacks
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) :
    (approximationFunctor B S hS 𝒳.val.val.p 𝒳.val.property).IsEquivalence
```

**`Deformation.Artin.faithful_approximationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/ApproximationRepresentable.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/ApproximationRepresentable.lean#L440). The attribute's comment: “faithfulness of the functor only, and only for a category fibred in groupoids whose structure functor is faithful, i.e. one fibred in setoids, with the faithfulness of that functor as an added hypothesis the source lacks; this covers the category represented by an object of the site, but neither fullness, nor essential surjectivity, nor a general algebraic stack”.

> **Stacks 07X8, faithfulness of the functor (Stacks 07X6)**, for a category fibred in
> groupoids whose structure functor is faithful, i.e. one fibred in setoids. This covers the
> category fibred in groupoids represented by an object of the big fppf site over `S`, i.e.
> by a scheme over `S`, which is Case I of the source proof.
>
> Faithfulness of `p` is a hypothesis the source does not impose; it holds exactly when `p`
> is fibred in setoids, so it excludes a general algebraic stack. The source's hypothesis
> that `S` is locally Noetherian is, on the other hand, not needed here.

```lean
public theorem faithful_approximationFunctor [p.Faithful]
    (hp : p.IsFiberedInGroupoids) :
    (approximationFunctor B S hS p hp).Faithful
```

**`Deformation.Artin.full_approximationFunctor_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/ApproximationRepresentable.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/ApproximationRepresentable.lean#L665). The attribute's comment: “fullness of the functor only, and only for the category fibred in groupoids represented by an object of the big fppf site over S, i.e. by a scheme over S; this is half of Case I of the source proof, and covers neither essential surjectivity nor the algebraic space of Case II nor the general algebraic stack of Case III”.

> **Stacks 07X8, fullness of the functor (Stacks 07X6)**, for the category fibred in
> groupoids represented by an object `Xo` of the big fppf site over `S`, i.e. by a scheme
> over `S`. This is the fullness half of Case I of the source proof.
>
> The source's hypothesis that `S` is locally Noetherian is not needed.

```lean
public theorem full_approximationFunctor_representable (Xo : BigFppfOver B S hS) :
    (approximationFunctor B S hS (Over.forget Xo)
      (Functor.IsFiberedInGroupoids.over_forget Xo)).Full
```

## Tag 07X9, a lemma

[Tag 07X9](https://stacks.math.columbia.edu/tag/07X9) in the Stacks Project.

**`Deformation.Artin.isEquivalence_approximationFunctor_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/ApproximationTwoFibreProduct.lean, line 905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FormalObject/ApproximationTwoFibreProduct.lean#L905).

> **Stacks 07X9.** The approximation equivalence is stable under 2-fibre products of
> categories fibred in groupoids over the big fppf site: if the approximation functor is an
> equivalence for `pX`, `pY` and `pZ`, then it is an equivalence for `pX ×_pY pZ`.

```lean
public theorem isEquivalence_approximationFunctor_twoFibreProduct
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type vX} [Category.{wX} X]
    {Y : Type vY} [Category.{wY} Y]
    {Z : Type vZ} [Category.{wZ} Z]
    (pX : X ⥤ BigFppfOver B S hS)
    (pY : Y ⥤ BigFppfOver B S hS)
    (pZ : Z ⥤ BigFppfOver B S hS)
    (f : X ⥤ Y) (g : Z ⥤ Y)
    (hpX : pX.IsFiberedInGroupoids) (hpY : pY.IsFiberedInGroupoids)
    (hpZ : pZ.IsFiberedInGroupoids)
    (hf : f ⋙ pY = pX) (hg : g ⋙ pY = pZ)
    (hX : (approximationFunctor B S hS pX hpX).IsEquivalence)
    (hY : (approximationFunctor B S hS pY hpY).IsEquivalence)
    (hZ : (approximationFunctor B S hS pZ hpZ).IsEquivalence) :
    (approximationFunctor B S hS
      (TwoFibreProductOver.structureFunctor pX pZ pY f g)
      (TwoFibreProductOver.isFiberedInGroupoids pX pZ pY f g
        hpX hpZ hpY hf hg)).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.9, Tag 07X3](https://stacks.math.columbia.edu/tag/07X3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
