---
declaration: section
origin: cited
lean: Stacks.Coherent.coherentAdicSystemsEquivFGModuleCat, Stacks.Coherent.globalSectionsComparison, Stacks.Coherent.globalSectionsComparison_naturality, Stacks.Coherent.globalSectionsComparison_projection_surjective, Stacks.Coherent.globalSectionsComparison_projection_ker, Stacks.Coherent.abelian_coherentAdicSystems, Stacks.Coherent.restrictFunctor_exact, Stacks.Coherent.exact_iff_restrict
statement: formalized
proof: formalized
---

# 30.23 Coherent formal modules

Section 30.23 of the Stacks Project, [Tag 0EHN](https://stacks.math.columbia.edu/tag/0EHN). 12 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 087W, a lemma

[Tag 087W](https://stacks.math.columbia.edu/tag/087W) in the Stacks Project.

**`Stacks.Coherent.coherentAdicSystemsEquivFGModuleCat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean#L542).

> **Stacks 087W.** Coherent inverse systems on an affine Noetherian scheme are equivalent to
> finite modules over the completion of its ring of global sections.

```lean
public noncomputable def coherentAdicSystemsEquivFGModuleCat
    (X : Scheme.{u}) [IsAffine X] [IsNoetherianRing Γ(X, ⊤)]
    (I : Ideal Γ(X, ⊤)) :
    CoherentAdicSystems
      (Scheme.IdealSheafData.ofIdealTop I) ≌
        FGModuleCat.{u} (AdicCompletion I Γ(X, ⊤))
```

**`Stacks.Coherent.globalSectionsComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean#L565). The attribute's comment: “inverse-limit object”.

> **Stacks 087W.** The canonical comparison with the inverse limit of global sections.

```lean
public noncomputable def globalSectionsComparison
    (X : Scheme.{u}) [IsAffine X] [IsNoetherianRing Γ(X, ⊤)]
    (I : Ideal Γ(X, ⊤))
    (F : CoherentAdicSystems (Scheme.IdealSheafData.ofIdealTop I)) :
    completedModuleAsBase X I F ≅ limit (globalSectionsSystem F)
```

**`Stacks.Coherent.globalSectionsComparison_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean#L582). The attribute's comment: “naturality”.

> **Stacks 087W.** The comparison is natural in morphisms of coherent adic systems.

```lean
public theorem globalSectionsComparison_naturality
    (X : Scheme.{u}) [IsAffine X] [IsNoetherianRing Γ(X, ⊤)]
    (I : Ideal Γ(X, ⊤))
    {F G : CoherentAdicSystems (Scheme.IdealSheafData.ofIdealTop I)}
    (f : F ⟶ G) :
    (ModuleCat.restrictScalars (algebraMap Γ(X, ⊤)
      (AdicCompletion I Γ(X, ⊤)))).map
        ((coherentAdicSystemsEquivFGModuleCat X I).functor.map f).hom ≫
      (globalSectionsComparison X I G).hom =
    (globalSectionsComparison X I F).hom ≫
      limMap (F := globalSectionsSystem F) (G := globalSectionsSystem G)
        (Functor.whiskerRight f.hom
        (SheafOfModules.evaluation X.ringCatSheaf (op ⊤)))
```

**`Stacks.Coherent.globalSectionsComparison_projection_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean#L617). The attribute's comment: “surjective projections”.

> **Stacks 087W.** Projection from the corresponding completed module onto any term is
> surjective.

```lean
public theorem globalSectionsComparison_projection_surjective
    (X : Scheme.{u}) [IsAffine X] [IsNoetherianRing Γ(X, ⊤)]
    (I : Ideal Γ(X, ⊤))
    (F : CoherentAdicSystems (Scheme.IdealSheafData.ofIdealTop I))
    (n : ℕ) :
    Function.Surjective
      (((globalSectionsComparison X I F).hom ≫
        limit.π (globalSectionsSystem F) (op n)).hom)
```

**`Stacks.Coherent.globalSectionsComparison_projection_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Equivalence.lean#L632). The attribute's comment: “canonical quotient”.

> **Stacks 087W.** The kernel of the projection is exactly the `(n+1)`-st ideal power multiple,
> so the induced map from the quotient is an isomorphism.

```lean
public theorem globalSectionsComparison_projection_ker
    (X : Scheme.{u}) [IsAffine X] [IsNoetherianRing Γ(X, ⊤)]
    (I : Ideal Γ(X, ⊤))
    (F : CoherentAdicSystems (Scheme.IdealSheafData.ofIdealTop I))
    (n : ℕ) :
    LinearMap.ker
      (((globalSectionsComparison X I F).hom ≫
        limit.π (globalSectionsSystem F) (op n)).hom) =
      I ^ (n + 1) • (⊤ : Submodule Γ(X, ⊤) (completedModuleAsBase X I F))
```

## Tag 087X, a lemma

[Tag 087X](https://stacks.math.columbia.edu/tag/087X) in the Stacks Project.

**`Stacks.Coherent.abelian_coherentAdicSystems`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Abelian.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Abelian.lean#L200). The attribute's comment: “the category is abelian”.

> **Part (1) of Tag 087X: the category of coherent adic systems on a Noetherian scheme is
> abelian.** It is preadditive, has kernels, cokernels and finite products, and its coimage-image
> comparisons are invertible.

```lean
public instance abelian_coherentAdicSystems {X : Scheme.{u}} [IsNoetherian X]
    (I : X.IdealSheafData) : Abelian (CoherentAdicSystems I)
```

**`Stacks.Coherent.restrictFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Abelian.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Abelian.lean#L208). The attribute's comment: “restriction to an open is exact”.

> **Part (2) of Tag 087X: restriction to an open subscheme is exact on coherent adic systems.**
> Restriction preserves finite limits, being compatible with the kernel construction, and finite
> colimits, being a left adjoint computed termwise.

```lean
public theorem restrictFunctor_exact {X : Scheme.{u}} [IsNoetherian X] (I : X.IdealSheafData)
    {Y : Scheme.{u}} (f : Y ⟶ X) [IsOpenImmersion f] :
    PreservesFiniteLimits (restrictFunctor I f) ∧
      PreservesFiniteColimits (restrictFunctor I f)
```

**`Stacks.Coherent.exact_iff_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/ExactnessLocal.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/ExactnessLocal.lean#L133). The attribute's comment: “exactness may be checked on an open covering”.

> **Part (3) of Tag 087X: exactness in `Coh(X, ℐ)` may be checked on an open covering of `X`.**
> A pair of morphisms `α : F ⟶ G` and `β : G ⟶ H` of coherent adic systems on a Noetherian scheme
> is an exact sequence if and only if, for every member `U j` of an open covering of `X`, the
> restrictions of `α` and `β` to `U j` form an exact sequence.
>
> Both the condition that the composite vanish and the exactness of the resulting short complex are
> local.

```lean
public theorem exact_iff_restrict {X : Scheme.{u}} [IsNoetherian X] (I : X.IdealSheafData)
    {F G H : CoherentAdicSystems I} (α : F ⟶ G) (β : G ⟶ H)
    {J : Type v} (U : J → X.Opens) (hU : iSup U = ⊤) :
    (∃ h : α ≫ β = 0, (ShortComplex.mk α β h).Exact) ↔
      ∀ j : J, ∃ h : (restrictFunctor I (U j).ι).map α ≫ (restrictFunctor I (U j).ι).map β = 0,
        (ShortComplex.mk ((restrictFunctor I (U j).ι).map α)
          ((restrictFunctor I (U j).ι).map β) h).Exact
```

## Tag 087Y, a lemma

[Tag 087Y](https://stacks.math.columbia.edu/tag/087Y) in the Stacks Project.

**`Stacks.Coherent.epi_iff_epi_app_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Epi.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Epi.lean#L65).

> **Stacks 087Y.** A morphism of coherent adic systems is surjective exactly when its
> component at the lowest level is surjective.

```lean
public theorem epi_iff_epi_app_zero {F G : CoherentAdicSystems I} (f : F ⟶ G) :
    Epi f ↔ Epi (f.hom.app (op 0))
```

## Tag 0880, an equation

[Tag 0880](https://stacks.math.columbia.edu/tag/0880) in the Stacks Project.

**`Stacks.Algebraization.completionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean#L475). The attribute's comment: “the functor”.

> Completion of a coherent sheaf along a quasi-coherent ideal, as a coherent adic inverse
> system.

```lean
public noncomputable def completionFunctor (X : Scheme.{u})
    [AlgebraicGeometry.IsLocallyNoetherian X] (I : X.IdealSheafData) :
    AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf ⥤
      Stacks.Coherent.CoherentAdicSystems I
```

**`Stacks.Algebraization.completionFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean#L488). The attribute's comment: “object formula”.

> The `n`-th term of the completion is the quotient by `I ^ (n+1)`.

```lean
public theorem completionFunctor_obj (X : Scheme.{u})
    [AlgebraicGeometry.IsLocallyNoetherian X] (I : X.IdealSheafData)
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (n : ℕ) :
    ((completionFunctor X I).obj F).obj.obj (op n) = idealPowerQuotient I (n + 1) F.obj
```

**`Stacks.Algebraization.completionProjection_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean#L504). The attribute's comment: “transition maps”.

> The projections are compatible with the transition maps of the inverse system.

```lean
public theorem completionProjection_transition (X : Scheme.{u})
    [AlgebraicGeometry.IsLocallyNoetherian X] (I : X.IdealSheafData)
    (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (n : ℕ) :
    completionProjection X I F (n + 1) ≫
        ((completionFunctor X I).obj F).obj.map (homOfLE (Nat.le_succ n)).op =
      completionProjection X I F n
```

**`Stacks.Algebraization.completionFunctor_map_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Basic.lean#L515). The attribute's comment: “morphism maps”.

> Completion maps are exactly the maps induced on the successive quotients.

```lean
public theorem completionFunctor_map_quotient (X : Scheme.{u})
    [AlgebraicGeometry.IsLocallyNoetherian X] (I : X.IdealSheafData)
    {F G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf} (f : F ⟶ G) (n : ℕ) :
    completionProjection X I F n ≫ ((completionFunctor X I).map f).hom.app (op n) =
      f.hom ≫ completionProjection X I G n
```

## Tag 0881, a lemma

[Tag 0881](https://stacks.math.columbia.edu/tag/0881) in the Stacks Project.

**`Stacks.Algebraization.completionFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Exactness.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/Exactness.lean#L389).

> **Stacks 0881: the completion functor `Coh(𝒪_X) ⥤ Coh(X, I)` of Stacks 0880 is exact.**
>
> It is right exact because the completion of a coherent module is a quotient construction, and it
> preserves monomorphisms by Artin–Rees; a right exact functor between abelian categories which
> preserves monomorphisms is exact.

```lean
public theorem completionFunctor_exact :
    exactFunctor _ _ (completionFunctor X I)
```

## Tag 0882, a lemma

[Tag 0882](https://stacks.math.columbia.edu/tag/0882) in the Stacks Project.

**`Stacks.Algebraization.completionInternalHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/InternalHomCompletion.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/InternalHomCompletion.lean#L228). References: SGA 2 X (2.2), “partial”.

> **Stacks 0882.** Let `X` be a locally Noetherian scheme, `I` a quasi-coherent sheaf of ideals
> on `X` and `G`, `F` coherent `𝒪_X`-modules; put `H = SheafHom(G, F)`. Then
>
> `lim_n H⁰(X, H / Iⁿ H) = Mor_{Coh(X, I)}(G^∧, F^∧)`.
>
> The left side is the inverse limit of the global sections of the completion of the internal hom;
> the right side the morphisms of coherent adic systems between the completions of `G` and `F`. The
> identification is additive.
>
> Four steps: global sections commute with the inverse limit; the comparison
> `lim H / Iⁿ H ⟶ SheafHom(G, lim F / Iⁿ F)` is an isomorphism
> (`isIso_completedSheafHomComparison`); the global sections of an internal hom are the morphisms
> (`internalHomSectionsTopEquiv`); and a morphism `G ⟶ lim F / Iⁿ F` is a morphism of coherent adic
> systems `G^∧ ⟶ F^∧` (`completionHomLimitEquiv`).
>
> Stacks states this for a Noetherian scheme; it holds, as here, on any locally Noetherian one.

```lean
public noncomputable def completionInternalHomEquiv (X : Scheme.{u}) [IsLocallyNoetherian X]
    (I : X.IdealSheafData)
    (G F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) :
    limit (C := ModuleCat.{u} Γ(X, ⊤)) (Stacks.Coherent.globalSectionsSystem
      ((completionFunctor X I).obj (internalHomCoherent X G F))) ≃+
      ((completionFunctor X I).obj G ⟶ (completionFunctor X I).obj F)
```

## Tag 0889, a lemma

[Tag 0889](https://stacks.math.columbia.edu/tag/0889) in the Stacks Project.

**`Stacks.Algebraization.exists_unique_algebraization_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/Algebraize.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/Algebraize.lean#L863). The attribute's comment: “part (1): algebraization of a map into a completion”.

> **Stacks 0889 (1) on a Noetherian scheme.** Let `X` be a Noetherian scheme, `ℐ` a
> quasi-coherent ideal sheaf, `G` a coherent `𝒪_X`-module and `(F_n)` a coherent `ℐ`-adic system. A
> morphism `α : (F_n) ⟶ G^∧` whose levelwise kernels and cokernels are annihilated by a power of
> `ℐ` admits a triple `(F, a, β)`, unique up to a unique isomorphism, with `F` a coherent
> `𝒪_X`-module, `a : F ⟶ G` a morphism whose kernel and cokernel are annihilated by a power of
> `ℐ`, `β : (F_n) ≅ F^∧` an isomorphism, and `α = a^∧ ∘ β`. Uniqueness: for a second such triple
> `(F', a', β')` there is exactly one isomorphism `d : F ≅ F'` of triples, that is, with
> `a' ∘ d = a` and `d^∧ ∘ β = β'`.
>
> The existence is `Stacks.Algebraization.exists_unique_algebraization` with its one premise
> supplied by `Stacks.Algebraization.isPowerAnnihilated_of_restrict`: on a Noetherian scheme the
> affine-local annihilation of a sheaf of modules by powers of `ℐ|_U` is annihilation by a single
> power of `ℐ`, because quasi-compactness extracts a finite affine covering and annihilation by a
> fixed power is local on the base. The uniqueness there is read on `lim (F_n)`, and
> `completionMap_comp_eq_iff_limMap` turns it into the compatibility `d^∧ ∘ β = β'`. The conditions
> are exactly those of the source.

```lean
public theorem exists_unique_algebraization_of_isNoetherian {X : Scheme.{u}} [IsNoetherian X]
    (I : X.IdealSheafData)
    (G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (Fsys : Stacks.Coherent.CoherentAdicSystems I)
    (α : Fsys.obj ⟶ ((completionFunctor X I).obj G).obj)
    (hα : IsKernelCokernelAnnihilatedByPower I α) :
    ∃ (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (a : F ⟶ G)
      (β : Fsys.obj ≅ ((completionFunctor X I).obj F).obj),
      (α = β.hom ≫ ((completionFunctor X I).map a).hom ∧
          IsPowerAnnihilated I (kernel (C := X.Modules) a.hom) ∧
            IsPowerAnnihilated I (cokernel (C := X.Modules) a.hom)) ∧
        ∀ (F' : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (a' : F' ⟶ G)
            (β' : Fsys.obj ≅ ((completionFunctor X I).obj F').obj),
          α = β'.hom ≫ ((completionFunctor X I).map a').hom →
            IsPowerAnnihilated I (kernel (C := X.Modules) a'.hom) →
              IsPowerAnnihilated I (cokernel (C := X.Modules) a'.hom) →
                ∃! d : F ≅ F',
                  d.hom ≫ a' = a ∧
                    β.hom ≫ ((completionFunctor X I).map d.hom).hom = β'.hom
```

**`Stacks.Algebraization.exists_unique_algebraization_dual_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizeDualTheorem.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizeDualTheorem.lean#L395). The attribute's comment: “part (2): algebraization of a map out of a completion”.

> **Stacks 0889 (2).** Let `X` be a Noetherian scheme, `ℐ` a quasi-coherent ideal sheaf, `G` a
> coherent `𝒪_X`-module and `(F_n)` a coherent `ℐ`-adic system. A morphism `α : G^∧ ⟶ (F_n)` whose
> levelwise kernels and cokernels are annihilated by a power of `ℐ` admits a triple `(F, a, β)`,
> unique up to a unique isomorphism, with `F` a coherent `𝒪_X`-module, `a : G ⟶ F` a morphism whose
> kernel and cokernel are annihilated by a power of `ℐ`, `β : F^∧ ≅ (F_n)` an isomorphism, and
> `α = β ∘ a^∧`.
>
> The existence is `Stacks.Algebraization.exists_algebraization_dual`, whose affine-local
> annihilation of the kernel and the cokernel of `a` becomes annihilation by a single power of `ℐ`
> by `Stacks.Algebraization.isPowerAnnihilated_of_restrict`, using that `X` is quasi-compact. The
> uniqueness is `Stacks.Algebraization.unique_algebraization_dual`.

```lean
public theorem exists_unique_algebraization_dual_of_isNoetherian {X : Scheme.{u}}
    [IsNoetherian X] (I : X.IdealSheafData)
    (G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (Fsys : Stacks.Coherent.CoherentAdicSystems I)
    (α : ((completionFunctor X I).obj G).obj ⟶ Fsys.obj)
    (hα : IsKernelCokernelAnnihilatedByPower I α) :
    ∃ (F : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (a : G ⟶ F)
      (β : ((completionFunctor X I).obj F).obj ≅ Fsys.obj),
      (α = ((completionFunctor X I).map a).hom ≫ β.hom ∧
          IsPowerAnnihilated I (kernel (C := X.Modules) a.hom) ∧
            IsPowerAnnihilated I (cokernel (C := X.Modules) a.hom)) ∧
        ∀ (F' : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf) (a' : G ⟶ F')
            (β' : ((completionFunctor X I).obj F').obj ≅ Fsys.obj),
          α = ((completionFunctor X I).map a').hom ≫ β'.hom →
            IsPowerAnnihilated I (kernel (C := X.Modules) a'.hom) →
              IsPowerAnnihilated I (cokernel (C := X.Modules) a'.hom) →
                ∃! d : F ≅ F',
                  a ≫ d.hom = a' ∧
                    ((completionFunctor X I).map d.hom).hom ≫ β'.hom = β.hom
```

## Tag 0EHP, a lemma

[Tag 0EHP](https://stacks.math.columbia.edu/tag/0EHP) in the Stacks Project.

**`Stacks.Algebraization.essImage_and_bijective_of_isPowerAnnihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/TorsionExtBijective.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionFunctor/TorsionExtBijective.lean#L532).

> **[Stacks, Tag 0EHP].** Let `X` be a Noetherian scheme and `ℐ ⊂ 𝒪_X` a quasi-coherent sheaf
> of ideals.
>
> * Any object of `Coh(X, ℐ)` annihilated by a power of `ℐ` is in the essential image of the
>   completion functor of Stacks 0880.
> * If `ℱ`, `𝒢` are coherent `𝒪_X`-modules and a power of `ℐ` annihilates `ℱ` or `𝒢`, then both
>
>   `Hom_X(ℱ, 𝒢) ⟶ Hom_{Coh(X, ℐ)}(ℱ^∧, 𝒢^∧)` and
>   `Ext_X(ℱ, 𝒢) ⟶ Ext_{Coh(X, ℐ)}(ℱ^∧, 𝒢^∧)`
>
>   are isomorphisms.
>
> Both comparison maps are the ones induced by the completion functor, and both are homomorphisms
> of abelian groups for formal reasons — the functor is additive — so their bijectivity is the
> whole of the source's assertion that they are isomorphisms.

```lean
public theorem essImage_and_bijective_of_isPowerAnnihilated (X : Scheme.{u}) [IsNoetherian X]
    (I : X.IdealSheafData) :
    (∀ S : Stacks.Coherent.CoherentAdicSystems I, IsSystemPowerAnnihilated I S.obj →
        (completionFunctor X I).essImage S) ∧
      ∀ F G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
        IsPowerAnnihilated I F.obj ∨ IsPowerAnnihilated I G.obj →
          Function.Bijective (fun f : F ⟶ G => (completionFunctor X I).map f) ∧
            Function.Bijective ((completionFunctor X I).mapExtAddHom F G 1)
```

## Tag 087Z, a lemma

[Tag 087Z](https://stacks.math.columbia.edu/tag/087Z) in the Stacks Project.

**`Stacks.Coherent.finiteTypeAssociatedGradedData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/AssociatedGraded/GradedModuleFiniteType.lean, line 670](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/AssociatedGraded/GradedModuleFiniteType.lean#L670).

> **Stacks Project, Tag 087Z.** For a Noetherian scheme `X` and a quasi-coherent sheaf of
> ideals `ℐ`, the transition kernels of an object of `Coh(X, ℐ)` form a finite type, graded,
> quasi-coherent module over the associated graded algebra `⨁ ℐ ⁿ / ℐ ⁿ⁺¹`.

```lean
public theorem finiteTypeAssociatedGradedData {X : Scheme.{u}} [IsNoetherian X]
    (I : X.IdealSheafData) (F : CoherentAdicSystems I) :
    Nonempty (AssociatedGradedData I F)
```

## Tag 0887, a lemma

[Tag 0887](https://stacks.math.columbia.edu/tag/0887) in the Stacks Project.

**`Stacks.Coherent.coherentAdicPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean#L200). The attribute's comment: “the functor f^*”.

> **Stacks 0887: the functor `f^* : Coh(Y, 𝒥) ⟶ Coh(X, ℐ)`.** For a morphism `f : X ⟶ Y` of
> Noetherian schemes and a quasi-coherent sheaf of ideals `𝒥` on `Y`, termwise pullback is a functor
> from the coherent adic systems along `𝒥` to those along `ℐ = f^{-1}𝒥 𝒪_X`.
>
> It is built as a lift of termwise pullback, so its action on objects and morphisms is the
> canonical one; see `Stacks.Coherent.coherentAdicPullback_obj_obj`.

```lean
public def coherentAdicPullback {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : X ⟶ Y) (J : Y.IdealSheafData) :
    CoherentAdicSystems J ⥤ CoherentAdicSystems (J.comap f)
```

**`Stacks.Coherent.coherentAdicPullback_obj_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean#L210). The attribute's comment: “the functor sends (G n) to (f^* G n)”.

> **The functor of Stacks 0887 sends the system `(G_n)` to the system `(f^*G_n)`.**

```lean
public theorem coherentAdicPullback_obj_obj {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : X ⟶ Y) (J : Y.IdealSheafData) (G : CoherentAdicSystems J) (n : ℕᵒᵖ) :
    ((coherentAdicPullback f J).obj G).obj.obj n =
      (Scheme.Modules.pullback f).obj (G.obj.obj n)
```

**`Stacks.Coherent.coherentAdicPullback_rightExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean#L233). The attribute's comment: “right exactness”.

> **Stacks 0887: the pullback functor on coherent adic systems is right exact.**
>
> Termwise pullback of inverse systems preserves all colimits, being a left adjoint; the inclusion
> of `Coh(Y, 𝒥)` preserves finite colimits, cokernels there being levelwise; so the composite of
> `f^*` with the inclusion of `Coh(X, ℐ)` preserves finite colimits, and that inclusion reflects
> them.

```lean
public theorem coherentAdicPullback_rightExact {X Y : Scheme.{u}} [IsNoetherian X]
    [IsNoetherian Y] (f : X ⟶ Y) (J : Y.IdealSheafData) :
    rightExactFunctor _ _ (coherentAdicPullback f J)
```

**`Stacks.Coherent.coherentAdicPullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/Pullback.lean#L351). The attribute's comment: “exactness when f is flat”.

> **Stacks 0887: along a flat morphism the pullback functor on coherent adic systems is
> exact.**

```lean
public theorem coherentAdicPullback_exact {X Y : Scheme.{u}} [IsNoetherian X] [IsNoetherian Y]
    (f : X ⟶ Y) (J : Y.IdealSheafData) [Flat f] :
    exactFunctor _ _ (coherentAdicPullback f J)
```

## Tag 0EHQ, a lemma

[Tag 0EHQ](https://stacks.math.columbia.edu/tag/0EHQ) in the Stacks Project.

**`Stacks.Coherent.coherentAdicPullback_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/PullbackEquivalence.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/PullbackEquivalence.lean#L737).

> **[Stacks, Tag 0EHQ].** Let `f : X ⟶ Y` be a flat morphism of Noetherian schemes, let
> `𝒥 ⊆ 𝒪_Y` be a quasi-coherent sheaf of ideals cutting out `Z ⊆ Y`, and let
> `ℐ = 𝒥.comap f ⊆ 𝒪_X` cut out the scheme-theoretic inverse image `Z' = f^{-1}Z`. If the induced
> morphism `Z' ⟶ Z` is an isomorphism, then the pullback functor
>
> `f^* : Coh(Y, 𝒥) ⟶ Coh(X, ℐ)`
>
> of [Stacks, Tag 0887] is an equivalence.
>
> The functor is left adjoint to the termwise direct image `coherentAdicPushforward`, which is an
> equivalence, and a left adjoint of an equivalence is an equivalence.

```lean
public theorem coherentAdicPullback_isEquivalence {X Y : Scheme.{u}} [IsNoetherian X]
    [IsNoetherian Y] (f : X ⟶ Y) [Flat f] (J : Y.IdealSheafData)
    [IsIso ((J.comapIso f).hom ≫ pullback.snd f J.subschemeι)] :
    (coherentAdicPullback f J).IsEquivalence
```

## Tag 0EHR, a lemma

[Tag 0EHR](https://stacks.math.columbia.edu/tag/0EHR) in the Stacks Project.

**`Stacks.Coherent.coherentAdicSystemsEquivOfSupportEq`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/IdealChange.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/IdealChange.lean#L616).

> **[Stacks, Tag 0EHR].** Let `X` be a Noetherian scheme and let `ℐ, 𝒥 ⊆ 𝒪_X` be quasi-coherent
> sheaves of ideals. If `V(ℐ) = V(𝒥)` as closed subsets of `X`, then the categories `Coh(X, ℐ)` and
> `Coh(X, 𝒥)` of coherent adic inverse systems are equivalent.
>
> Equal supports give positive exponents with `ℐ ᵃ ⊆ 𝒥` and `𝒥 ᵇ ⊆ ℐ`, and the two transfer functors
> they define are mutually quasi-inverse.

```lean
public def coherentAdicSystemsEquivOfSupportEq (X : Scheme.{u}) [IsNoetherian X]
    (I J : X.IdealSheafData) (h : I.support = J.support) :
    CoherentAdicSystems I ≌ CoherentAdicSystems J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.23, Tag 0EHN](https://stacks.math.columbia.edu/tag/0EHN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
