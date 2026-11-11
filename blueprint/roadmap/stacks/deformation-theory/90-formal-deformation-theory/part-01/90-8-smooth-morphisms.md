---
declaration: section
origin: cited
lean: Deformation.IsSmooth, Deformation.isSmooth_of_lifts_smallExtensions, Deformation.pushforwardFunctorsFormTwoCommutativeSquare, Deformation.inducedFunctorToPullback, Deformation.essSurj_inducedFunctorToPullback_of_isSmooth, Deformation.exists_lift_of_inducedFunctorToPullback_essSurj, Deformation.isSmooth_iff_inducedFunctorToPullback_essSurj, Deformation.isSmooth_iff_inducedFunctorToPullback_essSurj_smallExtension
statement: formalized
proof: formalized
---

# 90.8 Smooth morphisms

Section 90.8 of the Stacks Project, [Tag 06HF](https://stacks.math.columbia.edu/tag/06HF). 11 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06HG, a definition

[Tag 06HG](https://stacks.math.columbia.edu/tag/06HG) in the Stacks Project.

**`Deformation.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Basic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Basic.lean#L102). References: SGA 7 VI (2.1), “smooth”.

> A morphism of categories over `\mathcal C_\Lambda` is smooth if every
> lifting problem over a surjective map `B \to A` has a compatible solution over
> `B`.

```lean
public abbrev IsSmooth {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ
  k)} {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, v, w} Λ k)} (φ : BasedFunctor 𝓕 𝓖) : Prop
```

## Tag 06HH, a lemma

[Tag 06HH](https://stacks.math.columbia.edu/tag/06HH) in the Stacks Project.

**`Deformation.isSmooth_of_lifts_smallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SmoothMorphisms.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SmoothMorphisms.lean#L173). References: SGA 7 VI (2.2(a)), “(iii) => (i)”.

> For a morphism of categories cofibered in groupoids, the lifting property
> for small extensions implies the lifting property for every surjective morphism,
> and hence smoothness.

```lean
theorem isSmooth_of_lifts_smallExtensions
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p)
    (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖)
    (h : ∀ ⦃B A : ArtinianLocalAlgCat.{u, v, w} Λ k⦄ (f : B ⟶ A),
      IsSmallExtension (CommRingCat.ofHom f.hom.toRingHom) →
        ∀ (y : 𝓖.obj) (x : 𝓕.obj) (g : y ⟶ φ.obj x),
          𝓖.p.IsHomLift f g →
            ∃ (x' : 𝓕.obj) (lift : x' ⟶ x) (a : φ.obj x' ⟶ y),
              𝓕.p.IsHomLift f lift ∧
                𝓖.p.IsHomLift (𝟙 B) a ∧ φ.map lift = a ≫ g) :
    IsSmooth φ
```

## Tag 06HI, a remark

