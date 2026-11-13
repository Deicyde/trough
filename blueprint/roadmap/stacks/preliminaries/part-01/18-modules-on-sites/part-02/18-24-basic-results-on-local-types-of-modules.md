---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.LocalCokernel.isFinitePresentation_cokernel, Stacks.SheafOfModules.SliceFinite.isFiniteType_kernel_of_epi, ChaoticQCoh.quasiCoherent_iff_canonicalMap_isIso, Stacks.SheafOfModules.isQuasicoherent_iff_canonicalMap_isIso, Stacks.Sheaves.ChaoticFlatQuasicoherent.isQuasicoherentOnSite_isWeakSerreClass
statement: formalized
proof: formalized
---

# 18.24 Basic results on local types of modules

Section 18.24 of the Stacks Project, [Tag 082S](https://stacks.math.columbia.edu/tag/082S). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H98, a lemma

[Tag 0H98](https://stacks.math.columbia.edu/tag/0H98) in the Stacks Project.

**`Stacks.SheafOfModules.LocalCokernel.isFinitePresentation_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CokernelFinitePresentation.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/CokernelFinitePresentation.lean#L716).

> **Stacks Project, Tag 0H98.** The cokernel of a morphism from a finite-type sheaf of
> modules to a finitely presented sheaf of modules on a ringed site is finitely presented.

```lean
theorem isFinitePresentation_cokernel
    (X : AlgebraicGeometry.RingedSite.{u, v, w})
    [HasWeakSheafify X.J AddCommGrpCat.{w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{w}]
    [∀ U : X.C, HasWeakSheafify (X.J.over U) AddCommGrpCat.{w}]
    [∀ U : X.C, (X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    {F G : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)} (φ : G ⟶ F)
    [F.IsFinitePresentation] [G.IsFiniteType] :
    (cokernel φ).IsFinitePresentation
```

## Tag 082T, a lemma

[Tag 082T](https://stacks.math.columbia.edu/tag/082T) in the Stacks Project.

**`Stacks.SheafOfModules.SliceFinite.isFiniteType_kernel_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SliceRestrictionFiniteKernel.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SliceRestrictionFiniteKernel.lean#L226).

> On a site with no products and no pullbacks assumed, the kernel of a surjection from a sheaf
> of modules of finite type onto a sheaf of modules of finite presentation is of finite type. This
> also gives Stacks Project, Tag 01BP part (2).

```lean
theorem isFiniteType_kernel_of_epi {F G : SheafOfModules.{u} R}
    [F.IsFinitePresentation] [G.IsFiniteType] (theta : G ⟶ F) [Epi theta] :
    (kernel theta).IsFiniteType
```

## Tag 0GZN, a lemma

[Tag 0GZN](https://stacks.math.columbia.edu/tag/0GZN) in the Stacks Project.

**`ChaoticQCoh.quasiCoherent_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/QuasicoherentChaotic.lean, line 913](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/QuasicoherentChaotic.lean#L913).

> Stacks Tag `0GZN`, Lemma 18.24.3: A sheaf of `O`-modules `F` on the chaotic
> site `C` is quasi-coherent if and only if for every morphism `f : U ⟶ V` of `C`
> the canonical map `c_f : F(V) ⊗_{O(V)} O(U) ⟶ F(U)` is an isomorphism.

```lean
theorem quasiCoherent_iff_canonicalMap_isIso :
    QuasiCoherent O F ↔ ∀ ⦃U V : C⦄ (f : U ⟶ V), IsIso (canonicalMap O F f)
```

**`Stacks.SheafOfModules.isQuasicoherent_iff_canonicalMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentChaoticSite.lean, line 679](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentChaoticSite.lean#L679).

> A module sheaf on a chaotic site is quasi-coherent precisely when its
> canonical base-change maps are isomorphisms.

```lean
public theorem isQuasicoherent_iff_canonicalMap_isIso
    (hX : X.J = ⊥) :
    F.IsQuasicoherentOnSite ↔
      ∀ ⦃U V : X.C⦄ (f : U ⟶ V), IsIso (canonicalMap X F f)
```

## Tag 0GZP, a lemma

[Tag 0GZP](https://stacks.math.columbia.edu/tag/0GZP) in the Stacks Project.

**`Stacks.Sheaves.ChaoticFlatQuasicoherent.isQuasicoherentOnSite_isWeakSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ChaoticFlatQuasicoherent.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ChaoticFlatQuasicoherent.lean#L475).

> Quasi-coherent modules on a chaotic site with flat restrictions form a
> weak Serre subcategory of all sheaves of modules.

```lean
public instance isQuasicoherentOnSite_isWeakSerreClass
    (X : RingedSite.{u, v, r}) [Fact (X.J = ⊥)]
    [Fact (∀ {U V : X.Cᵒᵖ} (a : V ⟶ U),
      RingHom.Flat (X.O.obj.map a).hom)] :
    ObjectProperty.IsWeakSerreClass
      (SheafOfModules.isQuasicoherentOnSite (Stacks.SheafOfModules.Tensor.ringSheaf X.O) :
        ObjectProperty (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.24, Tag 082S](https://stacks.math.columbia.edu/tag/082S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
