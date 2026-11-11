---
declaration: section
origin: cited
lean: CategoryTheory.ObjectProperty.IsSaturated, CategoryTheory.Functor.isTriangulated_and_isSaturated_kernel, CategoryTheory.Functor.isTriangulated_and_isSaturated_homologicalKernel, StacksBoundedSubcategories.boundedBelow_strictlyFull, StacksBoundedSubcategories.boundedBelow_isTriangulated, StacksBoundedSubcategories.boundedBelow_isSaturated, StacksBoundedSubcategories.boundedAbove_strictlyFull, StacksBoundedSubcategories.boundedAbove_isTriangulated
statement: formalized
proof: formalized
---

# 13.6 Quotients of triangulated categories

Section 13.6 of the Stacks Project, [Tag 05RA](https://stacks.math.columbia.edu/tag/05RA). 11 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05RB, a definition

[Tag 05RB](https://stacks.math.columbia.edu/tag/05RB) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsSaturated`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L156). References: SGA 4½ Etat 0 (2.1.1), “partial”.

> A property `P` of the objects of a category with zero morphisms is *saturated* if whenever
> a biproduct `X ⊞ Y` is isomorphic to an object satisfying `P`, then both `X` and `Y` are
> isomorphic to objects satisfying `P`; equivalently, the objects isomorphic to an object
> satisfying `P` are closed under direct summands. For a pre-triangulated subcategory, this is
> also called being a *thick* subcategory.

```lean
public class IsSaturated : Prop
```

## Tag 05RC, a lemma

[Tag 05RC](https://stacks.math.columbia.edu/tag/05RC) in the Stacks Project.

**`CategoryTheory.Functor.isTriangulated_and_isSaturated_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L328). References: SGA 4½ Etat 0 (2.2), “thickness”.

> Let `F : C ⥤ D` be an exact functor of pre-triangulated categories. The full subcategory of `C`
> spanned by the objects `X` with `F X = 0`, namely `F.kernel`, is a pre-triangulated subcategory of
> `C` which is saturated. It is strictly full (`ObjectProperty.IsClosedUnderIsomorphisms`) without
> any hypothesis on `F`, and it is a triangulated subcategory as soon as `C` is a triangulated
> category, by `CategoryTheory.ObjectProperty.instIsTriangulatedFullSubcategory`.

```lean
theorem isTriangulated_and_isSaturated_kernel (F : C ⥤ D) [F.CommShift ℤ]
    [F.IsTriangulated] :
    F.kernel.IsTriangulated ∧ F.kernel.IsSaturated
```

## Tag 05RD, a lemma

[Tag 05RD](https://stacks.math.columbia.edu/tag/05RD) in the Stacks Project.

**`CategoryTheory.Functor.isTriangulated_and_isSaturated_homologicalKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L356). References: SGA 4½ Etat 0 (2.4.1), “thickness”.

> Let `H : C ⥤ A` be a homological functor from a pre-triangulated category to an abelian
> category. The full subcategory of `C` spanned by the objects `X` with `H (X⟦n⟧) = 0` for all
> `n : ℤ`, namely `H.homologicalKernel`, is a pre-triangulated subcategory of `C` which is saturated.
> It is strictly full (`ObjectProperty.IsClosedUnderIsomorphisms`), and it is a triangulated
> subcategory as soon as `C` is a triangulated category, by
> `CategoryTheory.ObjectProperty.instIsTriangulatedFullSubcategory`.

```lean
theorem isTriangulated_and_isSaturated_homologicalKernel (H : C ⥤ A) [H.IsHomological] :
    H.homologicalKernel.IsTriangulated ∧ H.homologicalKernel.IsSaturated
```

## Tag 05RE, a lemma

[Tag 05RE](https://stacks.math.columbia.edu/tag/05RE) in the Stacks Project.

**`StacksBoundedSubcategories.boundedBelow_strictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 981](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L981). The attribute's comment: “D\_H^+ strictly full”.

> The property `D_H^+` of being `H`-bounded below is closed under isomorphisms.

```lean
theorem boundedBelow_strictlyFull (H : D ⥤ A) [H.IsHomological] :
    (boundedBelow H).IsClosedUnderIsomorphisms
```

**`StacksBoundedSubcategories.boundedBelow_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 990](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L990). The attribute's comment: “D\_H^+ pre-triangulated”. References: SGA 4½ Etat 0 (1.2.3), “more general”; SGA 6 I (1.1.5), “more general”.

> `D_H^+` is a pre-triangulated subcategory: it contains a zero object, is stable under every
> shift `[n]`, and is closed under cones of distinguished triangles with two vertices in `D_H^+`.

```lean
theorem boundedBelow_isTriangulated (H : D ⥤ A) [H.IsHomological]
    [H.ShiftSequence ℤ] :
    (boundedBelow H).IsTriangulated
```

**`StacksBoundedSubcategories.boundedBelow_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1000](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1000). The attribute's comment: “D\_H^+ saturated”.

> `D_H^+` is saturated: if `X ⊞ Y` is bounded below then so are `X` and `Y`, each being a retract
> of the biproduct.

```lean
theorem boundedBelow_isSaturated (H : D ⥤ A) [H.IsHomological] :
    IsSaturated (boundedBelow H)
```

**`StacksBoundedSubcategories.boundedAbove_strictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1007](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1007). The attribute's comment: “D\_H^- strictly full”.

> The property `D_H^-` of being `H`-bounded above is closed under isomorphisms.

```lean
theorem boundedAbove_strictlyFull (H : D ⥤ A) [H.IsHomological] :
    (boundedAbove H).IsClosedUnderIsomorphisms
```

**`StacksBoundedSubcategories.boundedAbove_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1016](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1016). The attribute's comment: “D\_H^- pre-triangulated”. References: SGA 4½ Etat 0 (1.2.3), “more general”; SGA 6 I (1.1.5), “more general”.

> `D_H^-` is a pre-triangulated subcategory: it contains a zero object, is stable under every
> shift `[n]`, and is closed under cones of distinguished triangles with two vertices in `D_H^-`.

```lean
theorem boundedAbove_isTriangulated (H : D ⥤ A) [H.IsHomological]
    [H.ShiftSequence ℤ] :
    (boundedAbove H).IsTriangulated
```

**`StacksBoundedSubcategories.boundedAbove_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1026](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1026). The attribute's comment: “D\_H^- saturated”.

