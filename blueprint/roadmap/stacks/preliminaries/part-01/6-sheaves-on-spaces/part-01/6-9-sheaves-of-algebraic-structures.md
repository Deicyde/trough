---
declaration: section
origin: cited
lean: TopCat.Presheaf.SheafConditionEqualizerProducts.diagram, TopCat.Presheaf.IsSheafEqualizerProducts, TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts, presheafC0_isSheaf, exists_presheaf_topCat_isSheaf_forget_not_isSheaf
statement: formalized
proof: formalized
---

# 6.9 Sheaves of algebraic structures

Section 6.9 of the Stacks Project, [Tag 0071](https://stacks.math.columbia.edu/tag/0071). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0072, a definition

[Tag 0072](https://stacks.math.columbia.edu/tag/0072) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.SheafConditionEqualizerProducts.diagram`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.SheafConditionEqualizerProducts.diagram#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean#L24) (StacksFrontier): “the equalizer diagram `F(U) → ∏ F(Uᵢ) ⇉ ∏ F(U_{i₀} ∩ U_{i₁})`”. References: SGA 3 IV (4.1.4.0), “special case”.
- [`TopCat.Presheaf.IsSheafEqualizerProducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.IsSheafEqualizerProducts#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean#L27) (StacksFrontier): “the sheaf condition: that diagram is an equalizer for every open covering”.
- [`TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean#L29) (StacksFrontier): “agreement with the sheaf condition for a general target category”. References: SGA 3 IV (4.3.5), “special case”; SGA 4 II (2.4), “opens of a space”.

## Tag 0074, an example

[Tag 0074](https://stacks.math.columbia.edu/tag/0074) in the Stacks Project.

**`presheafC0_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/ContinuousFunctions.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/ContinuousFunctions.lean#L132). References: SGA 4½ Arcata (1.2.3), “special case”; SGA 6 II (AppII.3.0.1), “Y = ℝ”.

> The presheaf of (commutative) `ℝ`-algebras of continuous real-valued
> functions on a topological space `X` is a sheaf of `ℝ`-algebras.

```lean
theorem presheafC0_isSheaf (X : TopCat.{0}) :
    (presheafC0 X).IsSheaf
```

## Tag 0075, an example

[Tag 0075](https://stacks.math.columbia.edu/tag/0075) in the Stacks Project.

**`exists_presheaf_topCat_isSheaf_forget_not_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/TopCatNotSheaf.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheaf/TopCatNotSheaf.lean#L155). References: EGA 0 (3.1.4), “failure for top. spaces”.

> **Stacks Tag 0075.** There is a topological space `X` and a presheaf `F` of topological
> spaces on `X` whose underlying presheaf of sets is a sheaf, but which is not a sheaf of
> topological spaces: so Lemma 0073 has no analogue for `Top`, the forgetful functor
> `Top → Sets` not reflecting isomorphisms. The witness is the tag's: `X = ℕ` discrete, and
> `F(U) = ∏_{i ∈ U} Bool` with the discrete topology.

```lean
theorem exists_presheaf_topCat_isSheaf_forget_not_isSheaf :
    ∃ (X : TopCat.{0}) (F : X.Presheaf TopCat.{0}),
      TopCat.Presheaf.IsSheaf (F ⋙ forget TopCat) ∧ ¬ TopCat.Presheaf.IsSheaf F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.9, Tag 0071](https://stacks.math.columbia.edu/tag/0071)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
