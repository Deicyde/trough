---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.presheavesOfModules, AlgebraicGeometry.Stack.IsModule, AlgebraicGeometry.Stack.modules, AlgebraicGeometry.Stack.moduleFunctoriality, AlgebraicGeometry.Stack.modulePullback, AlgebraicGeometry.Stack.moduleSheafAdjunction, AlgebraicGeometry.Stack.moduleSheafFunctoriality
statement: formalized
proof: formalized
---

# 96.7 Sheaves of modules

Section 96.7 of the Stacks Project, [Tag 06WA](https://stacks.math.columbia.edu/tag/06WA). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06WB, a definition

[Tag 06WB](https://stacks.math.columbia.edu/tag/06WB) in the Stacks Project.

**`AlgebraicGeometry.Stack.presheavesOfModules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Modules.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Modules.lean#L99). The attribute's comment: “part (1), the category of presheaves of modules”.

> **Stacks 06WB, part (1).** A presheaf of modules on a category fibred in groupoids `𝒳` over
> the schemes over `S` is a presheaf of `𝒪_𝒳`-modules, and `PMod(𝒪_𝒳)` is the category they form,
> with morphisms the morphisms of presheaves of modules.

```lean
abbrev presheavesOfModules
```

**`AlgebraicGeometry.Stack.IsModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Modules.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Modules.lean#L105). The attribute's comment: “part (2), the fppf sheaf condition”.

> **Stacks 06WB, part (2).** A presheaf of `𝒪_𝒳`-modules is an `𝒪_𝒳`-module, or a sheaf of
> `𝒪_𝒳`-modules, when it is an fppf sheaf, that is, when its underlying presheaf of abelian
> groups satisfies the sheaf condition for the fppf topology on `𝒳`.

```lean
abbrev IsModule : ObjectProperty (presheavesOfModules.{u, v, w, m} B S hS p hp)
```

**`AlgebraicGeometry.Stack.modules`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Modules.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Modules.lean#L112). The attribute's comment: “part (2), the category of modules”.

> **Stacks 06WB, part (2).** The category `Mod(𝒪_𝒳)` of `𝒪_𝒳`-modules on a category fibred in
> groupoids `𝒳` over the schemes over `S`: presheaves of `𝒪_𝒳`-modules that are fppf sheaves,
> with morphisms the morphisms of presheaves of modules.

```lean
abbrev modules
```

## Tag 06WD, an equation

[Tag 06WD](https://stacks.math.columbia.edu/tag/06WD) in the Stacks Project.

**`AlgebraicGeometry.Stack.moduleFunctoriality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuleFunctoriality.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuleFunctoriality.lean#L407).

> The two functors on presheaves of modules induced by a morphism of
> categories fibred in groupoids over the big fppf site.

```lean
noncomputable def moduleFunctoriality (hf : f ⋙ pY = pX) :
    ModuleFunctoriality.{u, v, w, m, v', w'} B S hS pX pY hpX hpY f
```

## Tag 06WE, an equation

[Tag 06WE](https://stacks.math.columbia.edu/tag/06WE) in the Stacks Project.

**`AlgebraicGeometry.Stack.modulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuleSheafFunctoriality.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuleSheafFunctoriality.lean#L84). The attribute's comment: “the inverse image, in an arbitrary module universe”.

> The inverse image of sheaves of modules along a 1-morphism of categories fibred in
> groupoids, in an arbitrary module universe: objectwise restriction of modules along `f`, with
> scalars transported along `AlgebraicGeometry.Stack.ringStructureSheafCore_obj_eq`.

```lean
noncomputable def modulePullback :
    SheafOfModules.{m} (ringStructureSheafCore B S hS q hq τ hτ) ⥤
      SheafOfModules.{m} (ringStructureSheafCore B S hS p hp τ hτ)
```

**`AlgebraicGeometry.Stack.moduleSheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuleSheafFunctoriality.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuleSheafFunctoriality.lean#L191). The attribute's comment: “the adjunction”.

> The inverse image of sheaves of modules is left adjoint to the direct image.

```lean
noncomputable def moduleSheafAdjunction :
    modulePullback.{u, v, w, max u v w m v' w', v', w'} B S hS p q hp hq f hf τ hτ ⊣
      moduleSheafPushforward.{u, v, w, m, v', w'} B S hS p q hp hq f hf τ hτ
```

**`AlgebraicGeometry.Stack.moduleSheafFunctoriality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ModuleSheafFunctoriality.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ModuleSheafFunctoriality.lean#L206). The attribute's comment: “the adjoint pair on sheaves of modules”.

> The adjoint pair of inverse- and direct-image functors on sheaves of modules induced by a
> 1-morphism of categories fibred in groupoids.

```lean
noncomputable def moduleSheafFunctoriality :
    ModuleSheafFunctoriality.{u, v, w, m, v', w'} B S hS p q hp hq f hf τ hτ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.7, Tag 06WA](https://stacks.math.columbia.edu/tag/06WA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