> `D_H^-` is saturated: if `X ⊞ Y` is bounded above then so are `X` and `Y`, each being a retract
> of the biproduct.

```lean
theorem boundedAbove_isSaturated (H : D ⥤ A) [H.IsHomological] :
    IsSaturated (boundedAbove H)
```

**`StacksBoundedSubcategories.bounded_strictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1033). The attribute's comment: “D\_H^b strictly full”.

> The property `D_H^b` of being `H`-bounded is closed under isomorphisms.

```lean
theorem bounded_strictlyFull (H : D ⥤ A) [H.IsHomological] :
    (bounded H).IsClosedUnderIsomorphisms
```

**`StacksBoundedSubcategories.bounded_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1042](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1042). The attribute's comment: “D\_H^b pre-triangulated”. References: SGA 4½ Etat 0 (1.2.3), “more general”; SGA 6 I (1.1.5), “more general”.

> `D_H^b` is a pre-triangulated subcategory: it contains a zero object, is stable under every
> shift `[n]`, and is closed under cones of distinguished triangles with two vertices in `D_H^b`.

```lean
theorem bounded_isTriangulated (H : D ⥤ A) [H.IsHomological]
    [H.ShiftSequence ℤ] :
    (bounded H).IsTriangulated
```

**`StacksBoundedSubcategories.bounded_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1054](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1054). The attribute's comment: “D\_H^b saturated”.

> `D_H^b` is saturated: if `X ⊞ Y` is bounded then so are `X` and `Y`, each being a retract of
> the biproduct.

```lean
theorem bounded_isSaturated (H : D ⥤ A) [H.IsHomological] :
    IsSaturated (bounded H)
```

## Tag 05RF, a definition

[Tag 05RF](https://stacks.math.columbia.edu/tag/05RF) in the Stacks Project.

**`CategoryTheory.Functor.homologicalKernel_eq_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L381).

> The kernel of a functor `F` commuting with the shift by `ℤ`, described as in [Stacks, Tag 05RD]
> by the vanishing of `F (X⟦n⟧)` for all `n : ℤ`, is described as in [Stacks, Tag 05RC] by the
> vanishing of `F X`: the homological kernel and the kernel of such a functor — in particular of an
> exact functor of pre-triangulated categories — are the same strictly full subcategory of `C`.

```lean
public theorem homologicalKernel_eq_kernel (F : C ⥤ D) [F.CommShift ℤ] :
    F.homologicalKernel = F.kernel
```

## Tag 05RG, a lemma

