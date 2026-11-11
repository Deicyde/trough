---
declaration: section
origin: cited
lean: SheafOfModules.IsFinitePresentation, SheafOfModules.instIsQuasicoherentOfIsFinitePresentation, Stacks.SheafOfModules.isFinitePresentation_cokernel, Stacks.SheafOfModules.SliceFinite.isFiniteType_kernel_of_epi_from_finite_free, Stacks.SheafOfModules.LocalKernel.kernel_isFiniteType_of_epi_from_finiteType, Stacks.SheafOfModules.modulePullback_isFinitePresentation, Stacks.AssociatedSheaf.exists_directed_system_of_isFinitePresentation, Stacks.SheafOfModules.exists_iso_free_over_of_stalk_iso_free
statement: formalized
proof: formalized
---

# 17.11 Modules of finite presentation

Section 17.11 of the Stacks Project, [Tag 01BM](https://stacks.math.columbia.edu/tag/01BM). 7 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01BN, a definition

[Tag 01BN](https://stacks.math.columbia.edu/tag/01BN) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.IsFinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.IsFinitePresentation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch17.lean#L56) (StacksFrontier). References: EGA 0 (5.2.5); SGA 4 VI (5.6), “special case”; SGA 6 II (2.4.3).

## Tag 01BO, a lemma

[Tag 01BO](https://stacks.math.columbia.edu/tag/01BO) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.instIsQuasicoherentOfIsFinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instIsQuasicoherentOfIsFinitePresentation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch17.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch17.lean#L58) (StacksFrontier). References: EGA 0 (5.2.5), “more general”.

## Tag 0H96, a lemma

[Tag 0H96](https://stacks.math.columbia.edu/tag/0H96) in the Stacks Project.

**`Stacks.SheafOfModules.isFinitePresentation_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FinitePresentationCokernel.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FinitePresentationCokernel.lean#L224).

> The cokernel of a morphism from a finite type sheaf of modules to a finitely presented sheaf
> of modules is finitely presented.

```lean
theorem isFinitePresentation_cokernel {F G : SheafOfModules.{u} R} (φ : G ⟶ F)
    [F.IsFinitePresentation] [G.IsFiniteType] :
    (cokernel φ).IsFinitePresentation
```

## Tag 01BP, a lemma

[Tag 01BP](https://stacks.math.columbia.edu/tag/01BP) in the Stacks Project.

**`Stacks.SheafOfModules.SliceFinite.isFiniteType_kernel_of_epi_from_finite_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SliceRestrictionFiniteKernel.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SliceRestrictionFiniteKernel.lean#L253). The attribute's comment: “part (1)”.

> On a site with no products and no pullbacks assumed, the kernel of a surjection from a
> finite-rank free sheaf of modules onto a sheaf of modules of finite presentation is of finite
> type.

```lean
theorem isFiniteType_kernel_of_epi_from_finite_free {I : Type u} [Finite I]
    {F : SheafOfModules.{u} R} [F.IsFinitePresentation] (psi : free I ⟶ F) [Epi psi] :
    (kernel psi).IsFiniteType
```

**`Stacks.SheafOfModules.LocalKernel.kernel_isFiniteType_of_epi_from_finiteType`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorExactnessSheafify.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorExactnessSheafify.lean#L294). The attribute's comment: “part (2)”.

> The kernel of a surjection from a finite-type sheaf of modules onto a finitely presented sheaf
> of modules is of finite type.

```lean
instance kernel_isFiniteType_of_epi_from_finiteType {F G : SheafOfModules.{u} R}
    [F.IsFinitePresentation] [G.IsFiniteType] (theta : G ⟶ F) [Epi theta] :
    (kernel theta).IsFiniteType
```

## Tag 01BQ, a lemma

[Tag 01BQ](https://stacks.math.columbia.edu/tag/01BQ) in the Stacks Project.

**`Stacks.SheafOfModules.modulePullback_isFinitePresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FinitePresentationPullback.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FinitePresentationPullback.lean#L353).

> **Stacks 01BQ.** The pullback of a sheaf of modules of finite presentation along a
> morphism of ringed spaces is of finite presentation.

```lean
lemma modulePullback_isFinitePresentation {X Y : RingedSpace.{u, u}} (f : X ⟶ Y)
    (G : _root_.SheafOfModules.{u} (structureSheafRing Y)) [G.IsFinitePresentation] :
    ((modulePullback f).obj G).IsFinitePresentation
```

## Tag 01BR, a lemma

[Tag 01BR](https://stacks.math.columbia.edu/tag/01BR) in the Stacks Project.

**`Stacks.AssociatedSheaf.exists_directed_system_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafDirectedColimit.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AssociatedSheafDirectedColimit.lean#L51).

> **Stacks 01BR.** The sheaf associated to a module over a ring mapping to the global sections
> of a ringed space is a directed colimit of sheaves of modules of finite presentation.

```lean
theorem exists_directed_system_of_isFinitePresentation (X : RingedSpace.{u, u}) {R : Type u}
    [CommRing R] (α : R →+* X.presheaf.obj (op ⊤)) (M : ModuleCat.{u} R) :
    ∃ (I : Type u) (_ : Preorder I) (_ : Nonempty I)
      (_ : IsDirected I (· ≤ ·))
      (D : I ⥤ SheafOfModules.{u} (structureSheafRing X))
      (φ : D ⟶ (Functor.const I).obj (associatedSheaf X α M)),
      (∀ i, (D.obj i).IsFinitePresentation) ∧
        Nonempty (IsColimit (Cocone.mk (associatedSheaf X α M) φ))
```

## Tag 0B8J, a lemma

[Tag 0B8J](https://stacks.math.columbia.edu/tag/0B8J) in the Stacks Project.

**`Stacks.SheafOfModules.exists_iso_free_over_of_stalk_iso_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkFreeCover.lean, line 1455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkFreeCover.lean#L1455). References: EGA 0 (5.2.7), “free case G = O^r”.

> **Stacks Project, Tag 0B8J.** Let `(X, 𝒪_X)` be a ringed space and let `M` be a finitely
> presented sheaf of `𝒪_X`-modules. If the stalk of `M` at a point `x` is free of rank `r` over
> `𝒪_{X, x}`, then the restriction of `M` to some open neighbourhood of `x` is isomorphic to the
> free sheaf of modules of rank `r`.

```lean
theorem exists_iso_free_over_of_stalk_iso_free {X : TopCat.{u}}
    {R : TopCat.Sheaf RingCat.{u} X} (M : SheafOfModules.{u} R)
    (hM : M.IsFinitePresentation) (x : X) (r : ℕ)
    (hx : Nonempty
      (ToType (TopCat.Presheaf.stalk M.val.presheaf x) ≃ₗ[ToType (R.presheaf.stalk x)]
        (ULift.{u} (Fin r) →₀ ToType (R.presheaf.stalk x)))) :
    ∃ U : TopologicalSpace.Opens X, x ∈ U ∧
      Nonempty (M.over U ≅ SheafOfModules.free (ULift.{u} (Fin r)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.11, Tag 01BM](https://stacks.math.columbia.edu/tag/01BM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
