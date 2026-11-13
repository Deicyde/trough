---
declaration: section
origin: cited
lean: Deformation.Lift, Deformation.Lift.Hom, Deformation.LiftClasses, Deformation.Lift.over, Deformation.LiftClasses.over, Deformation.liftClassesEquivObjectsOver, Deformation.liftClassesTangentSpace, Deformation.liftClassesTangentSpace_naturality
statement: formalized
proof: formalized
---

# 90.17 Lifts of objects

Section 90.17 of the Stacks Project, [Tag 06JD](https://stacks.math.columbia.edu/tag/06JD). 9 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06JE, a definition

[Tag 06JE](https://stacks.math.columbia.edu/tag/06JE) in the Stacks Project.

**`Deformation.Lift`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L71). The attribute's comment: “objects”.

> The category of lifts of `x` along `f`. Its objects are arrows to `x` lying over `f`; its
> arrows are commuting triangles whose remaining side lies over the identity.

```lean
public structure Lift
    {C : Type u} [Category.{v} C] {F : Type uF} [Category.{vF} F]
    (p : F ⥤ C) {A' A : C} (f : A' ⟶ A) (x : p.Fiber A)
```

**`Deformation.Lift.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L86). The attribute's comment: “morphisms”.

> A morphism of lifts is a morphism over the identity which makes the triangle of
> lifting arrows commute.

```lean
public structure Lift.Hom
    {C : Type u} [Category.{v} C] {F : Type uF} [Category.{vF} F]
    {p : F ⥤ C} {A' A : C} {f : A' ⟶ A} {x : p.Fiber A}
    (a b : Lift p f x)
```

**`Deformation.LiftClasses`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L131). The attribute's comment: “the set of lifts”.

> The set of isomorphism classes of lifts of `x` along `f`.

```lean
public abbrev LiftClasses
    {C : Type u} [Category.{v} C] {F : Type uF} [Category.{vF} F]
    (p : F ⥤ C) {A' A : C} (f : A' ⟶ A) (x : p.Fiber A)
```

## Tag 06JF, a remark

[Tag 06JF](https://stacks.math.columbia.edu/tag/06JF) in the Stacks Project.

**`Deformation.Lift.over`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L141). The attribute's comment: “the category of lifts named by the source object”.

> The category of lifts of `x` to an object `A'` of the base category given together with
> its morphism to `A`: the lifts of `x` along that morphism, which the name leaves implicit.

```lean
public abbrev Lift.over
    {C : Type u} [Category.{v} C] {F : Type uF} [Category.{vF} F]
    (p : F ⥤ C) {A : C} (A' : Over A) (x : p.Fiber A)
```

**`Deformation.LiftClasses.over`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L149). The attribute's comment: “the set of lifts named by the source object”.

> The set of isomorphism classes of lifts of `x` to an object `A'` of the base category
> given together with its morphism to `A`, that morphism being left implicit.

```lean
public abbrev LiftClasses.over
    {C : Type u} [Category.{v} C] {F : Type uF} [Category.{vF} F]
    (p : F ⥤ C) {A : C} (A' : Over A) (x : p.Fiber A)
```

## Tag 06JG, a remark