[Tag 05RG](https://stacks.math.columbia.edu/tag/05RG) in the Stacks Project.

**`CategoryTheory.ObjectProperty.hasCalculusOfFractions_isCompatibleWithTriangulation_and_isSaturated_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L495). References: SGA 4½ Etat 0 (2.2), “S=φ(B) sat. mult. system”; SGA 4½ Etat 0 (2.3.1), “special case”.

> Let `C` be a triangulated category, let `P` be a full triangulated subcategory of `C`, and let
> `S` be the class of morphisms `f` that fit into a distinguished triangle `(X, Y, Z, f, g, h)` with
> `Z` isomorphic to an object of `P`. Then `S` is a multiplicative system (MS1, MS2, MS3, i.e. a left
> and a right calculus of fractions) compatible with the triangulated structure on `C` (MS5, MS6),
> and `S` is a saturated multiplicative system ([Stacks, Tag 05Q8]) if and only if `P` is saturated
> ([Stacks, Tag 05RB]).

```lean
theorem hasCalculusOfFractions_isCompatibleWithTriangulation_and_isSaturated_iff
    (P : ObjectProperty C) [P.IsTriangulated] (S : MorphismProperty C)
    (hS : ∀ ⦃X Y : C⦄ (f : X ⟶ Y), S f ↔ ∃ (Z : C) (g : Y ⟶ Z) (h : Z ⟶ X⟦(1 : ℤ)⟧),
      Triangle.mk f g h ∈ distTriang C ∧ P.isoClosure Z) :
    (S.HasLeftCalculusOfFractions ∧ S.HasRightCalculusOfFractions ∧
      S.IsCompatibleWithTriangulation) ∧ (S.IsSaturated ↔ P.IsSaturated)
```

## Tag 05RI, a definition

[Tag 05RI](https://stacks.math.columbia.edu/tag/05RI) in the Stacks Project.

**`CategoryTheory.ObjectProperty.verdierQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L553). References: SGA 4½ Etat 0 (2.3.3); SGA 4½ Etat 0 (2.5); SGA 4½ Etat 0 (Problem1); SGA 4½ Etat 0 (Problem2).

> The *quotient category* `C/P` of a pretriangulated category `C` by a subcategory
> `P : ObjectProperty C`: the localization `S⁻¹C` of `C` at the class `S = P.trW` of morphisms whose
> cone lies in `P`, which for `P` a full triangulated subcategory of a triangulated category is a
> multiplicative system ([Stacks, Tag 05RG]). The *quotient functor* `Q : C ⥤ C/P` is the
> localization functor `P.trW.Q` of this localization.
>
> In that triangulated situation this is the Verdier quotient: `C/P` is then triangulated and the
> quotient functor is exact ([Stacks, Tag 05R6]).

```lean
public abbrev verdierQuotient (P : ObjectProperty C) : Type u
```

## Tag 05RJ, a lemma

[Tag 05RJ](https://stacks.math.columbia.edu/tag/05RJ) in the Stacks Project.

**`VerdierQuotientUniversalProperty.homological_universal_property`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1133). The attribute's comment: “(1)”. References: SGA 4½ Etat 0 (2.4.1), “more general”.

> **Universal property of the Verdier quotient for homological functors**.
>
> Let `C` be a triangulated category, `P` a full triangulated subcategory (an
> `ObjectProperty` with `P.IsTriangulated`), and `Q = P.trW.Q : C ⥤ C / P` the Verdier
> quotient functor. Let `A` be abelian and `H : C ⥤ A` a homological functor whose
> homological kernel contains `P` (this is the hypothesis `B ⊆ Ker(H)`). Then:
>
> * **Existence + structure**: there is a functor `H' : C / P ⥤ A` together with a natural
>   isomorphism `fac : Q ⋙ H' ≅ H` (the factorization `H = H' ∘ Q`), and `H'` is again
>   homological.
> * **Uniqueness (up to unique natural isomorphism)**: for any functor `G : C / P ⥤ A`
>   equipped with a natural isomorphism `α : Q ⋙ G ≅ H`, there is a *unique* natural
>   isomorphism `e : G ≅ H'` compatible with the factorization isomorphisms, i.e. such that
>   `whiskerLeft Q e.hom ≫ fac.hom = α.hom`.

```lean
theorem homological_universal_property
    {C A : Type*} [Category C] [Preadditive C] [HasZeroObject C] [HasShift C ℤ]
    [∀ n : ℤ, (shiftFunctor C n).Additive] [Pretriangulated C] [IsTriangulated C]
    [Category A] [Abelian A]
    (P : ObjectProperty C) [P.IsTriangulated]
    (H : C ⥤ A) [H.IsHomological]
    (hker : P ≤ H.homologicalKernel) :
    ∃ (H' : P.trW.Localization ⥤ A) (fac : P.trW.Q ⋙ H' ≅ H),
      H'.IsHomological ∧
      ∀ (G : P.trW.Localization ⥤ A) (α : P.trW.Q ⋙ G ≅ H),
        ∃! e : G ≅ H', Functor.whiskerLeft P.trW.Q e.hom ≫ fac.hom = α.hom
```

