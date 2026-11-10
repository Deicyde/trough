---
declaration: section
origin: cited
lean: CategoryTheory.FilteredDerived.filteredDerivedPlus, CategoryTheory.FiniteFilteredObject.hasFiniteBiproducts, CategoryTheory.FilteredDerived.IsFilteredProjective, CochainComplex, CochainComplex.Plus, HomotopyCategory, HomotopyCategory.Plus, CochainComplex.filteredQuasiIsoC
statement: formalized
proof: formalized
---

# 64.7 Filtered derived category

Section 64.7 of the Stacks Project, [Tag 03T9](https://stacks.math.columbia.edu/tag/03T9). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 16 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03TA, a definition

[Tag 03TA](https://stacks.math.columbia.edu/tag/03TA) in the Stacks Project.

**`CategoryTheory.FilteredDerived.filteredDerivedPlus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L86). The attribute's comment: “filtered_derived_plus”. References: SGA 4 Vbis (2.5.1), “D^+F(A)”.

> The localisation of `K⁺(Fil^f(A))` at filtered quasi-isomorphisms.

```lean
abbrev filteredDerivedPlus (A : Type u) [Category.{v} A] [Abelian A]
```

**`CategoryTheory.FiniteFilteredObject.hasFiniteBiproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L90). The attribute's comment: “finite_filtered_additive”.

> The category of finite filtered objects has finite biproducts.

```lean
noncomputable instance hasFiniteBiproducts (C : Type u) [Category.{v} C]
    [Preadditive C] [HasZeroObject C] [HasBinaryBiproducts C] :
    HasFiniteBiproducts (FiniteFilteredObject C)
```

**`CategoryTheory.FilteredDerived.IsFilteredProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Projective.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Projective.lean#L62). The attribute's comment: “filtered_projective”.

> A finite filtered object is **filtered projective** if all its graded pieces are
> projective.

```lean
abbrev IsFilteredProjective {C : Type u} [Category.{v} C] [Abelian C]
    (I : FiniteFilteredObject C) : Prop
```

Declarations registered for the tag:

- [`CochainComplex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L55) (StacksFrontier): “filtered_complexes”. References: EGA 0 (11.2.1); EGA 0 (13.2.3); EGA III (6.2.1); SGA 2 VIII (1.2); SGA 4 XVII (2.2.7), “special case”; SGA 4 XVII (5.5.3); SGA 4½ Etat 0 (1.2.1); SGA 6 I (1.1.5).
- [`CochainComplex.Plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.Plus#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L56) (StacksFrontier): “filtered_complexes”. References: SGA 2 VIII (1.4); SGA 4 Vbis (2.5.1), “partial”.
- [`HomotopyCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L59) (StacksFrontier): “filtered_homotopy”. References: EGA 0 (20.6.26); SGA 4 Vbis (2.5.1); SGA 4 XVII (2.2.8), “absolute case of K(A/B)”; SGA 4½ Etat 0 (1.2.2); SGA 4½ Rapport (4.3), “arrows of K_parf(Λ)”; SGA 6 I (1.1.5), “partial”.
- [`HomotopyCategory.Plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HomotopyCategory.Plus#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L66) (StacksFrontier): “filtered_homotopy”. References: SGA 4 Vbis (2.3.3), “(A)”; SGA 4 Vbis (2.5.1), “K⁺(F(A))”; SGA 4 XVII (2.2.10), “special case”; SGA 4½ Etat 0 (1.2.3); SGA 6 I (1.1.5), “the fiber K⁺(C_X)”.
- [`CochainComplex.filteredQuasiIsoC`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FilteredDerivedCategory/Basic.lean#L359), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L72) (StacksFrontier): “filtered_quasi_isomorphism”.
- [`CochainComplex.FilteredDerivedCategory`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L348), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L73) (StacksFrontier): “filtered_derived”.
- [`CochainComplex.FilteredDerivedCategory.Qh`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FilteredDerivedCategory/Basic.lean#L440), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/DerivedCategory.lean#L74) (StacksFrontier): “filtered_derived”.
- [`CategoryTheory.FilteredObject`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FilteredObject#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L41) (StacksFrontier): “filtered_objects”. References: SGA 4 Vbis (2.5.1), “more general”.
- [`CategoryTheory.FilteredObject.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.FilteredObject.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L42) (StacksFrontier): “filtered_objects”.
- [`CategoryTheory.FiniteFilteredObject`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L236), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L43) (StacksFrontier): “finite_filtered”.
- [`CategoryTheory.FilteredObject.preadditive`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Preadditive.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L44) (StacksFrontier): “filtered_additive”. References: SGA 4 Vbis (2.5.1), “partial”.
- [`CategoryTheory.FilteredObject.hasFiniteBiproducts`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Filtration/Preadditive.lean#L367), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L45) (StacksFrontier): “filtered_additive”.
- [`CategoryTheory.FilteredObject.IsFilteredInjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L243), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L46) (StacksFrontier): “filtered_injective”.
- [`CategoryTheory.Preadditive.fullSubcategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Preadditive.fullSubcategory#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/Objects.lean#L47) (StacksFrontier): “finite_filtered_additive”.

## Tag 03TB, a lemma

[Tag 03TB](https://stacks.math.columbia.edu/tag/03TB) in the Stacks Project.

**`CategoryTheory.FilteredDerived.filteredProjectiveMinusToDerivedMinus_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FilteredDerived/Category/BoundedEquivalence.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/BoundedEquivalence.lean#L510). The attribute's comment: “projective case”.

> The bounded-above filtered derived category is equivalent to the bounded-above homotopy
> category of filtered projective objects.

```lean
theorem filteredProjectiveMinusToDerivedMinus_isEquivalence [EnoughProjectives A] :
    (filteredProjectiveMinusToDerivedMinus A).IsEquivalence
```

Declarations registered for the tag:

- [`CochainComplex.FilteredDerivedCategory.toPlus`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FilteredDerivedCategory/Triangulated.lean#L392), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/BoundedEquivalence.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/BoundedEquivalence.lean#L41) (StacksFrontier): “injective case”.
- [`CochainComplex.FilteredDerivedCategory.isEquivalence_isTriangulated_toPlus_and_squares`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/FilteredDerivedCategory/Triangulated.lean#L571), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FilteredDerived/Category/BoundedEquivalence.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FilteredDerived/Category/BoundedEquivalence.lean#L42) (StacksFrontier): “injective equivalence”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.7, Tag 03T9](https://stacks.math.columbia.edu/tag/03T9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