[Tag 06JG](https://stacks.math.columbia.edu/tag/06JG) in the Stacks Project.

**`Deformation.liftClassesEquivObjectsOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/TangentSpaceOfLifts.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/TangentSpaceOfLifts.lean#L128). The attribute's comment: “lifts as localized isomorphism classes”.

> A lift of `x₀` along a square-zero augmentation is an object of the localized category over
> `x₀` in the source fibre, up to isomorphism.

```lean
public noncomputable def liftClassesEquivObjectsOver
    (hp : IsCofiberedInGroupoids p)
    {A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    (e : A ⟶ residueFieldObject Λ k)
    (x₀ : p.Fiber (residueFieldObject Λ k)) :
    let q := objectsOverFunctor p x₀.1
    let hq := (isPredeformationCategory_objectsOverFunctor p hp x₀).cofibered
    { comparison : LiftClasses p e x₀ ≃
        (isomorphismClasses (BasedCategory.ofFunctor q) hq).obj A //
      ∀ a : Lift p e x₀, comparison (ThinSkeleton.mk a) =
        classOf (BasedCategory.ofFunctor q) hq
          (⟨Over.mk a.hom,
            IsHomLift.domain_eq p e a.hom⟩ : q.Fiber A) }
```

**`Deformation.liftClassesTangentSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/TangentSpaceOfLifts.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/TangentSpaceOfLifts.lean#L227). The attribute's comment: “tangent-space tensor identification”.

> Under (S2), the lifts to `k[V]` are the tangent space of the category localized at `x₀`,
> tensored with `V`, as vector spaces.

```lean
public noncomputable def liftClassesTangentSpace
    (hp : IsCofiberedInGroupoids p)
    (hS2 : SchlessingerConditionS2 p)
    (x₀ : p.Fiber (residueFieldObject Λ k))
    (V : FGModuleCat.{w} k)
    (e : (squareZeroExtensionArtinian Λ k).obj V ⟶ residueFieldObject Λ k) :
    LiftTangentSpaceData p hp hS2 x₀ V e
```

**`Deformation.liftClassesTangentSpace_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/TangentSpaceOfLifts.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/TangentSpaceOfLifts.lean#L288). The attribute's comment: “naturality in the vector space”.

> The tensor identification of lifts commutes with every linear map of finite-dimensional vector
> spaces, using the induced map on localized lifts.

```lean
public theorem liftClassesTangentSpace_naturality
    (hp : IsCofiberedInGroupoids p)
    (hS2 : SchlessingerConditionS2 p)
    (x₀ : p.Fiber (residueFieldObject Λ k))
    (V W : FGModuleCat.{w} k)
    (eV : (squareZeroExtensionArtinian Λ k).obj V ⟶ residueFieldObject Λ k)
    (eW : (squareZeroExtensionArtinian Λ k).obj W ⟶ residueFieldObject Λ k)
    (f : V ⟶ W) :
    let q := objectsOverFunctor p x₀.1
    let hpq := isPredeformationCategory_objectsOverFunctor p hp x₀
    let H := isomorphismClasses (BasedCategory.ofFunctor q) hpq.cofibered
    let DV := liftClassesTangentSpace p hp hS2 x₀ V eV
    let DW := liftClassesTangentSpace p hp hS2 x₀ W eW
    letI : Fact (IsPredeformationCategory (BasedCategory.ofFunctor q).p) := ⟨hpq⟩
    letI : Fact (SchlessingerConditionS2 (Functor.Elements.π H)) := ⟨DV.associatedS2⟩
    letI : AddCommGroup (artinianTangentSpace Λ k H) :=
      associatedTangentSpaceAddCommGroupUnlifted (BasedCategory.ofFunctor q)
    letI : Module k (artinianTangentSpace Λ k H) :=
      associatedTangentSpaceModuleUnlifted (BasedCategory.ofFunctor q)
    ∀ z : TensorProduct k (artinianTangentSpace Λ k H) V,
      (liftClassesEquivObjectsOver p hp eW x₀).1
          (DW.equiv (TensorProduct.map
            (LinearMap.id : artinianTangentSpace Λ k H →ₗ[k]
              artinianTangentSpace Λ k H) f.hom.hom z)) =
        H.map ((squareZeroExtensionArtinian Λ k).map f)
          ((liftClassesEquivObjectsOver p hp eV x₀).1 (DV.equiv z))
```

## Tag 06JH, a remark

[Tag 06JH](https://stacks.math.columbia.edu/tag/06JH) in the Stacks Project.

**`Deformation.liftClassesProdEquivPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L698). The attribute's comment: “product\_bijection”.

> Isomorphism classes of lifts to a fibre product are in bijection with pairs of
> isomorphism classes of lifts to the two factors when one structural map is surjective.

```lean
public theorem liftClassesProdEquivPullback
    {Λ : Type*} {k : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat Λ k)
    (hRS : SatisfiesRS p)
    {A₁ A₂ A : ArtinianLocalAlgCat Λ k}
    {f₁ : A₁ ⟶ A} {f₂ : A₂ ⟶ A}
    (c : PullbackCone f₁ f₂) (hc : IsLimit c)
    (hsurj : Function.Surjective f₁.hom ∨ Function.Surjective f₂.hom)
    (x : p.Fiber A) :
    Nonempty (LiftProductEquiv p c x)
```

**`Deformation.liftClassesEquivOfFixedLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 950](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L950). The attribute's comment: “fixed\_lift\_bijection”.

> After fixing a lift over the first factor, pushing along the second projection gives
> a bijection from lifts of the fixed object to lifts over the second factor.

```lean
public theorem liftClassesEquivOfFixedLift
    {Λ : Type*} {k : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat Λ k)
    (hRS : SatisfiesRS p)
    {A₁ A₂ A : ArtinianLocalAlgCat Λ k}
    {f₁ : A₁ ⟶ A} {f₂ : A₂ ⟶ A}
    (c : PullbackCone f₁ f₂) (hc : IsLimit c)
    (hsurj : Function.Surjective f₁.hom ∨ Function.Surjective f₂.hom)
    (x : p.Fiber A) (a₁ : Lift p f₁ x) :
    Nonempty (FixedLiftEquiv p c x a₁)
```

**`Deformation.liftClassesEquivProdOfCompositePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 1047](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L1047). The attribute's comment: “composite\_square\_bijection”.

