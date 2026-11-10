---
declaration: section
origin: cited
lean: AlgebraicGeometry.integralClosure_baseField_toSubring_eq
statement: formalized
proof: formalized
---

# 33.31 Uniqueness of base field

Section 33.31 of the Stacks Project, [Tag 04MJ](https://stacks.math.columbia.edu/tag/04MJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04MK, a proposition

[Tag 04MK](https://stacks.math.columbia.edu/tag/04MK) in the Stacks Project.

**`AlgebraicGeometry.integralClosure_baseField_toSubring_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Defs/BaseFieldUniqueness.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Defs/BaseFieldUniqueness.lean#L479).

> **Stacks Project, Tag 04MK (Uniqueness of base field).**  Let `X` be a reduced connected
> scheme which is locally of finite type over a field `k₁` and also over a field `k₂`.  Then the
> integral closure of `k₁` in `Γ(X, 𝒪_X)` and the integral closure of `k₂` in `Γ(X, 𝒪_X)` are the
> same subring of `Γ(X, 𝒪_X)`.
>
> Each inclusion is `isIntegralElem_of_isIntegralElem`: locally of finite type over a field makes
> `X` locally Noetherian, hence covered by quasi-compact connected opens, and on such an open the
> two closures agree because Tag 04L7 makes the invertible global functions modulo either closure
> finitely generated, which by the Hilbert Nullstellensatz forces each closure to be finite over
> their intersection.  A monic polynomial over `k₂` killing a section on one such open then kills it
> globally, since its value is everywhere locally zero or a unit — the closures are fields by Tag
> 04MI — so its nonvanishing locus is clopen and `X` is connected.

```lean
theorem integralClosure_baseField_toSubring_eq (k₁ k₂ : Type u) [Field k₁] [Field k₂]
    (X : Scheme.{u}) (a : X ⟶ Spec (.of k₁)) (b : X ⟶ Spec (.of k₂))
    [LocallyOfFiniteType a] [LocallyOfFiniteType b] [IsReduced X] [ConnectedSpace X] :
    letI : Algebra k₁ Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k₁)).inv ≫ a.appTop).hom.toAlgebra
    letI : Algebra k₂ Γ(X, ⊤) := ((Scheme.ΓSpecIso (.of k₂)).inv ≫ b.appTop).hom.toAlgebra
    (integralClosure k₁ Γ(X, ⊤)).toSubring = (integralClosure k₂ Γ(X, ⊤)).toSubring
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.31, Tag 04MJ](https://stacks.math.columbia.edu/tag/04MJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
