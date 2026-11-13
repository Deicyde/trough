---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsCategoricalQuotient, AlgebraicGeometry.Space.IsCategoricalQuotientIn, AlgebraicGeometry.Space.IsCategoricalQuotientInSchemes, AlgebraicGeometry.Space.categoricalQuotient_unique, AlgebraicGeometry.Space.categoricalQuotientIn_unique, AlgebraicGeometry.Space.IsUniversalCategoricalQuotientIn, AlgebraicGeometry.Space.IsUniformCategoricalQuotientIn, AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotient
statement: formalized
proof: formalized
---

# 83.4 Categorical quotients

Section 83.4 of the Stacks Project, [Tag 048I](https://stacks.math.columbia.edu/tag/048I). 5 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 048J, a definition

[Tag 048J](https://stacks.math.columbia.edu/tag/048J) in the Stacks Project.

**`AlgebraicGeometry.Space.IsCategoricalQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L57). The attribute's comment: “part (1): algebraic spaces”.

> A morphism `φ : U ⟶ X` of algebraic spaces over `B` is a *categorical quotient* of a
> pre-relation `j` when it is invariant under `j` and every invariant morphism out of `U` factors
> uniquely through it.

```lean
noncomputable abbrev IsCategoricalQuotient {R U X : Over B} (j : PreRelation R U)
    (φ : U ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsCategoricalQuotientIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L67). The attribute's comment: “part (2): full subcategory”.

> A morphism `φ : U ⟶ X` is a *categorical quotient in the full subcategory* cut out by an object
> property `P` when `R`, `U` and `X` lie in it and the universal property of a categorical quotient
> holds against the objects of `P`.

```lean
noncomputable abbrev IsCategoricalQuotientIn (P : ObjectProperty (Over B)) {R U X : Over B}
    (j : PreRelation R U) (φ : U ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsCategoricalQuotientInSchemes`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L77). The attribute's comment: “part (3): schemes”.

> A morphism `φ : U ⟶ X` of schemes over `T` is a *categorical quotient* of a pre-relation of
> schemes when it equalizes the target and the source of the pre-relation and every morphism out of
> `U` which does so factors uniquely through it.

```lean
noncomputable abbrev IsCategoricalQuotientInSchemes {T : Scheme.{u}} {R U X : Over T}
    (j : Stacks.Groupoids.PreRelation R U) (φ : U ⟶ X) : Prop
```

## Tag 048K, a lemma

[Tag 048K](https://stacks.math.columbia.edu/tag/048K) in the Stacks Project.

**`AlgebraicGeometry.Space.categoricalQuotient_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L105). The attribute's comment: “algebraic spaces over the base”.

> Two categorical quotients of a pre-relation of algebraic spaces over `B` are uniquely
> isomorphic over `B`, compatibly with their quotient maps.

```lean
theorem categoricalQuotient_unique {R U X Y : Over B} (j : PreRelation R U) (φ : U ⟶ X)
    (ψ : U ⟶ Y) (hφ : IsCategoricalQuotient j φ) (hψ : IsCategoricalQuotient j ψ) :
    ∃! e : X ≅ Y, φ ≫ e.hom = ψ
```

**`AlgebraicGeometry.Space.categoricalQuotientIn_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L114). The attribute's comment: “full subcategories”.

> Two categorical quotients of a pre-relation in the full subcategory cut out by an object
> property are uniquely isomorphic within that subcategory, compatibly with their quotient maps.

```lean
theorem categoricalQuotientIn_unique (P : ObjectProperty (Over B)) {R U X Y : Over B}
    (j : PreRelation R U) (φ : U ⟶ X) (ψ : U ⟶ Y)
    (hφ : IsCategoricalQuotientIn P j φ) (hψ : IsCategoricalQuotientIn P j ψ) :
    ∃! e : X ≅ Y, φ ≫ e.hom = ψ
```

## Tag 049V, an example

[Tag 049V](https://stacks.math.columbia.edu/tag/049V) in the Stacks Project.

**`AlgebraicGeometry.Space.IsCategoricalQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L57). The attribute's comment: “items (2)-(5): the separated, quasi-separated, locally separated and decent”.

> A morphism `φ : U ⟶ X` of algebraic spaces over `B` is a *categorical quotient* of a
> pre-relation `j` when it is invariant under `j` and every invariant morphism out of `U` factors
> uniquely through it.

```lean
noncomputable abbrev IsCategoricalQuotient {R U X : Over B} (j : PreRelation R U)
    (φ : U ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsCategoricalQuotientIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L67). The attribute's comment: “items (2)-(5): the separated, quasi-separated, locally separated and decent”.

> A morphism `φ : U ⟶ X` is a *categorical quotient in the full subcategory* cut out by an object
> property `P` when `R`, `U` and `X` lie in it and the universal property of a categorical quotient
> holds against the objects of `P`.

```lean
noncomputable abbrev IsCategoricalQuotientIn (P : ObjectProperty (Over B)) {R U X : Over B}
    (j : PreRelation R U) (φ : U ⟶ X) : Prop
```

**`AlgebraicGeometry.Space.IsCategoricalQuotientInSchemes`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotient.lean#L77). The attribute's comment: “items (2)-(5): the separated, quasi-separated, locally separated and decent”.

> A morphism `φ : U ⟶ X` of schemes over `T` is a *categorical quotient* of a pre-relation of
> schemes when it equalizes the target and the source of the pre-relation and every morphism out of
> `U` which does so factors uniquely through it.

```lean
noncomputable abbrev IsCategoricalQuotientInSchemes {T : Scheme.{u}} {R U X : Over T}
    (j : Stacks.Groupoids.PreRelation R U) (φ : U ⟶ X) : Prop
```

## Tag 048L, a definition

[Tag 048L](https://stacks.math.columbia.edu/tag/048L) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUniversalCategoricalQuotientIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean#L236). The attribute's comment: “part (1): universal categorical quotient”.

> **Stacks 048L, part (1).** An `R`-invariant morphism `φ : U ⟶ X` is a *universal
> categorical quotient* in a full subcategory `P` of the algebraic spaces over `B`, closed
> under fibre products, when `R`, `U` and `X` lie in `P` and for every morphism `f : X' ⟶ X`
> of `P` the projection `X' ×_X U ⟶ X'` is the categorical quotient in `P` of the base change
> of `j` along `f`.

```lean
abbrev IsUniversalCategoricalQuotientIn {B : AlgebraicSpaces site S hS}
    (P : ObjectProperty (Over B)) [P.IsClosedUnderLimitsOfShape WalkingCospan]
    {R U X : Over B} (j : PreRelation R U) (φ : U ⟶ X) (hφ : IsInvariant j φ.left) : Prop
```

**`AlgebraicGeometry.Space.IsUniformCategoricalQuotientIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/QuotientProperties.lean#L249). The attribute's comment: “part (2): uniform categorical quotient”.

> **Stacks 048L, part (2).** An `R`-invariant morphism `φ : U ⟶ X` is a *uniform
> categorical quotient* in a full subcategory `P` of the algebraic spaces over `B`, closed
> under fibre products, when `R`, `U` and `X` lie in `P` and for every flat morphism
> `f : X' ⟶ X` of `P` the projection `X' ×_X U ⟶ X'` is the categorical quotient in `P` of the
> base change of `j` along `f`.

```lean
abbrev IsUniformCategoricalQuotientIn {B : AlgebraicSpaces site S hS}
    (P : ObjectProperty (Over B)) [P.IsClosedUnderLimitsOfShape WalkingCospan]
    {R U X : Over B} (j : PreRelation R U) (φ : U ⟶ X) (hφ : IsInvariant j φ.left) : Prop
```

## Tag 049W, a lemma

[Tag 049W](https://stacks.math.columbia.edu/tag/049W) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean#L192). The attribute's comment: “algebraic spaces”.

> **Stacks 049W**, for algebraic spaces over the base. A categorical quotient of a reduced
> algebraic space is reduced. Unconditional.

```lean
theorem isReduced_of_isCategoricalQuotient
    {R U X : Over Base} (j : PreRelation R U) (φ : U ⟶ X)
    (hφ : IsCategoricalQuotient j φ)
    (hU : HasEtaleLocalProperty B S hS U.left.obj (fun Y : Scheme.{u} => IsReduced Y)) :
    HasEtaleLocalProperty B S hS X.left.obj (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotientInSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean#L206). The attribute's comment: “separated algebraic spaces”.

> **Stacks 049W**, for separated algebraic spaces. A categorical quotient in the full
> subcategory of separated algebraic spaces, of a reduced algebraic space, is reduced.
>
> The reduction of the target is separated because its inclusion is a closed immersion, hence a
> separated morphism by Stacks 04CH, and the target is separated — Stacks 04ZH, part (1).

```lean
theorem isReduced_of_isCategoricalQuotientInSeparated
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {R U X : Over Base} (j : PreRelation R U) (φ : U ⟶ X)
    (hφ : IsCategoricalQuotientIn
      (fun Y : Over Base => IsAbsolutelySeparated B S hS hZ Y.left.obj) j φ)
    (hU : HasEtaleLocalProperty B S hS U.left.obj (fun Y : Scheme.{u} => IsReduced Y)) :
    HasEtaleLocalProperty B S hS X.left.obj (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotientInQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean#L228). The attribute's comment: “quasi-separated algebraic spaces”.

> **Stacks 049W**, for quasi-separated algebraic spaces. A categorical quotient in the full
> subcategory of quasi-separated algebraic spaces, of a reduced algebraic space, is reduced.
>
> The inclusion of the reduction of the target is a closed immersion, hence separated by Stacks
> 04CH and so quasi-separated by Stacks 03KK; Stacks 04ZH, part (2) then transfers
> quasi-separatedness from the target.

```lean
theorem isReduced_of_isCategoricalQuotientInQuasiSeparated
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {R U X : Over Base} (j : PreRelation R U) (φ : U ⟶ X)
    (hφ : IsCategoricalQuotientIn
      (fun Y : Over Base => IsAbsolutelyQuasiSeparated B S hS hZ Y.left.obj) j φ)
    (hU : HasEtaleLocalProperty B S hS U.left.obj (fun Y : Scheme.{u} => IsReduced Y)) :
    HasEtaleLocalProperty B S hS X.left.obj (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotientInLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean#L251). The attribute's comment: “locally separated algebraic spaces”.

> **Stacks 049W**, for locally separated algebraic spaces. A categorical quotient in the full
> subcategory of locally separated algebraic spaces, of a reduced algebraic space, is reduced.
>
> The inclusion of the reduction of the target is a closed immersion, hence separated by Stacks
> 04CH and so locally separated by Stacks 03KK; Stacks 04ZH, part (3) then transfers local
> separatedness from the target.

```lean
theorem isReduced_of_isCategoricalQuotientInLocallySeparated
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {R U X : Over Base} (j : PreRelation R U) (φ : U ⟶ X)
    (hφ : IsCategoricalQuotientIn
      (fun Y : Over Base => IsAbsolutelyLocallySeparated B S hS hZ Y.left.obj) j φ)
    (hU : HasEtaleLocalProperty B S hS U.left.obj (fun Y : Scheme.{u} => IsReduced Y)) :
    HasEtaleLocalProperty B S hS X.left.obj (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotientInDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean#L274). The attribute's comment: “decent algebraic spaces”.

> **Stacks 049W**, for decent algebraic spaces. A categorical quotient in the full
> subcategory of decent algebraic spaces, of a reduced algebraic space, is reduced.
>
> The reduction of the target is decent because the inclusion of a closed subspace is
> representable and decency passes to the source of a representable morphism — Stacks 03KF for
> property `(γ)`, which is condition (4) of Stacks 03JV.

```lean
theorem isReduced_of_isCategoricalQuotientInDecent
    {R U X : Over Base} (j : PreRelation R U) (φ : U ⟶ X)
    (hφ : IsCategoricalQuotientIn
      (fun Y : Over Base => IsDecentSpace B S hS Y.left.obj) j φ)
    (hU : HasEtaleLocalProperty B S hS U.left.obj (fun Y : Scheme.{u} => IsReduced Y)) :
    HasEtaleLocalProperty B S hS X.left.obj (fun Y : Scheme.{u} => IsReduced Y)
```

**`AlgebraicGeometry.Space.isReduced_of_isCategoricalQuotientInSchemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Quotients/CategoricalQuotientReduced.lean#L294). The attribute's comment: “schemes”. References: SGA 3 VIB (9.2), “more general”.

> **Stacks 049W**, for schemes. A categorical quotient in the category of schemes over a base
> scheme, of a reduced scheme, is reduced.
>
> Unconditional: the reduction of a scheme is its closed subscheme cut out by the nilradical, and
> a morphism from a reduced scheme factors uniquely through it by Stacks 0356.

```lean
theorem isReduced_of_isCategoricalQuotientInSchemes
    {T : Scheme.{u}} {R U X : Over T} (j : Stacks.Groupoids.PreRelation R U)
    (φ : U ⟶ X) (hφ : IsCategoricalQuotientInSchemes j φ)
    (hU : IsReduced U.left) : IsReduced X.left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 83.4, Tag 048I](https://stacks.math.columbia.edu/tag/048I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
