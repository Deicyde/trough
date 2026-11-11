---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.VersalSituation, AlgebraicGeometry.Stack.IsVersalRingAt, AlgebraicGeometry.Stack.isVersalRingAt_iff_of_affineOpenPresentation, AlgebraicGeometry.Stack.isFiniteDimensionalDeformationCategory_of_versalSituation, AlgebraicGeometry.Stack.versalRing_powerSeries_comparison, AlgebraicGeometry.Stack.exists_isVersalRingAt, AlgebraicGeometry.Stack.exists_isVersalRingAt_fieldExtension, AlgebraicGeometry.Stack.isVersalAt_iff_exists_isRelativelySmooth_restrict
statement: formalized
proof: formalized
---

# 107.2 Versal rings

Section 107.2 of the Stacks Project, [Tag 0DQT](https://stacks.math.columbia.edu/tag/0DQT). 11 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DQU, a situation

[Tag 0DQU](https://stacks.math.columbia.edu/tag/0DQU) in the Stacks Project.

**`AlgebraicGeometry.Stack.VersalSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalSituation.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalSituation.lean#L58).

> **Stacks 0DQU.** The versal situation: an algebraic stack locally of finite type over a
> locally Noetherian scheme.

```lean
structure VersalSituation
```

## Tag 0DQV, a definition

[Tag 0DQV](https://stacks.math.columbia.edu/tag/0DQV) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsVersalRingAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRing/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRing/Basic.lean#L69).

> A complete Noetherian local algebra is a versal ring at a field-valued
> point if it is the base of a versal formal object in the point's
> predeformation category.

```lean
public abbrev IsVersalRingAt
    (D : AlgebraicGeometry.Stack.VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S)
    (_hiΛ : IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (_hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k) : Prop
```

**`AlgebraicGeometry.Stack.isVersalRingAt_iff_of_affineOpenPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRing/ChartIndependence.lean, line 794](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRing/ChartIndependence.lean#L794). The attribute's comment: “independence of affine-open presentation”.

> The notion of a versal ring is independent of which affine open
> neighborhood presents its structure morphism to `S`.

```lean
public theorem isVersalRingAt_iff_of_affineOpenPresentation
    (D : AlgebraicGeometry.Stack.VersalSituation.{u, w})
    {Λ Λ' k : Type u} [CommRing Λ] [CommRing Λ'] [Field k]
    [Algebra Λ k] [Algebra Λ' k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : IsOpenImmersion iΛ)
    (iΛ' : Spec (.of Λ') ⟶ D.S) (hiΛ' : IsOpenImmersion iΛ')
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hx₀' : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite' : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ') ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (A' : Deformation.CompleteLocalAlgCat.{u, u, u} Λ' k)
    (e : A ≃+* A')
    (heS : Spec.map (CommRingCat.ofHom e.toRingHom) ≫
        Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ iΛ =
      Spec.map (CommRingCat.ofHom (algebraMap Λ' A')) ≫ iΛ')
    (hek : ∀ a : A,
      A'.residueEquiv (residue A' (e a)) = A.residueEquiv (residue A a)) :
    IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A ↔
      IsVersalRingAt D iΛ' hiΛ' x₀ hx₀' hfinite' A'
```

## Tag 0DQW, a lemma

[Tag 0DQW](https://stacks.math.columbia.edu/tag/0DQW) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFiniteDimensionalDeformationCategory_of_versalSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalSituationFiniteDimensional.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalSituationFiniteDimensional.lean#L44).

> In Situation 0DQU, let `x₀` be an object of `𝒳` over `Spec k`, for a field `k` of finite type
> over `S`, and let `Spec Λ ⊆ S` be an affine open through which `Spec k ⟶ S` factors with `Λ → k`
> finite. Then `𝓕_{𝒳,k,x₀}` is a deformation category whose tangent space and space of infinitesimal
> automorphisms are finite-dimensional over `k`.

```lean
theorem isFiniteDimensionalDeformationCategory_of_versalSituation
    (D : VersalSituation.{u, w}) {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k] (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    letI := (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).category
    Deformation.IsFiniteDimensionalDeformationCategory
      (Deformation.Artin.predeformationCategory iΛ
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection
```

## Tag 0DQX, a lemma

[Tag 0DQX](https://stacks.math.columbia.edu/tag/0DQX) in the Stacks Project.

**`AlgebraicGeometry.Stack.versalRing_powerSeries_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRing/ComparisonAndExistence.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRing/ComparisonAndExistence.lean#L419). The attribute's comment: “the comparison of any two versal rings at x₀: A ≅ A'[[t₁,…,t\_r]] or A' ≅ A[[t₁,…,t\_r]]”.

> Two versal rings at a field-valued point of an algebraic stack are isomorphic over the base
> after adjoining finitely many formal variables to one of them.

```lean
theorem versalRing_powerSeries_comparison
    (D : AlgebraicGeometry.Stack.VersalSituation.{u, w})
    {Λ Λ' k : Type u} [CommRing Λ] [CommRing Λ'] [Field k]
    [Algebra Λ k] [Algebra Λ' k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : IsOpenImmersion iΛ)
    (iΛ' : Spec (.of Λ') ⟶ D.S) (hiΛ' : IsOpenImmersion iΛ')
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hx₀' : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite' : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ') ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (A' : Deformation.CompleteLocalAlgCat.{u, u, u} Λ' k)
    (hA : AlgebraicGeometry.Stack.IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A)
    (hA' : AlgebraicGeometry.Stack.IsVersalRingAt D iΛ' hiΛ' x₀ hx₀' hfinite' A') :
    (∃ r : ℕ, ∃ e : A ≃+* MvPowerSeries (Fin r) A',
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
        Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ iΛ =
      Spec.map (CommRingCat.ofHom
        (algebraMap Λ' (MvPowerSeries (Fin r) A'))) ≫ iΛ') ∨
    (∃ r : ℕ, ∃ e : A' ≃+* MvPowerSeries (Fin r) A,
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
        Spec.map (CommRingCat.ofHom (algebraMap Λ' A')) ≫ iΛ' =
      Spec.map (CommRingCat.ofHom
        (algebraMap Λ (MvPowerSeries (Fin r) A))) ≫ iΛ)
```

**`AlgebraicGeometry.Stack.exists_isVersalRingAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingExistence.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingExistence.lean#L38). The attribute's comment: “existence of a versal ring to 𝒳 at x₀”.

> **Stacks 0DQX**, first assertion. In Situation 0DQU, let `x₀` be an object of `𝒳` over
> `Spec k` for a field `k` of finite type over `S`, and let `Spec Λ ⊆ S` be an affine open through
> which `Spec k ⟶ S` factors. Then a versal ring to `𝒳` at `x₀` exists, presented over `Λ`.

```lean
theorem exists_isVersalRingAt
    (D : VersalSituation.{u, w}) {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    ∃ A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k,
      IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A
```

## Tag 0DQY, a lemma

[Tag 0DQY](https://stacks.math.columbia.edu/tag/0DQY) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isVersalRingAt_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFieldExtension.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFieldExtension.lean#L189).

> **Stacks 0DQY.** In Situation 0DQU, let `x₀` be an object of `𝒳` over `Spec k` for a field
> `k` of finite type over `S`, presented over an affine open `Spec Λ ⊆ S`, let `l/k` be a finite
> extension of fields, and let `x_{l,0}` be the induced point: an object `xₗ` over
> `Spec l ⟶ Spec Λ ⟶ S` with a morphism `η : xₗ ⟶ x₀` over `Spec l ⟶ Spec k`. Given a versal ring
> `A` to `𝒳` at `x₀` there are a versal ring `A'` to `𝒳` at `x_{l,0}` and an `S`-algebra map
> `f : A → A'` which is local, induces the given extension `l/k` on residue fields, and is formally
> smooth for the `𝔪_{A'}`-adic topology.

```lean
theorem exists_isVersalRingAt_fieldExtension
    (D : VersalSituation.{u, w})
    {Λ k l : Type u} [CommRing Λ] [Field k] [Field l] [Algebra Λ k] [Algebra k l]
    [Algebra Λ l] [IsScalarTower Λ k l] [Module.Finite k l]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (xₗ : D.𝒳.val.val.obj)
    (hxₗ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj xₗ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ l)) ≫ iΛ))
    (η : xₗ ⟶ x₀)
    (hηbase : eqToHom (congrArg Over.left hxₗ).symm ≫
      ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).map η).left ≫
      eqToHom (congrArg Over.left hx₀) = Spec.map (CommRingCat.ofHom (algebraMap k l)))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A) :
    ∃ (A' : Deformation.CompleteLocalAlgCat.{u, u, u} Λ l) (f : A →ₐ[Λ] A'),
      IsVersalRingAt D iΛ hiΛ xₗ hxₗ
          (locallyOfFiniteType_and_quasiCompact_fieldExtension iΛ hfinite) A' ∧
        IsLocalHom f.toRingHom ∧
        (∀ a : A, A'.residueEquiv (residue A' (f a)) =
          algebraMap k l (A.residueEquiv (residue A a))) ∧
        RingHom.FormallySmoothNAdic.{u} f.toRingHom (maximalIdeal A')
```

## Tag 0DQZ, a lemma

[Tag 0DQZ](https://stacks.math.columbia.edu/tag/0DQZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isVersalAt_iff_exists_isRelativelySmooth_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalChartSmoothBaseChange.lean, line 885](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalChartSmoothBaseChange.lean#L885). The attribute's comment: “the equivalence of (1) and (4): x is versal at u₀ exactly when there is an open neighbourhood U' ⊆ U of u₀ such that x|\_\{U'} : U' → 𝒳 is smooth”.

> **Stacks 0DQZ, the equivalence of (1) and (4).** In the versal situation, let `x` be an object
> of `𝒳` over a scheme `U` locally of finite type over `S`, and let `u₀ ∈ U` be a finite type point.
> Then `x` is versal at `u₀` exactly when there is an open neighbourhood `U' ⊆ U` of `u₀` such that
> `x|_{U'} : U' → 𝒳` is smooth.
>
> The open subscheme `U'` is read as an object of the site by
> `AlgebraicGeometry.BigFppfOver.openSubObj`, and `x|_{U'}` is the composite of its inclusion
> `U' → U` with the 1-morphism `x : U → 𝒳` of the 2-Yoneda lemma; it is representable by algebraic
> spaces, and smooth is meant in the sense of Stacks 04XB.
>
> The implication (4) ⟹ (1) is
> `AlgebraicGeometry.Stack.isVersalAt_of_exists_isRelativelySmooth_restrict`
> (Stacks 07WK, case (3), at the residue point of `u₀` in `U'`, and versality is unchanged by
> restriction to an open subscheme); (1) ⟹ (4) is
> `AlgebraicGeometry.Stack.exists_isRelativelySmooth_restrict_of_isVersalAt` (Stacks 0CXM along a
> smooth surjective presentation of `𝒳`, Stacks 06EJ, and descent of smoothness along a smooth
> surjection).

```lean
theorem isVersalAt_iff_exists_isRelativelySmooth_restrict (D : VersalSituation.{u, w})
    (x : D.𝒳.val.val.obj)
    [LocallyOfFiniteType ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).hom]
    (u₀ : ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left)
    (hu₀ : AlgebraicGeometry.IsFiniteTypePoint u₀) :
    Deformation.Artin.IsVersalAt ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x)
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) u₀ x rfl ↔
      ∃ V : (D.𝒳.val.val.p.obj x).left.obj.Opens, u₀ ∈ V ∧
        IsRelativelySmooth D.B D.S D.hS
          (schemeFibredCategoryMap D.B D.S D.hS
              (BigFppfOver.openSubHom D.B D.S D.hS (D.𝒳.val.val.p.obj x) V) ≫
            objectMorphism D.B D.S D.hS D.𝒳.val (Functor.Fiber.mk (a := x) rfl))
```

**`AlgebraicGeometry.Stack.isVersalAt_iff_isVersal_completion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingChartPoint.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingChartPoint.lean#L171). The attribute's comment: “the equivalence of (1) and (3): x is versal at u₀ exactly when the formal object associated to the restriction of x to Spec 𝒪^∧\_\{U,u₀} is versal”.

> **Stacks 0DQZ, the equivalence of (1) and (3).** In the versal situation, let `x` be an
> object of `𝒳` over a scheme `U` locally of finite type over `S`, let `u₀` be a point of `U`
> whose image in `S` lies in the affine open `Spec Λ`, and let `ξ` be the formal object the
> approximation functor attaches to a Cartesian restriction of `x` over a presentation of
> `𝒪^∧_{U, u₀}`. Then `x` is versal at `u₀` exactly when `ξ` is versal.
>
> This is Artin's Axioms, **Stacks 0CXK**, read in the versal situation of **Stacks 0DQU**, with
> the deformation base on the ring of an affine open of `S` rather than on a local ring of `S`.

```lean
theorem isVersalAt_iff_isVersal_completion
    (t : Spec (.of Λ)) (ht : iΛ t = Deformation.Artin.basePoint U u₀)
    [Algebra Λ (U.left.residueField u₀)]
    (hcompat : Spec.map (CommRingCat.ofHom (algebraMap Λ (U.left.residueField u₀))) ≫ iΛ =
      U.left.fromSpecResidueField u₀ ≫ U.hom) :
    Deformation.Artin.IsVersalAt U (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) u₀ x hx ↔
      Deformation.Artin.FormalObject.IsVersal D.B D.S D.hS D.𝒳.val.val.p D.𝒳.val.property
        ξ Λ iΛ hΛ
```

**`AlgebraicGeometry.Stack.isVersalRingAt_completeLocalBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingChartPoint.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingChartPoint.lean#L237). The attribute's comment: “the final statement: the completion 𝒪^∧\_\{U,u₀} is a versal ring to 𝒳 at the point x₀ induced by u₀”.

> **Stacks 0DQZ, the final statement.** In the versal situation, if `x` is versal at the
> finite type point `u₀`, then the completion `𝒪^∧_{U, u₀}` — presented by the complete local base
> of the formal object `ξ` attached to the restriction of `x` over it — is a versal ring to `𝒳` at
> the closed fibre `x₀` of `ξ`.
>
> The first conjunct identifies the point: the closed fibre `ξ.level 0`, over which the versal
> ring is exhibited, is the restriction of `x` along the residue point of `u₀`, hence the point
> `x₀` of the lemma's preamble. The second is the conclusion, and its proof is the one of the
> source: the equivalence of (1) and (3) turns versality of `x` at `u₀` into versality of `ξ`,
> and versality of a formal object is by definition versality of the formal object of the
> predeformation category of its closed fibre that it determines, which is exactly what
> **Stacks 0DQV** asks of a versal ring.

```lean
theorem isVersalRingAt_completeLocalBase
    (t : Spec (.of Λ)) (ht : iΛ t = Deformation.Artin.basePoint U u₀)
    [Algebra Λ (U.left.residueField u₀)]
    (hcompat : Spec.map (CommRingCat.ofHom (algebraMap Λ (U.left.residueField u₀))) ≫ iΛ =
      U.left.fromSpecResidueField u₀ ≫ U.hom)
    (hversal : Deformation.Artin.IsVersalAt U
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) u₀ x hx) :
    Deformation.Artin.schemeMap (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion)
          (ξ.basePoint Λ iΛ hΛ) hx
          (Deformation.Artin.approximationLevelToOriginal D.B D.S D.hS D.𝒳.val.val.p
            D.𝒳.val.property xR ξ hξ r 0) =
        Spec.map (CommRingCat.ofHom (residue ξ.base.R)) ≫ g ∧
      IsVersalRingAt D iΛ hiΛ (ξ.level 0) (ξ.basePoint Λ iΛ hΛ)
        (locallyOfFiniteType_and_quasiCompact_residueField_formalBase D ξ Λ iΛ hΛ)
        (ξ.completeLocalBase Λ)
```

**`AlgebraicGeometry.Stack.isVersalAt_iff_isSmooth_hatX`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingChartPoint.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingChartPoint.lean#L303). The attribute's comment: “the equivalence of (1) and (2): x is versal at u₀ exactly when x̂ : 𝓕\_\{U,k,u₀} ⟶ 𝓕\_\{𝒳,k,x₀} is smooth”.

> **Stacks 0DQZ, the equivalence of (1) and (2).** In the versal situation, let `x` be an
> object of `𝒳` over a scheme `U`, let `u₀ ∈ U` with residue field `k = κ(u₀)`, and let
> `Spec Λ ⊆ S` be an affine open through which `Spec k ⟶ S` factors. Then `x` is versal at `u₀`
> exactly when the map of predeformation categories over `𝒞_Λ`
> `x̂ : 𝓕_{U, k, u₀} ⟶ 𝓕_{𝒳, k, x₀}` induced by the 2-Yoneda morphism `x : (Sch/U)_{fppf} ⟶ 𝒳`
> (for any choice `c` of pullbacks) at the residue point of `u₀` is smooth.
>
> The source records this as "the definition of `x` being versal at `u₀`"; in this library
> `Deformation.Artin.IsVersalAt` is the lifting property spelled out over the local ring of `S`,
> so the equivalence is `Deformation.Artin.isVersalAt_iff_isSmooth_mapPredeformationCategory`.
> Neither local finite type of `U` nor the finite type of `u₀` is needed.

```lean
theorem isVersalAt_iff_isSmooth_hatX (t : Spec (.of Λ))
    (ht : iΛ t = Deformation.Artin.basePoint
      ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x) u₀) :
    Deformation.Artin.IsVersalAt ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x)
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) u₀ x rfl ↔
      Deformation.IsSmooth
        (Deformation.Artin.mapPredeformationCategory iΛ
          (Over.forget (D.𝒳.val.val.p.obj x) ⋙ Over.post D.B.inclusion)
          (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion)
          (c.sliceFunctor (⟨x, rfl⟩ : D.𝒳.val.val.p.Fiber (D.𝒳.val.val.p.obj x)))
          (Deformation.Artin.sliceFunctor_comp_post D.B D.S D.hS D.𝒳.val.val.p c x)
          (chartResiduePoint D x u₀) (chartResiduePoint_base D x u₀ iΛ hcompat)).toBasedFunctor
```

## Tag 0DZS, a lemma

[Tag 0DZS](https://stacks.math.columbia.edu/tag/0DZS) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsSmoothLocus.property_iff_isFormallySmoothAtClosedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingSmoothLocus.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingSmoothLocus.lean#L352). The attribute's comment: “the equivalence of (1) and (2): x₀ is in the smooth locus of 𝒳 → S iff 𝒪\_\{S,s} → A is formally smooth in the 𝔪\_A-adic topology”.

> **Stacks 0DZS, the equivalence of (1) and (2).** In Situation 0DQU — `𝒳` an algebraic stack
> locally of finite type over a locally Noetherian scheme `S` — let `x₀ : Spec k ⟶ 𝒳` be a point with
> `Spec k ⟶ S` of finite type, presented over an affine open `Spec Λ ⊆ S`, with image `s`, and let
> `A` be a versal ring to `𝒳` at `x₀`. Then `x₀` lies in the smooth locus `W` of `𝒳 ⟶ S`
> (Stacks 0DZR) if and only if `𝒪_{S, s} ⟶ A` is formally smooth for the `𝔪_A`-adic topology.
>
> The proof is the source's: condition (2) does not depend on the versal ring (Stacks 0DQX) and is
> unchanged by finite extensions of the residue field (Stacks 0DQY), so it may be tested at a point
> of a smooth chart `U ⟶ 𝒳`, where the versal ring is `𝒪^∧_{U, u₀}` (Stacks 0DQZ); there
> membership in the smooth locus of `𝒳 ⟶ S` is membership of `u₀` in the smooth locus of `U ⟶ S`
> (Stacks 0DZR), which is formal smoothness of `𝒪_{S, s} ⟶ 𝒪^∧_{U, u₀}` (Stacks 07VH).

```lean
theorem IsSmoothLocus.property_iff_isFormallySmoothAtClosedPoint
    {W : OpenSubstack D.𝒳}
    (hW : IsSmoothLocus D.B D.S D.hS (structureMorphism D.B D.S D.hS D.𝒳) W)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A) :
    W.property x₀ ↔
      IsFormallySmoothAtClosedPoint (Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ iΛ)
```

**`AlgebraicGeometry.Stack.isFormallySmoothAtClosedPoint_iff_isSmooth_baseProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingSmoothLocus.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingSmoothLocus.lean#L423). The attribute's comment: “the equivalence of (2) and (3): 𝒪\_\{S,s} → A is formally smooth in the 𝔪\_A-adic topology iff the predeformation category of x₀ is unobstructed”. References: SGA 7 VI (1.14), “special case”.

> **Stacks 0DZS, the equivalence of (2) and (3).** In Situation 0DQU let `x₀ : Spec k ⟶ 𝒳` be a
> point with `Spec k ⟶ S` of finite type, presented over an affine open `Spec Λ ⊆ S` with `Λ → k`
> finite (the presentation of Artin's Axioms, Section 07T2, on which the predeformation category
> `𝓕_{𝒳, k, x₀}` is built), and let `A` be a versal ring to `𝒳` at `x₀`. Then `𝒪_{S, s} ⟶ A` is
> formally smooth for the `𝔪_A`-adic topology if and only if `𝓕_{𝒳, k, x₀}` is unobstructed, that
> is its structure functor to `𝒞_Λ` is smooth. This is Formal Deformation Theory, Lemma 0DZK,
> together with the observation that `𝒪_{S, s}` is a localization of `Λ`.

```lean
theorem isFormallySmoothAtClosedPoint_iff_isSmooth_baseProjection
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A) :
    IsFormallySmoothAtClosedPoint (Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ iΛ) ↔
      let C := Deformation.Artin.predeformationCategory iΛ
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀
      letI : Category C.carrier := C.category
      Deformation.IsSmooth (Deformation.baseProjection C.projection)
```

**`AlgebraicGeometry.Stack.tfae_smoothLocus_formallySmooth_unobstructed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingSmoothLocus.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingSmoothLocus.lean#L471).

> **Stacks 0DZS.** In Situation 0DQU let `x₀ : Spec k ⟶ 𝒳` be a point with `Spec k ⟶ S` of finite
> type, presented over an affine open `Spec Λ ⊆ S` with `Λ → k` finite, with image `s ∈ S`, and let
> `A` be a versal ring to `𝒳` at `x₀`. The following are equivalent:
>
> 1. `x₀` is in the smooth locus of `𝒳 ⟶ S` (Stacks 0DZR);
> 2. `𝒪_{S, s} ⟶ A` is formally smooth in the `𝔪_A`-adic topology;
> 3. `𝓕_{𝒳, k, x₀}` is unobstructed.

```lean
theorem tfae_smoothLocus_formallySmooth_unobstructed
    {W : OpenSubstack D.𝒳}
    (hW : IsSmoothLocus D.B D.S D.hS (structureMorphism D.B D.S D.hS D.𝒳) W)
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A) :
    List.TFAE [W.property x₀,
      IsFormallySmoothAtClosedPoint (Spec.map (CommRingCat.ofHom (algebraMap Λ A)) ≫ iΛ),
      let C := Deformation.Artin.predeformationCategory iΛ
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀
      letI : Category C.carrier := C.category
      Deformation.IsSmooth (Deformation.baseProjection C.projection)]
```

## Tag 0DR0, a lemma

[Tag 0DR0](https://stacks.math.columbia.edu/tag/0DR0) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_smoothObject_completedLocalRing_equiv_versalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingArtinApproximation.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingArtinApproximation.lean#L814).

> **Stacks 0DR0.** In the versal situation, let `x₀` be a point of `𝒳` over
> `Spec k ⟶ Spec Λ ⟶ S`, for an affine open `Spec Λ ⊆ S` and a field `k` with `Spec k ⟶ S` of
> finite type and image `s`, and let `A` be a versal ring to `𝒳` at `x₀` (**Stacks 0DQV**). If
> `𝒪_{S,s}` is a G-ring, there are a smooth object `x` of `𝒳` (a smooth morphism `U ⟶ 𝒳` from a
> scheme `U`, here moreover locally of finite type over `S`) and a point `u₀ ∈ U` with residue field
> `k`, through `e : k ≅ κ(u₀)`, such that
> 1. `Spec k ⟶ U ⟶ 𝒳` is `x₀`: there is an arrow `x₀ ⟶ x` of `𝒳` lying over
>    `Spec k ≅ Spec κ(u₀) ⟶ U` (a 2-isomorphism of 1-morphisms out of `Spec k`);
> 2. there is an isomorphism `𝒪^∧_{U, u₀} ≅ A`.
>
> The proof is the source's: the versal formal object is effective (**Stacks 07X8**), so
> `AlgebraicGeometry.Stack.exists_smoothObject_completedLocalRing_realization` (Artin approximation,
> **Stacks 07XH**, with **Stacks 0DQJ**, **Stacks 0CMY** and **Stacks 0DQZ**) applies to a
> realization of it.

```lean
theorem exists_smoothObject_completedLocalRing_equiv_versalRing (D : VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (A : Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)
    (hA : IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite A)
    (s : D.S) (hs : (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) (closedPoint k) = s)
    (hG : IsGRing (D.S.presheaf.stalk s)) :
    ∃ (x : D.𝒳.val.val.obj) (u₀ : ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left)
      (e : k ≃+* ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.residueField u₀)
      (a : x₀ ⟶ x)
      (_ : ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.completedLocalRing u₀ ≃+* A),
      LocallyOfFiniteType ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).hom ∧
      smoothObject.{u, w} D.B D.S D.hS D.𝒳 x ∧
      Deformation.Artin.schemeMap (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) hx₀ rfl a =
        Spec.map (CommRingCat.ofHom e.symm.toRingHom) ≫
          ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.fromSpecResidueField u₀
```

## Tag 0DR1, a remark

[Tag 0DR1](https://stacks.math.columbia.edu/tag/0DR1) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_smoothObject_completedLocalRing_realization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingArtinApproximation.lean, line 717](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingArtinApproximation.lean#L717). The attribute's comment: “part (4): in Lemma 0DR0 the isomorphism 𝒪^∧\_\{U,u₀} ≅ A may be chosen so that Spec(A) → 𝒳 corresponds to the canonical map Spec(𝒪^∧\_\{U,u₀}) → U → 𝒳 of part (3)”.

> **Stacks 0DR1, part (4): Artin approximation compatible with the morphism `Spec A ⟶ 𝒳`.**
> In the versal situation, let `x₀` be a point of `𝒳` over `Spec k ⟶ Spec Λ ⟶ S`, for an affine open
> `Spec Λ ⊆ S` and a field `k` of finite type over `S`, with image `s ∈ S` such that `𝒪_{S,s}` is a
> G-ring; let `ξ` be a versal formal object of the predeformation category of `x₀`, with base the
> versal ring `A`, and let `y` be an object of `𝒳` over `Spec A ⟶ S` realizing `ξ` (the morphism
> `Spec A ⟶ 𝒳` of the remark). Then the data of **Stacks 0DR0** may be chosen compatibly with `y`:
> there are a smooth object `x` of `𝒳` over a scheme `U` locally of finite type over `S`, a point
> `u₀ ∈ U` with an identification `e : k ≅ κ(u₀)`, an arrow `x₀ ⟶ x` of `𝒳` over
> `Spec k ≅ Spec κ(u₀) ⟶ U` (so `Spec k ⟶ U ⟶ 𝒳` is `x₀`), an isomorphism `eA : 𝒪^∧_{U, u₀} ≅ A`,
> and an arrow `y ⟶ x` of `𝒳` over `Spec A ≅ Spec 𝒪^∧_{U, u₀} ⟶ U`: the morphism `Spec A ⟶ 𝒳` is,
> through `eA`, the canonical `Spec 𝒪^∧_{U, u₀} ⟶ U ⟶ 𝒳` of part (3). As the remark says, the
> triangles commute up to a 2-arrow, which is what an arrow of `𝒳` over a morphism of schemes is.
>
> This is Artin approximation, **Stacks 07XH**, at the formal object over the site of `ξ`, which is
> effective because it is realized and versal over `𝒪_{S,s}` by
> `Deformation.Artin.isVersal_stalk_ofPredeformation_of_realization`; the structure morphism of `𝒳`
> is limit preserving by **Stacks 0DQJ** and **Stacks 0CMY**. The chart Artin approximation produces
> is versal at `u₀`, hence smooth after shrinking by **Stacks 0DQZ**, (1) ⟹ (4). The arrow `y ⟶ x`
> is the preimage, under the fully faithful approximation functor (**Stacks 07X8**), of the
> isomorphism of formal objects that Artin approximation produces, followed by the restriction arrow
> of the chart to the completion.

```lean
theorem exists_smoothObject_completedLocalRing_realization (D : VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ)
    (s : D.S) (hs : (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) (closedPoint k) = s)
    (hG : IsGRing (D.S.presheaf.stalk s))
    {hA : D.B.Contains (Spec (.of ξ.base))} {y : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hA}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hA y hy) :
    ∃ (x : D.𝒳.val.val.obj) (u₀ : ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left)
      (e : k ≃+* ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.residueField u₀)
      (a : x₀ ⟶ x)
      (eA : ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.completedLocalRing u₀ ≃+*
        ξ.base),
      LocallyOfFiniteType ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).hom ∧
      smoothObject.{u, w} D.B D.S D.hS D.𝒳 x ∧
      Deformation.Artin.schemeMap (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) hx₀ rfl a =
        Spec.map (CommRingCat.ofHom e.symm.toRingHom) ≫
          ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.fromSpecResidueField u₀ ∧
      ∃ m : y ⟶ x, Deformation.Artin.schemeMap (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion)
          (congrArg (Over.post D.B.inclusion).obj hy) rfl m =
        Spec.map (CommRingCat.ofHom eA.toRingHom) ≫
          ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x).left.fromSpecCompletedLocalRing u₀
```

**`AlgebraicGeometry.Stack.exists_realization_of_predeformationFormalObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingArtinApproximation.lean, line 777](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingArtinApproximation.lean#L777). The attribute's comment: “preamble: the versal formal object over A comes from a morphism Spec(A) → 𝒳 over S (Artin's Axioms, Lemma 07X8)”.

> **Stacks 0DR1, the preamble: the versal formal object comes from a morphism `Spec A ⟶ 𝒳`.**
> In the versal situation, let `x₀` be a point of `𝒳` over `Spec k ⟶ Spec Λ ⟶ S`, for an affine open
> `Spec Λ ⊆ S` and a field `k` of finite type over `S`, and let `ξ` be a formal object of the
> predeformation category of `x₀` with base `A` — in the remark, the versal formal object over a
> versal ring `A`, though versality is not needed. Then `ξ` comes from a morphism `Spec A ⟶ 𝒳` over
> `S`: there is an object `y` of `𝒳` over `Spec A ⟶ Spec Λ ⟶ S` whose restrictions to the
> infinitesimal thickenings of the closed point are the levels of `ξ`, compatibly with the
> transitions (a `Deformation.Artin.FormalObject.Realization`); `y` names the 1-morphism
> `Spec A ⟶ 𝒳` under the 2-Yoneda lemma.
>
> This is effectivity of formal objects of an algebraic stack, the essential surjectivity half of
> **Stacks 07X8** (`Deformation.Artin.FormalObject.isEffective_of_isAlgebraicStack`), read over the
> base of `ξ` itself by `Deformation.Artin.FormalObject.exists_realization_of_isEffective`.

```lean
theorem exists_realization_of_predeformationFormalObject (D : VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection) :
    ∃ (y : D.𝒳.val.val.obj)
      (hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
        (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base)
        (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
          hfinite ξ).contains_spec_base),
      Nonempty ((Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p
        x₀ hx₀ hfinite ξ).Realization
          (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
            hfinite ξ).contains_spec_base y hy)
```

**`AlgebraicGeometry.Stack.exists_isVersalRingAt_fieldExtension_realization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFieldExtensionRealization.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFieldExtensionRealization.lean#L573). The attribute's comment: “part (2): in Lemma 0DQY the homomorphism A → A' may be chosen compatible with the morphisms Spec A → 𝒳, Spec A' → 𝒳”.

> **Stacks 0DR1, part (2).** In the versal situation of Stacks 0DQU, let `x₀` be a point of `𝒳`
> over `Spec k` for a field `k` of finite type over `S`, presented over an affine open `Spec Λ ⊆ S`,
> let `l/k` be a finite extension of fields and `x_{l,0}` the induced point (an object `xₗ` over
> `Spec l` with a morphism `η : xₗ ⟶ x₀` over `Spec l ⟶ Spec k`). Let `A` be a versal ring to `𝒳`
> at `x₀`, with versal formal object `ξ`, coming from a morphism `Spec A ⟶ 𝒳` over `S`: an object
> `y` of `𝒳` over `Spec A` realizing `ξ`. Then the homomorphism of **Stacks 0DQY** may be chosen
> compatible with the morphisms `Spec A ⟶ 𝒳` and `Spec A' ⟶ 𝒳`: there are a versal ring `A'` to `𝒳`
> at `x_{l,0}`, with versal formal object `ξₗ`, and an `S`-algebra map `f : A → A'` which is local,
> induces `l/k` on residue fields and is formally smooth for the `𝔪_{A'}`-adic topology, such that
>
> * when `Spec A'` belongs to the site, `ξₗ` comes from a morphism `Spec A' ⟶ 𝒳` (an object over
>   `Spec A'` realizing `ξₗ`), and
> * every object `y'` over `Spec A'` realizing `ξₗ` has a morphism `y' ⟶ y` of `𝒳` lying over
>   `Spec f : Spec A' ⟶ Spec A`.
>
> The morphism `y' ⟶ y` is the 2-arrow making the square `Spec A' ⟶ Spec A ⟶ 𝒳` 2-commute, which is
> how the source's "compatible" is to be read (the remark notes that the diagrams commute only up to
> a noncanonical 2-arrow). As in the source, the proof is that the maps of Stacks 0DQF and 07WX are
> compatible with the versal formal objects: the formal object of `𝓕_{l/k}` produced by Stacks 0DQF
> is the pushforward of `ξ` along `f`
> (`Deformation.exists_versal_formalObject_changeOfFields_pushforward`), and its image under the
> restriction functor of Stacks 07WX maps to `ξ` over the site over `Spec f`; fullness of the
> approximation functor (Stacks 07X8, `Deformation.Artin.full_approximationFunctor_algebraicStacks`)
> turns that morphism of formal objects into a morphism of the realizing objects.

```lean
theorem exists_isVersalRingAt_fieldExtension_realization
    {Λ k l : Type u} [CommRing Λ] [Field k] [Field l] [Algebra Λ k] [Algebra k l]
    [Algebra Λ l] [IsScalarTower Λ k l] [Module.Finite k l]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (xₗ : D.𝒳.val.val.obj)
    (hxₗ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj xₗ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ l)) ≫ iΛ))
    (η : xₗ ⟶ x₀)
    (hηbase : eqToHom (congrArg Over.left hxₗ).symm ≫
      ((D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).map η).left ≫
      eqToHom (congrArg Over.left hx₀) = Spec.map (CommRingCat.ofHom (algebraMap k l)))
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ)
    {hA : D.B.Contains (Spec (.of ξ.base))} {y : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hA}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hA y hy) :
    ∃ (ξₗ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) xₗ hxₗ).projection)
      (f : ξ.base →ₐ[Λ] ξₗ.base),
      Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
        D.B D.hS iΛ D.𝒳.val.val.p xₗ hxₗ D.𝒳.val.property).cofibered ξₗ ∧
      IsLocalHom f.toRingHom ∧
      (∀ a : ξ.base, ξₗ.base.residueEquiv (residue ξₗ.base (f a)) =
        algebraMap k l (ξ.base.residueEquiv (residue ξ.base a))) ∧
      RingHom.FormallySmoothNAdic.{u} f.toRingHom (maximalIdeal ξₗ.base) ∧
      (∀ hA' : D.B.Contains (Spec (.of ξₗ.base)), ∃ (y' : D.𝒳.val.val.obj)
        (hy' : D.𝒳.val.val.p.obj y' = Deformation.Artin.baseOver D.B D.S D.hS
          (Deformation.Artin.completeLocalAlgFormalBase iΛ
            (locallyOfFiniteType_and_quasiCompact_fieldExtension iΛ hfinite) ξₗ.base) hA'),
        Nonempty ((Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ
          D.𝒳.val.val.p xₗ hxₗ (locallyOfFiniteType_and_quasiCompact_fieldExtension iΛ hfinite)
            ξₗ).Realization hA' y' hy')) ∧
      ∀ {hA' : D.B.Contains (Spec (.of ξₗ.base))} {y' : D.𝒳.val.val.obj}
        {hy' : D.𝒳.val.val.p.obj y' = Deformation.Artin.baseOver D.B D.S D.hS
          (Deformation.Artin.completeLocalAlgFormalBase iΛ
            (locallyOfFiniteType_and_quasiCompact_fieldExtension iΛ hfinite) ξₗ.base) hA'},
        (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p xₗ hxₗ
          (locallyOfFiniteType_and_quasiCompact_fieldExtension iΛ hfinite) ξₗ).Realization
            hA' y' hy' →
        ∃ m : y' ⟶ y, (BigFppfOver.toScheme D.B D.S D.hS).map
            (eqToHom hy'.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy) =
          Spec.map (CommRingCat.ofHom f.toRingHom)
```

**`AlgebraicGeometry.Stack.isEffective_and_objectMorphism_completion_factors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFlatMorphism.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFlatMorphism.lean#L197). The attribute's comment: “the morphism Spec(A) ⟶ 𝒳 of the remark at the versal ring A = 𝒪^∧\_\{U,u₀} of Stacks 0DQZ, and clause (3): that morphism is the composition of the canonical map Spec(𝒪^∧\_\{U,u₀}) ⟶ U with the given map U ⟶ 𝒳”.

> **Stacks 0DR1 at the versal ring of Stacks 0DQZ, and its clause (3).** In the versal
> situation, let `x` be an object of `𝒳` over a scheme `U` locally of finite type over `S`, let
> `u₀` be a point of `U`, and let `xR` be a complete local object restricting `x` over the
> canonical morphism `Spec(𝒪^∧_{U, u₀}) ⟶ U`. Then the formal object `ξ` the approximation functor
> of **Stacks 07X6** attaches to `xR` is effective, so the versal formal object of **Stacks 0DQZ**
> comes from a morphism `Spec(𝒪^∧_{U, u₀}) ⟶ 𝒳` — the 1-morphism `xR` names under the 2-Yoneda
> lemma — and that morphism is the composition of the canonical map `Spec(𝒪^∧_{U, u₀}) ⟶ U` with
> the given map `U ⟶ 𝒳`.
>
> The three conclusions are the three halves of the statement: effectivity, which is the preamble
> of the remark; the identification of the morphism of the site that `r` lies over with the
> canonical morphism `AlgebraicGeometry.Scheme.fromSpecCompletedLocalRing` of the completion, read
> through the presentation `e`; and the 2-isomorphism of 1-morphisms, which is the 2-Yoneda
> functoriality `AlgebraicGeometry.Stack.objectMorphismFactorIso` of **Stacks 004B** at `r`. As the
> remark notes, the diagram only 2-commutes, after a choice of 2-arrow, which is why the third
> conclusion is a `Nonempty` of isomorphisms rather than an equality.

```lean
theorem isEffective_and_objectMorphism_completion_factors
    (ξ : Deformation.Artin.FormalObject D.B D.S D.hS D.𝒳.val.val.p)
    (hξ : ξ = (Deformation.Artin.approximationFunctor D.B D.S D.hS D.𝒳.val.val.p
      D.𝒳.val.property).obj xR) :
    Deformation.Artin.FormalObject.IsEffective D.B D.S D.hS D.𝒳.val.val.p
        D.𝒳.val.property ξ ∧
      ((eqToHom (Deformation.Artin.chosenBase_eq D.B D.S D.hS
            D.𝒳.val.val.p xR.obj).symm ≫ D.𝒳.val.val.p.map r).left.hom ≫
          eqToHom (congrArg Over.left hx)) =
        Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          U.left.fromSpecCompletedLocalRing u₀ ∧
      Nonempty (objectMorphism D.B D.S D.hS D.𝒳.val
          (Functor.Fiber.mk (a := xR.obj.1) rfl) ≅
        schemeFibredCategoryMap D.B D.S D.hS (D.𝒳.val.val.p.map r) ≫
          objectMorphism D.B D.S D.hS D.𝒳.val (Functor.Fiber.mk (a := x) rfl))
```

**`AlgebraicGeometry.Stack.exists_powerSeries_comparison_realization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingMorphism.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingMorphism.lean#L419). The attribute's comment: “part (1): in Lemma 0DQX the isomorphism A ≅ A'[[t₁,…,t\_r]] or A' ≅ A[[t₁,…,t\_r]] may be chosen compatible with the morphisms Spec A → 𝒳, Spec A' → 𝒳”.

> **Stacks 0DR1, part (1).** In the versal situation, let `x₀` be a point of `𝒳` over `Spec k`
> for a field `k` of finite type over `S`, and let `A`, `A'` be versal rings to `𝒳` at `x₀`
> (presented over affine opens `Spec Λ`, `Spec Λ'` of `S`), with versal formal objects `ξ`, `ξ'`
> coming from morphisms `Spec A ⟶ 𝒳` and `Spec A' ⟶ 𝒳` over `S`: objects `y`, `y'` of `𝒳` over
> `Spec A`, `Spec A'` realizing `ξ`, `ξ'`. Then the isomorphism of **Stacks 0DQX** may be chosen
> compatible with these morphisms: either there are `r` and an isomorphism
> `e : A ≅ A'[[t₁, …, t_r]]` over `S` together with a morphism `y ⟶ y'` of `𝒳` lying over
> `Spec A ≅ Spec A'[[t₁, …, t_r]] ⟶ Spec A'`, or the same with `A` and `A'` exchanged. The
> morphism `y ⟶ y'` is the 2-arrow making the triangle `Spec A ⟶ Spec A' ⟶ 𝒳` 2-commute, which
> is how the source's "compatible" is to be read (the remark notes that the diagrams commute only
> up to a noncanonical 2-arrow).
>
> Fullness of the approximation functor, the input from **Stacks 07X8**, is
> `Deformation.Artin.full_approximationFunctor_algebraicStacks`.

```lean
theorem exists_powerSeries_comparison_realization
    {Λ Λ' k : Type u} [CommRing Λ] [CommRing Λ'] [Field k]
    [Algebra Λ k] [Algebra Λ' k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : IsOpenImmersion iΛ)
    (iΛ' : Spec (.of Λ') ⟶ D.S) (hiΛ' : IsOpenImmersion iΛ')
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hx₀' : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite' : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ') ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ' k)) ≫ iΛ'))
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ)
    (ξ' : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ'
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀').projection)
    (hξ' : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ' D.𝒳.val.val.p x₀ hx₀' D.𝒳.val.property).cofibered ξ')
    {hA : D.B.Contains (Spec (.of ξ.base))} {hA' : D.B.Contains (Spec (.of ξ'.base))}
    {y y' : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hA}
    {hy' : D.𝒳.val.val.p.obj y' = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ' hfinite' ξ'.base) hA'}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hA y hy)
    (Ry' : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ' D.𝒳.val.val.p x₀
      hx₀' hfinite' ξ').Realization hA' y' hy') :
    (∃ r : ℕ, ∃ e : (ξ.base : Type u) ≃+* MvPowerSeries (Fin r) ξ'.base,
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          Spec.map (CommRingCat.ofHom (algebraMap Λ ξ.base)) ≫ iΛ =
        Spec.map (CommRingCat.ofHom (algebraMap Λ' (MvPowerSeries (Fin r) ξ'.base))) ≫ iΛ' ∧
      ∃ m : y ⟶ y', (BigFppfOver.toScheme D.B D.S D.hS).map
          (eqToHom hy.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy') =
        Spec.map (CommRingCat.ofHom (e.symm.toRingHom.comp MvPowerSeries.C))) ∨
    (∃ r : ℕ, ∃ e : (ξ'.base : Type u) ≃+* MvPowerSeries (Fin r) ξ.base,
      Spec.map (CommRingCat.ofHom e.toRingHom) ≫
          Spec.map (CommRingCat.ofHom (algebraMap Λ' ξ'.base)) ≫ iΛ' =
        Spec.map (CommRingCat.ofHom (algebraMap Λ (MvPowerSeries (Fin r) ξ.base))) ≫ iΛ ∧
      ∃ m : y' ⟶ y, (BigFppfOver.toScheme D.B D.S D.hS).map
          (eqToHom hy'.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy) =
        Spec.map (CommRingCat.ofHom (e.symm.toRingHom.comp MvPowerSeries.C)))
```

**`AlgebraicGeometry.Stack.formallyHomotopic_of_realization_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingMorphismHomotopy.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingMorphismHomotopy.lean#L541). The attribute's comment: “closing claim: the map in (1) is well defined up to formal homotopy (0DQD)”.

> **Stacks 0DR1, closing claim: the map of part (1) is well defined up to formal homotopy.** In
> the versal situation of Stacks 0DQU, let `x₀` be a point of `𝒳` over `Spec k` for a field `k` of
> finite type over `S`, presented over an affine open `Spec Λ ⊆ S` with `Λ → k` finite, so that
> `𝓕_{𝒳,k,x₀}` lives over `𝒞_Λ` (Stacks 07T2). Let `A'` be a versal ring to `𝒳` at `x₀` with versal
> formal object `ξ'`, let `A` be the base of a formal object `ξ` of `𝓕_{𝒳,k,x₀}` (for instance a
> second versal ring), and let `y'`, `y` be objects of `𝒳` over `Spec A'`, `Spec A` realizing `ξ'`,
> `ξ`, i.e. morphisms `Spec A' ⟶ 𝒳`, `Spec A ⟶ 𝒳` from which the formal objects come (Stacks 07X8).
> Then any two maps `f, g : A' ⟶ A` of `\widehat{𝒞}_Λ` compatible with these morphisms — each
> admitting a `2`-arrow `y ⟶ y'` lying over its spectrum and restricting to the identity of `x₀` —
> are formally homotopic (Stacks 0DQA). Applied with `A`, `A'` in either order this covers both the
> maps `A' → A` and `A → A'` of part (1) (see
> `AlgebraicGeometry.Stack.exists_powerSeries_comparison_realization_pointed`), and it is
> Stacks 0DQD, which applies since `𝓕_{𝒳,k,x₀}` is a deformation category with finite-dimensional
> tangent space and infinitesimal automorphisms (Stacks 0DQW).

```lean
theorem formallyHomotopic_of_realization_compatible
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (ξ ξ' : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ' : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ')
    {hA : D.B.Contains (Spec (.of ξ.base))} {hA' : D.B.Contains (Spec (.of ξ'.base))}
    {y y' : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hA}
    {hy' : D.𝒳.val.val.p.obj y' = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ'.base) hA'}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hA y hy)
    (Ry' : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ').Realization hA' y' hy')
    (f g : ξ'.base ⟶ ξ.base)
    (hf : ∃ m : y ⟶ y', (BigFppfOver.toScheme D.B D.S D.hS).map
        (eqToHom hy.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy') =
          Spec.map (CommRingCat.ofHom f.hom.toRingHom) ∧
        Deformation.Artin.realizationPointArrow Ry ≫ m =
          Deformation.Artin.realizationPointArrow Ry')
    (hg : ∃ m : y ⟶ y', (BigFppfOver.toScheme D.B D.S D.hS).map
        (eqToHom hy.symm ≫ D.𝒳.val.val.p.map m ≫ eqToHom hy') =
          Spec.map (CommRingCat.ofHom g.hom.toRingHom) ∧
        Deformation.Artin.realizationPointArrow Ry ≫ m =
          Deformation.Artin.realizationPointArrow Ry') :
    Deformation.CompleteLocalAlgCat.FormallyHomotopic f g
```

## Tag 0DR2, a lemma

[Tag 0DR2](https://stacks.math.columbia.edu/tag/0DR2) in the Stacks Project.

**`AlgebraicGeometry.Stack.flatObject_of_realization_of_isVersal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFlatAssembly.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingFlatAssembly.lean#L258).

> **Stacks 0DR2.** In Situation 0DQU — `𝒳` an algebraic stack locally of finite type over a
> locally Noetherian scheme `S` — let `x₀ : Spec k ⟶ 𝒳` be a point with `k` a field of finite type
> over `S`, presented over an affine open `Spec Λ ⊆ S`, and let `A` be a versal ring to `𝒳` at
> `x₀`, with versal formal object `ξ` over `A`. Then the morphism `Spec A ⟶ 𝒳` of Stacks 0DR1 —
> any object `y` of `𝒳` over `Spec A` realizing `ξ`, i.e. whose restrictions to the infinitesimal
> thickenings of the closed point are the levels of `ξ` — is flat.
>
> The proof is the source's: Step III reaches a point of a smooth chart, where the morphism is
> `Spec(𝒪^∧_{U, u₀}) ⟶ U ⟶ 𝒳`, through two field extensions, and Steps I and II carry flatness
> back along the faithfully flat comparisons of parts (1) and (2) of Stacks 0DR1.

```lean
theorem flatObject_of_realization_of_isVersal
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (ξ : Deformation.FormalObject (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection)
    (hξ : Deformation.IsVersal (Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ)
    {hA : D.B.Contains (Spec (.of ξ.base))} {y : D.𝒳.val.val.obj}
    {hy : D.𝒳.val.val.p.obj y = Deformation.Artin.baseOver D.B D.S D.hS
      (Deformation.Artin.completeLocalAlgFormalBase iΛ hfinite ξ.base) hA}
    (Ry : (Deformation.Artin.FormalObject.ofPredeformation D.B D.S D.hS iΛ D.𝒳.val.val.p x₀ hx₀
      hfinite ξ).Realization hA y hy) :
    flatObject D.B D.S D.hS D.𝒳.val y
```

## Tag 0DR3, a remark

[Tag 0DR3](https://stacks.math.columbia.edu/tag/0DR3) in the Stacks Project.

**`Deformation.RepresentablePresentation.comultiplication`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean#L142). The attribute's comment: “the comultiplication c : B ⟶ B ⊗̂\_\{s,A,t} B of the cogroupoid (A,B,s,t,c)”.

> **Stacks 0DR3.** The comultiplication `c : B ⟶ B ⊗̂_{s, A, t} B` of a representable
> presentation `(A, B, s, t)`: the composite of the two pushout inclusions under the presentation's
> composition law.

```lean
def comultiplication (P : RepresentablePresentation.{u, v, w} C) :
    P.arrows ⟶ pushout P.source P.target
```

**`Deformation.RepresentablePresentation.isCogroupoid_comultiplication`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean#L179). The attribute's comment: “(A,B,s,t,c) is a cogroupoid of complete local algebras”.

> **Stacks 0DR3.** A representable presentation `(A, B, s, t)` and its comultiplication `c` form
> a cogroupoid.

```lean
theorem isCogroupoid_comultiplication (P : RepresentablePresentation.{u, v, w} C) :
    IsCogroupoid.{u, v, w} P.source P.target P.comultiplication
```

**`Deformation.exists_cogroupoid_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean#L298). The attribute's comment: “the equivalence [A/B] → 𝓕 of groupoids cofibred over 𝒞\_Λ”.

> **Stacks 0DR3.** Unwinding a presentation of a category cofibered in groupoids over `𝒞_Λ` by
> a prorepresentable groupoid in functors: there are a cogroupoid `(A, B, s, t, c)` of Noetherian
> complete local `Λ`-algebras with residue field `k` and an equivalence
> `[A|_{𝒞_Λ} / B|_{𝒞_Λ}] ⟶ 𝓕` of groupoids cofibered over `𝒞_Λ`.

```lean
theorem exists_cogroupoid_presentation
    {F : Type uF} [Category.{vF} F]
    (p : F ⥤ ArtinianLocalAlgCat.{uΛ, v, uk} Λ k)
    {G : GroupoidInFunctors.{_, v, max v uz} (ArtinianLocalAlgCat.{uΛ, v, uk} Λ k)}
    (hG : GroupoidInFunctors.IsProrepresentable G) (E : Presentation G p) :
    ∃ P : RepresentablePresentation.{_, v, uz} (CompleteLocalAlgCat.{uΛ, v, uk} Λ k),
      IsCogroupoid.{_, v, uz} P.source P.target P.comultiplication ∧
        Nonempty (Presentation
          (GroupoidInFunctors.restrict P.groupoidInFunctors artinianToComplete) p)
```

**`AlgebraicGeometry.Stack.isVersalRingAt_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingCogroupoid.lean#L326). The attribute's comment: “A is a versal ring to 𝒳 at x₀”.

> **Stacks 0DR3**, last clause. The base of a versal formal object of the deformation category
> of a field-valued point of `𝒳` is a versal ring to `𝒳` at that point.

```lean
theorem isVersalRingAt_base
    (D : AlgebraicGeometry.Stack.VersalSituation.{u, w})
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : _root_.AlgebraicGeometry.LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      _root_.AlgebraicGeometry.QuasiCompact
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let C := Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀
    letI : Category C.carrier := C.category
    ∀ ξ : Deformation.FormalObject C.projection,
      Deformation.IsVersal
          (Deformation.Artin.predeformationCategory_isPredeformationCategory
            D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property).cofibered ξ →
        IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite ξ.base
```

**`AlgebraicGeometry.Stack.hasSmoothPresentation_predeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingPresentation.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingPresentation.lean#L227). The attribute's comment: “F\_\{X,k,x₀} has a presentation by a smooth prorepresentable groupoid in functors”.

> **Stacks 0DR3**, first sentence. In Situation 0DQU, let `x₀` be an object of `𝒳` over
> `Spec k` for a field `k` of finite type over `S`, and let `Spec Λ ⊆ S` be an affine open through
> which `Spec k ⟶ S` factors with `Λ → k` finite. Then `𝓕_{𝒳,k,x₀}` has a presentation by a smooth
> prorepresentable groupoid in functors on `𝒞_Λ`: this is Stacks 0DQW and Stacks 06L8.

```lean
theorem hasSmoothPresentation_predeformationCategory
    (D : VersalSituation.{u, w}) {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k] (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    letI := (Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).category
    Deformation.HasSmoothPresentation
      (Deformation.Artin.predeformationCategory iΛ
        (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀).projection
```

**`AlgebraicGeometry.Stack.exists_versalCogroupoid_predeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/VersalRingPresentation.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/VersalRingPresentation.lean#L264). The attribute's comment: “the unwinding: A with a versal formal object ξ, B with B|\_\{𝒞\_Λ} ≅ A|\_\{𝒞\_Λ} ×\_\{ξ,F,ξ} A|\_\{𝒞\_Λ}, the projections formally smooth maps s, t : A → B, (A,B,s,t,c) a cogroupoid, the equivalence [A|\_\{𝒞\_Λ}/B|\_\{𝒞\_Λ}] → F induced by ξ, the equivalence [A/B] → F^ over the completed category, and A a versal ring to 𝒳 at x₀”.

> **Stacks 0DR3**, the unwinding for `𝓕_{𝒳,k,x₀}`. In Situation 0DQU, let `x₀` be an object of
> `𝒳` over `Spec k` for a field `k` of finite type over `S`, and let `Spec Λ ⊆ S` be an affine open
> through which `Spec k ⟶ S` factors with `Λ → k` finite. Then there are
> 1. a versal formal object `ξ` of `𝓕 = 𝓕_{𝒳,k,x₀}` over a Noetherian complete local `Λ`-algebra
>    `A` with residue field `k`, and
> 2. a Noetherian complete local `Λ`-algebra `B` with residue field `k` and an isomorphism
>    `B|_{𝒞_Λ} ≅ A|_{𝒞_Λ} ×_{ξ, 𝓕, ξ} A|_{𝒞_Λ}`,
>
> namely a representable presentation `P` on `𝒞^_Λ` with objects `A` and arrows `B` whose
> restriction to `𝒞_Λ` is isomorphic to the groupoid in functors of `ξ` (Stacks 06KY), such that
> the projections are induced by formally smooth maps `s, t : A ⟶ B` (power series maps, formally
> smooth for the `𝔪_B`-adic topology), the comultiplication `c : B ⟶ B ⊗̂_{s, A, t} B` makes
> `(A, B, s, t, c)` a cogroupoid, `ξ` induces an equivalence `[A|_{𝒞_Λ} / B|_{𝒞_Λ}] → 𝓕` of groupoids
> cofibred over `𝒞_Λ`, there is an equivalence `[A/B] → 𝓕^` of groupoids cofibred over `𝒞^_Λ`, and
> `A` is a versal ring to `𝒳` at `x₀`.

```lean
theorem exists_versalCogroupoid_predeformationCategory
    (D : VersalSituation.{u, w}) {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k]
    [Module.Finite Λ k] (iΛ : Spec (.of Λ) ⟶ D.S) (hiΛ : AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : D.𝒳.val.val.obj)
    (hx₀ : (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    let C := Deformation.Artin.predeformationCategory iΛ
      (D.𝒳.val.val.p ⋙ Over.post D.B.inclusion) x₀ hx₀
    letI := C.category
    let hp := Deformation.Artin.predeformationCategory_isPredeformationCategory
      D.B D.hS iΛ D.𝒳.val.val.p x₀ hx₀ D.𝒳.val.property
    ∃ (ξ : Deformation.FormalObject C.projection) (_ : Deformation.IsVersal hp.cofibered ξ)
      (P : Deformation.RepresentablePresentation.{_, u, u}
        (Deformation.CompleteLocalAlgCat.{u, u, u} Λ k)),
      P.objects = ξ.base ∧
      Nonempty (Deformation.versalGroupoid C.projection hp ξ ≅
        Deformation.GroupoidInFunctors.restrict P.groupoidInFunctors
          Deformation.artinianToComplete) ∧
      (Deformation.IsPowerSeriesOver P.source ∧
        RingHom.FormallySmoothNAdic.{u} P.source.hom.toRingHom
          (IsLocalRing.maximalIdeal P.arrows)) ∧
      (Deformation.IsPowerSeriesOver P.target ∧
        RingHom.FormallySmoothNAdic.{u} P.target.hom.toRingHom
          (IsLocalRing.maximalIdeal P.arrows)) ∧
      Deformation.IsCogroupoid.{_, u, u} P.source P.target P.comultiplication ∧
      Nonempty (Deformation.Presentation (Deformation.GroupoidInFunctors.restrict
        P.groupoidInFunctors Deformation.artinianToComplete) C.projection) ∧
      Nonempty (Deformation.Presentation P.groupoidInFunctors
        (Deformation.FormalObject.projection (p := C.projection))) ∧
      IsVersalRingAt D iΛ hiΛ x₀ hx₀ hfinite P.objects
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 107.2, Tag 0DQT](https://stacks.math.columbia.edu/tag/0DQT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
