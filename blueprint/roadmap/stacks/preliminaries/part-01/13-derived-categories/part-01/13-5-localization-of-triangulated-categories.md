---
declaration: section
origin: cited
lean: CategoryTheory.MorphismProperty.isCompatibleWithTriangulation_iff_shift_one_and_hasMS6, CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation, CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation.toIsCompatibleWithShift, CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation.compatible_with_triangulation, CategoryTheory.MorphismProperty.isIso_mem_of_hasMS6, isCompatibleWithTriangulation_oreConditions, CategoryTheory.Functor.isSaturated_and_isCompatibleWithTriangulation_inverseImage_isomorphisms, CategoryTheory.Functor.isSaturated_and_isCompatibleWithTriangulation
statement: formalized
proof: formalized
---

# 13.5 Localization of triangulated categories

Section 13.5 of the Stacks Project, [Tag 05R1](https://stacks.math.columbia.edu/tag/05R1). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05R2, a definition

[Tag 05R2](https://stacks.math.columbia.edu/tag/05R2) in the Stacks Project.

**`CategoryTheory.MorphismProperty.isCompatibleWithTriangulation_iff_shift_one_and_hasMS6`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean#L119). The attribute's comment: “with MS5 in the form `f ∈ S ⇔ f[1] ∈ S`”.

> For a class `W` satisfying MS1, being compatible with the triangulated structure in the
> sense of `MorphismProperty.IsCompatibleWithTriangulation` is equivalent to the two axioms as
> Stacks states them: MS5 in the form `f ∈ W ⇔ f[1] ∈ W`, and MS6. The passage between the two
> forms of MS5 is `isCompatibleWithShift_iff_of_hasMS6`.

```lean
theorem isCompatibleWithTriangulation_iff_shift_one_and_hasMS6
    {C : Type u} [Category.{v} C] [HasShift C ℤ] [Preadditive C]
    [Limits.HasZeroObject C] [∀ n : ℤ, (shiftFunctor C n).Additive]
    [Pretriangulated C] (W : MorphismProperty C) [W.IsMultiplicative] :
    W.IsCompatibleWithTriangulation ↔
      (∀ ⦃X Y : C⦄ (f : X ⟶ Y), W f ↔ W (f⟦(1 : ℤ)⟧')) ∧ W.HasMS6
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L154) (StacksFrontier): “a multiplicative system compatible with the triangulated structure”.
- [`CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation.toIsCompatibleWithShift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation.toIsCompatibleWithShift#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L156) (StacksFrontier): “MS5, as stability under every shift `[n]`, `n : ℤ`; for a class with MS1 and MS6 this is equivalent to Stacks' form `f ∈ S ⇔ f[1] ∈ S` by Remark 0H30, `MorphismProperty.isCompatibleWithShift_iff_of_hasMS6`”.
- [`CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation.compatible_with_triangulation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.IsCompatibleWithTriangulation.compatible_with_triangulation#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L160) (StacksFrontier): “MS6”.

## Tag 05R3, a lemma

[Tag 05R3](https://stacks.math.columbia.edu/tag/05R3) in the Stacks Project.

**`CategoryTheory.MorphismProperty.isIso_mem_of_hasMS6`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean#L71). The attribute's comment: “(1)”.

> If `W` contains all identities and satisfies MS6, then `W` contains every isomorphism of
> `C`.

```lean
theorem isIso_mem_of_hasMS6
    {C : Type u} [Category.{v} C] [HasShift C ℤ] [Preadditive C]
    [Limits.HasZeroObject C] [∀ n : ℤ, (shiftFunctor C n).Additive]
    [Pretriangulated C] (W : MorphismProperty C)
    [W.ContainsIdentities] [W.HasMS6]
    {X Y : C} (f : X ⟶ Y) [IsIso f] : W f
```

**`isCompatibleWithTriangulation_oreConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean#L185). The attribute's comment: “(2)”.

> If `W` satisfies MS1 (`W.IsMultiplicative`), MS5 and MS6
> (`W.IsCompatibleWithTriangulation`), then `W` satisfies MS2: both the left (LMS2) and the right
> (RMS2) Ore conditions hold.

```lean
theorem isCompatibleWithTriangulation_oreConditions
    {C : Type u} [Category.{v} C] [HasShift C ℤ] [Preadditive C]
    [Limits.HasZeroObject C] [∀ n : ℤ, (shiftFunctor C n).Additive]
    [Pretriangulated C] (W : MorphismProperty C)
    [W.IsMultiplicative]
    [W.IsCompatibleWithTriangulation] :
    (∀ ⦃X Y : C⦄ (φ : W.RightFraction X Y),
        ∃ ψ : W.LeftFraction X Y, φ.f ≫ ψ.s = φ.s ≫ ψ.f)
    ∧
    (∀ ⦃X Y : C⦄ (φ : W.LeftFraction X Y),
        ∃ ψ : W.RightFraction X Y, ψ.s ≫ φ.f = ψ.f ≫ φ.s)
```

## Tag 05R4, a lemma

[Tag 05R4](https://stacks.math.columbia.edu/tag/05R4) in the Stacks Project.

**`CategoryTheory.Functor.isSaturated_and_isCompatibleWithTriangulation_inverseImage_isomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L345). References: SGA 4½ Etat 0 (2.2), “partial”.

> Let `F : C ⥤ D` be an exact functor of pre-triangulated categories. The class
> `W = (isomorphisms D).inverseImage F` of morphisms of `C` inverted by `F` is a saturated
> multiplicative system (MS1, MS2, MS3 and the cancellation axiom MS4) compatible with the
> triangulated structure on `C` (MS5, MS6).

```lean
theorem Functor.isSaturated_and_isCompatibleWithTriangulation_inverseImage_isomorphisms
    (F : C ⥤ D) [F.CommShift ℤ] [F.IsTriangulated] :
    ((isomorphisms D).inverseImage F).IsSaturated ∧
      ((isomorphisms D).inverseImage F).IsCompatibleWithTriangulation
```

## Tag 05R5, a lemma

[Tag 05R5](https://stacks.math.columbia.edu/tag/05R5) in the Stacks Project.

**`CategoryTheory.Functor.isSaturated_and_isCompatibleWithTriangulation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L442).

> Let `H : 𝒟 ⥤ 𝒜` be a homological functor from a pre-triangulated category to an abelian
> category. Then
> `S = {f ∈ Arrows(𝒟) ∣ Hⁱ(f) is an isomorphism for all i ∈ ℤ}`
> is a saturated multiplicative system compatible with the triangulated
> structure on `𝒟` (MS5 and MS6).

```lean
theorem CategoryTheory.Functor.isSaturated_and_isCompatibleWithTriangulation
    {D : Type u₁} [Category.{v₁} D] [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D]
    {A : Type u₂} [Category.{v₂} A] [Abelian A] (H : D ⥤ A) [H.IsHomological]
    (S : MorphismProperty D)
    (hS : ∀ ⦃X Y : D⦄ (f : X ⟶ Y), S f ↔ ∀ i : ℤ, IsIso (H.map (f⟦i⟧'))) :
    S.IsSaturated ∧ S.IsCompatibleWithTriangulation
```

## Tag 05R6, a proposition

[Tag 05R6](https://stacks.math.columbia.edu/tag/05R6) in the Stacks Project.

**`CategoryTheory.Triangulated.Localization.existsUnique_pretriangulated_and_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L497). References: SGA 4½ Etat 0 (Problem2), “A\_S exists, Q exact”; SGA 4½ Etat 0 (2.3.2), “partial”.

> Let `C` be a pre-triangulated category, let `W` be a multiplicative system of morphisms of `C`
> compatible with the triangulated structure, and let `L : C ⥤ D` be a localization functor for `W`,
> where `D` is additive, has a shift with which `L` commutes, and `L` is additive. Then there is a
> unique pre-triangulated structure on `D` making `L` exact, namely
> `CategoryTheory.Triangulated.Localization.pretriangulated L W`, and it is triangulated whenever `C`
> is.

```lean
theorem existsUnique_pretriangulated_and_isTriangulated :
    (letI := pretriangulated L W; L.IsTriangulated) ∧
      (∀ h : Pretriangulated D, (letI := h; L.IsTriangulated) → h = pretriangulated L W) ∧
        (letI := pretriangulated L W; IsTriangulated C → IsTriangulated D)
```

## Tag 05R7, a lemma

[Tag 05R7](https://stacks.math.columbia.edu/tag/05R7) in the Stacks Project.

**`CategoryTheory.Functor.isTriangulated_of_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L535). The attribute's comment: “(2)”. References: SGA 4½ Etat 0 (Problem2), “G is exact”; SGA 4½ Etat 0 (2.3.2), “partial”.

> Let `C` be a pre-triangulated category, `W` a multiplicative system of morphisms of `C`
> compatible with the triangulated structure, and `L : C ⥤ D` the (exact) localization functor. If
> `F : C ⥤ E` is an exact functor to a pre-triangulated category and `F' : D ⥤ E` is its
> factorization through `L`, then `F'`, for the commutation with the shift it inherits from that
> factorization, is exact.

```lean
theorem isTriangulated_of_localization
    {E : Type u₃} [Category.{v₃} E] [HasZeroObject E] [HasShift E ℤ] [Preadditive E]
    [∀ n : ℤ, (shiftFunctor E n).Additive] [Pretriangulated E]
    (F : C ⥤ E) [F.CommShift ℤ] [F.IsTriangulated] (F' : D ⥤ E) [Lifting L W F F'] :
    letI := commShiftOfLocalization L W ℤ F F'
    F'.IsTriangulated
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.isHomological_of_localization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.isHomological_of_localization#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Pretriangulated.lean#L546) (StacksFrontier): “(1)”.

## Tag 0GSL, a lemma

[Tag 0GSL](https://stacks.math.columbia.edu/tag/0GSL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isSaturated_and_isCompatibleWithTriangulation_inverseImage_ι_and_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/Resolutions.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/Resolutions.lean#L176).

> Let `C` be a pre-triangulated category, let `P` be a full pre-triangulated subcategory of `C`,
> and let `W` be a saturated multiplicative system of morphisms of `C` compatible with the
> triangulated structure. Then `W' = W ∩ Arrows(P)`, i.e. `W.inverseImage P.ι`, is a saturated
> multiplicative system on `P` compatible with the triangulated structure; the functor
> `W'⁻¹P ⥤ W⁻¹C` induced by the inclusion, with the commutation with shifts it inherits from the
> localization, is a triangulated (exact) functor of pre-triangulated categories; and if every
> object of `C` admits a resolution by `P` — a morphism `s : X' ⟶ X` in `W` with `X'` in `P` — this
> functor is an equivalence. Together: `W'⁻¹P ⥤ W⁻¹C` is an equivalence of pre-triangulated
> categories.

```lean
theorem isSaturated_and_isCompatibleWithTriangulation_inverseImage_ι_and_isTriangulated
    (hW : W.IsSaturated) [W.IsCompatibleWithTriangulation] :
    ∃ (hS : (W.inverseImage P.ι).IsSaturated)
      (hT : (W.inverseImage P.ι).IsCompatibleWithTriangulation),
      letI := hW.hasLeftCalculusOfFractions
      letI := hS.hasLeftCalculusOfFractions
      letI := hT
      (({ functor := P.ι, map := le_rfl } :
            LocalizerMorphism (W.inverseImage P.ι) W).localizedFunctor
          (W.inverseImage P.ι).Q W.Q).IsTriangulated ∧
      (({ functor := P.ι, map := le_rfl } :
            LocalizerMorphism (W.inverseImage P.ι) W).HasLeftResolutions →
        ({ functor := P.ι, map := le_rfl } :
            LocalizerMorphism (W.inverseImage P.ι) W).IsLocalizedEquivalence ∧
        (({ functor := P.ι, map := le_rfl } :
            LocalizerMorphism (W.inverseImage P.ι) W).localizedFunctor
          (W.inverseImage P.ι).Q W.Q).IsEquivalence)
```

## Tag 05R8, a lemma

[Tag 05R8](https://stacks.math.columbia.edu/tag/05R8) in the Stacks Project.

**`StacksLocalizationKernel.statementA`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean#L464). The attribute's comment: “(1)-(4)”.

> Let `S` be a multiplicative system compatible with the triangulated structure and `Q` a
> localization functor for `S`. For an object `Z`, the conditions `Cond1` to `Cond4` are
> equivalent.

```lean
theorem statementA
    (S : MorphismProperty 𝒟)
    {𝒟_S : Type*} [Category 𝒟_S] (Q : 𝒟 ⥤ 𝒟_S) [Q.IsLocalization S]
    (Z : 𝒟)
    (hL : S.HasLeftCalculusOfFractions)
    (hR : S.HasRightCalculusOfFractions) (hcompat : S.IsCompatibleWithTriangulation) :
    [Cond1 Q Z, Cond2 S Z, Cond3 S Z, Cond4 S Z].TFAE
```

**`StacksLocalizationKernel.statementB`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/OreConditionsAndKernel.lean#L483). The attribute's comment: “(5)-(7)”.

> Let `S` be a saturated multiplicative system compatible with the triangulated structure and
> `Q` a localization functor for `S`. For an object `Z`, the conditions `Cond1` to `Cond7` are
> equivalent.

```lean
theorem statementB
    (S : MorphismProperty 𝒟)
    {𝒟_S : Type*} [Category 𝒟_S] (Q : 𝒟 ⥤ 𝒟_S) [Q.IsLocalization S]
    (Z : 𝒟)
    (hL : S.HasLeftCalculusOfFractions)
    (hR : S.HasRightCalculusOfFractions) (hcompat : S.IsCompatibleWithTriangulation)
    (hsat : S.IsSaturatedMultiplicative) :
    [Cond1 Q Z, Cond2 S Z, Cond3 S Z, Cond4 S Z,
     Cond5 S Z, Cond6 S Z, Cond7 S Z].TFAE
```

## Tag 05R9, a lemma

[Tag 05R9](https://stacks.math.columbia.edu/tag/05R9) in the Stacks Project.

**`CategoryTheory.MorphismProperty.IsSaturated.isFiltered_and_final_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Localization/IndexCategory.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/Localization/IndexCategory.lean#L436). References: SGA 4 XVII (1.2.2.1).

> Let `W` be a saturated multiplicative system of a pre-triangulated category `C`, compatible
> with the triangulated structure, and let `T = (X, Y, Z, f, g, h)` be a distinguished triangle of
> `C`. Let `ℐ` be the category of `W`-morphisms of triangles out of `T`: the full subcategory of
> `Under T` in `Triangle C` whose objects are the morphisms of triangles `(s, s', s'') : T ⟶ T'` with
> `T'` distinguished and `s, s', s''` in `W`.
>
> Then `ℐ` is filtered, and the three functors `ℐ ⥤ X/W`, `ℐ ⥤ Y/W`, `ℐ ⥤ Z/W` given by
> `(s, s', s'') ↦ s`, `s'`, `s''` — the projections `Triangle.π₁`, `Triangle.π₂`, `Triangle.π₃` read
> on morphisms under `T` — are cofinal.

```lean
theorem CategoryTheory.MorphismProperty.IsSaturated.isFiltered_and_final_component
    {W : MorphismProperty C} (hW : W.IsSaturated) [W.IsCompatibleWithTriangulation]
    {T : Triangle C} (hT : T ∈ distTriang C) (ℐ : ObjectProperty (Under T))
    (hℐ : ∀ A : Under T, ℐ A ↔
      A.right ∈ distTriang C ∧ W A.hom.hom₁ ∧ W A.hom.hom₂ ∧ W A.hom.hom₃) :
    IsFiltered ℐ.FullSubcategory ∧
      (MorphismProperty.Comma.lift (ℐ.ι ⋙ Under.post Triangle.π₁)
        (fun A => ((hℐ _).1 A.2).2.1) (fun _ => trivial) (fun _ => trivial) :
          ℐ.FullSubcategory ⥤ W.Under ⊤ T.obj₁).Final ∧
      (MorphismProperty.Comma.lift (ℐ.ι ⋙ Under.post Triangle.π₂)
        (fun A => ((hℐ _).1 A.2).2.2.1) (fun _ => trivial) (fun _ => trivial) :
          ℐ.FullSubcategory ⥤ W.Under ⊤ T.obj₂).Final ∧
      (MorphismProperty.Comma.lift (ℐ.ι ⋙ Under.post Triangle.π₃)
        (fun A => ((hℐ _).1 A.2).2.2.2) (fun _ => trivial) (fun _ => trivial) :
          ℐ.FullSubcategory ⥤ W.Under ⊤ T.obj₃).Final
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.5, Tag 05R1](https://stacks.math.columbia.edu/tag/05R1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
