---
declaration: section
origin: cited
lean: AlgebraicGeometry.SpecToEquivOfLocalRing, AlgebraicGeometry.Scheme.fromSpecStalk, AlgebraicGeometry.pointsEquivFieldValuedPointClasses, AlgebraicGeometry.FieldValuedPoint.hasCommonExtension_iff_point_eq, AlgebraicGeometry.FieldValuedPoint.canonical_isSmallest, AlgebraicGeometry.FieldValuedPoint.uniqueIso_of_isSmallest, AlgebraicGeometry.Scheme.SpecToEquivOfField
statement: formalized
proof: formalized
---

# 26.13 Points of schemes

Section 26.13 of the Stacks Project, [Tag 01J5](https://stacks.math.columbia.edu/tag/01J5). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01J6, a lemma

[Tag 01J6](https://stacks.math.columbia.edu/tag/01J6) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.SpecToEquivOfLocalRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.SpecToEquivOfLocalRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L316) (StacksFrontier). References: EGA I (2.4.4); EGA I (3.4.5); SGA 3 XV (1.4), “partial”.

## Tag 02NA, an equation

[Tag 02NA](https://stacks.math.columbia.edu/tag/02NA) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.fromSpecStalk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.fromSpecStalk#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/CanonicalMorphismFromLocalRing.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/CanonicalMorphismFromLocalRing.lean#L20) (StacksFrontier): “the canonical morphism `Spec 𝒪_{X, x} ⟶ X`”. References: EGA I (2.4.2); EGA I (2.4.7), “zero ideal a\_y = 0”; EGA IV (5.9.6).

## Tag 01J9, a lemma

[Tag 01J9](https://stacks.math.columbia.edu/tag/01J9) in the Stacks Project.

**`AlgebraicGeometry.pointsEquivFieldValuedPointClasses`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean#L102). The attribute's comment: “the bijection with equivalence classes”.

> Points of a scheme correspond bijectively to equivalence classes of field-valued points.

```lean
noncomputable def pointsEquivFieldValuedPointClasses (X : Scheme.{u}) :
    X ≃ Quotient (FieldValuedPoint.setoid X)
```

**`AlgebraicGeometry.FieldValuedPoint.hasCommonExtension_iff_point_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean#L121). The attribute's comment: “the common-extension relation”. References: EGA I (3.4.5), “location map”.

> Two field-valued points have a common field-valued extension if and only if they have the same
> image point.

```lean
theorem hasCommonExtension_iff_point_eq {X : Scheme.{u}} (p q : FieldValuedPoint X) :
    p.HasCommonExtension q ↔ p.point = q.point
```

**`AlgebraicGeometry.FieldValuedPoint.canonical_isSmallest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean#L171). The attribute's comment: “the smallest representative”. References: EGA I (2.4.6), “factorization via κ(x)”.

> The canonical morphism `Spec(κ(x)) ⟶ X` is the smallest representative of the equivalence
> class corresponding to `x`.

```lean
theorem canonical_isSmallest {X : Scheme.{u}} (x : X) :
    (canonical X x).IsSmallest
```

**`AlgebraicGeometry.FieldValuedPoint.uniqueIso_of_isSmallest`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean#L195). The attribute's comment: “uniqueness up to unique isomorphism”.

> Any two smallest representatives of the same point are uniquely isomorphic over `X`.

```lean
theorem uniqueIso_of_isSmallest {X : Scheme.{u}} {p q : FieldValuedPoint X}
    (hp : p.IsSmallest) (hq : q.IsSmallest) (h : p.point = q.point) :
    ∃! e : Spec (.of p.carrier) ≅ Spec (.of q.carrier), e.hom ≫ q.map = p.map
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.SpecToEquivOfField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.SpecToEquivOfField#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Points/FieldValued.lean#L52) (StacksFrontier): “morphisms from the spectrum of a fixed field”. References: EGA I (2.4.6); EGA I (3.4.5), “partial, special case”; EGA II (1.7.10), “Opening clause”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.13, Tag 01J5](https://stacks.math.columbia.edu/tag/01J5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
