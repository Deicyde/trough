---
declaration: section
origin: cited
lean: Stacks.Groupoids.PreRelation, Stacks.Groupoids.PreRelation.target, Stacks.Groupoids.PreRelation.source, Stacks.Groupoids.IsPreEquivalenceRelation, CategoryTheory.Mono, CategoryTheory.IsEquivalenceRelation, AlgebraicGeometry.PreRelation.restrict, AlgebraicGeometry.PreRelation.isPreEquivalenceRelation_restrict
statement: formalized
proof: formalized
---

# 39.3 Equivalence relations

Section 39.3 of the Stacks Project, [Tag 022O](https://stacks.math.columbia.edu/tag/022O). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 022P, a definition

[Tag 022P](https://stacks.math.columbia.edu/tag/022P) in the Stacks Project.

**`Stacks.Groupoids.PreRelation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L64). The attribute's comment: “part (1): pre-relation”.

> **Stacks 022P, part (1).** A *pre-relation* from `R` to `U` over `S` is a morphism of
> `S`-schemes from `R` to the product `U ×_S U`.

```lean
abbrev PreRelation (R U : Over S)
```

**`Stacks.Groupoids.PreRelation.target`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L73). The attribute's comment: “part (1): target”.

> **Stacks 022P, part (1).** The *target* map of a pre-relation, its composite with the
> first projection of the product.

```lean
noncomputable abbrev target : R ⟶ U
```

**`Stacks.Groupoids.PreRelation.source`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L78). The attribute's comment: “part (1): source”.

> **Stacks 022P, part (1).** The *source* map of a pre-relation, its composite with the
> second projection of the product.

```lean
noncomputable abbrev source : R ⟶ U
```

**`Stacks.Groupoids.IsPreEquivalenceRelation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L91). The attribute's comment: “part (3): pre-equivalence relation”. References: SGA 3 IV (3.1), “pre-equiv. relation def”.

> **Stacks 022P, part (3).** A pre-relation is a *pre-equivalence relation* when the
> relation it induces on the `T`-valued points of `U` is an equivalence relation for every
> scheme `T` over `S`.

```lean
abbrev IsPreEquivalenceRelation {R U : Over S} (j : PreRelation R U) : Prop
```

Declarations registered for the tag:

- [`CategoryTheory.Mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L94) (StacksFrontier): “part (2): relation”. References: EGA IV (8.11.5.1); SGA 1 V (3.6); SGA 3 VIIB (2.4.1); SGA 3 VIII (3.4); SGA 4 I (10.4); SGA 4 II (3.2).
- [`CategoryTheory.IsEquivalenceRelation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsEquivalenceRelation#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EquivalenceRelations.lean#L95) (StacksFrontier): “part (4): equivalence relation”. References: SGA 3 IV (3.1.1); SGA 4 I (10.9); SGA 4 IV (9.8.2).

## Tag 02V8, a lemma

[Tag 02V8](https://stacks.math.columbia.edu/tag/02V8) in the Stacks Project.

**`AlgebraicGeometry.PreRelation.restrict`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L292). The attribute's comment: “the restricted pre-relation”.

> The restriction of a pre-relation along `g`.

```lean
noncomputable abbrev restrict (g : U' ⟶ U) :
    Stacks.Groupoids.PreRelation (restriction j g) U'
```

**`AlgebraicGeometry.PreRelation.isPreEquivalenceRelation_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L301). The attribute's comment: “preservation of pre-equivalence relations”.

> Restriction preserves pre-equivalence relations.

```lean
theorem isPreEquivalenceRelation_restrict (g : U' ⟶ U)
    (hj : Stacks.Groupoids.IsPreEquivalenceRelation j) :
    Stacks.Groupoids.IsPreEquivalenceRelation (restrict j g)
```

**`AlgebraicGeometry.PreRelation.isEquivalenceRelation_restrict`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L325). The attribute's comment: “preservation of equivalence relations”.

> Restriction preserves equivalence relations.

```lean
instance isEquivalenceRelation_restrict (g : U' ⟶ U)
    [hj : CategoryTheory.IsEquivalenceRelation j.target j.source] :
    CategoryTheory.IsEquivalenceRelation (restrict j g).target (restrict j g).source
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.pullback.fst_of_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.pullback.fst_of_mono#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L296) (StacksFrontier): “preservation of relations”. References: EGA I (3.3.12), “more general”.

## Tag 02V9, a definition

[Tag 02V9](https://stacks.math.columbia.edu/tag/02V9) in the Stacks Project.

**`AlgebraicGeometry.PreRelation.restrict`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L292). The attribute's comment: “the restriction R|\_\{U'} of a pre-relation along U' -> U”.

> The restriction of a pre-relation along `g`.

```lean
noncomputable abbrev restrict (g : U' ⟶ U) :
    Stacks.Groupoids.PreRelation (restriction j g) U'
```

## Tag 022Q, a lemma

[Tag 022Q](https://stacks.math.columbia.edu/tag/022Q) in the Stacks Project.

**`AlgebraicGeometry.PreRelation.equivalence_sourceTargetRel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L225).

> **Stacks Project, Tag 022Q.** A pre-equivalence relation induces an equivalence relation on
> the underlying points of the scheme.

```lean
theorem equivalence_sourceTargetRel {R U : Over S} (j : Stacks.Groupoids.PreRelation R U)
    (hj : Stacks.Groupoids.IsPreEquivalenceRelation j) :
    Equivalence (Function.SourceTargetRel j.source.left.base j.target.left.base)
```

Declarations registered for the tag:

- [`Function.SourceTargetRel`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Separation/KolmogorovQuotient.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Relations/PreRelations.lean#L131) (StacksFrontier): “the relation on points”.

## Tag 0DT7, a lemma

[Tag 0DT7](https://stacks.math.columbia.edu/tag/0DT7) in the Stacks Project.

**`AlgebraicGeometry.isEquivalenceRelation_of_unramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/EquivalenceRelation/Unramified.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/EquivalenceRelation/Unramified.lean#L89).

> **Stacks Project, Tag 0DT7.** An unramified pre-relation which is an equivalence relation on
> points over every algebraically closed field, and whose reflexivity, symmetry, and composition
> operations are represented by morphisms, is an equivalence relation.

```lean
theorem isEquivalenceRelation_of_unramified
    {S : Scheme.{u}} {R U : Over S} (j : PreRelation R U)
    [Unramified j.source.left] [Unramified j.target.left]
    (hpoints : ∀ (k : Type u) [Field k] [IsAlgClosed k]
      (p : Spec (.of k) ⟶ S),
      (Function.Injective (fun r : Over.mk p ⟶ R ↦ r ≫ j) ∧
        Equivalence (j.Rel (T := Over.mk p))))
    (e : U ⟶ R)
    (he_target : e ≫ j.target = 𝟙 U)
    (he_source : e ≫ j.source = 𝟙 U)
    (i : R ⟶ R)
    (hi_target : i ≫ j.target = j.source)
    (hi_source : i ≫ j.source = j.target)
    (c : pullback j.source j.target ⟶ R)
    (hc_target : c ≫ j.target = pullback.fst j.source j.target ≫ j.target)
    (hc_source : c ≫ j.source = pullback.snd j.source j.target ≫ j.source) :
    IsEquivalenceRelation j.target j.source
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.3, Tag 022O](https://stacks.math.columbia.edu/tag/022O)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
