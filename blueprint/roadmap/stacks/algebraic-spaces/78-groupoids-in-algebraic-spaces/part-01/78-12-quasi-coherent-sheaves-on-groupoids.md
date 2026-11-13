---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuasicoherentModule, AlgebraicGeometry.Space.QuasicoherentModule.isIso_alpha, AlgebraicGeometry.Space.groupoidQuasicoherentPullback, AlgebraicGeometry.Space.groupoidModulePullbackTransition_unit, AlgebraicGeometry.Space.groupoidModulePullbackTransition_cocycle, AlgebraicGeometry.Space.groupoidQuasicoherentPullbackPushforwardAdjunction, AlgebraicGeometry.Space.quasicoherentModule_hasColimits_of_closure, AlgebraicGeometry.Space.QuasicoherentModule.abelian_of_closure
statement: formalized
proof: formalized
---

# 78.12 Quasi-coherent sheaves on groupoids

Section 78.12 of the Stacks Project, [Tag 0440](https://stacks.math.columbia.edu/tag/0440). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0441, a definition

[Tag 0441](https://stacks.math.columbia.edu/tag/0441) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentModules.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentModules.lean#L392).

> **Stacks 0441.**  A quasi-coherent module on a groupoid in algebraic spaces `(U, R, s, t, c)`
> over `A`: a quasi-coherent `𝒪_U`-module `ℱ` together with a morphism `α : t^*ℱ ⟶ s^*ℱ` of
> `𝒪_R`-modules which satisfies the cocycle condition on the space of composable pairs of arrows
> and restricts to the identity along the unit.

```lean
structure QuasicoherentModule (G : GroupoidInAlgebraicSpaces B S hS A)
```

## Tag 077W, a lemma

[Tag 077W](https://stacks.math.columbia.edu/tag/077W) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule.isIso_alpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentTransition.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentTransition.lean#L347).

> The transition morphism `α : t^*ℱ ⟶ s^*ℱ` of a quasi-coherent module on a groupoid in
> algebraic spaces is an isomorphism.

```lean
theorem isIso_alpha (M : QuasicoherentModule 𝒞 S hS G) : IsIso M.alpha
```

## Tag 0442, a lemma

[Tag 0442](https://stacks.math.columbia.edu/tag/0442) in the Stacks Project.

**`AlgebraicGeometry.Space.groupoidQuasicoherentPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidQuasicoherentPullbackFunctor.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidQuasicoherentPullbackFunctor.lean#L216). The attribute's comment: “the inverse image functor on quasi-coherent modules”.

> **Stacks 0442.**  The inverse image along a morphism `f` of groupoids in algebraic spaces is
> a functor `QCoh(U', R', s', t', c') ⥤ QCoh(U, R, s, t, c)`: it sends a quasi-coherent module
> `(ℱ, α)` on the target groupoid to the inverse image `(f^*ℱ, f^*α)` of
> `AlgebraicGeometry.Space.groupoidQuasicoherentPullbackObj`, and a morphism to the inverse image
> of the underlying morphism of modules on the spaces of objects.

```lean
def groupoidQuasicoherentPullback :
    QuasicoherentModule B S hS G' ⥤ QuasicoherentModule B S hS G
```

**`AlgebraicGeometry.Space.groupoidModulePullbackTransition_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentPullback.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentPullback.lean#L514). The attribute's comment: “the unit law for the transition morphism of the inverse image”.

> **The unit law for the transition morphism of the inverse image.**  If the transition
> morphism `α` of a module on the target groupoid restricts along the unit arrow to the canonical
> identification of the two inverse images, then so does the transition morphism of the inverse
> image along the unit arrow of the source groupoid.
>
> This is the unit law of Stacks 0441 for the pair `(f^*ℱ, f^*α)`.

```lean
theorem groupoidModulePullbackTransition_unit (φ : Hom G G')
    (F : Modules.{u, u} B S hS G'.objects.1 G'.objects.2)
    (α : (modulePullback B S hS G'.target).obj F ⟶ (modulePullback B S hS G'.source).obj F)
    (hunit : groupoidPullbackTransition B S hS G' F α (identityArrow G') =
      pullbackTransport F ((identityArrow_comp_target G').trans
        (identityArrow_comp_source G').symm)) :
    groupoidPullbackTransition B S hS G ((modulePullback B S hS φ.objectsMap).obj F)
        (groupoidModulePullbackTransition B S hS φ F α) (identityArrow G) =
      pullbackTransport ((modulePullback B S hS φ.objectsMap).obj F)
        ((identityArrow_comp_target G).trans (identityArrow_comp_source G).symm)
```

**`AlgebraicGeometry.Space.groupoidModulePullbackTransition_cocycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentPullback.lean, line 564](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentPullback.lean#L564). The attribute's comment: “the cocycle law for the transition morphism of the inverse image”.

> **The cocycle law for the transition morphism of the inverse image.**  If the transition
> morphism `α` of a module on the target groupoid satisfies the cocycle law on the space of
> composable pairs of arrows of the target groupoid, then the transition morphism of the inverse
> image satisfies it on the space of composable pairs of arrows of the source groupoid.
>
> This is the cocycle law of Stacks 0441 for the pair `(f^*ℱ, f^*α)`.  Flattened along the map on
> objects, both sides become the corresponding sides of the law for `α` at the three morphisms the
> map on composable pairs carries the composition and the two projections to.

```lean
theorem groupoidModulePullbackTransition_cocycle (φ : Hom G G')
    (F : Modules.{u, u} B S hS G'.objects.1 G'.objects.2)
    (α : (modulePullback B S hS G'.target).obj F ⟶ (modulePullback B S hS G'.source).obj F)
    (hcocycle : groupoidPullbackTransition B S hS G' F α G'.comp =
      groupoidTransitionComposite B S hS G' F α) :
    groupoidPullbackTransition B S hS G ((modulePullback B S hS φ.objectsMap).obj F)
        (groupoidModulePullbackTransition B S hS φ F α) G.comp =
      groupoidTransitionComposite B S hS G ((modulePullback B S hS φ.objectsMap).obj F)
        (groupoidModulePullbackTransition B S hS φ F α)
```

## Tag 0GPM, a lemma

[Tag 0GPM](https://stacks.math.columbia.edu/tag/0GPM) in the Stacks Project.

**`AlgebraicGeometry.Space.groupoidQuasicoherentPullbackPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentPushforwardAdjunction.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentPushforwardAdjunction.lean#L391).

> **Stacks 0GPM.**  Let `f : (U, R, s, t, c) ⟶ (U', R', s', t', c')` be a morphism of
> groupoids in algebraic spaces over `A` such that `f : U ⟶ U'` is quasi-compact and
> quasi-separated, the square formed by `f : R ⟶ R'`, the target morphisms `t, t'` and
> `f : U ⟶ U'` is cartesian, and `s'` is flat.  Then pushforward `(ℱ, α) ↦ (f_*ℱ, f_*α)`
> (`AlgebraicGeometry.Space.groupoidQuasicoherentPushforward`) is a functor from the
> quasi-coherent modules on `(U, R, s, t, c)` to those on `(U', R', s', t', c')`, and it is right
> adjoint to the inverse image functor of Stacks 0442
> (`AlgebraicGeometry.Space.groupoidQuasicoherentPullback`).

```lean
def groupoidQuasicoherentPullbackPushforwardAdjunction :
    groupoidQuasicoherentPullback B S hS φ ⊣
      groupoidQuasicoherentPushforward B S hS φ hqc hqs hpb hsflat
```

## Tag 077X, a lemma

[Tag 077X](https://stacks.math.columbia.edu/tag/077X) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentModule_hasColimits_of_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentColimits.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentColimits.lean#L408).

> **Stacks 077X.**  The category of quasi-coherent modules on a groupoid in algebraic spaces
> has colimits, indexed by the categories of the universe of the schemes.
>
> A colimit is computed on the underlying `𝒪_U`-modules, where it exists because the sheaves of
> modules on the small étale ringed site of an algebraic space are cocomplete, and it is
> quasi-coherent by the arbitrary-colimit clause of Stacks 03M1,
> `AlgebraicGeometry.Space.isClosedUnderColimitsOfShape_quasicoherentSheaves_schemeUniverse`.

```lean
theorem quasicoherentModule_hasColimits_of_closure (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {A : AlgebraicSpaces B S hS}
    (G : GroupoidInAlgebraicSpaces B S hS A) :
    HasColimitsOfSize.{u, u} (QuasicoherentModule B S hS G)
```

## Tag 06VZ, a lemma

[Tag 06VZ](https://stacks.math.columbia.edu/tag/06VZ) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule.abelian_of_closure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentAbelian.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentAbelian.lean#L632).

> **Stacks 06VZ.**  If the source and the target of a groupoid in algebraic spaces
> `(U, R, s, t, c)` over `A` are flat, the quasi-coherent modules on it form an abelian category.
>
> Kernels and cokernels are computed on the underlying `𝒪_U`-modules, which are quasi-coherent by
> the kernel and cokernel clauses of Stacks 03M1(3).  A transition morphism is carried along a
> cokernel because an inverse image of `𝒪`-modules is a left adjoint, and along a kernel because
> the inverse images along `s`, along `c ≫ s` and along `e ≫ s` are left exact: `s` is flat,
> `c` is a base change of `s` by Stacks 043Z, and `e ≫ s` is the identity.  The flatness of `t` is
> not used, being equivalent to that of `s` in a groupoid.

```lean
noncomputable def abelian_of_closure (hs : IsFlat B S hS G.source.hom)
    (_ht : IsFlat B S hS G.target.hom) :
    Abelian (QuasicoherentModule B S hS G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.12, Tag 0440](https://stacks.math.columbia.edu/tag/0440)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
