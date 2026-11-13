---
declaration: section
origin: cited
lean: DifferentialGradedModule.cone, DifferentialGradedModule.exists_mappingConeMap_of_homotopic_square
statement: formalized
proof: formalized
---

# 22.6 Cones

Section 22.6 of the Stacks Project, [Tag 09K9](https://stacks.math.columbia.edu/tag/09K9). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09KA, a definition

[Tag 09KA](https://stacks.math.columbia.edu/tag/09KA) in the Stacks Project.

**`DifferentialGradedModule.cone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Cone.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Cone.lean#L218).

> The mapping cone, with its direct-sum coordinates and canonical maps.

```lean
noncomputable def cone (f : K ⟶ L) : Cone f
```

## Tag 09KD, a lemma

[Tag 09KD](https://stacks.math.columbia.edu/tag/09KD) in the Stacks Project.

**`DifferentialGradedModule.exists_mappingConeMap_of_homotopic_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeFunctorial.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeFunctorial.lean#L48).

> A square of homomorphisms of differential graded modules commuting up to homotopy extends to
> their mapping cones. The inclusion square and the shifted-projection square commute already
> before passing to homotopy classes.

```lean
theorem exists_mappingConeMap_of_homotopic_square
    (f₁ : K₁ ⟶ L₁) (f₂ : K₂ ⟶ L₂)
    (a : K₁ ⟶ K₂) (b : L₁ ⟶ L₂)
    (h : Homotopic (f₁ ≫ b) (a ≫ f₂)) :
    ∃ c : coneModule f₁ ⟶ coneModule f₂,
      coneInclusion f₁ ≫ c = b ≫ coneInclusion f₂ ∧
      c ≫ coneProjection f₂ = coneProjection f₁ ≫ shiftMap a 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.6, Tag 09K9](https://stacks.math.columbia.edu/tag/09K9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
