---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.smallEtaleBaseChange, Stacks.EtaleCohomology.smallEtaleBaseChangeObjIso_hom_fst
statement: formalized
proof: formalized
---

# 59.34 Functoriality of small étale topos

Section 59.34 of the Stacks Project, [Tag 04I0](https://stacks.math.columbia.edu/tag/04I0). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04I1, an equation

[Tag 04I1](https://stacks.math.columbia.edu/tag/04I1) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtaleBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/InverseImage.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/InverseImage.lean#L63).

> Base change along `f : X ⟶ Y`, as a functor from the small étale site of `Y` to that of
> `X`: an étale scheme `W` over `Y` is sent to the fibre product `W ×_Y X`, which is étale over
> `X` because étale morphisms are stable under base change. This is the functor
> `u : Y_étale → X_étale, V/Y ↦ X ×_Y V/X` of Tag 04I1, with the fibre product written in the
> other order (see `smallEtaleBaseChangeObjIso`).

```lean
public def smallEtaleBaseChange {X Y : Scheme.{u}} (f : X ⟶ Y) : Y.Etale ⥤ X.Etale
```

**`Stacks.EtaleCohomology.smallEtaleBaseChangeObjIso_hom_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/InverseImage.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GlobalSectionsClosed/InverseImage.lean#L82). The attribute's comment: “object formula”.

> The object formula `V/Y ↦ X ×_Y V/X` for the base-change functor `u : Y_étale → X_étale`:
> under `smallEtaleBaseChangeObjIso`, the structure morphism of the base change of `V` to `X` is
> the first projection `X ×_Y V ⟶ X`.

```lean
public theorem smallEtaleBaseChangeObjIso_hom_fst {X Y : Scheme.{u}} (f : X ⟶ Y) (V : Y.Etale) :
    (smallEtaleBaseChangeObjIso f V).hom ≫ pullback.fst f V.hom =
      ((smallEtaleBaseChange f).obj V).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.34, Tag 04I0](https://stacks.math.columbia.edu/tag/04I0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
