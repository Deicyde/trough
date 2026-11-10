---
declaration: section
origin: cited
lean: Deformation.Artin.IsOpenVersality, Deformation.Artin.IsOpenVersalityMorphism, Deformation.Artin.artinAxiomsFunctor, Deformation.Artin.artinAxiomsCategory, Deformation.Artin.nonempty_artinAxiomsFunctor_iff_exists_isCompact_open, Deformation.Artin.isVersalAt_sliceObject, Deformation.Artin.not_isVersalAt_sliceObject, Deformation.Artin.not_isOpenVersality_artinAxiomsCategory
statement: formalized
proof: formalized
---

# 98.13 Openness of versality

Section 98.13 of the Stacks Project, [Tag 07XP](https://stacks.math.columbia.edu/tag/07XP). 9 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07XQ, a definition

[Tag 07XQ](https://stacks.math.columbia.edu/tag/07XQ) in the Stacks Project.

**`Deformation.Artin.IsOpenVersality`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean#L147). The attribute's comment: “part (1)”.

> Versality of objects at finite-type points persists on an open neighbourhood.

```lean
public abbrev IsOpenVersality {S : Scheme.{u}} {X : Type vX} [Category.{wX} X]
    (q : X ⥤ Over S) (_hq : q.IsFiberedInGroupoids) : Prop
```

**`Deformation.Artin.IsOpenVersalityMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean#L161). The attribute's comment: “part (2)”.

> A morphism has openness of versality if its 2-fibre product with every
> scheme over a target object has openness of versality.

```lean
public noncomputable abbrev IsOpenVersalityMorphism {S : Scheme.{u}}
    {X : Type vX} [Category.{wX} X] {Y : Type vY} [Category.{wY} Y]
    (pX : X ⥤ Over S) (pY : Y ⥤ Over S) (F : X ⥤ Y)
    (hpX : pX.IsFiberedInGroupoids) (hpY : pY.IsFiberedInGroupoids)
    (hF : F ⋙ pY = pX) : Prop
```

## Tag 07XR, an example

[Tag 07XR](https://stacks.math.columbia.edu/tag/07XR) in the Stacks Project.

**`Deformation.Artin.artinAxiomsFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean#L57). The attribute's comment: “functor”.

> The functor which assigns a singleton to an admissible `k[s,t]`-algebra
> and the empty set to every other algebra.

```lean
public def artinAxiomsFunctor (k : Type u) [Field k] :
    CommAlgCat.{v, u} (MvPolynomial (Fin 2) k) ⥤ Type v
```

**`Deformation.Artin.artinAxiomsCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean#L93). The attribute's comment: “category”.

> The full subcategory of schemes over `Spec k[s,t]` admitting an affine open
> cover on which the functor of Tag 07XR has its unique value.

```lean
public abbrev artinAxiomsCategory (k : Type u) [Field k]
    (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of (MvPolynomial (Fin 2) k))))
```

**`Deformation.Artin.nonempty_artinAxiomsFunctor_iff_exists_isCompact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean#L229). The attribute's comment: “geometric_criterion”.

> The functor of Tag 07XR has its unique value on `A` if and only if
> `V(s,t) ⊆ Spec(A)` has a quasi-compact open neighbourhood on which `s`
> vanishes.

```lean
public theorem nonempty_artinAxiomsFunctor_iff_exists_isCompact_open
    (k : Type u) [Field k]
    (A : CommAlgCat.{v, u} (MvPolynomial (Fin 2) k)) :
    Nonempty ((artinAxiomsFunctor k).obj A) ↔
      ∃ W : Set (PrimeSpectrum A),
        IsOpen W ∧ IsCompact W ∧
          PrimeSpectrum.zeroLocus
              ({algebraMap (MvPolynomial (Fin 2) k) A (MvPolynomial.X 0),
                algebraMap (MvPolynomial (Fin 2) k) A (MvPolynomial.X 1)} : Set A) ⊆ W ∧
          ∀ x ∈ W,
            algebraMap A (Localization.AtPrime x.asIdeal)
                (algebraMap (MvPolynomial (Fin 2) k) A (MvPolynomial.X 0)) = 0
```

