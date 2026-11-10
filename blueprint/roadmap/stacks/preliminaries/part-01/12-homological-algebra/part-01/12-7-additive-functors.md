---
declaration: section
origin: cited
lean: Functor.additive_of_mono_biprodComparison, Functor.additive_of_epi_biprodComparison', Functor.preservesFiniteBiproductsOfAdditive, preservesBinaryBiproducts_of_preservesBiproducts, Functor.mapBiprod, CategoryTheory.Functor.preservesFiniteLimits_iff_forall_exact_map_and_mono, CategoryTheory.Functor.preservesFiniteColimits_iff_forall_exact_map_and_epi, CategoryTheory.Functor.exact_tfae
statement: formalized
proof: formalized
---

# 12.7 Additive functors

Section 12.7 of the Stacks Project, [Tag 010M](https://stacks.math.columbia.edu/tag/010M). 3 tags here are carried by 2 declarations of the repository (all in StacksCore) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DLP, a lemma

[Tag 0DLP](https://stacks.math.columbia.edu/tag/0DLP) in the Stacks Project.

**`Functor.additive_of_mono_biprodComparison`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L22). The attribute's comment: “(3) => (1)”.

```lean
lemma Functor.additive_of_mono_biprodComparison [HasBinaryBiproducts C] [HasBinaryBiproducts D]
    (G : C ⥤ D) [G.PreservesZeroMorphisms] (h : ∀ X Y : C, Mono (G.biprodComparison X Y)) :
    G.Additive
```

**`Functor.additive_of_epi_biprodComparison'`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L29). The attribute's comment: “(2) => (1)”.

```lean
lemma Functor.additive_of_epi_biprodComparison' [HasBinaryBiproducts C] [HasBinaryBiproducts D]
    (G : C ⥤ D) [G.PreservesZeroMorphisms] (h : ∀ X Y : C, Epi (G.biprodComparison' X Y)) :
    G.Additive
```

Declarations registered for the tag:

- [`Functor.preservesFiniteBiproductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.preservesFiniteBiproductsOfAdditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L17) (StacksCore).
- [`preservesBinaryBiproducts_of_preservesBiproducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesBinaryBiproducts_of_preservesBiproducts#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L18) (StacksCore).
- [`Functor.mapBiprod`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Functor.mapBiprod#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L19) (StacksCore): “1 => 2 and 1 => 3”.

## Tag 010N, a lemma

[Tag 010N](https://stacks.math.columbia.edu/tag/010N) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.preservesFiniteLimits_iff_forall_exact_map_and_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteLimits_iff_forall_exact_map_and_mono#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L13) (StacksCore): “part 2”.
- [`CategoryTheory.Functor.preservesFiniteColimits_iff_forall_exact_map_and_epi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteColimits_iff_forall_exact_map_and_epi#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L15) (StacksCore): “part 3”.
- [`CategoryTheory.Functor.exact_tfae`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.exact_tfae#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/ShortComplex/ExactFunctor.lean#L17) (StacksCore): “part 4”.
- [`CategoryTheory.AdditiveFunctor.ofLeftExact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.AdditiveFunctor.ofLeftExact#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L35) (StacksCore): “part 1 (i)”.
- [`CategoryTheory.AdditiveFunctor.ofRightExact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.AdditiveFunctor.ofRightExact#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L36) (StacksCore): “part 1 (ii)”.

## Tag 010O, a lemma

[Tag 010O](https://stacks.math.columbia.edu/tag/010O) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.Ext.mapExactFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.Ext.mapExactFunctor#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Homology/DerivedCategory/Ext/Map.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Homology/DerivedCategory/Ext/Map.lean#L8) (StacksCore). References: SGA 6 II (2.1.3).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.7, Tag 010M](https://stacks.math.columbia.edu/tag/010M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
