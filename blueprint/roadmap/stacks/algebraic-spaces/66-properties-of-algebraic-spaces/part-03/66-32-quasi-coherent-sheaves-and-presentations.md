---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.quasicoherentModuleOfBase, Stacks.Groupoids.GroupoidScheme.quasicoherentModuleOfBaseFunctor, AlgebraicGeometry.Space.quasicoherentModuleOfSpaceBase, AlgebraicGeometry.Space.isEquivalence_quasicoherentFromSpaceBase, AlgebraicGeometry.Space.equivalenceQuasicoherentFromSpaceBase, AlgebraicGeometry.Space.quasicoherentFromSpaceBase, AlgebraicGeometry.Space.quasicoherentSheaves_isGrothendieckAbelian_enoughInjectives_hasLimits, AlgebraicGeometry.Space.exists_coherator
statement: formalized
proof: formalized
---

# 66.32 Quasi-coherent sheaves and presentations

Section 66.32 of the Stacks Project, [Tag 03M2](https://stacks.math.columbia.edu/tag/03M2). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03M3, a proposition

[Tag 03M3](https://stacks.math.columbia.edu/tag/03M3) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.quasicoherentModuleOfBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/QuasicoherentFromBase.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/QuasicoherentFromBase.lean#L244). The attribute's comment: “the canonical descent datum on φ^*ℱ and the two conditions of Stacks 03LI, for a target which is a scheme”.

> **Stacks 03M3**, the descent datum.  For a quasi-coherent module `ℱ` on a scheme `X` and a
> morphism `φ : U ⟶ X` from the object scheme of a groupoid with `t ≫ φ = s ≫ φ`, the pullback
> `φ^*ℱ` together with its canonical descent morphism is a quasi-coherent module on the
> groupoid.

```lean
def quasicoherentModuleOfBase (F : X.Modules) (hF : F.IsQuasicoherent) :
    QuasicoherentModule G
```

**`Stacks.Groupoids.GroupoidScheme.quasicoherentModuleOfBaseFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/QuasicoherentFromBase.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/QuasicoherentFromBase.lean#L257). The attribute's comment: “the functor ℱ ↦ (φ^*ℱ, α), for a target which is a scheme”.

> **Stacks 03M3**, the functor.  Pullback along `φ` together with the canonical descent
> morphism is functorial in the quasi-coherent module on the base.

```lean
def quasicoherentModuleOfBaseFunctor :
    ObjectProperty.FullSubcategory (fun F : X.Modules => F.IsQuasicoherent) ⥤
      QuasicoherentModule G
```

**`AlgebraicGeometry.Space.quasicoherentModuleOfSpaceBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBase.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBase.lean#L341). The attribute's comment: “the canonical descent datum on φ^*ℱ and the two conditions of Stacks 0441, for a target which is an algebraic space”.

> **Stacks 03M3**, the descent datum, for a target which is an algebraic space.  For a
> quasi-coherent module `ℱ` on an algebraic space `X` and a morphism `φ : U ⟶ X` from the
> object space of a groupoid in algebraic spaces with `t ≫ φ = s ≫ φ`, the inverse image `φ^*ℱ`
> together with its canonical transition morphism is a quasi-coherent module on the groupoid.

```lean
def quasicoherentModuleOfSpaceBase (φ : G.objects ⟶ X)
    (hφ : G.target ≫ φ = G.source ≫ φ) (M : Modules.{u, u} B S hS X.1 X.2)
    (hM : M.IsQuasicoherentOnSite) : QuasicoherentModule B S hS G
```

**`AlgebraicGeometry.Space.isEquivalence_quasicoherentFromSpaceBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBaseEquivalence.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBaseEquivalence.lean#L252). The attribute's comment: “the functor QCoh(𝒪\_X) ⥤ QCoh(U, R, s, t, c) is an equivalence of categories, for a target which is an algebraic space: full faithfulness and essential surjectivity at the hypotheses of the source”.

> The functor `ℱ ↦ (φ^*ℱ, α)` from the quasi-coherent `𝒪_X`-modules to the quasi-coherent
> modules on `(U, R, s, t, c)` is an equivalence of categories, for `φ : U ⟶ X` étale with
> `t ≫ φ = s ≫ φ`, `{φ}` a surjective étale covering of `X`, `φ` relatively representable, and the
> arrow space the kernel pair `R = U ×_X U` with `t`, `s` the two projections.

```lean
theorem isEquivalence_quasicoherentFromSpaceBase
    (hcov : IsEtaleCovering B S hS (fun _ : Unit => G.objects.1) (fun _ => φ.hom))
    (hrep : yoneda.relativelyRepresentable φ.hom)
    (hpb : IsPullback G.target.hom G.source.hom φ.hom φ.hom) :
    (quasicoherentFromSpaceBase B S hS G φ hφ).IsEquivalence
```

**`AlgebraicGeometry.Space.equivalenceQuasicoherentFromSpaceBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBaseEquivalence.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBaseEquivalence.lean#L269). The attribute's comment: “the equivalence QCoh(𝒪\_X) ≌ QCoh(U, R, s, t, c) itself, for a target which is an algebraic space, at the hypotheses of the source”.

> The equivalence `QCoh(𝒪_X) ≌ QCoh(U, R, s, t, c)` whose functor is
> `AlgebraicGeometry.Space.quasicoherentFromSpaceBase`, under the hypotheses of
> `AlgebraicGeometry.Space.isEquivalence_quasicoherentFromSpaceBase`.

```lean
def equivalenceQuasicoherentFromSpaceBase
    (hcov : IsEtaleCovering B S hS (fun _ : Unit => G.objects.1) (fun _ => φ.hom))
    (hrep : yoneda.relativelyRepresentable φ.hom)
    (hpb : IsPullback G.target.hom G.source.hom φ.hom φ.hom) :
    QuasicoherentSheaves.{u, u} B S hS X.obj X.property ≌ QuasicoherentModule B S hS G
```

**`AlgebraicGeometry.Space.quasicoherentFromSpaceBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBaseFunctor.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasicoherentFromSpaceBaseFunctor.lean#L169). The attribute's comment: “the functor QCoh(𝒪\_X) ⥤ QCoh(U, R, s, t, c) of the equivalence, for a target which is an algebraic space; this declaration is the functor itself, that it is an equivalence being proved in QuasicoherentFromSpaceBaseEquivalence.lean”.

> **The functor `QCoh(𝒪_X) ⥤ QCoh(U, R, s, t, c)` attached to an étale `φ : U ⟶ X` with
> `t ≫ φ = s ≫ φ`**: it sends a quasi-coherent `𝒪_X`-module `ℱ` to `φ^*ℱ` with its canonical
> transition morphism, and a morphism to its inverse image along `φ`.

```lean
def quasicoherentFromSpaceBase :
    QuasicoherentSheaves.{u, u} B S hS X.obj X.property ⥤ QuasicoherentModule B S hS G
```

## Tag 077V, a proposition

[Tag 077V](https://stacks.math.columbia.edu/tag/077V) in the Stacks Project.

**`AlgebraicGeometry.Space.quasicoherentSheaves_isGrothendieckAbelian_enoughInjectives_hasLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSeparator.lean, line 1011](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSeparator.lean#L1011). The attribute's comment: “(1) QCoh(𝒪\_X) is a Grothendieck abelian category; consequently it has enough injectives and all limits”. References: SGA 4 I (7.13), “special case”; SGA 4 V (0.2.1), “special case”.

> **Stacks 077V, part (1).**  Let `F` be an algebraic space over a scheme `S`.  The category
> `QCoh(𝒪_F)` of quasi-coherent `𝒪_F`-modules is a Grothendieck abelian category; consequently it
> has enough injectives and all limits.
>
> The abelian structure is the one given by the kernel and cokernel clauses of Stacks 03M1.  The
> three conditions of a Grothendieck abelian category are: colimits, which exist and agree with
> those of `𝒪_F`-modules by Stacks 03M1; exactness of filtered colimits; and a generator, which
> is `AlgebraicGeometry.Space.hasSeparator_quasicoherentSheaves`, built from a presentation
> `F = U/R` through Stacks 03M3 and 077U.  The assertions on injectives and limits hold in every
> Grothendieck abelian category (Stacks 079H, 07D8).

```lean
theorem quasicoherentSheaves_isGrothendieckAbelian_enoughInjectives_hasLimits :
    letI := isClosedUnderKernels_quasicoherentSheaves_schemeUniverse B S hS F hF
    letI := isClosedUnderCokernels_quasicoherentSheaves B S hS F hF
    letI := quasicoherentSheaves_abelian_of_closure B S hS F hF
    IsGrothendieckAbelian.{u} (QuasicoherentSheaves.{u, u} B S hS F hF) ∧
      EnoughInjectives (QuasicoherentSheaves.{u, u} B S hS F hF) ∧
      HasLimitsOfSize.{u, u} (QuasicoherentSheaves.{u, u} B S hS F hF)
```

**`AlgebraicGeometry.Space.exists_coherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSeparator.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasicoherentSeparator.lean#L1033). The attribute's comment: “(2) the inclusion QCoh(𝒪\_X) ⥤ Mod(𝒪\_X) has a right adjoint Q whose adjunction morphism Q(F) ⟶ F is an isomorphism for every quasi-coherent F”.

> **Stacks 077V, part (2).**  Let `F` be an algebraic space over a scheme `S`.  The inclusion
> functor `QCoh(𝒪_F) ⥤ Mod(𝒪_F)` has a right adjoint `Q`, the *coherator*, such that for every
> quasi-coherent `𝒪_F`-module `𝓕` the adjunction morphism `Q(𝓕) ⟶ 𝓕` is an isomorphism.
>
> The right adjoint exists by the special adjoint functor theorem applied to the Grothendieck
> abelian category of part (1),
> `AlgebraicGeometry.Space.isLeftAdjoint_ι_quasicoherentSheaves`; the inclusion is fully
> faithful, so the counit is an isomorphism exactly on its essential image,
> `AlgebraicGeometry.Space.isIso_quasicoherentCoheratorCounit_app`.

```lean
theorem exists_coherator :
    ∃ (Q : Modules.{u, u} B S hS F hF ⥤ QuasicoherentSheaves.{u, u} B S hS F hF)
      (adj : (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS F hF).O))).ι ⊣ Q),
      ∀ (M : Modules.{u, u} B S hS F hF), M.IsQuasicoherentOnSite → IsIso (adj.counit.app M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.32, Tag 03M2](https://stacks.math.columbia.edu/tag/03M2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