**`Deformation.Artin.isVersalAt_sliceObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexample.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexample.lean#L498). The attribute's comment: “the object x over U = Spec(k[s,t]/(s)) is versal at u_0 = (s,t)”.

> **The slice is versal at the origin.**

```lean
public theorem isVersalAt_sliceObject (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of (MvPolynomial (Fin 2) k)))) :
    IsVersalAt (Over.mk (sliceImmersion k)) (artinAxiomsOver B hS) (slicePoint k)
      (sliceObject B hS) (by delta sliceObject; rfl)
```

**`Deformation.Artin.not_isVersalAt_sliceObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexample.lean, line 956](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexample.lean#L956). The attribute's comment: “x is versal at no other point of U”.

> **The slice is versal at no point other than the origin.**

```lean
public theorem not_isVersalAt_sliceObject (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of (MvPolynomial (Fin 2) k))))
    (hu : (u : PrimeSpectrum (sliceRing k)) ≠ slicePoint k) :
    ¬ IsVersalAt (Over.mk (sliceImmersion k)) (artinAxiomsOver B hS) u
      (sliceObject B hS) (by delta sliceObject; rfl)
```

**`Deformation.Artin.not_isOpenVersality_artinAxiomsCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexample.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexample.lean#L1012). The attribute's comment: “openness of versality fails for the category, hence axiom [5] fails”.

> **Openness of versality fails for the category of Tag 07XR**, written out: the slice is
> versal at the origin, which is a finite-type point, but every open neighbourhood of the
> origin contains a closed point at which it is not versal. Axiom [5] asks openness of
> versality of the category and of its diagonal, so this is the failure of axiom [5].

```lean
public theorem not_isOpenVersality_artinAxiomsCategory (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of (MvPolynomial (Fin 2) k)))) :
    ¬ ∀ (U : Over (Spec (.of (MvPolynomial (Fin 2) k)))), LocallyOfFiniteType U.hom →
        ∀ (x : artinAxiomsCategory k B hS)
          (hx : (artinAxiomsOver B hS).obj x = U) (u₀ : ↥U.left),
          IsFiniteTypePoint u₀ →
          IsVersalAt U (artinAxiomsOver B hS) u₀ x hx →
          ∃ V : U.left.Opens, u₀ ∈ V.1 ∧
            ∀ u ∈ V.1, IsFiniteTypePoint u →
              IsVersalAt U (artinAxiomsOver B hS) u x hx
```

**`Deformation.Artin.isStackInGroupoids_artinAxiomsCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean#L481). The attribute's comment: “axiom [0]: the category is a stack in groupoids, for the fppf topology”.

> The inclusion of the full subcategory `IsArtinAxiomsObject` is a stack in groupoids for the
> fppf topology of the big fppf site over `Spec k[s,t]`.

```lean
public theorem isStackInGroupoids_artinAxiomsCategory :
    (ObjectProperty.ι (IsArtinAxiomsObject k B hS)).IsStackInGroupoids.{w}
      (BigFppfOver.topology B _ hS)
```

**`Deformation.Artin.satisfiesRS_artinAxiomsCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean#L549). The attribute's comment: “axiom [2]: the category satisfies the Rim-Schlessinger condition (RS)”.

> The inclusion of the full subcategory `IsArtinAxiomsObject` satisfies condition (RS): for a
> pushout `Y' = Y ⨿_X X'` of finite type local Artinian schemes along a closed immersion `X → X'`,
> the comparison from the fibre over `Y'` to the
> two-fibre product of the fibres over `Y` and `X'` is an equivalence.

```lean
public theorem satisfiesRS_artinAxiomsCategory :
    SatisfiesRS B _ hS (ObjectProperty.ι (IsArtinAxiomsObject k B hS))
      (isFiberedInGroupoids_artinAxiomsCategory B hS)
```

