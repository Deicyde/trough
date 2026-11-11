---
declaration: section
origin: cited
lean: Deformation.Artin.existsUnique_infFlatBaseChange, Deformation.Artin.exists_infFlatBaseChange_of_inertia, Deformation.Artin.LiftClassSheaf.isSheaf_liftClassPresheaf, Deformation.Artin.exists_tangentFlatBaseChange, AlgebraicGeometry.Stack.exists_lift_of_fppf_lift_of_isDeformationSituation
statement: formalized
proof: formalized
---

# 106.7 Infinitesimal deformations

Section 106.7 of the Stacks Project, [Tag 0DNQ](https://stacks.math.columbia.edu/tag/0DNQ). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DNR, a lemma

[Tag 0DNR](https://stacks.math.columbia.edu/tag/0DNR) in the Stacks Project.

**`Deformation.Artin.existsUnique_infFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/FlatBaseChange.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Infinitesimal/FlatBaseChange.lean#L205).

> **Stacks 0DNR.** Let `𝒳` be a category fibred in groupoids over the big fppf site of `S`,
> let `A → C` be a flat homomorphism of `S`-algebras, let `x` be an object of `𝒳` over `Spec A`
> and let `y = x|_{Spec C}`. Then the infinitesimal automorphisms of the trivial deformations of
> `x` and of `y` satisfy `Inf_x(M) ⊗_A C = Inf_y(C ⊗_A M)`: there is a unique `C`-linear
> isomorphism `C ⊗_A Inf_x(M) ≅ Inf_y(N)`, for `N` a site module identified with `C ⊗_A M`,
> which sends `c ⊗ θ` to the base change of `θ` scaled by `c`.
>
> The identification of `Inf_x` with `Hom_A(Q, -)`, of `Inf_y` with `Hom_C(QC, -)`, and of `QC`
> with `C ⊗_A Q`, together with the finite presentation of `Q`, are hypotheses: they are the
> inputs the source takes from Stacks 0617, 05ZF and 05ZC, which this development does not have in
> that combined form. See `Deformation.Artin.InfHomRepresentation`. What is proved here is the flat
> base change itself, by Stacks 087R.

```lean
public theorem existsUnique_infFlatBaseChange
    (D : InfHomRepresentation A C B S hS toS hA toSC hC p x y hx hy hp Dx Dy Q QC)
    (M : SiteModule A B) (N : SiteModule C B)
    (hMN : (C ⊗[A] (M.obj : Type u)) ≃ₗ[C] (N.obj : Type u)) :
    ∃ e : (C ⊗[A] (Dx.functor.obj M : Type w)) ≃ₗ[C] (Dy.functor.obj N : Type w),
      (∀ (c a : C) (θ : (Dx.functor.obj M : Type w)) (q : Q),
        D.homRepY N (e (c ⊗ₜ[A] θ)) (D.baseChangeQ (a ⊗ₜ[A] q)) =
          hMN ((a * c) ⊗ₜ[A] D.homRepX M θ q)) ∧
      ∀ e' : (C ⊗[A] (Dx.functor.obj M : Type w)) ≃ₗ[C] (Dy.functor.obj N : Type w),
        (∀ (c a : C) (θ : (Dx.functor.obj M : Type w)) (q : Q),
          D.homRepY N (e' (c ⊗ₜ[A] θ)) (D.baseChangeQ (a ⊗ₜ[A] q)) =
            hMN ((a * c) ⊗ₜ[A] D.homRepX M θ q)) → e' = e
```

**`Deformation.Artin.exists_infFlatBaseChange_of_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/InfFlatBaseChangeStack.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Infinitesimal/InfFlatBaseChangeStack.lean#L322).

> **Stacks 0DNR: infinitesimal automorphisms commute with flat base change.** Let `𝒳` be an
> algebraic stack over `S` whose inertia `ℐ_𝒳 ⟶ 𝒳` is locally of finite presentation, let `A → C`
> be a flat homomorphism of `S`-algebras, let `x` be an object of `𝒳` over `Spec A` and let
> `y = x|_{Spec C}`, exhibited by an arrow `φ : y ⟶ x` over `Spec C ⟶ Spec A`. Then for every
> `A`-module `M` there is a `C`-linear isomorphism `C ⊗_A Inf_x(M) ≅ Inf_y(C ⊗_A M)`, sending `1 ⊗ θ`
> to the image of `θ` under the map `Inf_x(M) ⟶ Inf_y(C ⊗_A M)` of Stacks 07YA (restriction of
> infinitesimal automorphisms along the arrow of trivial deformations over
> `Spec C[C ⊗_A M] ⟶ Spec A[M]`). The modules `Inf_x`, `Inf_y` are arbitrary realizations of the
> functors of Stacks 07Y9.

```lean
theorem exists_infFlatBaseChange_of_inertia (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hI : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
      (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (A C : Type u) [CommRing A] [CommRing C] [Algebra A C] [Module.Flat A C]
    (toS : Spec (.of A) ⟶ S) (hA : B.Contains (Spec (.of A)))
    (toSC : Spec (.of C) ⟶ S) (hC : B.Contains (Spec (.of C)))
    (hf : Spec.map (CommRingCat.ofHom (algebraMap A C)) ≫ toS = toSC)
    (x y : 𝒳.val.val.obj) (hx : 𝒳.val.val.p.obj x = algebraOver A B S hS toS hA)
    (hy : 𝒳.val.val.p.obj y = algebraOver C B S hS toSC hC) (φ : y ⟶ x)
    (hφ : 𝒳.val.val.p.IsHomLift
      (algebraOverMapOfRingHom (algebraMap A C) B S hS toS toSC hA hC hf) φ)
    (Dx : InfinitesimalAutomorphismFunctorData A B S hS toS hA 𝒳.val.val.p x hx
      𝒳.val.isFiberedInGroupoids)
    (Dy : InfinitesimalAutomorphismFunctorData C B S hS toSC hC 𝒳.val.val.p y hy
      𝒳.val.isFiberedInGroupoids)
    (M : SiteModule A B) :
    ∃ e : (C ⊗[A] (Dx.functor.obj M : Type u)) ≃ₗ[C]
        (Dy.functor.obj ⟨ModuleCat.of C (C ⊗[A] M.obj), isSiteModule_tensor hC M⟩ : Type u),
      ∀ t : (Dx.functor.obj M : Type u), e ((1 : C) ⊗ₜ t) =
        infBaseChangeMap (algebraMap A C) B S hS toS hA toSC hC hf 𝒳.val.val.p x y hx hy φ hφ
          𝒳.val.isFiberedInGroupoids Dx Dy (tensorCoeff (A₁ := C) M.obj) t
```

## Tag 0DNS, a lemma

[Tag 0DNS](https://stacks.math.columbia.edu/tag/0DNS) in the Stacks Project.

**`Deformation.Artin.LiftClassSheaf.isSheaf_liftClassPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/LiftClassSheafCondition.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Infinitesimal/LiftClassSheafCondition.lean#L149).

> **Stacks 0DNS.** For an algebraic stack over a base scheme whose inertia is locally of finite
> presentation, and a deformation situation `(A' → A, x)`, the functor sending an affine
> `A'`-algebra `B'` to the isomorphism classes of lifts of `x|_{B' ⊗_{A'} A}` to `B'` is a sheaf on
> the big affine fppf site of `Spec A'`.

```lean
theorem isSheaf_liftClassPresheaf
    (hI : Stack.AlgebraicStacks.IsLocallyOfFinitePresentation B S hS
      (Stack.relativeInertiaProjection B S hS (Stack.structureMorphism B S hS 𝒳)))
    (hi : IsDeformationSituation (ringMap B S hS i).hom) (P : LiftClassPresheaf B S hS 𝒳 i x hx) :
    Presheaf.IsSheaf ((BigAffineFppf.topology B S hS).over U') P.presheaf
```

## Tag 0DNT, a lemma

[Tag 0DNT](https://stacks.math.columbia.edu/tag/0DNT) in the Stacks Project.

**`Deformation.Artin.exists_tangentFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Infinitesimal/TangentFlatBaseChangeStack.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Infinitesimal/TangentFlatBaseChangeStack.lean#L587).

> **Stacks 0DNT: tangent modules of an algebraic stack commute with flat base change.** Let `𝒳`
> be an algebraic stack over `S` with `𝒳 → S` locally of finite presentation, `A → C` a flat
> homomorphism of `S`-algebras, `x` an object of `𝒳` over `Spec A` and `y = x|_{Spec C}`, exhibited
> by a strongly cartesian arrow `β : y ⟶ x` over `Spec C ⟶ Spec A`. Then for every `A`-module `M`
> there is a `C`-linear isomorphism `C ⊗_A T_x(M) ≅ T_y(C ⊗_A M)`, the one induced by pulling lifts
> back along `Spec C[C ⊗_A M] ⟶ Spec A[M]`: the ring map `r : A[M] → C[C ⊗_A M]` is `A → C` on
> `A` and `m ↦ 1 ⊗ m` on `M`, and `1 ⊗ t` is sent to the class of the cartesian pullback along
> `Spec r` of a lift representing `t`. The tangent modules are arbitrary realizations of the
> tangent functors of Stacks 07Y9.

```lean
theorem exists_tangentFlatBaseChange
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (f : 𝒳 ⟶ Stack.schemeFibredCategory B S hS (Over.mk (𝟙 (B.obj hS))))
    (hf : HasPropertyOnEverySmoothDiagram B S hS
      (fun _ _ g => Space.IsLocallyOfFinitePresentation B S hS g) f)
    (A C : Type u) [CommRing A] [CommRing C] [Algebra A C] [Module.Flat A C]
    (toS : Spec (.of A) ⟶ S) (hA : B.Contains (Spec (.of A)))
    (toS' : Spec (.of C) ⟶ S) (hC : B.Contains (Spec (.of C)))
    (x y : 𝒳.val.obj) (hx : 𝒳.val.p.obj x = algebraOver A B S hS toS hA)
    (hy : 𝒳.val.p.obj y = algebraOver C B S hS toS' hC)
    (b : algebraOver C B S hS toS' hC ⟶ algebraOver A B S hS toS hA)
    (hb : (BigFppfOver.toScheme B S hS).map b = Spec.map (CommRingCat.ofHom (algebraMap A C)))
    (β : y ⟶ x) (hβ : 𝒳.val.p.IsStronglyCartesian b β)
    (M : SiteModule A B) (hMC : IsSiteModule C B (ModuleCat.of C (C ⊗[A] M.obj)))
    (Tx : TangentFunctorData A B S hS toS hA 𝒳.val.p x hx)
    (Ty : TangentFunctorData C B S hS toS' hC 𝒳.val.p y hy) :
    let N : SiteModule C B := ⟨ModuleCat.of C (C ⊗[A] M.obj), hMC⟩
    ∃ (r : squareZeroRing A M.obj ⟶ squareZeroRing C N.obj)
      (g : squareZeroOver C B S hS toS' N ⟶ squareZeroOver A B S hS toS M)
      (e : (C ⊗[A] (Tx.functor.obj M : Type _)) ≃ₗ[C] (Ty.functor.obj N : Type _)),
      ((BigFppfOver.toScheme B S hS).map g = Spec.map r) ∧
      (∀ z : TrivSqZeroExt A M.obj,
        (r.hom z).fst = algebraMap A C z.fst ∧ (r.hom z).snd = (1 : C) ⊗ₜ[A] z.snd) ∧
      (∀ t : (Tx.functor.obj M : Type _),
        ∃ (a : (Under.post 𝒳.val.p).Fiber
            (Under.mk (eqToHom hx ≫ squareZeroArrow A B S hS toS hA M)))
          (c : (Under.post 𝒳.val.p).Fiber
            (Under.mk (eqToHom hy ≫ squareZeroArrow C B S hS toS' hC N))),
          Quotient.mk _ a = Tx.liftEquiv M t ∧
          Quotient.mk _ c = Ty.liftEquiv N (e ((1 : C) ⊗ₜ[A] t)) ∧
          ∃ φ : c.1.right ⟶ a.1.right,
            𝒳.val.p.IsStronglyCartesian g φ ∧ c.1.hom ≫ φ = β ≫ a.1.hom)
```

## Tag 0DNU, a lemma

[Tag 0DNU](https://stacks.math.columbia.edu/tag/0DNU) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_lift_of_fppf_lift_of_isDeformationSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GroupoidLift/StackFppfLift.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GroupoidLift/StackFppfLift.lean#L333).

> **Stacks 0DNU.** Let `𝒳` be an algebraic stack over `S` whose structure morphism is locally of
> finite presentation, and let `(A' → A, x)` be a deformation situation, `A' → A` being
> `Γ(U') → Γ(U)` for the closed immersion `i : U ⟶ U'` of affines and `x` an object over `U`. If
> there are a faithfully flat finitely presented `A'`-algebra `B' = Γ(V')` and an object `y'` of `𝒳`
> over `B'` lifting the restriction `y` of `x` to `B' ⊗_{A'} A = Γ(V)`, then there is an object `x'`
> over `A'` lifting `x`.

```lean
theorem exists_lift_of_fppf_lift_of_isDeformationSituation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (f : 𝒳 ⟶ schemeFibredCategory B S hS (Over.mk (𝟙 (B.obj hS))))
    (hf : HasPropertyOnEverySmoothDiagram B S hS
      (fun _ _ g => Space.IsLocallyOfFinitePresentation B S hS g) f)
    (U U' V V' : BigAffineFppf B S hS)
    (i : U ⟶ U') (j : V ⟶ U) (l : V ⟶ V') (k : V' ⟶ U')
    (hsq : j ≫ i = l ≫ k)
    (hpb : IsPushout
      ((BigAffineFppf.toScheme B S hS).map i).appTop
      ((BigAffineFppf.toScheme B S hS).map k).appTop
      ((BigAffineFppf.toScheme B S hS).map j).appTop
      ((BigAffineFppf.toScheme B S hS).map l).appTop)
    (hi : Deformation.Artin.IsDeformationSituation
      ((BigAffineFppf.toScheme B S hS).map i).appTop.hom)
    (hff : ((BigAffineFppf.toScheme B S hS).map k).appTop.hom.FaithfullyFlat)
    (hfp : ((BigAffineFppf.toScheme B S hS).map k).appTop.hom.FinitePresentation)
    (x : 𝒳.val.obj)
    (hx : 𝒳.val.p.obj x = (BigAffineFppf.inclusion B S hS).obj U)
    (y : 𝒳.val.obj)
    (_hy : 𝒳.val.p.obj y = (BigAffineFppf.inclusion B S hS).obj V)
    (α : y ⟶ x)
    (hα : 𝒳.val.p.IsStronglyCartesian ((BigAffineFppf.inclusion B S hS).map j) α)
    (hlift : ∃ (y' : 𝒳.val.obj)
      (_hy' : 𝒳.val.p.obj y' = (BigAffineFppf.inclusion B S hS).obj V')
      (β : y ⟶ y'), 𝒳.val.p.IsStronglyCartesian ((BigAffineFppf.inclusion B S hS).map l) β) :
    ∃ (x' : 𝒳.val.obj)
      (_hx' : 𝒳.val.p.obj x' = (BigAffineFppf.inclusion B S hS).obj U')
      (β : x ⟶ x'), 𝒳.val.p.IsStronglyCartesian ((BigAffineFppf.inclusion B S hS).map i) β
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.7, Tag 0DNQ](https://stacks.math.columbia.edu/tag/0DNQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
