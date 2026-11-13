---
declaration: section
origin: cited
lean: AlgebraicGeometry.tilde_isFiniteType_iff, AlgebraicGeometry.tilde_isFinitePresentation_iff
statement: formalized
proof: formalized
---

# 28.17 Characterizing modules of finite type and finite presentation

Section 28.17 of the Stacks Project, [Tag 01PA](https://stacks.math.columbia.edu/tag/01PA). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01PB, a lemma

[Tag 01PB](https://stacks.math.columbia.edu/tag/01PB) in the Stacks Project.

**`AlgebraicGeometry.tilde_isFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeFiniteness.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Modules/TildeFiniteness.lean#L142). References: EGA II (1.4.5), “affine base, B = O\_Y”.

> An associated sheaf on `Spec R` is of finite type precisely when its module of global
> sections is finite over `R`.

```lean
theorem tilde_isFiniteType_iff {R : CommRingCat.{u}} (M : ModuleCat.{u} R) :
    (tilde M).IsFiniteType ↔ Module.Finite R M
```

## Tag 01PC, a lemma

[Tag 01PC](https://stacks.math.columbia.edu/tag/01PC) in the Stacks Project.

**`AlgebraicGeometry.tilde_isFinitePresentation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeFiniteness.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Modules/TildeFiniteness.lean#L200).

> The quasi-coherent sheaf on `Spec R` associated to an `R`-module `M` is of finite
> presentation if and only if `M` is a finitely presented module.

```lean
theorem tilde_isFinitePresentation_iff {R : CommRingCat.{u}} (M : ModuleCat.{u} R) :
    (tilde M).IsFinitePresentation ↔ Module.FinitePresentation R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.17, Tag 01PA](https://stacks.math.columbia.edu/tag/01PA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