[Tag 06HI](https://stacks.math.columbia.edu/tag/06HI) in the Stacks Project.

**`Deformation.pushforwardFunctorsFormTwoCommutativeSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Pushforward.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Pushforward.lean#L493). The attribute's comment: “pushforward\_square”.

> Chosen pushforwards along an arrow in the base give functors between the
> fibres, and a morphism of categories cofibered in groupoids intertwines these
> functors up to a natural isomorphism.

```lean
public theorem pushforwardFunctorsFormTwoCommutativeSquare
    {C : Type uC} [Category.{vC} C]
    {F : Type uF} [Category.{vF} F] {G : Type uG} [Category.{vG} G]
    (pF : F ⥤ C) (pG : G ⥤ C)
    (hG : IsCofiberedInGroupoids pG)
    (φ : F ⥤ G) (hφ : φ ⋙ pG = pF)
    {B A : C} {f : B ⟶ A}
    (PF : PushforwardChoice pF f) (PG : PushforwardChoice pG f) :
    Nonempty (PushforwardSquare φ hφ PF PG)
```

**`Deformation.inducedFunctorToPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Pushforward.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Pushforward.lean#L527). The attribute's comment: “induced\_functor”. References: SGA 7 VI (2.6(b)), “induced functor to 2-fp”.

> The functor from the source fibre to the categorical pullback induced by a
> chosen two-commutative pushforward square.

```lean
public def inducedFunctorToPullback
    {C : Type uC} [Category.{vC} C]
    {F : Type uF} [Category.{vF} F] {G : Type uG} [Category.{vG} G]
    {pF : F ⥤ C} {pG : G ⥤ C} {φ : F ⥤ G} {hφ : φ ⋙ pG = pF}
    {B A : C} {f : B ⟶ A}
    {PF : PushforwardChoice pF f}
    {PG : PushforwardChoice pG f}
    (Q : PushforwardSquare φ hφ PF PG) :
    pF.Fiber B ⥤
      Limits.CategoricalPullback
        (Functor.Fiber.inducedFunctor (p := pG) (S := A)
          (F := Functor.Fiber.fiberInclusion (p := pF) (S := A) ⋙ φ)
          (by simpa only [Functor.assoc, hφ] using
            (Functor.Fiber.fiberInclusion_comp_eq_const (p := pF) (S := A))))
        Q.target.toFunctor
```

**`Deformation.essSurj_inducedFunctorToPullback_of_isSmooth`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean#L90). The attribute's comment: “smooth\_iff\_essSurj”.

> **Stacks Project, Tag 06HI.** For a smooth morphism of categories cofibered in groupoids,
> the functor to the 2-fibre product determined by any choice of pushforwards along a surjection
> of the base is essentially surjective.

```lean
public lemma essSurj_inducedFunctorToPullback_of_isSmooth
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) (hsm : IsSmooth φ)
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A)
    (hf : Function.Surjective f.hom)
    (PF : PushforwardChoice 𝓕.p f) (PG : PushforwardChoice 𝓖.p f) :
    (inducedFunctorToPullback
      (pushforwardSquareOfChoices 𝓕.p 𝓖.p h𝓖 φ.toFunctor φ.w PF PG)).EssSurj
```

**`Deformation.exists_lift_of_inducedFunctorToPullback_essSurj`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean#L157). The attribute's comment: “smooth\_iff\_essSurj”. References: SGA 7 VI (2.6(b)), “The 'if' direction”.

> **Stacks Project, Tag 06HI.** If the functor to the 2-fibre product determined by some
> choice of pushforwards along an arrow `f` of the base is essentially surjective, then every
> lifting problem over `f` has a compatible solution.

```lean
public lemma exists_lift_of_inducedFunctorToPullback_essSurj
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖)
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A)
    (hes : ∀ (PF : PushforwardChoice 𝓕.p f) (PG : PushforwardChoice 𝓖.p f),
      (inducedFunctorToPullback
        (pushforwardSquareOfChoices 𝓕.p 𝓖.p h𝓖 φ.toFunctor φ.w PF PG)).EssSurj)
    (y : 𝓖.obj) (x : 𝓕.obj) (g : y ⟶ φ.obj x) (hg : 𝓖.p.IsHomLift f g) :
    ∃ (x' : 𝓕.obj) (lift : x' ⟶ x) (a : φ.obj x' ⟶ y),
      𝓕.p.IsHomLift f lift ∧ 𝓖.p.IsHomLift (𝟙 B) a ∧ φ.map lift = a ≫ g
```

**`Deformation.isSmooth_iff_inducedFunctorToPullback_essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean#L210). The attribute's comment: “smooth\_iff\_essSurj”.

> **Stacks Project, Tag 06HI.** A morphism of categories cofibered in groupoids over `𝒞_Λ`
> is smooth if and only if, for every surjection `B → A` of the base and every choice of
> pushforwards along it, the functor `𝓕(B) ⟶ 𝓕(A) ×_{𝓖(A)} 𝓖(B)` determined by those choices is
> essentially surjective.

```lean
public theorem isSmooth_iff_inducedFunctorToPullback_essSurj
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) :
    IsSmooth φ ↔
      ∀ ⦃B A : ArtinianLocalAlgCat.{u, v, w} Λ k⦄ (f : B ⟶ A),
        Function.Surjective f.hom →
        ∀ (PF : PushforwardChoice 𝓕.p f) (PG : PushforwardChoice 𝓖.p f),
          (inducedFunctorToPullback
            (pushforwardSquareOfChoices 𝓕.p 𝓖.p h𝓖 φ.toFunctor φ.w PF PG)).EssSurj