**`Deformation.Artin.isLimitPreserving_artinAxiomsCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean, line 680](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean#L680). The attribute's comment: “axiom [1]: the category is limit preserving, for inverse systems indexed by a category in the universe of the schemes”.

> The category fibred in groupoids `artinAxiomsCFG` is limit preserving: for a directed
> inverse system of affine schemes `Tᵢ` over `Spec k[s,t]` with limit `T`, the comparison
> `colim 𝒳_{Tᵢ} ⥤ 𝒳_T` is an equivalence.

```lean
public theorem isLimitPreserving_artinAxiomsCategory :
    IsLimitPreserving.{u, u, u, u + 1, u} B _ hS (artinAxiomsCFG B hS)
```

**`Deformation.Artin.finiteDimensional_tangentSpace_infinitesimalAutomorphisms_artinAxiomsCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean, line 732](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleAxioms.lean#L732). The attribute's comment: “axiom [3]: the tangent spaces and the spaces of infinitesimal automorphisms of the predeformation categories are finite dimensional”.

> For every finite-type field-valued point `x₀` of `artinAxiomsCategory`, the tangent space
> `T𝓕_{𝒳,k,x₀}` of its predeformation category is finite dimensional for its canonical vector space
> structure, and so is the group of infinitesimal automorphisms along every split pair
> `A₀ → A_ε → A₀`, for every vector space structure on it.

```lean
public theorem finiteDimensional_tangentSpace_infinitesimalAutomorphisms_artinAxiomsCategory
    {Λ K : Type u} [CommRing Λ] [Field K] [Algebra Λ K]
    (iΛ : Spec (.of Λ) ⟶ Spec (.of (MvPolynomial (Fin 2) k))) (x₀ : artinAxiomsCategory k B hS)
    (hx₀ : (ObjectProperty.ι (IsArtinAxiomsObject k B hS) ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ K)) ≫ iΛ))
    (hfin : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ K)) ≫ iΛ))
    (hqc : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ K)) ≫ iΛ)) :
    let D := predeformationCategory iΛ
      (ObjectProperty.ι (IsArtinAxiomsObject k B hS) ⋙ Over.post B.inclusion) x₀ hx₀
    letI := D.category
    let 𝓕 := BasedCategory.ofFunctor D.projection
    let hD : Deformation.IsDeformationCategory D.projection :=
      isDeformationCategory_predeformationCategory B _ hS _
        (isFiberedInGroupoids_artinAxiomsCategory B hS) (satisfiesRS_artinAxiomsCategory B hS)
        iΛ x₀ hx₀ hfin hqc
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
      (isomorphismClasses 𝓕 hD.predeformation.cofibered))) :=
      ⟨schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD⟩
    FiniteDimensional K
        (artinianTangentSpace Λ K (isomorphismClasses 𝓕 hD.predeformation.cofibered)) ∧
      ∀ {A₀ Aε : ArtinianLocalAlgCat.{u, u, u} Λ K} {z₀ : D.projection.Fiber A₀}
        {zε : D.projection.Fiber Aε} (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hge : g ≫ e = 𝟙 A₀)
        (i : z₀.1 ⟶ zε.1) (hi : D.projection.IsHomLift g i)
        [AddCommGroup ↥(infinitesimalAutomorphismsAlongSplitPair
          hD.predeformation.cofibered g e hge i hi)]
        [Module K ↥(infinitesimalAutomorphismsAlongSplitPair
          hD.predeformation.cofibered g e hge i hi)],
        FiniteDimensional K ↥(infinitesimalAutomorphismsAlongSplitPair
          hD.predeformation.cofibered g e hge i hi)
```

**`Deformation.Artin.isEquivalence_approximationFunctor_artinAxiomsCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleEffective.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/OpennessCounterexampleEffective.lean#L314). The attribute's comment: “axiom [4]: the functor of Stacks 07X6 from objects over Noetherian complete local rings to formal objects is an equivalence”.

> **The category of the openness-of-versality example satisfies axiom [4]**: the functor of
> Stacks 07X6, from objects over the spectra of Noetherian complete local rings to formal objects,
> is an equivalence.

```lean
public theorem isEquivalence_approximationFunctor_artinAxiomsCategory :
    (approximationFunctor B _ hS (ObjectProperty.ι (IsArtinAxiomsObject k B hS))
      (isFiberedInGroupoids_artinAxiomsCategory B hS)).IsEquivalence
```

## Tag 07XS, an equation

[Tag 07XS](https://stacks.math.columbia.edu/tag/07XS) in the Stacks Project.

**`Deformation.Artin.IsSmoothOnPredeformationCategories`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Basic.lean#L110).

> Smoothness of the induced map on predeformation categories at every
> finite-type field-valued point of the source.

```lean
public abbrev IsSmoothOnPredeformationCategories
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v₁} [Category.{w₁} X]
    {Y : Type v₂} [Category.{w₂} Y]
    (pX : X ⥤ BigFppfOver B S hS)
    (pY : Y ⥤ BigFppfOver B S hS)
    (F : X ⥤ Y) (hF : F ⋙ pY = pX) : Prop