**`VerdierQuotientUniversalProperty.exact_universal_property`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 1207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L1207). The attribute's comment: “(2)”. References: SGA 4½ Etat 0 (Problem1); SGA 4½ Etat 0 (2.2), “partial”; SGA 4½ Etat 0 (2.3.2), “(A\_S”; SGA 4½ Etat 0 (2.3.3), “more general”; SGA 4½ Etat 0 (4.2.3), “(b)”; SGA 4½ Etat 0 (Problem2), “partial”.

> **Universal property of the Verdier quotient for exact (triangulated) functors**.
>
> Let `C` be a triangulated category, `P` a full triangulated subcategory, and
> `Q = P.trW.Q : C ⥤ C / P` the Verdier quotient functor. Let `D'` be pretriangulated and
> `F : C ⥤ D'` an exact (triangulated) functor: it is additive (`F.Additive`), commutes
> with the shift (`F.CommShift ℤ`), and sends distinguished triangles to distinguished
> triangles (`F.IsTriangulated`). Assume its kernel contains `P`, i.e. `F` sends every
> object of `P` to a zero object (the hypothesis `B ⊆ Ker(F)`). Then:
>
> * **Existence + structure**: there is a functor `F' : C / P ⥤ D'` equipped with a
>   `CommShift ℤ` structure, a natural isomorphism `fac : Q ⋙ F' ≅ F` (the factorization
>   `F = F' ∘ Q`) which commutes with the shift structures on both sides
>   (`NatTrans.CommShift fac.hom ℤ`), and `F'` is again additive (`F'.Additive`) and
>   exact/triangulated (`F'.IsTriangulated`).
> * **Uniqueness (up to unique natural isomorphism)**: for any functor `G : C / P ⥤ D'`
>   equipped with a natural isomorphism `α : Q ⋙ G ≅ F`, there is a *unique* natural
>   isomorphism `e : G ≅ F'` compatible with the factorization isomorphisms, i.e. such that
>   `whiskerLeft Q e.hom ≫ fac.hom = α.hom`.

```lean
theorem exact_universal_property
    {C D' : Type*} [Category C] [Preadditive C] [HasZeroObject C] [HasShift C ℤ]
    [∀ n : ℤ, (shiftFunctor C n).Additive] [Pretriangulated C] [IsTriangulated C]
    [Category D'] [Preadditive D'] [HasZeroObject D'] [HasShift D' ℤ]
    [∀ n : ℤ, (shiftFunctor D' n).Additive] [Pretriangulated D']
    (P : ObjectProperty C) [P.IsTriangulated]
    (F : C ⥤ D') [F.Additive] [F.CommShift ℤ] [F.IsTriangulated]
    (hker : ∀ X, P X → IsZero (F.obj X)) :
    ∃ (F' : P.trW.Localization ⥤ D') (_ : F'.CommShift ℤ) (fac : P.trW.Q ⋙ F' ≅ F)
      (_ : NatTrans.CommShift fac.hom ℤ),
      F'.Additive ∧ F'.IsTriangulated ∧
      ∀ (G : P.trW.Localization ⥤ D') (α : P.trW.Q ⋙ G ≅ F),
        ∃! e : G ≅ F', Functor.whiskerLeft P.trW.Q e.hom ≫ fac.hom = α.hom
```

## Tag 05RK, a lemma

[Tag 05RK](https://stacks.math.columbia.edu/tag/05RK) in the Stacks Project.

**`CategoryTheory.ObjectProperty.kernel_iff_exists_isoClosure_biprod_and_isLeast_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L614).

> Let `C` be a triangulated category, let `P` be a full triangulated subcategory of `C` and let
> `L : C ⥤ D` be a localization of `C` at the class `P.trW` of morphisms whose cone lies in `P`, i.e.
> a quotient functor `C ⥤ C/P` ([Stacks, Tag 05RI]). Then an object `Z` of `C` lies in the kernel of
> `L` if and only if there is an object `Z'` such that `Z ⊞ Z'` is isomorphic to an object of `P`;
> and the kernel of `L` is the smallest strictly full saturated ([Stacks, Tag 05RB]) triangulated
> subcategory of `C` containing `P`.

```lean
theorem kernel_iff_exists_isoClosure_biprod_and_isLeast_kernel
    (P : ObjectProperty C) [P.IsTriangulated] (L : C ⥤ D) [L.IsLocalization P.trW] :
    (∀ Z : C, L.kernel Z ↔ ∃ Z' : C, P.isoClosure (Z ⊞ Z')) ∧
      IsLeast {P' : ObjectProperty C | P'.IsClosedUnderIsomorphisms ∧ P'.IsTriangulated ∧
        P'.IsSaturated ∧ P ≤ P'} L.kernel
