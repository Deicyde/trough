---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isFiniteType_classifyingStack_of_smoothSchemeCovering
statement: formalized
proof: formalized
---

# 110.53 Stack with quasi-compact flat covering which is not algebraic

Section 110.53 of the Stacks Project, [Tag 04AG](https://stacks.math.columbia.edu/tag/04AG). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04AH, a lemma

[Tag 04AH](https://stacks.math.columbia.edu/tag/04AH) in the Stacks Project.

**`AlgebraicGeometry.Stack.isFiniteType_classifyingStack_of_smoothSchemeCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/ClassifyingStackFiniteType.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/ClassifyingStackFiniteType.lean#L69).

> **Stacks 04AH.** Let `k` be a field and let `G` be an affine group scheme over `k`. If the
> classifying stack `[Spec(k)/G]` has a smooth surjective covering by a scheme, then `G` is of
> finite type over `k`.
>
> The covering hypothesis is the third clause of Stacks 026O for the classifying stack. By
> Stacks 04WZ the classifying stack is then algebraic, and by the half of Stacks 06PL going from
> algebraicity to flatness and local finite presentation, the group is locally of finite
> presentation over `k`.

```lean
theorem isFiniteType_classifyingStack_of_smoothSchemeCovering
    (G : Space.GroupAlgebraicSpace C (Spec (.of k)) hk
      (Space.terminalSpace C (Spec (.of k)) hk).obj
      (Space.terminalSpace C (Spec (.of k)) hk).property)
    (hAffine : Space.IsAffineHom C (Spec (.of k)) hk G.obj.X.hom)
    (hcov :
      ∃ (U : BigFppfOver C (Spec (.of k)) hk)
        (f : (schemeFibredCategory C (Spec (.of k)) hk U).val ⥤ᵇ
          (classifyingStack C hk G).val),
        IsRepresentableByAlgebraicSpaces C (Spec (.of k)) hk f ∧
          ∀ (V : BigFppfOver C (Spec (.of k)) hk)
            (y : BigFppfOver C V.left.1 V.left.2 ⥤ (classifyingStack C hk G).val.obj)
            (_hy : y ⋙ (classifyingStack C hk G).val.p = Over.map V.hom)
            (F : (BigFppfOver C V.left.1 V.left.2)ᵒᵖ ⥤ Type u)
            (hF : IsAlgebraicSpace C V.left.1 V.left.2 F),
            Nonempty (StacksRepresentableCFG.EquivalenceOver
              (TwoFibreProductOver.fst (Over.map V.hom)
                (schemeFibredCategory C (Spec (.of k)) hk U).val.p
                (classifyingStack C hk G).val.p y f.toFunctor)
              (presheafOfCategories (F ⋙ typeToCat)).p) →
              (let g := (algebraicSpaceMap C (Spec (.of k)) hk V
                ((spacesOverSmallerBaseFunctor C V.left.1 (Spec (.of k)) V.left.2 hk
                  V.hom).obj ⟨F, hF⟩)).hom
               Space.IsSurjective C (Spec (.of k)) hk g ∧
                 Space.IsSmooth C (Spec (.of k)) hk g)) :
    Space.IsFiniteType C (Spec (.of k)) hk G.obj.X.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.53, Tag 04AG](https://stacks.math.columbia.edu/tag/04AG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