```

## Tag 07XT, a lemma

[Tag 07XT](https://stacks.math.columbia.edu/tag/07XT) in the Stacks Project.

**`Deformation.Artin.isSmoothOnPredeformationCategories_sliceFunctor_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothnessConditionFromVersality.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/SmoothnessConditionFromVersality.lean#L63).

> **Stacks 07XT.** Let `𝒳` be a category fibred in groupoids over the big fppf site of a
> locally Noetherian scheme `S`, let `U` be a scheme locally of finite type over `S`, and let
> `x` be an object of `𝒳` over `U`. If `x` is versal at every finite type point of `U` and
> `𝒳` satisfies (RS), then the 1-morphism `x : (Sch/U)_fppf ⟶ 𝒳` satisfies the smoothness
> condition of Tag 07XS on predeformation categories.

```lean
public theorem isSmoothOnPredeformationCategories_sliceFunctor_of_isVersalAt
    [IsLocallyNoetherian S] (hp : p.IsFiberedInGroupoids)
    (hU : LocallyOfFiniteType ((p ⋙ Over.post B.inclusion).obj x).hom)
    (hversal : ∀ u₀ : ((p ⋙ Over.post B.inclusion).obj x).left,
      AlgebraicGeometry.IsFiniteTypePoint u₀ →
        IsVersalAt ((p ⋙ Over.post B.inclusion).obj x)
          (p ⋙ Over.post B.inclusion) u₀ x rfl)
    (hRS : SatisfiesRS B S hS p hp) :
    letI : p.IsFibered := hp.isFibered
    IsSmoothOnPredeformationCategories B S hS (Over.forget (p.obj x)) p
      (p.chosenPullbacks.sliceFunctor (⟨x, rfl⟩ : p.Fiber (p.obj x)))
      (p.chosenPullbacks.sliceFunctor_comp (⟨x, rfl⟩ : p.Fiber (p.obj x)))
```

## Tag 07XU, a lemma

[Tag 07XU](https://stacks.math.columbia.edu/tag/07XU) in the Stacks Project.

**`Deformation.Artin.isSmoothOnPredeformationCategories_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/Composition.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/Composition.lean#L291).

> The composite of two morphisms smooth on predeformation categories is
> smooth on predeformation categories.

```lean
public theorem isSmoothOnPredeformationCategories_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X : Type v₁} [Category.{w₁} X]
    {Y : Type v₂} [Category.{w₂} Y]
    {Z : Type v₃} [Category.{w₃} Z]
    (pX : X ⥤ BigFppfOver B S hS)
    (pY : Y ⥤ BigFppfOver B S hS)
    (pZ : Z ⥤ BigFppfOver B S hS)
    (F : X ⥤ Y) (G : Y ⥤ Z)
    (hF : F ⋙ pY = pX) (hG : G ⋙ pZ = pY)
    (hSmoothF : IsSmoothOnPredeformationCategories B S hS pX pY F hF)
    (hSmoothG : IsSmoothOnPredeformationCategories B S hS pY pZ G hG) :
    IsSmoothOnPredeformationCategories B S hS pX pZ (F ⋙ G)
      (by rw [Functor.assoc, hG, hF])
