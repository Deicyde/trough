---
declaration: section
origin: cited
lean: AlgebraicGeometry.CurveFamily, AlgebraicGeometry.CurveFamily.Hom, AlgebraicGeometry.curvesProjection, AlgebraicGeometry.curvesToCartesianProperFlat, AlgebraicGeometry.curvesProjection_isFiberedInGroupoids, AlgebraicGeometry.curvesProjection_isStackInGroupoids, AlgebraicGeometry.C1590Private.hasRepresentableDiagonal_curvesFiberedCategory, AlgebraicGeometry.CurveFamilyOver
statement: formalized
proof: formalized
---

# 99.15 The stack of curves

Section 99.15 of the Stacks Project, [Tag 0D4Y](https://stacks.math.columbia.edu/tag/0D4Y). 14 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D4Z, a situation

[Tag 0D4Z](https://stacks.math.columbia.edu/tag/0D4Z) in the Stacks Project.

**`AlgebraicGeometry.CurveFamily`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean#L83). The attribute's comment: “objects”.

> A *family of curves*: a morphism from an algebraic space to a scheme of
> the big fppf site which is flat, proper, of finite presentation and of relative dimension at
> most one.

```lean
structure CurveFamily
```

**`AlgebraicGeometry.CurveFamily.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean#L109). The attribute's comment: “morphisms”.

> A morphism of families of curves: a morphism of total spaces over a
> morphism of base schemes whose square is cartesian.

```lean
structure Hom (X Y : CurveFamily B hZ)
```

**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean#L135). The attribute's comment: “category”.

> Families of curves and cartesian squares between them form a category,
> with componentwise identities and composition.

```lean
instance : Category (CurveFamily B hZ)
```

**`AlgebraicGeometry.curvesProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamilies.lean#L153). The attribute's comment: “projection”.

> The forgetful functor taking a family of curves to its base scheme, which makes the category
> of families of curves a category over the big fppf site.

```lean
def curvesProjection : CurveFamily B hZ ⥤ B.Schemes
```

## Tag 0D50, an equation

[Tag 0D50](https://stacks.math.columbia.edu/tag/0D50) in the Stacks Project.

**`AlgebraicGeometry.curvesToCartesianProperFlat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean#L403). The attribute's comment: “the inclusion”.

> **Stacks equation 0D50.** The inclusion of the category of families of curves into the
> category of finitely presented, flat and proper families of algebraic spaces over varying base
> schemes, forgetting the bound on the relative dimension of the structure morphism: on objects it
> is `AlgebraicGeometry.CurveFamily.toCartesianProperFlat` and on morphisms it keeps the morphism
> of total spaces and the morphism of base schemes, the cartesian square of a morphism of families
> of curves being exactly the strongly cartesian condition on the larger side.
>
> The equation displays only this inclusion. That the two sides are categories fibred in groupoids
> over the big fppf site and that the inclusion is one of categories over that site is the ambient
> Situation 99.15.1 of the source, realised here by
> `AlgebraicGeometry.curvesProjection_isFiberedInGroupoids`,
> `AlgebraicGeometry.cartesianProperFlatProjection_isFiberedInGroupoids` and
> `AlgebraicGeometry.curvesToCartesianProperFlat_comp_cartesianProperFlatProjection`; that the
> inclusion is one of a full subcategory is
> `AlgebraicGeometry.curvesToCartesianProperFlat_full` together with
> `AlgebraicGeometry.curvesToCartesianProperFlat_faithful`.

```lean
def curvesToCartesianProperFlat :
    CurveFamily B hZ ⥤ CartesianProperFlatSpaces B integerBase hZ
```

## Tag 0D51, a lemma

[Tag 0D51](https://stacks.math.columbia.edu/tag/0D51) in the Stacks Project.

**`AlgebraicGeometry.curvesProjection_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean#L182).

> **Stacks 0D51.** The category of families of curves is fibred in groupoids over the big fppf
> site of schemes.

```lean
theorem curvesProjection_isFiberedInGroupoids :
    (curvesProjection B hZ).IsFiberedInGroupoids
```

## Tag 0D52, a lemma

[Tag 0D52](https://stacks.math.columbia.edu/tag/0D52) in the Stacks Project.

**`AlgebraicGeometry.curvesProjection_isStackInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesStack.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesStack.lean#L262).

> **Stacks 0D52.** The category of families of curves is a stack in groupoids over the big fppf
> site of schemes, for covering families indexed in every universe.
>
> It is a stack (`AlgebraicGeometry.curvesProjection_isStack`) whose projection is fibred in
> groupoids (Stacks 0D51, `AlgebraicGeometry.curvesProjection_isFiberedInGroupoids`), and such a
> stack is a stack in groupoids by the implication (3) ⟹ (1) of Stacks 02ZJ.

```lean
theorem curvesProjection_isStackInGroupoids :
    (curvesProjection B hZ).IsStackInGroupoids.{w} B.topology
```

## Tag 0D53, a lemma

[Tag 0D53](https://stacks.math.columbia.edu/tag/0D53) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.C1590Private.hasRepresentableDiagonal_curvesFiberedCategory`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/C1590Private/CurvesDiagonal.lean#L77), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/CurvesAlgebraicStackUnconditional.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesAlgebraicStackUnconditional.lean#L42) (StacksFrontier).

## Tag 0D54, a remark

[Tag 0D54](https://stacks.math.columbia.edu/tag/0D54) in the Stacks Project.

**`AlgebraicGeometry.CurveFamilyOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesOverSpace.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesOverSpace.lean#L95). The attribute's comment: “the category of families of curves over a base algebraic space”.

> **Stacks 0D54.** The category of families of curves over a fixed algebraic space `A`: an object
> is a family of curves together with a morphism from its base scheme to `A`, and a morphism is a
> morphism of families of curves commuting with those morphisms.

```lean
abbrev CurveFamilyOver (A : AlgebraicSpaces B integerBase hZ)
```

**`AlgebraicGeometry.CurveFamilyOver.isEquivalence_toTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesOverSpace.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesOverSpace.lean#L179). The attribute's comment: “the base-change square”.

> **Stacks 0D54.** The absolute and the relative categories of curves form a 2-fibre product
> square over the big fppf site of schemes: the canonical comparison from families of curves over `A`
> to the 2-fibre product of families of curves with the schemes over `A` is an equivalence.

```lean
theorem isEquivalence_toTwoFibreProduct (A : AlgebraicSpaces B integerBase hZ) :
    (toTwoFibreProduct B hZ A).IsEquivalence
```

## Tag 0D55, a lemma

[Tag 0D55](https://stacks.math.columbia.edu/tag/0D55) in the Stacks Project.

**`AlgebraicGeometry.isLimitPreserving_curvesFiberedCategory_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLimitPreservingUnconditional.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLimitPreservingUnconditional.lean#L51). The attribute's comment: “at a small index category”.

> **Stacks 0D55.** The stack of families of curves over the big fppf site of `Spec(ℤ)` is limit
> preserving in the sense of Artin's Axioms, Definition 07XL: for every inverse system of affine
> schemes of the site whose limit of underlying schemes is `T`, the canonical comparison
> `colim Curves_{Tᵢ} ⥤ Curves_T` is an equivalence of categories. The index category is taken in
> the universe of the schemes.

```lean
theorem isLimitPreserving_curvesFiberedCategory_unconditional :
    Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u + 1} B integerBase hZ
      (curvesFiberedCategory B hZ)
```

## Tag 0D56, a lemma

[Tag 0D56](https://stacks.math.columbia.edu/tag/0D56) in the Stacks Project.

**`AlgebraicGeometry.curvePushoutEquivalenceOfIsPushout`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ProperPushoutGluingUnconditional.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ProperPushoutGluingUnconditional.lean#L58).

> **[Stacks Project, Tag 0D56].** For a pushout `S' = S ⨿_T T'` of schemes along a
> thickening `i : T ⟶ T'` and an affine morphism `f : T ⟶ S`, the canonical restriction functor
> from the families of curves over `S'` to the compatible pairs of families over `S` and `T'` is
> an equivalence.

```lean
def curvePushoutEquivalenceOfIsPushout {T T' S S' : B.Schemes}
    (i : T ⟶ T') (f : T ⟶ S) (g : T' ⟶ S') (h : S ⟶ S')
    (hi : Stacks.Thickenings.IsThickening (B.inclusion.map i))
    [IsAffineHom (B.inclusion.map f)]
    (hsq : IsPushout (B.inclusion.map i) (B.inclusion.map f)
      (B.inclusion.map g) (B.inclusion.map h)) :
    CurvePushoutEquivalenceData B hZ i f g h
```

## Tag 0D57, a lemma

[Tag 0D57](https://stacks.math.columbia.edu/tag/0D57) in the Stacks Project.

**`AlgebraicGeometry.CurveDeformation.finiteDimensional_predeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveDeformationsFiniteDimensional.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveDeformationsFiniteDimensional.lean#L68). The attribute's comment: “(1): for a family of curves x over any field k and any Λ with Spec k → Spec Λ, the predeformation category F_{X,k,x} is a deformation category whose tangent space T F and infinitesimal automorphisms Inf(F) are finite dimensional; k need not be of finite type over Z”.

> **Stacks Project, Tag 0D57, part (1).** Let `k` be a field and let `x = (X → Spec k)` be a
> family of curves over `Spec k`, lying over `Spec k → Spec Λ → Spec ℤ`. Then the predeformation
> category `𝓕_{𝒳,k,x}` over `𝒞_Λ` is a deformation category, its tangent space `T𝓕_{𝒳,k,x}` is a
> finite-dimensional `k`-vector space, and so are its infinitesimal automorphisms
> `Inf(𝓕_{𝒳,k,x})`, the kernel of `Aut_{k[ε]}(x'₀) → Aut_k(x₀)`, at every object of the special
> fibre and for every choice of its pushforwards.
>
> This generalizes the source: `k` need not be of finite type over `ℤ`, and `Λ` is any ring with
> a `Λ`-algebra structure on `k` and any morphism `Spec Λ ⟶ Spec ℤ`. The proof identifies
> `𝓕_{𝒳,k,x}` with the deformation category of the scheme `X` (the total space of a curve over a
> field is a scheme, Stacks 0ADD) and applies the finiteness of Stacks 0DYA for that category, in
> place of the source's appeal to Stacks 0D1K.

```lean
theorem finiteDimensional_predeformation :
    letI := (predeformation x hx).category
    ∃ hD : IsDeformationCategory.{u, u, u} (predeformation x hx).projection,
      (letI : Fact (IsPredeformationCategory
          (BasedCategory.ofFunctor (predeformation x hx).projection).p) := ⟨hD.predeformation⟩;
        letI : Fact (SchlessingerConditionS2 (CategoryOfElements.π
          (isomorphismClasses (BasedCategory.ofFunctor (predeformation x hx).projection)
            hD.predeformation.cofibered))) := ⟨tangentConditionS2.{u, u, u} hD⟩;
        FiniteDimensional k (artinianTangentSpace Λ k
          (isomorphismClasses (BasedCategory.ofFunctor (predeformation x hx).projection)
            hD.predeformation.cofibered))) ∧
      ∀ y, (predeformation x hx).projection.obj y = residueFieldObject.{u, u, u} Λ k →
        ∀ PF : ChosenPushforwardsAt (predeformation x hx).projection y,
          FiniteDimensional k ↥((infinitesimalAutomorphismLinearLift.{u, u, u} PF
            hD.satisfiesRS).functor.obj (FGModuleCat.of k (ULift.{u} k)))
```

**`AlgebraicGeometry.finiteDimensional_curves_tangentFunctor_infinitesimalAutomorphismFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveTangentFunctor.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveTangentFunctor.lean#L68). The attribute's comment: “(2): for a family of curves x over a field k, the tangent functor T_x and the functor Inf_x of Stacks 07Y9 exist, and T_x(k) and Inf_x(k) are finite dimensional; both are stated for every k-linear functor carrying the identifications of 07Y9”.

> Let `k` be a field and let `x = (X → Spec k)` be a family of curves over `Spec k`. Then the
> tangent functor `T_x` and the functor of infinitesimal automorphisms `Inf_x` of Stacks 07Y9 exist,
> and `T_x(k)` and `Inf_x(k)` are finite-dimensional `k`-vector spaces.
>
> Each functor is stated as a structure (`TangentFunctorData`,
> `InfinitesimalAutomorphismFunctorData`) carrying a `k`-linear functor on the site modules together
> with its identification with the isomorphism classes of lifts of `x`, respectively with the
> infinitesimal automorphisms of the trivial lifts of `x`, natural in the module. The statement
> gives that such a functor exists and that the value at `k` of *every* such functor is
> finite-dimensional, so it holds for the functors `T_x` and `Inf_x` of Stacks 07Y9, which are
> determined by these identifications. No condition on `k` is assumed.

```lean
theorem finiteDimensional_curves_tangentFunctor_infinitesimalAutomorphismFunctor {k : Type u}
    [Field k] {toS : Spec (.of k) ⟶ integerBase} {hk : B.Contains (Spec (.of k))}
    (x : CurveFamily B hZ)
    (hx : (curvesProjectionOver B hZ).obj x = algebraOver k B integerBase hZ toS hk) :
    (Nonempty (TangentFunctorData k B integerBase hZ toS hk (curvesProjectionOver B hZ) x hx) ∧
      ∀ T : TangentFunctorData k B integerBase hZ toS hk (curvesProjectionOver B hZ) x hx,
        FiniteDimensional k (T.functor.obj ((fgSiteModule B hk).obj (FGModuleCat.of k k)))) ∧
    (Nonempty (InfinitesimalAutomorphismFunctorData k B integerBase hZ toS hk
        (curvesProjectionOver B hZ) x hx
        CurveDeformation.curvesProjectionOver_isFiberedInGroupoids) ∧
      ∀ I : InfinitesimalAutomorphismFunctorData k B integerBase hZ toS hk
          (curvesProjectionOver B hZ) x hx
          CurveDeformation.curvesProjectionOver_isFiberedInGroupoids,
        FiniteDimensional k (I.functor.obj ((fgSiteModule B hk).obj (FGModuleCat.of k k))))
```

## Tag 0D58, a lemma

[Tag 0D58](https://stacks.math.columbia.edu/tag/0D58) in the Stacks Project.

**`AlgebraicGeometry.curvesFormalObject_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesFormalEffectiveUnconditional.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesFormalEffectiveUnconditional.lean#L54).

> Every formal object of the stack `Curves` of families of curves over `Spec(ℤ)` is effective:
> it comes, up to isomorphism of formal objects, from a family of curves over the spectrum of its
> Noetherian complete local base.

```lean
theorem curvesFormalObject_isEffective (B : BigFppfSite.{u}) (hZ : B.Contains integerBase)
    (ξ : Deformation.Artin.FormalObject B integerBase hZ (curvesProjectionOver B hZ)) :
    Deformation.Artin.FormalObject.IsEffective B integerBase hZ (curvesProjectionOver B hZ)
      (Functor.IsFiberedInGroupoids.of_comp_over (B.obj hZ) (curvesProjection B hZ)
        (curvesProjectionOver B hZ) (by rfl) (curvesProjection_isFiberedInGroupoids B hZ)) ξ
```

## Tag 0D59, a lemma

[Tag 0D59](https://stacks.math.columbia.edu/tag/0D59) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.curves_openVersalityOf_specZ`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ProperFlatOpennessOfVersalityOfDiagonal.lean#L117), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/CurvesOpennessOfVersalityTags.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesOpennessOfVersalityTags.lean#L28) (StacksFrontier): “the first assertion: the stack of curves satisfies openness of versality over `Spec(ℤ)`”.
- [`AlgebraicGeometry.curves_openVersalityOf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/ProperFlatOpennessOfVersalityOfDiagonal.lean#L124), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/CurvesOpennessOfVersalityTags.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesOpennessOfVersalityTags.lean#L32) (StacksFrontier): “the second assertion: for a Noetherian scheme `S` of the site, the stack of `S`-curves -- the base change of Remark 0D54 -- satisfies openness of versality over `S`”.

## Tag 0D5A, a theorem

[Tag 0D5A](https://stacks.math.columbia.edu/tag/0D5A) in the Stacks Project.

**`AlgebraicGeometry.isAlgebraicStack_curvesStack_and_curveFamilyOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesAlgebraicStackUnconditional.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesAlgebraicStackUnconditional.lean#L47).

> The stack `Curves` (Situation 0D4Z) is algebraic. In fact, for every algebraic space `A` the
> stack `A-Curves` of families of curves over `A` (Remark 0D54) is algebraic.

```lean
theorem isAlgebraicStack_curvesStack_and_curveFamilyOver :
    Stack.IsAlgebraicStack.{u, u + 1, u + 1, u + 1} B integerBase hZ
        (curvesFiberedCategory B hZ).val ∧
      ∀ A : AlgebraicSpaces B integerBase hZ,
        Stack.IsAlgebraicStack.{u, u + 1} B integerBase hZ (curveFamilyOverBased B hZ A)
```

## Tag 0D5B, a lemma

[Tag 0D5B](https://stacks.math.columbia.edu/tag/0D5B) in the Stacks Project.

**`AlgebraicGeometry.isRepresentableByAlgebraicSpaces_curvesToCartesianProperFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean, line 1153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean#L1153). The attribute's comment: “representability by algebraic spaces”.

> **Stacks 0D5B.** The 1-morphism from the category of families of curves to the category of
> finitely presented, flat and proper families of algebraic spaces of Stacks equation 0D50 is
> representable by algebraic spaces.

```lean
theorem isRepresentableByAlgebraicSpaces_curvesToCartesianProperFlat :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
      (curvesToCartesianProperFlatHom B hZ).hom
```

**`AlgebraicGeometry.isOpenImmersion_curvesToCartesianProperFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean, line 1194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean#L1194). The attribute's comment: “open immersions”.

> **Stacks 0D5B.** The 1-morphism from the category of families of curves to the category of
> finitely presented, flat and proper families of algebraic spaces of Stacks equation 0D50 is an
> open immersion: every algebraic space representing one of its base changes has open immersion
> structural morphism.

```lean
theorem isOpenImmersion_curvesToCartesianProperFlat :
    Stack.IsOpenImmersion B integerBase hZ (curvesToCartesianProperFlatHom B hZ)
```

**`AlgebraicGeometry.isClosedImmersion_curvesToCartesianProperFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean, line 1205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurveFamiliesFibered.lean#L1205). The attribute's comment: “closed immersions”.

> **Stacks 0D5B.** The 1-morphism from the category of families of curves to the category of
> finitely presented, flat and proper families of algebraic spaces of Stacks equation 0D50 is a
> closed immersion: every algebraic space representing one of its base changes has closed immersion
> structural morphism.

```lean
theorem isClosedImmersion_curvesToCartesianProperFlat :
    Stack.IsClosedImmersion B integerBase hZ (curvesToCartesianProperFlatHom B hZ)
```

## Tag 0D5C, a remark

[Tag 0D5C](https://stacks.math.columbia.edu/tag/0D5C) in the Stacks Project.

**`AlgebraicGeometry.polarizedCurvesToCurves_isAlgebraic_smooth_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/C1783/PolarizedCurvesRemark.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/C1783/PolarizedCurvesRemark.lean#L176).

> **Stacks 0D5C.** Let `PolarizedCurves = 𝒞urves ×_{𝒮paces'_{fp, flat, proper}} 𝒫olarized`
> (`AlgebraicGeometry.polarizedCurvesUnconditional`), over the big fppf site of `Spec ℤ`.
>
> 1. PolarizedCurves parametrizes polarized curves: its first projection is an equivalence onto the
>    category of polarized families of relative dimension at most one, i.e. of families of curves
>    endowed with a relatively ample invertible sheaf.
> 2. PolarizedCurves is an open and closed substack of the algebraic stack `𝒫olarized`: `𝒫olarized`
>    is an algebraic stack, the projection `PolarizedCurves ⟶ 𝒫olarized` is representable by
>    algebraic spaces, an open immersion and a closed immersion, and PolarizedCurves is an algebraic
>    stack.
> 3. `PolarizedCurves ⟶ 𝒞urves` is a base change of the arrow `𝒫olarized ⟶ 𝒮paces'_{fp,flat,proper}`
>    of Stacks 0D41: its base change along every scheme point `z` of `𝒞urves` is equivalent over the
>    site to the base change of the forgetful 1-morphism of Stacks 0D41 along the image of `z` in
>    `𝒮paces'_{fp, flat, proper}`.
> 4. `PolarizedCurves ⟶ 𝒞urves` is algebraic (Stacks 06CF): its base change along every scheme point
>    of `𝒞urves` is an algebraic stack.
> 5. `PolarizedCurves ⟶ 𝒞urves` is smooth: each of these base changes is smooth over the scheme
>    (Stacks 075U).
> 6. `PolarizedCurves ⟶ 𝒞urves` is surjective: every point of `𝒞urves` is in the image
>    (surjectivity on objects, Stacks 06D4), and the 1-morphism of algebraic stacks is surjective on
>    points (Stacks 04ZS).
> 7. Another approach to the algebraicity of `𝒞urves`: `𝒞urves` is an algebraic stack, as the
>    target of the smooth, surjective, algebraic 1-morphism `PolarizedCurves ⟶ 𝒞urves` from the
>    algebraic stack PolarizedCurves.
>
> Clauses 4–6 are stated for the hom-shrunk models `AlgebraicGeometry.polarizedCurvesSmall` and
> `AlgebraicGeometry.curvesSmall`, equivalent over the site to PolarizedCurves and `𝒞urves`, with
> the projection `AlgebraicGeometry.polarizedCurvesSmallToCurvesSmall`; surjectivity on objects in
> clause 6 is also stated for PolarizedCurves itself.

```lean
theorem polarizedCurvesToCurves_isAlgebraic_smooth_surjective :
    -- (1) PolarizedCurves parametrizes polarized curves
    (polarizedCurvesToIsPolarizedCurve B hZ).IsEquivalence ∧
    -- (2) PolarizedCurves is an open and closed substack of the algebraic stack `𝒫olarized`
    (Stack.IsAlgebraicStack.{u, w} B integerBase hZ (polarizedFiberedCategory B hZ
        (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B)).val ∧
      Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (polarizedCurvesToPolarizedUnconditional B hZ).hom ∧
      Stack.IsOpenImmersion B integerBase hZ (polarizedCurvesToPolarizedUnconditional B hZ) ∧
      Stack.IsClosedImmersion B integerBase hZ (polarizedCurvesToPolarizedUnconditional B hZ) ∧
      Stack.IsAlgebraicStack.{u, w} B integerBase hZ (polarizedCurvesUnconditional B hZ).val) ∧
    -- (3) `PolarizedCurves ⟶ 𝒞urves` is a base change of the arrow of Stacks 0D41
    (∀ (Z : BigFppfOver B integerBase hZ)
      (z : BigFppfOver B Z.left.1 Z.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj),
      z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map Z.hom →
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (TwoFibreProductOver.structureFunctor (Over.map Z.hom)
          (polarizedProjection B ⋙ schemeOverIntegers B)
          (cartesianProperFlatProjection B integerBase hZ)
          (z ⋙ curvesToCartesianProperFlat B hZ) (forgetPolarization B))
        (TwoFibreProductOver.structureFunctor (Over.map Z.hom)
          (polarizedCurvesUnconditional B hZ).val.p (curvesFiberedCategory B hZ).val.p z
          (CatFiberedInGroupoids.homFunctor (polarizedCurvesSquare B hZ
            (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B)).snd)))) ∧
    -- (4) `PolarizedCurves ⟶ 𝒞urves` is algebraic
    (∀ (Z : BigFppfOver B integerBase hZ)
      (z : BigFppfOver B Z.left.1 Z.left.2 ⥤ (curvesSmall B hZ).val.obj)
      (hz : z ⋙ (curvesSmall B hZ).val.p = Over.map Z.hom),
      Stack.IsAlgebraicStack.{u, w} B integerBase hZ
        (CatFiberedInGroupoids.twoFibreProductSquare.{u, u, u + 1, u + 1}
          (Stack.schemeSliceMap B integerBase hZ Z z hz)
          (polarizedCurvesSmallToCurvesSmall B hZ
            (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B))).pt.val) ∧
    -- (5) `PolarizedCurves ⟶ 𝒞urves` is smooth
    (∀ (Z : BigFppfOver B integerBase hZ)
      (z : BigFppfOver B Z.left.1 Z.left.2 ⥤ (curvesSmall B hZ).val.obj)
      (hz : z ⋙ (curvesSmall B hZ).val.p = Over.map Z.hom),
      Stack.HasPropertyOnSomeSmoothDiagram B integerBase hZ
        (fun _ _ h => Space.IsSmooth B integerBase hZ h)
        (CatFiberedInGroupoids.twoFibreProductSquare.{u, u, u + 1, u + 1}
          (Stack.schemeSliceMap B integerBase hZ Z z hz)
          (polarizedCurvesSmallToCurvesSmall B hZ
            (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B))).fst) ∧
    -- (6) `PolarizedCurves ⟶ 𝒞urves` is surjective
    (Stack.IsSurjectiveOnObjects B integerBase hZ
        (polarizedCurvesUnconditional B hZ).val.p (curvesFiberedCategory B hZ).val.p
        (CatFiberedInGroupoids.homFunctor (polarizedCurvesSquare B hZ
          (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B)).snd) ∧
      Stack.IsSurjectiveOnObjects B integerBase hZ
        (polarizedCurvesSmall B hZ
          (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B)).val.p
        (curvesSmall B hZ).val.p
        (CatFiberedInGroupoids.homFunctor (polarizedCurvesSmallToCurvesSmall B hZ
          (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B))) ∧
      ∃ (hX : Stack.IsAlgebraicStack.{u, w} B integerBase hZ
          (polarizedCurvesUnconditional B hZ).val)
        (hY : Stack.IsAlgebraicStack.{u, w} B integerBase hZ (curvesFiberedCategory B hZ).val),
        Stack.IsSurjective B integerBase hZ (polarizedCurvesToCurvesAlgebraic B hZ
          (polarizedProjection_comp_schemeOverIntegers_isFiberedInGroupoids B) hX hY)) ∧
    -- (7) `𝒞urves` is an algebraic stack
    Stack.IsAlgebraicStack.{u, w} B integerBase hZ (curvesFiberedCategory B hZ).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.15, Tag 0D4Y](https://stacks.math.columbia.edu/tag/0D4Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
