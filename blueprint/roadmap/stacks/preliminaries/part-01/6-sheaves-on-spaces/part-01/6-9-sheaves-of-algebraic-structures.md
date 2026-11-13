---
declaration: section
origin: cited
lean: TopCat.Presheaf.SheafConditionEqualizerProducts.diagram, TopCat.Presheaf.IsSheafEqualizerProducts, TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts, presheafC0_isSheaf, forget_topCat_not_reflectsIsomorphisms_and_presheafToDiscreteTypes
statement: formalized
proof: formalized
---

# 6.9 Sheaves of algebraic structures

Section 6.9 of the Stacks Project, [Tag 0071](https://stacks.math.columbia.edu/tag/0071). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0072, a definition

[Tag 0072](https://stacks.math.columbia.edu/tag/0072) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.SheafConditionEqualizerProducts.diagram`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.SheafConditionEqualizerProducts.diagram#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean#L24) (StacksFrontier): “the equalizer diagram `F(U) → ∏ F(Uᵢ) ⇉ ∏ F(U_{i₀} ∩ U_{i₁})`”. References: SGA 3 IV (4.1.4.0), “special case”.
- [`TopCat.Presheaf.IsSheafEqualizerProducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.IsSheafEqualizerProducts#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean#L27) (StacksFrontier): “the sheaf condition: that diagram is an equalizer for every open covering”.
- [`TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.isSheaf_iff_isSheafEqualizerProducts#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/EqualizerProducts.lean#L29) (StacksFrontier): “agreement with the sheaf condition for a general target category”. References: SGA 3 IV (4.3.5), “special case”; SGA 4 II (2.4), “opens of a space”.

## Tag 0074, an example

[Tag 0074](https://stacks.math.columbia.edu/tag/0074) in the Stacks Project.

**`presheafC0_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/ContinuousFunctions.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/ContinuousFunctions.lean#L132). References: SGA 4½ Arcata (1.2.3), “special case”; SGA 6 II (AppII.3.0.1), “Y = ℝ”.

> The presheaf of (commutative) `ℝ`-algebras of continuous real-valued
> functions on a topological space `X` is a sheaf of `ℝ`-algebras.

```lean
theorem presheafC0_isSheaf (X : TopCat.{0}) :
    (presheafC0 X).IsSheaf
```

## Tag 0075, an example

[Tag 0075](https://stacks.math.columbia.edu/tag/0075) in the Stacks Project.

**`forget_topCat_not_reflectsIsomorphisms_and_presheafToDiscreteTypes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheaf/TopCatNotSheaf.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheaf/TopCatNotSheaf.lean#L224).

> **Stacks Tag 0075.** The forgetful functor `Top → Sets` is faithful and commutes with
> limits, in particular with products and equalizers (Mathlib's instances `(forget C).Faithful`
> and `TopCat.forget_preservesLimits`), but it does not reflect isomorphisms; and the analogue of
> Lemma 0073 fails for `Top`. Namely, let `X = ℕ` with the discrete topology and let `A i`,
> `i ∈ ℕ`, be discrete spaces. Then `F(U) = ∏_{i ∈ U} A i` with the discrete topology is a
> presheaf of topological spaces whose underlying presheaf of sets is a sheaf (Example 006X); if
> each `A i` has at least two elements, it is not a sheaf of topological spaces; and putting the
> product topology on each `F(U)` instead does give a sheaf of topological spaces.

```lean
theorem forget_topCat_not_reflectsIsomorphisms_and_presheafToDiscreteTypes :
    (forget TopCat.{0}).Faithful ∧ Limits.PreservesLimits (forget TopCat.{0}) ∧
      ¬ (forget TopCat.{0}).ReflectsIsomorphisms ∧
      ∀ (A : TopCat.of ℕ → Type) [∀ i, TopologicalSpace (A i)] [∀ i, DiscreteTopology (A i)],
        TopCat.Presheaf.IsSheaf (presheafToDiscreteTypes (TopCat.of ℕ) A ⋙ forget TopCat) ∧
        ((∀ i, Nontrivial (A i)) → ¬ (presheafToDiscreteTypes (TopCat.of ℕ) A).IsSheaf) ∧
        (presheafToPiTop (TopCat.of ℕ) fun i => TopCat.of (A i)).IsSheaf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.9, Tag 0071](https://stacks.math.columbia.edu/tag/0071)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
