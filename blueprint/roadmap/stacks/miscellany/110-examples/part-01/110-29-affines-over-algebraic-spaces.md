---
declaration: section
origin: cited
lean: Stacks.Examples.exists_finiteType_affine_not_immersion_into_affineSpace
statement: formalized
proof: formalized
---

# 110.29 Affines over algebraic spaces

Section 110.29 of the Stacks Project, [Tag 088V](https://stacks.math.columbia.edu/tag/088V). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 088W, a lemma

[Tag 088W](https://stacks.math.columbia.edu/tag/088W) in the Stacks Project.

**`Stacks.Examples.exists_finiteType_affine_not_immersion_into_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/AffineOverSpaceNoImmersion.lean, line 743](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/AffineOverSpaceNoImmersion.lean#L743). The attribute's comment: “the counterexample”.

> **Stacks 088W.**  There is a finite-type morphism `Y ⟶ X` of algebraic spaces with `Y`
> an affine scheme and `X` quasi-separated which admits no immersion of `Y`, over `X`, into
> relative affine `n`-space over `X` for any `n`.
>
> Take for `X` the quotient `𝔸¹_k/R` of Stacks 02Z1 over a field in which two is invertible,
> for `Y` its chart `𝔸¹_k`, and for the morphism the chart itself: it is étale, hence locally
> of finite type, and quasi-compact because its source is quasi-compact and `X` is
> quasi-separated — that is
> `AffineOverAlgebraicSpace.isFiniteType_quotientSpaceMap`.  The nonexistence of an immersion
> is `AffineOverAlgebraicSpace.not_isImmersion_affineSpaceOver_quotientSpaceMap`.
>
> Algebraicity and quasi-separatedness of the target come from Stacks 02Z1 in the form in
> which the relation of this example is an affine morphism, so Stacks 0265 applies to it with
> no effective-descent input:
> `AlgebraicGeometry.AffineLineInvolution.isAlgebraicSpace_involutionQuotient_of_isAffineHom`
> rests on the relation being affine, which is Mathlib's `IsAffineHom` instance for a morphism
> between affine schemes, and the descent that Stacks 0265 then consumes is effective descent at
> the affine monomorphisms locally of finite type, proved outright in
> `StacksFrontier/AlgebraicGeometry/Descent/AffineHomCoveringSieveDescent.lean`.

```lean
theorem exists_finiteType_affine_not_immersion_into_affineSpace
    (k : Type u) [Field k] (hchar : (2 : k) ≠ 0)
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of k)))
    (hZ : B.Contains (⊤_ Scheme.{u}))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    ∃ (Y : BigFppfOver B (Spec (.of k)) hS)
      (X : (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u)
      (f : yoneda.obj Y ⟶ X),
      IsAffine ((BigFppfOver.toScheme B (Spec (.of k)) hS).obj Y) ∧
      IsAlgebraicSpace B (Spec (.of k)) hS (yoneda.obj Y) ∧
      IsAlgebraicSpace B (Spec (.of k)) hS X ∧
      Space.IsFiniteType B (Spec (.of k)) hS f ∧
      Space.IsAbsolutelyQuasiSeparated B (Spec (.of k)) hS hZ X ∧
      ∀ (n : ℕ) (j : yoneda.obj Y ⟶ Space.affineSpaceOver B (Spec (.of k)) hS X n),
        j ≫ prod.fst = f → ¬ Space.IsImmersion B (Spec (.of k)) hS j
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.29, Tag 088V](https://stacks.math.columbia.edu/tag/088V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
