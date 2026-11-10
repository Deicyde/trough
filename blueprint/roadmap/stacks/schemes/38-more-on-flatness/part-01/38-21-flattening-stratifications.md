---
declaration: section
origin: cited
lean: AlgebraicGeometry.FlatnessSituation.HasUniversalFlattening, AlgebraicGeometry.HasUniversalFlattening, AlgebraicGeometry.PlaneFlatteningExample.flatFunctor_unique_isEmpty_not_representable, AlgebraicGeometry.FlatnessSituation.HasFlatteningStratification, AlgebraicGeometry.HasFlatteningStratification
statement: formalized
proof: formalized
---

# 38.21 Flattening stratifications

Section 38.21 of the Stacks Project, [Tag 052F](https://stacks.math.columbia.edu/tag/052F). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05P6, a definition

[Tag 05P6](https://stacks.math.columbia.edu/tag/05P6) in the Stacks Project.

**`AlgebraicGeometry.FlatnessSituation.HasUniversalFlattening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean#L48). The attribute's comment: “the universal flattening of a module”.

> A quasi-coherent module admits a universal flattening when its flatness functor is
> represented by a scheme over the base.

```lean
public noncomputable abbrev FlatnessSituation.HasUniversalFlattening
    (D : FlatnessSituation.{u}) : Prop
```

**`AlgebraicGeometry.HasUniversalFlattening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean#L63). The attribute's comment: “the universal flattening of a scheme”.

> A scheme over `S` admits a universal flattening when its structure sheaf does.

```lean
public noncomputable abbrev HasUniversalFlattening {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 0FJ1, an example

[Tag 0FJ1](https://stacks.math.columbia.edu/tag/0FJ1) in the Stacks Project.

**`AlgebraicGeometry.PlaneFlatteningExample.flatFunctor_unique_isEmpty_not_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/PlaneExampleNotRepresentable.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/PlaneExampleNotRepresentable.lean#L254).

> **Stacks 0FJ1.** Let `k` be a field, `X = S = Spec k[x, y]` and `𝓕` the quasi-coherent
> module associated to `k[x, x⁻¹, y]/(y)`, with flatness functor `F_flat`, and write
> `F_flat(A) = F_flat(Spec A)` for a `k[x, y]`-algebra `A`.  Then `F_flat(k[x, y]/(x, y)^n)` is a
> singleton for every `n`, while `F_flat(k[[x, y]])` is empty.  Hence `F_flat` is not
> representable even by an algebraic space (on any big fppf site containing `Spec k[[x, y]]`, the
> restriction of `F_flat` is isomorphic to no algebraic space over `S`), and in particular it is
> not representable by a scheme over `S`: the universal flattening of `𝓕` does not exist.

```lean
public theorem flatFunctor_unique_isEmpty_not_representable (E : PlaneFlatteningExample.{u}) :
    (∀ n : ℕ, Nonempty (Unique (E.flatValue (E.R ⧸ Ideal.span ({E.x, E.y} : Set E.R) ^ n)))) ∧
    IsEmpty (E.flatValue E.formalPlane) ∧
    (∀ (B : BigFppfSite.{u}) (hS : B.Contains E.X), B.Contains (Spec (.of E.formalPlane)) →
      ¬ ∃ X : (BigFppfOver B E.X hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B E.X hS X ∧
        Nonempty (X ≅ (Over.post B.inclusion).op ⋙
          E.flatnessSituation.flatFunctor ⋙ uliftFunctor)) ∧
    ¬ E.flatnessSituation.flatFunctor.IsRepresentable
```

## Tag 05P7, a definition

[Tag 05P7](https://stacks.math.columbia.edu/tag/05P7) in the Stacks Project.

**`AlgebraicGeometry.FlatnessSituation.HasFlatteningStratification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean#L74). The attribute's comment: “the module”.

> A quasi-coherent module has a flattening stratification if its flatness functor is
> represented by the monomorphism associated to a locally finite scheme-theoretic stratification
> of the base: closed subschemes `J i`, indexed by a partial order, whose supports cover `S` and
> form a locally finite family, with `J i ⊔ J j` the infimum of the `J k` for `k ≤ i` and `k ≤ j`,
> together with opens `U i` of the subschemes `J i` whose images are the supports of `J i` minus
> those of the `J j` with `j < i`, such that the representing object is isomorphic over `S` to the
> coproduct of the `U i` and its structure morphism is a monomorphism.

```lean
public def FlatnessSituation.HasFlatteningStratification (D : FlatnessSituation.{u}) : Prop
```

**`AlgebraicGeometry.HasFlatteningStratification`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/FlatteningStratification/Basic.lean#L91). The attribute's comment: “the scheme”.

> A scheme over `S` has a flattening stratification when its structure sheaf does.

```lean
public abbrev HasFlatteningStratification {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.21, Tag 052F](https://stacks.math.columbia.edu/tag/052F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
