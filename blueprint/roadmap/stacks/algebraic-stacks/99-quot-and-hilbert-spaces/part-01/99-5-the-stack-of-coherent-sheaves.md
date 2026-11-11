---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.CoherentSituation, AlgebraicGeometry.Space.CoherentObject, AlgebraicGeometry.Space.CoherentHom, AlgebraicGeometry.Space.CoherentSituation.categoryData, AlgebraicGeometry.Space.CoherentSituation.projection_isFiberedInGroupoids, AlgebraicGeometry.Space.coherentProjection_isFiberedInGroupoids, AlgebraicGeometry.Space.coherentProjection_isFiberedInGroupoids', AlgebraicGeometry.Space.CoherentSituation.coherentCFG_diagonal_isRepresentableByAlgebraicSpaces
statement: formalized
proof: formalized
---

# 99.5 The stack of coherent sheaves

Section 99.5 of the Stacks Project, [Tag 08KA](https://stacks.math.columbia.edu/tag/08KA). 12 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08KB, a situation

[Tag 08KB](https://stacks.math.columbia.edu/tag/08KB) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStack.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStack.lean#L217). The attribute's comment: “the relative algebraic space”.

> **Stacks 08KB, the standing data.**  A morphism `f : X ⟶ Y` of algebraic spaces over `S` of
> finite presentation: the relative algebraic space whose coherent sheaves with proper support
> the category `Coh_{X/Y}` classifies.

```lean
structure CoherentSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

**`AlgebraicGeometry.Space.CoherentObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStack.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStack.lean#L404). The attribute's comment: “objects”.

> **Stacks 08KB, the objects.**  An object of `Coh_{X/Y}`: a scheme `T` of the site over `Y`
> together with a quasi-coherent `𝒪_{X_T}`-module of finite presentation which is flat over `T`
> and whose support is proper over `T`.

```lean
structure CoherentObject (D : CoherentSituation B S hS)
```

**`AlgebraicGeometry.Space.CoherentHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStack.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStack.lean#L427). The attribute's comment: “morphisms”.

> **Stacks 08KB, the morphisms.**  A morphism of `Coh_{X/Y}`: a morphism `h : T ⟶ T'` of
> test schemes over `Y` together with an isomorphism `(X_h)^*F' ⟶ F` of `𝒪_{X_T}`-modules.

```lean
structure CoherentHom {D : CoherentSituation B S hS} (A A' : CoherentObject D)
```

**`AlgebraicGeometry.Space.CoherentSituation.categoryData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackCategory.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackCategory.lean#L227). The attribute's comment: “the category structure on Coh\_\{X/Y}: the identity and associativity laws, which Stacks 08KB asserts by designation and this library had left unverified”.

> **`Coh_{X/Y}` is a category**, for the canonical pseudofunctoriality datum
> `AlgebraicGeometry.Space.modulePushforwardCoherence` of the direct images of Stacks 03LU.

```lean
def categoryData : CoherentCategoryData (modulePushforwardCoherence B S hS) D
```

## Tag 08W5, a lemma

[Tag 08W5](https://stacks.math.columbia.edu/tag/08W5) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.projection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackCanonical.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackCanonical.lean#L70).

> In the situation of Stacks 08KB the projection `p : Coh_{X/Y} ⟶ (Sch/S)_fppf`, which sends
> an object `(T, g, F)` to its test scheme `T`, is fibred in groupoids.

```lean
theorem projection_isFiberedInGroupoids :
    letI : Category.{u + 1} (CoherentObject D) := D.categoryData.category
    Functor.IsFiberedInGroupoids
      (D.categoryData.projection ⋙ CostructuredArrow.proj (schemeSpaceFunctor B S hS) D.Y)
```

**`AlgebraicGeometry.Space.coherentProjection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackFibered.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackFibered.lean#L475). The attribute's comment: “conditional on the three cited base-change stability results 05VW, 0CZJ and 03DO(7)”.

> **Stacks 08W5.**  In the situation of Stacks 08KB the projection
> `p : Coh_{X/Y} ⟶ (Sch/S)_fppf`, which sends an object `(T, g, F)` to its test scheme `T`, is
> fibred in groupoids.
>
> The projection of `Coh_{X/Y}` to the test schemes over `Y` is fibred in groupoids by
> `AlgebraicGeometry.Space.coherentProjection_isFiberedInGroupoids_schemesOver`, the projection of
> the test schemes over `Y` to the schemes of the site is fibred in groupoids by
> `CategoryTheory.Functor.IsFiberedInGroupoids.costructuredArrow_proj`, and Stacks 09WW composes
> the two.
>
> **This carrier is conditional, and so asserts less than the tag.** Stacks 08W5 is
> unconditional; the `hst : ModulePullbackStability B S hS` hypothesis stands in for three cited
> results that the library does not yet carry — 05VW (flatness under base change), 0CZJ (proper
> support under base change) and clause (7) of 03DO (finite presentation of a pullback) — each
> stated in that structure at the generality of its own source page. The attribute is qualified
> accordingly, and no unqualified 08W5 claim is made here. Discharging those three fields turns
> this into the tag itself with no change to the statement below.

```lean
theorem coherentProjection_isFiberedInGroupoids
    (hc : ModulePushforwardCoherence B S hS) (hst : ModulePullbackStability B S hS)
    {D : CoherentSituation B S hS} (cd : CoherentCategoryData hc D) :
    letI : Category.{u + 1} (CoherentObject D) := cd.category
    Functor.IsFiberedInGroupoids
      (cd.projection ⋙ CostructuredArrow.proj (schemeSpaceFunctor B S hS) D.Y)
```

**`AlgebraicGeometry.Space.coherentProjection_isFiberedInGroupoids'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackFiberedUnconditional.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackFiberedUnconditional.lean#L178). The attribute's comment: “for a given category structure on the objects”.

> **Stacks 08W5.**  In the situation of Stacks 08KB the projection
> `p : Coh_{X/Y} ⟶ (Sch/S)_fppf`, which sends an object `(T, g, F)` to its test scheme `T`, is
> fibred in groupoids.

```lean
theorem coherentProjection_isFiberedInGroupoids'
    (hc : ModulePushforwardCoherence B S hS) {D : CoherentSituation B S hS}
    (cd : CoherentCategoryData hc D) :
    letI : Category.{u + 1} (CoherentObject D) := cd.category
    Functor.IsFiberedInGroupoids
      (cd.projection ⋙ CostructuredArrow.proj (schemeSpaceFunctor B S hS) D.Y)
```

## Tag 08W6, a lemma

[Tag 08W6](https://stacks.math.columbia.edu/tag/08W6) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.coherentCFG_diagonal_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentStackDiagonalRepresentable.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/CoherentStackDiagonalRepresentable.lean#L65).

> **Stacks 08W6.** In Situation 08KB, with `𝒳 = Coh_{X/Y}` the stack of coherent sheaves with
> proper support of a morphism `f : X ⟶ Y` of finite presentation of algebraic spaces over `S`,
> the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is representable by algebraic spaces.

```lean
theorem coherentCFG_diagonal_isRepresentableByAlgebraicSpaces (D : CoherentSituation B S hS) :
    Stack.IsRepresentableByAlgebraicSpaces B S hS
      (Stack.diagonalBasedFunctor B S hS D.coherentCFG)
```

## Tag 08KC, a lemma

[Tag 08KC](https://stacks.math.columbia.edu/tag/08KC) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackIsStackInGroupoids.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackIsStackInGroupoids.lean#L65).

> **Stacks 08KC.**  In Situation 08KB the projection `Coh_{X/Y} ⟶ (Sch/S)_fppf`,
> `(T, g, F) ↦ T`, makes the category `Coh_{X/Y}` of Stacks 08KB a stack in groupoids over the big
> fppf site of `S`.

```lean
theorem isStackInGroupoids :
    (coherentBasedCategory D.categoryData).p.IsStackInGroupoids.{w}
      (BigFppfOver.topology B S hS)
```

## Tag 08LP, a remark

[Tag 08LP](https://stacks.math.columbia.edu/tag/08LP) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.canonicalBaseChangeSquare_isTwoFibreProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackCanonical.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackCanonical.lean#L98). The attribute's comment: “the base-change square is 2-cartesian”.

> The square `Coh_{X'/Y'} ⟶ Coh_{X/Y}`, `𝒮_{Y'} ⟶ 𝒮_Y` is 2-cartesian: `Coh_{X'/Y'}`, with
> the base-change functor and the projection forgetting the module, is a 2-fibre product of the
> projection `Coh_{X/Y} ⟶ 𝒮_Y` with the morphism `𝒮_{Y'} ⟶ 𝒮_Y`.

```lean
def canonicalBaseChangeSquare_isTwoFibreProduct (g : Y' ⟶ D.Y) :
    Bicategory.IsTwoFibreProduct (D.canonicalBaseChangeSquare g)
```

**`AlgebraicGeometry.Space.coherentToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackProjection.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackProjection.lean#L187). The attribute's comment: “the projection to the base”.

> **Stacks 08LP, the projection to the base.**  The rule `(T, g, ℱ) ↦ (T, g)` which forgets the
> module is a 1-morphism `Coh_{X/Y} ⟶ 𝒮_Y` of categories over the big fppf site of `S`: it lands in
> the test schemes over `Y` by construction, and the scheme it names is the one `Coh_{X/Y}` already
> projects to.

```lean
def coherentToBase (cd : CoherentCategoryData hc D) :
    coherentBasedCategory cd ⥤ᵇ baseBasedCategory D.Y
```

## Tag 08KD, a lemma

[Tag 08KD](https://stacks.math.columbia.edu/tag/08KD) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.isLimitPreserving_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackLimitFlatProperSupport.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackLimitFlatProperSupport.lean#L706). The attribute's comment: “at a small index category”.

> **Stacks 08KD.** In Situation 08KB, let `f : X ⟶ Y` be a morphism of finite presentation of
> algebraic spaces over `S` and assume `Y` locally of finite presentation over `S`. Then
> `Coh_{X/Y}` is limit preserving in the sense of Artin's Axioms, Definition 07XL: for every
> cofiltered inverse system of affine schemes `T_j` of the big fppf site, indexed by a category in
> the scheme universe, whose limit `T` in schemes lies in the site, the comparison functor
> `colim Coh_{X/Y, T_j} ⥤ Coh_{X/Y, T}` is an equivalence.
>
> The index category is taken in the scheme universe, which is the smallness the source's
> directed sets have, as in `AlgebraicGeometry.isLimitPreservingPolarizedUnconditional`.

```lean
theorem isLimitPreserving_coherent
    (hY : IsLocallyOfFinitePresentation B S hS (terminal.from D.Y.1)) :
    Deformation.Artin.IsLimitPreserving.{u, u, u} B S hS D.coherentCFG
```

## Tag 08LQ, a lemma

[Tag 08LQ](https://stacks.math.columbia.edu/tag/08LQ) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.fiberSquareComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushoutModules.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackPushoutModules.lean#L485).

> **Stacks Project, Tag 08LQ.**  In Situation 08KB, let `f : X ⟶ B` be a morphism of algebraic
> spaces over `S` of finite presentation, and let
>
> ```
>   Z ---i---> Z'
>   |          |
>   f          a
>   v          v
>   Y ---b---> Y'
> ```
>
> be a pushout in the category of schemes over `S` with `Z ⟶ Z'` a thickening and `Z ⟶ Y` affine
> (Stacks 07RT). Then the functor on fibre categories
> `Coh_{X/B, Y'} ⟶ Coh_{X/B, Y} ×_{Coh_{X/B, Z}} Coh_{X/B, Z'}` is an equivalence.
>
> Here `Coh_{X/B}` is the category of `AlgebraicGeometry.Space.CoherentSituation.categoryData`
> fibred over the schemes over `S` by `AlgebraicGeometry.Space.coherentSiteProjection`, and the
> functor is `Deformation.Artin.fiberSquareComparison` at its chosen pullbacks, for the square
> `f ≫ b = i ≫ a` of schemes over `S`, which commutes by
> `AlgebraicGeometry.Space.CoherentSituation.comm_of_isPushout_toScheme`.
>
> The proof follows the source: the map `B(Y') ⟶ B(Y) ×_{B(Z)} B(Z')` is bijective (Stacks 07SY),
> which fixes the morphism `Y' ⟶ B` (`fiberSquareComparison_isEquivalence_of_modulesGlueOver`),
> and the statement becomes Stacks 08KV for the base change `X ×_B Y' ⟶ Y'`
> (`modulesGlueOver_of_isPushout`).

```lean
theorem fiberSquareComparison_isEquivalence (D : CoherentSituation B S hS)
    {Z Z' Y Y' : BigFppfOver B S hS} (i : Z ⟶ Z') (f : Z ⟶ Y) (a : Z' ⟶ Y') (b : Y ⟶ Y')
    (hi : Stacks.Thickenings.IsThickening ((BigFppfOver.toScheme B S hS).map i))
    [AlgebraicGeometry.IsAffineHom ((BigFppfOver.toScheme B S hS).map f)]
    (hsq : IsPushout ((BigFppfOver.toScheme B S hS).map i)
      ((BigFppfOver.toScheme B S hS).map f) ((BigFppfOver.toScheme B S hS).map a)
      ((BigFppfOver.toScheme B S hS).map b)) :
    letI : Category.{u + 1} (CoherentObject D) := D.categoryData.category
    letI : (coherentSiteProjection D.categoryData).IsFibered :=
      D.isFiberedInGroupoids_siteProjection.isFibered
    (Deformation.Artin.fiberSquareComparison (coherentSiteProjection D.categoryData)
      (coherentSiteProjection D.categoryData).chosenPullbacks f i b a
        (comm_of_isPushout_toScheme hsq)).IsEquivalence
```

## Tag 08W7, a lemma

[Tag 08W7](https://stacks.math.columbia.edu/tag/08W7) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_tfae_of_isPullback_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackThickeningFinitePresentation.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackThickeningFinitePresentation.lean#L102).

> **Stacks 08W7.** Let `X ⟶ X'` over `T ⟶ T'` be a cartesian square of algebraic spaces in
> which `t : T ⟶ T'` is a first order thickening, let `ℱ'` be an `𝒪_{X'}`-module flat over `T'`
> and set `ℱ = i^*ℱ'`.  Then the following are equivalent: (1) `ℱ'` is a quasi-coherent
> `𝒪_{X'}`-module of finite presentation; (2) `ℱ'` is an `𝒪_{X'}`-module of finite presentation;
> (3) `ℱ` is a quasi-coherent `𝒪_X`-module of finite presentation; (4) `ℱ` is an `𝒪_X`-module of
> finite presentation.

```lean
theorem isFinitePresentationOnSite_tfae_of_isPullback_of_isFirstOrderThickening
    {T T' X X' : AlgebraicSpaces B S hS} (t : T ⟶ T') [Mono t.hom]
    (ht : IsFirstOrderThickening B S hS T' (Subfunctor.range t.hom))
    (i : X ⟶ X') (f : X ⟶ T) (f' : X' ⟶ T') (hsq : IsPullback i f f' t)
    (F' : Modules.{u, u} B S hS X'.1 X'.2) (hflat : IsFlatOver B S hS X'.2 f'.hom F') :
    List.TFAE
      [F'.IsQuasicoherentOnSite ∧ F'.IsFinitePresentationOnSite,
        F'.IsFinitePresentationOnSite,
        ((modulePullback B S hS i).obj F').IsQuasicoherentOnSite ∧
          ((modulePullback B S hS i).obj F').IsFinitePresentationOnSite,
        ((modulePullback B S hS i).obj F').IsFinitePresentationOnSite]
```

## Tag 08W8, a lemma

[Tag 08W8](https://stacks.math.columbia.edu/tag/08W8) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.finiteDimensional_tangentSpace_and_infinitesimalAutomorphisms_cohDef`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackInfFinite.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackInfFinite.lean#L686).

> **Stacks 08W8.** In Situation 08KB (`f : X ⟶ Y` of finite presentation) assume that `S` is
> locally Noetherian and `Y ⟶ S` locally of finite presentation. Let `k` be a field of finite type
> over `S`, with `Spec Λ ⊆ S` an affine open through which `Spec k ⟶ S` factors and `Λ → k` finite
> as in Section 07T2, and let `x₀ = (Spec k, g₀, 𝒢₀)` be an object of `Coh_{X/Y}` over `Spec k`.
> Then the tangent space `T𝓕` and the infinitesimal automorphisms `Inf(𝓕)` of
> `𝓕 = 𝓕_{Coh_{X/Y}, k, x₀}` are finite-dimensional over `k`. The vector-space structures are those
> of the deformation category `𝓕` (Stacks 07WU with Stacks 07WQ), which the conclusion records.
>
> The conclusion spells out the two clauses of `Deformation.IsFiniteDimensionalDeformationCategory`:
> that predicate asks the morphisms of `𝓕` to live in the universe of the rings of `𝒞_Λ`, while the
> morphisms of `Coh_{X/Y}`, which carry morphisms of sheaves of modules, live one universe higher.

```lean
theorem finiteDimensional_tangentSpace_and_infinitesimalAutomorphisms_cohDef
    [IsLocallyNoetherian S]
    (hlfp : IsLocallyOfFinitePresentation B S hS (terminal.from D.Y.1)) [Module.Finite Λ k]
    (hiΛ : AlgebraicGeometry.IsOpenImmersion iΛ)
    (hfinite : AlgebraicGeometry.LocallyOfFiniteType
        (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ) ∧
      AlgebraicGeometry.QuasiCompact (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    ∃ hp : IsDeformationCategory.{u, u, u} (D.cohDef iΛ x₀ hx₀).projection,
      (letI : Fact (IsPredeformationCategory.{u, u, u}
          (BasedCategory.ofFunctor (D.cohDef iΛ x₀ hx₀).projection).p) := ⟨hp.predeformation⟩;
        letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
          (isomorphismClasses (BasedCategory.ofFunctor (D.cohDef iΛ x₀ hx₀).projection)
            hp.predeformation.cofibered))) := ⟨tangentConditionS2.{u, u, u} hp⟩;
        FiniteDimensional k (tangentSpaceArtinian.{u, u, u} Λ k
          (isomorphismClasses (BasedCategory.ofFunctor (D.cohDef iΛ x₀ hx₀).projection)
            hp.predeformation.cofibered))) ∧
      ∀ (x : (D.cohDef iΛ x₀ hx₀).carrier),
        (D.cohDef iΛ x₀ hx₀).projection.obj x = Deformation.residueFieldObject.{u, u, u} Λ k →
        ∀ PF : ChosenPushforwardsAt (D.cohDef iΛ x₀ hx₀).projection x, FiniteDimensional k
          ↥((infinitesimalAutomorphismLinearLift.{u, u, u} PF hp.satisfiesRS).functor.obj
            (FGModuleCat.of k (ULift.{u} k)))
```

## Tag 08W9, a lemma

[Tag 08W9](https://stacks.math.columbia.edu/tag/08W9) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.isEquivalence_approximationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackApproximation.lean, line 942](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackApproximation.lean#L942).

> In Situation 08KB, with `f : X ⟶ Y` separated, the functor of Artin's Axioms, Equation 07X6,
> at `Coh_{X/Y}` — from objects over spectra of Noetherian complete local rings with residue field
> of finite type over `S` to formal objects — is an equivalence. No Noetherian hypothesis on `S` is
> assumed.

```lean
theorem isEquivalence_approximationFunctor (hsep : IsSeparated B S hS D.f.hom) :
    letI : Category.{u + 1} (CoherentObject D) := D.categoryData.category
    D.approximationFunctor.IsEquivalence
```

## Tag 08WA, a lemma

[Tag 08WA](https://stacks.math.columbia.edu/tag/08WA) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.hasOpenVersality_coherentCFG_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackOpenVersalityOfFlat.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackOpenVersalityOfFlat.lean#L49).

> **Openness of versality for `Coh_{X/B}`** (Stacks 08WA). In Situation Stacks 08KB assume that
> `S` is a locally Noetherian scheme, `S = B` (here: the base `Y` is final) and `f : X → B` is flat.
> Then `𝒳 = Coh_{X/B}` satisfies openness of versality (Stacks 07XQ).
>
> This is the second proof of the source, through Stacks 0CYF: the diagonal of `𝒳` is representable
> by algebraic spaces (Stacks 08W6), `𝒳` satisfies (RS*) (Stacks 08LQ) and is limit preserving
> (Stacks 08KD), and over a Noetherian affine chart `x = (Spec A, ℱ)` the tangent space is
> `T_x(M) = Ext¹_{X_A}(ℱ, ℱ ⊗ f^*M̃)`, naturally in `M`, and the obstruction class of a
> square-zero thickening `A' → A` with kernel `I` lies in `Ext²_{X_A}(ℱ, ℱ ⊗ f^*Ĩ)`, functorially
> along surjections of thickenings (Stacks 08VW, 0CYE).

```lean
theorem hasOpenVersality_coherentCFG_of_isFlat
    [_root_.AlgebraicGeometry.IsLocallyNoetherian S] (hY : IsTerminal D.Y)
    (hflat : IsFlat B S hS D.f.hom) :
    HasOpenVersality ((coherentCFG D).val.p ⋙ Over.post B.inclusion)
```

## Tag 08WC, a theorem

[Tag 08WC](https://stacks.math.columbia.edu/tag/08WC) in the Stacks Project.

**`AlgebraicGeometry.Space.CoherentSituation.isAlgebraicStack_coherentCFG_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackAlgebraicFlat.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackAlgebraicFlat.lean#L40).

> **Algebraicity of the stack of coherent sheaves, flat case.** Let `S` be a scheme and
> `f : X ⟶ B` a morphism of algebraic spaces over `S` which is of finite presentation (a field of the
> standing datum `D` of Situation 08KB), separated and flat. Then `Coh_{X/B}` is an algebraic stack
> over `S`.

```lean
theorem isAlgebraicStack_coherentCFG_of_isFlat.{w} {B : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : B.Contains S} (D : CoherentSituation B S hS) (hsep : IsSeparated B S hS D.f.hom)
    (hflat : IsFlat B S hS D.f.hom) :
    Stack.IsAlgebraicStack.{u, w} B S hS D.coherentCFG.val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.5, Tag 08KA](https://stacks.math.columbia.edu/tag/08KA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