```

**`Deformation.isSmooth_iff_inducedFunctorToPullback_essSurj_smallExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/PushforwardSmooth.lean#L227). The attribute's comment: “smooth\_iff\_essSurj\_smallExtension”.

> **Stacks Project, Tag 06HI.** The same equivalence, tested only on small extensions: by
> Tag 06HH the lifting property for small extensions already implies smoothness.

```lean
public theorem isSmooth_iff_inducedFunctorToPullback_essSurj_smallExtension
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) :
    IsSmooth φ ↔
      ∀ ⦃B A : ArtinianLocalAlgCat.{u, v, w} Λ k⦄ (f : B ⟶ A),
        IsSmallExtension (CommRingCat.ofHom f.hom.toRingHom) →
        ∀ (PF : PushforwardChoice 𝓕.p f) (PG : PushforwardChoice 𝓖.p f),
          (inducedFunctorToPullback
            (pushforwardSquareOfChoices 𝓕.p 𝓖.p h𝓖 φ.toFunctor φ.w PF PG)).EssSurj
```

## Tag 06HJ, a remark

[Tag 06HJ](https://stacks.math.columbia.edu/tag/06HJ) in the Stacks Project.

**`Deformation.isSmooth_elementsBasedFunctor_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SmoothMorphisms.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SmoothMorphisms.lean#L239).

> Smoothness of a morphism between categories of elements is equivalent to
> surjectivity of the usual map to the fibre product for every surjection in
> `𝒞_Λ`.

```lean
theorem isSmooth_elementsBasedFunctor_iff
    {F G : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type t} (α : F ⟶ G) :
    IsSmooth (elementsBasedFunctor α) ↔
      ∀ ⦃B A : ArtinianLocalAlgCat.{u, v, w} Λ k⦄ (f : B ⟶ A),
        Function.Surjective f.hom →
          ∀ (xA : F.obj A) (yB : G.obj B),
            α.app A xA = G.map f yB →
            ∃ xB : F.obj B, F.map f xB = xA ∧ α.app B xB = yB
```

## Tag 06HK, a remark

[Tag 06HK](https://stacks.math.columbia.edu/tag/06HK) in the Stacks Project.

**`Deformation.isSmooth_toIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/IsomorphismClasses.lean#L425).

> The canonical morphism from a category cofibered in groupoids to its associated functor of
> isomorphism classes is smooth.

```lean
public theorem isSmooth_toIsomorphismClasses
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ k))
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p) :
    IsSmooth (toIsomorphismClasses 𝓕 h𝓕)
```

## Tag 06HL, a lemma

[Tag 06HL](https://stacks.math.columbia.edu/tag/06HL) in the Stacks Project.

**`Deformation.restrictedRepresentableMap_isSmooth_iff_isPowerSeriesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/PowerSeries.lean, line 1001](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/PowerSeries.lean#L1001). The attribute's comment: “smooth if and only if a power series ring”. References: SGA 7 VI (2.2(c)); SGA 1 III (1.5), “complete local case”.

> The morphism between restricted representable categories induced by `f : R ⟶ S` is smooth
> if and only if `f` exhibits `S` as a formal power series ring in finitely many variables over
> `R`.

```lean
public theorem restrictedRepresentableMap_isSmooth_iff_isPowerSeriesOver
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R ⟶ S) :
    IsSmooth (restrictedRepresentableMap f) ↔ IsPowerSeriesOver f
```

## Tag 06HM, a lemma

[Tag 06HM](https://stacks.math.columbia.edu/tag/06HM) in the Stacks Project.

**`Deformation.isSmooth_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Basic.lean#L122). The attribute's comment: “smooth\_comp”. References: SGA 7 VI (2.3), “(a)”.

> The composite of two smooth morphisms of categories over
> `\mathcal C_\Lambda` is smooth.

```lean
public theorem isSmooth_comp
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓗 : BasedCategory.{v₃, u₃} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    (φ : BasedFunctor 𝓕 𝓖) (ψ : BasedFunctor 𝓖 𝓗)
    (hφ : IsSmooth φ) (hψ : IsSmooth ψ) :
    IsSmooth (BasedFunctor.comp φ ψ)
```

**`Deformation.isSmooth_twoFibreProductSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Basic.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Basic.lean#L184). The attribute's comment: “smooth\_base\_change”.

> A base change of a smooth morphism of categories cofibered in groupoids is smooth.

```lean
public theorem isSmooth_twoFibreProductSnd
    {𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓖 : BasedCategory.{vG, uG} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓖' : BasedCategory.{vG', uG'} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖) (θ : BasedFunctor 𝓖' 𝓖)
    (hφ : IsSmooth φ) : IsSmooth (twoFibreProductSnd φ θ)
```

**`Deformation.isSmooth_of_essSurj_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Basic.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Basic.lean#L249). The attribute's comment: “smooth\_of\_essentially\_surjective\_smooth\_comp”. References: SGA 7 VI (2.3), “(b)”.

> If the first of two morphisms of categories cofibered in groupoids is
> essentially surjective and their composite is smooth, then the second morphism
> is smooth.

```lean
public theorem isSmooth_of_essSurj_comp
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓗 : BasedCategory.{v₃, u₃} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p)
    (φ : BasedFunctor 𝓕 𝓖) (ψ : BasedFunctor 𝓖 𝓗) [φ.toFunctor.EssSurj]
    (h : IsSmooth (BasedFunctor.comp φ ψ)) : IsSmooth ψ
```

## Tag 06HN, a lemma

[Tag 06HN](https://stacks.math.columbia.edu/tag/06HN) in the Stacks Project.

**`Deformation.essSurj_of_isSmooth_of_fiber_essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/EssentiallySurjective.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/EssentiallySurjective.lean#L63). The attribute's comment: “essentially\_surjective”.

> A smooth morphism of categories over `\mathcal C_\Lambda` with cofibered
> target is essentially surjective whenever its special-fibre functor is.

```lean
public theorem essSurj_of_isSmooth_of_fiber_essSurj
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, w, w} Λ k)}
    (φ : BasedFunctor 𝓕 𝓖)
    (h𝓖 : IsCofiberedInGroupoids 𝓖.p)
    (hφ : IsSmooth φ)
    (h₀ : (fiberFunctor φ (residueFieldObject Λ k)).EssSurj) :
    φ.toFunctor.EssSurj
