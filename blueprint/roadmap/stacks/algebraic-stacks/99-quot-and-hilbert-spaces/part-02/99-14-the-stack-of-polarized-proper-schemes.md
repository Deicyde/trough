---
declaration: section
origin: cited
lean: AlgebraicGeometry.PolarizedFamily, AlgebraicGeometry.PolarizedFamily.Hom, AlgebraicGeometry.PolarizedFamily.instCategory, AlgebraicGeometry.polarizedProjection, AlgebraicGeometry.forgetPolarization, AlgebraicGeometry.forgetPolarization_obj_base, AlgebraicGeometry.forgetPolarization_map_base, AlgebraicGeometry.polarizedSpacesForget_isFiberedInGroupoids
statement: formalized
proof: formalized
---

# 99.14 The stack of polarized proper schemes

Section 99.14 of the Stacks Project, [Tag 0D1L](https://stacks.math.columbia.edu/tag/0D1L). 15 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D1M, a situation

[Tag 0D1M](https://stacks.math.columbia.edu/tag/0D1M) in the Stacks Project.

**`AlgebraicGeometry.PolarizedFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean#L73). The attribute's comment: “objects”.

> **Stacks 0D1M.** A *polarized family*: a proper, flat, finitely presented morphism from a
> scheme to a scheme of the big fppf site, together with an invertible module on the total space
> which is relatively ample for that morphism.

```lean
structure PolarizedFamily
```

**`AlgebraicGeometry.PolarizedFamily.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean#L103). The attribute's comment: “morphisms”.

> **Stacks 0D1M.** A morphism of polarized families: a morphism of total spaces over a morphism
> of base schemes whose square is cartesian, together with an isomorphism from the pullback of the
> polarization of the target to the polarization of the source.

```lean
structure Hom (X Y : PolarizedFamily B)
```

**`AlgebraicGeometry.PolarizedFamily.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean#L247). The attribute's comment: “category”.

> **Stacks 0D1M.** Polarized families, cartesian squares between them and comparisons of
> polarizations form a category: the two underlying morphisms compose componentwise and the
> comparisons compose through the pullback pseudofunctor.

```lean
instance instCategory : Category.{u} (PolarizedFamily B)
```

**`AlgebraicGeometry.polarizedProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamilies.lean#L278). The attribute's comment: “projection”.

> **Stacks 0D1M.** The forgetful functor taking a polarized family to its base scheme, which is
> how the category of polarized families is viewed as a category over the big fppf site.

```lean
def polarizedProjection : PolarizedFamily B ⥤ B.Schemes
```

## Tag 0D3Y, an equation

[Tag 0D3Y](https://stacks.math.columbia.edu/tag/0D3Y) in the Stacks Project.

**`AlgebraicGeometry.forgetPolarization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesForget.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesForget.lean#L258). The attribute's comment: “the forgetful functor”.

> **Stacks 0D3Y.** Forget the polarization of a polarized family, keeping the finitely
> presented, flat and proper family of algebraic spaces over the same base.

```lean
def forgetPolarization :
    PolarizedFamily B ⥤ CartesianProperFlatSpaces B integerBase B.contains_integerBase
```

**`AlgebraicGeometry.forgetPolarization_obj_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesForget.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesForget.lean#L306). The attribute's comment: “the forgetful functor is over the site”.

> **Stacks 0D3Y.** Forgetting the polarization keeps the base scheme, so the forgetful functor
> is a functor over the big fppf site.

```lean
theorem forgetPolarization_obj_base (X : PolarizedFamily B) :
    (cartesianProperFlatProjection B integerBase B.contains_integerBase).obj
      ((forgetPolarization B).obj X) = (schemeOverIntegers B).obj X.base
```

**`AlgebraicGeometry.forgetPolarization_map_base`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesForget.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesForget.lean#L313). The attribute's comment: “the forgetful functor is over the site”.

> **Stacks 0D3Y.** Forgetting the polarization keeps the morphism of base schemes.

```lean
theorem forgetPolarization_map_base {X Y : PolarizedFamily B} (f : X ⟶ Y) :
    (cartesianProperFlatProjection B integerBase B.contains_integerBase).map
      ((forgetPolarization B).map f) = (schemeOverIntegers B).map f.baseMap
```

## Tag 0D3Z, a lemma

[Tag 0D3Z](https://stacks.math.columbia.edu/tag/0D3Z) in the Stacks Project.

**`AlgebraicGeometry.polarizedSpacesForget_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesFiberedForget.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesFiberedForget.lean#L122). The attribute's comment: “fibred in groupoids over the stack of finitely presented, flat and proper families”.

> **Stacks 0D3Z.** Polarized families are fibred in groupoids over the finitely presented, flat
> and proper families of algebraic spaces of Stacks 0D1E.
>
> Condition (a) of Stacks 003S is base change of the polarized family along the base scheme of the
> given family of algebraic spaces, and condition (b) holds because the base morphism the fill-in
> must lie over is forced by the two comparison isomorphisms, so the fill-in is the one
> `AlgebraicGeometry.polarizedProjection_uniqueLift` provides over the site.

```lean
theorem polarizedSpacesForget_isFiberedInGroupoids :
    (polarizedSpacesForget B).IsFiberedInGroupoids
```

**`AlgebraicGeometry.toPolarizedSpaces_comp_polarizedSpacesForget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesFiberedForget.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesFiberedForget.lean#L149). The attribute's comment: “identification of the replacement category with the polarized families”.

> **Stacks 0D3Z.** The comparison equivalence carries the projection of
> `AlgebraicGeometry.PolarizedSpaces` to the family of algebraic spaces back to the forgetful
> functor of Stacks 0D3Y, so `AlgebraicGeometry.polarizedSpacesForget_isFiberedInGroupoids` is the
> assertion of the tag for `AlgebraicGeometry.forgetPolarization`.

```lean
theorem toPolarizedSpaces_comp_polarizedSpacesForget :
    toPolarizedSpaces B ⋙ polarizedSpacesForget B = forgetPolarization B
```

**`AlgebraicGeometry.polarizedProjection_isFiberedInGroupoids_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedStackUnconditional.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedStackUnconditional.lean#L59). The attribute's comment: “fibred in groupoids over the fppf site of schemes”.

> **Stacks 003S for polarized families, with no hypothesis.** Polarized families of Stacks
> 0D1M form a category fibred in groupoids over the big fppf site.
>
> This is also **Stacks 0D3Z** over the big fppf site of schemes: condition (a) of Stacks 003S is
> `AlgebraicGeometry.polarizedProjection_existsLift`, by base change, and condition (b) is
> `AlgebraicGeometry.polarizedProjection_uniqueLift`.

```lean
theorem polarizedProjection_isFiberedInGroupoids_unconditional {B : BigFppfSite.{u}} :
    (polarizedProjection B).IsFiberedInGroupoids
```

## Tag 0D40, a lemma

[Tag 0D40](https://stacks.math.columbia.edu/tag/0D40) in the Stacks Project.

**`AlgebraicGeometry.polarized_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedStackRepresentable.lean, line 872](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedStackRepresentable.lean#L872).

> **Stacks 0D40.** The category `𝒫olarized` of polarized families is a stack in groupoids over
> `Spaces'_{fp, flat, proper}`, endowed with the topology inherited from the big fppf site
> (Stacks 06NV), and it is a stack in groupoids over the big fppf site of schemes.

```lean
theorem polarized_isStackInGroupoids :
    (polarizedSpacesForget B).IsStackInGroupoids.{w}
        ((polarizedFamiliesProperFlatProjection B).inheritedTopology B.topology) ∧
      (polarizedProjection B).IsStackInGroupoids.{w} B.topology
```

## Tag 0E94, a lemma

[Tag 0E94](https://stacks.math.columbia.edu/tag/0E94) in the Stacks Project.

**`AlgebraicGeometry.PolarizedOverSpace.polarizedBaseChange_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedOverSpaceEquivalence.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedOverSpaceEquivalence.lean#L68). The attribute's comment: “base change is an equivalence of the polarized proper flat finitely presented spaces over T with Mor\_\{Cat/Sch\_fppf}(S\_T, Polarized)”.

> Let `T` be an algebraic space over `Spec(ℤ)` and `𝒮_T` its algebraic stack. Base change is an
> equivalence from the category of pairs `(X ⟶ T, L)`, where `X ⟶ T` is a proper, flat and finitely
> presented morphism of algebraic spaces and `L` is an invertible module ample on `X/T`, to the
> category of functors over the site from `𝒮_T` to `Polarized`
> (`Mor_{Cat/Sch_fppf}(𝒮_T, Polarized)`).

```lean
theorem polarizedBaseChange_isEquivalence : (polarizedBaseChange B T).IsEquivalence
```

## Tag 0D1N, a remark

[Tag 0D1N](https://stacks.math.columbia.edu/tag/0D1N) in the Stacks Project.

**`AlgebraicGeometry.PolarizedFamilyOver`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean#L81). The attribute's comment: “objects”.

> **Stacks 0D1N.** A *polarized family over the space* `A`: a polarized family together with a
> structure morphism of its base scheme over the base of the site and a point of `A` there.

```lean
structure PolarizedFamilyOver
```

**`AlgebraicGeometry.PolarizedFamilyOver.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean#L102). The attribute's comment: “morphisms”.

> **Stacks 0D1N.** A morphism of polarized families over `A`: a morphism of the underlying
> polarized families whose base map lies over the base of the site and carries the point of the
> target to the point of the source.

```lean
structure Hom (X Y : PolarizedFamilyOver B S hS A)
```

**`AlgebraicGeometry.PolarizedFamilyOver.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean#L135). The attribute's comment: “category”.

> **Stacks 0D1N.** Polarized families over `A` and the morphisms compatible with their points
> form a category, with the identities and composition of the underlying polarized families.

```lean
instance instCategory : Category.{u} (PolarizedFamilyOver B S hS A)
```

**`AlgebraicGeometry.PolarizedFamilyOver.isEquivalence_toCategoricalPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFamiliesOverSpace.lean#L293). The attribute's comment: “the 2-fibre product square”.

> **Stacks 0D1N.** The canonical comparison from polarized families over `A` to the 2-fibre
> product of polarized families and schemes carrying a point of `A`, over the big fppf site of
> schemes, is an equivalence: the displayed square is a 2-fibre product square.

```lean
theorem isEquivalence_toCategoricalPullback :
    (toCategoricalPullback B S hS A).IsEquivalence
```

## Tag 0D41, a lemma

[Tag 0D41](https://stacks.math.columbia.edu/tag/0D41) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicMorphism_forgetPolarizationOneMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedForgetAlgebraicMorphism.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedForgetAlgebraicMorphism.lean#L65).

> **Stacks 0D41.** The forgetful functor of Stacks 0D3Y, `(X ⟶ S, ℒ) ↦ (X ⟶ S)`, defines a
> 1-morphism `Polarized ⟶ Spaces'_{fp, flat, proper}` of stacks in groupoids over the big fppf site
> of `Spec ℤ` (Stacks 0D40, 0D1G) which is algebraic in the sense of Stacks 06CF: its 2-fibre
> product with every scheme-valued point of `Spaces'_{fp, flat, proper}` is an algebraic stack.

```lean
theorem isAlgebraicMorphism_forgetPolarizationOneMorphism :
    Stack.IsAlgebraicMorphism.{u, w, w, w} B integerBase B.contains_integerBase
      (𝒳 := polarizedStackInGroupoids.{w} B (polarizedProjection_isStack B))
      (𝒴 := properFlatSpacesStackInGroupoids.{w} B integerBase B.contains_integerBase)
      (forgetPolarizationBased B)
```

## Tag 0D42, a lemma

[Tag 0D42](https://stacks.math.columbia.edu/tag/0D42) in the Stacks Project.

**`AlgebraicGeometry.hasRepresentableDiagonal_polarizedStackUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedDiagonal.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedDiagonal.lean#L64).

> The diagonal `𝒫olarized ⟶ 𝒫olarized × 𝒫olarized` of the stack of polarized proper flat
> families of finite presentation, over the big fppf site of a terminal base scheme, is representable
> by algebraic spaces.

```lean
theorem hasRepresentableDiagonal_polarizedStackUnconditional :
    Stack.HasRepresentableDiagonal B S hS (polarizedStackUnconditional B hS hT)
```

## Tag 0D43, a lemma

[Tag 0D43](https://stacks.math.columbia.edu/tag/0D43) in the Stacks Project.

**`AlgebraicGeometry.isLimitPreservingPolarizedUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedLimitPreservingProof.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedLimitPreservingProof.lean#L80). The attribute's comment: “at a small index category”.

> **Stacks 0D43.** The stack in groupoids `𝒫olarized` of polarized proper schemes is limit
> preserving in the sense of Stacks 07XL: for every cofiltered inverse system of affine schemes over
> the terminal base whose limit of underlying schemes is `T`, the canonical comparison
> `colim 𝒫olarized_{Tᵢ} ⥤ 𝒫olarized_T` is an equivalence of categories. The index category is taken
> in the scheme universe, which is the smallness the source's directed sets have.

```lean
theorem isLimitPreservingPolarizedUnconditional (B : BigFppfSite.{u}) {S : Scheme.{u}}
    (hS : B.Contains S) (hT : IsTerminal (B.obj hS)) :
    IsLimitPreservingPolarizedUnconditional.{u, u, u} B hS hT
```

## Tag 0D44, a lemma

[Tag 0D44](https://stacks.math.columbia.edu/tag/0D44) in the Stacks Project.

**`AlgebraicGeometry.polarizedPushoutRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedPushout.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedPushout.lean#L350). The attribute's comment: “the functor of the comparison on fibre categories; that it is an equivalence is not proved here, Stacks 07RX being absent”.

> **Stacks 0D44.** For a commutative square `f ≫ h = i ≫ g` of schemes of the big fppf site,
> the comparison functor from the polarized families with base `S'` to the 2-fibre product of those
> with base `S` and those with base `T'` over those with base `T`.

```lean
def polarizedPushoutRestriction {T T' S S' : B.Schemes} (i : T ⟶ T') (f : T ⟶ S) (g : T' ⟶ S')
    (h : S ⟶ S') (hsq : f ≫ h = i ≫ g) :
    (polarizedProjection B).Fiber S' ⥤
      (polarizedFiberPullback B f) ⊡ (polarizedFiberPullback B i)
```

**`AlgebraicGeometry.isEquivalence_polarizedPushoutRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedPushoutEquivalence.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedPushoutEquivalence.lean#L284). The attribute's comment: “the comparison functor `polarizedPushoutRestriction` of a pushout square of schemes with `T ⟶ T'` a thickening and `T ⟶ S` affine is an equivalence”.

> **Stacks 0D44.** Let
>
> ```
> T  --i-->  T'
> |          |
> f          g
> |          |
> v          v
> S  --h-->  S'
> ```
>
> be a pushout in the category of schemes, of schemes of the big fppf site, where `T ⟶ T'` is a
> thickening and `T ⟶ S` is affine. Then the functor on fibre categories of the stack of polarized
> schemes
>
> `𝒫olarized_{S'} ⟶ 𝒫olarized_S ×_{𝒫olarized_T} 𝒫olarized_{T'}`
>
> is an equivalence. (The source states the lemma "in Situation 08KB"; that situation fixes data
> which the statement does not use.)

```lean
theorem isEquivalence_polarizedPushoutRestriction {T T' S S' : B.Schemes} (i : T ⟶ T')
    (f : T ⟶ S) (g : T' ⟶ S') (h : S ⟶ S') (hsq : f ≫ h = i ≫ g)
    (hpush : IsPushout (B.inclusion.map f) (B.inclusion.map i) (B.inclusion.map h)
      (B.inclusion.map g))
    (hi : IsThickening (B.inclusion.map i)) [IsAffineHom (B.inclusion.map f)] :
    (polarizedPushoutRestriction B i f g h hsq).IsEquivalence
```

## Tag 0D4S, a lemma

[Tag 0D4S](https://stacks.math.columbia.edu/tag/0D4S) in the Stacks Project.

**`AlgebraicGeometry.PolarizedDeformation.finiteDimensional_tangentFunctor_infinitesimalAutomorphismFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedDeformationFiniteDimensional.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedDeformationFiniteDimensional.lean#L64). The attribute's comment: “(2): for a polarized proper scheme x over any field k, the functors T\_x and Inf\_x of Stacks 07Y9 exist (𝒫olarized satisfies RS* by 0D44) and T\_x(k) and Inf\_x(k) are finite dimensional; both finiteness statements hold for every k-linear functor carrying the identifications of 07Y9”.

> **Stacks Project, Tag 0D4S, part (2).** Let `k` be a field and let `x = (X → Spec k, ℒ)` be an
> object of `𝒫olarized` over `Spec k`. Then the tangent functor `T_x` and the functor of
> infinitesimal automorphisms `Inf_x` of Stacks 07Y9 exist, and `T_x(k)` and `Inf_x(k)` are
> finite-dimensional `k`-vector spaces.
>
> Each functor is stated as a structure (`TangentFunctorData`,
> `InfinitesimalAutomorphismFunctorData`) carrying a `k`-linear functor on the site modules together
> with its identification with the isomorphism classes of lifts of `x`, respectively with the
> infinitesimal automorphisms of the trivial lifts of `x`, natural in the module. The statement gives
> that such a functor exists and that the value at `k` of every such functor is finite-dimensional.
> No condition on `k` is assumed.

```lean
theorem finiteDimensional_tangentFunctor_infinitesimalAutomorphismFunctor {k : Type u} [Field k]
    (toS : Spec (.of k) ⟶ S) (hk : B.Contains (Spec (.of k))) (x : PolarizedFamily B)
    (hx : (polarizedSliceProjection B hS hT).obj x = algebraOver k B S hS toS hk) :
    (Nonempty (TangentFunctorData k B S hS toS hk (polarizedSliceProjection B hS hT) x hx) ∧
      ∀ T : TangentFunctorData k B S hS toS hk (polarizedSliceProjection B hS hT) x hx,
        FiniteDimensional k (T.functor.obj ((fgSiteModule B hk).obj (FGModuleCat.of k k)))) ∧
    (Nonempty (InfinitesimalAutomorphismFunctorData k B S hS toS hk
        (polarizedSliceProjection B hS hT) x hx
        (isFiberedInGroupoids_polarizedSliceProjection B hS hT)) ∧
      ∀ I : InfinitesimalAutomorphismFunctorData k B S hS toS hk
          (polarizedSliceProjection B hS hT) x hx
          (isFiberedInGroupoids_polarizedSliceProjection B hS hT),
        FiniteDimensional k (I.functor.obj ((fgSiteModule B hk).obj (FGModuleCat.of k k))))
```

**`AlgebraicGeometry.PolarizedDeformation.isFiniteDimensionalDeformationCategory_predeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedDeformationFiniteDimensional.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedDeformationFiniteDimensional.lean#L98). The attribute's comment: “(1): for a field k of finite type over the base and a polarized proper scheme x over k, the deformation category F\_\{X,k,x} has finite dimensional tangent space T F\_\{X,k,x} and finite dimensional Inf(F\_\{X,k,x}); the base is any terminal scheme of the site, e.g. Spec Z”.

> **Stacks Project, Tag 0D4S, part (1).** Let `k` be a field of finite type over the base (for
> the base `Spec ℤ`: of finite type over `ℤ`), presented through `Spec k ⟶ Spec Λ ⟶ S`, and let
> `x = (X → Spec k, ℒ)` be an object of `𝒫olarized` over `Spec k`. Then the predeformation category
> `𝓕_{𝒳,k,x}` of Stacks 07T2 is a deformation category whose tangent space `T𝓕_{𝒳,k,x}` and whose
> infinitesimal automorphisms `Inf(𝓕_{𝒳,k,x})` (Stacks 07WY) are finite-dimensional `k`-vector
> spaces.
>
> The base is any scheme `S` which is terminal in the big fppf site; no condition is put on `Λ`
> beyond the factorization.

```lean
theorem isFiniteDimensionalDeformationCategory_predeformationCategory
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] (iΛ : Spec (.of Λ) ⟶ S)
    (x : PolarizedFamily B)
    (hx₀ : (polarizedSliceProjection B hS hT ⋙ Over.post B.inclusion).obj x =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ))
    (hfinite : LocallyOfFiniteType (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    IsFiniteDimensionalDeformationCategory
      (predeformationCategory iΛ (polarizedSliceProjection B hS hT ⋙ Over.post B.inclusion) x
        hx₀).projection
```

## Tag 0D4T, a lemma

[Tag 0D4T](https://stacks.math.columbia.edu/tag/0D4T) in the Stacks Project.

**`Stacks.PolarizedAlgebraization.exists_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PolarizedAlgebraization/StrongFormalEffectiveness.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PolarizedAlgebraization/StrongFormalEffectiveness.lean#L115). References: SGA 7 IX (7.1.3), “partial”.

> **Strong formal effectiveness for polarized schemes.** Let `(R_n)` be an inverse system of
> rings with surjective transition maps whose kernels are locally nilpotent, and `R = lim R_n`. Let
> `X_n ⟶ Spec R_n` be schemes with cartesian squares over the transitions
> `Spec R_n ⟶ Spec R_{n + 1}`, `ℒ_n` invertible `𝒪_{X_n}`-modules and `φ_n : i_n^* ℒ_{n + 1} ≅ ℒ_n`.
> If every `X_n ⟶ Spec R_n` is proper, flat and of finite presentation, and `ℒ_0` is ample, then
> there are a proper, flat, finitely presented `X ⟶ Spec R`, an ample invertible `ℒ` on `X`,
> identifications `X_n ≅ X ×_{Spec R} Spec R_n` (cartesian squares through `j_n : X_n ⟶ X`) and
> isomorphisms `e_n : ℒ|_{X_n} ≅ ℒ_n`, compatible with the `i_n` and the `φ_n`. The index `n : ℕ`
> stands for the source's `n + 1`.

```lean
theorem exists_algebraization (R : ℕᵒᵖ ⥤ CommRingCat.{u})
    (hsurj : ∀ n : ℕ, Function.Surjective (R.map (homOfLE (Nat.le_succ n)).op).hom)
    (hnil : ∀ n : ℕ,
      RingHom.ker (R.map (homOfLE (Nat.le_succ n)).op).hom ≤ nilradical (R.obj (op (n + 1))))
    (X : ℕ → Scheme.{u}) (f : ∀ n : ℕ, X n ⟶ Spec (R.obj (op n)))
    (i : ∀ n : ℕ, X n ⟶ X (n + 1))
    (hpb : ∀ n : ℕ,
      IsPullback (i n) (f n) (f (n + 1)) (Spec.map (R.map (homOfLE (Nat.le_succ n)).op)))
    (L : ∀ n : ℕ, (X n).Modules) [hL : ∀ n : ℕ, IsInvertibleModule (X n) (L n)]
    (φ : ∀ n : ℕ, (Scheme.Modules.pullback (i n)).obj (L (n + 1)) ≅ L n)
    [hproper : ∀ n : ℕ, IsProper (f n)] [hflat : ∀ n : ℕ, Flat (f n)]
    (hfp : ∀ n : ℕ, _root_.AlgebraicGeometry.FinitePresentation (f n))
    (hample : IsAmple (X 0) (L 0)) :
    ∃ (Y : Scheme.{u}) (g : Y ⟶ Spec (limit R)) (ℒ : Y.Modules) (_ : IsInvertibleModule Y ℒ)
      (j : ∀ n : ℕ, X n ⟶ Y) (hj : ∀ n : ℕ, i n ≫ j (n + 1) = j n)
      (e : ∀ n : ℕ, (Scheme.Modules.pullback (j n)).obj ℒ ⟶ L n),
      IsProper g ∧ Flat g ∧ _root_.AlgebraicGeometry.FinitePresentation g ∧ IsAmple Y ℒ ∧
      (∀ n : ℕ, IsPullback (j n) (f n) g (Spec.map (limit.π R (op n)))) ∧
      (∀ n : ℕ, IsIso (e n)) ∧
      ∀ n : ℕ, (Scheme.Modules.pullbackComp (i n) (j (n + 1))).hom.app ℒ ≫
          (Scheme.Modules.pullbackCongr (hj n)).hom.app ℒ ≫ e n =
        (Scheme.Modules.pullback (i n)).map (e (n + 1)) ≫ (φ n).hom
```

## Tag 0D4U, a lemma

[Tag 0D4U](https://stacks.math.columbia.edu/tag/0D4U) in the Stacks Project.

**`AlgebraicGeometry.polarizedFormalObject_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedFormalEffective.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedFormalEffective.lean#L474).

> **Stacks 0D4U.** Consider the stack `𝒫olarized` over the base scheme `Spec ℤ`. Then every
> formal object (Stacks 07X4) is effective (Stacks 07X7): it is, up to isomorphism, the system of
> restrictions to the infinitesimal thickenings `Spec(R / 𝔪^{n+1})` of a polarized family over its
> complete local base `Spec R`.

```lean
theorem polarizedFormalObject_isEffective (B : BigFppfSite.{u})
    (hZ : B.Contains (Spec (CommRingCat.of (ULift.{u} ℤ))))
    (ξ : FormalObject B _ hZ (polarizedSliceProjection B hZ (isTerminal_obj_specULiftZ B hZ))) :
    FormalObject.IsEffective B _ hZ (polarizedSliceProjection B hZ (isTerminal_obj_specULiftZ B hZ))
      (polarizedProjection_isFiberedInGroupoids_unconditional.sliceAtTerminal
        (isTerminal_obj_specULiftZ B hZ)) ξ
```

## Tag 0D4V, a lemma

[Tag 0D4V](https://stacks.math.columbia.edu/tag/0D4V) in the Stacks Project.

**`AlgebraicGeometry.hasOpenVersality_polarizedStackUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedVersality/PolarizedOpennessOfVersality.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedVersality/PolarizedOpennessOfVersality.lean#L55). The attribute's comment: “openness of versality for `𝒫olarized` over `Spec(ℤ)`”.

> The stack in groupoids `𝒫olarized` of polarized proper flat families of finite presentation
> (Stacks 0D1M), over the big fppf site of `Spec(ℤ)`, satisfies openness of versality: if an object
> over a scheme `U` locally of finite type over `Spec(ℤ)` is versal at a finite type point `u₀`, it
> is versal at every finite type point of an open neighbourhood of `u₀`.

```lean
theorem hasOpenVersality_polarizedStackUnconditional (B : BigFppfSite.{u})
    (hZ : B.Contains (Spec (CommRingCat.of (ULift.{u} ℤ)))) :
    HasOpenVersality
      ((polarizedStackUnconditional B hZ (isTerminal_obj_specULiftZ B hZ)).val.p ⋙
        Over.post B.inclusion)
```

**`AlgebraicGeometry.hasOpenVersality_polarizedOverNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedVersality/PolarizedOpennessOfVersality.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedVersality/PolarizedOpennessOfVersality.lean#L72). The attribute's comment: “openness of versality for `S-𝒫olarized` over a Noetherian base scheme `S`”.

> For a Noetherian scheme `S`, the stack `S-𝒫olarized` of Remark 0D1N — polarized proper flat
> families of finite presentation together with a morphism of their base to `S` — over the big fppf
> site of `S` satisfies openness of versality: if an object over a scheme `U` locally of finite type
> over `S` is versal at a finite type point `u₀`, it is versal at every finite type point of an open
> neighbourhood of `u₀`.

```lean
theorem hasOpenVersality_polarizedOverNoetherian (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) [IsNoetherian S] :
    HasOpenVersality
      ((PolarizedVersality.PolarizedOver.stack B S hS).val.p ⋙ Over.post B.inclusion)
```

## Tag 0D4X, a theorem

[Tag 0D4X](https://stacks.math.columbia.edu/tag/0D4X) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicStack_polarizedStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedAlgebraicStack.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedAlgebraicStack.lean#L94).

> **Stacks 0D4X.** The stack `𝒫olarized` of polarized proper schemes (Situation 0D1M) over the
> big fppf site of `Spec ℤ` is an algebraic stack. In fact, for every algebraic space `A` over
> `Spec ℤ`, the stack `A-Polarized` of Remark 0D1N, of polarized proper schemes `(X ⟶ S, ℒ)`
> together with a morphism `S ⟶ A`, is an algebraic stack.

```lean
theorem isAlgebraicStack_polarizedStack :
    Stack.IsAlgebraicStack.{u, w} B integerBase B.contains_integerBase
        (polarizedStackUnconditional B B.contains_integerBase
          (isTerminal_obj_specULiftZ B B.contains_integerBase)).val ∧
      ∀ (A : (BigFppfOver B integerBase B.contains_integerBase)ᵒᵖ ⥤ Type u),
        IsAlgebraicSpace B integerBase B.contains_integerBase A →
        Stack.IsAlgebraicStack.{u, w} B integerBase B.contains_integerBase
          (BasedCategory.ofFunctor
            (AlgebraicGeometry.PolarizedFamilyOver.projection B integerBase
              B.contains_integerBase A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.14, Tag 0D1L](https://stacks.math.columbia.edu/tag/0D1L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
