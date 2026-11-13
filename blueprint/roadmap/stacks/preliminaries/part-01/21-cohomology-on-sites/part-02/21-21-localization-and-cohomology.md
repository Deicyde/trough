---
declaration: section
origin: cited
lean: Stacks.Cohomology.Localization.derivedOverPushforwardBaseChangeIso, Stacks.Cohomology.Localization.derivedModulesPushforwardBaseChangeIso
statement: formalized
proof: formalized
---

# 21.21 Localization and cohomology

Section 21.21 of the Stacks Project, [Tag 0EYZ](https://stacks.math.columbia.edu/tag/0EYZ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EZ0, a lemma

[Tag 0EZ0](https://stacks.math.columbia.edu/tag/0EZ0) in the Stacks Project.

**`Stacks.Cohomology.Localization.derivedOverPushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/AbelianSheavesOnALocalizedSite.lean, line 682](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/AbelianSheavesOnALocalizedSite.lean#L682).

> **Stacks 0EZ0.** For a Cartesian square
> ```
>   X' --a--> X
>   |b         |c
>   Y' --d--> Y
> ```
> in a site, inverse image along `d` after derived direct image along `c` is naturally isomorphic
> to derived direct image along `b` after inverse image along `a`.
>
> All four derived functors are arbitrary choices with their canonical transformations from the
> corresponding functors on homotopy categories.

```lean
noncomputable def derivedOverPushforwardBaseChangeIso
    (J : GrothendieckTopology C) {X' X Y' Y : C}
    (a : X' ⟶ X) (b : X' ⟶ Y') (c : X ⟶ Y) (d : Y' ⟶ Y)
    (h : IsPullback a b c d)
    [∀ U : C, HasSheafify (J.over U) Ab.{max u v}]
    [HasDerivedCategory.{wX} (AbelianSheaves J X)]
    [HasDerivedCategory.{wY} (AbelianSheaves J Y)]
    [HasDerivedCategory.{wU} (AbelianSheaves J X')]
    [HasDerivedCategory.{wV'} (AbelianSheaves J Y')]
    (Rc : DerivedCategory (AbelianSheaves J X) ⥤
      DerivedCategory (AbelianSheaves J Y))
    (Rb : DerivedCategory (AbelianSheaves J X') ⥤
      DerivedCategory (AbelianSheaves J Y'))
    (Ra : DerivedCategory (AbelianSheaves J X) ⥤
      DerivedCategory (AbelianSheaves J X'))
    (Rd : DerivedCategory (AbelianSheaves J Y) ⥤
      DerivedCategory (AbelianSheaves J Y'))
    (αc : homotopyToDerived (overPushforward J c) ⟶ DerivedCategory.Qh ⋙ Rc)
    (αb : homotopyToDerived (overPushforward J b) ⟶ DerivedCategory.Qh ⋙ Rb)
    (αa : homotopyToDerived (overPullback J a) ⟶ DerivedCategory.Qh ⋙ Ra)
    (αd : homotopyToDerived (overPullback J d) ⟶ DerivedCategory.Qh ⋙ Rd)
    [Rc.IsRightDerivedFunctor αc
      (HomotopyCategory.quasiIso (AbelianSheaves J X) (ComplexShape.up ℤ))]
    [Rb.IsRightDerivedFunctor αb
      (HomotopyCategory.quasiIso (AbelianSheaves J X') (ComplexShape.up ℤ))]
    [Ra.IsRightDerivedFunctor αa
      (HomotopyCategory.quasiIso (AbelianSheaves J X) (ComplexShape.up ℤ))]
    [Rd.IsRightDerivedFunctor αd
      (HomotopyCategory.quasiIso (AbelianSheaves J Y) (ComplexShape.up ℤ))] :
    Rc ⋙ Rd ≅ Ra ⋙ Rb
```

## Tag 0FN5, a lemma

[Tag 0FN5](https://stacks.math.columbia.edu/tag/0FN5) in the Stacks Project.

**`Stacks.Cohomology.Localization.derivedModulesPushforwardBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedBaseChangeOfModules.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/Localization/DerivedBaseChangeOfModules.lean#L127).

> **Stacks 0FN5.** For a cartesian square
> ```
>   X' --a--> X
>   |b        |c
>   V         V
>   Y' --d--> Y
> ```
> of a ringed site `(C, O)`, the inverse image of sheaves of modules along the relocalization at `d`
> after the derived direct image along the relocalization at `c` is naturally isomorphic to the
> derived direct image along the relocalization at `b` after the inverse image along the
> relocalization at `a`.
>
> All four derived functors are arbitrary choices with their canonical transformations from the
> corresponding functors on homotopy categories.

```lean
def derivedModulesPushforwardBaseChangeIso
    (a : X' ⟶ X) (b : X' ⟶ Y') (c : X ⟶ Y) (d : Y' ⟶ Y) (hsq : IsPullback a b c d)
    [HasDerivedCategory.{wX} (_root_.SheafOfModules.{u} (O.over X))]
    [HasDerivedCategory.{wY} (_root_.SheafOfModules.{u} (O.over Y))]
    [HasDerivedCategory.{wU} (_root_.SheafOfModules.{u} (O.over X'))]
    [HasDerivedCategory.{wV} (_root_.SheafOfModules.{u} (O.over Y'))]
    (Rc : DerivedCategory (_root_.SheafOfModules.{u} (O.over X)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (O.over Y)))
    (Rb : DerivedCategory (_root_.SheafOfModules.{u} (O.over X')) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (O.over Y')))
    (Ra : DerivedCategory (_root_.SheafOfModules.{u} (O.over X)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (O.over X')))
    (Rd : DerivedCategory (_root_.SheafOfModules.{u} (O.over Y)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (O.over Y')))
    (αc : homotopyToDerived (Stacks.SheafOfModules.Relocalization.pushforward J O c) ⟶
      DerivedCategory.Qh ⋙ Rc)
    (αb : homotopyToDerived (Stacks.SheafOfModules.Relocalization.pushforward J O b) ⟶
      DerivedCategory.Qh ⋙ Rb)
    (αa : homotopyToDerived (_root_.SheafOfModules.overMap.{u} O a) ⟶ DerivedCategory.Qh ⋙ Ra)
    (αd : homotopyToDerived (_root_.SheafOfModules.overMap.{u} O d) ⟶ DerivedCategory.Qh ⋙ Rd)
    [Rc.IsRightDerivedFunctor αc
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (O.over X)) (ComplexShape.up ℤ))]
    [Rb.IsRightDerivedFunctor αb
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (O.over X')) (ComplexShape.up ℤ))]
    [Ra.IsRightDerivedFunctor αa
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (O.over X)) (ComplexShape.up ℤ))]
    [Rd.IsRightDerivedFunctor αd
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (O.over Y)) (ComplexShape.up ℤ))] :
    Rc ⋙ Rd ≅ Ra ⋙ Rb
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.21, Tag 0EYZ](https://stacks.math.columbia.edu/tag/0EYZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