> Let `left` be a fibre square of a surjection `g : A₁' ⟶ A₁` and the first projection of
> `right`. Isomorphism classes of lifts of the source of `a₁` along `left.fst ≫ g` are in
> bijection with pairs of isomorphism classes of lifts of it along `g` and along `right.fst`.

```lean
public theorem liftClassesEquivProdOfCompositePullback
    {Λ : Type*} {k : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat Λ k)
    (hRS : SatisfiesRS p)
    {A₁' A₁ A₂ A : ArtinianLocalAlgCat Λ k}
    {f₁ : A₁ ⟶ A} {f₂ : A₂ ⟶ A} {g : A₁' ⟶ A₁}
    (right : PullbackCone f₁ f₂)
    (left : PullbackCone g right.fst)
    (hleft : IsLimit left)
    (hg : Function.Surjective g.hom)
    (x : p.Fiber A) (a₁ : Lift p f₁ x) :
    Nonempty (LiftClasses p (left.fst ≫ g) (liftSourceFiber a₁) ≃
      LiftClasses p g (liftSourceFiber a₁) ×
        LiftClasses p right.fst (liftSourceFiber a₁))
```

**`Deformation.liftClassesEquivOuterProdOfCompositePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Lift.lean, line 1071](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Lift.lean#L1071). The attribute's comment: “composite\_square\_bijection”.

> Let `right` be a fibre square of `f₁` and `f₂` with `f₁` surjective, and `left` a fibre
> square of a surjection `g : A₁' ⟶ A₁` and the first projection of `right`. Isomorphism classes
> of lifts of the source of `a₁` along `left.fst ≫ g` are in bijection with pairs of an
> isomorphism class of lifts of it along `g` and an isomorphism class of lifts of `x` along
> `f₂`.

```lean
public theorem liftClassesEquivOuterProdOfCompositePullback
    {Λ : Type*} {k : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat Λ k)
    (hRS : SatisfiesRS p)
    {A₁' A₁ A₂ A : ArtinianLocalAlgCat Λ k}
    {f₁ : A₁ ⟶ A} {f₂ : A₂ ⟶ A} {g : A₁' ⟶ A₁}
    (right : PullbackCone f₁ f₂)
    (hright : IsLimit right)
    (left : PullbackCone g right.fst)
    (hleft : IsLimit left)
    (hg : Function.Surjective g.hom)
    (hf₁ : Function.Surjective f₁.hom)
    (x : p.Fiber A) (a₁ : Lift p f₁ x) :
    Nonempty (LiftClasses p (left.fst ≫ g) (liftSourceFiber a₁) ≃
      LiftClasses p g (liftSourceFiber a₁) × LiftClasses p f₂ x)
```

## Tag 06JI, a lemma

