---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_comp_fromSpecResidueField_eq, AlgebraicGeometry.exists_factorization_through_residueFields
statement: formalized
proof: formalized
---

# 29.59 Miscellany

Section 29.59 of the Stacks Project, [Tag 0H1L](https://stacks.math.columbia.edu/tag/0H1L). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H1M, a lemma

[Tag 0H1M](https://stacks.math.columbia.edu/tag/0H1M) in the Stacks Project.

**`AlgebraicGeometry.exists_comp_fromSpecResidueField_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Misc/PointFactorization.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Misc/PointFactorization.lean#L43).

> **Stacks Project, Tag 0H1M.** A morphism from a reduced scheme whose image is contained in a
> single point factors through the spectrum of the residue field of that point.

```lean
lemma exists_comp_fromSpecResidueField_eq {X Y : Scheme.{u}} (f : Y ⟶ X) (x : X)
    [IsReduced Y] (hf : Set.range f.base ⊆ {x}) :
    ∃ g : Y ⟶ Spec (.of (X.residueField x)), g ≫ X.fromSpecResidueField x = f
```

## Tag 0H1N, a lemma

[Tag 0H1N](https://stacks.math.columbia.edu/tag/0H1N) in the Stacks Project.

**`AlgebraicGeometry.exists_factorization_through_residueFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Misc/ResidueFieldFactorization.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Misc/ResidueFieldFactorization.lean#L226).

> **Stacks Project, Tag 0H1N.** A morphism from a reduced scheme into a locally Noetherian
> scheme, whose image lies in a set having no nontrivial specializations among its points, factors
> through the coproduct of the corresponding residue-field points.

```lean
theorem exists_factorization_through_residueFields
    {X Y : Scheme.{u}} (f : Y ⟶ X) (E : Set X)
    [IsLocallyNoetherian X] [IsReduced Y]
    (hE : ∀ x x' : E, x.1 ⤳ x'.1 → x.1 = x'.1)
    (hf : ∀ y : Y, f y ∈ E) :
    ∃ g : Y ⟶ ∐ fun x : E ↦ Spec (.of (X.residueField x.1)),
      g ≫ Sigma.desc (fun x : E ↦ X.fromSpecResidueField x.1) = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.59, Tag 0H1L](https://stacks.math.columbia.edu/tag/0H1L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
