---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.IsLocallyProjective, AlgebraicGeometry.isLocallyProjective_iff_exists_affineOpen_cover, AlgebraicGeometry.isLocallyProjective_tilde_iff_projective, AlgebraicGeometry.pullback_isLocallyProjective
statement: formalized
proof: formalized
---

# 28.22 Locally projective modules

Section 28.22 of the Stacks Project, [Tag 05JN](https://stacks.math.columbia.edu/tag/05JN). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05JP, a definition

[Tag 05JP](https://stacks.math.columbia.edu/tag/05JP) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.IsLocallyProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocallyProjective.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/LocallyProjective.lean#L45).

> A sheaf of modules on a scheme is locally projective if its sections on every affine open
> are projective over the ring of functions on that open.

```lean
public abbrev IsLocallyProjective {X : Scheme.{u}}
    (M : SheafOfModules.{m} X.ringCatSheaf) : Prop
```

## Tag 05JQ, a lemma

[Tag 05JQ](https://stacks.math.columbia.edu/tag/05JQ) in the Stacks Project.

**`AlgebraicGeometry.isLocallyProjective_iff_exists_affineOpen_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/LocallyProjectiveCover.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/LocallyProjectiveCover.lean#L162). The attribute's comment: “affine open cover characterization”. References: SGA 3 VIB (11.9.1), “(i) <=> (ii)”.

> **Stacks Project, Tag 05JQ.** A quasi-coherent sheaf of modules is locally projective
> if and only if its sections are projective on every member of some affine open cover.

```lean
theorem isLocallyProjective_iff_exists_affineOpen_cover {X : Scheme.{u}} (M : X.Modules)
    [M.IsQuasicoherent] :
    Scheme.Modules.IsLocallyProjective M ↔
      ∃ (ι : Type u) (U : ι → X.Opens),
        IsOpenCover U ∧
          (∀ i, IsAffineOpen (U i)) ∧
          ∀ i, Module.Projective Γ(X, U i) Γ(M, U i)
```

**`AlgebraicGeometry.isLocallyProjective_tilde_iff_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/LocallyProjectiveCover.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/AmpleAndExtension/LocallyProjectiveCover.lean#L192). The attribute's comment: “affine specialization”. References: SGA 3 VIB (11.9.1), “affine case”.

> **Stacks Project, Tag 05JQ.** The sheaf associated to a module on an affine scheme is
> locally projective if and only if the original module is projective.

```lean
theorem isLocallyProjective_tilde_iff_projective (R : CommRingCat.{u})
    (M : ModuleCat.{u} R) :
    Scheme.Modules.IsLocallyProjective (tilde M) ↔ Module.Projective R M
```

## Tag 060M, a lemma

[Tag 060M](https://stacks.math.columbia.edu/tag/060M) in the Stacks Project.

**`AlgebraicGeometry.pullback_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/LocallyProjectivePullback.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/LocallyProjectivePullback.lean#L65).

> **Stacks Project, Tag 060M.** The pullback of a locally projective quasi-coherent module
> along a morphism of schemes is locally projective.

```lean
theorem pullback_isLocallyProjective {X Y : Scheme.{u}} (f : X ⟶ Y) (G : Y.Modules)
    [G.IsQuasicoherent] (hG : Scheme.Modules.IsLocallyProjective G) :
    Scheme.Modules.IsLocallyProjective ((Scheme.Modules.pullback f).obj G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.22, Tag 05JN](https://stacks.math.columbia.edu/tag/05JN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
