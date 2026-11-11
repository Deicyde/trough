---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.exists_rightDerivedExtension, SheafOfModules.DifferentialGradedModule.derivedSheafHom_isRightDerivedFunctor, SheafOfModules.DifferentialGradedModule.derivedToposPushforward_isRightDerivedFunctor, SheafOfModules.DifferentialGradedModule.derivedTensorProductSheafHomAdjunction, SheafOfModules.DifferentialGradedModule.derivedPullbackRingedToposAdjunction, SheafOfModules.DifferentialGradedModule.exists_isTriangulated_homotopyToposPushforwardSheafHomTopos, SheafOfModules.DifferentialGradedModule.exists_iso_derivedToposPushforwardSheafHom, SheafOfModules.DifferentialGradedModule.derivedToposPushforward_comp
statement: formalized
proof: formalized
---

# 24.29 Derived pushforward

Section 24.29 of the Stacks Project, [Tag 0FTM](https://stacks.math.columbia.edu/tag/0FTM). 10 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FTN, a lemma

[Tag 0FTN](https://stacks.math.columbia.edu/tag/0FTN) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_rightDerivedExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRightDerivedExtension.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRightDerivedExtension.lean#L342).

> Let `X` be a ringed site and let `(A, d)` be a sheaf of differential graded algebras on it.
> Every functor `T : K(Mod(A, d)) ⥤ D` out of the homotopy category of right differential graded
> `A`-modules has a right derived extension `RT : D(A, d) ⥤ D` along the localization, and the value
> of `RT` on a graded injective and K-injective right differential graded `A`-module `I` is
> `T(I)`.

```lean
theorem exists_rightDerivedExtension
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    {H : Type*} [Category H] (T : HomotopyCategory.{u, v, max u v w} A ⥤ H) :
    ∃ (RT : derivedCategory.{u, v, max u v w} A ⥤ H)
      (β : T ⟶ toDerivedCategory.{u, v, max u v w} A ⋙ RT),
      RT.IsRightDerivedFunctor β (quasiIsomorphisms.{u, v, max u v w} A) ∧
        ∀ I : DifferentialGradedModule.{u, v, max u v w} A,
          GradedInjective I → IsKInjective I →
            RT.obj ((toDerivedCategory.{u, v, max u v w} A).obj
                ((HomotopyCategory.quotient A).obj I)) =
              T.obj ((HomotopyCategory.quotient A).obj I)
```

## Tag 0FTP, a definition

[Tag 0FTP](https://stacks.math.columbia.edu/tag/0FTP) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedSheafHom_isRightDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedInternalHomPushforward.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedInternalHomPushforward.lean#L66). The attribute's comment: “(1) derived internal hom”.

> **Stacks Project, Tag 0FTP (1): the derived internal hom.** Let `(C, O)` be a ringed site, let
> `𝒜`, `ℬ` be sheaves of differential graded `O`-algebras and let `𝒩` be a differential graded
> `(𝒜, ℬ)`-bimodule. The derived internal hom `RSheafHom_ℬ(𝒩, -) : D(ℬ, d) ⥤ D(𝒜, d)`, with its
> comparison map, is the right derived functor of the internal hom functor
> `K(SheafHom^dg_ℬ(𝒩, -)) : K(Mod(ℬ, d)) ⥤ K(Mod(𝒜, d))` followed by the localization, and its value
> on a graded injective K-injective module `ℐ` is `SheafHom^dg_ℬ(𝒩, ℐ)`.

```lean
theorem derivedSheafHom_isRightDerivedFunctor {X : AlgebraicGeometry.RingedSite.{u, u, u}}
    {A B : DifferentialGradedAlgebra.{u, u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)}
    (N : DifferentialGradedBimodule.{u, u, u} A B) :
    (derivedSheafHom N).IsRightDerivedFunctor (derivedSheafHomUnit N)
        (quasiIsomorphisms.{u, u, u} B) ∧
      ∀ I : DifferentialGradedModule.{u, u, u} B, IsDGInjective I →
        IsIso ((derivedSheafHomUnit N).app ((HomotopyCategory.quotient B).obj I))
```

**`SheafOfModules.DifferentialGradedModule.derivedToposPushforward_isRightDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedInternalHomPushforward.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedInternalHomPushforward.lean#L83). The attribute's comment: “(2) derived pushforward”.

> **Stacks Project, Tag 0FTP (2): the derived pushforward.** Let
> `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of ringed topoi, let `𝒜` be a sheaf of
> differential graded `O_C`-algebras, `ℬ` one of `O_D`-algebras and `φ : ℬ ⟶ f_*𝒜` a homomorphism
> of sheaves of differential graded `O_D`-algebras; these preserve `1` in the source, which is the
> hypothesis `unital`. The derived pushforward `Rf_* : D(𝒜, d) ⥤ D(ℬ, d)`, with its comparison map,
> is the right derived functor of the pushforward `K(f_*) : K(Mod(𝒜, d)) ⥤ K(Mod(ℬ, d))` followed by
> the localization, and its value on a graded injective K-injective module `ℐ` is `f_*ℐ`.

```lean
theorem derivedToposPushforward_isRightDerivedFunctor
    {X Y : AlgebraicGeometry.RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    (A : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O))
    (B : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O))
    (φ : B ⟶ toposPushforwardAlgebra (Osharp := X.O) (Psharp := Y.O)
      (toposDirectImageModules (X := X) (Y := Y) f) A) (unital : φ.IsUnital) :
    (derivedToposPushforward f A B φ unital).IsRightDerivedFunctor
        (derivedToposPushforwardUnit f A B φ unital) (quasiIsomorphisms.{u, u, u} A) ∧
      ∀ I : DifferentialGradedModule.{u, u, u} A, IsDGInjective I →
        IsIso ((derivedToposPushforwardUnit f A B φ unital).app
          ((HomotopyCategory.quotient A).obj I))
```

## Tag 0FTQ, a lemma

[Tag 0FTQ](https://stacks.math.columbia.edu/tag/0FTQ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedTensorProductSheafHomAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedSheafHom.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedSheafHom.lean#L176). References: SGA 5 IIIB (5.2), “more general”.

> **Stacks 0FTQ**: let `(C, O)` be a ringed site, let `𝒜` and `ℬ` be sheaves of differential
> graded `O`-algebras and let `𝒩` be a differential graded `(𝒜, ℬ)`-bimodule. Then the derived
> internal hom `RSheafHom_ℬ(𝒩, -) : D(ℬ, d) ⥤ D(𝒜, d)` is right adjoint to the derived tensor
> product `- ⊗^𝐋_𝒜 𝒩 : D(𝒜, d) ⥤ D(ℬ, d)`.
>
> The adjunction is derived (Tag 0FND, `CategoryTheory.Adjunction.derived`) from the tensor-hom
> adjunction of homotopy categories (Tag 0FRS).

```lean
def derivedTensorProductSheafHomAdjunction : derivedTensorProduct N ⊣ derivedSheafHom N
```

## Tag 0FTR, a lemma

[Tag 0FTR](https://stacks.math.columbia.edu/tag/0FTR) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedPullbackRingedToposAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackAdjunction.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPullbackAdjunction.lean#L117).

> **Stacks Project, Tag 0FTR.** Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of
> ringed topoi, let `A` be a differential graded `O_C`-algebra, let `B` be a differential graded
> `O_D`-algebra and let `φ : B ⟶ f_*A` be a homomorphism of differential graded `O_D`-algebras.
> Then `Rf_* : D(A, d) ⥤ D(B, d)` is right adjoint to `Lf^* : D(B, d) ⥤ D(A, d)`.
>
> `Lf^*` is the derived pullback of Tag 0FTG (2), `derivedPullbackRingedTopos`, and `Rf_*` the
> derived pushforward of Tag 0FTP (2), `derivedToposPushforward`. The adjunction is derived
> (Tag 0FND, `CategoryTheory.Adjunction.derived`) from the adjunction `f^* ⊣ f_*` of homotopy
> categories, `homotopyToposPullbackPushforwardAdjunction`, which is Tag 0FRU descended.

```lean
def derivedPullbackRingedToposAdjunction :
    derivedPullbackRingedTopos f φ hφ ⊣ derivedToposPushforward f A B φ hφ
```

## Tag 0FTS, an equation

[Tag 0FTS](https://stacks.math.columbia.edu/tag/0FTS) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_isTriangulated_homotopyToposPushforwardSheafHomTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPushforwardSheafHomExact.lean, line 428](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPushforwardSheafHomExact.lean#L428).

> **Stacks 0FTS.** Let `(f, f♯) : (Sh(𝒞), O_𝒞) ⟶ (Sh(𝒟), O_𝒟)` be a morphism of ringed topoi,
> let `𝒜` and `𝒜'` be sheaves of differential graded `O_𝒞`-algebras, let `ℬ` be a sheaf of
> differential graded `O_𝒟`-algebras, let `φ : ℬ ⟶ f_*𝒜` be a homomorphism and let `𝒩` be a
> differential graded `(𝒜, 𝒜')`-bimodule. Then the functor `ℳ ↦ f_*SheafHom^dg_{𝒜'}(𝒩, ℳ)`
> induces an exact functor
>
> `K(Mod(𝒜', d)) ⥤ K(Mod(ℬ, d))`
>
> of triangulated categories: there is a functor `Φ` of homotopy categories through which the
> functor of modules factors along the two quotient functors, it is the only one, and it commutes
> with the translations and carries distinguished triangles to distinguished triangles.
>
> The homomorphism `φ` is unital, as a homomorphism of differential graded algebras is in the
> source; the direct image `f_*` is that of sheaves of modules along `(f, f♯)`, made a functor of
> right differential graded modules by transporting the action along its lax monoidal structure
> and restricting scalars along `φ`.

```lean
theorem exists_isTriangulated_homotopyToposPushforwardSheafHomTopos
    {X Y : AlgebraicGeometry.RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    {A A' : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O)}
    {B : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O)}
    (φ : B ⟶ toposPushforwardAlgebra (Osharp := X.O) (Psharp := Y.O)
      (toposDirectImageModules (X := X) (Y := Y) f) A) (hφ : φ.IsUnital)
    (N : DifferentialGradedBimodule.{u, u, u} A A') :
    ∃ (Φ : HomotopyCategory.{u, u, u} A' ⥤ HomotopyCategory.{u, u, u} B)
      (_ : Φ.CommShift ℤ), Φ.IsTriangulated ∧
      HomotopyCategory.quotient A' ⋙ Φ =
        (sheafHomFunctor N ⋙
          toposPushforward (toposDirectImageModules (X := X) (Y := Y) f) φ hφ) ⋙
          HomotopyCategory.quotient B ∧
      ∀ Ψ : HomotopyCategory.{u, u, u} A' ⥤ HomotopyCategory.{u, u, u} B,
        HomotopyCategory.quotient A' ⋙ Ψ =
          (sheafHomFunctor N ⋙
            toposPushforward (toposDirectImageModules (X := X) (Y := Y) f) φ hφ) ⋙
            HomotopyCategory.quotient B → Ψ = Φ
```

## Tag 0FTT, a lemma

[Tag 0FTT](https://stacks.math.columbia.edu/tag/0FTT) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_iso_derivedToposPushforwardSheafHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPushforwardSheafHomDerived.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposPushforwardSheafHomDerived.lean#L346).

> **Stacks 0FTT.** Let `(f, f♯) : (Sh(𝒞), O_𝒞) ⟶ (Sh(𝒟), O_𝒟)` be a morphism of ringed topoi,
> let `𝒜` and `𝒜'` be sheaves of differential graded `O_𝒞`-algebras, let `ℬ` be a sheaf of
> differential graded `O_𝒟`-algebras, let `φ : ℬ ⟶ f_*𝒜` be a homomorphism and let `𝒩` be a
> differential graded `(𝒜, 𝒜')`-bimodule. Let `RT : D(𝒜', d) ⥤ D(ℬ, d)` be the right derived
> extension of the functor `ℳ ↦ f_*SheafHom^dg_{𝒜'}(𝒩, ℳ)` of [Stacks, Tag 0FTS], let
> `RSheafHom^dg_{𝒜'}(𝒩, -)` be the derived internal hom and `Rf_*` the derived pushforward of
> [Stacks, Tag 0FTP]. Then
>
> `RT(ℳ) = Rf_* RSheafHom^dg_{𝒜'}(𝒩, ℳ)`
>
> functorially in `ℳ`: there is an isomorphism of functors `RT ≅ RSheafHom^dg_{𝒜'}(𝒩, -) ⋙ Rf_*`,
> and it may be chosen compatible with the comparison maps, which is
> `exists_iso_derivedToposPushforwardSheafHom_fac`.
>
> The homomorphism `φ` is unital, as a homomorphism of differential graded algebras is in the
> source; the direct image `f_*` is that of sheaves of modules along `(f, f♯)`.

```lean
theorem exists_iso_derivedToposPushforwardSheafHom
    (N : DifferentialGradedBimodule.{u, u, u} A A') :
    Nonempty (derivedToposPushforwardSheafHom f φ hφ N ≅
      derivedSheafHom (X := X.toRingedSite) N ⋙ derivedToposPushforward f A B φ hφ)
```

## Tag 0FTU, a lemma

[Tag 0FTU](https://stacks.math.columbia.edu/tag/0FTU) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedToposPushforward_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPushforwardComp.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPushforwardComp.lean#L624).

> **Stacks Tag 0FTU.** Let `(f, f♯) : (Sh(C), O) ⟶ (Sh(C'), O')` and
> `(g, g♯) : (Sh(C'), O') ⟶ (Sh(C''), O'')` be morphisms of ringed topoi. Let `A`, `A'` and `A''`
> be a differential graded `O`-algebra, `O'`-algebra and `O''`-algebra, and let `φ : A' ⟶ f_*A`
> and `φ' : A'' ⟶ g_*A'` be homomorphisms of differential graded algebras. Then
> `R(g ∘ f)_* = Rg_* ∘ Rf_* : D(A, d) ⟶ D(A'', d)`.
>
> Here `R(g ∘ f)_*` is the derived pushforward along the composite morphism of ringed topoi
> `g.comp f` and the composite homomorphism `A'' ⟶ g_*A' ⟶ g_*f_*A = (g ∘ f)_*A`
> (`toposCompAlgebraHom`, degreewise `toposCompAlgebraHom_f`), and each derived pushforward is the
> right derived extension of the direct image of differential graded modules on homotopy
> categories (`derivedToposPushforward`). The three clauses are:
>
> 1. the direct image of differential graded modules along `g ∘ f` is the direct image along `f`
>    followed by the direct image along `g`, by the isomorphism `ηU` which in every degree is the
>    comparison `(g ∘ f)_* ≅ g_* ∘ f_*` of direct images of sheaves of modules;
> 2. `R(g ∘ f)_*` is isomorphic to `Rf_*` followed by `Rg_*`, by an isomorphism `ηD`;
> 3. `ηD` is the one induced by `ηU` (`IsInducedDerivedCompIso`): composed with the comparison map
>    of `R(g ∘ f)_*` it is the image of `ηU` followed by the composite of the comparison maps of
>    `Rf_*` and `Rg_*`.
>
> The equality of the source is an isomorphism here, the derived functors being pinned by their
> universal property. The ringed topoi have their sites and structure sheaves in one universe, the
> setting of the K-injective resolutions of Tag 0FT0.

```lean
theorem derivedToposPushforward_comp
    (f : AlgebraicGeometry.RingedToposHom X Y) (g : AlgebraicGeometry.RingedToposHom Y Z)
    (A : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O))
    (A' : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O))
    (A'' : DifferentialGradedAlgebra.{u, u} (toRingCat Z.J Z.O))
    (φ : A' ⟶ toposPushforwardAlgebra (Osharp := X.O) (Psharp := Y.O)
      (toposDirectImageModules (X := X) (Y := Y) f.toModulesHom) A)
    (unitalφ : φ.IsUnital)
    (φ' : A'' ⟶ toposPushforwardAlgebra (Osharp := Y.O) (Psharp := Z.O)
      (toposDirectImageModules (X := Y) (Y := Z) g.toModulesHom) A')
    (unitalφ' : φ'.IsUnital) :
    ∃ (ηU : toposPushforward (toposDirectImageModules (X := X) (Y := Z) (g.comp f).toModulesHom)
          (toposCompAlgebraHom (X := X) (Y := Y) (Z := Z) f g A φ φ')
          (isUnital_toposCompAlgebraHom (X := X) (Y := Y) (Z := Z) f g A unitalφ unitalφ') ≅
        toposPushforward (toposDirectImageModules (X := X) (Y := Y) f.toModulesHom) φ unitalφ ⋙
          toposPushforward (toposDirectImageModules (X := Y) (Y := Z) g.toModulesHom) φ' unitalφ')
      (ηD : derivedToposPushforward (X := X) (Y := Z) (g.comp f).toModulesHom A A''
          (toposCompAlgebraHom (X := X) (Y := Y) (Z := Z) f g A φ φ')
          (isUnital_toposCompAlgebraHom (X := X) (Y := Y) (Z := Z) f g A unitalφ unitalφ') ≅
        derivedToposPushforward (X := X) (Y := Y) f.toModulesHom A A' φ unitalφ ⋙
          derivedToposPushforward (X := Y) (Y := Z) g.toModulesHom A' A'' φ' unitalφ'),
      (∀ (M : DifferentialGradedModule.{u, u, u} A) (n : ℤ),
        (ηU.inv.app M).toHomologicalComplex.f n =
          (toposDirectImageModulesCompIso (X := X) (Y := Y) (Z := Z) f g).hom.app
            (M.complex.X n)) ∧
      IsInducedDerivedCompIso ηU ηD
```

## Tag 0FTV, a lemma

[Tag 0FTV](https://stacks.math.columbia.edu/tag/0FTV) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedSheafHomTensorBimoduleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedSheafHomTensor.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedSheafHomTensor.lean#L70).

> **Stacks 0FTV**: let `(C, O)` be a ringed site, let `𝒜`, `𝒜'`, `𝒜''` be sheaves of
> differential graded `O`-algebras, let `𝒩` be a differential graded `(𝒜, 𝒜')`-bimodule and `𝒩'` a
> differential graded `(𝒜', 𝒜'')`-bimodule, and assume that the canonical map
> `𝒩 ⊗^𝐋_{𝒜'} 𝒩' ⟶ 𝒩 ⊗_{𝒜'} 𝒩'` of `D(𝒜'', d)` is a quasi-isomorphism, `𝒩` being read as a right
> differential graded `𝒜'`-module. Then
>
> `RSheafHom_{𝒜''}(𝒩 ⊗_{𝒜'} 𝒩', -) ≅ RSheafHom_{𝒜'}(𝒩, RSheafHom_{𝒜''}(𝒩', -))`
>
> as functors `D(𝒜'', d) ⥤ D(𝒜, d)`. Both are right adjoint to `- ⊗^𝐋_𝒜 (𝒩 ⊗_{𝒜'} 𝒩')`: the first
> by Tag 0FTQ, the second as the composite of the adjunctions of Tag 0FTQ for `𝒩` and `𝒩'`,
> transported along the isomorphism `(- ⊗^𝐋_𝒜 𝒩) ⊗^𝐋_{𝒜'} 𝒩' ≅ - ⊗^𝐋_𝒜 (𝒩 ⊗_{𝒜'} 𝒩')` of
> Tag 0FTL.

```lean
def derivedSheafHomTensorBimoduleIso
    (hN : IsIso ((derivedTensorProductCounit N').app
      ((HomotopyCategory.quotient A').obj N.toRightModule))) :
    derivedSheafHom (DifferentialGradedBimodule.tensorBimodule N N') ≅
      derivedSheafHom N' ⋙ derivedSheafHom N
```

## Tag 0FTW, a lemma

[Tag 0FTW](https://stacks.math.columbia.edu/tag/0FTW) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.derivedToposPushforwardForgetIsoTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPushforwardForget.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedToposDerivedPushforwardForget.lean#L644).

> **Stacks Project, Tag 0FTW.** Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of
> ringed topoi, let `A` be a sheaf of differential graded `O_C`-algebras, `B` one of
> `O_D`-algebras and `φ : B ⟶ f_*A` a homomorphism of sheaves of differential graded
> `O_D`-algebras. Homomorphisms of differential graded algebras preserve `1` in the source, while a
> homomorphism in this development need not, so this is the hypothesis `hφ : φ.IsUnital`. Then the
> square
>
> `D(A, d) ⥤ D(O_C) ⥤ D(O_D)` and `D(A, d) ⥤ D(B, d) ⥤ D(O_D)`
>
> of the forgetful functors and the derived pushforwards commutes: `Rf_* ⋙ forget ≅ forget ⋙ Rf_*`.
> Both composites are right derived functors of the direct image of differential graded modules
> followed by forgetting the action, and the isomorphism is the one compatible with their
> comparison maps.

```lean
noncomputable def derivedToposPushforwardForgetIsoTopos
    {X Y : AlgebraicGeometry.RingedTopos.{u, u, u}} (f : RingedToposHom X Y)
    (A : DifferentialGradedAlgebra.{u, u} (toRingCat X.J X.O))
    (B : DifferentialGradedAlgebra.{u, u} (toRingCat Y.J Y.O))
    (φ : B ⟶ toposPushforwardAlgebra (Osharp := X.O) (Psharp := Y.O)
      (toposDirectImageModules (X := X) (Y := Y) f) A) (hφ : φ.IsUnital) :
    derivedToposPushforward f A B φ hφ ⋙ derivedForget B ≅
      derivedForget A ⋙ derivedModulePushforward (X := X) (Y := Y) f
```

## Tag 0FTX, a lemma

[Tag 0FTX](https://stacks.math.columbia.edu/tag/0FTX) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.cohomologyAddEquivDerivedHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologyDerivedHom.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCohomologyDerivedHom.lean#L620).

> Let `(C, O)` be a ringed site, `A` a sheaf of differential graded `O`-algebras, `M` a right
> differential graded `A`-module and `n` an integer. Then `H^n(C, M) = Hom_{D(A, d)}(A, M[n])`,
> where on the left `M` is viewed as a complex of `O`-modules.
>
> The identification is the source's: for a quasi-isomorphism `M[n] ⟶ I` into a graded injective
> and K-injective module (Tag 0FT0), morphisms `A ⟶ M[n]` of `D(A, d)` are morphisms `A ⟶ I` of
> the homotopy category (Tag 0FT8), which are morphisms `O ⟶ I` of complexes up to homotopy, and
> these compute `H^0(RΓ(C, I)) = H^n(C, M)`. The last step is the source's `RΓ(C, M) = Γ(C, I)`;
> it is proved here by comparing with a K-injective resolution of `I` in `D(O)`, using that `O`
> is resolved by flat and K-flat right differential graded `(O, 0)`-modules, the tensor product
> with `A` of such a resolution is a resolution of `A` (Tag 0FSI), and extension of scalars along
> `(O, 0) ⟶ A` is left adjoint to restriction (Tag 0FRP).

```lean
noncomputable def cohomologyAddEquivDerivedHom
    (A : DifferentialGradedAlgebra.{u, u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (M : DifferentialGradedModule.{u, u, u} A) (n : ℤ) :
    cohomology M n ≃+
      ((toDerivedCategory.{u, u, u} A).obj ((HomotopyCategory.quotient A).obj (regularModule A)) ⟶
        ((toDerivedCategory.{u, u, u} A).obj ((HomotopyCategory.quotient A).obj M))⟦n⟧)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.29, Tag 0FTM](https://stacks.math.columbia.edu/tag/0FTM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
