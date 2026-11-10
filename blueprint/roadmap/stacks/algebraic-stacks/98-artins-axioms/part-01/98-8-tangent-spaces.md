---
declaration: section
origin: cited
lean: Deformation.Artin.tangentSpaceModuleOfSatisfiesRS, Deformation.Artin.tangentSpaceModuleOfSatisfiesRS_carrier, Deformation.Artin.infinitesimalAutomorphismModuleOfSatisfiesRS, Deformation.Artin.infinitesimalAutomorphismModuleOfSatisfiesRS_carrier, Deformation.Artin.isFiniteDimensionalDeformationCategory_predeformationCategory_iff, Deformation.Artin.squareZeroLiftClasses, Deformation.Artin.infinitesimalAutomorphisms_equiv_restrictionKernel, Deformation.Artin.isFiniteDimensionalDeformationCategory_of_isAlgebraicStack
statement: formalized
proof: formalized
---

# 98.8 Tangent spaces

Section 98.8 of the Stacks Project, [Tag 07WY](https://stacks.math.columbia.edu/tag/07WY). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07WY, the section

[Tag 07WY](https://stacks.math.columbia.edu/tag/07WY) in the Stacks Project.

**`Deformation.Artin.tangentSpaceModuleOfSatisfiesRS`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean#L99). The attribute's comment: “if X satisfies (RS), TF\_\{X,k,x\_0} has a natural k-vector space structure (Lemma 06IH, assumptions by Lemma 07WU and Remark 07WV)”.

> **The tangent space as a vector space.** For `𝒳` satisfying (RS), the tangent space
> `T𝓕_{𝒳,k,x₀}` of the predeformation category, with the natural `k`-vector space structure of
> Stacks 06IH.

```lean
def tangentSpaceModuleOfSatisfiesRS : ModuleCat.{max (u + 1) v w} k
```

**`Deformation.Artin.tangentSpaceModuleOfSatisfiesRS_carrier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean#L116). The attribute's comment: “the underlying set of the k-vector space TF\_\{X,k,x\_0} is the set of isomorphism classes of objects of F\_\{X,k,x\_0} over k[ε]”.

> The underlying set of the `k`-vector space `tangentSpaceModuleOfSatisfiesRS` is the tangent
> space `T𝓕_{𝒳,k,x₀}`: the set of isomorphism classes of the fibre of `𝓕_{𝒳,k,x₀}` over the dual
> numbers `k[ε]`, that is of morphisms `x₀ ⟶ x` of `𝒳` over `Spec k ⟶ Spec k[ε]`.

```lean
theorem tangentSpaceModuleOfSatisfiesRS_carrier :
    let D := predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀
    letI := D.category
    ((tangentSpaceModuleOfSatisfiesRS B S hS p hp hRS iΛ x₀ hx₀ hfinite hqc : ModuleCat k) :
        Type _) =
      Quotient (isIsomorphicSetoid
        (D.projection.Fiber (artinianDualNumbers.{u, u, u} Λ k)))
```

**`Deformation.Artin.infinitesimalAutomorphismModuleOfSatisfiesRS`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean#L133). The attribute's comment: “Inf(F\_\{X,k,x\_0}) has a natural k-vector space structure (Lemma 06JX)”.

> **Infinitesimal automorphisms as a vector space.** For `𝒳` satisfying (RS), the
> infinitesimal automorphisms `Inf(𝓕_{𝒳,k,x₀})` at an object `x` of `𝓕_{𝒳,k,x₀}` over `k` and a
> choice `P` of pushforwards of `x`, with the natural `k`-vector space structure of Stacks 06JX (the
> value at the rank-one module of the canonical linear lift of `M ↦ Inf(x[M]/x)`).

```lean
def infinitesimalAutomorphismModuleOfSatisfiesRS
    (x : (letI := (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).category
      (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection.Fiber
        (residueFieldObject.{u, u, u} Λ k)))
    (P : letI := (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).category
      ChosenPushforwardsAt (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection
        x.1) :
    ModuleCat.{max u w} k
```

**`Deformation.Artin.infinitesimalAutomorphismModuleOfSatisfiesRS_carrier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean#L154). The attribute's comment: “the k-vector space structure on Inf(F\_\{X,k,x\_0}) is such that addition agrees with composition of automorphisms”.

> **Addition on `Inf` is composition.** The underlying set of
> `infinitesimalAutomorphismModuleOfSatisfiesRS` is the kernel of the restriction homomorphism
> `Aut(x'₀) ⟶ Aut(x)` from the automorphisms of the chosen dual-number pushforward `x'₀` of `x`
> to those of `x` over `k`; under this identification addition is composition of automorphisms,
> and multiplication by `c ∈ k` is transport along the scaling `ε ↦ cε` of the dual numbers.

```lean
theorem infinitesimalAutomorphismModuleOfSatisfiesRS_carrier
    (x : (letI := (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).category
      (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection.Fiber
        (residueFieldObject.{u, u, u} Λ k)))
    (P : letI := (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).category
      ChosenPushforwardsAt (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection
        x.1) :
    letI := (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).category
    ∃ h : ((infinitesimalAutomorphismModuleOfSatisfiesRS B S hS p hp hRS iΛ x₀ hx₀ hfinite hqc
        x P : ModuleCat k) : Type _) =
        infinitesimalAutomorphismKernel P
          (squareZeroUnderRed (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀
            hx₀).projection x.1 (FGModuleCat.of k (ULift.{u} k))),
      (∀ a b, cast h (a + b) = cast h a * cast h b) ∧
        ∀ (c : k) a, (cast h (c • a)).1 =
          P.transportAutHom (squareZeroUnderMap
            (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection x.1
            (FGModuleCat.ofHom (c • LinearMap.id : ULift.{u} k →ₗ[k] ULift.{u} k)))
            (cast h a).1
```

**`Deformation.Artin.isFiniteDimensionalDeformationCategory_predeformationCategory_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/TangentSpaceVectorStructure.lean#L198). The attribute's comment: “the natural condition: the vector spaces TF\_\{X,k,x\_0} and Inf(F\_\{X,k,x\_0}) have finite dimension”.

> **The finite-dimensionality condition.** For `𝒳` satisfying (RS), the condition
> `Deformation.IsFiniteDimensionalDeformationCategory` on `𝓕_{𝒳,k,x₀}` holds exactly when the two
> vector spaces `T𝓕_{𝒳,k,x₀}` and `Inf(𝓕_{𝒳,k,x₀})` (at every object over `k` and every choice of
> pushforwards) are finite dimensional.

```lean
theorem isFiniteDimensionalDeformationCategory_predeformationCategory_iff :
    letI := (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).category
    IsFiniteDimensionalDeformationCategory.{u, u, u}
        (predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀).projection ↔
      FiniteDimensional k
          (tangentSpaceModuleOfSatisfiesRS B S hS p hp hRS iΛ x₀ hx₀ hfinite hqc) ∧
        ∀ x P, FiniteDimensional k
          (infinitesimalAutomorphismModuleOfSatisfiesRS B S hS p hp hRS iΛ x₀ hx₀ hfinite hqc
            x P)
```

## Tag 07WZ, an equation

[Tag 07WZ](https://stacks.math.columbia.edu/tag/07WZ) in the Stacks Project.

**`Deformation.Artin.squareZeroLiftClasses`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TangentFunctor.lean, line 923](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Infinitesimal/TangentFunctor.lean#L923). The attribute's comment: “lift classes at the dual numbers”.

> Isomorphism classes of lifts of `x` to `Spec A[M]`, together with their identification
> with `x` after restriction to `Spec A`.

```lean
public abbrev squareZeroLiftClasses (M : SiteModule A B) : Type _
```

## Tag 07X0, an equation

[Tag 07X0](https://stacks.math.columbia.edu/tag/07X0) in the Stacks Project.

**`Deformation.Artin.infinitesimalAutomorphisms_equiv_restrictionKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/TangentSpace.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/TangentSpace.lean#L403).

> **Infinitesimal automorphisms of `𝓕_{𝓧,k,x₀}`.** Let `𝓧` be fibred in groupoids over the
> big fppf site of `S` and let `x₀` lie over `Spec k`. For a pushforward `z₀ ⟶ zε` of a point of
> the special fibre along the constant inclusion `k ⟶ k[ε]`, the infinitesimal automorphisms of
> the predeformation category `𝓕_{𝓧,k,x₀}` are canonically the kernel of the restriction
> homomorphism from the automorphisms of the dual-number object `x₀'` of `𝓧` to the
> automorphisms of `x₀`; the identification keeps the underlying arrow of `𝓧`.

```lean
public theorem infinitesimalAutomorphisms_equiv_restrictionKernel
    (B : BigFppfSite.{u})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    {S : Scheme.{u}} (contains : B.Contains S) (iΛ : Spec (.of Λ) ⟶ S)
    {X : Type v} [Category.{w} X]
    (p : X ⥤ BigFppfOver B S contains)
    (fibered : p.IsFiberedInGroupoids) (x₀ : X)
    (hx₀ : (p ⋙ Over.post B.inclusion).obj x₀ = Over.mk
      (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let D := predeformationCategory iΛ (p ⋙ Over.post B.inclusion) x₀ hx₀
    letI : Category.{max u w} D.carrier := D.category
    ∀ {A₀ Aε : ArtinianLocalAlgCat.{u, u, u} Λ k}
      {z₀ : D.projection.Fiber A₀} {zε : D.projection.Fiber Aε}
      (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀)
      (hpair : IsCanonicalDualNumberPair g e)
      (i : z₀.1 ⟶ zε.1) (hi : D.projection.IsHomLift g i),
      let y := (D.objects zε.1).point
      let xε' : p.op.Fiber (Opposite.op (p.obj y)) := ⟨Opposite.op y, rfl⟩
      let x₀' : p.op.Fiber (Opposite.op (p.obj x₀)) := ⟨Opposite.op x₀, rfl⟩
      let r := (D.objects zε.1).arrow
      let restriction : Aut xε' →* Aut x₀' :=
        pushforwardAutomorphismHom
          (p := p.op) (x' := xε') (x := x₀')
          (isCofiberedInGroupoids_op_of_isFiberedInGroupoids fibered)
          (p.op.map r.op) r.op (Functor.IsHomLift.map (p := p.op) r.op)
      ∃! E : ↥(infinitesimalAutomorphisms
          (predeformationCategory_isPredeformationCategory B contains iΛ p x₀ hx₀
            fibered).cofibered g e hpair i hi) ≃* ↥(MonoidHom.ker restriction),
        ∀ a, (E a).val.asIso.hom.val.unop =
          (D.morphisms zε.1 zε.1 a.val.asIso.hom.val).arrow
```

## Tag 07X1, a lemma

[Tag 07X1](https://stacks.math.columbia.edu/tag/07X1) in the Stacks Project.

**`Deformation.Artin.isFiniteDimensionalDeformationCategory_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/AlgebraicStackFiniteDimensional.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/AlgebraicStackFiniteDimensional.lean#L351).

> **Stacks Project, Tag 07X1.** Let `S` be a locally Noetherian scheme, `𝒳` an algebraic
> stack over `S`, `U` a scheme locally of finite type over `S`, and `(Sch/U) ⟶ 𝒳` a smooth
> surjective 1-morphism. For every deformation category `𝓕 = 𝓕_{𝒳,k,x₀}` of Tag 07T2 — a point
> `x₀` of `𝒳` over a field `k` of finite type over `S`, and an affine open `Spec Λ ⊂ S` through
> which `Spec k ⟶ S` factors with `Λ ⟶ k` finite — the tangent space `T𝓕` and the space of
> infinitesimal automorphisms `Inf(𝓕)` are finite dimensional over `k`.

```lean
theorem isFiniteDimensionalDeformationCategory_of_isAlgebraicStack [IsLocallyNoetherian S]
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) (U : BigFppfOver B S hS)
    [LocallyOfFiniteType (B.inclusion.map U.hom)]
    (a : Stack.schemeStack.{u, w} B S hS U ⟶ 𝒳)
    (hsurj : Stack.IsSurjective B S hS a) (hsm : Stack.AlgebraicStacks.IsSmooth B S hS a)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) [IsOpenImmersion iΛ]
    (x₀ : 𝒳.val.val.obj)
    (hx₀ : (𝒳.val.val.p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let D := predeformationCategory iΛ (𝒳.val.val.p ⋙ Over.post B.inclusion) x₀ hx₀
    letI := D.category
    IsFiniteDimensionalDeformationCategory D.projection
```

**`Deformation.Artin.isFiniteDimensionalDeformationCategory_of_algebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/FiniteDimensional/AlgebraicStack.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/FiniteDimensional/AlgebraicStack.lean#L53).

> Let `S` be a locally Noetherian scheme, `𝒳` an algebraic stack over `S`, `U` a scheme locally
> of finite type over `S` and `f : (Sch/U)_{fppf} ⟶ 𝒳` a smooth surjective 1-morphism. Then for every
> `𝓕 = 𝓕_{𝒳,k,x₀}` as in Section 07T2 — `k` a field of finite type over `S`, `Spec Λ ⊆ S` an affine
> open through which `Spec k ⟶ S` factors with `Λ → k` finite, `x₀` an object of `𝒳` over `Spec k`
> — the tangent space `T𝓕` and the infinitesimal automorphisms `Inf(𝓕)` are finite-dimensional over
> `k`, for the vector-space structures of the deformation category `𝓕`.

```lean
theorem isFiniteDimensionalDeformationCategory_of_algebraicStack [IsLocallyNoetherian S]
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (U : BigFppfOver B S hS) [LocallyOfFiniteType (B.inclusion.map U.hom)]
    (f : Stack.schemeFibredCategory B S hS U ⟶ 𝒳.val)
    (hf : Stack.IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hsmoothsurj : ∀ (W : BigFppfOver B S hS)
      (yv : BigFppfOver B W.left.1 W.left.2 ⥤ 𝒳.val.val.obj)
      (_hyv : yv ⋙ 𝒳.val.val.p = Over.map W.hom)
      (F : (BigFppfOver B W.left.1 W.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B W.left.1 W.left.2 F),
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.fst (Over.map W.hom) (Stack.schemeFibredCategory B S hS U).val.p
          𝒳.val.val.p yv (CatFiberedInGroupoids.homFunctor f))
        (presheafOfCategories (F ⋙ typeToCat)).p) →
      (let h := (algebraicSpaceMap B S hS W
        ((spacesOverSmallerBaseFunctor B W.left.1 S W.left.2 hS W.hom).obj ⟨F, hF⟩)).hom
       Space.IsSurjective B S hS h ∧ Space.IsSmooth B S hS h))
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) (hiΛ : IsOpenImmersion iΛ) (x₀ : 𝒳.val.val.obj)
    (hx₀ : (𝒳.val.val.p ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    letI := (predeformationCategory iΛ (𝒳.val.val.p ⋙ Over.post B.inclusion) x₀ hx₀).category
    IsFiniteDimensionalDeformationCategory
      (predeformationCategory iΛ (𝒳.val.val.p ⋙ Over.post B.inclusion) x₀ hx₀).projection
```

## Tag 07X2, a lemma

[Tag 07X2](https://stacks.math.columbia.edu/tag/07X2) in the Stacks Project.

**`Deformation.Artin.sixTermExact_twoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ArtinCriteria/TangentSpace/SixTermExact.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ArtinCriteria/TangentSpace/SixTermExact.lean#L202).

> **Stacks Project, Tag 07X2**, the full six-term exact sequence.
>
> Let `S` be a locally Noetherian scheme, let `Φ : 𝒳 ⟶ 𝒴` and `Ψ : 𝒵 ⟶ 𝒴` be `1`-morphisms
> of categories fibred in groupoids over the big fppf site of `S`, and assume `𝒳`, `𝒴`, `𝒵`
> satisfy (RS). Let `k` be a field of finite type over `S` and let `w₀` be an object of
> `𝒲 = 𝒳 ×_𝒴 𝒵` over `k`, with induced objects `x₀`, `y₀ = Φ(x₀)`, `z₀` of `𝒳`, `𝒴`,
> `𝒵`. Then
>
> `0 → Inf(𝓕_𝒲) → Inf(𝓕_𝒳) ⊕ Inf(𝓕_𝒵) → Inf(𝓕_𝒴) → T𝓕_𝒲 → T𝓕_𝒳 ⊕ T𝓕_𝒵 → T𝓕_𝒴`
>
> is an exact sequence, with the first pair of maps induced by the two projections of `𝒲`, the
> first difference by the maps induced by `Φ` and by `Ψ` (the latter transported along the
> comparison isomorphism `ψ(w₀) : Φ(x₀) ≅ Ψ(z₀)`), a boundary map out of `Inf(𝓕_𝒴)`, and again
> the pair of projections and the difference of the maps induced by `Φ` and `Ψ`, now on tangent
> spaces.
>
> The square of predeformation categories is a `2`-fibre product (Tag 07WL): the comparison
> `1`-morphism from `𝒲` to `CategoryTheory.TwoFibreProductOver` is an equivalence
> (`Deformation.Artin.fibreProductOfPredeformationCategoriesOfEssSurj`). Each of the five
> exactness/injectivity claims of the abstract six-term sequence for the literal `2`-fibre product
> (Tag 06L5, `Deformation.SixTerm.twoFibreProduct_sixTermExact`) is transported along this
> equivalence, respectively by `Deformation.injective_infProjPairOfLift`,
> `Deformation.exact_infProjPairOfLift`, `Deformation.exact_infLegDiff_infBoundaryLinearMapOfLift`,
> `Deformation.exact_infBoundaryLinearMapOfLift_tangentProjPairOfLift` and
> `Deformation.exact_tangentPairOfLift_tangentLegDiffOfEq`.

```lean
public theorem sixTermExact_twoFibreProduct
    (hΦ : Φ ⋙ p𝒴 = p𝒳) (hΨ : Ψ ⋙ p𝒴 = p𝒵)
    (h𝒳 : p𝒳.IsFiberedInGroupoids) (h𝒴 : p𝒴.IsFiberedInGroupoids)
    (h𝒵 : p𝒵.IsFiberedInGroupoids)
    (hRS𝒳 : SatisfiesRS B S hS p𝒳 h𝒳) (hRS𝒴 : SatisfiesRS B S hS p𝒴 h𝒴)
    (hRS𝒵 : SatisfiesRS B S hS p𝒵 h𝒵)
    (w₀ : TwoFibreProductOver p𝒳 p𝒵 p𝒴 Φ Ψ)
    (hw₀base : (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙
      Over.post B.inclusion).obj w₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
      (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hqc : QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let hA := fst_comp_post_eq B S hS p𝒳 p𝒴 p𝒵 Φ Ψ
    let hB := snd_comp_post_eq B S hS p𝒳 p𝒴 p𝒵 Φ Ψ
    let hF : Φ ⋙ p𝒴 ⋙ Over.post B.inclusion = p𝒳 ⋙ Over.post B.inclusion :=
      congrArg (fun H => H ⋙ Over.post B.inclusion) hΦ
    let hG : Ψ ⋙ p𝒴 ⋙ Over.post B.inclusion = p𝒵 ⋙ Over.post B.inclusion :=
      congrArg (fun H => H ⋙ Over.post B.inclusion) hΨ
    let hX := imageBasePoint (qY := p𝒳 ⋙ Over.post B.inclusion) iΛ
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙ Over.post B.inclusion)
      (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ) hA w₀ hw₀base
    let hZ := imageBasePoint (qY := p𝒵 ⋙ Over.post B.inclusion) iΛ
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙ Over.post B.inclusion)
      (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 Φ Ψ) hB w₀ hw₀base
    let hY := imageBasePoint (qY := p𝒴 ⋙ Over.post B.inclusion) iΛ
      (p𝒳 ⋙ Over.post B.inclusion) Φ hF ((TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀) hX
    let D𝒲 := predeformationCategory iΛ
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙ Over.post B.inclusion) w₀ hw₀base
    let D𝒳 := predeformationCategory iΛ (p𝒳 ⋙ Over.post B.inclusion)
      ((TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀) hX
    let D𝒵 := predeformationCategory iΛ (p𝒵 ⋙ Over.post B.inclusion)
      ((TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀) hZ
    let D𝒴 := predeformationCategory iΛ (p𝒴 ⋙ Over.post B.inclusion)
      (Φ.obj ((TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀)) hY
    letI := D𝒲.category
    letI := D𝒳.category
    letI := D𝒵.category
    letI := D𝒴.category
    let mA := mapPredeformationCategory iΛ
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙ Over.post B.inclusion)
      (p𝒳 ⋙ Over.post B.inclusion) (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ) hA w₀ hw₀base
    let mB := mapPredeformationCategory iΛ
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙ Over.post B.inclusion)
      (p𝒵 ⋙ Over.post B.inclusion) (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 Φ Ψ) hB w₀ hw₀base
    let mF := mapPredeformationCategory iΛ (p𝒳 ⋙ Over.post B.inclusion)
      (p𝒴 ⋙ Over.post B.inclusion) Φ hF
      ((TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀) hX
    let data := fibreProductOfPredeformationCategoriesOfEssSurj iΛ
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ ⋙ Over.post B.inclusion)
      (p𝒳 ⋙ Over.post B.inclusion) (p𝒵 ⋙ Over.post B.inclusion)
      (p𝒴 ⋙ Over.post B.inclusion) (TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ)
      (TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 Φ Ψ) Φ Ψ hA hB hF
      (TwoFibreProductOver.psiIso p𝒳 p𝒵 p𝒴 Φ Ψ) w₀ hw₀base hG
      (isHomLift_psiIso_post B S hS p𝒳 p𝒴 p𝒵 Φ Ψ)
      (exists_liftPost_iso_over_base B S hS p𝒳 p𝒴 p𝒵 Φ Ψ)
      (isEquivalence_liftPost B S hS p𝒳 p𝒴 p𝒵 Φ Ψ)
    let hD𝒲 := isDeformationCategory_predeformationCategory B S hS
      (TwoFibreProductOver.structureFunctor p𝒳 p𝒵 p𝒴 Φ Ψ)
      (TwoFibreProductOver.isFiberedInGroupoids p𝒳 p𝒵 p𝒴 Φ Ψ h𝒳 h𝒵 h𝒴 hΦ hΨ)
      (satisfiesRS_twoFibreProductOver B S hS p𝒳 p𝒴 p𝒵 Φ Ψ h𝒳 h𝒴 h𝒵 hΦ hΨ
        hRS𝒳 hRS𝒴 hRS𝒵) iΛ w₀ hw₀base hfinite hqc
    let hD𝒳 := isDeformationCategory_predeformationCategory B S hS p𝒳 h𝒳 hRS𝒳 iΛ
      ((TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀) hX hfinite hqc
    let hD𝒵 := isDeformationCategory_predeformationCategory B S hS p𝒵 h𝒵 hRS𝒵 iΛ
      ((TwoFibreProductOver.snd p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀) hZ hfinite hqc
    let hD𝒴 := isDeformationCategory_predeformationCategory B S hS p𝒴 h𝒴 hRS𝒴 iΛ
      (Φ.obj ((TwoFibreProductOver.fst p𝒳 p𝒵 p𝒴 Φ Ψ).obj w₀)) hY hfinite hqc
    let hA' : mA.toFunctor ⋙ (mF.toFunctor ⋙ D𝒴.projection) = D𝒲.projection :=
      (congrArg (mA.toFunctor ⋙ ·) mF.projection_comm).trans mA.projection_comm
    let hB' : mB.toFunctor ⋙ (data.rightFunctor ⋙ D𝒴.projection) = D𝒲.projection :=
      (congrArg (mB.toFunctor ⋙ ·) data.rightFunctor_projection).trans mB.projection_comm
    let hH' : IsDeformationCategory (mF.toFunctor ⋙ D𝒴.projection) := mF.projection_comm ▸ hD𝒳
    let hG' : IsDeformationCategory (data.rightFunctor ⋙ D𝒴.projection) :=
      data.rightFunctor_projection ▸ hD𝒵
    let hlift' : (TwoFibreProductOver.lift (mF.toFunctor ⋙ D𝒴.projection)
        (data.rightFunctor ⋙ D𝒴.projection) D𝒴.projection mF.toFunctor data.rightFunctor
        D𝒲.projection mA.toFunctor mB.toFunctor hA' hB' data.filler
        data.filler_vertical).IsEquivalence :=
      Deformation.isEquivalence_lift_congr D𝒴.projection D𝒲.projection mF.toFunctor
        data.rightFunctor mA.toFunctor mB.toFunctor D𝒳.projection
        (mF.toFunctor ⋙ D𝒴.projection) mF.projection_comm.symm D𝒵.projection
        (data.rightFunctor ⋙ D𝒴.projection) data.rightFunctor_projection.symm
        mA.projection_comm hA' mB.projection_comm hB' data.filler data.filler_vertical
        data.isEquivalence
    letI := hlift'
    let w₀' : D𝒲.projection.Fiber (Deformation.residueFieldObject Λ k) :=
      (Classical.choice hD𝒲.predeformation.specialFiber).inverse.obj ⟨PUnit.unit⟩
    let hw₀ : (mF.toFunctor ⋙ D𝒴.projection).obj (mA.toFunctor.obj w₀'.1) =
        Deformation.residueFieldObject Λ k :=
      (Functor.congr_obj mF.projection_comm (mA.toFunctor.obj w₀'.1)).trans
        ((Functor.congr_obj mA.projection_comm w₀'.1).trans w₀'.2)
    let PW := Deformation.chosenPushforwardsAtOfCofiberedInGroupoids
      hD𝒲.predeformation.cofibered w₀'.1
    let QH := Deformation.chosenPushforwardsAtOfCofiberedInGroupoids
      hH'.predeformation.cofibered (mA.toFunctor.obj w₀'.1)
    let QG := Deformation.chosenPushforwardsAtOfCofiberedInGroupoids
      hG'.predeformation.cofibered (mB.toFunctor.obj w₀'.1)
    let PF := Deformation.chosenPushforwardsAtOfCofiberedInGroupoids
      hD𝒴.predeformation.cofibered (mF.toFunctor.obj (mA.toFunctor.obj w₀'.1))
    let PF' := Deformation.chosenPushforwardsAtOfCofiberedInGroupoids
      hD𝒴.predeformation.cofibered (data.rightFunctor.obj (mB.toFunctor.obj w₀'.1))
    let PL := Deformation.transportChosenPushforwardsAt
      (TwoFibreProductOver.lift (mF.toFunctor ⋙ D𝒴.projection)
        (data.rightFunctor ⋙ D𝒴.projection) D𝒴.projection mF.toFunctor data.rightFunctor
        D𝒲.projection mA.toFunctor mB.toFunctor hA' hB' data.filler data.filler_vertical)
      (TwoFibreProductOver.lift_comp_structureFunctor ..) w₀'.1 PW
    letI := Deformation.naturalLocalizedTangentAddCommGroup PW hD𝒲.satisfiesRS
    letI := Deformation.naturalLocalizedTangentModule PW hD𝒲.satisfiesRS
    letI := Deformation.naturalLocalizedTangentAddCommGroup QH hH'.satisfiesRS
    letI := Deformation.naturalLocalizedTangentModule QH hH'.satisfiesRS
    letI := Deformation.naturalLocalizedTangentAddCommGroup QG hG'.satisfiesRS
    letI := Deformation.naturalLocalizedTangentModule QG hG'.satisfiesRS
    letI := Deformation.naturalLocalizedTangentAddCommGroup PF hD𝒴.satisfiesRS
    letI := Deformation.naturalLocalizedTangentModule PF hD𝒴.satisfiesRS
    Function.Injective
      (LinearMap.prod
        (Deformation.inducedInfinitesimalLinearMapOfEq mA.toFunctor hA' hD𝒲.satisfiesRS
          hH'.satisfiesRS PW QH)
        (Deformation.inducedInfinitesimalLinearMapOfEq mB.toFunctor hB' hD𝒲.satisfiesRS
          hG'.satisfiesRS PW QG)) ∧
    Function.Exact
      (LinearMap.prod
        (Deformation.inducedInfinitesimalLinearMapOfEq mA.toFunctor hA' hD𝒲.satisfiesRS
          hH'.satisfiesRS PW QH)
        (Deformation.inducedInfinitesimalLinearMapOfEq mB.toFunctor hB' hD𝒲.satisfiesRS
          hG'.satisfiesRS PW QG))
      (Deformation.infLegDiff D𝒴.projection mF.toFunctor data.rightFunctor hH' hG' hD𝒴
        (w₀ :=
          (⟨D𝒲.projection.obj w₀'.1, mA.toFunctor.obj w₀'.1, mB.toFunctor.obj w₀'.1,
              Functor.congr_obj hA' w₀'.1, Functor.congr_obj hB' w₀'.1,
              data.filler.app w₀'.1, data.filler_vertical w₀'.1⟩ :
            TwoFibreProductOver (mF.toFunctor ⋙ D𝒴.projection)
              (data.rightFunctor ⋙ D𝒴.projection) D𝒴.projection mF.toFunctor
              data.rightFunctor))
        QH QG PF PF' hw₀) ∧
    Function.Exact
      (Deformation.infLegDiff D𝒴.projection mF.toFunctor data.rightFunctor hH' hG' hD𝒴
        (w₀ :=
          (⟨D𝒲.projection.obj w₀'.1, mA.toFunctor.obj w₀'.1, mB.toFunctor.obj w₀'.1,
              Functor.congr_obj hA' w₀'.1, Functor.congr_obj hB' w₀'.1,
              data.filler.app w₀'.1, data.filler_vertical w₀'.1⟩ :
            TwoFibreProductOver (mF.toFunctor ⋙ D𝒴.projection)
              (data.rightFunctor ⋙ D𝒴.projection) D𝒴.projection mF.toFunctor
              data.rightFunctor))
        QH QG PF PF' hw₀)
      (Deformation.infBoundaryLinearMapOfLift D𝒴.projection D𝒲.projection mF.toFunctor
        data.rightFunctor mA.toFunctor mB.toFunctor hA' hB' data.filler data.filler_vertical
        hlift' hD𝒲 hH' hG' hD𝒴 QH QG PF) ∧
    Function.Exact
      (Deformation.infBoundaryLinearMapOfLift D𝒴.projection D𝒲.projection mF.toFunctor
        data.rightFunctor mA.toFunctor mB.toFunctor hA' hB' data.filler data.filler_vertical
        hlift' hD𝒲 hH' hG' hD𝒴 QH QG PF)
      (LinearMap.prod
        (Deformation.tangentMapAt hD𝒲 hH'
          ({ toFunctor := mA.toFunctor, w := hA' } :
            BasedCategory.ofFunctor D𝒲.projection ⥤ᵇ
              BasedCategory.ofFunctor (mF.toFunctor ⋙ D𝒴.projection))
          (FGModuleCat.of k (ULift.{u} k)))
        (Deformation.tangentMapAt hD𝒲 hG'
          ({ toFunctor := mB.toFunctor, w := hB' } :
            BasedCategory.ofFunctor D𝒲.projection ⥤ᵇ
              BasedCategory.ofFunctor (data.rightFunctor ⋙ D𝒴.projection))
          (FGModuleCat.of k (ULift.{u} k)))) ∧
    Function.Exact
      (LinearMap.prod
        (Deformation.tangentMapAt hD𝒲 hH'
          ({ toFunctor := mA.toFunctor, w := hA' } :
            BasedCategory.ofFunctor D𝒲.projection ⥤ᵇ
              BasedCategory.ofFunctor (mF.toFunctor ⋙ D𝒴.projection))
          (FGModuleCat.of k (ULift.{u} k)))
        (Deformation.tangentMapAt hD𝒲 hG'
          ({ toFunctor := mB.toFunctor, w := hB' } :
            BasedCategory.ofFunctor D𝒲.projection ⥤ᵇ
              BasedCategory.ofFunctor (data.rightFunctor ⋙ D𝒴.projection))
          (FGModuleCat.of k (ULift.{u} k))))
      ((Deformation.tangentMapAt hH' hD𝒴
            ({ toFunctor := mF.toFunctor, w := rfl } :
              BasedCategory.ofFunctor (mF.toFunctor ⋙ D𝒴.projection) ⥤ᵇ
                BasedCategory.ofFunctor D𝒴.projection)
            (FGModuleCat.of k (ULift.{u} k))).comp
          (LinearMap.fst k
            ↥(Deformation.tangentModuleAt
              (BasedCategory.ofFunctor (mF.toFunctor ⋙ D𝒴.projection)) hH'
              (FGModuleCat.of k (ULift.{u} k)))
            ↥(Deformation.tangentModuleAt
              (BasedCategory.ofFunctor (data.rightFunctor ⋙ D𝒴.projection)) hG'
              (FGModuleCat.of k (ULift.{u} k)))) -
        (Deformation.tangentMapAt hG' hD𝒴
            ({ toFunctor := data.rightFunctor, w := rfl } :
              BasedCategory.ofFunctor (data.rightFunctor ⋙ D𝒴.projection) ⥤ᵇ
                BasedCategory.ofFunctor D𝒴.projection)
            (FGModuleCat.of k (ULift.{u} k))).comp
          (LinearMap.snd k
            ↥(Deformation.tangentModuleAt
              (BasedCategory.ofFunctor (mF.toFunctor ⋙ D𝒴.projection)) hH'
              (FGModuleCat.of k (ULift.{u} k)))
            ↥(Deformation.tangentModuleAt
              (BasedCategory.ofFunctor (data.rightFunctor ⋙ D𝒴.projection)) hG'
              (FGModuleCat.of k (ULift.{u} k)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.8, Tag 07WY](https://stacks.math.columbia.edu/tag/07WY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
