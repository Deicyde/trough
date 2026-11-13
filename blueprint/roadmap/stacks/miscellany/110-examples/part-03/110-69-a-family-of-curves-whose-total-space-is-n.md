---
declaration: section
origin: cited
lean: Stacks.Examples.CurveFamilyNotScheme.exists_curveFamily_total_not_scheme
statement: formalized
proof: formalized
---

# 110.69 A family of curves whose total space is not a scheme

Section 110.69 of the Stacks Project, [Tag 0D5D](https://stacks.math.columbia.edu/tag/0D5D). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D5E, a lemma

[Tag 0D5E](https://stacks.math.columbia.edu/tag/0D5E) in the Stacks Project.

**`Stacks.Examples.CurveFamilyNotScheme.exists_curveFamily_total_not_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/CurveFamilyNotScheme/Main.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Spaces/CurveFamilyNotScheme/Main.lean#L63). The attribute's comment: “with k = ℂ: a family of curves over A¹\_ℂ in the sense of Tag 0D4Z, Artin's contraction of the strict transform of the central fibre of the blown-up cubic surface, whose total space is not isomorphic to the algebraic space of any scheme”.

> **A family of curves whose total space is not a scheme** ([Stacks, Tag 0D5E]). There are a
> field `k` and a family of curves `F` (Stacks 0D4Z: a flat, proper morphism of finite
> presentation of relative dimension at most one, from an algebraic space over `Spec ℤ` to a
> scheme) in a big fppf site, whose base is the affine line `A¹_k = Spec k[t]` and whose total space
> is not isomorphic to the algebraic space of any scheme.
>
> The construction is that of Stacks, Section 0D5D, with `k = ℂ`: `Y ⊆ ℙ²_{k[t]}` is the cubic
> surface `T₀ ^ 3 + T₁ ^ 3 + T₂ ^ 3 - t T₀ T₁ T₂ = 0`, `y` a point of the central fibre `Y₀` with
> property (2), `Z` the blowup of `Y` at `y` and `C ⊆ Z` the strict transform of `Y₀`; the total
> space of `F` is Artin's contraction of `C` (Stacks 0GIB), read over `Spec ℤ`.

```lean
theorem exists_curveFamily_total_not_scheme :
    ∃ (k : Type) (_ : Field k) (B : BigFppfSite.{0}) (hZ : B.Contains integerBase)
      (F : AlgebraicGeometry.CurveFamily B hZ),
      Nonempty (F.base.left.obj ≅ Spec (CommRingCat.of (Polynomial k))) ∧
        ¬ ∃ V : BigFppfOver B integerBase hZ, Nonempty (F.total ≅ schemeSpace V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.69, Tag 0D5D](https://stacks.math.columbia.edu/tag/0D5D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
