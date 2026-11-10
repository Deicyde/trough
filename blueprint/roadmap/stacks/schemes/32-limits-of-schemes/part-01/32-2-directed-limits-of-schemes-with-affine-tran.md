---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLimitPullbackCone, AlgebraicGeometry.hasLimit_of_isCofiltered_of_isAffineHom, AlgebraicGeometry.isAffineHom_π_app, AlgebraicGeometry.isLimitOpensCone, AlgebraicGeometry.Scheme.affineLimitCone, AlgebraicGeometry.Scheme.hasLimit_of_isAffine
statement: formalized
proof: formalized
---

# 32.2 Directed limits of schemes with affine transition maps

Section 32.2 of the Stacks Project, [Tag 01YV](https://stacks.math.columbia.edu/tag/01YV). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01YV, the section

[Tag 01YV](https://stacks.math.columbia.edu/tag/01YV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.isLimitPullbackCone`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/BaseChange.lean#L132), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/BaseChange.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/BaseChange.lean#L151) (StacksFrontier): “base change commutes with the limit of the system (Lemma 01YZ)”.
- [`AlgebraicGeometry.hasLimit_of_isCofiltered_of_isAffineHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L605), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L631) (StacksFrontier): “the construction of the limit of an inverse system of schemes whose transition morphisms are affine (Lemma 01YX)”.
- [`AlgebraicGeometry.isAffineHom_π_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineHom_π_app#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L634) (StacksFrontier): “the projections of the limit are affine (Lemma 01YX (1))”. References: EGA IV (8.13.4), “partial”.
- [`AlgebraicGeometry.isLimitOpensCone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isLimitOpensCone#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L636) (StacksFrontier): “the inverse image of an open subscheme under a projection is the limit of its inverse images (Lemma 01YX (2))”.
- [`AlgebraicGeometry.Scheme.affineLimitCone`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean#L54), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean#L89) (StacksFrontier): “the construction of the limit when all the schemes of the system are affine: the limit cone is `Spec` of the colimit of the rings of global sections (Lemma 01YW)”.
- [`AlgebraicGeometry.Scheme.hasLimit_of_isAffine`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean#L69), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean#L92) (StacksFrontier): “existence of the limit when all the schemes of the system are affine (Lemma 01YW)”.

## Tag 01YW, a lemma

[Tag 01YW](https://stacks.math.columbia.edu/tag/01YW) in the Stacks Project.

**`AlgebraicGeometry.Scheme.affineLimitCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean#L54). The attribute's comment: “the limit cone, as Spec of the colimit of global sections”. References: SGA 4 VII (5.1), “all schemes affine”.

> The limit cone of a diagram of affine schemes, with apex `Spec` applied to the limit in
> `CommRingCatᵒᵖ` of the diagram of rings of global sections.

```lean
noncomputable def affineLimitCone : LimitCone D
```

**`AlgebraicGeometry.Scheme.hasLimit_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/AffineTransition.lean#L69). The attribute's comment: “existence of the limit”. References: SGA 4 VII (5.1), “all schemes affine”.

> A diagram of affine schemes has a limit in the category of schemes.

```lean
theorem hasLimit_of_isAffine : HasLimit D
```

## Tag 01YX, a lemma

[Tag 01YX](https://stacks.math.columbia.edu/tag/01YX) in the Stacks Project.

**`AlgebraicGeometry.hasLimit_of_isCofiltered_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L605). The attribute's comment: “existence”. References: SGA 4 VII (5.1), “existence of lim”.

> **Limits of inverse systems with affine transition morphisms.** A cofiltered diagram of
> schemes whose transition morphisms are affine has a limit in the category of schemes.
>
> The limit is constructed by gluing, over the affine opens `U` of a fixed stage `D i₀`, the
> affine schemes `lim_j (D j ×_{D i₀} U)`; see
> `AlgebraicGeometry.CofilteredLimit.hasLimit_of_isAffineHom_of_isCofiltered`.

```lean
theorem hasLimit_of_isCofiltered_of_isAffineHom
    {I : Type u} [Category.{u} I] [IsCofiltered I] (D : I ⥤ Scheme.{u})
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)] : HasLimit D
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isAffineHom_π_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineHom_π_app#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L622) (StacksFrontier): “part (1)”. References: EGA IV (8.13.4), “partial”.
- [`AlgebraicGeometry.isLimitOpensCone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isLimitOpensCone#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/Basic.lean#L624) (StacksFrontier): “part (2)”.

## Tag 01YZ, a lemma

[Tag 01YZ](https://stacks.math.columbia.edu/tag/01YZ) in the Stacks Project.

**`AlgebraicGeometry.isLimitPullbackCone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CofilteredLimits/BaseChange.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CofilteredLimits/BaseChange.lean#L132).

> **Base change commutes with inverse limits of schemes.** Let `{ Dⱼ }` be an inverse system of
> schemes indexed by a cofiltered category, let `c` be a limit cone over it, let `i` be an index,
> and let `f : T ⟶ Dᵢ` be a scheme over the stage `Dᵢ`. Then
> `(lim Dⱼ) ×_{Dᵢ} T = lim_{j ≥ i} (Dⱼ ×_{Dᵢ} T)`.
>
> This is stated for an arbitrary limit cone `c`, so it applies in particular to the limit of a
> system with affine transition morphisms, whose existence is
> `AlgebraicGeometry.hasLimit_of_isCofiltered_of_isAffineHom`; that specialisation is recorded as
> `AlgebraicGeometry.isLimitPullbackConeLimitCone`.

```lean
def isLimitPullbackCone [IsCofiltered I] (i : I) (f : T ⟶ D.obj i) :
    IsLimit (pullbackCone D c i f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.2, Tag 01YV](https://stacks.math.columbia.edu/tag/01YV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