[Tag 06JI](https://stacks.math.columbia.edu/tag/06JI) in the Stacks Project.

**`Deformation.liftAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean#L63). The attribute's comment: “action”.

> **Stacks Project, Tag 06JI.** The canonical additive action of tangent vectors tensored
> with the infinitesimal kernel on the classes of lifts.

```lean
public noncomputable def liftAction
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p)
    {A' A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    (f : A' ⟶ A) (hf : Function.Surjective f.hom)
    (hann : ∀ a : A', a ∈ maximalIdeal A' →
      ∀ i : RingHom.ker f.hom.toRingHom, a * (i : A') = 0)
    (x : 𝓕.p.Fiber A) :
    letI : Module k (RingHom.ker f.hom.toRingHom) := kernelModule f hann
    let hS2 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓕 h𝓕.predeformation.cofibered
      (schlessingerConditionS2_of_satisfiesRS h𝓕.satisfiesRS)
      (.inl h𝓕.predeformation)
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨h𝓕.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))) := ⟨hS2⟩
    AddAction
      (TensorProduct k
        (artinianTangentSpace Λ k
          (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))
        (RingHom.ker f.hom.toRingHom))
      (LiftClasses 𝓕.p f x)
```

**`Deformation.liftDifference_isPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean#L182). The attribute's comment: “difference is canonical pushforward”.

> **Stacks Project, Tag 06JI.** The infinitesimal difference of any two lifts is exactly the
> canonical tangent coordinate of the cocartesian pushforward of their fibre product along
> `(a₁, a₂) ↦ (ā₁, a₂ - a₁)`.

```lean
public theorem liftDifference_isPushforward
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p)
    {A' A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    (f : A' ⟶ A) (hf : Function.Surjective f.hom)
    (hann : ∀ a : A', a ∈ maximalIdeal A' →
      ∀ i : RingHom.ker f.hom.toRingHom, a * (i : A') = 0)
    (x : 𝓕.p.Fiber A) :
    letI : Module k (RingHom.ker f.hom.toRingHom) := kernelModule f hann
    let hS2 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓕 h𝓕.predeformation.cofibered
      (schlessingerConditionS2_of_satisfiesRS h𝓕.satisfiesRS)
      (.inl h𝓕.predeformation)
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨h𝓕.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))) := ⟨hS2⟩
    ∀ a b : LiftClasses 𝓕.p f x,
      IsPushforwardDifference 𝓕 h𝓕 f hf hann x a b
        (liftDifference 𝓕 h𝓕 f hf hann x a b)
```

**`Deformation.liftAction_difference`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean#L253). The attribute's comment: “difference characterization”.

> **Stacks Project, Tag 06JI.** The action is the unique lift whose infinitesimal difference
> from the given lift is the prescribed tangent vector.

```lean
public theorem liftAction_difference
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p)
    {A' A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    (f : A' ⟶ A) (hf : Function.Surjective f.hom)
    (hann : ∀ a : A', a ∈ maximalIdeal A' →
      ∀ i : RingHom.ker f.hom.toRingHom, a * (i : A') = 0)
    (x : 𝓕.p.Fiber A) :
    letI : Module k (RingHom.ker f.hom.toRingHom) := kernelModule f hann
    let hS2 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓕 h𝓕.predeformation.cofibered
      (schlessingerConditionS2_of_satisfiesRS h𝓕.satisfiesRS)
      (.inl h𝓕.predeformation)
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨h𝓕.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))) := ⟨hS2⟩
    letI := liftAction 𝓕 h𝓕 f hf hann x
    ∀ (a : LiftClasses 𝓕.p f x)
      (t : TensorProduct k
        (artinianTangentSpace Λ k
          (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))
        (RingHom.ker f.hom.toRingHom)),
      liftDifference 𝓕 h𝓕 f hf hann x a (t +ᵥ a) = t
```

