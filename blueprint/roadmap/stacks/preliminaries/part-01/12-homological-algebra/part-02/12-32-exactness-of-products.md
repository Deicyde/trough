---
declaration: section
origin: cited
lean: CategoryTheory.ShortComplex.pi, CategoryTheory.ShortComplex.piHomologyIso, CategoryTheory.ShortComplex.piHomologyIsoAddCommGrpCat, instHasExactLimitsOfShapeDiscreteAddCommGrpCat, instAB4StarAddCommGrpCat
statement: formalized
proof: formalized
---

# 12.32 Exactness of products

Section 12.32 of the Stacks Project, [Tag 060J](https://stacks.math.columbia.edu/tag/060J). 1 tag here is carried by 3 declarations of the repository (all in StacksCore) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 060K, a lemma

[Tag 060K](https://stacks.math.columbia.edu/tag/060K) in the Stacks Project.

**`CategoryTheory.ShortComplex.pi`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/Products.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/Products.lean#L78). The attribute's comment: “The product `∏ L_i ⟶ ∏ M_i ⟶ ∏ N_i` is a complex (the `zero` field)”.

> The product short complex `∏ (S i).X₁ ⟶ ∏ (S i).X₂ ⟶ ∏ (S i).X₃` of a family of short
> complexes, with the differentials `Pi.map`. Its `zero` field is the clause of Stacks 060K that
> `∏ L_i ⟶ ∏ M_i ⟶ ∏ N_i` is again a complex.

```lean
noncomputable def pi : ShortComplex C
```

**`CategoryTheory.ShortComplex.piHomologyIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/Products.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/Products.lean#L143). The attribute's comment: “General version: exact products of short complexes in an abelian category”.

> **Exactness of products** (Stacks 060K, general version): when `I`-indexed products are
> exact in the abelian category `C`, the homology of the product short complex `pi S` is the
> product of the homologies of the `S i`.

```lean
noncomputable def piHomologyIso : (pi S).homology ≅ ∏ᶜ fun i ↦ (S i).homology
```

**`CategoryTheory.ShortComplex.piHomologyIsoAddCommGrpCat`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Homology/ShortComplex/Products.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/Products.lean#L194). The attribute's comment: “The Stacks statement: products of complexes of abelian groups”.

> **Exactness of products** (Stacks 060K): for a family `L_i ⟶ M_i ⟶ N_i` of complexes of
> abelian groups with cohomology `H_i`, the complex `∏ L_i ⟶ ∏ M_i ⟶ ∏ N_i` (`pi S`) has homology
> `∏ H_i`. Products of abelian groups are exact by Mathlib's `AB4Star AddCommGrpCat`.

```lean
noncomputable def piHomologyIsoAddCommGrpCat :
    (pi S).homology ≅ ∏ᶜ fun i ↦ (S i).homology
```

Declarations registered for the tag:

- [`instHasExactLimitsOfShapeDiscreteAddCommGrpCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instHasExactLimitsOfShapeDiscreteAddCommGrpCat#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/Products.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/Products.lean#L40) (StacksCore): “products in Ab are exact”.
- [`instAB4StarAddCommGrpCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instAB4StarAddCommGrpCat#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/Products.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Homology/ShortComplex/Products.lean#L41) (StacksCore): “products in Ab are exact (AB4*)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.32, Tag 060J](https://stacks.math.columbia.edu/tag/060J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
