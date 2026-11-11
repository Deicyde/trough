---
declaration: section
origin: cited
lean: AlgebraicGeometry.groupoidSchemeOfAction, AlgebraicGeometry.equivariantModuleEquivalence, AlgebraicGeometry.equivariantModuleEquivalence_functor_obj_module, AlgebraicGeometry.equivariantModuleEquivalence_functor_obj_alpha, AlgebraicGeometry.equivariantModuleEquivalence_functor_map_hom
statement: formalized
proof: formalized
---

# 39.16 Groupoids and group schemes

Section 39.16 of the Stacks Project, [Tag 03LK](https://stacks.math.columbia.edu/tag/03LK). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0234, a lemma

[Tag 0234](https://stacks.math.columbia.edu/tag/0234) in the Stacks Project.

**`AlgebraicGeometry.groupoidSchemeOfAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/ActionGroupoid.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/ActionGroupoid.lean#L210). References: SGA 3 V (10.2).

> The action groupoid scheme of a group scheme action, with objects `X`, arrows `G ×_Y X`,
> and the source, target, composition, identity, and inverse maps given by the standard
> formulas.

```lean
noncomputable def groupoidSchemeOfAction : ActionGroupoidConstruction Y G X
```

## Tag 03LL, a lemma

[Tag 03LL](https://stacks.math.columbia.edu/tag/03LL) in the Stacks Project.

**`AlgebraicGeometry.equivariantModuleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean#L336). The attribute's comment: “the canonical equivalence”.

> **Stacks Project, Tag 03LL.** Equivariant quasi-coherent modules for an action of a group
> scheme are the same as quasi-coherent modules on the associated action groupoid scheme.

```lean
noncomputable def equivariantModuleEquivalence :
    EquivariantModule Y G X ≌
      GroupoidScheme.QuasicoherentModule (groupoidSchemeOfAction Y G X).groupoid
```

**`AlgebraicGeometry.equivariantModuleEquivalence_functor_obj_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean#L355). The attribute's comment: “underlying module”.

> **Stacks Project, Tag 03LL.** The canonical comparison leaves the underlying quasi-coherent
> module unchanged.

```lean
theorem equivariantModuleEquivalence_functor_obj_module (M : EquivariantModule Y G X) :
    ((toActionGroupoidModule Y G X).obj M).module = M.module
```

**`AlgebraicGeometry.equivariantModuleEquivalence_functor_obj_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean#L362). The attribute's comment: “descent morphism”.

> **Stacks Project, Tag 03LL.** The canonical comparison leaves the descent morphism
> unchanged.

```lean
theorem equivariantModuleEquivalence_functor_obj_alpha (M : EquivariantModule Y G X) :
    ((toActionGroupoidModule Y G X).obj M).alpha = M.alpha
```

**`AlgebraicGeometry.equivariantModuleEquivalence_functor_map_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantModule.lean#L369). The attribute's comment: “morphisms”.

> **Stacks Project, Tag 03LL.** On morphisms the canonical comparison is the identity on the
> underlying morphism of modules.

```lean
theorem equivariantModuleEquivalence_functor_map_hom {M N : EquivariantModule Y G X}
    (f : M ⟶ N) :
    ((toActionGroupoidModule Y G X).map f).hom = f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.16, Tag 03LK](https://stacks.math.columbia.edu/tag/03LK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
