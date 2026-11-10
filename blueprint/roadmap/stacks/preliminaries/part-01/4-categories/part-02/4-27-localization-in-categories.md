---
declaration: section
origin: cited
lean: MorphismProperty.IsMultiplicative, MorphismProperty.HasLeftCalculusOfFractions, MorphismProperty.HasRightCalculusOfFractions, MorphismProperty.LeftFraction, CategoryTheory.MorphismProperty.LeftFractionRel, MorphismProperty.equivalenceLeftFractionRel, MorphismProperty.LeftFraction.comp₀_rel, MorphismProperty.LeftFraction.Localization.Hom.comp_eq
statement: formalized
proof: formalized
---

# 4.27 Localization in categories

Section 4.27 of the Stacks Project, [Tag 04VB](https://stacks.math.columbia.edu/tag/04VB). 20 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 19 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04VC, a definition

[Tag 04VC](https://stacks.math.columbia.edu/tag/04VC) in the Stacks Project.

Declarations registered for the tag:

- [`MorphismProperty.IsMultiplicative`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.IsMultiplicative#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L77) (StacksFrontier): “LMS1 = RMS1: identities and composites of elements of S lie in S”.
- [`MorphismProperty.HasLeftCalculusOfFractions`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.HasLeftCalculusOfFractions#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L79) (StacksFrontier): “left multiplicative system: LMS1, LMS2 (exists\_leftFraction), LMS3 (ext)”.
- [`MorphismProperty.HasRightCalculusOfFractions`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.HasRightCalculusOfFractions#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L81) (StacksFrontier): “right multiplicative system: RMS1, RMS2 (exists\_rightFraction), RMS3 (ext)”.

## Tag 04VD, a lemma

[Tag 04VD](https://stacks.math.columbia.edu/tag/04VD) in the Stacks Project.

Declarations registered for the tag:

- [`MorphismProperty.LeftFraction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L83) (StacksFrontier): “the pairs (f : X → Y', s : Y → Y') with s ∈ S”.
- [`CategoryTheory.MorphismProperty.LeftFractionRel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.LeftFractionRel#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L85) (StacksFrontier): “the relation on pairs”.
- [`MorphismProperty.equivalenceLeftFractionRel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.equivalenceLeftFractionRel#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L86) (StacksFrontier): “(1) the relation is an equivalence relation”.
- [`MorphismProperty.LeftFraction.comp₀_rel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.comp₀_rel#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L88) (StacksFrontier): “(2) the class of the composite does not depend on the square chosen by LMS2”.
- [`MorphismProperty.LeftFraction.Localization.Hom.comp_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.Hom.comp_eq#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L90) (StacksFrontier): “(2) composition of classes is computed on representatives”.
- [`MorphismProperty.LeftFraction.Localization.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L92) (StacksFrontier): “(3) the category S⁻¹C”.

## Tag 0BM2, a definition

[Tag 0BM2](https://stacks.math.columbia.edu/tag/0BM2) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.LeftFraction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.LeftFraction#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L106) (StacksFrontier): “the pair `(f : X ⟶ Y', s : Y ⟶ Y')` with `s ∈ S`”.
- [`CategoryTheory.MorphismProperty.LeftFraction.Localization.Hom.mk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.LeftFraction.Localization.Hom.mk#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L108) (StacksFrontier): “its equivalence class `s⁻¹f`, a morphism `X ⟶ Y` of `S⁻¹C`”.

## Tag 04VE, a lemma

[Tag 04VE](https://stacks.math.columbia.edu/tag/04VE) in the Stacks Project.

**`CategoryTheory.Localization.exists_common_leftFraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/CommonDenominator.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/CommonDenominator.lean#L141).

> **Stacks 04VE**.
> Let `W : MorphismProperty C` have left calculus of fractions and let `L` be a
> localisation functor for `W`. For any finite family
> `g : ∀ i, L.obj (X i) ⟶ L.obj Y`, there exist a common target `Y' : C`, a
> morphism `s : Y ⟶ Y'` with `W s`, and a family `f : ∀ i, X i ⟶ Y'` such that
> each `g i` equals `L.map (f i) ≫ (Localization.isoOfHom L W s _).inv`.

```lean
theorem exists_common_leftFraction
    {C : Type u} [Category.{v} C] {W : MorphismProperty C}
    {D : Type*} [Category D] (L : C ⥤ D) [L.IsLocalization W]
    [W.HasLeftCalculusOfFractions]
    {ι : Type*} [Finite ι]
    {X : ι → C} {Y : C}
    (g : ∀ i, L.obj (X i) ⟶ L.obj Y) :
    ∃ (Y' : C) (s : Y ⟶ Y') (hs : W s) (f : ∀ i, X i ⟶ Y'),
      ∀ i, g i = L.map (f i) ≫ (Localization.isoOfHom L W s hs).inv
```

## Tag 04VF, a lemma

[Tag 04VF](https://stacks.math.columbia.edu/tag/04VF) in the Stacks Project.

**`map_eq_iff_leftFractionRel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/Equality.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/Equality.lean#L55).

> **Stacks 04VF.** For a left multiplicative system `W` on `C` and a localization functor
> `L : C ⥤ D` at `W`, two left fractions `φ ψ : X ⟶ Y` have the same image in `D` if and only if
> `LeftFractionRel φ ψ`, i.e. if and only if they agree after postcomposition with a suitable
> morphism of `W`.

```lean
theorem map_eq_iff_leftFractionRel {C D : Type*} [Category C] [Category D] (L : C ⥤ D)
    {W : MorphismProperty C} [W.HasLeftCalculusOfFractions] [L.IsLocalization W]
    {X Y : C} (φ ψ : W.LeftFraction X Y) :
    φ.map L (Localization.inverts _ _) = ψ.map L (Localization.inverts _ _) ↔
      LeftFractionRel φ ψ
```

## Tag 05Q0, a remark

[Tag 05Q0](https://stacks.math.columbia.edu/tag/05Q0) in the Stacks Project.

**`CategoryTheory.MorphismProperty.isColimitUnderHomCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/HomAsColimit.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/HomAsColimit.lean#L128). The attribute's comment: “the displayed formula 05Q1: the morphisms X ⟶ Y of the localization are the filtered colimit of the sets Mor\_C(X, Y') over the objects (s : Y ⟶ Y') of Y/S, at the tautological cocone whose leg at s sends f to the left fraction s⁻¹ f”. References: SGA 4 VI (6.5).

> **Morphisms of `W⁻¹C` as a colimit over `Y/S`**: for a left multiplicative system `W` on `C`,
> a localization functor `L : C ⥤ D` of `C` at `W` and objects `X`, `Y` of `C`, the morphisms
> `L.obj X ⟶ L.obj Y` of `W⁻¹C` are the colimit `colim_{(s : Y ⟶ Y') ∈ Y/S} Mor_C(X, Y')`, in the
> sense that the tautological cocone `underHomCocone`, whose leg at `s` sends `f` to the left
> fraction `s⁻¹ f`, is a colimit cocone.
> The index category `Y/S` is filtered by
> `MorphismProperty.isFiltered_under_of_hasLeftCalculusOfFractions`, so this exhibits the morphisms
> of `W⁻¹C` as a filtered colimit of morphisms of `C`.

```lean
noncomputable def isColimitUnderHomCocone (X Y : C) : IsColimit (W.underHomCocone L X Y)
```

## Tag 04VG, a lemma

[Tag 04VG](https://stacks.math.columbia.edu/tag/04VG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.LeftFraction.Localization.Q`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.LeftFraction.Localization.Q#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L94) (StacksFrontier): “(1) the functor Q”. References: SGA 4 VI (6.5); SGA 4½ Etat 0 (2.3.1).
- [`MorphismProperty.LeftFraction.Localization.Q_map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.Q_map#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L95) (StacksFrontier): “(1) Q sends f to the class of (f, id)”.
- [`MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.inverts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.inverts#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L97) (StacksFrontier): “(2) Q(s) is an isomorphism for s ∈ S”.
- [`MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.lift#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L99) (StacksFrontier): “(3) existence of H”.
- [`MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.fac`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.fac#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L101) (StacksFrontier): “(3) H ∘ Q = G”.
- [`MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.uniq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=MorphismProperty.LeftFraction.Localization.StrictUniversalPropertyFixedTarget.uniq#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch04.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch04.lean#L103) (StacksFrontier): “(3) uniqueness of H”.

## Tag 05Q2, a lemma

[Tag 05Q2](https://stacks.math.columbia.edu/tag/05Q2) in the Stacks Project.

**`CategoryTheory.MorphismProperty.Q_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/Commutation.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/Commutation.lean#L53). References: SGA 5 V (2.3.4), “first assertion”.

> **Stacks 05Q2.** For a left multiplicative system `W` on `C`, the localization functor
> `Q : C ⥤ W⁻¹C` commutes with finite colimits. This does not assert that `W⁻¹C` has finite
> colimits: only that `Q` carries a finite colimit cocone of `C` to a colimit cocone.

```lean
theorem Q_preservesFiniteColimits
    {C : Type*} [Category C] (W : MorphismProperty C) [W.HasLeftCalculusOfFractions] :
    Limits.PreservesFiniteColimits W.Q
```

## Tag 05Q3, a lemma

[Tag 05Q3](https://stacks.math.columbia.edu/tag/05Q3) in the Stacks Project.

**`CategoryTheory.MorphismProperty.exists_leftFraction_lift_of_commSq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/LiftSquare.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/LiftSquare.lean#L116).

> **Stacks 05Q3**.
> A commutative square in the left localisation `W⁻¹C` between images of
> morphisms `f : X ⟶ Y` and `f' : X' ⟶ Y'` of `C` lifts to a commutative
> diagram in `C` involving two morphisms in `W`.

```lean
lemma exists_leftFraction_lift_of_commSq
    {X Y X' Y' : C} (f : X ⟶ Y) (f' : X' ⟶ Y')
    (a : (LeftFraction.Localization.Q W).obj X ⟶ (LeftFraction.Localization.Q W).obj X')
    (b : (LeftFraction.Localization.Q W).obj Y ⟶ (LeftFraction.Localization.Q W).obj Y')
    (sq : (LeftFraction.Localization.Q W).map f ≫ b =
      a ≫ (LeftFraction.Localization.Q W).map f') :
    ∃ (X'' Y'' : C) (g : X ⟶ X'') (s : X' ⟶ X'') (hs : W s)
      (h : Y ⟶ Y'') (t : Y' ⟶ Y'') (ht : W t) (f'' : X'' ⟶ Y''),
      f ≫ h = g ≫ f'' ∧ s ≫ f'' = f' ≫ t ∧
      a = (LeftFraction.mk g s hs).map (LeftFraction.Localization.Q W)
            (Localization.inverts _ _) ∧
      b = (LeftFraction.mk h t ht).map (LeftFraction.Localization.Q W)
            (Localization.inverts _ _)
```

## Tag 04VH, a lemma

[Tag 04VH](https://stacks.math.columbia.edu/tag/04VH) in the Stacks Project.

**`CategoryTheory.MorphismProperty.RightFraction.comp_rel_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/Defs.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/Defs.lean#L174). The attribute's comment: “(2)”. References: SGA 4 VI (6.5), “6.5 c)”.

> **Stacks 04VH (2)**.
> The canonical composition of representatives respects the equivalence relation
> in both arguments. Combined with `RightFraction.comp_rel_compOfOre`, which identifies it
> with the composition along an arbitrary Ore square, this is well-definedness of
> composition on the quotient.

```lean
theorem RightFraction.comp_rel_comp [W.HasRightCalculusOfFractions] {X Y Z : C}
    {φ φ' : W.RightFraction X Y} {ψ ψ' : W.RightFraction Y Z} (hφ : RightFractionRel φ φ')
    (hψ : RightFractionRel ψ ψ') :
    RightFractionRel (RightFraction.comp W φ ψ) (RightFraction.comp W φ' ψ')
```

**`CategoryTheory.MorphismProperty.RightLocalization.category`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/Defs.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/Defs.lean#L272). The attribute's comment: “(3)”. References: SGA 4 VI (6.5).

> **Stacks 04VH (3)**.
> The objects of the right-fractions model `W⁻¹C` are the objects of `C`, the hom-sets are
> `RightLocalization.Hom W X Y`, identities are `RightLocalization.Hom.id W X`, and
> composition is `RightLocalization.Hom.comp W`. The category axioms are
> `RightLocalization.Hom.id_comp`, `.comp_id` and `.assoc`.

```lean
noncomputable instance RightLocalization.category [W.HasRightCalculusOfFractions] :
    Category (RightLocalization W)
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.equivalenceRightFractionRel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.equivalenceRightFractionRel#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Localization/RightFraction/Defs.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/Defs.lean#L52) (StacksFrontier): “(1)”.

## Tag 0BM3, a definition

[Tag 0BM3](https://stacks.math.columbia.edu/tag/0BM3) in the Stacks Project.

**`RightLocalizationAsFraction.fInvS`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/Morphism.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/Morphism.lean#L69).

> Given a morphism `f : X' ⟶ Y` and a morphism `s : X' ⟶ X` with `s ∈ W` (where
> `W` is a right multiplicative system, i.e. has a right calculus of fractions),
> the morphism `f s⁻¹ : X ⟶ Y` in the localized category `S⁻¹C = W.Localization`.
>
> Concretely, this is the image under `W.Q` of the pair `(f, s)`, which represents
> the equivalence class of `(f, s)` under `RightFractionRel`.

```lean
noncomputable def fInvS [W.HasRightCalculusOfFractions]
    {X Y X' : C} (f : X' ⟶ Y) (s : X' ⟶ X) (hs : W s) :
    W.Q.obj X ⟶ W.Q.obj Y
```

## Tag 04VI, a lemma

[Tag 04VI](https://stacks.math.columbia.edu/tag/04VI) in the Stacks Project.

**`CategoryTheory.Localization.exists_common_rightFraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/CommonDenominator.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/CommonDenominator.lean#L169). References: SGA 4½ Etat 0 (2.3.2), “partial”.

> **Stacks 04VI** (common right denominator).
>
> Let `W : MorphismProperty C` admit a right calculus of fractions. Given a
> finite family of morphisms `g i : W.Q.obj X ⟶ W.Q.obj (Y i)` in the
> localization with common source `W.Q.obj X`, there exist an object `X'` of
> `C`, a morphism `s : X' ⟶ X` in `W`, and a family `f i : X' ⟶ Y i` in `C`
> such that each `g i` is represented by the right fraction `(s, f i)`.

```lean
theorem exists_common_rightFraction
    (W : MorphismProperty C) [W.HasRightCalculusOfFractions]
    {ι : Type*} [Finite ι] {X : C} {Y : ι → C}
    (g : ∀ i, W.Q.obj X ⟶ W.Q.obj (Y i)) :
    ∃ (X' : C) (s : X' ⟶ X) (hs : W s) (f : ∀ i, X' ⟶ Y i),
      ∀ i, g i = (MorphismProperty.RightFraction.mk s hs (f i)).map
        W.Q (Localization.inverts _ W)
```

## Tag 04VJ, a lemma

[Tag 04VJ](https://stacks.math.columbia.edu/tag/04VJ) in the Stacks Project.

**`map_eq_iff_rightFractionRel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/Equality.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/Equality.lean#L55).

> **Stacks 04VJ.** For a right multiplicative system `W` on `C` and a localization functor
> `L : C ⥤ D` at `W`, two right fractions `φ ψ : X ⟶ Y` have the same image in `D` if and only if
> `RightFractionRel φ ψ`, i.e. if and only if they agree after precomposition with a suitable
> morphism of `W`.

```lean
theorem map_eq_iff_rightFractionRel {C D : Type*} [Category C] [Category D] (L : C ⥤ D)
    {W : MorphismProperty C} [W.HasRightCalculusOfFractions] [L.IsLocalization W]
    {X Y : C} (φ ψ : W.RightFraction X Y) :
    φ.map L (Localization.inverts _ _) = ψ.map L (Localization.inverts _ _) ↔
      RightFractionRel φ ψ
```

## Tag 05Q4, a remark

[Tag 05Q4](https://stacks.math.columbia.edu/tag/05Q4) in the Stacks Project.

**`CategoryTheory.MorphismProperty.isCofiltered_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/AsColimit.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/AsColimit.lean#L66).

> **Stacks 05Q4**, first claim: for a right multiplicative system `W` on `C` and an
> object `X` of `C`, the category `S/X = W.Over ⊤ X` of `W`-morphisms to `X` is cofiltered
> in the sense of Stacks 04AZ, i.e. its identity diagram is a cofiltered diagram.

```lean
theorem isCofiltered_over (X : C) : (𝟭 (W.Over ⊤ X)).IsCofiltered
```

**`CategoryTheory.MorphismProperty.isColimitOverHomCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/LeftFraction/AsColimit.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/LeftFraction/AsColimit.lean#L147). References: SGA 4½ Etat 0 (2.3.2); SGA 5 V (2.3.3), “Hom-set clause”.

> **Stacks 05Q4**, second claim: for a right multiplicative system `W` on `C`, a
> localization functor `L : C ⥤ D` of `C` at `W` and objects `X`, `Y` of `C`, the
> morphisms `L.obj X ⟶ L.obj Y` of `W⁻¹C` are the colimit
> `colim_{(s : X' ⟶ X) ∈ (S/X)ᵒᵖ} Mor_C(X', Y)`, in the sense that the tautological cocone
> `overHomCocone`, whose leg at `s` sends `f` to the right fraction `f s⁻¹`, is a colimit
> cocone. The index category `(S/X)ᵒᵖ` is filtered by `isCofiltered_over`, so this
> exhibits the morphisms of `W⁻¹C` as a filtered colimit of morphisms of `C`.

```lean
noncomputable def isColimitOverHomCocone (X Y : C) : IsColimit (W.overHomCocone L X Y)
```

## Tag 04VK, a lemma

[Tag 04VK](https://stacks.math.columbia.edu/tag/04VK) in the Stacks Project.

**`Q04VK`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/UniversalProperty.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/UniversalProperty.lean#L64). The attribute's comment: “(1)”. References: SGA 5 V (2.3), “functor p : E → E(S⁻¹)”; SGA 4½ Etat 0 (2.3.1).

> The canonical localization functor `Q04VK : 𝓒 ⥤ S⁻¹𝓒` (Stacks Tag 04VK (1)).
> This is the Mathlib functor `LeftFraction.Localization.Q`.

```lean
noncomputable def Q04VK : 𝓒 ⥤ LeftFraction.Localization S
```

**`Q_isIso_of_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/UniversalProperty.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/UniversalProperty.lean#L81). The attribute's comment: “(2)”.

> Stacks 04VK (2): For any `s ∈ S` the morphism `Q04VK(s)` is an isomorphism
> in `S⁻¹𝓒`.

```lean
theorem Q_isIso_of_mem {X Y : 𝓒} (s : X ⟶ Y) (hs : S s) :
    IsIso ((Q04VK S).map s)
```

**`exists_unique_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/UniversalProperty.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/UniversalProperty.lean#L92). The attribute's comment: “(3)”. References: SGA 5 V (2.3), “left calc. of fractions”; SGA 4½ Etat 0 (2.3.1), “partial”; SGA 4½ Etat 0 (Problem2), “partial”.

> Stacks 04VK (3) — combined statement: for any functor `G : 𝓒 ⥤ 𝓓`
> inverting `S`, there exists a *unique* functor `H : S⁻¹𝓒 ⥤ 𝓓` such that
> `H ∘ Q04VK = G`.

```lean
theorem exists_unique_lift (G : 𝓒 ⥤ 𝓓) (hG : S.IsInvertedBy G) :
    ∃! H : LeftFraction.Localization S ⥤ 𝓓, (Q04VK S) ⋙ H = G
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.q_isLocalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.q_isLocalization#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks04VK.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Stacks04VK.lean#L10) (StacksFrontier). References: SGA 4½ Etat 0 (2.3.1), “partial”; SGA 4½ Etat 0 (2.3.2), “partial”.

## Tag 05Q6, a lemma

[Tag 05Q6](https://stacks.math.columbia.edu/tag/05Q6) in the Stacks Project.

**`CategoryTheory.MorphismProperty.Q_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/Commutation.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/Commutation.lean#L354).

> **Stacks 05Q6.** For a right multiplicative system `W` on `C`, the localization functor
> `Q : C ⥤ W⁻¹C` commutes with finite limits. This does not assert that `W⁻¹C` has finite
> limits: only that `Q` carries a finite limit cone of `C` to a limit cone.

```lean
theorem Q_preservesFiniteLimits
    {C : Type*} [Category C] (W : MorphismProperty C)
    [W.HasRightCalculusOfFractions] :
    PreservesFiniteLimits W.Q
```

## Tag 05Q7, a lemma

[Tag 05Q7](https://stacks.math.columbia.edu/tag/05Q7) in the Stacks Project.

**`CategoryTheory.MorphismProperty.exists_rightFraction_lift_of_commSq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/RightFraction/LiftSquare.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/RightFraction/LiftSquare.lean#L59).

> **Stacks 05Q7.**
> Let `W : MorphismProperty C` admit a right calculus of fractions and let
> `L : C ⥤ D` be a localization of `C` at `W`. Given morphisms `f : X ⟶ Y` and
> `f' : X' ⟶ Y'` in `C`, and morphisms `a : L.obj X ⟶ L.obj X'`,
> `b : L.obj Y ⟶ L.obj Y'` in `D` such that `a ≫ L.map f' = L.map f ≫ b`,
> there exist objects `X''`, `Y''` in `C`, a morphism `f'' : X'' ⟶ Y''`,
> morphisms `s : X'' ⟶ X`, `t : Y'' ⟶ Y` with `W s`, `W t`, and morphisms
> `g : X'' ⟶ X'`, `h : Y'' ⟶ Y'` such that
> `s ≫ f = f'' ≫ t`, `g ≫ f' = f'' ≫ h`,
> `L.map s ≫ a = L.map g`, and `L.map t ≫ b = L.map h`.

```lean
theorem exists_rightFraction_lift_of_commSq
    [L.IsLocalization W] [HasRightCalculusOfFractions W]
    {X Y X' Y' : C} (f : X ⟶ Y) (f' : X' ⟶ Y')
    (a : L.obj X ⟶ L.obj X') (b : L.obj Y ⟶ L.obj Y')
    (sq : a ≫ L.map f' = L.map f ≫ b) :
    ∃ (X'' Y'' : C) (f'' : X'' ⟶ Y'')
      (s : X'' ⟶ X) (_ : W s) (t : Y'' ⟶ Y) (_ : W t)
      (g : X'' ⟶ X') (h : Y'' ⟶ Y'),
        s ≫ f = f'' ≫ t ∧ g ≫ f' = f'' ≫ h ∧
        L.map s ≫ a = L.map g ∧
        L.map t ≫ b = L.map h
```

## Tag 04VL, a lemma

[Tag 04VL](https://stacks.math.columbia.edu/tag/04VL) in the Stacks Project.

**`CategoryTheory.MorphismProperty.leftFractionEquivRightFraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Comparison.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Comparison.lean#L68). References: SGA 4½ Etat 0 (2.3.1), “partial”.

> **Stacks 04VL.**
> The category of left fractions `LeftFraction.Localization W` and the category of right
> fractions `(LeftFraction.Localization W.op)ᵒᵖ` of `C` at the multiplicative system `W` are
> canonically equivalent. The equivalence is the one induced by the universal property of the
> localisation: both `LeftFraction.Localization.Q W` and `rightFractionQ W` invert exactly `W`,
> so `Localization.uniq` produces the canonical comparison, compatible with the two
> localisation functors (see `compLeftFractionEquivRightFractionFunctor`).

```lean
noncomputable def leftFractionEquivRightFraction :
    LeftFraction.Localization W ≌ (LeftFraction.Localization W.op)ᵒᵖ
```

**`CategoryTheory.MorphismProperty.compLeftFractionEquivRightFractionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Comparison.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Comparison.lean#L76).

> **Stacks 04VL.** The canonical equivalence of 04VL is *canonical*: it is compatible
> with the two localisation functors out of `C`, i.e. it identifies a morphism written as a
> left fraction with the same morphism written as a right fraction.

```lean
noncomputable def compLeftFractionEquivRightFractionFunctor :
    LeftFraction.Localization.Q W ⋙ (leftFractionEquivRightFraction W).functor ≅
      rightFractionQ W
```

## Tag 05Q8, a definition

[Tag 05Q8](https://stacks.math.columbia.edu/tag/05Q8) in the Stacks Project.

**`CategoryTheory.MorphismProperty.IsSaturated`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Saturated/Defs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Saturated/Defs.lean#L49).

> `W` is a *saturated multiplicative system* when it is a multiplicative system — MS1 together
> with the two Ore conditions MS2 and the two cancellation conditions MS3, i.e. both a left and a
> right calculus of fractions — and satisfies MS4: for composable `f : X ⟶ Y`, `g : Y ⟶ Z`,
> `h : Z ⟶ T`, if `W (f ≫ g)` and `W (g ≫ h)` then `W g`.

```lean
structure IsSaturated (W : MorphismProperty C) : Prop
```

## Tag 05Q9, a lemma

[Tag 05Q9](https://stacks.math.columbia.edu/tag/05Q9) in the Stacks Project.

**`CategoryTheory.MorphismProperty.invertedClosure_eq_satClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean#L172).

> `Ŝ = S'`: a morphism becomes invertible in the localization exactly
> when it has a `W`-partner on each side.

```lean
theorem invertedClosure_eq_satClosure : W.invertedClosure = W.satClosure
```

**`CategoryTheory.MorphismProperty.le_invertedClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean#L180).

> `W ≤ Ŝ`: every morphism of `W` is inverted by `Q`.

```lean
theorem le_invertedClosure : W ≤ W.invertedClosure
```

**`CategoryTheory.MorphismProperty.isSaturated_invertedClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean#L255).

> `Ŝ` is itself a saturated multiplicative system: it has a left and a right calculus of
> fractions and satisfies MS4.

```lean
theorem isSaturated_invertedClosure : IsSaturated W.invertedClosure
```

**`CategoryTheory.MorphismProperty.invertedClosure_le_of_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean#L272).

> `Ŝ` is the *smallest* saturated multiplicative system containing `W`:
> it is contained in every saturated multiplicative system containing `W`.

```lean
theorem invertedClosure_le_of_isSaturated (W' : MorphismProperty C)
    (hW' : IsSaturated W') (hWW' : W ≤ W') : W.invertedClosure ≤ W'
```

**`CategoryTheory.MorphismProperty.IsSaturated.invertedClosure_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/Saturated/Closure.lean#L278).

> If `W` is already saturated then `Ŝ = W`.

```lean
theorem IsSaturated.invertedClosure_eq (hW : IsSaturated W) :
    W.invertedClosure = W
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.27, Tag 04VB](https://stacks.math.columbia.edu/tag/04VB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
