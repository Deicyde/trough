---
declaration: section
origin: cited
lean: Stacks.Triangulated.RightOrthogonal.inRightOrthogonal_iff_postcomp_bijective, Stacks.Triangulated.AdmissibleSubcategories.isLeftOrthogonal_iff_bijective_precompMap, CategoryTheory.ObjectProperty.isStableUnderRetracts_rightOrthogonal_and_leftOrthogonal, CategoryTheory.ObjectProperty.isTriangulated_extensionProduct_of_le_rightOrthogonal, CategoryTheory.ObjectProperty.isTriangulated_extensionProduct_leftOrthogonal_self, CategoryTheory.ObjectProperty.isLeftAdjoint_ι_iff_extensionProduct_rightOrthogonal_eq_top_and_isSaturated, CategoryTheory.ObjectProperty.isRightAdjoint_ι_iff_extensionProduct_leftOrthogonal_self_eq_top_and_isSaturated, CategoryTheory.ObjectProperty.IsRightAdmissible
statement: formalized
proof: formalized
---

# 13.40 Admissible subcategories

Section 13.40 of the Stacks Project, [Tag 0CQP](https://stacks.math.columbia.edu/tag/0CQP). 9 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CQQ, a lemma

[Tag 0CQQ](https://stacks.math.columbia.edu/tag/0CQQ) in the Stacks Project.

**`Stacks.Triangulated.RightOrthogonal.inRightOrthogonal_iff_postcomp_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L1012).

> Stacks Tag 0CQQ / Lemma 13.40.2.
>
> Let `A ⊆ D` (described by `P`) be a full subcategory invariant under all shifts
> (up to isomorphism), and let `X --f--> Y --g--> Z --h--> X[1]` be a distinguished
> triangle. Then `Z` is in the right orthogonal `Aᗮ` if and only if, for every
> object `A` of `A`, the map `f_* : Hom(A, X) → Hom(A, Y)`, `g ↦ g ≫ f`, is an
> isomorphism of abelian groups (here expressed as a bijection).
>
> Proof outline (as in the source), applying the homological functor `Hom(A,-)`:
> * `(1) ⇒ (2)`: injectivity of `f_*` uses the inverse-rotated triangle
>   `Z⟦-1⟧ → X → Y` and `coyoneda_exact₂`: a kernel element factors through
>   `Z⟦-1⟧`, which vanishes by `hom_to_shift_eq_zero`; surjectivity uses
>   `coyoneda_exact₂` on `T` since `u ≫ g = 0` for any `u : A ⟶ Y` (as `Z ∈ Aᗮ`).
> * `(2) ⇒ (1)`: for `u : A ⟶ Z`, first `u ≫ h = 0` by injectivity of `· ≫ f⟦1⟧`
>   (Helper 3 and `bijective_postcomp_shift` transport bijectivity to `Hom(A, X⟦1⟧)`) together with
>   `comp_distTriang_mor_zero₂₃` on the rotated triangle; then `coyoneda_exact₂` on
>   the rotated triangle factors `u = v ≫ g`, surjectivity of `f_*` gives `v = w ≫ f`,
>   and `f ≫ g = 0` yields `u = w ≫ (f ≫ g) = 0`.

```lean
theorem inRightOrthogonal_iff_postcomp_bijective
    (P : C → Prop) (hP : InvariantUnderAllShifts P)
    (T : Triangle C) (hT : T ∈ distinguishedTriangles) :
    InRightOrthogonal P T.obj₃ ↔
      ∀ (A : C), P A → Function.Bijective (fun g : A ⟶ T.obj₁ => g ≫ T.mor₁)
```

## Tag 0H0M, a lemma

[Tag 0H0M](https://stacks.math.columbia.edu/tag/0H0M) in the Stacks Project.

**`Stacks.Triangulated.AdmissibleSubcategories.isLeftOrthogonal_iff_bijective_precompMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 1245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L1245).

> **Theorem (Stacks Tag 0H0M, Lemma 13.40.3).**
> Let `B ⊂ D` be a full subcategory invariant under all shifts, and let
> `X --f--> Y --g--> Z --h--> X[1]` be a distinguished triangle. Then `X` lies in the left
> orthogonal `ᗮB` if and only if, for every object `B` of `B`, the precomposition map
> `g* : Hom_D(Z, B) → Hom_D(Y, B)` is bijective.

```lean
theorem isLeftOrthogonal_iff_bijective_precompMap
    (B : D → Prop) (hB : ShiftInvariant B)
    (T : Triangle D) (hT : T ∈ distinguishedTriangles) :
    IsLeftOrthogonal B T.obj₁ ↔
      ∀ (b : D), B b → Function.Bijective (precompMap T b)
```

## Tag 0FXC, a lemma

[Tag 0FXC](https://stacks.math.columbia.edu/tag/0FXC) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isStableUnderRetracts_rightOrthogonal_and_leftOrthogonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L158). References: SGA 4½ Etat 0 (2.6.2), “thickness”.

> Let `C` be a category with zero morphisms and `P : ObjectProperty C` a property of its
> objects. Then both the right orthogonal `P.rightOrthogonal` and the left orthogonal
> `P.leftOrthogonal` are stable under retracts; in particular they are saturated, i.e. thick, and
> strictly full subcategories of `C`.

```lean
theorem isStableUnderRetracts_rightOrthogonal_and_leftOrthogonal (P : ObjectProperty C) :
    P.rightOrthogonal.IsStableUnderRetracts ∧ P.leftOrthogonal.IsStableUnderRetracts
```

## Tag 0CQR, a lemma

[Tag 0CQR](https://stacks.math.columbia.edu/tag/0CQR) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isTriangulated_extensionProduct_of_le_rightOrthogonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L580).

> Let `C` be a triangulated category, let `A` and `B` be triangulated subcategories of `C`
> with `B` contained in the right orthogonal of `A`. Then the objects `X` of `C` that fit in a
> distinguished triangle `A' ⟶ X ⟶ B' ⟶ A'⟦1⟧` with `A'` in `A` and `B'` in `B` form a
> triangulated subcategory of `C`: they are stable under shifts, two out of three of them in a
> distinguished triangle forces the third, and they are stable under direct sums. For
> `B = A.rightOrthogonal` this is the property `P` of [Stacks, Tag 0CQR].

```lean
theorem isTriangulated_extensionProduct_of_le_rightOrthogonal
    (A B : ObjectProperty C) [A.IsTriangulated] [B.IsTriangulated]
    (hB : B ≤ A.rightOrthogonal) :
    (A.extensionProduct B).IsTriangulated
```

## Tag 0H0N, a lemma

[Tag 0H0N](https://stacks.math.columbia.edu/tag/0H0N) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isTriangulated_extensionProduct_leftOrthogonal_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 599](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L599).

> Let `C` be a triangulated category and let `B` be a triangulated subcategory of `C`. Then
> the objects `X` of `C` that fit in a distinguished triangle `A ⟶ X ⟶ B' ⟶ A⟦1⟧` with `A` in the
> left orthogonal of `B` and `B'` in `B` form a triangulated subcategory of `C`: they are stable
> under shifts, two out of three of them in a distinguished triangle forces the third, and they are
> stable under direct sums. This is the property `P` of [Stacks, Tag 0H0N].

```lean
theorem isTriangulated_extensionProduct_leftOrthogonal_self (B : ObjectProperty C)
    [B.IsTriangulated] :
    (B.leftOrthogonal.extensionProduct B).IsTriangulated
```

## Tag 0CQS, a lemma

[Tag 0CQS](https://stacks.math.columbia.edu/tag/0CQS) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isLeftAdjoint_ι_iff_extensionProduct_rightOrthogonal_eq_top_and_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L342).

> Let `C` be a pretriangulated category and let `A : ObjectProperty C` be invariant under all
> shifts, for instance a triangulated subcategory of `C`. Then the inclusion
> `A.ι : A.FullSubcategory ⥤ C` has a right adjoint if and only if every object `X` of `C` fits in
> a distinguished triangle `A' ⟶ X ⟶ B ⟶ A'⟦1⟧` with `A'` satisfying `A` and `B` in the right
> orthogonal of `A`, i.e. if and only if `A.extensionProduct A.rightOrthogonal = ⊤`; and in that
> case `A` is saturated, i.e. thick ([Stacks, Tag 05RB]), and the objects isomorphic to an object
> satisfying `A` are exactly the objects of the left orthogonal of `A.rightOrthogonal`, so a
> strictly full such `A` satisfies `A = ᗮ(Aᗮ)`.

```lean
theorem isLeftAdjoint_ι_iff_extensionProduct_rightOrthogonal_eq_top_and_isSaturated
    (A : ObjectProperty C) [A.IsStableUnderShift ℤ] :
    (A.ι.IsLeftAdjoint ↔ A.extensionProduct A.rightOrthogonal = ⊤) ∧
      (A.extensionProduct A.rightOrthogonal = ⊤ →
        A.IsSaturated ∧ A.isoClosure = A.rightOrthogonal.leftOrthogonal)
```

## Tag 0CQT, a lemma

[Tag 0CQT](https://stacks.math.columbia.edu/tag/0CQT) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isRightAdjoint_ι_iff_extensionProduct_leftOrthogonal_self_eq_top_and_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L484).

> Let `C` be a pretriangulated category and let `B : ObjectProperty C` be invariant under all
> shifts, for instance a triangulated subcategory of `C`. Then the inclusion
> `B.ι : B.FullSubcategory ⥤ C` has a left adjoint if and only if every object `X` of `C` fits in a
> distinguished triangle `A ⟶ X ⟶ B' ⟶ A⟦1⟧` with `A` in the left orthogonal of `B` and `B'`
> satisfying `B`, i.e. if and only if `B.leftOrthogonal.extensionProduct B = ⊤`; and in that case
> `B` is saturated, i.e. thick ([Stacks, Tag 05RB]), and the objects isomorphic to an object
> satisfying `B` are exactly the objects of the right orthogonal of `B.leftOrthogonal`, so a
> strictly full such `B` satisfies `B = (ᗮB)ᗮ`.

```lean
theorem isRightAdjoint_ι_iff_extensionProduct_leftOrthogonal_self_eq_top_and_isSaturated
    (B : ObjectProperty C) [B.IsStableUnderShift ℤ] :
    (B.ι.IsRightAdjoint ↔ B.leftOrthogonal.extensionProduct B = ⊤) ∧
      (B.leftOrthogonal.extensionProduct B = ⊤ →
        B.IsSaturated ∧ B.isoClosure = B.leftOrthogonal.rightOrthogonal)
```

## Tag 0FXD, a definition

[Tag 0FXD](https://stacks.math.columbia.edu/tag/0FXD) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsRightAdmissible`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L271).

> A property `A` of the objects of a pretriangulated category `C` is *right admissible* if it is
> strictly full (closed under isomorphisms) and triangulated, and the inclusion
> `A.ι : A.FullSubcategory ⥤ C` has a right adjoint. By [Stacks, Tag 0CQS] the last condition holds
> if and only if every object `X` of `C` fits in a distinguished triangle `A' ⟶ X ⟶ B ⟶ A'⟦1⟧` with
> `A'` satisfying `A` and `B` in the right orthogonal of `A`, and it then forces `A = ᗮ(Aᗮ)`.

```lean
public class IsRightAdmissible (A : ObjectProperty C) : Prop extends
  A.IsClosedUnderIsomorphisms, A.IsTriangulated, A.ι.IsLeftAdjoint
```

**`CategoryTheory.ObjectProperty.IsLeftAdmissible`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L280).

> A property `A` of the objects of a pretriangulated category `C` is *left admissible* if it is
> strictly full (closed under isomorphisms) and triangulated, and the inclusion
> `A.ι : A.FullSubcategory ⥤ C` has a left adjoint. By [Stacks, Tag 0CQT] the last condition holds
> if and only if every object `X` of `C` fits in a distinguished triangle `A' ⟶ X ⟶ B ⟶ A'⟦1⟧` with
> `A'` in the left orthogonal of `A` and `B` satisfying `A`, and it then forces `A = (ᗮA)ᗮ`.

```lean
public class IsLeftAdmissible (A : ObjectProperty C) : Prop extends
  A.IsClosedUnderIsomorphisms, A.IsTriangulated, A.ι.IsRightAdjoint
```

**`CategoryTheory.ObjectProperty.IsTwoSidedAdmissible`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L287).

> A property `A` of the objects of a pretriangulated category `C` is *two-sided admissible* if
> it is both right and left admissible, i.e. `A` is a strictly full triangulated subcategory whose
> inclusion `A.ι : A.FullSubcategory ⥤ C` has both a right and a left adjoint.

```lean
public class IsTwoSidedAdmissible (A : ObjectProperty C) : Prop extends
  A.IsRightAdmissible, A.IsLeftAdmissible
```

## Tag 0H0P, a proposition

[Tag 0H0P](https://stacks.math.columbia.edu/tag/0H0P) in the Stacks Project.

**`CategoryTheory.ObjectProperty.tfae_isRightAdmissible_isLeftAdmissible_extensionProduct_and_isEquivalence_ι_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean, line 820](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Triangulated/AdmissibleSubcategories.lean#L820). References: SGA 4½ Etat 0 (2.6.6).

> Let `C` be a triangulated category and let `A B : ObjectProperty C` be strictly full and
> invariant under all shifts. Then: `A` is right admissible with `B = Aᗮ` if and only if `B` is left
> admissible with `A = ᗮB` if and only if `Hom(A', B') = 0` for `A'` in `A` and `B'` in `B` and every
> object `X` of `C` fits in a distinguished triangle `A' ⟶ X ⟶ B' ⟶ A'⟦1⟧` with `A' ∈ A`, `B' ∈ B`.
> If this holds, then for every Verdier quotient `L : C ⥤ Q` of `C` by `B`, i.e. every localization
> of `C` at `B.trW`, the composite `A.ι ⋙ L : A ⥤ Q` is an equivalence and a right adjoint of the
> inclusion `A.ι` is `L ⋙ G` for some `G : Q ⥤ A`, necessarily a quasi-inverse of `A.ι ⋙ L`; and
> dually for the Verdier quotient of `C` by `A`, the inclusion `B.ι` and its left adjoint.

```lean
theorem tfae_isRightAdmissible_isLeftAdmissible_extensionProduct_and_isEquivalence_ι_comp
    (A B : ObjectProperty C) [A.IsClosedUnderIsomorphisms] [B.IsClosedUnderIsomorphisms]
    [A.IsStableUnderShift ℤ] [B.IsStableUnderShift ℤ] :
    [A.IsRightAdmissible ∧ B = A.rightOrthogonal,
      B.IsLeftAdmissible ∧ A = B.leftOrthogonal,
      A ≤ B.leftOrthogonal ∧ A.extensionProduct B = ⊤].TFAE ∧
    (A ≤ B.leftOrthogonal → A.extensionProduct B = ⊤ →
      (∀ {Q : Type w} [Category.{w'} Q] (L : C ⥤ Q) [L.IsLocalization B.trW],
          (A.ι ⋙ L).IsEquivalence ∧
            ∃ G : Q ⥤ A.FullSubcategory, Nonempty (A.ι ⊣ L ⋙ G)) ∧
      (∀ {Q : Type w} [Category.{w'} Q] (L : C ⥤ Q) [L.IsLocalization A.trW],
          (B.ι ⋙ L).IsEquivalence ∧
            ∃ G : Q ⥤ B.FullSubcategory, Nonempty (L ⋙ G ⊣ B.ι)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.40, Tag 0CQP](https://stacks.math.columbia.edu/tag/0CQP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
