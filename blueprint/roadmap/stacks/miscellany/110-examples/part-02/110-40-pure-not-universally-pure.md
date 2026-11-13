---
declaration: section
origin: cited
lean: Stacks.Examples.exists_isPureRelative_not_isUniversallyPureRelative
statement: formalized
proof: formalized
---

# 110.40 Pure not universally pure

Section 110.40 of the Stacks Project, [Tag 05JJ](https://stacks.math.columbia.edu/tag/05JJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05JK, a lemma

[Tag 05JK](https://stacks.math.columbia.edu/tag/05JK) in the Stacks Project.

**`Stacks.Examples.exists_isPureRelative_not_isUniversallyPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/PureNotUniversallyPure.lean, line 828](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/PureNotUniversallyPure.lean#L828).

> There is a morphism of affine schemes of finite presentation and a module of finite
> presentation on its source which is pure relative to the base, but not universally pure relative
> to it.

```lean
theorem exists_isPureRelative_not_isUniversallyPureRelative :
    ∃ (X S : Scheme.{u}) (_ : IsAffine X) (_ : IsAffine S) (f : X ⟶ S)
      (hf : FinitePresentation f) (F : X.Modules)
      (hF : SheafOfModules.IsFinitePresentation.{u, u, u} F)
      (hFT : SheafOfModules.IsFiniteType.{u, u, u} F)
      (hQC : SheafOfModules.IsQuasicoherent.{u, u, u} F),
      letI : LocallyOfFinitePresentation f := hf.1
      letI : LocallyOfFiniteType f := inferInstance
      letI : QuasiCompact f := hf.2.1
      letI : SheafOfModules.IsFinitePresentation.{u, u, u} F := hF
      letI : SheafOfModules.IsFiniteType.{u, u, u} F := hFT
      letI : SheafOfModules.IsQuasicoherent.{u, u, u} F := hQC
      IsPureRelative f F ∧ ¬ IsUniversallyPureRelative f F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.40, Tag 05JJ](https://stacks.math.columbia.edu/tag/05JJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
