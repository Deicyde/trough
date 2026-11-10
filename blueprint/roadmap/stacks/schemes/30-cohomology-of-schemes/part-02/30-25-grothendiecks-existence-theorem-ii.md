---
declaration: section
origin: cited
lean: Ideal.existsUnique_canonicalMap_of_smul_eq_bot, Ideal.pow_le_annihilator_ker_mapQ_of_exact, Ideal.pow_le_annihilator_coker_mapQ_of_exact, Stacks.Algebraization.idealPowerMultiple_kernel_cokernel_idealPowerQuotientMap, Stacks.Algebraization.isKernelCokernelAnnihilatedByPower_iff_affine, Stacks.Algebraization.isKernelCokernelAnnihilatedByPower_tfae, Stacks.Algebraization.IsKernelCokernelAnnihilatedByPower, Stacks.Coherent.isCoherentAdicSystem_liftedQuotientTower
statement: formalized
proof: formalized
---

# 30.25 Grothendieck's existence theorem, II

Section 30.25 of the Stacks Project, [Tag 0886](https://stacks.math.columbia.edu/tag/0886). 4 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0888, a remark

[Tag 0888](https://stacks.math.columbia.edu/tag/0888) in the Stacks Project.

**`Ideal.existsUnique_canonicalMap_of_smul_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean#L114). The attribute's comment: “canonical_fg_map”.

> **Stacks Project, Tag 0888.** In an exact sequence whose two end modules are annihilated by
> an ideal `I`, elements `f, g ∈ I` determine a unique linear map `N → M`. Its value at `y` is
> `g • x` for any lift `x` of `f • y`, and its composite with `M → N` is multiplication by
> `f * g`.

```lean
theorem existsUnique_canonicalMap_of_smul_eq_bot
    (i : T →ₗ[A] M) (a : M →ₗ[A] N) (q : N →ₗ[A] Q)
    (hia : Function.Exact i a) (haq : Function.Exact a q)
    (I : Ideal A)
    (hT : I • (⊤ : Submodule A T) = ⊥)
    (hQ : I • (⊤ : Submodule A Q) = ⊥)
    {f g : A} (hf : f ∈ I) (hg : g ∈ I) :
    ∃! b : N →ₗ[A] M,
      (∀ (y : N) (x : M), a x = f • y → b y = g • x) ∧
        b.comp a = LinearMap.lsmul A M (f * g)
```

**`Ideal.pow_le_annihilator_ker_mapQ_of_exact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean#L154). The attribute's comment: “annihilation_mod_ideal”.

> **Stacks Project, Tag 0888.** In an exact five-term sequence whose end modules are
> annihilated by `K ^ t`, the power `K ^ (2 * t)` annihilates the kernel of the map induced after
> reduction modulo any ideal `J`.

```lean
lemma pow_le_annihilator_ker_mapQ_of_exact
    (i : T →ₗ[A] M) (a : M →ₗ[A] N) (q : N →ₗ[A] Q)
    (_hi : Function.Injective i) (hia : Function.Exact i a)
    (haq : Function.Exact a q) (_hq : Function.Surjective q)
    (K : Ideal A) (t : ℕ) (_ht : 0 < t)
    (hT : K ^ t ≤ Module.annihilator A T)
    (hQ : K ^ t ≤ Module.annihilator A Q) (J : Ideal A) :
    K ^ (2 * t) ≤ Module.annihilator A
      ↑(LinearMap.ker (Submodule.mapQ (J • (⊤ : Submodule A M))
        (J • (⊤ : Submodule A N)) a
        (Submodule.smul_top_le_comap_smul_top J a)))
```

**`Ideal.pow_le_annihilator_coker_mapQ_of_exact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/Annihilator.lean#L196). The attribute's comment: “annihilation_mod_ideal”.

> **Stacks Project, Tag 0888.** In an exact five-term sequence whose end modules are
> annihilated by `K ^ t`, the power `K ^ (2 * t)` annihilates the cokernel of the map induced
> after reduction modulo any ideal `J`.

```lean
lemma pow_le_annihilator_coker_mapQ_of_exact
    (i : T →ₗ[A] M) (a : M →ₗ[A] N) (q : N →ₗ[A] Q)
    (_hi : Function.Injective i) (_hia : Function.Exact i a)
    (haq : Function.Exact a q) (_hq : Function.Surjective q)
    (K : Ideal A) (t : ℕ) (_ht : 0 < t)
    (_hT : K ^ t ≤ Module.annihilator A T)
    (hQ : K ^ t ≤ Module.annihilator A Q) (J : Ideal A) :
    K ^ (2 * t) ≤ Module.annihilator A
      (_ ⧸ LinearMap.range
        (Submodule.mapQ (J • (⊤ : Submodule A M)) (J • (⊤ : Submodule A N)) a
          (Submodule.smul_top_le_comap_smul_top J a)))
```

**`Stacks.Algebraization.idealPowerMultiple_kernel_cokernel_idealPowerQuotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AnnihilatorSheaf.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/Coherent/AnnihilatorSheaf.lean#L255). The attribute's comment: “annihilation_mod_ideal, over sheaves of modules”.

> Let `a : M ⟶ N` be a morphism of quasi-coherent `𝒪_X`-modules whose kernel and cokernel are
> annihilated by `𝒦 ᵗ`, and let `ℐ` be any quasi-coherent ideal sheaf. Then `𝒦 ²ᵗ` annihilates both
> the kernel and the cokernel of the induced map `M / ℐ ⁿ M ⟶ N / ℐ ⁿ N`.
>
> This is the sheaf-of-modules form of `Ideal.pow_le_annihilator_ker_mapQ_of_exact` and
> `Ideal.pow_le_annihilator_coker_mapQ_of_exact`.

```lean
public theorem idealPowerMultiple_kernel_cokernel_idealPowerQuotientMap
    (I K : X.IdealSheafData) {M N : X.Modules} [M.IsQuasicoherent] [N.IsQuasicoherent]
    (a : M ⟶ N) {t : ℕ}
    (hk : idealPowerMultiple K t (kernel (C := X.Modules) a) = ⊥)
    (hc : idealPowerMultiple K t (cokernel (C := X.Modules) a) = ⊥) (n : ℕ) :
    idealPowerMultiple K (2 * t)
        (kernel (C := X.Modules) (idealPowerQuotientMap I I n n le_rfl a)) = ⊥ ∧
      idealPowerMultiple K (2 * t)
        (cokernel (C := X.Modules) (idealPowerQuotientMap I I n n le_rfl a)) = ⊥
```

**`Stacks.Algebraization.isKernelCokernelAnnihilatedByPower_iff_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AnnihilatedAffineCriterion.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AnnihilatedAffineCriterion.lean#L516). The attribute's comment: “equivalence of (1) and (2) on an affine scheme”.

> **Stacks Project, Tag 0888, conditions (1) and (2) on an affine scheme.** For a morphism `α`
> of `Coh(Y, 𝓘)` on an affine Noetherian scheme `Y` the following are equivalent: one positive power
> of `𝓚` annihilates every levelwise kernel `Ker(α_n)` and every levelwise cokernel `Coker(α_n)`;
> and one positive power of `K = 𝓚(⊤)` annihilates the kernel and the cokernel of the map
> `α_Y : M → N` of finite modules over the completion which Tag 087W attaches to `α`.
>
> Both ideal sheaves on an affine scheme are attached to ideals of `Γ(Y, ⊤)`, by
> `AlgebraicGeometry.Scheme.IdealSheafData.equivOfIsAffine`, so the statement may be reduced to that
> presentation.

```lean
public theorem isKernelCokernelAnnihilatedByPower_iff_affine {Y : Scheme.{u}} [IsAffine Y]
    [IsNoetherianRing Γ(Y, ⊤)] (ℐ 𝒦 : Y.IdealSheafData)
    {F G : Stacks.Coherent.CoherentAdicSystems ℐ} (f : F ⟶ G) :
    IsKernelCokernelAnnihilatedByPower 𝒦 f.hom ↔
      IsAffineKernelCokernelAnnihilated (𝒦.ideal ⟨⊤, isAffineOpen_top Y⟩) f
```

**`Stacks.Algebraization.isKernelCokernelAnnihilatedByPower_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AnnihilatedLocal.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/AnnihilatedLocal.lean#L202). The attribute's comment: “the equivalence of (1), (2) and (3)”.

> **Stacks Project, Tag 0888.** For a morphism `α` of `Coh(X, 𝓘)` on a Noetherian scheme `X` and
> a quasi-coherent sheaf of ideals `𝓚`, the following are equivalent:
>
> 1. one positive power of `𝓚` annihilates every levelwise kernel `Ker(α_n)` and every levelwise
>    cokernel `Coker(α_n)`;
> 2. for every affine open `U ⊆ X` one positive power of `𝓚(U)` annihilates `Ker(α_U)` and
>    `Coker(α_U)`, where `α_U` is the map of finite modules over the completion attached to `α|_U`
>    by Tag 087W;
> 3. the conclusion of (2) holds for the members of some finite affine open covering of `X`.
>
> A morphism satisfying these conditions is the source's *map whose kernel and cokernel are
> annihilated by a power of `𝓚`*.

```lean
public theorem isKernelCokernelAnnihilatedByPower_tfae {X : Scheme.{u}} [IsNoetherian X]
    (ℐ 𝒦 : X.IdealSheafData) {F G : Stacks.Coherent.CoherentAdicSystems ℐ} (α : F ⟶ G) :
    List.TFAE
      [IsKernelCokernelAnnihilatedByPower 𝒦 α.hom,
        ∀ U : X.affineOpens, IsAffineLocalKernelCokernelAnnihilated 𝒦 α U,
        ∃ (J : Type u) (_ : Finite J) (U : J → X.affineOpens),
          iSup (fun j => (U j).1) = ⊤ ∧
            ∀ j, IsAffineLocalKernelCokernelAnnihilated 𝒦 α (U j)]
```

**`Stacks.Algebraization.IsKernelCokernelAnnihilatedByPower`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/PowerAnnihilated.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/PowerAnnihilated.lean#L435). The attribute's comment: “the notion named by the remark”.

> **Tag 0888 (1).** A morphism `α` of inverse systems of sheaves of modules has *kernel and
> cokernel annihilated by a power of `K`* if there is one positive exponent `t` for which `K ^ t`
> annihilates both `Ker(α_k)` and `Coker(α_k)`, simultaneously for every index `k`.
>
> Kernel and cokernel are taken levelwise, in the abelian category `X.Modules`. This is the notion
> the source names at the end of the remark, once its three conditions have been shown
> equivalent.

```lean
public def IsKernelCokernelAnnihilatedByPower (K : X.IdealSheafData) {F G : ℕᵒᵖ ⥤ X.Modules}
    (α : F ⟶ G) : Prop
```

## Tag 088A, a lemma

[Tag 088A](https://stacks.math.columbia.edu/tag/088A) in the Stacks Project.

**`Stacks.Coherent.isCoherentAdicSystem_liftedQuotientTower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/LiftedQuotientAdicSystem.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CoherentAdicSystem/LiftedQuotientAdicSystem.lean#L286). The attribute's comment: “proof step 4, adic form: the tower of algebraizations lies in Coh(X, 𝒦)”.

> **Tag 088A: the tower of algebraizations is a coherent adic system along `𝒦`.** Let `X` be
> Noetherian, let `ℐ, 𝒦` be quasi-coherent ideal sheaves satisfying hypothesis (1) of
> [Stacks, Tag 088A] at every level, and let `(G_e)` be a tower of coherent `𝒪_X`-modules, the
> term `e` annihilated by `𝒦 ᵉ⁺¹`, whose termwise `ℐ`-completion is identified naturally with the
> tower of `𝒦 ᵉ⁺¹`-reductions of an object `(F_n)` of `Coh(X, ℐ)`. Then the underlying inverse
> system of `(G_e)` is an object of `Coh(X, 𝒦)`.
>
> Only the quotient clause needs proof. The transition `G_{e+1} ⟶ G_e` descends through the
> projection onto `G_{e+1} / 𝒦 ᵉ⁺¹ G_{e+1}`, and `Stacks.Coherent.completion_quotientDesc_eq`
> identifies the completion of that descent with the composite of
> `Stacks.Coherent.idealPowerQuotientAdicCompletionIso`, the given identification and
> `Stacks.Coherent.idealPowerQuotientAdicCollapseIso`, hence with an isomorphism. Both modules are
> annihilated by `𝒦 ᵉ⁺¹`, so completion reflects the isomorphism by
> `Stacks.Coherent.isIso_of_isIso_completion_map_of_power_annihilated`.

```lean
public theorem isCoherentAdicSystem_liftedQuotientTower [IsNoetherian X]
    (F : CoherentAdicSystems I) (h : IsCompletionEquivalenceOnPowerThickenings I K)
    (G : ℕᵒᵖ ⥤ AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (hG : ∀ e : ℕ, idealPowerMultiple K (e + 1) (G.obj (op e)).obj = ⊥)
    (c : G ⋙ completionFunctor X I ≅
      idealPowerQuotientAdicTower I K ⋙ (evaluation _ _).obj F) :
    IsCoherentAdicSystem K (G ⋙ ObjectProperty.ι _)
```

**`Stacks.Coherent.isCoherentAdicSystem_and_annihilated_idealPowerQuotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L225). The attribute's comment: “proof step 1: the 𝒦ᵉ-reduction is in Coh(X, ℐ), annihilated by 𝒦ᵉ”.

> **Tag 088A, the opening step of the proof.** For a locally Noetherian `X`, quasi-coherent
> ideal sheaves `ℐ, 𝒦`, an exponent `e` and a coherent adic system `(F_n)` along `ℐ`, the reduction
> `n ↦ F_n / 𝒦 ᵉ F_n` is again a coherent adic system along `ℐ`, and every one of its terms is
> annihilated by `𝒦 ᵉ`.
>
> This is the sense in which the source's `(F_n / 𝒦 ᵉ F_n)` is "a system of `Coh(X, ℐ)`" lying in
> the full subcategory of objects annihilated by `𝒦 ᵉ` — the subcategory which hypothesis (1) of
> Tag 088A, read through the closed-immersion equivalence of Tag 087T, identifies with
> `Coh(X_e, ℐ_e)`.
>
> The first clause is `Stacks.Coherent.isCoherentAdicSystem_idealPowerQuotientSystem`, whose
> substance is that the two orders of division agree. The second is
> `Stacks.Algebraization.idealPowerMultiple_idealPowerQuotient_eq_bot`, applied to each term; it
> needs the term to be quasi-coherent, which is the coherence clause of the given system.

```lean
public theorem isCoherentAdicSystem_and_annihilated_idealPowerQuotientSystem
    [IsLocallyNoetherian X] {I : X.IdealSheafData} (K : X.IdealSheafData) (e : ℕ)
    {F : ℕᵒᵖ ⥤ X.Modules} (hF : IsCoherentAdicSystem I F) :
    IsCoherentAdicSystem I (idealPowerQuotientSystem K e F) ∧
      ∀ n : ℕ, idealPowerMultiple K e ((idealPowerQuotientSystem K e F).obj (op n)) = ⊥
```

**`Stacks.Coherent.isKernelCokernelAnnihilatedByPower_whiskerRight_idealPowerQuotientFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L250). The attribute's comment: “proof step 2: the 𝒦ᵉ-reduction of a map with 𝒦ᵗ-annihilated kernel and cokernel has 𝒦²ᵗ-annihilated kernel and cokernel”.

> **Tag 088A, the second step of the proof.** Reducing a morphism of inverse systems of
> quasi-coherent modules modulo the fixed power `𝒦 ᵉ` doubles the exponent in hypothesis (2): if
> `𝒦 ᵗ` annihilates every levelwise kernel and cokernel of `α`, then `𝒦 ²ᵗ` annihilates every
> levelwise kernel and cokernel of
> `n ↦ (F_n / 𝒦 ᵉ F_n ⟶ G_n / 𝒦 ᵉ G_n)`.
>
> This is the source's first application of the remark of Tag 0888, which this library has over
> sheaves of modules as
> `Stacks.Algebraization.idealPowerMultiple_kernel_cokernel_idealPowerQuotientMap`; the source
> applies it a second time further on and reaches `𝒦 ⁴ᵗ`.
>
> Applied with `(G_n) = H ^∧` it is the statement that the comparison map of hypothesis (2) of
> Tag 088A survives the reduction of the opening step with its kernel–cokernel condition intact,
> which is what makes the reduced system an object to which Tag 0889 can be applied.

```lean
public theorem isKernelCokernelAnnihilatedByPower_whiskerRight_idealPowerQuotientFunctor
    (K : X.IdealSheafData) (e : ℕ) {F G : ℕᵒᵖ ⥤ X.Modules}
    (hF : ∀ n : ℕ, (F.obj (op n)).IsQuasicoherent)
    (hG : ∀ n : ℕ, (G.obj (op n)).IsQuasicoherent)
    {α : F ⟶ G} (hα : IsKernelCokernelAnnihilatedByPower K α) :
    IsKernelCokernelAnnihilatedByPower K
      (Functor.whiskerRight α (idealPowerQuotientFunctor K e))
```

**`Stacks.Coherent.exists_coherent_annihilated_completion_iso_idealPowerQuotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L315). The attribute's comment: “proof step 3: hypothesis (1) algebraizes the 𝒦ᵉ-reduction”.

> **Tag 088A, the third step of the proof.** Let `X` be a Noetherian scheme, let `ℐ, 𝒦` be
> quasi-coherent ideal sheaves, let `e` be an exponent and let `(F_n)` be an object of
> `Coh(X, ℐ)`. If hypothesis (1) of Tag 088A holds at the level `e` — that is, the completion
> functor of `X_e = V(𝒦 ᵉ⁺¹)` along `ℐ 𝒪_{X_e}` is an equivalence — then the `𝒦 ᵉ⁺¹`-reduction of
> `(F_n)` is the completion of a coherent `𝒪_X`-module annihilated by `𝒦 ᵉ⁺¹`.
>
> This is where hypothesis (1) enters. The reduction is carried to `X_e` by the pullback functor
> of Tag 0887, where the hypothesis algebraizes it to a coherent module `M`; the algebraization on
> `X` is `G = i_* M`, coherent by Tag 087T and annihilated by `𝒦 ᵉ⁺¹` because it is a direct image
> along the inclusion of `V(𝒦 ᵉ⁺¹)`. The comparison of completions is
> `Stacks.Coherent.completionPushforwardIso`, which identifies the completion of `i_* M` with the
> direct image of the completion of `M`, followed by
> `Stacks.Coherent.idealPowerQuotientSystemPushforwardIso`, which is Tag 0EL1 identifying
> `i_* i^* F_n` with `F_n / 𝒦 ᵉ⁺¹ F_n`.

```lean
public theorem exists_coherent_annihilated_completion_iso_idealPowerQuotientSystem
    [IsNoetherian X] (I K : X.IdealSheafData) (e : ℕ) (Fsys : CoherentAdicSystems I)
    (h : letI : IsLocallyNoetherian (K ^ (e + 1)).subscheme :=
        LocallyOfFiniteType.isLocallyNoetherian (K ^ (e + 1)).subschemeι
      (completionFunctor (K ^ (e + 1)).subscheme
        (I.comap (K ^ (e + 1)).subschemeι)).IsEquivalence) :
    ∃ G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
      idealPowerMultiple K (e + 1) G.obj = ⊥ ∧
      Nonempty (((completionFunctor X I).obj G).obj ≅
        idealPowerQuotientSystem K (e + 1) Fsys.obj)
```

**`Stacks.Coherent.exists_coherentAdicSystem_completion_iso_idealPowerQuotientSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L374). The attribute's comment: “proof step 4: the algebraizations G_e assemble into an object of Coh(X, 𝒦)”.

> **Tag 088A, the fourth step of the proof: the algebraizations assemble.** Let `X` be a
> Noetherian scheme, let `ℐ, 𝒦` be quasi-coherent ideal sheaves and let `(F_n)` be an object of
> `Coh(X, ℐ)`. If hypothesis (1) of Tag 088A holds at every level — the completion functor of
> `X_e = V(𝒦 ᵉ⁺¹)` along `ℐ 𝒪_{X_e}` is an equivalence — then the coherent modules `G_e`
> algebraizing the reductions `(F_n / 𝒦 ᵉ⁺¹ F_n)` form an object of `Coh(X, 𝒦)`.
>
> The modules themselves and their defining property are the third step,
> `Stacks.Coherent.exists_coherent_annihilated_completion_iso_idealPowerQuotientSystem`. What is
> added here is the identification `G_{e+1} / 𝒦 ᵉ⁺¹ G_{e+1} ≅ G_e`, read off the completions by
> `Stacks.Coherent.nonempty_idealPowerQuotient_iso_of_completion_iso`: completion along `ℐ`
> carries the left-hand side to
>
> `(F_n / 𝒦 ᵉ⁺² F_n) / 𝒦 ᵉ⁺¹ (…) ≅ F_n / 𝒦 ᵉ⁺¹ F_n`,
>
> by `Stacks.Coherent.completionIdealPowerQuotientSystemIso` and
> `Stacks.Coherent.idealPowerQuotientSystemCollapseIso`, which is the completion of the right-hand
> side; and completion along `ℐ`, although not known to be full on all of `Coh(𝒪_X)`, is fully
> faithful on the modules annihilated by `𝒦 ᵉ⁺¹`. The assembly of the identified modules into an
> object of `Coh(X, 𝒦)` is `Stacks.Coherent.exists_coherentAdicSystem_of_succQuotientIso`.
>
> The conclusion keeps the sequence `G` alongside the assembled system, because the rest of the
> source's argument speaks about the terms: the comparison with `H ^∧` is built level by level.

```lean
public theorem exists_coherentAdicSystem_completion_iso_idealPowerQuotientSystem
    [IsNoetherian X] (I K : X.IdealSheafData) (Fsys : CoherentAdicSystems I)
    (h : ∀ e : ℕ,
      letI : IsLocallyNoetherian (K ^ (e + 1)).subscheme :=
        LocallyOfFiniteType.isLocallyNoetherian (K ^ (e + 1)).subschemeι
      (completionFunctor (K ^ (e + 1)).subscheme
        (I.comap (K ^ (e + 1)).subschemeι)).IsEquivalence) :
    ∃ Gsys : CoherentAdicSystems K,
      ∃ G : ℕ → AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
        (∀ e : ℕ, Gsys.obj.obj (op e) = (G e).obj) ∧
        ∀ e : ℕ, idealPowerMultiple K (e + 1) (G e).obj = ⊥ ∧
          Nonempty (((completionFunctor X I).obj (G e)).obj ≅
            idealPowerQuotientSystem K (e + 1) Fsys.obj)
```

**`Stacks.Coherent.exists_lifted_quotient_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L423). The attribute's comment: “proof step 4, natural form: the algebraizations G_e form a tower whose ℐ-completion is the tower of 𝒦-power reductions of (F_n)”.

> **Tag 088A, the fourth step in the form the rest of the proof needs it.** Under hypothesis
> (1) of Tag 088A at every level, the algebraizations `G_e` of the reductions
> `(F_n / 𝒦 ᵉ⁺¹ F_n)` form a tower of coherent `𝒪_X`-modules, the term `e` annihilated by
> `𝒦 ᵉ⁺¹`, whose termwise `ℐ`-completion is identified with the tower of reductions **naturally
> in `e`**.
>
> `Stacks.Coherent.exists_coherentAdicSystem_completion_iso_idealPowerQuotientSystem` assembles
> the same modules into an object of `Coh(X, 𝒦)`, but its identification of completions is one
> isomorphism for each `e` separately. What is added here is the naturality: the transition
> `G_{e+1} ⟶ G_e` is obtained by lifting the transition of the tower of reductions through the
> full faithfulness of completion on the `𝒦 ᵉ⁺²`-annihilated modules
> (`Stacks.Coherent.exists_unique_completion_preimage_of_power_annihilated`), so the chosen
> isomorphisms commute with the transitions by construction.
>
> This is the datum that
> `Stacks.Coherent.exists_tower_map_to_completion` consumes to produce the comparison
> `(G_e) ⟶ H ^∧_𝒦` along `𝒦`.

```lean
public theorem exists_lifted_quotient_tower [IsNoetherian X] (I K : X.IdealSheafData)
    (Fsys : CoherentAdicSystems I)
    (h : ∀ e : ℕ,
      letI : IsLocallyNoetherian (K ^ (e + 1)).subscheme :=
        LocallyOfFiniteType.isLocallyNoetherian (K ^ (e + 1)).subschemeι
      (completionFunctor (K ^ (e + 1)).subscheme
        (I.comap (K ^ (e + 1)).subschemeι)).IsEquivalence) :
    ∃ G : ℕᵒᵖ ⥤ AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
      (∀ e : ℕ, idealPowerMultiple K (e + 1) (G.obj (op e)).obj = ⊥) ∧
      Nonempty (G ⋙ completionFunctor X I ≅
        idealPowerQuotientAdicTower I K ⋙ (evaluation _ _).obj Fsys)
```

**`Stacks.Coherent.exists_lifted_quotient_tower_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L490). The attribute's comment: “proof step 5: the comparison (G_e) ⟶ H^∧_𝒦 along 𝒦, with its levelwise kernels and cokernels annihilated by a power of 𝒦”.

> **Tag 088A, the fifth step: the comparison along `𝒦` exists and satisfies the hypothesis of
> Tag 0889.** Let `X` be Noetherian, let `ℐ, 𝒦` be quasi-coherent ideal sheaves satisfying
> hypothesis (1) of Tag 088A at every level, and let `α : (F_n) ⟶ H ^∧_ℐ` be a comparison whose
> levelwise kernels and cokernels are annihilated by a power of `𝒦` — hypothesis (2). Then the
> tower `(G_e)` of algebraizations of the reductions carries a morphism `γ : (G_e) ⟶ H ^∧_𝒦` whose
> kernels and cokernels are annihilated by a single positive power of `𝒦`.
>
> This is the whole of the source's passage from the comparison along `ℐ` to the comparison along
> `𝒦`: the tower is `Stacks.Coherent.exists_lifted_quotient_tower`, the comparison is
> `Stacks.Coherent.exists_tower_map_to_completion` — the reduction of `α` lifted through the
> fullness of completion on `𝒦`-power-annihilated towers — and the annihilation is
> `Stacks.Coherent.idealPowerMultiple_kernel_cokernel_tower_map_eq_bot`, the remark of Tag 0888
> followed by the reflection of annihilation along completion.
>
> What remains of the proof of Tag 088A after this is the final identification: Tag 0889 applied
> to `γ` algebraizes it, and its uniqueness clause, threaded through the two towers, identifies
> `(F_n)` with the completion of the resulting module.

```lean
public theorem exists_lifted_quotient_tower_comparison [IsNoetherian X]
    (I K : X.IdealSheafData) (Fsys : CoherentAdicSystems I)
    (h : ∀ e : ℕ,
      letI : IsLocallyNoetherian (K ^ (e + 1)).subscheme :=
        LocallyOfFiniteType.isLocallyNoetherian (K ^ (e + 1)).subschemeι
      (completionFunctor (K ^ (e + 1)).subscheme
        (I.comap (K ^ (e + 1)).subschemeι)).IsEquivalence)
    (H : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (α : Fsys ⟶ (completionFunctor X I).obj H)
    (hα : IsKernelCokernelAnnihilatedByPower K α.hom) :
    ∃ (G : ℕᵒᵖ ⥤ AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
      (γ : G ⟶ completionTermTower K H),
      (∀ e : ℕ, idealPowerMultiple K (e + 1) (G.obj (op e)).obj = ⊥) ∧
      Nonempty (G ⋙ completionFunctor X I ≅
        idealPowerQuotientAdicTower I K ⋙ (evaluation _ _).obj Fsys) ∧
      ∃ s : ℕ, 0 < s ∧ ∀ e : ℕ,
        idealPowerMultiple K s (kernel (C := X.Modules) (γ.app (op e)).hom) = ⊥ ∧
          idealPowerMultiple K s (cokernel (C := X.Modules) (γ.app (op e)).hom) = ⊥
```

**`Stacks.Coherent.essImage_completionFunctor_of_pow_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 534](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L534). The attribute's comment: “the case ℐᵐ ≤ 𝒦, hypothesis (1) unused; incomparable case not claimed”.

> **Tag 088A in the case `ℐ ᵐ ≤ 𝒦`.** Let `X` be a Noetherian scheme, let `ℐ, 𝒦` be
> quasi-coherent ideal sheaves on `X` with `ℐ ᵐ ≤ 𝒦` for some `m ≥ 1`, let `H` be a coherent
> `𝒪_X`-module and let `(F_n)` be an object of `Coh(X, ℐ)` admitting a map `α : (F_n) ⟶ H ^∧`
> whose levelwise kernels and cokernels are annihilated by a power of `𝒦`. Then `(F_n)` is in the
> essential image of the completion functor of Tag 0880.
>
> Hypothesis (1) of the source is not needed here, and no reduction modulo a power of `𝒦` occurs:
> the containment turns hypothesis (2) into the hypothesis of Tag 0889 part (1) by
> `Stacks.Coherent.isKernelCokernelAnnihilatedByPower_of_pow_le`, and
> `Stacks.Algebraization.exists_unique_algebraization_of_isNoetherian` then algebraizes `α`,
> delivering a coherent module `F` and an isomorphism `(F_n) ≅ F ^∧`. The isomorphism is of the
> underlying inverse systems and is promoted to the full subcategory `Coh(X, ℐ)` by
> `CategoryTheory.ObjectProperty.isoMk`.
>
> The source's own application has `ℐ` the pullback of an ideal of the base and `𝒦` the ideal of
> the complement of the dense open on which Chow's lemma is an isomorphism; no power of `ℐ` is
> contained in `𝒦` there, so this case does not cover it.

```lean
public theorem essImage_completionFunctor_of_pow_le [IsNoetherian X] {I K : X.IdealSheafData}
    {m : ℕ} (hm : 0 < m) (hIK : I ^ m ≤ K)
    (H : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (Fsys : CoherentAdicSystems I)
    (α : Fsys.obj ⟶ ((completionFunctor X I).obj H).obj)
    (hα : IsKernelCokernelAnnihilatedByPower K α) :
    (completionFunctor X I).essImage Fsys
```

**`Stacks.Coherent.essImage_completionFunctor_of_isKernelCokernelAnnihilatedByPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckExistenceII.lean#L580).

> **[Stacks, Tag 088A].** Let `X` be a Noetherian scheme and let `ℐ, 𝒦 ⊆ 𝒪_X` be quasi-coherent
> ideal sheaves. Let `(F_n)` be an object of `Coh(X, ℐ)` and suppose
>
> 1. for every `e`, completion along `ℐ 𝒪_{X_e}` is an equivalence on `Coh(𝒪_{X_e})`, where
>    `X_e = V(𝒦 ᵉ⁺¹)` is the closed subscheme cut out by the positive power `𝒦 ᵉ⁺¹`, and
> 2. there is a coherent `𝒪_X`-module `H` and a morphism `α : (F_n) ⟶ H ^∧_ℐ` whose levelwise
>    kernels and cokernels are annihilated by a power of `𝒦`.
>
> Then `(F_n)` is in the essential image of the completion functor of [Stacks, Tag 0880]: it is
> the `ℐ`-completion of a coherent `𝒪_X`-module.
>
> The proof is the source's, assembled from the steps carried above and in
> `FormalGeometry.CoherentAdicSystem`. Dividing `(F_n)` by the powers of `𝒦` and algebraizing the
> reductions with hypothesis (1) produces the tower `(G_e)` of
> `Stacks.Coherent.exists_lifted_quotient_tower`, which is an object of `Coh(X, 𝒦)` by
> `Stacks.Coherent.isCoherentAdicSystem_liftedQuotientTower`; the reduction of `α`, lifted through
> the fullness of completion on the annihilated towers, is the comparison
> `γ : (G_e) ⟶ H ^∧_𝒦` of `Stacks.Coherent.exists_tower_map_to_completion`, and its levelwise
> kernels and cokernels are annihilated by one power of `𝒦`
> (`Stacks.Coherent.idealPowerMultiple_kernel_cokernel_tower_map_eq_bot`). So [Stacks, Tag 0889]
> part (1) algebraizes `γ` to a coherent module `M` with `(G_e) ≅ M ^∧_𝒦`.
>
> What remains is to recognize `(F_n)` as `M ^∧_ℐ`. Reading the identification of the completed
> tower `(G_e) ^∧_ℐ` with the tower of reductions of `(F_n)` along the *other* index
> (`Stacks.Coherent.liftedQuotientRowTowerIso`) turns the algebraization of `γ` into an
> identification of the `𝒦`-completions of the terms of `(F_n)` and of `M ^∧_ℐ`, compatible with
> `α` and with `α ^∧` by `Stacks.Coherent.liftedQuotientRowIso_map_to_completion`; the uniqueness
> clause of Tag 0889 applied termwise then identifies the two systems, which is
> `Stacks.Coherent.nonempty_iso_of_completion_iso_over_power_annihilated`.
>
> `Stacks.Coherent.essImage_completionFunctor_of_pow_le` is the special case `ℐ ᵐ ≤ 𝒦`, where
> hypothesis (1) is not needed.

```lean
public theorem essImage_completionFunctor_of_isKernelCokernelAnnihilatedByPower [IsNoetherian X]
    (I K : X.IdealSheafData) (Fsys : CoherentAdicSystems I)
    (h : ∀ e : ℕ,
      letI : IsLocallyNoetherian (K ^ (e + 1)).subscheme :=
        LocallyOfFiniteType.isLocallyNoetherian (K ^ (e + 1)).subschemeι
      (completionFunctor (K ^ (e + 1)).subscheme
        (I.comap (K ^ (e + 1)).subschemeι)).IsEquivalence)
    (H : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (α : Fsys ⟶ (completionFunctor X I).obj H)
    (hα : IsKernelCokernelAnnihilatedByPower K α.hom) :
    (completionFunctor X I).essImage Fsys
```

## Tag 088B, a lemma

[Tag 088B](https://stacks.math.columbia.edu/tag/088B) in the Stacks Project.

**`Stacks.Coherent.exists_isKernelCokernelAnnihilatedByPower_comparisonMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ExceptionalComparisonMap.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/ExceptionalComparisonMap.lean#L75).

> **Stacks 088B.** Let `Y` be a Noetherian scheme and let `𝒥, 𝒦 ⊆ 𝒪_Y` be quasi-coherent
> sheaves of ideals. Let `f : X ⟶ Y` be a proper morphism which is an isomorphism over
> `V = Y ∖ V(𝒦)`, and set `ℐ = f^{-1}𝒥 𝒪_X`. Let `(𝒢_n)` be an object of `Coh(Y, 𝒥)`, let `𝓕` be
> a coherent `𝒪_X`-module, and let `β : (f^*𝒢_n) ⟶ 𝓕^` be an isomorphism in `Coh(X, ℐ)`. Then
> there exists a map
>
> `α : (𝒢_n) ⟶ (f_*𝓕)^`
>
> in `Coh(Y, 𝒥)` whose kernel and cokernel are annihilated by a power of `𝒦`.

```lean
public theorem exists_isKernelCokernelAnnihilatedByPower_comparisonMap
    {X Y : Scheme.{u}} [IsNoetherian Y] (J K : Y.IdealSheafData)
    (f : X ⟶ Y) [IsProper f] (hf : IsIso (f ∣_ K.support.compl))
    (G : CoherentAdicSystems J) (F : X.Modules) [F.IsCoherent] :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : IsNoetherian X :=
      { toIsLocallyNoetherian := LocallyOfFiniteType.isLocallyNoetherian f
        toCompactSpace := QuasiCompact.compactSpace_of_compactSpace f }
    letI : ((Scheme.Modules.pushforward f).obj F).IsCoherent :=
      AlgebraicGeometry.ProperCoherenceWitness.isCoherent_pushforward f F
    ∀ _β : (coherentAdicPullback f J).obj G ≅
        (completionFunctor X (J.comap f)).obj ⟨F, inferInstance⟩,
      ∃ α : G ⟶ (completionFunctor Y J).obj
          ⟨(Scheme.Modules.pushforward f).obj F, inferInstance⟩,
        IsKernelCokernelAnnihilatedByPower K α.hom
```

## Tag 088C, a proposition

[Tag 088C](https://stacks.math.columbia.edu/tag/088C) in the Stacks Project.

**`Stacks.Algebraization.isEquivalence_completionFunctor_of_devissage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/Devissage.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/Devissage.lean#L267). The attribute's comment: “for a proper f, with the theorem on formal functions in degree zero (087U) as the hypothesis hFF and the inductive step of the source's Noetherian induction over the quasi-coherent ideal sheaves of X as the hypothesis hDev -- that a coherent adic system killed by an ideal sheaf K is in the essential image of the completion functor as soon as every coherent adic system killed by a strictly larger ideal sheaf is. The induction itself, its ascending chain condition (for which the source cites 01Y8) and its conclusion at the zero ideal sheaf are proved unconditionally here; the source supplies hDev from Chow's lemma (0200), 087T, the projective case (0885), the coherence of a proper direct image (02O5) and 088A with 088B”.

> **Stacks 088C.** Let `A` be a Noetherian ring complete with respect to an ideal `I`, let
> `f : X ⟶ Spec A` be a proper morphism of schemes and set `𝓘 = I · 𝒪_X`. Then the completion
> functor `Coh(𝒪_X) ⥤ Coh(X, 𝓘)` of Stacks 0880 is an equivalence — faithful, full and essentially
> surjective — granted
>
> * `hFF`, the theorem on formal functions in degree zero (Stacks 087U), which is what Stacks 0883
>   assumes for full faithfulness and which this library does not carry unconditionally, and
> * `hDev`, the inductive step of the source's Noetherian induction: a coherent `𝓘`-adic system
>   killed by a quasi-coherent ideal sheaf `K` is in the essential image of the completion functor
>   as soon as every coherent `𝓘`-adic system killed by an ideal sheaf strictly larger than `K` is.
>
> Everything else is proved here. Full faithfulness is Stacks 0883 read through `hFF`. Essential
> surjectivity is the Noetherian induction `essImage_completionFunctor_of_devissage` applied at the
> zero ideal sheaf, which kills every system by `isSystemAnnihilatedBy_bot`; the induction is
> legitimate because the quasi-coherent ideal sheaves of the Noetherian scheme `X` satisfy the
> ascending chain condition. Noetherianity of `X` is not an added hypothesis: local Noetherianity
> follows from `LocallyOfFiniteType f` over the Noetherian base and quasi-compactness from the
> universal closedness of `f` and the quasi-compactness of `Spec A`.
>
> `hDev` is the source's own step. Granted `hFF` it is, like the generation hypothesis `hGen` of
> `Stacks.Algebraization.isEquivalence_completionFunctor_of_exists_epi`, equivalent to the
> conclusion; what differs is the obligation. `hGen` grants nothing and is not a step of the
> source's proof for a proper morphism — the source proves it only in the projective case, by
> Stacks 0884 — whereas `hDev` is discharged one ideal sheaf at a time with the statement already
> available on every strictly larger ideal sheaf. The source supplies `hDev`
> by Chow's lemma (Stacks 0200), Stacks 087T, the projective case Stacks 0885, the coherence of a
> proper direct image (Stacks 02O5) and Stacks 088A together with 088B; of those this library
> carries 0200 and 087T unconditionally, has 0885 only with `hFF` and a generation hypothesis
> resting on the absent Stacks 0884 and 0897, and carries none of 02O5, 088A, 088B.

```lean
public theorem isEquivalence_completionFunctor_of_devissage
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsProper f]
    (hFF : letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
      ∀ H : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
        IsIso (globalSectionsToLimit (baseIdealSheaf A I f) H))
    (hDev : letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
      ∀ K : X.IdealSheafData,
        (∀ K' : X.IdealSheafData, K < K' →
            ∀ 𝓖 : Stacks.Coherent.CoherentAdicSystems (baseIdealSheaf A I f),
              IsSystemAnnihilatedBy K' 𝓖.obj →
                (completionFunctor X (baseIdealSheaf A I f)).essImage 𝓖) →
          ∀ 𝓕 : Stacks.Coherent.CoherentAdicSystems (baseIdealSheaf A I f),
            IsSystemAnnihilatedBy K 𝓕.obj →
              (completionFunctor X (baseIdealSheaf A I f)).essImage 𝓕) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    (completionFunctor X (baseIdealSheaf A I f)).IsEquivalence
```

**`Stacks.Algebraization.isEquivalence_completionFunctor_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/GrothendieckExistenceProper.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/GrothendieckExistenceProper.lean#L136).

> **Stacks 088C: Grothendieck's existence theorem for a proper morphism.** Let `A` be a
> Noetherian ring complete with respect to an ideal `I`, let `f : X ⟶ Spec A` be a proper morphism
> of schemes and set `𝓘 = I · 𝒪_X`. Then the completion functor `Coh(𝒪_X) ⥤ Coh(X, 𝓘)` of
> Stacks 0880 is an equivalence.
>
> This is `Stacks.Algebraization.isEquivalence_completionFunctor_of_devissage` with both of its
> hypotheses discharged: `hFF` by the theorem on formal functions in degree zero over a complete
> base, `isIso_globalSectionsToLimit_of_isProper`, and `hDev` by
> `Stacks.Coherent.essImage_completionFunctor_of_devissageStep`.

```lean
public theorem isEquivalence_completionFunctor_of_isProper
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsProper f] :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    (completionFunctor X (baseIdealSheaf A I f)).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.25, Tag 0886](https://stacks.math.columbia.edu/tag/0886)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
