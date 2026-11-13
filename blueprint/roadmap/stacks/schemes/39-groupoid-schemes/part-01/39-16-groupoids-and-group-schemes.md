---
declaration: section
origin: cited
lean: AlgebraicGeometry.groupoidSchemeOfAction, AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence, AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence_functor_obj_module, AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence_functor_obj_alpha, AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence_functor_map_hom
statement: formalized
proof: formalized
---

# 39.16 Groupoids and group schemes

Section 39.16 of the Stacks Project, [Tag 03LK](https://stacks.math.columbia.edu/tag/03LK). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0234, a lemma

[Tag 0234](https://stacks.math.columbia.edu/tag/0234) in the Stacks Project.

**`AlgebraicGeometry.groupoidSchemeOfAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/ActionGroupoid.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/ActionGroupoid.lean#L210). References: SGA 3 V (10.2).

> The action groupoid scheme of a group scheme action, with objects `X`, arrows `G ×_Y X`,
> and the source, target, composition, identity, and inverse maps given by the standard
> formulas.

```lean
noncomputable def groupoidSchemeOfAction : ActionGroupoidConstruction Y G X
```

## Tag 03LL, a lemma

[Tag 03LL](https://stacks.math.columbia.edu/tag/03LL) in the Stacks Project.

**`AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean#L293). The attribute's comment: “the equivalence (F, α) ↦ (F, α)”.

> **Stacks Project, Tag 03LL.** The rule `(F, α) ↦ (F, α)` is an equivalence between
> `G`-equivariant quasi-coherent modules on `X` (Stacks 03LF, cocycle on `G ×_Y G ×_Y X`) and
> quasi-coherent modules on the action groupoid scheme `(X, G ×_Y X, s, t, c)` (cocycle on
> `R ×_{s, X, t} R`).

```lean
noncomputable def equivariantQuasicoherentModuleEquivalence :
    EquivariantQuasicoherentModule Y G X ≌
      GroupoidScheme.QuasicoherentModule (groupoidSchemeOfAction Y G X).groupoid
```

**`AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence_functor_obj_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean#L307). The attribute's comment: “underlying module”.

> **Stacks Project, Tag 03LL.** The equivalence keeps the underlying quasi-coherent module.

```lean
theorem equivariantQuasicoherentModuleEquivalence_functor_obj_module
    (M : EquivariantQuasicoherentModule Y G X) :
    ((equivariantQuasicoherentModuleEquivalence Y G X).functor.obj M).module = M.module
```

**`AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence_functor_obj_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean#L314). The attribute's comment: “the map α”.

> **Stacks Project, Tag 03LL.** The equivalence keeps the map `α`.

```lean
theorem equivariantQuasicoherentModuleEquivalence_functor_obj_alpha
    (M : EquivariantQuasicoherentModule Y G X) :
    ((equivariantQuasicoherentModuleEquivalence Y G X).functor.obj M).alpha = M.alpha
```

**`AlgebraicGeometry.equivariantQuasicoherentModuleEquivalence_functor_map_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/EquivariantQuasicoherentModule.lean#L322). The attribute's comment: “morphisms”.

> **Stacks Project, Tag 03LL.** On morphisms the equivalence is the identity on the underlying
> morphism of modules.

```lean
theorem equivariantQuasicoherentModuleEquivalence_functor_map_hom
    {M N : EquivariantQuasicoherentModule Y G X} (f : M ⟶ N) :
    ((equivariantQuasicoherentModuleEquivalence Y G X).functor.map f).hom = f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.16, Tag 03LK](https://stacks.math.columbia.edu/tag/03LK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
