---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.hasChowSchemeCover_of_isSeparated_isFiniteType
statement: formalized
proof: formalized
---

# 69.18 A weak version of Chow's lemma

Section 69.18 of the Stacks Project, [Tag 089I](https://stacks.math.columbia.edu/tag/089I). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 089J, a lemma

[Tag 089J](https://stacks.math.columbia.edu/tag/089J) in the Stacks Project.

**`AlgebraicGeometry.Space.hasChowSchemeCover_of_isSeparated_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/Induction.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/Induction.lean#L288).

> **Chow's lemma for algebraic spaces, [Stacks, Tag 089J].**
>
> Let `A` be a ring whose spectrum lies in the chosen big fppf site, and let `X` be an algebraic
> space over `Spec A` whose structure morphism is separated and of finite type. Then there is an
> object `X'` of the site — a scheme over `Spec A` — and a proper surjective morphism from the
> presheaf it represents to `X`, such that the structure morphism of `X'` to `Spec A` is
> H-quasi-projective.
>
> The morphism `f` quantified over is the structure morphism of `X` and nothing else: its target
> is the presheaf represented by the base, which is terminal by
> `AlgebraicGeometry.Space.isTerminal_yoneda_obj_base`.
>
> The proof is Stacks 089J's. An affine surjective étale chart exists by Stacks 03H6; a separated
> algebraic space over an affine base is reasonable by Stacks 03JX, so the fibre degrees of that
> chart are bounded, by the degree stratification of Stacks 07S8; and
> `AlgebraicGeometry.Space.hasChowSchemeCover_of_chart_fibre_le` performs the induction on that
> bound.

```lean
theorem hasChowSchemeCover_of_isSeparated_isFiniteType
    (B : BigFppfSite.{u}) (A : CommRingCat.{u}) (hA : B.Contains (Spec A))
    (X : (BigFppfOver B (Spec A) hA)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B (Spec A) hA X)
    (f : X ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hA))))
    (hsep : IsSeparated B (Spec A) hA f) (hft : IsFiniteType B (Spec A) hA f) :
    HasChowSchemeCover B (Spec A) hA X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.18, Tag 089I](https://stacks.math.columbia.edu/tag/089I)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
