---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.exists_isTriangulated_homotopyToposPullbackTensorTopos, SheafOfModules.DifferentialGradedModule.isLeftDerived_derivedPullbackTensorRingedTopos, SheafOfModules.DifferentialGradedModule.derivedPullbackRingedTopos, SheafOfModules.DifferentialGradedModule.derivedTensorProductTopos, SheafOfModules.DifferentialGradedModule.exists_iso_derivedPullbackTensorRingedTopos_derivedPullbackRingedTopos_comp_topos, SheafOfModules.DifferentialGradedModule.derivedPullbackRingedToposCompIso, SheafOfModules.DifferentialGradedModule.isIso_derivedTensorProductMap, SheafOfModules.DifferentialGradedModule.isIso_derivedTensorProductCounit_of_isGood
statement: formalized
proof: formalized
---

# 24.28 Derived pullback

Section 24.28 of the Stacks Project, [Tag 0FTD](https://stacks.math.columbia.edu/tag/0FTD). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FTE, an equation

[Tag 0FTE](https://stacks.math.columbia.edu/tag/0FTE) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_isTriangulated_homotopyToposPullbackTensorTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPullbackTensorExact.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPullbackTensorExact.lean#L290).

> **Stacks 0FTE.** Let `(f, f♯) : (Sh(𝒞), O_𝒞) ⟶ (Sh(𝒟), O_𝒟)` be a morphism of ringed topoi,
> let `𝒜` and `𝒜'` be sheaves of differential graded `O_𝒞`-algebras, let `ℬ` be a sheaf of
> differential graded `O_𝒟`-algebras, let `φ : ℬ ⟶ f_*𝒜` be a homomorphism and let `𝒩` be a
> differential graded `(𝒜, 𝒜')`-bimodule. Then the functor `ℳ ↦ f^*ℳ ⊗_𝒜 𝒩` induces an exact
> functor
>
> `K(Mod(ℬ, d)) ⥤ K(Mod(𝒜', d))`
>
> of triangulated categories: there is a functor `Φ` of homotopy categories through which the
> functor of modules factors along the two quotient functors, it is the only one, and it commutes
> with the translations and carries distinguished triangles to distinguished triangles.
>
> Here `f^*ℳ` is the pullback `f^*ℳ ⊗_{f^*ℬ} 𝒜` along `(f, 𝒜, φ)`, the homomorphism `φ` is
> unital, as a homomorphism of differential graded algebras is in the source, and `Φ` is
> `homotopyToposPullbackTensor`, by `homotopyToposPullbackTensor_eq`.

```lean
theorem exists_isTriangulated_homotopyToposPullbackTensorTopos
    {X Y : AlgebraicGeometry.RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    {A A' : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O)}
    {B : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O)}
    (φ : B ⟶ toposPushforwardAlgebra (Osharp := X.O) (Psharp := Y.O)
      (toposDirectImageModules (X := X) (Y := Y) f) A) (hφ : φ.IsUnital)
    (N : DifferentialGradedBimodule.{u, u, u} A A') :
    ∃ (Φ : HomotopyCategory.{u, u, u} B ⥤ HomotopyCategory.{u, u, u} A')
      (_ : Φ.CommShift ℤ), Φ.IsTriangulated ∧
      HomotopyCategory.quotient B ⋙ Φ =
        toposPullbackTensor (X := X) (Y := Y) f φ hφ N ⋙ HomotopyCategory.quotient A' ∧
      ∀ Ψ : HomotopyCategory.{u, u, u} B ⥤ HomotopyCategory.{u, u, u} A',
        HomotopyCategory.quotient B ⋙ Ψ =
          toposPullbackTensor (X := X) (Y := Y) f φ hφ N ⋙ HomotopyCategory.quotient A' →
            Ψ = Φ
```

## Tag 0FTF, a lemma

[Tag 0FTF](https://stacks.math.columbia.edu/tag/0FTF) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isLeftDerived_derivedPullbackTensorRingedTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackTriangulated.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackTriangulated.lean#L245). References: SGA 4 XVII (4.2.12), “more general”.

> **Stacks Project, Tag 0FTF.** Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of
> ringed topoi, let `A` and `A'` be sheaves of differential graded `O_C`-algebras, let `B` be a sheaf
> of differential graded `O_D`-algebras, let `φ : B ⟶ f_*A` be a homomorphism of sheaves of
> differential graded algebras and let `𝒩` be a differential graded `(A, A')`-bimodule. The exact
> functor `K(Mod(B, d)) ⟶ K(Mod(A', d))`, `M ↦ f^*M ⊗_A 𝒩` of Tag 0FTE (where `f^*M = f^*M ⊗_{f^*B} A`
> is the pullback along `(f, A, φ)`), composed with the localization functor
> `K(Mod(A', d)) → D(A', d)`, has a left derived extension `D(B, d) → D(A', d)` whose value on a good
> right differential graded `B`-module `P` is `f^*P ⊗_A 𝒩`: `derivedPullbackTensorRingedTopos`, with
> its comparison map, is the left derived functor, the comparison map is invertible at every good
> module (so that the value there is `derivedPullbackTensorRingedToposObjIso`), and the extension is
> an exact functor of triangulated categories.

```lean
theorem isLeftDerived_derivedPullbackTensorRingedTopos :
    (derivedPullbackTensorRingedTopos f φ hφ N).IsLeftDerivedFunctor
        (derivedPullbackTensorRingedToposCounit f φ hφ N) (quasiIsomorphisms.{u, u, u} B) ∧
      (∀ P : DifferentialGradedModule.{u, u, u} B, IsGoodToposBaseChange.{u, u, u} P →
        IsIso ((derivedPullbackTensorRingedToposCounit f φ hφ N).app
          ((HomotopyCategory.quotient B).obj P))) ∧
      ∃ (_ : (derivedPullbackTensorRingedTopos f φ hφ N).CommShift ℤ),
        (derivedPullbackTensorRingedTopos f φ hφ N).IsTriangulated
```

## Tag 0FTG, a definition

[Tag 0FTG](https://stacks.math.columbia.edu/tag/0FTG) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedPullbackRingedTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullback.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullback.lean#L577). The attribute's comment: “(2) derived pullback Lf^*”. References: SGA 4 XVII (4.2.12), “Lg*, special case”.

> **The derived pullback** `Lf^* : D(B, d) ⥤ D(A, d)` along a morphism of ringed topoi
> `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and a homomorphism `φ : B ⟶ f_*A` of sheaves of
> differential graded algebras: the functor of Tag 0FTF for the diagonal bimodule `{}_A A_A`, that
> is `derivedPullbackTensorRingedTopos f φ hφ A.diagonalBimodule`. It is the left derived functor
> of `M ↦ f^*M ⊗_A A` followed by the localization
> (`isLeftDerivedFunctor_derivedPullbackRingedTopos`), and its value on a good module `P` is
> `f^*P = f^*P ⊗_{f^*B} A` (`derivedPullbackRingedToposObjIso`).

```lean
def derivedPullbackRingedTopos : derivedCategory.{u, u, u} B ⥤ derivedCategory.{u, u, u} A
```

**`SheafOfModules.DifferentialGradedModule.derivedTensorProductTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedTensorProduct.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedTensorProduct.lean#L337). The attribute's comment: “(1) the derived tensor product - ⊗^L\_A N”. References: SGA 4 XVII (4.2.12), “The case g = id”.

> **The derived tensor product** `- ⊗^𝐋_A N : D(A, d) ⥤ D(A', d)`. Let `(Sh(C), O)` be a ringed
> topos, let `A` and `A'` be sheaves of differential graded `O`-algebras and let `N` be a
> differential graded `(A, A')`-bimodule. The derived tensor product is the functor
> `D(A, d) ⥤ D(A', d)` of Tag 0FTF for the identity morphism of `(Sh(C), O)` and the identity
> homomorphism `A ⟶ id_*A`: `derivedPullbackTensorRingedTopos` at `RingedToposHom.id` and
> `toposIdAlgebraHom`. It is the left derived functor of `M ↦ M ⊗_A N` followed by the localization,
> and it is the derived tensor product `derivedTensorProduct` constructed on the ringed site
> (`derivedTensorProductToposIso`).

```lean
def derivedTensorProductTopos :
    derivedCategory.{u, u, u} A ⥤ derivedCategory.{u, u, u} A'
```

## Tag 0FTH, a lemma

[Tag 0FTH](https://stacks.math.columbia.edu/tag/0FTH) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_iso_derivedPullbackTensorRingedTopos_derivedPullbackRingedTopos_comp_topos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackComp.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackComp.lean#L473).

> Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of ringed topoi, `A`, `A'` sheaves
> of differential graded `O_C`-algebras, `B` a sheaf of differential graded `O_D`-algebras,
> `φ : B ⟶ f_*A` a homomorphism of differential graded algebras and `𝒩` a differential graded
> `(A, A')`-bimodule. The functor `D(B, d) ⥤ D(A', d)` of Tag 0FTF,
> `derivedPullbackTensorRingedTopos f φ hφ 𝒩`, is `M ↦ Lf^*M ⊗^𝐋_A 𝒩`, where `Lf^*` is the
> derived pullback of Tag 0FTG (2) and `- ⊗^𝐋_A 𝒩` the derived tensor product of Tag 0FTG (1),
> `derivedTensorProductTopos`: there is an isomorphism
> `derivedPullbackTensorRingedTopos f φ hφ 𝒩 ≅ Lf^* ⋙ - ⊗^𝐋_A 𝒩` carrying the comparison map of
> the former to that of the latter.

```lean
theorem exists_iso_derivedPullbackTensorRingedTopos_derivedPullbackRingedTopos_comp_topos :
    ∃ e : derivedPullbackTensorRingedTopos f φ hφ N ≅
        derivedPullbackRingedTopos f φ hφ ⋙ derivedTensorProductTopos N,
      Functor.whiskerLeft (toDerivedCategory B) e.hom ≫
          derivedPullbackRingedToposTensorToposCounit f φ hφ N =
        derivedPullbackTensorRingedToposCounit f φ hφ N
```

## Tag 0FTI, a lemma

[Tag 0FTI](https://stacks.math.columbia.edu/tag/0FTI) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedPullbackRingedToposCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackComp.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackComp.lean#L505).

> Let `(f, f♯) : (Sh(C), O) ⟶ (Sh(C'), O')` and `(g, g♯) : (Sh(C'), O') ⟶ (Sh(C''), O'')` be
> morphisms of ringed topoi, `𝒜`, `𝒜'`, `𝒜''` differential graded `O`-, `O'`- and `O''`-algebras,
> and `φ : 𝒜' ⟶ f_*𝒜`, `φ' : 𝒜'' ⟶ g_*𝒜'` homomorphisms of differential graded algebras. Then
> `L(g ∘ f)^* = Lf^* ∘ Lg^*` as functors `D(𝒜'', d) ⥤ D(𝒜, d)`, the derived pullback along `g ∘ f`
> being taken along the composite homomorphism `𝒜'' ⟶ g_*𝒜' ⟶ g_*f_*𝒜 = (g ∘ f)_*𝒜`.

```lean
def derivedPullbackRingedToposCompIso :
    derivedPullbackRingedTopos (X := X) (Y := Z)
        (RingedToposHom.comp (X := X) (Y := Y) (Z := Z) g f)
        (toposCompHom (X := X) (Y := Y) (Z := Z) f g A φ φ')
        (isUnital_toposCompHom (X := X) (Y := Y) (Z := Z) f g A hφ hφ') ≅
      derivedPullbackRingedTopos (X := Y) (Y := Z) g φ' hφ' ⋙
        derivedPullbackRingedTopos (X := X) (Y := Y) f φ hφ
```

## Tag 0FTJ, a lemma

[Tag 0FTJ](https://stacks.math.columbia.edu/tag/0FTJ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isIso_derivedTensorProductMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedTensorProductMap.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedTensorProductMap.lean#L242).

> **Stacks 0FTJ.** Let `(𝒞, 𝒪)` be a ringed site, let `𝒜` and `ℬ` be differential graded
> `𝒪`-algebras and let `ν : 𝒩 ⟶ 𝒩'` be a homomorphism of differential graded
> `(𝒜, ℬ)`-bimodules which is an isomorphism on cohomology sheaves. Then the canonical
> transformation `t : (- ⊗^𝐋_𝒜 𝒩) ⟶ (- ⊗^𝐋_𝒜 𝒩')` is an isomorphism of functors
> `D(𝒜, d) ⥤ D(ℬ, d)`.

```lean
theorem isIso_derivedTensorProductMap (ν : N ⟶ N') (qis : IsCohomologyIso ν.toHomologicalComplex) :
    IsIso (derivedTensorProductMap ν)
```

## Tag 0FTK, a lemma

[Tag 0FTK](https://stacks.math.columbia.edu/tag/0FTK) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isIso_derivedTensorProductCounit_of_isGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedTensorKFlat.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedTensorKFlat.lean#L212). The attribute's comment: “M ⊗^L\_A N = M ⊗\_A N for N good as a left module”.

> Let `(𝒞, 𝒪)` be a ringed site, `𝒜`, `𝒜'` differential graded `𝒪`-algebras and `𝒩` a
> differential graded `(𝒜, 𝒜')`-bimodule which is good (Tag 0FSA) as a left differential graded
> `𝒜`-module. Then `ℳ ⊗^𝐋_𝒜 𝒩 = ℳ ⊗_𝒜 𝒩` for every differential graded `𝒜`-module `ℳ`: the canonical
> map from the derived tensor product to the tensor product is an isomorphism of functors.

```lean
theorem isIso_derivedTensorProductCounit_of_isGood
    (hN : IsGoodToposBaseChange.{u, v₁, u₁} (Y := X.toRingedTopos)
      (A := (A : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O)).op)
      N.toLeftDifferentialGradedModule.opRight) :
    IsIso (derivedTensorProductCounit N)
```

## Tag 0FTL, a lemma

[Tag 0FTL](https://stacks.math.columbia.edu/tag/0FTL) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedTensorProductCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedTensorProductComposition.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedTensorProductComposition.lean#L208).

> Let `(𝒞, 𝒪)` be a ringed site, let `𝒜`, `𝒜'`, `𝒜''` be sheaves of differential graded
> `𝒪`-algebras, let `𝒩` be a differential graded `(𝒜, 𝒜')`-bimodule and `𝒩'` a differential graded
> `(𝒜', 𝒜'')`-bimodule. Assume that the canonical map `𝒩 ⊗^𝐋_{𝒜'} 𝒩' ⟶ 𝒩 ⊗_{𝒜'} 𝒩'` of `D(𝒜'', d)` is
> an isomorphism. Then `(ℳ ⊗^𝐋_𝒜 𝒩) ⊗^𝐋_{𝒜'} 𝒩' = ℳ ⊗^𝐋_𝒜 (𝒩 ⊗_{𝒜'} 𝒩')` as functors
> `D(𝒜, d) ⥤ D(𝒜'', d)`.

```lean
noncomputable def derivedTensorProductCompIso
    (hN : IsIso ((derivedTensorProductCounit N').app
      ((HomotopyCategory.quotient A').obj N.toRightModule))) :
    derivedTensorProduct N ⋙ derivedTensorProduct N' ≅
      derivedTensorProduct (DifferentialGradedBimodule.tensorBimodule N N')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.28, Tag 0FTD](https://stacks.math.columbia.edu/tag/0FTD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
