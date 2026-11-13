---
declaration: section
origin: cited
lean: AlgebraicGeometry.DescentData.sheafEquivalence, AlgebraicGeometry.DescentData.representableBy_sheafEquivalence_functor, AlgebraicGeometry.DescentData.representableBy_sheafEquivalence_inverse, AlgebraicGeometry.DescentData.isRepresentable_sheafEquivalence_functor_iff, AlgebraicGeometry.DescentData.isRepresentable_iff_isFamilyEffective_sheafEquivalence_inverse, CategoryTheory.isRepresentable_overMap_iff
statement: formalized
proof: formalized
---

# 35.39 Descent data in terms of sheaves

Section 35.39 of the Stacks Project, [Tag 02W4](https://stacks.math.columbia.edu/tag/02W4). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02W5, a lemma

[Tag 02W5](https://stacks.math.columbia.edu/tag/02W5) in the Stacks Project.

**`AlgebraicGeometry.DescentData.sheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean, line 1059](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean#L1059). The attribute's comment: “the equivalence of categories”.

> **Stacks 02W5.** Let `J` be a subcanonical topology on the category of schemes (for instance
> the Zariski, étale, smooth, syntomic or fppf topology), let `S` be a scheme and let
> `{f i : X i ⟶ S}` be a `J`-covering of `S`. Then descent data `(V_i, φ_ij)` of schemes relative to
> `{f i}` are equivalent to sheaves `F` on `(Sch/S)_J` such that every product `h_{X i} × F` is
> representable. The functor sends `D` to the sheaf `T ↦ Hom(can T, D)` of morphisms of descent
> data out of the canonical descent datum of `T`.

```lean
noncomputable def sheafEquivalence :
    DescentData f ≌ (sheavesLocallyRepresentable J f).FullSubcategory
```

**`AlgebraicGeometry.DescentData.representableBy_sheafEquivalence_functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean, line 1072](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean#L1072). The attribute's comment: “part (1): the objects representing `h_{S_i} × F` are the schemes `X_i`”.

> **Stacks 02W5, part (1)**, from left to right: for a descent datum `(V_i, φ_ij)`, the product
> `h_{X i} × F` with the corresponding sheaf `F` is represented by `V_i`, viewed as a scheme over
> `S`.

```lean
noncomputable def representableBy_sheafEquivalence_functor (D : DescentData f) (i : ι) :
    (yoneda.obj (Over.mk (f i)) ⨯ ((sheafEquivalence hf).functor.obj D).obj.obj).RepresentableBy
      ((Over.map (f i)).obj (D.obj i))
```

**`AlgebraicGeometry.DescentData.representableBy_sheafEquivalence_inverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean, line 1081](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean#L1081). The attribute's comment: “part (1), from sheaves to descent data”.

> **Stacks 02W5, part (1)**, from right to left: for a sheaf `F` on `(Sch/S)_J` with every
> `h_{X i} × F` representable, the product `h_{X i} × F` is represented by the `i`-th component of
> the corresponding descent datum, viewed as a scheme over `S`.

```lean
noncomputable def representableBy_sheafEquivalence_inverse
    (F : (sheavesLocallyRepresentable J f).FullSubcategory) (i : ι) :
    (yoneda.obj (Over.mk (f i)) ⨯ F.obj.obj).RepresentableBy
      ((Over.map (f i)).obj (((sheafEquivalence hf).inverse.obj F).obj i))
```

**`AlgebraicGeometry.DescentData.isRepresentable_sheafEquivalence_functor_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean, line 1092](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean#L1092). The attribute's comment: “part (2): `F` is representable if and only if the descent datum is effective”.

> **Stacks 02W5, part (2)**: the sheaf corresponding to a descent datum is representable if and
> only if the descent datum is effective.

```lean
theorem isRepresentable_sheafEquivalence_functor_iff (D : DescentData f) :
    ((sheafEquivalence hf).functor.obj D).obj.obj.IsRepresentable ↔ D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isRepresentable_iff_isFamilyEffective_sheafEquivalence_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean, line 1118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/DescentDataSheaves.lean#L1118). The attribute's comment: “part (2), from sheaves to descent data”.

> **Stacks 02W5, part (2)**, from the side of sheaves: a sheaf `F` on `(Sch/S)_J` with every
> `h_{X i} × F` representable is representable if and only if the corresponding descent datum is
> effective.

```lean
theorem isRepresentable_iff_isFamilyEffective_sheafEquivalence_inverse
    (F : (sheavesLocallyRepresentable J f).FullSubcategory) :
    F.obj.obj.IsRepresentable ↔ ((sheafEquivalence hf).inverse.obj F).IsFamilyEffective
```

## Tag 02W6, a remark

[Tag 02W6](https://stacks.math.columbia.edu/tag/02W6) in the Stacks Project.

**`CategoryTheory.isRepresentable_overMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean#L303).

> Let `S` be an object of a category `C`, let `T` be an object over `S` and let `F` be a presheaf
> of types on `C/S`. Then the product `h_T ⨯ F` is representable if and only if the restriction of
> `F` to `C/T.left` is representable.

```lean
theorem isRepresentable_overMap_iff {C : Type u} [Category.{v} C] {S : C} (T : Over S)
    (F : (Over S)ᵒᵖ ⥤ Type v) :
    ((Over.map T.hom).op ⋙ F).IsRepresentable ↔ (yoneda.obj T ⨯ F).IsRepresentable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.39, Tag 02W4](https://stacks.math.columbia.edu/tag/02W4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