```

## Tag 07XV, a lemma

[Tag 07XV](https://stacks.math.columbia.edu/tag/07XV) in the Stacks Project.

**`Deformation.Artin.isSmoothOnPredeformationCategories_twoFibreProductSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/Openness/BaseChange.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/Openness/BaseChange.lean#L622).

> **Stacks 07XV.** Smoothness on predeformation categories is stable under base change of
> categories fibred in groupoids: if `f : 𝒳 ⟶ 𝒴` is smooth on predeformation categories, so is
> the projection `𝒳 ×_𝒴 𝒵 ⟶ 𝒵`.

```lean
public theorem isSmoothOnPredeformationCategories_twoFibreProductSnd
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {X : Type vX} [Category.{wX} X] {Y : Type vY} [Category.{wY} Y]
    {Z : Type vZ} [Category.{wZ} Z]
    (pX : X ⥤ BigFppfOver B S hS) (pY : Y ⥤ BigFppfOver B S hS)
    (pZ : Z ⥤ BigFppfOver B S hS) (f : X ⥤ Y) (g : Z ⥤ Y)
    (_hpX : pX.IsFiberedInGroupoids) (hpY : pY.IsFiberedInGroupoids)
    (_hpZ : pZ.IsFiberedInGroupoids)
    (hf : f ⋙ pY = pX) (hg : g ⋙ pY = pZ)
    (h : IsSmoothOnPredeformationCategories B S hS pX pY f hf) :
    IsSmoothOnPredeformationCategories B S hS
      (TwoFibreProductOver.structureFunctor pX pZ pY f g) pZ
      (TwoFibreProductOver.snd pX pZ pY f g)
      (by exact TwoFibreProductOver.snd_comp_eq)
```

## Tag 07XW, a lemma

[Tag 07XW](https://stacks.math.columbia.edu/tag/07XW) in the Stacks Project.

**`Deformation.Artin.isSmoothOnPredeformationCategories_of_isRelativelySmooth'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/RepresentableSmoothVersality.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/RepresentableSmoothVersality.lean#L57). The attribute's comment: “the representable-and-smooth clause: representable by algebraic spaces and smooth implies smooth on predeformation categories”.

> **Stacks 07XW, the representable-and-smooth clause.** A 1-morphism of categories fibred in
> groupoids over the big fppf category of a locally Noetherian scheme `S` which is representable by
> algebraic spaces and smooth induces a smooth functor of predeformation categories at every finite
> type field-valued point of the source; that is, it satisfies the condition of Stacks 07XS.

```lean
public theorem isSmoothOnPredeformationCategories_of_isRelativelySmooth'
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hsmooth : Stack.IsRelativelySmooth B S hS p) :
    IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
```

**`Deformation.Artin.isSmoothOnPredeformationCategories_of_isRelativelySmooth_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothImpliesVersalityCondition.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/SmoothImpliesVersalityCondition.lean#L109). The attribute's comment: “the representable-and-smooth clause, for a 1-morphism whose base changes along scheme-valued points of the target are representable by schemes”.

> A 1-morphism `p` of categories fibred in groupoids over the big fppf category of a locally
> Noetherian scheme `S` which is representable by algebraic spaces and smooth, and such that each
> algebraic space representing a base change of `p` along a scheme-valued point of the target is
> representable by schemes (`hrep`), induces a smooth functor of predeformation categories at every
> finite type field-valued point of the source.

```lean
public theorem isSmoothOnPredeformationCategories_of_isRelativelySmooth_of_representable
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hsmooth : Stack.IsRelativelySmooth B S hS p)
    (hrep : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
      (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (_hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
          (CatFiberedInGroupoids.homFunctor p))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      yoneda.relativelyRepresentable (OverShriek.relocalizeToYoneda U.hom F)) :
    IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
```

