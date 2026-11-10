---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.locallyRepresentableEquivalence, CategoryTheory.GrothendieckTopology.representableByProdYoneda, CategoryTheory.GrothendieckTopology.effectiveDescentData_toDescentData_iff, CategoryTheory.GrothendieckTopology.effectiveDescentDataSheafified_toDescentData_iff, CategoryTheory.isRepresentable_overMap_iff
statement: formalized
proof: formalized
---

# 35.39 Descent data in terms of sheaves

Section 35.39 of the Stacks Project, [Tag 02W4](https://stacks.math.columbia.edu/tag/02W4). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02W5, a lemma

[Tag 02W5](https://stacks.math.columbia.edu/tag/02W5) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.locallyRepresentableEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean#L381). The attribute's comment: “the equivalence of categories”. References: SGA 3 IV (4.6.8).

> Let `(C, J)` be a site, let `{f i : X i ⟶ S}` be a covering of an object `S` of `C`, and let
> `G` range over the sheaves of types on the slice site `C/S`. The sheaves for which every product
> `h_{X i} ⨯ G` is representable are equivalent to the descent data for the covering with
> representable components, via the functor sending a sheaf to its canonical descent datum.

```lean
noncomputable def locallyRepresentableEquivalence
    [HasLimitsOfSize.{max u v, max u v} (Type v)] (hf : Sieve.ofArrows X f ∈ J S) :
    (locallyRepresentable J f).FullSubcategory ≌
      (descentDataRepresentable J f).FullSubcategory
```

**`CategoryTheory.GrothendieckTopology.representableByProdYoneda`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean#L393). The attribute's comment: “part (1): the representing objects are the components of the descent datum”.

> The object representing the product `h_{X i} ⨯ G` is the object over `X i` representing the
> `i`-th component of the canonical descent datum of `G`, viewed as an object over `S`.

```lean
noncomputable def representableByProdYoneda (G : Sheaf (J.over S) (Type v)) (i : ι)
    {Z : Over (X i)}
    (r : ((((J.pseudofunctorOver (Type v)).toDescentData f).obj G).obj i).obj.RepresentableBy Z) :
    (CategoryTheory.yoneda.obj (Over.mk (f i)) ⨯ G.obj).RepresentableBy
      ((Over.map (f i)).obj Z)
```

**`CategoryTheory.GrothendieckTopology.effectiveDescentData_toDescentData_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean#L412). The attribute's comment: “part (2): representable if and only if effective”. References: SGA 3 IV (4.6.8), “partial”.

> The canonical descent datum of a sheaf `G` on `C/S` relative to a covering `{f i : X i ⟶ S}` is
> effective if and only if `G` is representable.

```lean
theorem effectiveDescentData_toDescentData_iff [J.Subcanonical]
    [HasLimitsOfSize.{max u v, max u v} (Type v)] (hf : Sieve.ofArrows X f ∈ J S)
    (G : Sheaf (J.over S) (Type v)) :
    effectiveDescentData J f (((J.pseudofunctorOver (Type v)).toDescentData f).obj G) ↔
      G.obj.IsRepresentable
```

**`CategoryTheory.GrothendieckTopology.effectiveDescentDataSheafified_toDescentData_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheavesSheafified.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheavesSheafified.lean#L148). The attribute's comment: “part (2), for sheafified ULift Yoneda”. References: SGA 3 IV (4.6.8), “partial”.

> **Stacks 02W5, part (2), for sheaves of large sets.** Let `(C, J)` be a subcanonical site
> with `C : Type u` and `Category.{v} C`, let `{f i : X i ⟶ S}` be a covering of an object `S`
> of `C`, and let `G` be a sheaf of `Type (max u v)`-valued sets on the slice site `C/S`. Then the
> canonical descent datum of `G` is effective — isomorphic to the descent datum of a sheafified
> representable — if and only if the underlying presheaf of `G` is representable.

```lean
theorem effectiveDescentDataSheafified_toDescentData_iff [J.Subcanonical]
    [HasWeakSheafify (J.over S) (Type max u v)] (hf : Sieve.ofArrows X f ∈ J S)
    (G : Sheaf (J.over S) (Type max u v)) :
    effectiveDescentDataSheafified J f
        (((J.pseudofunctorOver (Type max u v)).toDescentData f).obj G) ↔
      G.obj.IsRepresentable
```

## Tag 02W6, a remark

[Tag 02W6](https://stacks.math.columbia.edu/tag/02W6) in the Stacks Project.

**`CategoryTheory.isRepresentable_overMap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/LocallyRepresentableSheaves.lean#L292).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
