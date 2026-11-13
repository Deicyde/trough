---
declaration: section
origin: cited
lean: Deformation.Artin.FormalObject.IsVersalOverScheme, Deformation.Artin.hatX, Deformation.Artin.IsVersalAt, Deformation.Artin.isVersalAt_iff_isVersal, Deformation.Artin.smoothAt_iff_isVersalAt, Deformation.Artin.isSmooth_mapPredeformationCategory_of_isVersalAt, Deformation.Artin.BaseChange.isSmoothAt_baseChange_of_isVersalAt, Deformation.Artin.exists_finiteType_versal_approximation
statement: formalized
proof: formalized
---

# 98.12 Versality

Section 98.12 of the Stacks Project, [Tag 07XD](https://stacks.math.columbia.edu/tag/07XD). 9 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CXJ, a definition

[Tag 0CXJ](https://stacks.math.columbia.edu/tag/0CXJ) in the Stacks Project.

**`Deformation.Artin.FormalObject.IsVersalOverScheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FormalObject/Versal.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/FormalObject/Versal.lean#L164). The attribute's comment: “versal for one, equivalently every, affine open `Spec Λ ⊆ S` through which the closed point factors; the independence is `FormalObject.isVersal_iff_of_isOpenImmersion`”.

> **Stacks 0CXJ.** A formal object `ξ = (R, ξ_n, f_n)` of a category fibred in groupoids over
> the big fppf site of `S`, with `k = R / 𝔪` and `x₀ = ξ_0`, is *versal* when `ξ`, read as a
> formal object of the predeformation category `𝓕_{𝒳,k,x₀}` (**Stacks 0CXH**), is versal in the
> sense of **Stacks 06HR**.
>
> The predeformation category is built over `𝒞_Λ` for an affine open `Spec Λ ⊆ S` through which
> `Spec k ⟶ S` factors (**Stacks 07T2**): here `iΛ : Spec Λ ⟶ S` is an open immersion and the
> `Λ`-algebra structure of `R` is the one factoring the structure morphism of `ξ` through
> `Spec Λ` (it exists and is unique, `Spec R` being local and `iΛ` a monomorphism). The
> definition asks for one such affine open; by
> `Deformation.Artin.FormalObject.isVersal_iff_of_isOpenImmersion` the answer is the same for
> every one of them, which is the independence of the choice noted in **Stacks 07T2**, and
> `Deformation.Artin.FormalObject.isVersalOverScheme_iff_forall` restates it with all affine
> opens. In particular it is the same for the affine opens with `Λ → k` finite that
> **Stacks 07T2** picks.

```lean
def FormalObject.IsVersalOverScheme (hp : p.IsFiberedInGroupoids)
    (ξ : FormalObject B S hS p) : Prop
```

## Tag 07XE, an equation

[Tag 07XE](https://stacks.math.columbia.edu/tag/07XE) in the Stacks Project.

**`Deformation.Artin.hatX`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality.lean#L214).

> The map `\hat x : 𝓕_{(Sch/U)_{fppf},k,u₀} ⟶ 𝓕_{𝓧,k,x₀}` over
> `𝒞_Λ`, for the 2-Yoneda functor associated to the given object over `U`.

```lean
public noncomputable def hatX
    (x : X) (hx : q.obj x = U) (_ : q.IsFiberedInGroupoids) :
    HatXConstruction iΛ U q u₀ hu₀ x hx
```

## Tag 07XF, a definition

[Tag 07XF](https://stacks.math.columbia.edu/tag/07XF) in the Stacks Project.

**`Deformation.Artin.IsVersalAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality.lean#L108).

> An object `x` over `U` is versal at `u₀` if the induced map of predeformation categories is
> smooth: for a surjection `B ⟶ A` of Artinian local algebras, an arrow `y ⟶ z` over
> `Spec A ⟶ Spec B` and an arrow `y ⟶ x` restricting to `u₀` extend to an arrow `z ⟶ x` making
> the triangle commute.

```lean
public noncomputable abbrev IsVersalAt
    (u₀ : U.left) (x : X) (hx : q.obj x = U) : Prop
```

## Tag 0CXK, a lemma

[Tag 0CXK](https://stacks.math.columbia.edu/tag/0CXK) in the Stacks Project.

**`Deformation.Artin.isVersalAt_iff_isVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/FormalObjectVersal/VersalityCriterion.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/FormalObjectVersal/VersalityCriterion.lean#L293).

> With the notation of **Stacks 07XF**, let `R` be the completed local ring of `U` at a finite
> type point `u₀`, presented by a ring equivalence `e`, and let `ξ` be the formal object attached
> by the approximation functor of **Stacks 07X6** to a Cartesian restriction `x_R` of `x` over
> `Spec R`. Then `x` is versal at `u₀` exactly when `ξ` is versal in the sense of
> **Stacks 0CXJ**.

```lean
public theorem isVersalAt_iff_isVersal
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : Type v} [Category.{w} F]
    (p : F ⥤ AlgebraicGeometry.BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids)
    (U : Over S) (x : F)
    (hx : (p ⋙ Over.post B.inclusion).obj x = U)
    (u₀ : U.left)
    [IsLocallyNoetherian S] [LocallyOfFiniteType U.hom]
    (_hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀)
    (xR : Deformation.Artin.CompleteLocalObjects B S hS p)
    (ξ : Deformation.Artin.FormalObject B S hS p)
    (hξ : ξ = (Deformation.Artin.approximationFunctor B S hS p hp).obj xR)
    (e : AlgebraicGeometry.Scheme.completedLocalRing U.left u₀ ≃+* ξ.base.R)
    (g : Spec (.of ξ.base.R) ⟶ U.left)
    (hg : g = Spec.map (CommRingCat.ofHom e.toRingHom) ≫
      Spec.map (CommRingCat.ofHom
        (algebraMap (U.left.presheaf.stalk u₀)
          (AlgebraicGeometry.Scheme.completedLocalRing U.left u₀))) ≫
      U.left.fromSpecStalk u₀)
    (hbase : ξ.base.toS = g ≫ U.hom)
    (r : xR.obj.1 ⟶ x)
    (_hr : p.IsCartesian (p.map r) r)
    (hrbase : HEq
      ((eqToHom (Deformation.Artin.chosenBase_eq B S hS p xR.obj).symm ≫
        p.map r).left.hom ≫ eqToHom (congrArg Over.left hx)) g)
    (Λ : Type u) [CommRing Λ] [Algebra Λ ξ.base.R]
    (hΛstalk : CommRingCat.of Λ = S.presheaf.stalk (Deformation.Artin.basePoint U u₀))
    (iΛ : Spec (.of Λ) ⟶ S)
    (hiΛ : HEq iΛ (S.fromSpecStalk (Deformation.Artin.basePoint U u₀)))
    (hΛ : Spec.map (CommRingCat.ofHom (algebraMap Λ ξ.base.R)) ≫ iΛ =
      ξ.base.toS) :
    Deformation.Artin.IsVersalAt U (p ⋙ Over.post B.inclusion) u₀ x hx ↔
      Deformation.Artin.FormalObject.IsVersal B S hS p hp ξ Λ iΛ hΛ
```

## Tag 0CXL, a lemma

[Tag 0CXL](https://stacks.math.columbia.edu/tag/0CXL) in the Stacks Project.

**`Deformation.Artin.smoothAt_iff_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/Versality.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ArtinCriteria/Versality.lean#L214).

> Smoothness at a finite-type point is equivalent to versality of the
> corresponding object of the slice fibred over schemes over `S`.

```lean
public theorem smoothAt_iff_isVersalAt
    {U V S : Scheme.{u}} (f : U ⟶ V) (g : V ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType (f ≫ g)]
    [LocallyOfFiniteType g] (u₀ : U)
    (hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀) :
    InfinitesimalLifting.SmoothAt f u₀ ↔
      Deformation.Artin.IsVersalAt (Over.mk (f ≫ g))
        (Over.forget (Over.mk g)) u₀
        (Over.mk (Over.homMk f (by simp))) rfl
```

## Tag 07XG, a lemma

[Tag 07XG](https://stacks.math.columbia.edu/tag/07XG) in the Stacks Project.

**`Deformation.Artin.isSmooth_mapPredeformationCategory_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/FiniteResidueFieldExtension/Smoothness.lean, line 1229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/FiniteResidueFieldExtension/Smoothness.lean#L1229).

> **Stacks 07XG.** Let `𝒳` be a category fibred in groupoids over the big fppf site of a
> locally Noetherian scheme `S`, let `x` be an object of `𝒳` over a scheme `U` locally of
> finite type over `S`, and let `u₀` be a finite type point of `U`. Let `l` be a finite
> extension of `κ(u₀)` and let `u_{l,0} : Spec l ⟶ U` be the induced `l`-valued point of `U`.
> If `𝒳` satisfies (RS) and `x` is versal at `u₀`, then the morphism of predeformation
> categories `𝓕_{(Sch/U)_fppf, l, u_{l,0}} ⟶ 𝓕_{𝒳, l, x_{l,0}}` is smooth.

```lean
public theorem isSmooth_mapPredeformationCategory_of_isVersalAt
    [IsLocallyNoetherian S] (hp : p.IsFiberedInGroupoids)
    (hU : LocallyOfFiniteType ((p ⋙ Over.post B.inclusion).obj x).hom)
    (u₀ : ((p ⋙ Over.post B.inclusion).obj x).left)
    (hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀)
    [Algebra (((p ⋙ Over.post B.inclusion).obj x).left.residueField u₀) l]
    [Module.Finite (((p ⋙ Over.post B.inclusion).obj x).left.residueField u₀) l]
    (hfieldPoint : fieldPointMap B S hS p x iΛ uₗ₀ huₗ₀ =
      Spec.map (CommRingCat.ofHom (algebraMap
          (((p ⋙ Over.post B.inclusion).obj x).left.residueField u₀) l)) ≫
        ((p ⋙ Over.post B.inclusion).obj x).left.fromSpecResidueField u₀)
    (hversal : IsVersalAt ((p ⋙ Over.post B.inclusion).obj x)
      (p ⋙ Over.post B.inclusion) u₀ x rfl)
    (hRS : SatisfiesRS B S hS p hp) :
  letI : p.IsFibered := hp.isFibered
  Deformation.IsSmooth
    (mapPredeformationCategory iΛ
      (Over.forget (p.obj x) ⋙ Over.post B.inclusion)
      (p ⋙ Over.post B.inclusion)
      (p.chosenPullbacks.sliceFunctor (⟨x, rfl⟩ : p.Fiber (p.obj x)))
      (sliceFunctor_comp_post B S hS p p.chosenPullbacks x) uₗ₀ huₗ₀).toBasedFunctor
```

## Tag 0CXM, a lemma

[Tag 0CXM](https://stacks.math.columbia.edu/tag/0CXM) in the Stacks Project.

**`Deformation.Artin.BaseChange.isSmoothAt_baseChange_of_isVersalAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/VersalBaseChange/Smoothness.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ArtinCriteria/VersalBaseChange/Smoothness.lean#L268).

> **Stacks 0CXM.** Let `𝒳` be a category fibred in groupoids over the big fppf site of a
> locally Noetherian scheme `S`, let `x` be an object of `𝒳` over a scheme `U` locally of finite
> type over `S`, and let `u₀` be a finite type point of `U`.  Assume the diagonal of `𝒳` is
> representable by algebraic spaces and locally of finite type, and that `𝒳` satisfies (RS).
> Let `V` be a scheme locally of finite type over `S`, let `y` be an object of `𝒳` over `V`, let
> `F` be the algebraic space representing the 2-fibre product
> `𝒵 = (Sch/V)_{fppf} ×_𝒳 (Sch/U)_{fppf}` over `V`, and let `z₀` be a finite type point of `F`
> lying over `u₀`.  If `x` is versal at `u₀`, then `F ⟶ V` is smooth at `z₀`.

```lean
public theorem isSmoothAt_baseChange_of_isVersalAt
    [IsLocallyNoetherian S]
    (hΔ : AlgebraicGeometry.Stack.HasRepresentableDiagonal B S hS 𝒳)
    (hΔlft :
      letI : 𝒳.val.p.IsFibered := 𝒳.isFiberedInGroupoids.isFibered
      ∀ (T : AlgebraicGeometry.BigFppfOver B S hS)
        (a b : 𝒳.val.p.Fiber T)
        (G : (AlgebraicGeometry.BigFppfOver B T.left.1 T.left.2)ᵒᵖ ⥤ Type u),
        AlgebraicGeometry.IsAlgebraicSpace B T.left.1 T.left.2 G →
        Nonempty (G ⋙ uliftFunctor.{v, u} ≅
          ((Over.iteratedSliceBackward T).op ⋙ 𝒳.val.p.isomPresheaf a b) ⋙
            uliftFunctor.{u, v}) →
        AlgebraicGeometry.Space.IsLocallyOfFiniteType B T.left.1 T.left.2
          (terminal.from G : G ⟶
            ⊤_ ((AlgebraicGeometry.BigFppfOver B T.left.1 T.left.2)ᵒᵖ ⥤ Type u)))
    (hRS : Deformation.Artin.SatisfiesRS B S hS 𝒳.val.p
      𝒳.isFiberedInGroupoids)
    (U V : AlgebraicGeometry.BigFppfOver B S hS)
    [LocallyOfFiniteType (B.inclusion.map U.hom)]
    [LocallyOfFiniteType (B.inclusion.map V.hom)]
    (x : 𝒳.val.obj) (hx : 𝒳.val.p.obj x = U)
    (u₀ : U.left.1)
    (hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀)
    (y : AlgebraicGeometry.BigFppfOver B V.left.1 V.left.2 ⥤ 𝒳.val.obj)
    (hy : y ⋙ 𝒳.val.p = Over.map V.hom)
    (F : (AlgebraicGeometry.BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
    (hF : AlgebraicGeometry.IsAlgebraicSpace B V.left.1 V.left.2 F)
    (e : BaseChangeEquivalence B S hS 𝒳 U V x hx y F)
    (z₀ : AlgebraicGeometry.Space.FieldValuedPoint B V.left.1 V.left.2 F)
    (hz₀ : AlgebraicGeometry.Space.IsFiniteTypePoint B V.left.1 V.left.2 F
      (z₀.class B V.left.1 V.left.2 F))
    (hzu :
      letI : Category (TwoFibreProductOver (Over.map V.hom)
        (Over.forget U) 𝒳.val.p y
        (Functor.TwoYoneda.liftBased 𝒳.val.p
          𝒳.isFiberedInGroupoids U ⟨x, hx⟩).toFunctor) :=
            TwoFibreProductOver.instCategory
      let P := e.inv.functor.obj ⟨z₀.siteObject, Discrete.mk z₀.value⟩
      ∃ hP : P.x = z₀.siteObject,
        (B.inclusion.map
          ((eqToHom (P.hx.trans P.hy.symm) ≫ P.y.hom).left))
          ((B.inclusion.map (eqToHom (congrArg Over.left hP).symm))
            (IsLocalRing.closedPoint z₀.carrier)) = u₀)
    (hversal : Deformation.Artin.IsVersalAt (Over.mk (B.inclusion.map U.hom))
      (𝒳.val.p ⋙ Over.post B.inclusion) u₀ x
      (by simpa using congrArg (Over.post B.inclusion).obj hx)) :
    AlgebraicGeometry.Space.IsSmoothAt B V.left.1 V.left.2
      (terminal.from F : F ⟶
        ⊤_ ((AlgebraicGeometry.BigFppfOver B V.left.1 V.left.2)ᵒᵖ ⥤ Type u))
      (z₀.class B V.left.1 V.left.2 F)
```

## Tag 07XH, a lemma

[Tag 07XH](https://stacks.math.columbia.edu/tag/07XH) in the Stacks Project.

**`Deformation.Artin.exists_finiteType_versal_approximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/FormalObjectApproximation/StalkBaseVersality.lean, line 905](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/FormalObjectApproximation/StalkBaseVersality.lean#L905). The attribute's comment: “the whole statement, unconditionally: Stacks 07QZ — Artin approximation over a G-ring — is proved in this library, so the Stacks 07XB that this uses is itself unconditional”.

> An effective versal formal object over a locally Noetherian base whose local ring at the
> image point is a G-ring is the system of infinitesimal restrictions of an object over a
> finite-type neighbourhood, versal at a finite type point with the same residue field.

```lean
public theorem exists_finiteType_versal_approximation
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [IsLocallyNoetherian S]
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
      (AlgebraicGeometry.BigFppfOver B S hS))
    (ξ : Deformation.Artin.FormalObject B S hS 𝒳.val.p)
    (heffective : Deformation.Artin.FormalObject.IsEffective B S hS 𝒳.val.p
      𝒳.property ξ)
    (s : S) (hs : ξ.base.toS (closedPoint ξ.base.R) = s)
    (hG : IsGRing (S.presheaf.stalk s))
    (hlimit : AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B S hS 𝒳
      (baseFiberedCategory B S hS)
      (structureMorphism B S hS 𝒳))
    [Algebra (S.presheaf.stalk s : Type u) ξ.base.R]
    (iΛ : Spec (.of (S.presheaf.stalk s : Type u)) ⟶ S)
    (hiΛ : iΛ = S.fromSpecStalk s)
    (hΛ : Spec.map (CommRingCat.ofHom
        (algebraMap (S.presheaf.stalk s : Type u) ξ.base.R)) ≫ iΛ = ξ.base.toS)
    (hversal : Deformation.Artin.FormalObject.IsVersal B S hS 𝒳.val.p 𝒳.property
      ξ (S.presheaf.stalk s : Type u) iΛ hΛ) :
    ∃ (U : Over S) (u₀ : U.left)
      (V : AlgebraicGeometry.BigFppfOver B S hS)
      (_ : (Over.post B.inclusion).obj V = U)
      (x : 𝒳.val.p.Fiber V)
      (hx : (𝒳.val.p ⋙ Over.post B.inclusion).obj x.1 = U),
      LocallyOfFiniteType U.hom ∧ QuasiCompact U.hom ∧
      AlgebraicGeometry.IsFiniteTypePoint u₀ ∧
      (letI : CommRing ξ.base.R := ξ.base.commRing
       letI : IsLocalRing ξ.base.R := ξ.base.localRing
       Nonempty (U.left.residueField u₀ ≃+* ResidueField ξ.base.R)) ∧
      Deformation.Artin.IsVersalAt U (𝒳.val.p ⋙ Over.post B.inclusion) u₀ x.1 hx ∧
      ∃ (xR : Deformation.Artin.CompleteLocalObjects B S hS 𝒳.val.p),
        Nonempty (ξ ≅ (Deformation.Artin.approximationFunctor B S hS 𝒳.val.p
          𝒳.property).obj xR) ∧
      ∃ (r : xR.obj.1 ⟶ x.1)
        (eR : AlgebraicGeometry.Scheme.completedLocalRing U.left u₀ ≃+*
          (Deformation.Artin.chosenBase B S hS 𝒳.val.p xR.obj).R),
        𝒳.val.p.IsCartesian (𝒳.val.p.map r) r ∧
        ((eqToHom (Deformation.Artin.chosenBase_eq B S hS 𝒳.val.p xR.obj).symm ≫
            𝒳.val.p.map r).left.hom ≫ eqToHom (congrArg Over.left hx)) =
          (Spec.map (CommRingCat.ofHom
            eR.toRingHom) ≫
            Spec.map (CommRingCat.ofHom
              (algebraMap (U.left.presheaf.stalk u₀)
                (AlgebraicGeometry.Scheme.completedLocalRing U.left u₀))) ≫
            U.left.fromSpecStalk u₀)
```

## Tag 07XI, an example

[Tag 07XI](https://stacks.math.columbia.edu/tag/07XI) in the Stacks Project.

**`Deformation.Artin.GRingCounterexample.stack`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingCounterexample.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingCounterexample.lean#L210). The attribute's comment: “the Example's construction: the functor `F` on the big fppf site of `S = Spec(Λ)`, which is a one-point set on a `T` whose structure morphism factors through `S' = (S ∖ {𝔪}) ⨿ Spec(C)` and empty otherwise, and the category `𝒳 = 𝒮_F` fibred in sets that it defines. The source's three assertions about them are `Deformation.Artin.GRingCounterexample.isLimitPreservingOnObjects_stack`, `Deformation.Artin.GRingCounterexample.isEffective_formalObject` and `Deformation.Artin.GRingCounterexample.isVersal_formalObject`, about the formal object `Deformation.Artin.GRingCounterexample.formalObject`; the Example whole -- those assertions together with the Example's conditional conclusion, which assumes the conclusion of Stacks 07XH for these `𝒳` rather than any G-ring property -- is `Deformation.Artin.GRingCounterexample.exists_algHom_henselian`.”.

> **The category `𝒳 = 𝒮_F` fibred in groupoids over the big fppf site of `S`,** built from
> the functor `F` via the Grothendieck construction of **Stacks 0458**.

```lean
public def stack (m : Ideal Λ) [m.IsMaximal] (C : Type u) [CommRing C] (φ : Λ →+* C)
    (B : AlgebraicGeometry.BigFppfSite.{u}) (hS : B.Contains (Spec (.of Λ))) :
    CategoryTheory.CatFiberedInGroupoids (BigFppfOver B (Spec (.of Λ)) hS)
```

**`Deformation.Artin.GRingCounterexample.formalObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingCounterexample.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingCounterexample.lean#L367). The attribute's comment: “the formal object `ξ` over `R = Λ_𝔪^∧` whose existence the Example asserts: the complete local base `R` over `S = Spec(Λ)`, the level of `ξ` at each infinitesimal neighbourhood of the closed point of `Spec(R)`, and the transitions. That `ξ` is effective (`Deformation.Artin.FormalObject.IsEffective`, Stacks 07X7) is `Deformation.Artin.GRingCounterexample.isEffective_formalObject`, and that it is versal (`Deformation.Artin.FormalObject.IsVersal`, Stacks 0CXJ) is `Deformation.Artin.GRingCounterexample.isVersal_formalObject`. The Example whole -- the three assertions together with the Example's conditional conclusion, which assumes the conclusion of Stacks 07XH for these `𝒳` rather than any G-ring property -- is `Deformation.Artin.GRingCounterexample.exists_algHom_henselian`.”.

> **The formal object `ξ` over `R = Λ_𝔪^∧`** of the Example. Each level is the unique point
> of `F(Spec(R/𝔪_R^{n+1}))`, which is nonempty because the Example's factorization
> `Λ → C → R` makes every infinitesimal neighbourhood of the closed point map to `Spec(C)`, and
> the transitions are the unique morphisms of `𝒳 = 𝒮_F` lying over the closed immersions
> `Spec(R/𝔪_R^{n+1}) ↪ Spec(R/𝔪_R^{n+2})`, the fibres of `𝒮_F` being discrete and `F` taking
> only subsingleton values.

```lean
public def formalObject (ψ : C →+* completion m)
    (hψ : ψ.comp φ = algebraMap Λ (completion m))
    (hR : B.Contains (Spec (.of (completion m)))) :
    Deformation.Artin.FormalObject B (Spec (.of Λ)) hS (stack m C φ B hS).val.p
```

**`Deformation.Artin.GRingCounterexample.isLimitPreservingOnObjects_stack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingCounterexample.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingCounterexample.lean#L481). The attribute's comment: “the Example's assertion that `𝒳 = 𝒮_F ⟶ (Sch/S)_{fppf}` is limit preserving on objects. The construction of `F` and `𝒳` is `Deformation.Artin.GRingCounterexample.stack`, and the other two assertions, about the formal object `ξ` over `R = Λ_𝔪^∧`, are `Deformation.Artin.GRingCounterexample.isEffective_formalObject` and `Deformation.Artin.GRingCounterexample.isVersal_formalObject`. The Example whole is `Deformation.Artin.GRingCounterexample.exists_algHom_henselian`.”.

> **`𝒳 = 𝒮_F` is limit preserving on objects**, the first of the Example's three assertions
> about `𝒳`.

```lean
public theorem isLimitPreservingOnObjects_stack [IsNoetherianRing Λ]
    (hφ : RingHom.FiniteType φ) :
    AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1}
      B (Spec (.of Λ)) hS (stack m C φ B hS)
      (Deformation.Artin.Approximation.baseFiberedCategory B (Spec (.of Λ)) hS)
      (Deformation.Artin.Approximation.structureMorphism B (Spec (.of Λ)) hS
        (stack m C φ B hS))
```

**`Deformation.Artin.GRingCounterexample.isEffective_formalObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingCounterexampleEffective.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingCounterexampleEffective.lean#L116). The attribute's comment: “the Example's assertion that the formal object `ξ` over `R = Λ_𝔪^∧` is effective. The construction of `F`, `𝒳 = 𝒮_F` and `ξ` is in `StacksFrontier.Deformation.Artin.Versality.GRingCounterexample`, limit preservation on objects is `Deformation.Artin.GRingCounterexample.isLimitPreservingOnObjects_stack`, and versality is `Deformation.Artin.GRingCounterexample.isVersal_formalObject`. The Example whole -- these three assertions together with the Example's conditional conclusion, which assumes the conclusion of Stacks 07XH for these `𝒳` rather than any G-ring property -- is `Deformation.Artin.GRingCounterexample.exists_algHom_henselian`. NOT covered, and formalized nowhere: the Example's closing step from solvability in the henselization to `Λ_𝔪^h` and `Λ_𝔪` being G-rings, which the Stacks Project itself defers ("insert future reference here"), so there is no statement to formalize against.”.

> **The formal object `ξ` over `R = Λ_𝔪^∧` is effective**, the first of the Example's two
> assertions about `ξ`.

```lean
public theorem isEffective_formalObject :
    Deformation.Artin.FormalObject.IsEffective B (Spec (.of Λ)) hS (stack m C φ B hS).val.p
      ((stack m C φ B hS).isFiberedInGroupoids) (formalObject m C φ B hS ψ hψ hR)
```

**`Deformation.Artin.GRingCounterexample.isVersal_formalObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingCounterexampleVersal.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingCounterexampleVersal.lean#L75). The attribute's comment: “the Example's assertion that the formal object `ξ` over `R = Λ_𝔪^∧` is versal, relative to `Λ_𝔪`, through which the structure morphism of `R` factors. The construction of `F`, `𝒳 = 𝒮_F` and `ξ` is in `StacksFrontier.Deformation.Artin.Versality.GRingCounterexample`, limit preservation on objects is `Deformation.Artin.GRingCounterexample.isLimitPreservingOnObjects_stack`, and effectivity is `Deformation.Artin.GRingCounterexample.isEffective_formalObject`. Versality relative to the local ring of `S` at `𝔪`, which is the form Stacks 07XH consumes, is `Deformation.Artin.GRingCounterexample.isVersal_formalObject_stalk`, and the Example whole is `Deformation.Artin.GRingCounterexample.exists_algHom_henselian`. NOT covered, and formalized nowhere: the Example's closing step from solvability in the henselization to `Λ_𝔪^h` and `Λ_𝔪` being G-rings, which the Stacks Project itself defers ("insert future reference here"), so there is no statement to formalize against.”.

> **The formal object `ξ` over `R = Λ_𝔪^∧` is versal**, the last of the Example's three
> assertions about `𝒳 = 𝒮_F`. Versality is relative to `Λ_𝔪`, through which the structure morphism
> of `R` factors by `Deformation.Artin.GRingCounterexample.base_toS_eq`.

```lean
public theorem isVersal_formalObject :
    Deformation.Artin.FormalObject.IsVersal B (Spec (.of Λ)) hS (stack m C φ B hS).val.p
      ((stack m C φ B hS).isFiberedInGroupoids) (formalObject m C φ B hS ψ hψ hR)
      (Localization.AtPrime m) (localChart m) (base_toS_eq m C φ B hS ψ hψ hR)
```

**`Deformation.Artin.GRingCounterexample.exists_algHom_henselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingExample.lean, line 844](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingExample.lean#L844). The attribute's comment: “the Example whole, in the Example's own logical direction: the functor `F` on the big fppf site of `S = Spec(Λ)` (`Deformation.Artin.GRingCounterexample.functor`, whose displayed defining property -- a one-point set on a `T` whose structure morphism factors through `S' = (S ∖ {𝔪}) ⨿ Spec(C)`, empty otherwise -- is the first conjunct below), the category `𝒳 = 𝒮_F` fibred in sets it defines (`Deformation.Artin.GRingCounterexample.stack`), the formal object `ξ` over `R = Λ_𝔪^∧` (`Deformation.Artin.GRingCounterexample.formalObject`), the source's three assertions about them -- limit preservation on objects, effectivity and versality of `ξ` -- and the Example's conditional conclusion: IF the conclusion of Stacks 07XH holds for all these `𝒳`, i.e. if every finite type factorization `Λ → C' → R` carries the three-item datum the Example reads off it (`Deformation.Artin.AlgebraizesFiniteTypeFactorizations`: a finite type `Λ`-algebra `A`, a maximal ideal `𝔪_A` over `𝔪` with `κ(𝔪) = κ(𝔪_A)` and condition (4) of Stacks 02HT, and a `Λ`-algebra map `C' → A`), THEN `C` maps over `Λ` to every henselian local `Λ`-algebra whose maximal ideal contracts to `𝔪` and every polynomial system over `Λ` with a solution in `R` has a solution in a henselization of `Λ_𝔪` -- the approximation property for `Λ_𝔪^h`, which is the source's closing sentence. The G-ring property is NOT hypothesised anywhere here: in the Example it is the *conclusion* drawn from that approximation property (\"In this example we show that the local ring `O_{S, s}` has to be a G-ring in order for the result of Lemma 07XH to be true\"), and the conclusion of 07XH is assumed, in the antecedent, rather than derived from a G-ring assumption. NOT covered: the source's final step, from the approximation property of `Λ_𝔪^h` to `Λ_𝔪^h` and then `Λ_𝔪` being G-rings, which the Stacks Project itself defers (\"insert future reference here\"), so there is no statement to formalize against.”.

> Let `Λ` be a Noetherian ring, let `𝔪 ⊂ Λ` be a maximal
> ideal, let `R = Λ_𝔪^∧`, and let `Λ → C → R` be a factorization with `C` of finite type over
> `Λ`. Set `S = Spec(Λ)`, `U = S ∖ {𝔪}` and `S' = U ⨿ Spec(C)`, and let `F`, `𝒳 = 𝒮_F` and `ξ`
> be the functor on the big fppf site of `S`, the category fibred in sets it defines, and the
> formal object over `R` that the Example builds from that factorization. Then
>
> * `F` is the functor the Example displays: its value at `T` is a subsingleton, and it is
>   nonempty exactly when the structure morphism of `T` factors through `S'`,
> * `𝒳 → (Sch/S)_{fppf}` is limit preserving on objects,
> * `ξ` is effective,
> * `ξ` is versal, relative to `𝒪_{S, 𝔪}`, and
> * **if** the conclusion of Stacks 07XH holds for all of these `𝒳` -- that is, if every
>   factorization `Λ → C' → R` with `C'` of finite type over `Λ` carries the three-item datum
>   `Deformation.Artin.AlgebraizesFiniteTypeFactorizations` that the Example reads off that
>   conclusion, namely a finite type `Λ`-algebra `A` with a maximal ideal `𝔪_A` over `𝔪` such
>   that `κ(𝔪) = κ(𝔪_A)`, such that `Λ → A` satisfies condition (4) of Stacks 02HT at `𝔪_A`
>   -- hence is smooth there -- and such that `C'` maps to `A` over `Λ` -- then `C` maps to
>   every henselian local `Λ`-algebra `H` whose maximal ideal contracts to `𝔪` by a
>   `Λ`-algebra map, and every finite system of polynomial equations over `Λ` with a solution
>   in `R` has a solution in a henselization of `Λ_𝔪`.
>
> **No G-ring hypothesis is made, and the conclusion of Stacks 07XH is assumed rather than
> used:** it enters only as the antecedent of the last clause.

```lean
public theorem exists_algHom_henselian (hφ : RingHom.FiniteType φ) :
    (∀ T : (AlgebraicGeometry.BigFppfOver B (Spec (CommRingCat.of Λ)) hS)ᵒᵖ,
        Subsingleton ((functor m C φ B hS).obj T) ∧
          (Nonempty ((functor m C φ B hS).obj T) ↔ Factors m C φ B hS T.unop)) ∧
      AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B
        (Spec (CommRingCat.of Λ)) hS (stack m C φ B hS)
        (Deformation.Artin.Approximation.baseFiberedCategory B (Spec (CommRingCat.of Λ)) hS)
        (Deformation.Artin.Approximation.structureMorphism B (Spec (CommRingCat.of Λ)) hS
          (stack m C φ B hS)) ∧
      Deformation.Artin.FormalObject.IsEffective B (Spec (CommRingCat.of Λ)) hS
        (stack m C φ B hS).val.p ((stack m C φ B hS).isFiberedInGroupoids)
        (formalObject m C φ B hS ψ hψ hR) ∧
      (@Deformation.Artin.FormalObject.IsVersal B (Spec (CommRingCat.of Λ)) hS _ _
        (stack m C φ B hS).val.p ((stack m C φ B hS).isFiberedInGroupoids)
        (formalObject m C φ B hS ψ hψ hR) (stalkPoint m) _
        (algebra_formalObject_base_stalk m C φ B hS ψ hψ hR)
        ((Spec (CommRingCat.of Λ)).fromSpecStalk (point m))
        (base_toS_eq_stalk m C φ B hS ψ hψ hR)) ∧
      (Deformation.Artin.AlgebraizesFiniteTypeFactorizations Λ m (completion m) →
        (∀ (H : Type u) [CommRing H] [HenselianLocalRing H] [Algebra Λ H],
            m = (maximalIdeal H).comap (algebraMap Λ H) →
            ∃ χ : C →+* H, χ.comp φ = algebraMap Λ H) ∧
          ∀ (H : Type u) [CommRing H] [IsLocalRing H] [Algebra Λ H]
              [Algebra (Localization.AtPrime m) H]
              [IsScalarTower Λ (Localization.AtPrime m) H]
              [IsHenselization (Localization.AtPrime m)
                (ResidueField (Localization.AtPrime m)) H]
              (n k : ℕ) (f : Fin k → MvPolynomial (Fin n) Λ) (a : Fin n → completion m),
            (∀ j, MvPolynomial.aeval a (f j) = 0) →
              ∃ b : Fin n → H, ∀ j, MvPolynomial.aeval b (f j) = 0)
```

**`Deformation.Artin.GRingNecessity.hasApproximationProperty_and_isGRing_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingNecessity.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingNecessity.lean#L87). The attribute's comment: “the approximation property of the henselization `Λ_𝔪^h` and, by Rotthaus' theorem (the reference the source leaves missing), that `Λ_𝔪^h` is a G-ring”.

> **Stacks Example 98.12.8 (Tag 07XI), the approximation property of `Λ_𝔪^h`.** If the
> conclusion of Lemma 98.12.7 holds for the categories `𝒳 = 𝒮_F` and formal objects `ξ` of the
> Example, then every henselization `H` of `Λ_𝔪` has the approximation property (a system of
> polynomial equations over `H` with a solution in the completion of `H` has a solution in `H`) and
> is a G-ring. The second assertion is Rotthaus' theorem, the reference missing in the source.

```lean
theorem hasApproximationProperty_and_isGRing_henselization
    (h : ∀ (C : Type u) [CommRing C] [Algebra Λ C], Algebra.FiniteType Λ C →
      ∀ φ : C →ₐ[Λ] Completion 𝔪,
        AlgebraizationConclusion B (AlgebraicGeometry.Spec (.of Λ)) hS
          (factorizationCategory 𝔪 C B hS) (formalObject 𝔪 C φ B hS))
    (H : Type u) [CommRing H] [IsLocalRing H] [Algebra Λ H] [Algebra (Localization.AtPrime 𝔪) H]
    [IsScalarTower Λ (Localization.AtPrime 𝔪) H]
    [IsHenselization (Localization.AtPrime 𝔪) (ResidueField (Localization.AtPrime 𝔪)) H] :
    HasApproximationProperty H ∧ IsGRing H
```

**`Deformation.Artin.GRingNecessity.isGRing_of_forall_algebraizationConclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingNecessity.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingNecessity.lean#L113). The attribute's comment: “the conclusion of the Example: if the conclusion of Lemma 98.12.7 (07XH) holds for every `𝒳 = 𝒮_F` as above, then `Λ_𝔪` is a G-ring; the conclusion of 07XH is `AlgebraizationConclusion`, copied verbatim from the formalization of 07XH”.

> **Stacks Example 98.12.8 (Tag 07XI).** Let `Λ` be a Noetherian ring and `𝔪` a maximal ideal
> of `Λ`. If for every finite type `Λ`-algebra `C` and every `Λ`-algebra map `φ : C → Λ_𝔪^∧` the
> conclusion of Lemma 98.12.7 (Tag 07XH) holds for the category `𝒳 = 𝒮_F` fibred in sets over the
> big fppf site of `S = Spec Λ` attached to `S' = (S ∖ {𝔪}) ⨿ Spec C` and its effective versal formal
> object `ξ` over `Λ_𝔪^∧`, then `Λ_𝔪` is a G-ring.

```lean
theorem isGRing_of_forall_algebraizationConclusion
    (h : ∀ (C : Type u) [CommRing C] [Algebra Λ C], Algebra.FiniteType Λ C →
      ∀ φ : C →ₐ[Λ] Completion 𝔪,
        AlgebraizationConclusion B (AlgebraicGeometry.Spec (.of Λ)) hS
          (factorizationCategory 𝔪 C B hS) (formalObject 𝔪 C φ B hS)) :
    IsGRing (Localization.AtPrime 𝔪)
```

**`Deformation.Artin.GRingNecessity.isGRing_of_forall_algebraizationLemmaHolds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingNecessity.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingNecessity.lean#L130). The attribute's comment: “with Lemma 98.12.7 assumed in lemma form (for every formal object of `𝒳` satisfying its hypotheses other than the G-ring hypothesis): `Λ_𝔪` is a G-ring”.

> **Stacks Example 98.12.8 (Tag 07XI), with Lemma 98.12.7 assumed in lemma form.** If for
> every finite type `Λ`-algebra `C` the statement of Lemma 98.12.7 (Tag 07XH) without its G-ring
> hypothesis holds for the category `𝒳 = 𝒮_F` of the Example (`AlgebraizationLemmaHolds`), then
> `Λ_𝔪` is a G-ring.

```lean
theorem isGRing_of_forall_algebraizationLemmaHolds
    (h : ∀ (C : Type u) [CommRing C] [Algebra Λ C], Algebra.FiniteType Λ C →
      AlgebraizationLemmaHolds 𝔪 B hS C) :
    IsGRing (Localization.AtPrime 𝔪)
```

**`Deformation.Artin.GRingNecessity.exists_lift_smallExtension_of_algebraizationConclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingNecessity/Datum.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingNecessity/Datum.lean#L147). The attribute's comment: “the datum read off the conclusion of 07XH: `A` of finite type, `𝔪_A` over `𝔪` with `κ(𝔪) = κ(𝔪_A)`, condition (4) of 02HT for `Λ → A` at `𝔪_A`, and `C → A`”.

> **Stacks Example 98.12.8, from the conclusion of Stacks 07XH to the datum.** Let `C` be a
> finite type `Λ`-algebra (as in the source; the proof does not use this) and `φ : C → Λ_𝔪^∧` a
> `Λ`-algebra map. If the conclusion of Stacks Lemma 98.12.7 holds for the category `𝒳 = 𝒮_F` and
> the formal object `ξ` of the Example, then there are a finite type `Λ`-algebra `A` and a maximal
> ideal `𝔪_A` of `A` lying over `𝔪`, with `κ(𝔪) → κ(𝔪_A)` bijective and `Λ → A`, `𝔪_A` satisfying
> condition (4) of Stacks 02HT (the last condition of `Algebra.isSmoothAt_tfae`), together with a
> `Λ`-algebra map `C → A`.

```lean
theorem exists_lift_smallExtension_of_algebraizationConclusion [Algebra.FiniteType Λ C]
    (h : AlgebraizationConclusion B (Spec (.of Λ)) hS (factorizationCategory 𝔪 C B hS)
      (formalObject 𝔪 C φ B hS)) :
    ∃ (A : Type u) (_ : CommRing A) (_ : Algebra Λ A), Algebra.FiniteType Λ A ∧
      ∃ (mA : Ideal A) (_ : mA.IsMaximal) (hmA : 𝔪 = mA.comap (algebraMap Λ A)),
        Function.Bijective (Ideal.ResidueField.map 𝔪 mA (algebraMap Λ A) hmA) ∧
        (∀ (T₂ T₁ : Type u) [CommRing T₂] [CommRing T₁] [IsLocalRing T₂] [IsLocalRing T₁]
          [IsArtinianRing T₂] [IsArtinianRing T₁] [Algebra Λ T₂] [Algebra Λ T₁]
          (e : T₂ →ₐ[Λ] T₁), Function.Surjective e →
          IsSimpleModule T₂ (RingHom.ker (e : T₂ →+* T₁)) →
          ∀ (g : A →ₐ[Λ] T₁) (hq : (maximalIdeal T₁).comap (g : A →+* T₁) = mA),
            Function.Surjective (Ideal.ResidueField.mapₐ mA (maximalIdeal T₁) g hq.symm) →
            ∃ g' : A →ₐ[Λ] T₂, e.comp g' = g) ∧
        Nonempty (C →ₐ[Λ] A)
```

**`Deformation.Artin.GRingNecessity.isLimitPreservingOnObjects_and_formalObject_isEffective_isVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Versality/GRingNecessity/Hypotheses.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/Versality/GRingNecessity/Hypotheses.lean#L60). The attribute's comment: “first assertion of the Example: `𝒳 = 𝒮_F` is limit preserving on objects and has an effective, versal formal object `ξ` over `R = Λ_𝔪^∧`”.

> **Stacks Example 98.12.8 (Tag 07XI), the properties of `𝒳` and `ξ`.** Let `C` be a finite
> type `Λ`-algebra and `φ : C → Λ_𝔪^∧` a `Λ`-algebra map. The category `𝒳 = 𝒮_F` fibred in sets
> over the big fppf site of `S = Spec Λ` is limit preserving on objects, and `ξ` is a formal object
> of `𝒳` over `R = Λ_𝔪^∧` (its base is isomorphic to `R` over `S`) which is effective and versal.
> Versality holds over the local ring `𝒪_{S,s}` of `S` at any point `s`, for every algebra
> structure of the base of `ξ` over `𝒪_{S,s}` compatible with the structure morphisms, and such a
> structure exists at the image `formalObjectPoint` of the closed point of the base, where the
> versality hypothesis of Lemma 98.12.7 is formulated.

```lean
theorem isLimitPreservingOnObjects_and_formalObject_isEffective_isVersal
    (C : Type u) [CommRing C] [Algebra Λ C] [Algebra.FiniteType Λ C]
    (φ : C →ₐ[Λ] Completion 𝔪) :
    BigFppfOver.IsLimitPreservingOnObjects.{u, u, u, u, u + 1} B (Spec (.of Λ)) hS
        (factorizationCategory 𝔪 C B hS)
        (Approximation.baseFiberedCategory B (Spec (.of Λ)) hS)
        (Approximation.structureMorphism B (Spec (.of Λ)) hS (factorizationCategory 𝔪 C B hS)) ∧
      IsCompletionBase 𝔪 (formalObject 𝔪 C φ B hS).base ∧
      FormalObject.IsEffective B (Spec (.of Λ)) hS (factorizationCategory 𝔪 C B hS).val.p
        (factorizationCategory 𝔪 C B hS).property (formalObject 𝔪 C φ B hS) ∧
      (∃ _ : Algebra ((Spec (.of Λ)).presheaf.stalk (formalObjectPoint 𝔪 C B hS φ) : Type u)
          (formalObject 𝔪 C φ B hS).base.R,
        Spec.map (CommRingCat.ofHom (algebraMap
            ((Spec (.of Λ)).presheaf.stalk (formalObjectPoint 𝔪 C B hS φ) : Type u)
            (formalObject 𝔪 C φ B hS).base.R)) ≫
          (Spec (.of Λ)).fromSpecStalk (formalObjectPoint 𝔪 C B hS φ) =
        (formalObject 𝔪 C φ B hS).base.toS) ∧
      ∀ (s : Spec (.of Λ))
        [Algebra ((Spec (.of Λ)).presheaf.stalk s : Type u) (formalObject 𝔪 C φ B hS).base.R]
        (iΛ : Spec (.of ((Spec (.of Λ)).presheaf.stalk s : Type u)) ⟶ Spec (.of Λ))
        (_ : iΛ = (Spec (.of Λ)).fromSpecStalk s)
        (hΛ : Spec.map (CommRingCat.ofHom (algebraMap
            ((Spec (.of Λ)).presheaf.stalk s : Type u) (formalObject 𝔪 C φ B hS).base.R)) ≫ iΛ =
          (formalObject 𝔪 C φ B hS).base.toS),
        FormalObject.IsVersal B (Spec (.of Λ)) hS (factorizationCategory 𝔪 C B hS).val.p
          (factorizationCategory 𝔪 C B hS).property (formalObject 𝔪 C φ B hS)
          ((Spec (.of Λ)).presheaf.stalk s : Type u) iΛ hΛ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.12, Tag 07XD](https://stacks.math.columbia.edu/tag/07XD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