```

## Tag 05RL, a lemma

[Tag 05RL](https://stacks.math.columbia.edu/tag/05RL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isLeast_trW_kernel_and_kernel_eq_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 708](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L708).

> Let `C` be a triangulated category. Passing from a multiplicative system `S` compatible with
> the triangulated structure to the kernel `B(S)` of a localization of `C` at `S`, and from a full
> triangulated subcategory `P` to the class `S(P) = P.trW` of morphisms whose cone lies in `P`, one
> has:
>
> * `S(B(S))` is the *saturation* of `S`: the smallest saturated multiplicative system
>   ([Stacks, Tag 05Q8]) of `C` containing `S`;
> * if `P` is a strictly full saturated ([Stacks, Tag 05RB]) triangulated subcategory, then
>   `B(S(P)) = P`.
>
> Together with [Stacks, Tag 05RK] — which says that `B(S(P))` is in general the smallest strictly
> full saturated triangulated subcategory containing `P` — this says that the two constructions are
> mutually inverse, order preserving bijections between the saturated multiplicative systems of `C`
> compatible with the triangulated structure and the strictly full saturated triangulated
> subcategories of `C`.

```lean
theorem isLeast_trW_kernel_and_kernel_eq_self :
    (∀ (S : MorphismProperty C) [S.HasLeftCalculusOfFractions]
        [S.HasRightCalculusOfFractions] [S.IsCompatibleWithTriangulation]
        (L : C ⥤ D) [L.IsLocalization S],
      IsLeast {S' : MorphismProperty C | S'.IsSaturated ∧ S ≤ S'} L.kernel.trW) ∧
    (∀ (P : ObjectProperty C) [P.IsTriangulated] [P.IsClosedUnderIsomorphisms] [P.IsSaturated]
        (L : C ⥤ D) [L.IsLocalization P.trW],
      L.kernel = P)
```

## Tag 05RM, a lemma

[Tag 05RM](https://stacks.math.columbia.edu/tag/05RM) in the Stacks Project.

**`CategoryTheory.Functor.isSaturated_homologicalKernel_and_mem_trW_iff_and_exists_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/Quotient.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/Quotient.lean#L807). References: SGA 4½ Etat 0 (2.4.1); SGA 4½ Etat 0 (3.1.6), “factors through quotient”.

> Let `H : C ⥤ A` be a homological functor from a triangulated category to an abelian category,
> write `Hⁱ = H(-⟦i⟧)`, and let `L : C ⥤ D` be a localization of `C` at the class of morphisms whose
> cone lies in the kernel of `H`. Then:
>
> * `Ker(H)` is a strictly full saturated ([Stacks, Tag 05RB]) triangulated subcategory of `C`;
> * the multiplicative system attached to it by [Stacks, Tag 05RL] is saturated ([Stacks, Tag 05Q8]),
>   compatible with the triangulated structure, and is the class
>   `S = {f ∣ Hⁱ(f) is an isomorphism for all i ∈ ℤ}`;
> * `H` factors through `L`, and so does every `Hⁱ`.

```lean
theorem isSaturated_homologicalKernel_and_mem_trW_iff_and_exists_lift
    (H : C ⥤ A) [H.IsHomological] (L : C ⥤ D)
    [L.IsLocalization H.homologicalKernel.trW] :
    (H.homologicalKernel.IsClosedUnderIsomorphisms ∧ H.homologicalKernel.IsTriangulated ∧
        H.homologicalKernel.IsSaturated) ∧
      (H.homologicalKernel.trW.IsSaturated ∧
          H.homologicalKernel.trW.IsCompatibleWithTriangulation ∧
          ∀ ⦃X Y : C⦄ (f : X ⟶ Y),
            H.homologicalKernel.trW f ↔ ∀ i : ℤ, IsIso (H.map (f⟦i⟧'))) ∧
      (∃ H' : D ⥤ A, Nonempty (L ⋙ H' ≅ H)) ∧
      ∀ i : ℤ, ∃ H' : D ⥤ A, Nonempty (L ⋙ H' ≅ shiftFunctor C i ⋙ H)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.6, Tag 05RA](https://stacks.math.columbia.edu/tag/05RA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