**`Deformation.liftAction_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Action/FreeTransitive.lean#L293). The attribute's comment: “free and transitive”.

> **Stacks Project, Tag 06JI.** From any fixed lift, addition of tangent vectors is a
> bijection onto all isomorphism classes of lifts; equivalently, the action is free and
> transitive.

```lean
public theorem liftAction_bijective
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p)
    {A' A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    (f : A' ⟶ A) (hf : Function.Surjective f.hom)
    (hann : ∀ a : A', a ∈ maximalIdeal A' →
      ∀ i : RingHom.ker f.hom.toRingHom, a * (i : A') = 0)
    (x : 𝓕.p.Fiber A) :
    letI : Module k (RingHom.ker f.hom.toRingHom) := kernelModule f hann
    let hS2 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓕 h𝓕.predeformation.cofibered
      (schlessingerConditionS2_of_satisfiesRS h𝓕.satisfiesRS)
      (.inl h𝓕.predeformation)
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨h𝓕.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))) := ⟨hS2⟩
    letI := liftAction 𝓕 h𝓕 f hf hann x
    ∀ a : LiftClasses 𝓕.p f x,
      Function.Bijective
        (fun t : TensorProduct k
          (artinianTangentSpace Λ k
            (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))
          (RingHom.ker f.hom.toRingHom) => t +ᵥ a)