**`Deformation.Artin.isSmoothOnPredeformationCategories_of_isFormallySmoothOnObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothPredeformation.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/SmoothPredeformation.lean#L523). The attribute's comment: “the formally-smooth-on-objects clause: formally smooth on objects implies smooth on predeformation categories”.

> **Stacks 07WK**, case (1). A 1-morphism of categories fibred in groupoids over the big
> fppf category of `S` which is formally smooth on objects induces a smooth functor of
> predeformation categories at every finite type field-valued point of the source.
>
> This is also the formally-smooth-on-objects clause of Stacks 07XW — the condition the
> openness-of-versality statement is about — so both tags are registered here, on the declaration
> that carries the proof.

```lean
public theorem isSmoothOnPredeformationCategories_of_isFormallySmoothOnObjects
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) [IsLocallyNoetherian S]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (p : 𝒳 ⟶ 𝒴)
    (hp : Stack.IsFormallySmoothOnObjects B S hS 𝒳 𝒴 p) :
    IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)
      (CatFiberedInGroupoids.homFunctor_comp_p p)
```

## Tag 07XX, a lemma

[Tag 07XX](https://stacks.math.columbia.edu/tag/07XX) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRelativelySmooth_of_isSmoothOnPredeformationCategories`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSliceAtlas.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/TwoFibreProductSliceAtlas.lean#L1089). The attribute's comment: “the general 1-morphism, at the source's own hypotheses: (1) hfrep, (2) hf, (3) hlimX, (4) hlimY, and S locally Noetherian. The case of a 1-morphism induced by a morphism of schemes is smooth_of_isSmoothOnPredeformationCategories”.

> **Stacks 07XX.** Let `S` be a locally Noetherian scheme and `f : 𝒳 ⟶ 𝒴` a 1-morphism of
> categories fibred in groupoids over the big fppf site of `S`. If (1) `f` is representable by
> algebraic spaces, (2) `f` satisfies the deformation-theoretic smoothness condition of
> **Stacks 07XS**, (3) the structure morphism `𝒳 ⟶ (Sch/S)_{fppf}` is limit preserving on objects
> in the sense of **Stacks 06CU**, and (4) `𝒴` is limit preserving in the sense of **Stacks 07XL**,
> then `f` is smooth.
>
> `AlgebraicGeometry.Stack.IsRelativelySmooth` bundles the representability witness with the
> relative property of Stacks 03YK at the smooth property, which is what "smooth" means for a
> 1-morphism, so this is
> `AlgebraicGeometry.Stack.hasRelativeProperty_smooth_of_isSmoothOnPredeformationCategories` paired
> with `hfrep`. Condition (3) enters only through the cancellation for Stacks 06CU,
> `AlgebraicGeometry.Stack.isLimitPreservingOnObjects_of_toTerminalCFG`.
>
> The case of a 1-morphism induced by a morphism of schemes — the key ingredient, where the
> appeal to More on Morphisms is made — is
> `Deformation.Artin.smooth_of_isSmoothOnPredeformationCategories`.

```lean
theorem isRelativelySmooth_of_isSmoothOnPredeformationCategories
    (hfrep : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hlimX : BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒳
      (terminalCFG B S hS) (Bicategory.InducedBicategory.mkHom (toTerminalCFG B S hS 𝒳)))
    (hlimY : Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u} B S hS 𝒴)
    (hf : Deformation.Artin.IsSmoothOnPredeformationCategories B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor f) (CatFiberedInGroupoids.homFunctor_comp_p f)) :
    IsRelativelySmooth B S hS f
```

**`Deformation.Artin.smooth_of_isSmoothOnPredeformationCategories`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/SmoothnessFromPredeformation.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Versality/SmoothnessFromPredeformation.lean#L714). The attribute's comment: “the case of the 1-morphism induced by a morphism g : W ⟶ V of schemes over S. Hypothesis (2) is the hypothesis `hs`; hypothesis (1) is automatic for such a 1-morphism; and hypotheses (3) and (4) are replaced by `W` and `V` being locally of finite type over `S`, which over a locally Noetherian base is the finite-presentation content of limit preservation. The conclusion is smoothness of the morphism of schemes `g` -- what the relative property of Stacks 03YK amounts to for this 1-morphism, though that identification is not formalized here. The bookkeeping that reduces the general statement to this case (the 2-fibre product, its etale atlas, and part (3) of Stacks 07XN, which the library does not have) is NOT carried out, so the general 1-morphism of 07XX is not covered”.

