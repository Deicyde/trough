---
declaration: section
origin: cited
lean: DerivedCategory.isGE_iff, CategoryTheory.Triangulated.TStructure.plus, DerivedCategory.isLE_iff, CategoryTheory.Triangulated.TStructure.minus, CategoryTheory.Triangulated.TStructure.bounded, CategoryTheory.HomotopyCategory.PlusInjective.isEquivalence_toDerivedPlus, CochainComplex.Qh_map_bijective_of_projective_of_minus, CochainComplex.Qh_map_bijective_of_injective_of_plus
statement: formalized
proof: formalized
---

# 64.6 Derived categories

Section 64.6 of the Stacks Project, [Tag 03T3](https://stacks.math.columbia.edu/tag/03T3). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03T5, a lemma

[Tag 03T5](https://stacks.math.columbia.edu/tag/03T5) in the Stacks Project.

Declarations registered for the tag:

- [`DerivedCategory.isGE_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory.isGE_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch64.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch64.lean#L19) (StacksFrontier): “D^+, with `TStructure.plus`”.
- [`CategoryTheory.Triangulated.TStructure.plus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Triangulated.TStructure.plus#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch64.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch64.lean#L20) (StacksFrontier): “D^+: `t.plus X` is `∃ n, t.IsGE X n`”.
- [`DerivedCategory.isLE_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DerivedCategory.isLE_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch64.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch64.lean#L22) (StacksFrontier): “D^-, with `TStructure.minus`”.
- [`CategoryTheory.Triangulated.TStructure.minus`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Triangulated.TStructure.minus#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch64.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch64.lean#L23) (StacksFrontier): “D^-: `t.minus X` is `∃ n, t.IsLE X n`”.
- [`CategoryTheory.Triangulated.TStructure.bounded`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Triangulated.TStructure.bounded#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch64.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch64.lean#L25) (StacksFrontier): “D^b: `t.bounded` is `t.plus ⊓ t.minus`”.

## Tag 03T6, a lemma

[Tag 03T6](https://stacks.math.columbia.edu/tag/03T6) in the Stacks Project.

**`CategoryTheory.HomotopyCategory.PlusInjective.isEquivalence_toDerivedPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BoundedBelowInjectiveEquivalence.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/BoundedBelowInjectiveEquivalence.lean#L120). The attribute's comment: “injective_equivalence”. References: SGA 4½ Etat 0 (3.2.3), “(3)”; SGA 4½ Etat 0 (3.1.4).

> **Stacks 03T6, part (3).** If `A` has enough injectives and `I ⊆ A` is the additive
> subcategory of injectives, then `D⁺(A) ≅ K⁺(I)`: the canonical functor from the bounded below
> homotopy category of complexes of injective objects to the bounded below derived category is
> an equivalence.

```lean
theorem isEquivalence_toDerivedPlus [EnoughInjectives A] :
    (toDerivedPlus A).IsEquivalence
```

**`CochainComplex.Qh_map_bijective_of_projective_of_minus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/MorphismsFromBoundedAboveProjectives.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/MorphismsFromBoundedAboveProjectives.lean#L49). The attribute's comment: “projective_hom”. References: SGA 4½ Etat 0 (3.2.3), “(4) proj. analogue”.

> **Stacks 03T6, part (2).** A bounded above complex of projective objects computes
> morphisms from it in the derived category already in the homotopy category.

```lean
theorem Qh_map_bijective_of_projective_of_minus [HasDerivedCategory.{w} A]
    (P : CochainComplex A ℤ) (K : HomotopyCategory A (ComplexShape.up ℤ))
    (hP : CochainComplex.minus A P) [∀ n, Projective (P.X n)] :
    Function.Bijective (DerivedCategory.Qh.map :
      ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj P ⟶ K) → _)
```

**`CochainComplex.Qh_map_bijective_of_injective_of_plus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/MorphismsIntoBoundedBelowInjectives.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/MorphismsIntoBoundedBelowInjectives.lean#L49). The attribute's comment: “injective_hom”.

> **Stacks 03T6, part (1).** A bounded below complex of injective objects computes
> morphisms into it in the derived category already in the homotopy category.

```lean
theorem Qh_map_bijective_of_injective_of_plus [HasDerivedCategory.{w} A]
    (K : HomotopyCategory A (ComplexShape.up ℤ)) (I : CochainComplex A ℤ)
    (hI : CochainComplex.plus A I) [∀ n, Injective (I.X n)] :
    Function.Bijective (DerivedCategory.Qh.map :
      (K ⟶ (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj I) → _)
```

**`CategoryTheory.HomotopyCategory.MinusProjective.isEquivalence_toDerivedMinus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L155). The attribute's comment: “projective_equivalence”. References: SGA 4½ Etat 0 (3.2.3), “(4) proj. analogue”.

> **Stacks 03T6, part (4).** If `A` has enough projectives and `P ⊆ A` is the additive
> subcategory of projectives, then `D⁻(A) ≅ K⁻(P)`: the canonical functor from the bounded above
> homotopy category of complexes of projective objects to the bounded above derived category is
> an equivalence.

```lean
theorem isEquivalence_toDerivedMinus [EnoughProjectives A] :
    (toDerivedMinus A).IsEquivalence
```

## Tag 03T7, a definition

[Tag 03T7](https://stacks.math.columbia.edu/tag/03T7) in the Stacks Project.

**`CategoryTheory.Functor.mapMinusProjectiveToDerivedMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L192). The attribute's comment: “the projective-complex route for the left derived functor”.

> The lower route in the diagram defining the total left derived functor: apply the
> additive functor termwise to a bounded above complex of projectives, then pass to the
> bounded above derived category.

```lean
def mapMinusProjectiveToDerivedMinus (G : A ⥤ B) [G.Additive] :
    HomotopyCategory.MinusProjective A ⥤ DerivedCategory.Minus B
```

**`CategoryTheory.Functor.leftDerivedFunctorMinus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L213). The attribute's comment: “the total left derived functor”. References: SGA 4½ Etat 0 (4.1.2), “left derived functor”; SGA 4½ Etat 0 (4.1.4), “LF”; SGA 4½ Etat 0 (4.1.5), “L^- f”; SGA 4 XVII (1.2.5), “(ii), single functor”; SGA 4½ Etat 0 (4.1.3), “L⁻ f”.

> The total left derived functor on the bounded above derived category, constructed using
> bounded above complexes of projective objects.

```lean
def leftDerivedFunctorMinus (G : A ⥤ B) [G.Additive] [EnoughProjectives A] :
    DerivedCategory.Minus A ⥤ DerivedCategory.Minus B
```

**`CategoryTheory.Functor.leftDerivedFunctorMinusIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L223). The attribute's comment: “the comparison isomorphism for the total left derived functor”.

> The natural commuting isomorphism in the projective-resolution diagram defining the total
> left derived functor.

```lean
def leftDerivedFunctorMinusIso (G : A ⥤ B) [G.Additive] [EnoughProjectives A] :
    HomotopyCategory.MinusProjective.toDerivedMinus A ⋙ leftDerivedFunctorMinus G ≅
      mapMinusProjectiveToDerivedMinus G
```

**`CategoryTheory.Functor.mapPlusInjectiveToDerivedPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L236). The attribute's comment: “the injective-complex route for the right derived functor”.

> The lower route in the diagram defining the total right derived functor: apply the
> additive functor termwise to a bounded below complex of injectives, then pass to the
> bounded below derived category.

```lean
def mapPlusInjectiveToDerivedPlus (F : A ⥤ B) [F.Additive] :
    HomotopyCategory.PlusInjective A ⥤ DerivedCategory.Plus B
```

**`CategoryTheory.Functor.rightDerivedFunctorPlusOfInjectives`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L255). The attribute's comment: “the total right derived functor”. References: SGA 4½ Etat 0 (4.1.2), “right derived functor”; SGA 4½ Etat 0 (4.1.4), “RF”; SGA 4 XVII (1.2.5), “(ii), single functor”.

> The total right derived functor on the bounded below derived category, constructed using
> bounded below complexes of injective objects.

```lean
def rightDerivedFunctorPlusOfInjectives (F : A ⥤ B) [F.Additive] [EnoughInjectives A] :
    DerivedCategory.Plus A ⥤ DerivedCategory.Plus B
```

**`CategoryTheory.Functor.rightDerivedFunctorPlusOfInjectivesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L265). The attribute's comment: “the comparison isomorphism for the total right derived functor”.

> The natural commuting isomorphism in the injective-resolution diagram defining the total
> right derived functor.

```lean
def rightDerivedFunctorPlusOfInjectivesIso (F : A ⥤ B) [F.Additive] [EnoughInjectives A] :
    HomotopyCategory.PlusInjective.toDerivedPlus A ⋙ rightDerivedFunctorPlusOfInjectives F ≅
      mapPlusInjectiveToDerivedPlus F
```

**`CategoryTheory.Functor.rightDerivedFunctorPlusOfInjectivesUnit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TotalDerivedFunctors.lean#L304). The attribute's comment: “the comparison map for the total right derived functor”.

> The comparison map for the total right derived functor: the natural transformation from
> "apply `F` termwise, then localize" to the composite of the localization functor with
> `RF`.

```lean
def rightDerivedFunctorPlusOfInjectivesUnit (F : A ⥤ B) [F.Additive] [EnoughInjectives A] :
    F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ⟶
      DerivedCategory.Plus.Qh ⋙ rightDerivedFunctorPlusOfInjectives F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.6, Tag 03T3](https://stacks.math.columbia.edu/tag/03T3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
