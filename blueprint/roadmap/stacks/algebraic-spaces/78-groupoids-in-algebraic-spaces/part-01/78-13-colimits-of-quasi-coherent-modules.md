---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuasicoherentModule.forgetAdjunction, AlgebraicGeometry.Space.QuasicoherentModule.forgetAdjunction_unit_app, AlgebraicGeometry.Space.isCoherent_intersectionPushforward, AlgebraicGeometry.Space.QuasicoherentModule.exists_filtered_diagram_isCoherent
statement: formalized
proof: formalized
---

# 78.13 Colimits of quasi-coherent modules

Section 78.13 of the Stacks Project, [Tag 0GPN](https://stacks.math.columbia.edu/tag/0GPN). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GPP, a lemma

[Tag 0GPP](https://stacks.math.columbia.edu/tag/0GPP) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule.forgetAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentCofree.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentCofree.lean#L507).

> **Stacks 0GPP.**  Let `(U, R, s, t, c)` be a groupoid in algebraic spaces with `s` (and hence
> `t = s ∘ i`) flat, quasi-compact and quasi-separated.  For a quasi-coherent `𝒪_U`-module `𝒢` the
> module `s_*t^*𝒢` carries a canonical isomorphism `α : t^*s_*t^*𝒢 ⟶ s^*s_*t^*𝒢` making
> `(s_*t^*𝒢, α)` a quasi-coherent module on `(U, R, s, t, c)`; this defines the functor
> `AlgebraicGeometry.Space.QuasicoherentModule.cofree`, and it is right adjoint to the forgetful
> functor `(ℱ, β) ↦ ℱ`.

```lean
def forgetAdjunction : forgetQuasicoherent G ⊣ cofree G hsflat hsqc hsqs
```

## Tag 0GPQ, a remark

[Tag 0GPQ](https://stacks.math.columbia.edu/tag/0GPQ) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule.forgetAdjunction_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentCofreeUnit.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentCofreeUnit.lean#L58).

> **Stacks 0GPQ.**  Let `(U, R, s, t, c)` be a groupoid in algebraic spaces with `s` flat,
> quasi-compact and quasi-separated (then so is `t = s ∘ i`), and let
> `forgetQuasicoherent G ⊣ cofree G` be the adjunction of Stacks 0GPP between the forgetful functor
> `(ℱ, β) ↦ ℱ` and `𝒢 ↦ (s_*t^*𝒢, α)`.  The unit of this adjunction at a quasi-coherent module
> `(ℱ, β)` on the groupoid is
>
> `ℱ ⟶ s_*s^*ℱ ⟶ s_*t^*ℱ`,
>
> the unit of the adjunction `s^* ⊣ s_*` at `ℱ` followed by the direct image along `s` of the
> inverse of `β : t^*ℱ ⟶ s^*ℱ`.

```lean
theorem forgetAdjunction_unit_app (M : QuasicoherentModule B S hS G) :
    ((forgetAdjunction G hsflat hsqc hsqs).unit.app M).hom =
      (modulePullbackAdjunction B S hS G.source).unit.app M.F.obj ≫
        (modulePushforward B S hS G.source).map (inv M.alpha)
```

## Tag 0GPR, a lemma

[Tag 0GPR](https://stacks.math.columbia.edu/tag/0GPR) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_intersectionPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentIntersectionPushforwardCoherence.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentIntersectionPushforwardCoherence.lean#L149).

> **Stacks 0GPR.**  Let `f : Y ⟶ X` be a morphism of algebraic spaces over a scheme `S`, let
> `F` be a quasi-coherent `𝒪_X`-module, let `G` be an `𝒪_Y`-module and let `φ : G ⟶ f^*F` be a map
> of `𝒪_Y`-modules.  Assume that `φ` is injective, that `f` is quasi-compact, quasi-separated,
> flat and surjective, that `X` and `Y` are locally Noetherian, and that `G` is coherent.  Then
> `F ∩ f_*G`, the fibre product of `F ⟶ f_*f^*F ⟵ f_*G`, is a coherent `𝒪_X`-module.
>
> The two direct images `f_*G` and `f_*f^*F` are quasi-coherent by Stacks 03M9, so `F ∩ f_*G` is
> quasi-coherent.  Its inverse image `f^*(F ∩ f_*G)` is a quasi-coherent submodule of `G`, by
> `AlgebraicGeometry.Space.mono_intersectionPushforwardAdj`, hence coherent by Stacks 07UD, and
> coherence descends along `f` by
> `AlgebraicGeometry.Space.isCoherent_of_isCoherent_modulePullback`.

```lean
theorem isCoherent_intersectionPushforward (f : Y ⟶ X)
    (F : Modules.{u, u} B S hS X.1 X.2) (G : Modules.{u, u} B S hS Y.1 Y.2)
    (φ : G ⟶ (modulePullback B S hS f).obj F) (mono : Mono φ)
    (quasiCompact : IsQuasiCompact B S hS f.hom)
    (quasiSeparated : IsQuasiSeparated B S hS f.hom)
    (flat : IsFlat B S hS f.hom) (surjective : IsSurjective B S hS f.hom)
    (X_noetherian : HasEtaleLocalProperty B S hS X.1
      (fun V : Scheme.{u} => IsLocallyNoetherian V))
    (Y_noetherian : HasEtaleLocalProperty B S hS Y.1
      (fun V : Scheme.{u} => IsLocallyNoetherian V))
    (F_qcoh : F.IsQuasicoherentOnSite) (G_coherent : IsCoherent B S hS Y.1 Y.2 G) :
    IsCoherent B S hS X.1 X.2 (intersectionPushforward B S hS f φ)
```

## Tag 0GPS, a lemma

[Tag 0GPS](https://stacks.math.columbia.edu/tag/0GPS) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasicoherentModule.exists_filtered_diagram_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CoherentColimit.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CoherentColimit.lean#L625).

> **Stacks 0GPS.**  Let `(U, R, s, t, c)` be a groupoid in algebraic spaces over `B` such that
> `U` and `R` are Noetherian and `s` and `t` are flat, quasi-compact and quasi-separated.  Then every
> quasi-coherent module `(ℱ, β)` on `(U, R, s, t, c)` is a filtered colimit of coherent modules: it
> is the colimit of a diagram, indexed by a filtered category, of quasi-coherent modules on
> `(U, R, s, t, c)` whose underlying `𝒪_U`-modules are coherent.
>
> The diagram is indexed by the coherent submodules `ℋ` of `ℱ`, and its term at `ℋ` is the fibre
> product of the unit `(ℱ, β) ⟶ (s_*t^*ℱ, α)` of Stacks 0GPP with `(s_*t^*ℋ, α) ⟶ (s_*t^*ℱ, α)`.
> By the description of the unit in Stacks 0GPQ its underlying module is `ℱ ∩ s_*t^*ℋ`, which is
> coherent by Stacks 0GPR.

```lean
theorem exists_filtered_diagram_isCoherent (terminal_mem : B.Contains (⊤_ Scheme.{u}))
    (objects_noetherian : IsNoetherian B S hS terminal_mem G.objects.1)
    (arrows_noetherian : IsNoetherian B S hS terminal_mem G.arrows.1)
    (source_flat : IsFlat B S hS G.source.hom)
    (source_quasiCompact : IsQuasiCompact B S hS G.source.hom)
    (source_quasiSeparated : IsQuasiSeparated B S hS G.source.hom)
    (target_flat : IsFlat B S hS G.target.hom)
    (_target_quasiCompact : IsQuasiCompact B S hS G.target.hom)
    (_target_quasiSeparated : IsQuasiSeparated B S hS G.target.hom)
    (M : QuasicoherentModule B S hS G) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ QuasicoherentModule B S hS G) (φ : D ⟶ (Functor.const I).obj M),
      (∀ i, IsCoherent B S hS G.objects.1 G.objects.2 (D.obj i).F.obj) ∧
        Nonempty (IsColimit (Cocone.mk M φ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.13, Tag 0GPN](https://stacks.math.columbia.edu/tag/0GPN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