> A morphism `g : W ⟶ V` of schemes locally of finite type over a locally Noetherian base `S`
> whose induced 1-morphism of slice categories satisfies the deformation-theoretic smoothness
> condition of Stacks 07XS is a smooth morphism of schemes.
>
> This is the case of Stacks 07XX in which the 1-morphism is the one induced by a morphism of
> schemes over `S`. It is the step the source calls the key ingredient of its proof, namely its
> appeal to More on Morphisms, Lemma 02HX; here that appeal is routed through the scheme-level
> criterion `Deformation.Artin.smoothAt_iff_isVersalAt` (Stacks 0CXL), which is 02HX in versality
> form, together with openness of the smooth locus and density of finite type points
> (Stacks 02J4).

```lean
public theorem smooth_of_isSmoothOnPredeformationCategories
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (W V : AlgebraicGeometry.BigFppfOver B S hS) (g : W ⟶ V)
    [LocallyOfFiniteType W.hom.hom] [LocallyOfFiniteType V.hom.hom]
    (hs : Deformation.Artin.IsSmoothOnPredeformationCategories B S hS
      (Over.map W.hom) (Over.map V.hom) (Over.map g.left)
      (by rw [← Over.mapComp_eq, g.w])) : Smooth g.left.hom
```

## Tag 07XY, a lemma

