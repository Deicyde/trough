---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_affine_open_etale_affineSpace
statement: formalized
proof: formalized
---

# 41.13 Étale and smooth morphisms

Section 41.13 of the Stacks Project, [Tag 039P](https://stacks.math.columbia.edu/tag/039P). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 039Q, a theorem

[Tag 039Q](https://stacks.math.columbia.edu/tag/039Q) in the Stacks Project.

**`AlgebraicGeometry.exists_affine_open_etale_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/EtaleAffineSpace.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/EtaleAffineSpace.lean#L100). The attribute's comment: “smooth at a point is étale-locally an affine space”. References: EGA IV (17.11.4), “smooth ⇒ étale/A^d”.

> A morphism of schemes which is smooth at a point is, over any affine open neighbourhood `V`
> of the image of that point, étale-locally an affine space over `V`: there is an affine open
> neighbourhood `U` of the point mapping into `V` and an étale morphism from `U` to an affine
> space over `V` commuting with the morphism.

```lean
theorem exists_affine_open_etale_affineSpace {X Y : Scheme.{u}} (f : X ⟶ Y) (x : X)
    (V : Y.Opens) (hV : IsAffineOpen V) (hxV : x ∈ f ⁻¹ᵁ V)
    (hf : InfinitesimalLifting.SmoothAt f x) :
    ∃ (d : ℕ) (U : X.Opens) (_ : IsAffineOpen U) (_ : x ∈ U) (hUV : U ≤ f ⁻¹ᵁ V)
      (π : U.toScheme ⟶ AffineSpace (ULift.{u} (Fin d)) V.toScheme),
      Etale π ∧
        π ≫ (AffineSpace (ULift.{u} (Fin d)) V.toScheme ↘ V.toScheme) =
          f.resLE V U hUV
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.13, Tag 039P](https://stacks.math.columbia.edu/tag/039P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
