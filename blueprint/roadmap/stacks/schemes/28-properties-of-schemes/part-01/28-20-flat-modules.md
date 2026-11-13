---
declaration: section
origin: cited
lean: AlgebraicGeometry.isFlat_tilde_iff_flat
statement: formalized
proof: formalized
---

# 28.20 Flat modules

Section 28.20 of the Stacks Project, [Tag 05NZ](https://stacks.math.columbia.edu/tag/05NZ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05P0, a lemma

[Tag 05P0](https://stacks.math.columbia.edu/tag/05P0) in the Stacks Project.

**`AlgebraicGeometry.isFlat_tilde_iff_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeFlat.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Modules/TildeFlat.lean#L99). References: EGA III (1.4.15.5), “case A = B, φ = id”; EGA IV (2.1.2), “A = B, φ = id”.

> **Stacks Project, Tag 05P0.** The sheaf associated to a module on an affine
> scheme is flat if and only if the module is flat.

```lean
theorem isFlat_tilde_iff_flat {R : CommRingCat.{u}} (M : ModuleCat.{u} R) :
    AlgebraicGeometry.SheafOfModules.IsFlat (tilde M) ↔ Module.Flat R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.20, Tag 05NZ](https://stacks.math.columbia.edu/tag/05NZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
