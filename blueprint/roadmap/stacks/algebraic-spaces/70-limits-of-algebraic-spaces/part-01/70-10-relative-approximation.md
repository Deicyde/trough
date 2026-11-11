---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.hasRelativeApproximation_of_isQuasiCompactSpace, AlgebraicGeometry.Space.exists_isLimit_finitePresentation
statement: formalized
proof: formalized
---

# 70.10 Relative approximation

Section 70.10 of the Stacks Project, [Tag 09NR](https://stacks.math.columbia.edu/tag/09NR). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GS3, a lemma

[Tag 0GS3](https://stacks.math.columbia.edu/tag/0GS3) in the Stacks Project.

**`AlgebraicGeometry.Space.hasRelativeApproximation_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationApproximation.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationApproximation.lean#L52).

> **Relative approximation over `Spec ℤ`, on any big fppf site.** A morphism `f : X ⟶ Y` of
> quasi-compact quasi-separated algebraic spaces over `Spec ℤ` is the limit of a directed inverse
> system of morphisms of quasi-separated algebraic spaces of finite type over `Spec ℤ` with affine
> transition morphisms. It is built on an enlargement of the site on which `X` and `Y` have small
> atlases, and descended.

```lean
theorem hasRelativeApproximation_of_isQuasiCompactSpace (B : BigFppfSite.{u})
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : (BigFppfOver B (⊤_ Scheme.{u}) hZ)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (hX : IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ X)
    (hY : IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ Y)
    (hXqc : IsQuasiCompactSpace B (⊤_ Scheme.{u}) hZ X)
    (hYqc : IsQuasiCompactSpace B (⊤_ Scheme.{u}) hZ Y)
    (hXqs : IsAbsolutelyQuasiSeparated B (⊤_ Scheme.{u}) hZ hZ X)
    (hYqs : IsAbsolutelyQuasiSeparated B (⊤_ Scheme.{u}) hZ hZ Y) :
    HasRelativeApproximation B hZ f
```

## Tag 09NS, a lemma

[Tag 09NS](https://stacks.math.columbia.edu/tag/09NS) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isLimit_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationApproximation.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/FinitePresentationApproximation.lean#L93).

> **Stacks 09NS.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S`, with `X`
> quasi-compact and quasi-separated and `Y` quasi-separated. Then `X` is the limit of a directed
> inverse system of algebraic spaces `Xᵢ` of finite presentation over `Y`, with affine transition
> morphisms over `Y`: an inverse system `D` of algebraic spaces over `S` with morphisms
> `tᵢ : Xᵢ ⟶ Y` of finite presentation compatible with the affine transition morphisms, and a
> limit cone `X ⟶ Xᵢ` over `Y`.

```lean
theorem exists_isLimit_finitePresentation (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hXqc : IsQuasiCompactSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y) :
    ∃ (I : Type (u + 1)) (_ : Preorder I) (_ : Nonempty I) (_ : IsDirectedOrder I)
      (D : Iᵒᵖ ⥤ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
      (t : D ⟶ (Functor.const Iᵒᵖ).obj Y) (p : (Functor.const Iᵒᵖ).obj X ⟶ D)
      (_ : IsLimit (Cone.mk X p)),
      (p ≫ t = (Functor.const Iᵒᵖ).map f) ∧
        (∀ i, IsAlgebraicSpace B S hS (D.obj i)) ∧
        (∀ i, IsFinitePresentation B S hS (t.app i)) ∧
        (∀ {i j : Iᵒᵖ} (g : i ⟶ j), IsAffineHom B S hS (D.map g))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.10, Tag 09NR](https://stacks.math.columbia.edu/tag/09NR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