```

## Tag 06TA, an equation

[Tag 06TA](https://stacks.math.columbia.edu/tag/06TA) in the Stacks Project.

**`Deformation.liftClassesEquivSquareZeroPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/SquareZeroPullback.lean, line 658](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/SquareZeroPullback.lean#L658).

> The canonical difference isomorphism
> `A' ×_A A' ≅ A' ×_k k[I]` induces a bijection of lifts of `x` over these
> two objects, compatible with pushforward of each representative. The presentation
> `coord` of `k[I]` respects its `Λ`-algebra map and its chosen residue-field
> identification, as required for an identification in `𝒞_Λ`.

```lean
public theorem liftClassesEquivSquareZeroPullback
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsDeformationCategory p)
    {A' A S K P Q : ArtinianLocalAlgCat.{u, max v w, w} Λ k}
    (f : A' ⟶ A) (_hf : Function.Surjective f.hom)
    (hann : ∀ a : A', a ∈ IsLocalRing.maximalIdeal A' →
      ∀ i : RingHom.ker f.hom.toRingHom, a * (i : A') = 0)
    [Module k (RingHom.ker f.hom.toRingHom)]
    [Module kᵐᵒᵖ (RingHom.ker f.hom.toRingHom)]
    [IsCentralScalar k (RingHom.ker f.hom.toRingHom)]
    (hmodule : ∀ (a : A') (i : RingHom.ker f.hom.toRingHom),
      (A'.residueEquiv (IsLocalRing.residue A' a)) • i = a • i)
    (coord : S ≃+* TrivSqZeroExt k (RingHom.ker f.hom.toRingHom))
    (hcoordΛ : ∀ a : Λ, coord (algebraMap Λ S a) =
      TrivSqZeroExt.inl (algebraMap Λ k a))
    (hcoordResidue : ∀ s : S,
      (coord s).fst = S.residueEquiv (IsLocalRing.residue S s))
    (hK : K ≅ residueFieldObject.{u, v, w} Λ k)
    (rA : A' ⟶ K) (rS : S ⟶ K)
    (p₁ p₂ : P ⟶ A') (hP : IsPullback p₁ p₂ f f)
    (q₁ : Q ⟶ A') (q₂ : Q ⟶ S) (hQ : IsPullback q₁ q₂ rA rS)
    (x : p.Fiber A) :
    Nonempty (DifferenceLiftEquiv p f rA rS p₁ p₂ q₁ q₂ coord x)
```

## Tag 06TB, an equation

[Tag 06TB](https://stacks.math.columbia.edu/tag/06TB) in the Stacks Project.

Declarations registered for the tag:

- [`liftClassesProdEquivPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=liftClassesProdEquivPullback#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/LiftsOfObjects/SquareZeroPullback.lean, line 793](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/SquareZeroPullback.lean#L793) (StacksFrontier).

## Tag 06TC, an equation

[Tag 06TC](https://stacks.math.columbia.edu/tag/06TC) in the Stacks Project.

**`Deformation.liftClassesEquivProdOfResiduePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/CompositeProjection.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/CompositeProjection.lean#L178).

> For a composite of two fibre squares, lifts over the outer pullback are identified with a
> lift over the inner factor and a lift over the other outer factor, via the two projections.

```lean
public theorem liftClassesEquivProdOfResiduePullback
    {Λ : Type*} {k : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat Λ k)
    (hp : IsDeformationCategory p)
    {A₁' A₁ A₂ A : ArtinianLocalAlgCat Λ k}
    {f₁ : A₁ ⟶ A} {f₂ : A₂ ⟶ A} {g : A₁' ⟶ A₁}
    (right : PullbackCone f₁ f₂) (hright : IsLimit right)
    (left : PullbackCone g right.fst) (hleft : IsLimit left)
    (hg : Function.Surjective g.hom)
    (hf₁ : Function.Surjective f₁.hom)
    (x₀ : p.Fiber A) (a₁ : Lift p f₁ x₀) :
    Nonempty (LiftProjectionEquiv p right left x₀ a₁)
```

## Tag 06JJ, a remark

[Tag 06JJ](https://stacks.math.columbia.edu/tag/06JJ) in the Stacks Project.

**`Deformation.mapLiftClasses_vadd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/LiftsOfObjects/Action/Functoriality.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/LiftsOfObjects/Action/Functoriality.lean#L288).

> **Stacks Project, Tag 06JJ.** The map on lift classes commutes with the torsor actions,
> with tangent vectors mapped by the differential tensored with the identity of the kernel.

```lean
public theorem mapLiftClasses_vadd
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (𝓕 : BasedCategory.{vF, uF} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (𝓖 : BasedCategory.{vG, uG} (ArtinianLocalAlgCat.{u, w, w} Λ k))
    (h𝓕 : IsDeformationCategory 𝓕.p)
    (h𝓖 : IsDeformationCategory 𝓖.p)
    (φ : BasedFunctor 𝓕 𝓖)
    {A' A : ArtinianLocalAlgCat.{u, w, w} Λ k}
    (f : A' ⟶ A) (hf : Function.Surjective f.hom)
    (hann : ∀ a : A', a ∈ maximalIdeal A' →
      ∀ i : RingHom.ker f.hom.toRingHom, a * (i : A') = 0)
    (x : 𝓕.p.Fiber A) :
    letI : Module k (RingHom.ker f.hom.toRingHom) := kernelModule f hann
    let hS2𝓕 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓕 h𝓕.predeformation.cofibered
      (schlessingerConditionS2_of_satisfiesRS h𝓕.satisfiesRS)
      (.inl h𝓕.predeformation)
    let hS2𝓖 := schlessingerConditionS2_of_isIsomorphismClasses
      𝓖 h𝓖.predeformation.cofibered
      (schlessingerConditionS2_of_satisfiesRS h𝓖.satisfiesRS)
      (.inl h𝓖.predeformation)
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨h𝓕.predeformation⟩
    letI : Fact (IsPredeformationCategory 𝓖.p) := ⟨h𝓖.predeformation⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))) := ⟨hS2𝓕⟩
    letI : Fact (SchlessingerConditionS2
      (Functor.Elements.π (isomorphismClasses 𝓖 h𝓖.predeformation.cofibered))) := ⟨hS2𝓖⟩
    letI := liftAction 𝓕 h𝓕 f hf hann x
    letI := liftAction 𝓖 h𝓖 f hf hann ((fiberFunctor φ A).obj x)
    let dφ := IsLinearMap.mk' (differential h𝓕.predeformation.cofibered
      h𝓖.predeformation.cofibered φ)
      (differential_isLinearMap 𝓕 𝓖 h𝓕.predeformation h𝓖.predeformation hS2𝓕 hS2𝓖 φ)
    ∀ (a : LiftClasses 𝓕.p f x)
      (t : TensorProduct k
        (artinianTangentSpace Λ k
          (isomorphismClasses 𝓕 h𝓕.predeformation.cofibered))
        (RingHom.ker f.hom.toRingHom)),
      mapLiftClasses φ f x (t +ᵥ a) =
        (TensorProduct.map dφ (LinearMap.id :
          RingHom.ker f.hom.toRingHom →ₗ[k] RingHom.ker f.hom.toRingHom) t) +ᵥ
          mapLiftClasses φ f x a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.17, Tag 06JD](https://stacks.math.columbia.edu/tag/06JD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