```

**`Deformation.completionMap_essSurj_of_isSmooth_of_fiber_essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/EssentiallySurjective.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/EssentiallySurjective.lean#L278). The attribute's comment: “completion\_essentially\_surjective”.

> A smooth morphism, essentially surjective over the residue field, is
> essentially surjective after completion.

```lean
public theorem completionMap_essSurj_of_isSmooth_of_fiber_essSurj
    {F : Type uF} [Category.{vF} F] {G : Type uG} [Category.{vG} G]
    {p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    {q : G ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (φ : BasedFunctor (BasedCategory.ofFunctor p) (BasedCategory.ofFunctor q))
    (hq : IsCofiberedInGroupoids q)
    (hφ : IsSmooth φ)
    (h₀ : (fiberFunctor φ (residueFieldObject Λ k)).EssSurj) :
    (completionMap φ).toFunctor.EssSurj
```

## Tag 06HR, a definition

[Tag 06HR](https://stacks.math.columbia.edu/tag/06HR) in the Stacks Project.

**`Deformation.IsVersal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Smooth/Versal.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Smooth/Versal.lean#L94). References: SGA 7 VI (1.19), “(1)”; SGA 7 VI (1.9), “versal formal object”.

> A formal object is versal when its associated morphism from the represented
> functor is smooth, independently of the auxiliary pushforward choices.

```lean
public abbrev IsVersal (hp : IsCofiberedInGroupoids p)
    (ξ : FormalObject p) : Prop
```

## Tag 06HS, a remark

[Tag 06HS](https://stacks.math.columbia.edu/tag/06HS) in the Stacks Project.

**`Deformation.isVersal_iff_lifts_artinian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/VersalLifting.lean, line 716](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/VersalLifting.lean#L716). The attribute's comment: “lifting criterion”. References: SGA 7 VI (2.2(d)), “lifting criterion”; SGA 7 VI (1.9), “versal formal object”; SGA 7 VI (1.19), “(1)”.

> Versality is equivalent to solving every lifting triangle in the completion
> whose lower arrow is a surjective map of Artinian local algebras.

```lean
public theorem isVersal_iff_lifts_artinian
    (hp : IsCofiberedInGroupoids p) (ξ : FormalObject p) :
    IsVersal hp ξ ↔
      ∀ {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A),
        Function.Surjective f.hom →
          ∀ {y x : FormalObject p} (g : y ⟶ x),
            (FormalObject.projection (p := p)).IsHomLift
              (artinianToComplete.map f) g →
              ∀ (a : ξ ⟶ x), ∃ b : ξ ⟶ y, b ≫ g = a
```

**`Deformation.isVersal_iff_lifts_smallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/VersalLifting.lean, line 745](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/VersalLifting.lean#L745). The attribute's comment: “small-extension criterion”.

> In the intrinsic lifting criterion, it suffices to test small extensions
> of Artinian local algebras.

```lean
public theorem isVersal_iff_lifts_smallExtensions
    (hp : IsCofiberedInGroupoids p) (ξ : FormalObject p) :
    IsVersal hp ξ ↔
      ∀ {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A),
        InfinitesimalLifting.IsSmallExtension
          (CommRingCat.ofHom f.hom.toRingHom) →
          ∀ {y x : FormalObject p} (g : y ⟶ x),
            (FormalObject.projection (p := p)).IsHomLift
              (artinianToComplete.map f) g →
              ∀ (a : ξ ⟶ x), ∃ b : ξ ⟶ y, b ≫ g = a
```

**`Deformation.isSmooth_associatedMorphism_iff_isVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/FormalObject/VersalLifting.lean, line 812](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/FormalObject/VersalLifting.lean#L812). The attribute's comment: “independence of pushforwards”. References: SGA 7 VI (2.2(d)), “smooth ⟺ versal”.

> Smoothness of the morphism associated to a formal object is independent of
> the choices of pushforwards used to construct that morphism.

```lean
public theorem isSmooth_associatedMorphism_iff_isVersal
    (hp : IsCofiberedInGroupoids p) (ξ : FormalObject p)
    (pushforwards : ChosenPushforwards p) :
    IsSmooth (associatedMorphism hp ξ pushforwards).toBasedFunctor ↔
      IsVersal hp ξ
```

## Tag 06HT, a lemma

[Tag 06HT](https://stacks.math.columbia.edu/tag/06HT) in the Stacks Project.

**`Deformation.nonempty_hom_of_isVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Formal/VersalObject/MapsToFormalObject.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Formal/VersalObject/MapsToFormalObject.lean#L306).

> A versal formal object admits a morphism to every formal object.

```lean
public theorem nonempty_hom_of_isVersal (hp : IsPredeformationCategory p)
    (ξ η : FormalObject p) (hξ : IsVersal hp.cofibered ξ) :
    Nonempty (ξ ⟶ η)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.8, Tag 06HF](https://stacks.math.columbia.edu/tag/06HF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