[Tag 07XY](https://stacks.math.columbia.edu/tag/07XY) in the Stacks Project.

**`Deformation.Artin.exists_smooth_finiteType_neighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/SmoothNeighborhood.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ArtinCriteria/SmoothNeighborhood.lean#L108). The attribute's comment: “the finite-type base, the object over it, its finite type point with residue field k, the restriction of that object to x₀ there, and smoothness of the 2-Yoneda morphism attached to it”.

> **Stacks 07XY.** Let `𝒳` be a category fibred in groupoids over the big fppf site of a
> locally Noetherian scheme `S` whose diagonal is representable by algebraic spaces, which is
> limit preserving (axiom [1]), satisfies (RS) (axiom [2]) and has finite-dimensional tangent
> spaces (the tangent-space half of axiom [3]), all of whose formal objects are effective, for
> which versality is open, and let `x₀` be an object of `𝒳` over a quasi-compact finite-type
> field point `i₀ : Spec k ⟶ S` whose image is a point `s` at which the local ring of `S` is a
> G-ring.
>
> Then there is a base `U = 𝒳.val.p.obj x` of finite type over `S` — locally of finite type and
> quasi-compact — an object `x` of `𝒳` over it, and a finite type point `u₀` of `U` with residue
> field `k`, such that `x` restricts to `x₀` at `u₀` along a Cartesian arrow `r : x₀ ⟶ x`
> realizing that identification of residue fields, and the 1-morphism
> `(Sch/U)_{fppf} ⟶ 𝒳` attached to `x` by the 2-Yoneda lemma is smooth.
>
> The proof is the proof of the source: the versal finite-type point of Stacks 07XH, shrunk by
> openness of versality, carries a smooth 2-Yoneda 1-morphism by Stacks 0CXM.

```lean
public theorem exists_smooth_finiteType_neighborhood
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w}
      (AlgebraicGeometry.BigFppfOver B S hS))
    (k : Type u) [Field k]
    (i₀ : Spec (.of k) ⟶ S) (x₀ : 𝒳.val.obj)
    (hx₀ : (𝒳.val.p ⋙ Over.post B.inclusion).obj x₀ = Over.mk i₀)
    (hfinite₀ : LocallyOfFiniteType i₀) (hqc₀ : QuasiCompact i₀)
    (s : S) (hs : i₀ (IsLocalRing.closedPoint k) = s)
    (hdiag : AlgebraicGeometry.Stack.HasRepresentableDiagonal B S hS 𝒳)
    (hlimit : IsLimitPreserving.{u, u, u, max (u + 1) v w, max u v} B S hS 𝒳)
    (hRS : SatisfiesRS B S hS 𝒳.val.p 𝒳.property)
    (htangent :
      ∀ (Λ : Type u) [CommRing Λ] [Algebra Λ k]
        (_ : Λ = S.presheaf.stalk s)
        (iΛ : Spec (.of Λ) ⟶ S)
        (_ : HEq iΛ (S.fromSpecStalk s))
        (hbase : Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ = i₀),
        let hx : (𝒳.val.p ⋙ Over.post B.inclusion).obj x₀ =
          Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) :=
          hx₀.trans (congrArg Over.mk hbase.symm)
        let D := predeformationCategory iΛ
          (𝒳.val.p ⋙ Over.post B.inclusion) x₀ hx
        letI : Category D.carrier := D.category
        ∀ hD : Deformation.IsDeformationCategory D.projection,
          let 𝓕 := BasedCategory.ofFunctor D.projection
          let hS2 := schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory 𝓕 hD
          letI : Fact (Deformation.IsPredeformationCategory 𝓕.p) :=
            ⟨hD.predeformation⟩
          letI : Fact (Deformation.SchlessingerConditionS2
            (CategoryOfElements.π
              (Deformation.isomorphismClasses 𝓕 hD.predeformation.cofibered))) :=
            ⟨hS2⟩
          let F := Deformation.isomorphismClasses 𝓕 hD.predeformation.cofibered
          let T := Deformation.artinianTangentSpace Λ k F
          letI : AddCommGroup T := Deformation.associatedTangentSpaceAddCommGroupUnlifted 𝓕
          letI : Module k T := Deformation.associatedTangentSpaceModuleUnlifted 𝓕
          FiniteDimensional k T)
    (heffective : ∀ ξ : FormalObject B S hS 𝒳.val.p,
      FormalObject.IsEffective B S hS 𝒳.val.p 𝒳.property ξ)
    (hopen : ∀ U : Over S, LocallyOfFiniteType U.hom →
      ∀ (y : 𝒳.val.obj) (hy : (𝒳.val.p ⋙ Over.post B.inclusion).obj y = U) (u : U.left),
        AlgebraicGeometry.IsFiniteTypePoint u →
        IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u y hy →
        ∃ V : U.left.Opens, u ∈ V.1 ∧
          ∀ u' : U.left, u' ∈ V.1 →
            AlgebraicGeometry.IsFiniteTypePoint u' →
            IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u' y hy)
    (hG : IsGRing (S.presheaf.stalk s)) :
    ∃ (x : 𝒳.val.obj)
      (u₀ : ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).left)
      (e : ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).left.residueField u₀ ≃+* k)
      (r : x₀ ⟶ x)
      (f : (AlgebraicGeometry.Stack.schemeFibredCategory B S hS
        (𝒳.val.p.obj x)).val ⥤ᵇ 𝒳.val),
      LocallyOfFiniteType ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).hom ∧
      QuasiCompact ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).hom ∧
      AlgebraicGeometry.IsFiniteTypePoint u₀ ∧
      𝒳.val.p.IsCartesian (𝒳.val.p.map r) r ∧
      (eqToHom hx₀.symm ≫ (𝒳.val.p ⋙ Over.post B.inclusion).map r).left =
        Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          ((𝒳.val.p ⋙ Over.post B.inclusion).obj x).left.fromSpecResidueField u₀ ∧
      Nonempty ((Functor.twoYonedaEvaluation 𝒳.val.p (𝒳.val.p.obj x)).obj f ≅
        (⟨x, rfl⟩ : 𝒳.val.p.Fiber (𝒳.val.p.obj x))) ∧
      (∃ hf : AlgebraicGeometry.IsRepresentableByAlgebraicSpaces B S hS f,
        AlgebraicGeometry.Stack.HasRelativePropertyBased.{u, u, u + 1,
            max u v, max (u + 1) v w, u} B S hS
          (AlgebraicGeometry.Space.smoothMorphismProperty B S hS) f hf)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.13, Tag 07XP](https://stacks.math.columbia.edu/tag/07XP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
