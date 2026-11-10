---
declaration: section
origin: cited
lean: Stacks.Sites.ExtensionByZero.stalkExtensionByZeroIso, Stacks.Sites.ExtensionByZero.OfEssentiallySmall.stalkExtensionByZeroIso
statement: formalized
proof: formalized
---

# 18.38 Localization and points

Section 18.38 of the Stacks Project, [Tag 070Z](https://stacks.math.columbia.edu/tag/070Z). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0710, a lemma

[Tag 0710](https://stacks.math.columbia.edu/tag/0710) in the Stacks Project.

**`Stacks.Sites.ExtensionByZero.stalkExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Gate18/StalkOfExtensionByZero.lean, line 611](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Gate18/StalkOfExtensionByZero.lean#L611).

> The stalk of extension by zero from `C/U` is the direct sum of the stalks
> at the points of `C/U` above the given point.

```lean
noncomputable def stalkExtensionByZeroIso
    (X : RingedSite.{u, u, u}) (p : GrothendieckTopology.Point.{u, u, u} X.J)
    (U : X.C) (G : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
    [HasWeakSheafify X.J AddCommGrpCat.{u}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{u}] :
    (p.presheafFiber.obj (((SheafOfModules.pullback.{u}
      (F := Over.forget U)
        (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))).obj G).val.presheaf)) ≅
      ∐ fun x : p.fiber.obj U => (p.over x).presheafFiber.obj G.val.presheaf
```

**`Stacks.Sites.ExtensionByZero.OfEssentiallySmall.stalkExtensionByZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Gate18/StalkOfExtensionByZeroEssentiallySmall.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Gate18/StalkOfExtensionByZeroEssentiallySmall.lean#L602).

> The stalk of extension by zero from `C/U` is the direct sum of the stalks
> at the points of `C/U` above the given point, for a ringed site whose objects may live in a
> universe above its morphisms, structure rings and module sections.

```lean
noncomputable def stalkExtensionByZeroIso
    (X : RingedSite.{c, u, u}) [EssentiallySmall.{u} X.C]
    (p : GrothendieckTopology.Point.{u, u, c} X.J)
    (U : X.C) (G : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
    [HasWeakSheafify X.J AddCommGrpCat.{u}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{u}] :
    (p.presheafFiber.obj (((SheafOfModules.pullback.{u}
      (F := Over.forget U) (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))).obj
        G).val.presheaf)) ≅
      ∐ fun x : p.fiber.obj U => (p.over x).presheafFiber.obj G.val.presheaf
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.38, Tag 070Z](https://stacks.math.columbia.edu/tag/070Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
