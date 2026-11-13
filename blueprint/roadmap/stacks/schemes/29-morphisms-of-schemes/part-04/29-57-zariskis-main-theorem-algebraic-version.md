---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.exists_isIso_morphismRestrict_toNormalization, AlgebraicGeometry.mem_quasiFiniteLocus_iff, AlgebraicGeometry.locallyOfFiniteType_quasiFiniteLocus, AlgebraicGeometry.locallyQuasiFinite_quasiFiniteLocus, AlgebraicGeometry.exists_isOpenImmersion_isFinite_factorization, AlgebraicGeometry.isNowhereDense_image_of_quasiFinite
statement: formalized
proof: formalized
---

# 29.57 Zariski's Main Theorem (algebraic version)

Section 29.57 of the Stacks Project, [Tag 03GS](https://stacks.math.columbia.edu/tag/03GS). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03GT, a theorem

[Tag 03GT](https://stacks.math.columbia.edu/tag/03GT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.exists_isIso_morphismRestrict_toNormalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.exists_isIso_morphismRestrict_toNormalization#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L131) (StacksFrontier). References: EGA III (4.4.1), “more general”; EGA III (4.4.12), “partial”.

## Tag 01TI, a lemma

[Tag 01TI](https://stacks.math.columbia.edu/tag/01TI) in the Stacks Project.

**`AlgebraicGeometry.mem_quasiFiniteLocus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Locus.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Locus.lean#L66). The attribute's comment: “openness of the quasi-finite locus”.

> A point belongs to the locally quasi-finite locus exactly when the morphism is quasi-finite
> at that point. In particular, the set of such points is open.

```lean
public theorem mem_quasiFiniteLocus_iff {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    x ∈ quasiFiniteLocus f ↔ quasiFiniteAt f x
```

**`AlgebraicGeometry.locallyOfFiniteType_quasiFiniteLocus`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Locus.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Locus.lean#L92). The attribute's comment: “the induced morphism, local finite type”.

> The restriction to the quasi-finite locus is locally of finite type.

```lean
public instance locallyOfFiniteType_quasiFiniteLocus {X S : Scheme.{u}} (f : X ⟶ S) :
    LocallyOfFiniteType ((quasiFiniteLocus f).ι ≫ f)
```

**`AlgebraicGeometry.locallyQuasiFinite_quasiFiniteLocus`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Locus.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/Locus.lean#L124). The attribute's comment: “the induced morphism, fiber isolation”.

> The restriction to the quasi-finite locus is locally quasi-finite in Mathlib's
> fiber-isolation sense.

```lean
public instance locallyQuasiFinite_quasiFiniteLocus {X S : Scheme.{u}} (f : X ⟶ S) :
    LocallyQuasiFinite ((quasiFiniteLocus f).ι ≫ f)
```

## Tag 03GU, a lemma

[Tag 03GU](https://stacks.math.columbia.edu/tag/03GU) in the Stacks Project.

**`AlgebraicGeometry.exists_isOpenImmersion_isFinite_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFactorization.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteFactorization.lean#L176). References: EGA IV (18.12.13), “affine case”; EGA IV (8.12.6), “affine case”; EGA III (4.4.3), “special case”; SGA 3 VIB (5.6.0), “(ii), special case”.

> **Stacks Project, Tag 03GU.** A quasi-finite morphism `f : Y ⟶ X` of affine schemes factors
> as `j ≫ π` with `Z` affine, `j : Y ⟶ Z` an open immersion and `π : Z ⟶ X` finite.
>
> Quasi-compactness of `f` is not assumed: it is automatic for an affine source.

```lean
public theorem exists_isOpenImmersion_isFinite_factorization {X Y : Scheme.{u}} (f : Y ⟶ X)
    [IsAffine X] [IsAffine Y] [LocallyOfFiniteType f] [LocallyQuasiFinite f] :
    ∃ (Z : Scheme.{u}) (_ : IsAffine Z) (j : Y ⟶ Z) (π : Z ⟶ X),
      IsOpenImmersion j ∧ IsFinite π ∧ j ≫ π = f
```

## Tag 03J2, a lemma

[Tag 03J2](https://stacks.math.columbia.edu/tag/03J2) in the Stacks Project.

**`AlgebraicGeometry.isNowhereDense_image_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/NowhereDenseImage.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/NowhereDenseImage.lean#L111).

> **Stacks Project, Tag 03J2.** The image of a closed nowhere dense subset under a quasi-finite
> morphism of schemes is nowhere dense.

```lean
theorem isNowhereDense_image_of_quasiFinite {Y X : Scheme.{u}} (f : Y ⟶ X)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [QuasiCompact f] (T : Set Y)
    (hT_closed : IsClosed T) (hT_nowhereDense : IsNowhereDense T) :
    IsNowhereDense (f.base '' T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.57, Tag 03GS](https://stacks.math.columbia.edu/tag/03GS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
