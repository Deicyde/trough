---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.IsConstant, AlgebraicGeometry.isClosed_singleton_of_range_eq_singleton, AlgebraicGeometry.NonsingularProjectiveModel.existsUnique_iso, AlgebraicGeometry.exists_forall_not_smooth_nonsingularProjectiveModel, AlgebraicGeometry.exists_open_extension_of_valuationRing_stalk, AlgebraicGeometry.toRationalMap_bijective, AlgebraicGeometry.isFlat_of_nonconstant_of_isNormal, AlgebraicGeometry.isFinite_of_isProper_dimension_le_one_of_nontrivial_image_components
statement: formalized
proof: formalized
---

# 53.2 Curves and function fields

Section 53.2 of the Stacks Project, [Tag 0BXX](https://stacks.math.columbia.edu/tag/0BXX). 10 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BXX, the section

[Tag 0BXX](https://stacks.math.columbia.edu/tag/0BXX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.IsConstant`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/ConstantMorphism.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/ConstantMorphism.lean#L49). The attribute's comment: “a morphism of varieties is constant if its image consists of a single point”.

> **A constant morphism** (Section 0BXX): a morphism `f : X ⟶ Y` whose image `f(X)` consists of
> a single point of `Y`.

```lean
def Scheme.Hom.IsConstant {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.isClosed_singleton_of_range_eq_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/ConstantMorphism.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/ConstantMorphism.lean#L57). The attribute's comment: “if a morphism of varieties is constant, with image the point y, then y is a closed point”.

> **The image of a constant morphism of varieties is a closed point** (Section 0BXX). Let
> `f : X ⟶ Y` be a morphism of varieties over a field `k` whose image is the single point `y`.
> Then `y` is a closed point of `Y`: the image of a closed point of `X` is a closed point of `Y`.

```lean
theorem isClosed_singleton_of_range_eq_singleton (k : Type u) [Field k] {X Y : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) (sY : Y ⟶ Spec (.of k)) [IsVariety k sX] [IsVariety k sY]
    (f : X ⟶ Y) (hf : f ≫ sY = sX) {y : Y} (hy : Set.range f.base = {y}) :
    IsClosed ({y} : Set Y)
```

**`AlgebraicGeometry.NonsingularProjectiveModel.existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L144). The attribute's comment: “a nonsingular projective model is determined up to unique isomorphism, by Theorem 0BY1”.

> **The nonsingular projective model is unique up to unique isomorphism** (Section 0BXX). For two
> nonsingular projective models `(Y₁, φ₁)` and `(Y₂, φ₂)` of a curve `X` over `k`, there is exactly
> one isomorphism `e : Y₁ ≅ Y₂` over `k` whose map of function fields `k(Y₂) ⟶ k(Y₁)` carries
> `φ₂` to `φ₁`.

```lean
theorem NonsingularProjectiveModel.existsUnique_iso (M₁ M₂ : NonsingularProjectiveModel k X sX) :
    letI : IsCurve k M₁.structureMap := M₁.isCurve
    letI : IsCurve k M₂.structureMap := M₂.isCurve
    ∃! e : M₁.Y ≅ M₂.Y, e.hom ≫ M₂.structureMap = M₁.structureMap ∧
      ∀ a : X.functionField,
        functionFieldMap e.hom (M₂.functionFieldRingEquiv a) = M₁.functionFieldRingEquiv a
```

**`AlgebraicGeometry.exists_forall_not_smooth_nonsingularProjectiveModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L314). The attribute's comment: “the warning after Definition 0BY2, its first half: the nonsingular projective model of a curve need not be smooth over k”.

> **The nonsingular projective model need not be smooth** (the warning after Definition 0BY2,
> Section 0BXX). There is a curve `X` over a field `k` which has a nonsingular projective model, and
> no nonsingular projective model of `X` is smooth over `k`.
>
> Here `k = 𝔽₂(t)` and `X` is the nonsingular projective model `Y` of the affine line over
> `𝔽₂(√t)`, which is its own model. The affine line is an open subscheme of `Y`, and it is not smooth
> over `k`, because `𝔽₂(√t)/𝔽₂(t)` is not separable; so `Y` is not smooth over `k`, and neither is
> any other model, all models being isomorphic over `k`.

```lean
theorem exists_forall_not_smooth_nonsingularProjectiveModel :
    ∃ (k : Type u) (_ : Field k) (X : Scheme.{u}) (sX : X ⟶ Spec (.of k)) (_ : IsCurve k sX),
      Nonempty (NonsingularProjectiveModel k X sX) ∧
        ∀ M : NonsingularProjectiveModel k X sX, ¬ Smooth M.structureMap
```

Declarations registered for the tag:

- [`AlgebraicGeometry.exists_open_extension_of_valuationRing_stalk`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/Extension.lean#L209), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L104) (StacksFrontier): “Lemma 0BXY of the section: a morphism from a nonempty open of a curve to a proper variety extends across a closed point whose local ring is a discrete valuation ring”.
- [`AlgebraicGeometry.toRationalMap_bijective`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/RationalMapExtension.lean#L165), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L108) (StacksFrontier): “Lemma 0BXZ of the section: rational maps from a normal curve to a proper variety are morphisms”.
- [`AlgebraicGeometry.isFlat_of_nonconstant_of_isNormal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FlatMorphism.lean#L59), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L111) (StacksFrontier): “Lemma 0CCK of the section: a nonconstant morphism of curves with normal target is flat”.
- [`AlgebraicGeometry.isFinite_of_isProper_dimension_le_one_of_nontrivial_image_components`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/Basic.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L114) (StacksFrontier): “Lemma 0CCL of the section: a morphism from a proper scheme of dimension at most one which is nonconstant on every one-dimensional component is finite”.
- [`AlgebraicGeometry.isIso_globalSections_of_smooth_model_reducedBaseChange`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ModelGlobalSections.lean#L212), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L118) (StacksFrontier): “Lemma 0BY4 of the section, part (3): a smooth nonsingular projective model of a reduced base change has the base field as global regular functions”.
- [`AlgebraicGeometry.curveEquivalenceFinitelyGeneratedFieldExtensionTrdegOneOpposite`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L270), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L122) (StacksFrontier): “the main theorem of the section, Theorem 0BY1: the category of curves and dominant rational maps is anti-equivalent to that of finitely generated field extensions of transcendence degree one”.
- [`AlgebraicGeometry.normalProjectiveCurveEquivalenceCurve`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L722), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L127) (StacksFrontier): “the main theorem of the section, Theorem 0BY1: normal projective curves and nonconstant morphisms are equivalent to curves and dominant rational maps”.
- [`AlgebraicGeometry.NonsingularProjectiveModel`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModel.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L131) (StacksFrontier): “Definition 0BY2 of the section: a nonsingular projective model of a curve”.
- [`AlgebraicGeometry.NonsingularProjectiveModel.isSmoothProjectiveCurve`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/SmoothModelOverPerfectField.lean#L91), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModelUnique.lean#L134) (StacksFrontier): “the warning after Definition 0BY2, its second half: a nonsingular projective model fails to be smooth only over an imperfect field, hence only in positive characteristic (Lemma 0BY3)”.

## Tag 0BXY, a lemma

[Tag 0BXY](https://stacks.math.columbia.edu/tag/0BXY) in the Stacks Project.

**`AlgebraicGeometry.exists_open_extension_of_valuationRing_stalk`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/Extension.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Valuative/Extension.lean#L209). The attribute's comment: “the case of a curve over a field with proper target, where the stalk is a”.

> **Stacks Project, Tag 0BX7.** A morphism from an open subscheme extends across a point
> whose local ring is a valuation ring, provided the target is proper over the base and the
> source is either reduced with finitely many irreducible components or Noetherian.

```lean
lemma exists_open_extension_of_valuationRing_stalk
    {S X Y : Scheme.{u}} (pX : X ⟶ S) (pY : Y ⟶ S)
    (x : X) (U : X.Opens) (f : (U : Scheme.{u}) ⟶ Y)
    (hf : f ≫ pY = U.ι ≫ pX)
    (hxU : x ∈ closure (U : Set X))
    (hX : (IsReduced X ∧ (irreducibleComponents X).Finite) ∨
      IsNoetherian X)
    [IsDomain (X.presheaf.stalk x)] [ValuationRing (X.presheaf.stalk x)]
    [IsProper pY] :
    ∃ (U' : X.Opens) (hUU' : U ≤ U') (_ : x ∈ U')
      (f' : (U' : Scheme.{u}) ⟶ Y),
      f' ≫ pY = U'.ι ≫ pX ∧ X.homOfLE hUU' ≫ f' = f
```

## Tag 0BXZ, a lemma

[Tag 0BXZ](https://stacks.math.columbia.edu/tag/0BXZ) in the Stacks Project.

**`AlgebraicGeometry.toRationalMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/RationalMapExtension.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/RationalMapExtension.lean#L165). References: EGA II (7.4.9).

> **Stacks Project, Tag 0BXZ.** Morphisms from a normal curve to a proper variety are in
> canonical bijection with the rational maps over the base field.

```lean
theorem toRationalMap_bijective
    (k : Type u) [Field k] (X Y : Over (Spec (.of k)))
    [IsCurve k X.hom] [IsNormal X.left] [IsProperVariety k Y.hom] :
    Function.Bijective
      (fun f : X ⟶ Y ↦
        (⟨f.left.toRationalMap, inferInstance⟩ :
          {g : Scheme.RationalMap X.left Y.left // g.IsOver (Spec (.of k))}))
```

## Tag 0CCK, a lemma

[Tag 0CCK](https://stacks.math.columbia.edu/tag/0CCK) in the Stacks Project.

**`AlgebraicGeometry.isFlat_of_nonconstant_of_isNormal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FlatMorphism.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FlatMorphism.lean#L59).

> **Stacks Project, Tag 0CCK.** A nonconstant morphism of curves over a field is flat if the
> target curve is normal.

```lean
lemma isFlat_of_nonconstant_of_isNormal
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) (pY : Y ⟶ Spec (.of k))
    [IsCurve k pX] [IsCurve k pY]
    (f : X ⟶ Y) (_hf : f ≫ pY = pX) (hnonconstant : (Set.range f).Nontrivial)
    [IsNormal Y] :
    IsFlat f.toLRSHom.toShHom
```

## Tag 0CCL, a lemma

[Tag 0CCL](https://stacks.math.columbia.edu/tag/0CCL) in the Stacks Project.

**`AlgebraicGeometry.isFinite_of_isProper_dimension_le_one_of_nontrivial_image_components`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/Basic.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/CurvesFunctionFields/Basic.lean#L85).

> A morphism from a proper scheme of dimension at most one to a separated scheme over a
> field is finite if the image of every one-dimensional irreducible component contains at least
> two points.

```lean
lemma isFinite_of_isProper_dimension_le_one_of_nontrivial_image_components
    {k : Type u} [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (.of k)) [IsProper pX]
    (pY : Y ⟶ Spec (.of k)) [IsSeparated pY]
    (f : X ⟶ Y) (hf : f ≫ pY = pX)
    (hX : topologicalKrullDim X ≤ 1)
    (hcomponents : ∀ Z : irreducibleComponents X,
      topologicalKrullDim (Z : Set X) = 1 → (f '' (Z : Set X)).Nontrivial) :
    IsFinite f
```

## Tag 0BY0, a lemma

[Tag 0BY0](https://stacks.math.columbia.edu/tag/0BY0) in the Stacks Project.

**`AlgebraicGeometry.exists_isOpenImmersion_isCurve_isProjectiveMorphism_factorization_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Curve/ProjectiveCurveFactorizationUnconditional.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/Curve/ProjectiveCurveFactorizationUnconditional.lean#L74). The attribute's comment: “the full statement with nothing assumed. Both clauses are proved of the scheme constructed: `j` is an open immersion and `q` makes `Xbar` a curve (Tag 0A23) which is H-projective over `k` (Tag 01W8). The factorization `j ≫ G = g` is part of the conclusion, together with `j ≫ q = pX` and `G ≫ pY = q`, so both halves are morphisms of `k`-schemes. Tag 09NZ is not assumed: a curve is integral, hence reduced, and the library's Tag 0BXW, `Stacks.CurveProjectiveCompletion.exists_projective_completion_discreteValuation_of_isReduced`, carries nothing for a reduced source”.

> **[Stacks, Tag 0BY0].** Let `k` be a field, let `X` be a curve over `k` and `Y` a proper
> variety over `k`, and let `g : X ⟶ Y` be a morphism over `k`. Then there is a factorization
> `X ⟶ X̄ ⟶ Y` of `g` in which `X ⟶ X̄` is an open immersion and `X̄` is a projective curve over
> `k`, that is, a curve whose structure morphism is H-projective.

```lean
theorem exists_isOpenImmersion_isCurve_isProjectiveMorphism_factorization_of_isCurve
    (k : Type u) [Field k] {X Y : Scheme.{u}}
    (pX : X ⟶ Spec (CommRingCat.of k)) (pY : Y ⟶ Spec (CommRingCat.of k))
    [IsCurve k pX] [IsProperVariety k pY] (g : X ⟶ Y) (hg : g ≫ pY = pX) :
    ∃ (Xbar : Scheme.{u}) (q : Xbar ⟶ Spec (CommRingCat.of k)) (j : X ⟶ Xbar) (G : Xbar ⟶ Y),
      IsOpenImmersion j ∧ IsCurve k q ∧ IsProjectiveMorphism q ∧
        j ≫ q = pX ∧ G ≫ pY = q ∧ j ≫ G = g
```

## Tag 0BY1, a theorem

[Tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1) in the Stacks Project.

**`AlgebraicGeometry.curveEquivalenceFinitelyGeneratedFieldExtensionTrdegOneOpposite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L270). The attribute's comment: “the equivalence of categories (1) and (2), as the anti-equivalence of Tag 0BXN restricted to transcendence degree one”.

> **Stacks Project, Tag 0BY1, categories (1) and (2).** Over a field `k`, the category of
> curves over `k` and dominant rational maps is anti-equivalent to the category of finitely
> generated field extensions of `k` of transcendence degree one.
>
> This is the restriction of the anti-equivalence of Stacks 0BXN,
> `AlgebraicGeometry.varietyEquivalenceFinitelyGeneratedFieldExtensionOpposite`, to the varieties
> whose function field has transcendence degree one; those are exactly the curves, by
> `AlgebraicGeometry.isCurve_iff_trdeg_functionField_eq_one`.

```lean
noncomputable def curveEquivalenceFinitelyGeneratedFieldExtensionTrdegOneOpposite
    (k : Type u) [Field k] :
    Curve k ≌ (FinitelyGeneratedFieldExtensionTrdegOne k)ᵒᵖ
```

**`AlgebraicGeometry.normalProjectiveCurveEquivalenceRegularProjectiveCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L367). The attribute's comment: “that categories (3) and (5) are the same category: the inclusion of the normal projective curves into the regular projective curves, which is the identity on schemes and on morphisms, is an equivalence”.

> **Stacks Project, Tag 0BY1, categories (3) and (5).** The category of normal projective
> curves over `k` and nonconstant morphisms and the category of regular projective curves over `k`
> and nonconstant morphisms are the same: the equivalence is the inclusion of full subcategories,
> which is the identity on underlying schemes and on morphisms, and it is an equivalence because
> normality and regularity are the same condition on a curve, Stacks 0BX2
> (`AlgebraicGeometry.isRegular_iff_isNormal_of_isCurve`).

```lean
noncomputable def normalProjectiveCurveEquivalenceRegularProjectiveCurve
    (k : Type u) [Field k] : NormalProjectiveCurve k ≌ RegularProjectiveCurve k
```

**`AlgebraicGeometry.nonsingularProjectiveCurveEquivalenceRegularProjectiveCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L388). The attribute's comment: “that categories (4) and (5) are the same category; since `IsRegular` (Tag 02IS) formalizes both `nonsingular` and `regular`, the two categories are the same type and this is the identity equivalence”.

> **Stacks Project, Tag 0BY1, categories (4) and (5).** The category of nonsingular projective
> curves over `k` and nonconstant morphisms is the category of regular projective curves over `k`
> and nonconstant morphisms.
>
> "Nonsingular" and "regular" are synonyms, Stacks 02IS: this library has one predicate,
> `AlgebraicGeometry.IsRegular`, formalizing both, so `AlgebraicGeometry.NonsingularProjectiveCurve`
> and `AlgebraicGeometry.RegularProjectiveCurve` are the same type and the comparison is the
> identity equivalence. The content of the source's claim is the synonymy of the two words, which
> is a matter of terminology and not a mathematical statement that can be formalized separately.

```lean
noncomputable def nonsingularProjectiveCurveEquivalenceRegularProjectiveCurve
    (k : Type u) [Field k] :
    NonsingularProjectiveCurve k ≌ RegularProjectiveCurve k
```

**`AlgebraicGeometry.normalProjectiveCurveEquivalenceNormalProperCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L439). The attribute's comment: “that categories (3) and (6) are the same category: the inclusion of the normal projective curves into the normal proper curves, which is the identity on schemes and on morphisms, is an equivalence”.

> **Stacks Project, Tag 0BY1, categories (3) and (6).** The category of normal projective
> curves over `k` and nonconstant morphisms and the category of normal proper curves over `k` and
> nonconstant morphisms are the same: the equivalence is the inclusion of full subcategories,
> which is the identity on underlying schemes and on morphisms, and it is an equivalence because a
> proper curve is projective, the case of Stacks 0A26 proved outright in
> `AlgebraicGeometry.isProjectiveMorphism_of_isProper_of_isCurve`.

```lean
noncomputable def normalProjectiveCurveEquivalenceNormalProperCurve
    (k : Type u) [Field k] : NormalProjectiveCurve k ≌ NormalProperCurve k
```

**`AlgebraicGeometry.normalProjectiveCurveToCurveFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L545). The attribute's comment: “only that the functor from category (3) to category (2) is fully faithful, which is the source's step `there is a fully faithful functor (5) to (1)`. Essential surjectivity of that functor — the source's final paragraph, that every finitely generated field extension of transcendence degree one is the function field of a normal projective curve — is NOT proved here, so this does not cover the equivalence of categories (2) and (3)”.

> **Stacks Project, Tag 0BY1, the fully faithful functor from category (3) to category (2).**
> Over a field `k`, passing from a normal projective curve and its nonconstant morphisms to the
> same curve and the rational maps of those morphisms is a fully faithful functor from category (3)
> to category (2).
>
> This is the source's step "there is a fully faithful functor (5) → (1)", transported along the
> identification of category (3) with category (5) and along the anti-equivalence of categories (1)
> and (2); both halves are Stacks 0BXZ,
> `AlgebraicGeometry.toRationalMap_bijective` — morphisms from a normal curve to a proper variety
> are exactly the rational maps over the base field — applied to the normal curve `X` and the
> projective, hence proper, curve `Y`.
>
> Essential surjectivity of this functor is `AlgebraicGeometry.normalProjectiveCurveToCurve_essSurj`
> below, and the two together are the equivalence
> `AlgebraicGeometry.normalProjectiveCurveEquivalenceCurve`; this declaration is the fully faithful
> half alone.

```lean
noncomputable def normalProjectiveCurveToCurveFullyFaithful (k : Type u) [Field k] :
    (normalProjectiveCurveToCurve k).FullyFaithful
```

**`AlgebraicGeometry.normalProjectiveCurveEquivalenceCurve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean, line 722](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/FunctionFieldCategories.lean#L722). The attribute's comment: “the equivalence of categories (2) and (3): the functor of `AlgebraicGeometry.normalProjectiveCurveToCurve`, fully faithful by Tag 0BXZ and essentially surjective by `AlgebraicGeometry.normalProjectiveCurveToCurve_essSurj`, which is the source's final paragraph — every curve over `k` is birational to a normal projective curve, obtained by compactifying (Tag 0BXV, outright for an integral scheme of dimension one) and then normalizing (Tag 0BXR, proper by Tag 0GK4)”.

> **Stacks Project, Tag 0BY1, categories (2) and (3).** Over a field `k`, the category of
> normal projective curves over `k` and nonconstant morphisms is equivalent to the category of
> curves over `k` and dominant rational maps.
>
> The functor is the one of `AlgebraicGeometry.normalProjectiveCurveToCurve`; it is fully faithful
> by [Stacks, Tag 0BXZ] and essentially surjective by
> `AlgebraicGeometry.normalProjectiveCurveToCurve_essSurj`. Together with the anti-equivalence of
> categories (1) and (2) and the identifications of categories (3), (4), (5) and (6), all six
> categories of the source are equivalent.

```lean
noncomputable def normalProjectiveCurveEquivalenceCurve (k : Type u) [Field k] :
    NormalProjectiveCurve k ≌ Curve k
```

## Tag 0BY2, a definition

[Tag 0BY2](https://stacks.math.columbia.edu/tag/0BY2) in the Stacks Project.

**`AlgebraicGeometry.NonsingularProjectiveModel`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModel.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NonsingularProjectiveModel.lean#L66).

> A nonsingular projective model of a curve `X` over a field `k` is a regular projective curve
> over `k` together with a `k`-algebra isomorphism from the function field of `X` to its own function
> field.

```lean
structure NonsingularProjectiveModel (k : Type u) [Field k]
    (X : Scheme.{u}) (sX : X ⟶ Spec (.of k)) [IsCurve k sX]
```

## Tag 0BY3, a lemma

[Tag 0BY3](https://stacks.math.columbia.edu/tag/0BY3) in the Stacks Project.

**`AlgebraicGeometry.NonsingularProjectiveModel.isSmoothProjectiveCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SmoothModelOverPerfectField.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/SmoothModelOverPerfectField.lean#L91).

> **Stacks Project, Tag 0BY3.** Let `k` be a field, let `X` be a curve over `k` and let `Y` be
> a nonsingular projective model of `X`. If `k` is perfect then `Y` is a smooth projective
> curve.

```lean
public theorem isSmoothProjectiveCurve [PerfectField k]
    (M : NonsingularProjectiveModel k X sX) :
    Smooth M.structureMap ∧ IsProjectiveVariety k M.structureMap ∧
      IsCurve k M.structureMap
```

## Tag 0BY4, a lemma

[Tag 0BY4](https://stacks.math.columbia.edu/tag/0BY4) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_pullback_of_smooth_models`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ModelBaseChange.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ModelBaseChange.lean#L507). The attribute's comment: “part (4): for a commuting square of fields k to K to Omega and k to K' to Omega with the models Y\_K and Y\_K' smooth, the nonsingular projective model Y\_Omega of (X\_Omega)\_red is isomorphic over Omega to the base change of Y\_K and to the base change of Y\_K'. The three binders `[IsCurve _ (reducedBaseChangeStructureMap k _ sX)]` add nothing: each follows from `[IsCurve k sX]` and `[GeometricallyIrreducible sX]` by the instance `AlgebraicGeometry.isCurve_reducedBaseChangeStructureMap'`, which is not in this file's import closure”.

> **Stacks Project, Tag 0BY4, part (4).** Let `k` be a field and let `X` be a geometrically
> irreducible curve over `k`. For a field extension `K/k` write `Y_K` for a nonsingular projective
> model of `(X_K)_red`. Given a commutative diagram of fields
>
> ```
> Ω  ←  K'
> ↑     ↑
> K  ←  k
> ```
>
> such that `Y_K` and `Y_{K'}` are smooth, we have `Y_Ω = (Y_K)_Ω = (Y_{K'})_Ω`: both base changes
> are isomorphic to `Y_Ω` as schemes over `Ω`, and hence to each other.
>
> The commuting square of fields is the two scalar towers `k ⊆ K ⊆ Ω` and `k ⊆ K' ⊆ Ω`. The
> equality of the source is a canonical isomorphism of schemes over `Ω`: the isomorphism is
> compatible with the structure morphisms, which is part of the conclusion, and it is the only such
> isomorphism matching the birational identifications, by
> `AlgebraicGeometry.NonsingularProjectiveModel.hom_ext`.
>
> The three instance binders `[IsCurve K (reducedBaseChangeStructureMap k K sX)]` and its analogues
> for `K'` and `Ω` are not added hypotheses: each follows from `[IsCurve k sX]` and
> `[GeometricallyIrreducible sX]` by the instance
> `AlgebraicGeometry.isCurve_reducedBaseChangeStructureMap'`, which lives in
> `StacksFrontier/AlgebraicGeometry/Curves/ModelNormalization.lean` and is not in this file's import
> closure, so the facts are named instead.

```lean
public theorem exists_iso_pullback_of_smooth_models
    (k K K' Ω : Type u) [Field k] [Field K] [Field K'] [Field Ω]
    [Algebra k K] [Algebra k K'] [Algebra K Ω] [Algebra K' Ω] [Algebra k Ω]
    [IsScalarTower k K Ω] [IsScalarTower k K' Ω]
    {X : Scheme.{u}} (sX : X ⟶ Spec (.of k))
    [IsCurve k sX] [GeometricallyIrreducible sX]
    [IsCurve K (reducedBaseChangeStructureMap k K sX)]
    [IsCurve K' (reducedBaseChangeStructureMap k K' sX)]
    [IsCurve Ω (reducedBaseChangeStructureMap k Ω sX)]
    (M_K : NonsingularProjectiveModel K (reducedBaseChange k K sX)
      (reducedBaseChangeStructureMap k K sX))
    (M_K' : NonsingularProjectiveModel K' (reducedBaseChange k K' sX)
      (reducedBaseChangeStructureMap k K' sX))
    (M_Ω : NonsingularProjectiveModel Ω (reducedBaseChange k Ω sX)
      (reducedBaseChangeStructureMap k Ω sX))
    (hK : Smooth M_K.structureMap) (hK' : Smooth M_K'.structureMap) :
    (∃ e : M_Ω.Y ≅ pullback M_K.structureMap
        (Spec.map (CommRingCat.ofHom (algebraMap K Ω))),
      e.hom ≫ pullback.snd M_K.structureMap
        (Spec.map (CommRingCat.ofHom (algebraMap K Ω))) = M_Ω.structureMap) ∧
    (∃ e : M_Ω.Y ≅ pullback M_K'.structureMap
        (Spec.map (CommRingCat.ofHom (algebraMap K' Ω))),
      e.hom ≫ pullback.snd M_K'.structureMap
        (Spec.map (CommRingCat.ofHom (algebraMap K' Ω))) = M_Ω.structureMap)
```

**`AlgebraicGeometry.exists_isPurelyInseparable_smooth_nonsingularProjectiveModel_of_isCurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ModelFunctionFieldInvariance.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ModelFunctionFieldInvariance.lean#L338). The attribute's comment: “part (2), with nothing carried and `X` not assumed proper. Tag 09NZ is not needed: the compactification of a curve is Tag 0BXV for an integral scheme of dimension one, where Tag 0A25 holds outright, and the model of a proper curve is its normalization, again integral of dimension one. The source's reduction of the general case to the projective case is carried out with the compactification behind `AlgebraicGeometry.normalProjectiveCurveToCurve_essSurj` (Tag 0BY1) together with `AlgebraicGeometry.NonsingularProjectiveModel.ofFunctionFieldAlgEquiv`, that a nonsingular projective model depends only on the function field”.

> **Stacks Project, Tag 0BY4, part (2).** Let `k` be a field and let `X` be a geometrically
> irreducible curve over `k`. There is a finite purely inseparable extension `K/k` for which
> `(X_K)_red` has a smooth nonsingular projective model.
>
> Nothing is carried and `X` is not assumed proper. The general case is reduced to the proper one
> exactly as in the source: `X` is a dense open subscheme of a projective curve `X̄` over `k`
> (`AlgebraicGeometry.exists_isCurve_isProjectiveMorphism_isOpenImmersion`, the compactification
> behind the essential surjectivity half of [Stacks, Tag 0BY1]), which is again geometrically
> irreducible; the proper case,
> `AlgebraicGeometry.exists_isPurelyInseparable_smooth_nonsingularProjectiveModel'`, applied to `X̄`
> supplies `K` and a smooth model of `(X̄_K)_red`; and that is a model of `(X_K)_red` as well,
> because the reduced base change of a dense open immersion is a dominant open immersion, so the
> two have the same function field over `K`, and a nonsingular projective model depends only on
> the function field.

```lean
public theorem exists_isPurelyInseparable_smooth_nonsingularProjectiveModel_of_isCurve
    (k : Type u) [Field k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k))
    [IsCurve k sX] [GeometricallyIrreducible sX] :
    ∃ (K : Type u) (_ : Field K) (_ : Algebra k K) (_ : Module.Finite k K)
      (_ : IsPurelyInseparable k K),
      ∃ M : NonsingularProjectiveModel K (reducedBaseChange k K sX)
          (reducedBaseChangeStructureMap k K sX),
        Smooth M.structureMap
```

**`AlgebraicGeometry.isIso_globalSections_of_geometricallyReduced_model_reducedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ModelGlobalSections.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ModelGlobalSections.lean#L183). The attribute's comment: “part (3), with the source's own footnote hypothesis: the model is assumed only geometrically reduced, not smooth. The binder `[IsCurve K (reducedBaseChangeStructureMap k K sX)]` adds nothing: it follows from `[IsCurve k sX]` and `[GeometricallyIrreducible sX]` by the instance `AlgebraicGeometry.isCurve_reducedBaseChangeStructureMap'`, which is proved in a module importing this one and so is unavailable here”.

> **Stacks Project, Tag 0BY4, part (3).** Let `k` be a field, let `X` be a geometrically
> irreducible curve over `k`, let `K/k` be a field extension and let `Y_K` be a nonsingular
> projective model of `(X_K)_red`. If `Y_K` is geometrically reduced over `K`, then `K` is the
> ring of global regular functions on `Y_K`.
>
> The instance binder `[IsCurve K (reducedBaseChangeStructureMap k K sX)]` is not an added
> hypothesis: it is a consequence of `[IsCurve k sX]` and `[GeometricallyIrreducible sX]`, proved
> as the instance `AlgebraicGeometry.isCurve_reducedBaseChangeStructureMap'`. That instance lives in
> `StacksFrontier/AlgebraicGeometry/Curves/ModelNormalization.lean`, which imports this file, so it
> cannot be used here and the fact is named instead.

```lean
public theorem isIso_globalSections_of_geometricallyReduced_model_reducedBaseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K] {X : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) [IsCurve k sX] [GeometricallyIrreducible sX]
    [IsCurve K (reducedBaseChangeStructureMap k K sX)]
    (M : NonsingularProjectiveModel K (reducedBaseChange k K sX)
      (reducedBaseChangeStructureMap k K sX))
    (hred : GeometricallyReduced M.structureMap) :
    IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ M.structureMap.appTop)
```

**`AlgebraicGeometry.isIso_globalSections_of_smooth_model_reducedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ModelGlobalSections.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ModelGlobalSections.lean#L212). The attribute's comment: “part (3). The binder `[IsCurve K (reducedBaseChangeStructureMap k K sX)]` adds nothing: it follows from `[IsCurve k sX]` and `[GeometricallyIrreducible sX]` by the instance `AlgebraicGeometry.isCurve_reducedBaseChangeStructureMap'`, which is proved in a module importing this one and so is unavailable here”.

> **Stacks Project, Tag 0BY4, part (3).** Let `k` be a field, let `X` be a geometrically
> irreducible curve over `k`, let `K/k` be a field extension and let `Y_K` be a nonsingular
> projective model of `(X_K)_red`. If `Y_K` is smooth over `K`, then `K` is the ring of global
> regular functions on `Y_K`.
>
> The instance binder `[IsCurve K (reducedBaseChangeStructureMap k K sX)]` adds nothing, for the
> reason given on
> `AlgebraicGeometry.isIso_globalSections_of_geometricallyReduced_model_reducedBaseChange`.

```lean
public theorem isIso_globalSections_of_smooth_model_reducedBaseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K] {X : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) [IsCurve k sX] [GeometricallyIrreducible sX]
    [IsCurve K (reducedBaseChangeStructureMap k K sX)]
    (M : NonsingularProjectiveModel K (reducedBaseChange k K sX)
      (reducedBaseChangeStructureMap k K sX))
    (hsm : Smooth M.structureMap) :
    IsIso ((Scheme.ΓSpecIso (.of K)).inv ≫ M.structureMap.appTop)
```

**`AlgebraicGeometry.exists_nonsingularProjectiveModel_iso_normalization_reducedBaseChange'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ModelNormalization.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/ModelNormalization.lean#L471). The attribute's comment: “part (1), with nothing carried: the source's step `a proper curve is projective` is applied to a normalization, which is integral of dimension one, so Tag 0A25 holds outright as `Stacks.HQuasiProjectiveDimensionOne.isHQuasiProjective_of_isIntegral` and Tag 09NZ is not needed”.

> **Stacks Project, Tag 0BY4, part (1).** Let `k` be a field, let `X` be a proper
> geometrically irreducible curve over `k` and let `K/k` be a field extension. Then `(X_K)_red` has
> a nonsingular projective model whose underlying scheme is the normalization of `X_K` over `K`.
>
> Nothing is carried: the model is `AlgebraicGeometry.normalizationModel'`, whose projectivity is
> the step "a proper curve is projective" applied to a normalization. This is
> `AlgebraicGeometry.exists_nonsingularProjectiveModel_iso_normalization_reducedBaseChange`, proved
> another way.

```lean
public theorem exists_nonsingularProjectiveModel_iso_normalization_reducedBaseChange'
    (k K : Type u) [Field k] [Field K] [Algebra k K] {X : Scheme.{u}}
    (sX : X ⟶ Spec (.of k)) [IsCurve k sX] [GeometricallyIrreducible sX] [IsProper sX] :
    ∃ M : NonsingularProjectiveModel K (reducedBaseChange k K sX)
        (reducedBaseChangeStructureMap k K sX),
      ∃ e : normalizationSchemeOverField K
          (pullback.snd sX (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ≅ M.Y,
        normalizationOverField K
            (pullback.snd sX (Spec.map (CommRingCat.ofHom (algebraMap k K)))) ≫
          pullback.snd sX (Spec.map (CommRingCat.ofHom (algebraMap k K))) =
            e.hom ≫ M.structureMap
```

**`AlgebraicGeometry.exists_isPurelyInseparable_smooth_nonsingularProjectiveModel'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/SmoothModelPurelyInseparable.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/SmoothModelPurelyInseparable.lean#L178). The attribute's comment: “part (2) for a proper `X`, with nothing carried: Tag 09NZ is not assumed, because the model is the normalization of `(X_K)_red`, integral of dimension one, where Tag 0A25 holds outright from Tag 09ND. One hypothesis is named: `X` is assumed proper, because the source's reduction of the general case to the projective case replaces `X` by a nonsingular projective model and so uses Theorem 0BY1; that reduction is carried out in `AlgebraicGeometry.exists_isPurelyInseparable_smooth_nonsingularProjectiveModel_of_isCurve`”.

> **Stacks Project, Tag 0BY4, part (2).** Let `k` be a field and let `X` be a proper
> geometrically irreducible curve over `k`. There is a finite purely inseparable extension `K/k`
> for which `(X_K)_red` has a smooth nonsingular projective model.
>
> Nothing is carried; `X` is assumed proper. This is
> `AlgebraicGeometry.exists_isPurelyInseparable_smooth_nonsingularProjectiveModel` with the model
> `AlgebraicGeometry.normalizationModel'`.

```lean
public theorem exists_isPurelyInseparable_smooth_nonsingularProjectiveModel'
    (k : Type u) [Field k] {X : Scheme.{u}} (sX : X ⟶ Spec (.of k))
    [IsCurve k sX] [GeometricallyIrreducible sX] [IsProper sX] :
    ∃ (K : Type u) (_ : Field K) (_ : Algebra k K) (_ : Module.Finite k K)
      (_ : IsPurelyInseparable k K),
      ∃ M : NonsingularProjectiveModel K (reducedBaseChange k K sX)
          (reducedBaseChangeStructureMap k K sX),
        Smooth M.structureMap
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.2, Tag 0BXX](https://stacks.math.columbia.edu/tag/0BXX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
