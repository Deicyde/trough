---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.exists_admissibleBlowup_flat_finitePresentation_closedSubstack
statement: formalized
proof: formalized
---

# 106.9 Blowing up and flatness

Section 106.9 of the Stacks Project, [Tag 0CQ3](https://stacks.math.columbia.edu/tag/0CQ3). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CQ4, a lemma

[Tag 0CQ4](https://stacks.math.columbia.edu/tag/0CQ4) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_admissibleBlowup_flat_finitePresentation_closedSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatteningByBlowupStack.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatteningByBlowupStack.lean#L42).

> **Flattening by blowing up.** Let `f : 𝒳 ⟶ Y` be a 1-morphism from an algebraic stack to an
> algebraic space and `V ⊆ Y` an open subspace, with (1) `Y` quasi-compact and quasi-separated, (2)
> `f` of finite type and quasi-separated, (3) `V` quasi-compact and (4) `𝒳_V ⟶ V` flat and locally
> of finite presentation. Then there are a `V`-admissible blowup `b : Y' ⟶ Y` and a closed substack
> `𝒳' ⊆ 𝒳_{Y'}` containing every object of `𝒳_{Y'}` over `b⁻¹V` (so `𝒳'_V = 𝒳_V`, `b` being an
> isomorphism over `V`) such that `𝒳' ⟶ Y'` is flat and of finite presentation.

```lean
theorem exists_admissibleBlowup_flat_finitePresentation_closedSubstack
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hY : IsAlgebraicSpace B S hS Y)
    (hYqc : Space.IsQuasiCompactSpace B S hS Y)
    (hYqs : Space.IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    {𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS Y hY)
    (hft : IsFiniteType B S hS f) (hqs : IsQuasiSeparated B S hS f)
    (V : Subfunctor Y) (hV : Space.IsOpenSubspace B S hS V)
    (hVqc : Space.IsQuasiCompactSpace B S hS V.toFunctor)
    (hflat : IsFlat B S hS
      (twoFibreProductSquare B S hS (algebraicSpaceStackMap.{u, w} B S hS hV.1 hY V.ι) f).fst)
    (hlfp : IsLocallyOfFinitePresentation B S hS
      (twoFibreProductSquare B S hS (algebraicSpaceStackMap.{u, w} B S hS hV.1 hY V.ι) f).fst) :
    ∃ (Y' : AlgebraicSpaces B S hS) (b : Y' ⟶ ⟨Y, hY⟩),
      Space.IsAdmissibleBlowup B S hS ⟨V, hV⟩ b ∧
        ∃ P : ObjectProperty (twoFibreProductSquare B S hS
            (algebraicSpaceStackMap.{u, w} B S hS Y'.2 hY b.hom) f).pt.val.val.obj,
          IsClosedSubstack _ P ∧
          (∀ x, ((twoFibreProductSquare B S hS
              (algebraicSpaceStackMap.{u, w} B S hS Y'.2 hY b.hom) f).fst.hom.hom.obj
                x).fiber.as ∈ (V.preimage b.hom).obj (Opposite.op ((twoFibreProductSquare B S hS
                  (algebraicSpaceStackMap.{u, w} B S hS Y'.2 hY b.hom) f).fst.hom.hom.obj
                    x).base) →
            P x) ∧
          ∀ hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased _ P),
            IsFlat B S hS (fullSubcategoryInclusion _ P hP ≫ (twoFibreProductSquare B S hS
              (algebraicSpaceStackMap.{u, w} B S hS Y'.2 hY b.hom) f).fst) ∧
            IsFinitePresentation B S hS (fullSubcategoryInclusion _ P hP ≫
              (twoFibreProductSquare B S hS
                (algebraicSpaceStackMap.{u, w} B S hS Y'.2 hY b.hom) f).fst)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.9, Tag 0CQ3](https://stacks.math.columbia.edu/tag/0CQ3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
