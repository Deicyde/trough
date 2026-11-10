---
declaration: section
origin: cited
lean: CategoryTheory.EssentiallyConstantInd.isEssentiallyConstantInd_iff_exists_biproduct, CategoryTheory.EssentiallyConstantPro.isEssentiallyConstantPro_iff_exists_biproduct, hasColimit_biprod_iff, colimitBiprodIso, colimitBiprodIso_of_hasColimit_biprod, isEssentiallyConstantInd_biprod_iff
statement: formalized
proof: formalized
---

# 12.30 Essentially constant systems

Section 12.30 of the Stacks Project, [Tag 0A2D](https://stacks.math.columbia.edu/tag/0A2D). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A2E, a lemma

[Tag 0A2E](https://stacks.math.columbia.edu/tag/0A2E) in the Stacks Project.

**`CategoryTheory.EssentiallyConstantInd.isEssentiallyConstantInd_iff_exists_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Karoubian.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Karoubian.lean#L204). The attribute's comment: “(1)”.

> Stacks 0A2E (1). Let `M : I ⥤ A` be a diagram over a filtered category in a preadditive
> Karoubian category. Then `M` is essentially constant if and only if `colim M` exists and there are
> a filtered category `I'` with a fully faithful cofinal functor `H : I' ⥤ I` (a cofinal
> filtered full subcategory) and, for each `i' : I'`, a direct sum
> decomposition `M (H i') ≅ X_{i'} ⊕ Z_{i'}` such that `X_{i'}` maps isomorphically to `colim M` and
> `Z_{i'}` maps to zero in `M (H i'')` for some `i' ⟶ i''` in `I'`.

```lean
theorem isEssentiallyConstantInd_iff_exists_biproduct [IsFiltered I] [IsIdempotentComplete A]
    (M : I ⥤ A) :
    IsEssentiallyConstantInd M ↔
      ∃ (_ : HasColimit M) (I' : Type u') (_ : Category.{v'} I') (_ : IsFiltered I')
        (H : I' ⥤ I) (_ : H.Full) (_ : H.Faithful) (_ : H.Final), ∀ i' : I',
          ∃ (X' Z' : A) (b : BinaryBicone X' Z') (_ : b.IsBilimit) (e : b.pt ≅ M.obj (H.obj i')),
            IsIso (b.inl ≫ e.hom ≫ colimit.ι M (H.obj i')) ∧
            ∃ (i'' : I') (f : i' ⟶ i''), b.inr ≫ e.hom ≫ M.map (H.map f) = 0
```

**`CategoryTheory.EssentiallyConstantPro.isEssentiallyConstantPro_iff_exists_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Karoubian.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Karoubian.lean#L334). The attribute's comment: “(2)”.

> Stacks 0A2E (2). Let `M : I ⥤ A` be a diagram over a cofiltered category in a preadditive
> Karoubian category. Then `M` is essentially constant if and only if `lim M` exists and there are
> a cofiltered category `I'` with a fully faithful initial functor `H : I' ⥤ I` (an initial
> cofiltered full subcategory) and, for each `i' : I'`, a direct
> sum decomposition `M (H i') ≅ X_{i'} ⊕ Z_{i'}` such that `lim M` maps isomorphically to `X_{i'}`
> and `M (H i'') ⟶ Z_{i'}` is zero for some `i'' ⟶ i'` in `I'`.

```lean
theorem isEssentiallyConstantPro_iff_exists_biproduct [IsCofiltered I] [IsIdempotentComplete A]
    (M : I ⥤ A) :
    IsEssentiallyConstantPro M ↔
      ∃ (_ : HasLimit M) (I' : Type u') (_ : Category.{v'} I') (_ : IsCofiltered I')
        (H : I' ⥤ I) (_ : H.Full) (_ : H.Faithful) (_ : H.Initial), ∀ i' : I',
          ∃ (X' Z' : A) (b : BinaryBicone X' Z') (_ : b.IsBilimit) (e : b.pt ≅ M.obj (H.obj i')),
            IsIso (limit.π M (H.obj i') ≫ e.inv ≫ b.fst) ∧
            ∃ (i'' : I') (f : i'' ⟶ i'), M.map (H.map f) ≫ e.inv ≫ b.snd = 0
```

## Tag 0A2F, a lemma

[Tag 0A2F](https://stacks.math.columbia.edu/tag/0A2F) in the Stacks Project.

**`hasColimit_biprod_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean#L186). The attribute's comment: “iff”.

> In a Karoubian additive category, the pointwise biproduct functor `F ⊞ G`
> has a colimit iff both `F` and `G` do.

```lean
theorem hasColimit_biprod_iff
    {I C : Type*} [Category I] [Category C]
    [Preadditive C] [HasBinaryBiproducts C] [IsIdempotentComplete C]
    (F G : I ⥤ C) :
    HasColimit (F ⊞ G) ↔ HasColimit F ∧ HasColimit G
```

**`colimitBiprodIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean#L213). The attribute's comment: “iso”.

> In a Karoubian additive category, if both `F` and `G` have colimits, then
> the colimit of the pointwise biproduct is canonically isomorphic to the
> biproduct of the colimits.

```lean
noncomputable def colimitBiprodIso
    {I C : Type*} [Category I] [Category C]
    [Preadditive C] [HasBinaryBiproducts C] [IsIdempotentComplete C]
    (F G : I ⥤ C) [HasColimit F] [HasColimit G] :
    haveI := hasColimit_biprod_of_hasColimit F G
    colimit (F ⊞ G) ≅ colimit F ⊞ colimit G
```

**`colimitBiprodIso_of_hasColimit_biprod`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean#L226). The attribute's comment: “iso_from_biprod”.

> In a Karoubian additive category, if `F ⊞ G` has a colimit, then it is canonically isomorphic
> to the biproduct of the colimits of `F` and `G`.

```lean
noncomputable def colimitBiprodIso_of_hasColimit_biprod
    {I C : Type*} [Category I] [Category C]
    [Preadditive C] [HasBinaryBiproducts C] [IsIdempotentComplete C]
    (F G : I ⥤ C) [HasColimit (F ⊞ G)] :
    haveI := hasColimit_of_hasColimit_biprod_left F G
    haveI := hasColimit_of_hasColimit_biprod_right F G
    colimit (F ⊞ G) ≅ colimit F ⊞ colimit G
```

## Tag 0A2G, a lemma

[Tag 0A2G](https://stacks.math.columbia.edu/tag/0A2G) in the Stacks Project.

**`isEssentiallyConstantInd_biprod_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/EssentiallyConstant/Biproducts.lean#L385).

> Let `I` be a filtered category and `C` an additive Karoubian category. For
> two functors `F, G : I ⥤ C`, the direct sum `F ⊞ G` is essentially constant
> iff both `F` and `G` are essentially constant.

```lean
theorem isEssentiallyConstantInd_biprod_iff
    {I : Type u} [Category.{v} I] [IsFiltered I]
    {C : Type u'} [Category.{v'} C] [Preadditive C]
    [HasFiniteBiproducts C] [IsIdempotentComplete C]
    (F G : I ⥤ C) :
    haveI : HasBinaryBiproducts C := hasBinaryBiproducts_of_finite_biproducts C
    IsEssentiallyConstantInd (F ⊞ G) ↔
      IsEssentiallyConstantInd F ∧ IsEssentiallyConstantInd G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.30, Tag 0A2D](https://stacks.math.columbia.edu/tag/0A2D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
