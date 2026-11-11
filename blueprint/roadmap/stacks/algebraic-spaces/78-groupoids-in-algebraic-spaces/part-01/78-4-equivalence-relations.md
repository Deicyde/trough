---
declaration: section
origin: cited
lean: AlgebraicGeometry.AlgebraicSpaces.hasPullbacks, AlgebraicGeometry.Space.hasBinaryProducts_over_algebraicSpace, AlgebraicGeometry.Space.PreRelation, AlgebraicGeometry.Space.PreRelation.target, AlgebraicGeometry.Space.PreRelation.source, AlgebraicGeometry.Space.IsPreEquivalenceRelation, AlgebraicGeometry.Space.isEquivalenceRelation_iff_mono_and_isPreEquivalenceRelation, CategoryTheory.Mono
statement: formalized
proof: formalized
---

# 78.4 Equivalence relations

Section 78.4 of the Stacks Project, [Tag 043B](https://stacks.math.columbia.edu/tag/043B). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 043C, a definition

[Tag 043C](https://stacks.math.columbia.edu/tag/043C) in the Stacks Project.

**`AlgebraicGeometry.AlgebraicSpaces.hasPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Category.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L432). The attribute's comment: “fibre products of algebraic spaces”.

> The category of algebraic spaces over a scheme has fibre products: they are the presheaf
> fibre products, which are again algebraic spaces.

```lean
instance hasPullbacks : HasPullbacks (AlgebraicSpaces B S hS)
```

**`AlgebraicGeometry.Space.hasBinaryProducts_over_algebraicSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits.lean#L99). The attribute's comment: “products over a base algebraic space”.

> The category of algebraic spaces over `S` equipped with a morphism to a fixed algebraic space
> `Z` has binary products, namely the fibre products over `Z`.

```lean
noncomputable instance hasBinaryProducts_over_algebraicSpace
    (Z : AlgebraicSpaces B S hS) : HasBinaryProducts (Over Z)
```

**`AlgebraicGeometry.Space.PreRelation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L130). The attribute's comment: “part (1): pre-relation”.

> **Stacks 043C, part (1).** A *pre-relation* from `R` to `U` is a morphism from `R` to
> the product `U ⨯ U`.
>
> This is stated for an arbitrary category with binary products because the two bases it is
> taken over are different categories. Over a base algebraic space `Z` it is instantiated at
> the slice `CategoryTheory.Over Z` of presheaves on the big fppf site, whose categorical
> product is the fibre product `U ×_Z U`, which is the notion of the source; over an
> algebraic space `B` it is instantiated at the slice `CategoryTheory.Over B` of the category
> `AlgebraicGeometry.AlgebraicSpaces`, which is the shape the invariance notions of **Stacks
> 048E** in `StacksFrontier/AlgebraicGeometry/Spaces/InvariantMorphisms.lean` are stated at.

```lean
abbrev PreRelation (R U : C)
```

**`AlgebraicGeometry.Space.PreRelation.target`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L139). The attribute's comment: “part (1): target”.

> **Stacks 043C, part (1).** The *target* map of a pre-relation, its composite with the
> first projection of the product.

```lean
noncomputable abbrev target : R ⟶ U
```

**`AlgebraicGeometry.Space.PreRelation.source`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L144). The attribute's comment: “part (1): source”.

> **Stacks 043C, part (1).** The *source* map of a pre-relation, its composite with the
> second projection of the product.

```lean
noncomputable abbrev source : R ⟶ U
```

**`AlgebraicGeometry.Space.IsPreEquivalenceRelation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L188). The attribute's comment: “part (3): pre-equivalence relation”.

> **Stacks 043C, part (3).** A pre-relation is a *pre-equivalence relation* when the
> relation it induces on the `U`-valued points is an equivalence relation for every test
> scheme over the base.

```lean
abbrev IsPreEquivalenceRelation {R U : Over Z} (j : PreRelation R U) : Prop
```

**`AlgebraicGeometry.Space.isEquivalenceRelation_iff_mono_and_isPreEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L279). The attribute's comment: “parts (2)-(4): pointwise characterization”.

> **Stacks 043C, parts (2)-(4).** A pre-relation of algebraic spaces over `Z` is an
> internal categorical equivalence relation exactly when it is a monomorphism and the
> relation it induces on the points of every test scheme over `Z` is an equivalence
> relation.

```lean
theorem isEquivalenceRelation_iff_mono_and_isPreEquivalenceRelation
    {R U : Over Z} (j : PreRelation R U) :
    CategoryTheory.IsEquivalenceRelation j.target j.source ↔
      (CategoryTheory.Mono j ∧ IsPreEquivalenceRelation j)
```

Declarations registered for the tag:

- [`CategoryTheory.Mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L191) (StacksFrontier): “part (2): relation”. References: EGA IV (8.11.5.1); SGA 1 V (3.6); SGA 3 VIIB (2.4.1); SGA 3 VIII (3.4); SGA 4 I (10.4); SGA 4 II (3.2).
- [`CategoryTheory.IsEquivalenceRelation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsEquivalenceRelation#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelationsOverSpace.lean#L192) (StacksFrontier): “part (4): equivalence relation”. References: SGA 3 IV (3.1.1); SGA 4 I (10.9); SGA 4 IV (9.8.2).

## Tag 043D, a lemma

[Tag 043D](https://stacks.math.columbia.edu/tag/043D) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.restrict`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean#L89). The attribute's comment: “the restricted pre-relation”.

> **Stacks 043D.** The restriction of a pre-relation along a morphism `g : U' ⟶ U` over `Z`,
> that is the first projection of the pullback defining `restriction`.

```lean
noncomputable abbrev restrict (g : U' ⟶ U) : PreRelation (restriction j g) U'
```

**`AlgebraicGeometry.Space.PreRelation.isPreEquivalenceRelation_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean#L110). The attribute's comment: “preservation of pre-equivalence relations”.

> **Stacks 043D.** Restriction preserves pre-equivalence relations.

```lean
theorem isPreEquivalenceRelation_restrict (g : U' ⟶ U) (hj : IsPreEquivalenceRelation j) :
    IsPreEquivalenceRelation (restrict j g)
```

**`AlgebraicGeometry.Space.PreRelation.isEquivalenceRelation_restrict`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean#L157). The attribute's comment: “preservation of equivalence relations”.

> **Stacks 043D.** Restriction preserves equivalence relations.

```lean
instance isEquivalenceRelation_restrict (g : U' ⟶ U)
    [hj : IsEquivalenceRelation j.target j.source] :
    IsEquivalenceRelation (restrict j g).target (restrict j g).source
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.pullback.fst_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.pullback.fst_of_mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean#L92) (StacksFrontier): “preservation of relations”. References: EGA I (3.3.12), “more general”.

## Tag 043E, a definition

[Tag 043E](https://stacks.math.columbia.edu/tag/043E) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.restrict`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/Restriction.lean#L89). The attribute's comment: “the restriction `R|_{U'}` of a pre-relation along `g : U' ⟶ U`”.

> **Stacks 043D.** The restriction of a pre-relation along a morphism `g : U' ⟶ U` over `Z`,
> that is the first projection of the pullback defining `restriction`.

```lean
noncomputable abbrev restrict (g : U' ⟶ U) : PreRelation (restriction j g) U'
```

## Tag 043F, a lemma

[Tag 043F](https://stacks.math.columbia.edu/tag/043F) in the Stacks Project.

**`AlgebraicGeometry.Space.PreRelation.isPreEquivalenceRelation_sourceTargetRel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RelationOnPoints.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RelationOnPoints.lean#L236).

> A pre-equivalence relation `j : R ⟶ U ×_Z U` induces an equivalence relation on `|U|`:
> `x` is related to `y` when some point `r` of `|R|` has `t(r) = x` and `s(r) = y`.

```lean
theorem isPreEquivalenceRelation_sourceTargetRel (hj : IsPreEquivalenceRelation j) :
    Equivalence
      (Function.SourceTargetRel
        (pointsMap B S hS R.left j.source.left)
        (pointsMap B S hS R.left j.target.left))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.4, Tag 043B](https://stacks.math.columbia.edu/tag/043B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
