---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.QuasicoherentModule, Stacks.Groupoids.GroupoidScheme.QuasicoherentModule.alpha_isIso, Stacks.Groupoids.GroupoidScheme.pullbackFunctor, Stacks.Groupoids.GroupoidScheme.pullbackFunctor_obj_module, Stacks.Groupoids.GroupoidScheme.pullbackFunctor_obj_alpha, Stacks.Groupoids.GroupoidScheme.pullbackFunctor_map_hom, Stacks.Groupoids.GroupoidScheme.pushforwardFunctor, Stacks.Groupoids.GroupoidScheme.pushforwardFunctor_obj_module
statement: formalized
proof: formalized
---

# 39.14 Quasi-coherent sheaves on groupoids

Section 39.14 of the Stacks Project, [Tag 03LH](https://stacks.math.columbia.edu/tag/03LH). 6 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03LI, a definition

[Tag 03LI](https://stacks.math.columbia.edu/tag/03LI) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.QuasicoherentModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Pullback.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/Pullback.lean#L200).

> A quasi-coherent module on a groupoid scheme, with its descent morphism, cocycle law, and
> normalization along the identity section.

```lean
structure QuasicoherentModule {S : Scheme.{u}} (G : GroupoidScheme S)
```

## Tag 077Q, a lemma

[Tag 077Q](https://stacks.math.columbia.edu/tag/077Q) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.QuasicoherentModule.alpha_isIso`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/DescentIso.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/DescentIso.lean#L424).

> The descent morphism of a quasi-coherent module on a groupoid scheme is an isomorphism.

```lean
instance alpha_isIso (M : QuasicoherentModule G) : IsIso M.alpha
```

## Tag 03LJ, a lemma

[Tag 03LJ](https://stacks.math.columbia.edu/tag/03LJ) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.pullbackFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean#L197). The attribute's comment: “the functor”.

> **Stacks Project, Tag 03LJ.** Pullback along a morphism of groupoid schemes, as a functor on
> quasi-coherent modules equipped with groupoid descent data.  On objects it sends `(F, α)` to
> `(f⁺F, f⁺α)`, using the canonical comparison isomorphisms for pullback along composites; on
> morphisms it is the usual pullback of morphisms of modules.

```lean
noncomputable def pullbackFunctor (f : Hom G H) :
    QuasicoherentModule H ⥤ QuasicoherentModule G
```

**`Stacks.Groupoids.GroupoidScheme.pullbackFunctor_obj_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean#L220). The attribute's comment: “underlying modules”.

> **Stacks Project, Tag 03LJ.** Pullback along a morphism of groupoid schemes pulls back the
> underlying module along the map on objects.

```lean
theorem pullbackFunctor_obj_module (f : Hom G H) (M : QuasicoherentModule H) :
    ((pullbackFunctor f).obj M).module =
      (Scheme.Modules.pullback f.mapObjects.left).obj M.module
```

**`Stacks.Groupoids.GroupoidScheme.pullbackFunctor_obj_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean#L228). The attribute's comment: “descent morphisms”.

> **Stacks Project, Tag 03LJ.** The descent morphism of a pulled-back module is the canonical
> pullback of the original descent morphism.

```lean
theorem pullbackFunctor_obj_alpha (f : Hom G H) (M : QuasicoherentModule H) :
    Eq.ndrec (motive := fun X =>
      (Scheme.Modules.pullback G.target.left).obj X ⟶
        (Scheme.Modules.pullback G.source.left).obj X)
      ((pullbackFunctor f).obj M).alpha (pullbackFunctor_obj_module f M) =
      pullbackDescent f M
```

**`Stacks.Groupoids.GroupoidScheme.pullbackFunctor_map_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PullbackFunctor.lean#L239). The attribute's comment: “morphisms”.

> **Stacks Project, Tag 03LJ.** Pullback of a morphism of quasi-coherent modules on a groupoid
> scheme is the usual pullback of morphisms of modules.

```lean
theorem pullbackFunctor_map_hom (f : Hom G H) {M N : QuasicoherentModule H} (g : M ⟶ N) :
    (pullbackFunctor_obj_module f M) ▸
      (pullbackFunctor_obj_module f N) ▸
        (QuasicoherentModule.Hom.hom ((pullbackFunctor f).map g)) =
      (Scheme.Modules.pullback f.mapObjects.left).map g.hom
```

## Tag 09VH, a lemma

[Tag 09VH](https://stacks.math.columbia.edu/tag/09VH) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.pushforwardFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean#L507). The attribute's comment: “the functor”. References: SGA 3 I (6.6.2), “more general”.

> **Stacks Project, Tag 09VH.** Pushforward along a morphism of groupoid schemes, as a functor
> on quasi-coherent modules equipped with groupoid descent data:  on objects it sends `(𝓕, α)` to
> `(f_*𝓕, f_*α)`, and on morphisms it is the direct image of morphisms of modules.

```lean
noncomputable def pushforwardFunctor :
    QuasicoherentModule G ⥤ QuasicoherentModule H
```

**`Stacks.Groupoids.GroupoidScheme.pushforwardFunctor_obj_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean#L530). The attribute's comment: “underlying modules”.

> **Stacks Project, Tag 09VH.** Pushforward along a morphism of groupoid schemes pushes the
> underlying module forward along the map on objects.

```lean
theorem pushforwardFunctor_obj_module (M : QuasicoherentModule G) :
    ((pushforwardFunctor f h).obj M).module =
      (Scheme.Modules.pushforward f.mapObjects.left).obj M.module
```

**`Stacks.Groupoids.GroupoidScheme.pushforwardFunctor_obj_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean#L538). The attribute's comment: “descent morphisms”.

> **Stacks Project, Tag 09VH.** The descent morphism of a pushed-forward module is the
> pushed-forward descent morphism.

```lean
theorem pushforwardFunctor_obj_alpha (M : QuasicoherentModule G) :
    Eq.ndrec (motive := fun X =>
      (Scheme.Modules.pullback H.target.left).obj X ⟶
        (Scheme.Modules.pullback H.source.left).obj X)
      ((pushforwardFunctor f h).obj M).alpha (pushforwardFunctor_obj_module f h M) =
      pushforwardDescent f h M
```

**`Stacks.Groupoids.GroupoidScheme.pushforwardFunctor_map_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean#L549). The attribute's comment: “morphisms”.

> **Stacks Project, Tag 09VH.** Pushforward of a morphism of quasi-coherent modules on a
> groupoid scheme is the direct image of morphisms of modules.

```lean
theorem pushforwardFunctor_map_hom {M N : QuasicoherentModule G} (g : M ⟶ N) :
    (pushforwardFunctor_obj_module f h M) ▸
      (pushforwardFunctor_obj_module f h N) ▸
        (QuasicoherentModule.Hom.hom ((pushforwardFunctor f h).map g)) =
      (Scheme.Modules.pushforward f.mapObjects.left).map
        (QuasicoherentModule.Hom.hom g)
```

**`Stacks.Groupoids.GroupoidScheme.pullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean, line 656](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Equivariant/PushforwardDescent.lean#L656). The attribute's comment: “right adjointness to the pullback functor of Tag 03LJ”.

> **Stacks Project, Tag 09VH.** Pushforward along a morphism of groupoid schemes is right
> adjoint to the pullback functor of Tag 03LJ:  on underlying modules the adjunction is the
> inverse-image--direct-image adjunction along the map on objects, under which the two
> compatibility conditions with the descent morphisms correspond.

```lean
noncomputable def pullbackPushforwardAdjunction :
    pullbackFunctor f ⊣ pushforwardFunctor f h
```

## Tag 077R, a lemma

[Tag 077R](https://stacks.math.columbia.edu/tag/077R) in the Stacks Project.

**`AlgebraicGeometry.instHasColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidColimits.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidColimits.lean#L252).

> The category of quasi-coherent modules on a groupoid scheme admits all colimits.

```lean
instance instHasColimits {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) :
    HasColimits (Stacks.Groupoids.GroupoidScheme.QuasicoherentModule G)
```

## Tag 077S, a lemma

[Tag 077S](https://stacks.math.columbia.edu/tag/077S) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.QuasicoherentModule.abelian`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/QuasicoherentAbelian.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/QuasicoherentAbelian.lean#L480). References: SGA 3 I (4.7.2.1), “Mod.q.c. case”.

> **Let `S` be a scheme and let `G` be a groupoid scheme over `S` whose source and target are
> flat.  Then the category of quasi-coherent modules on `G` is abelian.**

```lean
noncomputable instance abelian : Abelian (QuasicoherentModule G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.14, Tag 03LH](https://stacks.math.columbia.edu/tag/03LH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
