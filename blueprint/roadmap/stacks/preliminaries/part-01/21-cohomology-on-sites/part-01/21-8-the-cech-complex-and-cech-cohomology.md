---
declaration: section
origin: cited
lean: Stacks.CechSite.cechComplex, Stacks.CechSite.cechCohomology, Stacks.CechSite.cechRestrictionToCohomology_bijective_iff, Stacks.CechSite.isSheaf_iff_bijective_cechRestriction, Stacks.CechSite.cechComplexMap
statement: formalized
proof: formalized
---

# 21.8 The Čech complex and Čech cohomology

Section 21.8 of the Stacks Project, [Tag 03AK](https://stacks.math.columbia.edu/tag/03AK). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03AL, an equation

[Tag 03AL](https://stacks.math.columbia.edu/tag/03AL) in the Stacks Project.

**`Stacks.CechSite.cechComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean#L153). The attribute's comment: “the alternating-sum differential of the Čech complex”. References: SGA 4 V (2.4.3), “Čech complex”.

> The Čech complex associated to an additive presheaf and a family of morphisms with fixed
> target whose finite nonempty fibre products exist.

```lean
noncomputable abbrev cechComplex
    {A : Type u'} [Category.{v'} A] [HasProducts.{w} A] [Preadditive A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (F : CategoryTheory.Functor Cᵒᵖ A) : CochainComplex A ℕ
```

## Tag 03AM, a definition

[Tag 03AM](https://stacks.math.columbia.edu/tag/03AM) in the Stacks Project.

**`Stacks.CechSite.cechComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean#L153). The attribute's comment: “the Čech complex”. References: SGA 4 V (2.4.3), “Čech complex”.

> The Čech complex associated to an additive presheaf and a family of morphisms with fixed
> target whose finite nonempty fibre products exist.

```lean
noncomputable abbrev cechComplex
    {A : Type u'} [Category.{v'} A] [HasProducts.{w} A] [Preadditive A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (F : CategoryTheory.Functor Cᵒᵖ A) : CochainComplex A ℕ
```

**`Stacks.CechSite.cechCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexOfAFamily.lean#L165). The attribute's comment: “the Čech cohomology groups”. References: SGA 4 V (2.4.3), “Čech cohomology of 𝒰”.

> The degree-`n` Čech cohomology object of a presheaf with respect to a family of morphisms
> with fixed target. For abelian-group-valued presheaves this is the Čech cohomology group.

```lean
noncomputable abbrev cechCohomology
    {A : Type u'} [Category.{v'} A] [HasProducts.{w} A] [Abelian A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀),
      HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    (F : CategoryTheory.Functor Cᵒᵖ A) (n : ℕ) : A
```

## Tag 03AN, a lemma

[Tag 03AN](https://stacks.math.columbia.edu/tag/03AN) in the Stacks Project.

**`Stacks.CechSite.cechRestrictionToCohomology_bijective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroAndSheafCondition.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroAndSheafCondition.lean#L430). The attribute's comment: “the Čech-complex formulation”.

> For an individual family whose Čech complex exists, bijectivity into degree-zero
> Čech homology is equivalent to bijectivity into matching families.

```lean
public theorem cechRestrictionToCohomology_bijective_iff {X : C}
    (E : PreZeroHypercover.{w} X)
    [HasProducts.{w} AddCommGrpCat.{a}]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀), HasProduct (fun j ↦ Over.mk (E.f (i j)))]
    (F : Cᵒᵖ ⥤ AddCommGrpCat.{a}) :
    Function.Bijective (cechRestrictionToCohomology E F) ↔
      Function.Bijective (cechRestriction E F)
```

**`Stacks.CechSite.isSheaf_iff_bijective_cechRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroAndSheafCondition.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/DegreeZeroAndSheafCondition.lean#L453).

> **Stacks 03AN.** An abelian presheaf is a sheaf if and only if restriction to the
> degree-zero Čech cohomology of every covering family is bijective.

```lean
public theorem isSheaf_iff_bijective_cechRestriction
    (J : GrothendieckTopology C) (F : Cᵒᵖ ⥤ AddCommGrpCat.{a}) :
    Presheaf.IsSheaf J F ↔
      ∀ {X : C} (E : PreZeroHypercover.{max u v} X), E.sieve₀ ∈ J X →
        Function.Bijective (cechRestriction E F)
```

## Tag 03F4, an equation

[Tag 03F4](https://stacks.math.columbia.edu/tag/03F4) in the Stacks Project.

**`Stacks.CechSite.cechComplexMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexMapOfARefinement.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Cech/ComplexMapOfARefinement.lean#L380).

> The map of Čech complexes induced by a morphism of families of morphisms with fixed target,
> from the Čech complex of the refined family `G` to that of the refining family `E`.

```lean
noncomputable def cechComplexMap
    {C : Type u} [Category.{v} C] {U V : C}
    (E : PreZeroHypercover.{w} U) (G : PreZeroHypercover.{w'} V) {f : U ⟶ V}
    (φ : E.HomOver G f)
    {A : Type u'} [Category.{v'} A] [Preadditive A]
    [HasProducts.{w} A] [HasProducts.{w'} A]
    [∀ (n : ℕ) (i : Fin (n + 1) → E.I₀), HasProduct (fun a ↦ Over.mk (E.f (i a)))]
    [∀ (n : ℕ) (i : Fin (n + 1) → G.I₀), HasProduct (fun a ↦ Over.mk (G.f (i a)))]
    (F : Cᵒᵖ ⥤ A) :
    cechComplex G F ⟶ cechComplex E F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.8, Tag 03AK](https://stacks.math.columbia.edu/tag/03AK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
