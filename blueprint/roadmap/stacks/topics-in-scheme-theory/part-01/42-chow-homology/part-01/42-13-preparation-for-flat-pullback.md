---
declaration: section
origin: cited
lean: Stacks.Chow.dense_image_irreducibleComponent_pullback, Stacks.Chow.schemeDeltaDimension_pullback_snd_comp, Stacks.Chow.deltaDimension_irreducibleComponent_pullback_snd_comp, Stacks.Chow.schemeDeltaDimension_pullback_snd_comp_eq_iSup_add, Stacks.Chow.not_forall_schemeDeltaDimension_pullback_snd_comp_of_nonempty, LocallyFinite.preimage_continuous
statement: formalized
proof: formalized
---

# 42.13 Preparation for flat pullback

Section 42.13 of the Stacks Project, [Tag 02R7](https://stacks.math.columbia.edu/tag/02R7). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02R8, a lemma

[Tag 02R8](https://stacks.math.columbia.edu/tag/02R8) in the Stacks Project.

**`Stacks.Chow.dense_image_irreducibleComponent_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimension.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimension.lean#L147). The attribute's comment: “dominance of components”. References: EGA IV (2.3.4), “(iii), special case”; EGA IV (4.4.1), “special case”; SGA 7 VIII (5.2), “partial”.

> **Stacks 02R8.** Every irreducible component of the scheme-theoretic inverse image of an
> irreducible closed subscheme along a flat morphism dominates that subscheme: the inverse image
> is flat over the subscheme by base change.

```lean
theorem dense_image_irreducibleComponent_pullback {X Y Z : Scheme.{u}} (f : X ⟶ Y) [Flat f]
    (i : Z ⟶ Y) [IrreducibleSpace Z]
    (W : irreducibleComponents (pullback f i : Scheme.{u})) :
    closure ((pullback.snd f i).base '' (W : Set (pullback f i : Scheme.{u}))) = Set.univ
```

**`Stacks.Chow.schemeDeltaDimension_pullback_snd_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimension.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimension.lean#L331). The attribute's comment: “dimension of the inverse image”.

> **Stacks 02R8.** The scheme-theoretic inverse image of a closed subscheme `i : Z ⟶ Y` along
> a flat morphism `f : X ⟶ Y` of relative dimension `r` has delta-dimension `dim_δ(Z) + r`, as
> soon as its projection to `Z` meets every irreducible component of `Z`.

```lean
theorem schemeDeltaDimension_pullback_snd_comp (C : ChowSituation.{u}) {X Y Z : Scheme.{u}}
    (g : Y ⟶ C.S) [LocallyOfFiniteType g] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (i : Z ⟶ Y) [IsClosedImmersion i]
    (hmeets : ∀ V : irreducibleComponents Z,
      ∃ x : (pullback f i : Scheme.{u}), (pullback.snd f i).base x ∈ (V : Set Z)) :
    schemeDeltaDimension C (pullback.snd f i ≫ i ≫ g) =
      schemeDeltaDimension C (i ≫ g) + ((r : ℤ) : EInt)
```

**`Stacks.Chow.deltaDimension_irreducibleComponent_pullback_snd_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimension.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimension.lean#L347). The attribute's comment: “dimension of components”.

> **Stacks 02R8.** Over an irreducible closed subscheme `i : Z ⟶ Y`, every irreducible
> component of the scheme-theoretic inverse image along a flat morphism `f : X ⟶ Y` of relative
> dimension `r` has delta-dimension `dim_δ(Z) + r`.

```lean
theorem deltaDimension_irreducibleComponent_pullback_snd_comp (C : ChowSituation.{u})
    {X Y Z : Scheme.{u}} (g : Y ⟶ C.S) [LocallyOfFiniteType g] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (i : Z ⟶ Y) [IsClosedImmersion i] [IrreducibleSpace Z]
    (W : irreducibleComponents (pullback f i : Scheme.{u})) :
    deltaDimension C (pullback.snd f i ≫ i ≫ g)
        ⟨(W : Set (pullback f i : Scheme.{u})), W.2.1,
          isClosed_of_mem_irreducibleComponents (W : Set (pullback f i : Scheme.{u})) W.2⟩ =
      deltaDimension C (i ≫ g)
          ⟨Set.univ, IrreducibleSpace.isIrreducible_univ Z, isClosed_univ⟩ + (r : ℤ)
```

**`Stacks.Chow.schemeDeltaDimension_pullback_snd_comp_eq_iSup_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimensionCounterexample.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimensionCounterexample.lean#L156). The attribute's comment: “corrected dimension formula: sup over the components of Z met by f⁻¹(Z)”.

> **Stacks 02R8**, the dimension formula for the inverse image, at the source's hypotheses.
> The source asserts `dim_δ(f⁻¹(Z)) = dim_δ(Z) + r` for a closed subscheme `i : Z ⟶ Y` and a flat
> `f : X ⟶ Y` of relative dimension `r`, provided `f⁻¹(Z)` is nonempty; that is false
> (`Stacks.Chow.not_forall_schemeDeltaDimension_pullback_snd_comp_of_nonempty`), because a component
> of `Z` missed by the image of `f` counts in `dim_δ(Z)` and in nothing upstairs. What the source's
> proof does establish, with no hypothesis beyond flatness and relative dimension `r`, is this:
> `dim_δ(f⁻¹(Z))` is `r` more than the supremum of `dim_δ(V)` over the irreducible components `V`
> of `Z` that `f⁻¹(Z)` lies over. When every irreducible component of `Z` has nonempty inverse
> image that supremum is `dim_δ(Z)`, which is
> `Stacks.Chow.schemeDeltaDimension_pullback_snd_comp`.

```lean
theorem schemeDeltaDimension_pullback_snd_comp_eq_iSup_add (C : ChowSituation.{u})
    {X Y Z : Scheme.{u}} (g : Y ⟶ C.S) [LocallyOfFiniteType g] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r)
    (i : Z ⟶ Y) [IsClosedImmersion i] :
    schemeDeltaDimension C (pullback.snd f i ≫ i ≫ g) =
      (⨆ V : {V : irreducibleComponents Z //
          ∃ x : (pullback f i : Scheme.{u}), (pullback.snd f i).base x ∈ (V.1 : Set Z)},
          (deltaDimension C (i ≫ g)
            ⟨(V.1 : Set Z), V.1.2.1, isClosed_of_mem_irreducibleComponents (V.1 : Set Z) V.1.2⟩ :
            EInt)) + ((r : ℤ) : EInt)
```

**`Stacks.Chow.not_forall_schemeDeltaDimension_pullback_snd_comp_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimensionCounterexample.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InverseImageDimensionCounterexample.lean#L317). The attribute's comment: “the first claim is false as stated: f⁻¹(Z) nonempty does not suffice”.

> **Stacks 02R8**: the first claim, `dim_δ(f⁻¹(Z)) = dim_δ(Z) + r` for a closed subscheme
> `Z ⊂ Y` provided only that `f⁻¹(Z)` is nonempty, is false. The counterexample is
> `Stacks.Chow.schemeDeltaDimension_pullback_firstPointInclusion_ne`; the corrected formula is
> `Stacks.Chow.schemeDeltaDimension_pullback_snd_comp_eq_iSup_add`, and under the additional
> hypothesis that every irreducible component of `Z` has nonempty inverse image the source's
> formula holds, `Stacks.Chow.schemeDeltaDimension_pullback_snd_comp`.

```lean
theorem not_forall_schemeDeltaDimension_pullback_snd_comp_of_nonempty :
    ¬ ∀ (C : ChowSituation.{u}) {X Y Z : Scheme.{u}} (g : Y ⟶ C.S) [LocallyOfFiniteType g]
      (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f] (r : ℕ)
      (_ : AlgebraicGeometry.RelativeDimension f r) (i : Z ⟶ Y) [IsClosedImmersion i],
      Nonempty (pullback f i : Scheme.{u}) →
        schemeDeltaDimension C (pullback.snd f i ≫ i ≫ g) =
          schemeDeltaDimension C (i ≫ g) + ((r : ℤ) : EInt)
```

## Tag 02R9, a lemma

[Tag 02R9](https://stacks.math.columbia.edu/tag/02R9) in the Stacks Project.

Declarations registered for the tag:

- [`LocallyFinite.preimage_continuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyFinite.preimage_continuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/LocallyFinitePreimage.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/LocallyFinitePreimage.lean#L41) (StacksFrontier): “the inverse image of a locally finite collection of subsets along a continuous map is locally finite”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.13, Tag 02R7](https://stacks.math.columbia.edu/tag/02R7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
