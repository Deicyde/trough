---
declaration: section
origin: cited
lean: AlgebraicGeometry.isPerfect_derivedPushforward_tensor_and_isIso_tensorFlatBaseChangeMap, Stacks.AlgebraicGeometry.FinitePresentationGlobalSectionsModel.exists_finiteProjectiveModel_of_properSupport, Stacks.AlgebraicGeometry.ProperSupportModel.exists_finiteProjectiveModel_derivedGlobalSections_functorial, AlgebraicGeometry.isPseudoCoherent_derivedPushforward_tensor_and_isIso_tensorFlatBaseChangeMap, AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.perfectDerivedPushforward, AlgebraicGeometry.ProperFlatBaseChange.isIso_derivedBaseChangeMap_of_isPerfect, AlgebraicGeometry.ProperFlatBaseChange.isIso_derivedBaseChangeComp_singleDegree_of_isFinitePresentation, AlgebraicGeometry.isPerfect_derivedPushforward_and_isIso_derivedBaseChangeMap_of_flat_of_isProper
statement: formalized
proof: formalized
---

# 36.30 Cohomology and base change, VI

Section 36.30 of the Stacks Project, [Tag 0A1G](https://stacks.math.columbia.edu/tag/0A1G). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A1H, a lemma

[Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H) in the Stacks Project.

**`AlgebraicGeometry.isPerfect_derivedPushforward_tensor_and_isIso_tensorFlatBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TensorFinitelyPresentedPerfect.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/TensorFinitelyPresentedPerfect.lean#L88).

> **[Stacks, Tag 0A1H].** Let `f : X ⟶ S` be a morphism of schemes of finite presentation, let
> `E` be a perfect object of `D(𝒪_X)` and let `𝒢^•` be a bounded complex of finitely presented
> `𝒪_X`-modules, flat over `S`, with support proper over `S`. Then
> `K = Rf_*(E ⊗^L_{𝒪_X} 𝒢^•)` is a perfect object of `D(𝒪_S)`, and its formation commutes with
> arbitrary base change: for every cartesian square the canonical map
> `Lg^*Rf_*(E ⊗^L 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L (g')^*𝒢^•)` of
> `AlgebraicGeometry.tensorFlatBaseChangeMap` is an isomorphism.

```lean
theorem isPerfect_derivedPushforward_tensor_and_isIso_tensorFlatBaseChangeMap {X S : Scheme.{u}}
    (f : X ⟶ S) (hf : FinitePresentation f) (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E) (G : CochainComplex X.Modules ℤ)
    (hG : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      FlatProperSupportFinitelyPresented f G) :
    RingedSpace.IsPerfect (X := S.toRingedSpace)
        ((derivedPushforward f.toLRSHom.toShHom).obj
          (((derivedTensorProductFunctor X.sheaf).obj E).obj (DerivedCategory.Q.obj G))) ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (hsq : IsPullback g' f' f g),
        IsIso (tensorFlatBaseChangeMap f g f' g' (comp_toShHom_of_comm hsq.w) E G)
```

## Tag 0A1I, a remark

[Tag 0A1I](https://stacks.math.columbia.edu/tag/0A1I) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FinitePresentationGlobalSectionsModel.exists_finiteProjectiveModel_of_properSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/FinitePresentationGlobalSectionsModel.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/FinitePresentationGlobalSectionsModel.lean#L149). The attribute's comment: “existence of the finite projective model M and the identification RGamma(X_{R'}, G_{R'}) = M tensor_R R' for every base change; naturality in R' NOT stated. CARRIED: the pseudo-coherence half of the perfection, as the named residue PseudoCoherentDerivedGlobalSectionsOfProperSupport, and separatedness of f, a narrowing. Proved: the finite-Tor-dimension half and the identification. Accounting in the docstring”.

> Let `R` be a ring, let `X` be a scheme of finite presentation over `R`, separated over `R`,
> and let `G` be a finitely presented `𝒪_X`-module, flat over `R`, whose support is proper over `R`.
> Assume `hres`, pseudo-coherence of `RΓ(X, G)` in this generality. Then there is a finite complex
> `M` of finite projective `R`-modules such that for every homomorphism `φ : R ⟶ R'` and every
> cartesian square exhibiting `X'` as the base change of `X` along `Spec R' ⟶ Spec R`,
>
> `RΓ(X_{R'}, G_{R'}) ≅ M ⊗_R R'`  in  `D(R')`.
>
> Naturality of this identification in `R'` is not asserted.

```lean
theorem exists_finiteProjectiveModel_of_properSupport
    (hres : PseudoCoherentDerivedGlobalSectionsOfProperSupport.{u})
    {R : Type u} [CommRing R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IsSeparated f]
    (hf : FinitePresentation f) (G : X.Modules) (hGfp : G.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom G)
    (hsupp : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      ∃ Z : Closeds X, IsProperOver f Z ∧ SheafOfModules.supp G ⊆ (Z : Set X)) :
    ∃ (M : CochainComplex (ModuleCat.{u} R) ℤ) (a b : ℤ),
      M.IsStrictlyGE a ∧ M.IsStrictlyLE b ∧
        (∀ i : ℤ, Module.Finite R (M.X i)) ∧ (∀ i : ℤ, Module.Projective R (M.X i)) ∧
        ∀ {R' : Type u} [CommRing R'] (φ : R →+* R') {X' : Scheme.{u}}
          {f' : X' ⟶ Spec (.of R')} {g : X' ⟶ X}
          (_hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ))),
          Nonempty (derivedGlobalSectionsOverBase f' ((Scheme.Modules.pullback g).obj G) ≅
            DerivedCategory.Q.obj (extendScalarsComplex φ M))
```

**`Stacks.AlgebraicGeometry.ProperSupportModel.exists_finiteProjectiveModel_derivedGlobalSections_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperSupportModel/FunctorialModel.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperSupportModel/FunctorialModel.lean#L203). The attribute's comment: “the remark in full: one finite complex M of finite projective R-modules, the identification RGamma(X_{R'}, G_{R'}) = M tensor_R R' in D(R') for every base change, as a family of isomorphisms indexed by the ring map and the cartesian square and pinned to a single chain-level model over R, and the functoriality in R' as the cocycle square of the chain-level comparisons for two successive base changes; under exactly the source's hypotheses (X of finite presentation over R, not assumed separated; G finitely presented, flat over R, with proper support). The comparisons are Čech models of the scheme-theoretic support of G, which is proper over R; the cover is bound inside the existential”.

> **[Stacks, Tag 0A1I].** Let `R` be a ring, let `X` be a scheme of finite presentation over `R`
> and let `G` be a finitely presented `𝒪_X`-module, flat over `R`, whose support is proper over `R`.
> Then there is a finite complex `M` of finite projective `R`-modules and, for every ring map
> `φ : R ⟶ R'` and every cartesian square exhibiting `X'` as `X ×_R R'`, an identification
>
> `c(φ, square) : RΓ(X_{R'}, G_{R'}) ≅ M ⊗_R R'`  in `D(R')`,
>
> functorial in `R'`: there are a finite affine open cover `U` of the scheme-theoretic support `Z`
> of `G` and chain-level comparisons
>
> `Θ(φ, square) : M ⊗_R R' ⟶ Č_alt(Z_{R'}, U_{R'}, G'_{R'})`,
>
> `G' = G|_Z`, such that
>
> * every `Θ(φ, square)` is a quasi-isomorphism;
> * `c(φ, square)` is the identification `Θ(φ, square)` induces, through the Čech model of
>   `RΓ(Z_{R'}, G'_{R'})` and the canonical `RΓ(Z_{R'}, G'_{R'}) ≅ RΓ(X_{R'}, G_{R'})`
>   (`supportComparisonIso`);
> * **the comparisons are functorial in `R'`**: for a second ring map `ψ : R' ⟶ R''` and a second
>   cartesian square, the extension of scalars along `ψ` of `Θ(φ, square)`, followed by the Čech
>   base-change isomorphism of [Stacks, Tag 07VK] (2) for `Z_{R''} = Z_{R'} ×_{R'} R''` and by the
>   identifications of the modules and covers, is `Θ(ψ ∘ φ, pasted square)` read through
>   `(M ⊗_R R') ⊗_{R'} R'' ≅ M ⊗_R R''`.
>
> The hypotheses are exactly the source's: `X` is not assumed separated, and nothing about
> `RΓ(X, G)` is assumed. `M` comes from the perfection of `RΓ(X, G)`, which is [Stacks, Tag 0A1H];
> the identifications and their functoriality are computed on the support `Z`, which is proper and
> hence separated over `R`; see the module docstring.

```lean
theorem exists_finiteProjectiveModel_derivedGlobalSections_functorial
    {R : Type u} [CommRing R] {X : Scheme.{u}} (f : X ⟶ Spec (.of R))
    (hf : FinitePresentation f) (G : X.Modules) (hGfp : G.IsFinitePresentation)
    (hflat : IsFlatOver f.toLRSHom.toShHom G)
    (hsupp : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      ∃ Z : Closeds X, IsProperOver f Z ∧ SheafOfModules.supp G ⊆ (Z : Set X)) :
    haveI : G.IsQuasicoherent := Stacks.Modules.isQuasicoherent_of_isFinitePresentation G
    haveI : G.IsFiniteType := Stacks.StalkFiniteType.isFiniteType_of_isFinitePresentation G
    letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
    haveI : IsProper (supportι G ≫ f) := isProper_supportι_comp G f hsupp
    ∃ (M : CochainComplex (ModuleCat.{u} R) ℤ) (a b : ℤ),
      M.IsStrictlyGE a ∧ M.IsStrictlyLE b ∧
        (∀ i : ℤ, Module.Finite R (M.X i)) ∧ (∀ i : ℤ, Module.Projective R (M.X i)) ∧
        ∃ (c : ∀ {R' : Type u} [CommRing R'] (φ : R →+* R') {X' : Scheme.{u}}
              {f' : X' ⟶ Spec (.of R')} {g : X' ⟶ X},
              IsPullback g f' f (Spec.map (CommRingCat.ofHom φ)) →
                (derivedGlobalSectionsOverBase f' ((Scheme.Modules.pullback g).obj G) ≅
                  DerivedCategory.Q.obj (extendScalarsComplex φ M)))
          (I : Type u) (hIfin : Finite I) (hIlin : LinearOrder I)
          (U : I → (supportScheme G).Opens) (hU : (⊤ : (supportScheme G).Opens) = ⨆ i, U i)
          (hUaff : ∀ i, IsAffineOpen (U i)),
          haveI : Finite I := hIfin
          letI : LinearOrder I := hIlin
          ∃ (_haff : ∀ (r : ℕ) (s : Fin (r + 1) → I), IsAffineOpen (⨅ k, U (s k)))
            (Θ : ∀ {R' : Type u} [CommRing R'] (φ : R →+* R') {X' : Scheme.{u}}
                {f' : X' ⟶ Spec (.of R')} {g : X' ⟶ X},
                IsPullback g f' f (Spec.map (CommRingCat.ofHom φ)) →
                  (extendScalarsComplex φ M ⟶
                    baseAlternatingCechComplex (supportSnd G g ≫ f')
                      (fun j => supportFst G g ⁻¹ᵁ U j) (top_eq_iSup_preimage _ U hU)
                      ((Scheme.Modules.pullback (supportFst G g)).obj (supportModule G)))),
            (∀ {R' : Type u} [CommRing R'] (φ : R →+* R') {X' : Scheme.{u}}
                {f' : X' ⟶ Spec (.of R')} {g : X' ⟶ X}
                (hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ))),
                QuasiIso (Θ φ hsq)) ∧
              (∀ {R' : Type u} [CommRing R'] (φ : R →+* R') {X' : Scheme.{u}}
                  {f' : X' ⟶ Spec (.of R')} {g : X' ⟶ X}
                  (hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ))),
                  (c φ hsq).inv =
                    (DerivedCategory.Q.map (Θ φ hsq) ≫
                      (alternatingCechIsoDerivedGlobalSectionsOverBase (supportSnd G g ≫ f')
                        (fun j => supportFst G g ⁻¹ᵁ U j) (top_eq_iSup_preimage _ U hU)
                        ((Scheme.Modules.pullback (supportFst G g)).obj (supportModule G))
                        (iInf_preimage_isAffineOpen φ (isPullback_support G g f φ hsq) U
                          hUaff)).hom) ≫
                      (supportComparisonIso G g f').hom) ∧
              (∀ {R' R'' : Type u} [CommRing R'] [CommRing R''] (φ : R →+* R') (ψ : R' →+* R'')
                  {X' X'' : Scheme.{u}} {f' : X' ⟶ Spec (.of R')} {f'' : X'' ⟶ Spec (.of R'')}
                  {g : X' ⟶ X} {g' : X'' ⟶ X'}
                  (hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ)))
                  (hsq' : IsPullback g' f'' f' (Spec.map (CommRingCat.ofHom ψ))),
                  haveI : IsSeparated (supportSnd G g ≫ f') :=
                    isSeparated_of_isPullback φ (isPullback_support G g f φ hsq)
                  ((ModuleCat.extendScalars.{u, u, u} ψ).mapHomologicalComplex
                          (ComplexShape.up ℤ)).map (Θ φ hsq) ≫
                      (baseAlternatingCechComplexBaseChangeIso ψ
                          (isPullback_supportTower G g g' ψ hsq')
                          ((Scheme.Modules.pullback (supportFst G g)).obj (supportModule G))
                          (fun j => supportFst G g ⁻¹ᵁ U j) (top_eq_iSup_preimage _ U hU)
                          (isAffineOpen_preimage φ (isPullback_support G g f φ hsq) U
                            hUaff)).hom ≫
                      (baseAlternatingCechComplexMapIso (supportSnd G (g' ≫ g) ≫ f'')
                        (fun j => (supportTowerMap G g g' ≫ supportFst G g) ⁻¹ᵁ U j)
                        (top_eq_iSup_preimage _ U hU)
                        ((Scheme.Modules.pullbackComp (supportTowerMap G g g')
                          (supportFst G g)).app (supportModule G))).hom ≫
                      (cechCongrIso (supportModule G) U hU (supportTowerMap_fst G g g')).hom =
                    (extendScalarsComplexCompIso φ ψ).hom.app M ≫
                      Θ (ψ.comp φ) (Stacks.Cech.isPullback_comp_specMap φ ψ f f' f'' g g' hsq
                        hsq'))
```

## Tag 0CSC, a lemma

[Tag 0CSC](https://stacks.math.columbia.edu/tag/0CSC) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherent_derivedPushforward_tensor_and_isIso_tensorFlatBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/TensorPseudoCoherentPushforward.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/TensorPseudoCoherentPushforward.lean#L368).

> **[Stacks, Tag 0CSC].** Let `f : X ⟶ S` be a morphism of schemes of finite presentation, let
> `E` be a pseudo-coherent object of `D(𝒪_X)` and let `𝒢^•` be a bounded above complex of finitely
> presented `𝒪_X`-modules, flat over `S`, with support proper over `S`. Then
> `K = Rf_*(E ⊗^L_{𝒪_X} 𝒢^•)` is a pseudo-coherent object of `D(𝒪_S)`, and its formation commutes
> with arbitrary base change: for every cartesian square the canonical map
> `Lg^*Rf_*(E ⊗^L 𝒢^•) ⟶ Rf'_*(L(g')^*E ⊗^L (g')^*𝒢^•)` of
> `AlgebraicGeometry.tensorFlatBaseChangeMap` is an isomorphism.
>
> Support proper over `S` means that a single closed subset of `X` proper over `S` contains the
> support of every term of `𝒢^•`.

```lean
theorem isPseudoCoherent_derivedPushforward_tensor_and_isIso_tensorFlatBaseChangeMap
    (hf : FinitePresentation f)
    (E : DerivedCategory X.Modules) (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E)
    (G : CochainComplex X.Modules ℤ) (hGminus : CochainComplex.minus X.Modules G)
    (hfp : ∀ i : ℤ, (G.X i).IsFinitePresentation)
    (hflat : ∀ i : ℤ, IsFlatOver f.toLRSHom.toShHom (G.X i))
    (hsupp : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      ∃ Z : Closeds X, IsProperOver f Z ∧ ∀ i : ℤ, SheafOfModules.supp (G.X i) ⊆ (Z : Set X)) :
    RingedSpace.IsPseudoCoherent (X := S.toRingedSpace)
        ((derivedPushforward f.toLRSHom.toShHom).obj
          (((derivedTensorProductFunctor X.sheaf).obj E).obj (DerivedCategory.Q.obj G))) ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (hsq : IsPullback g' f' f g),
        IsIso (tensorFlatBaseChangeMap f g f' g' (comp_toShHom_of_comm hsq.w) E G)
```

## Tag 0B91, a lemma

[Tag 0B91](https://stacks.math.columbia.edu/tag/0B91) in the Stacks Project.

**`AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.perfectDerivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPerfection/Assembly.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPerfection/Assembly.lean#L95). The attribute's comment: “clause (2), the perfection half: for f proper of finite presentation and a module of finite presentation flat over S, Rf_*F is a perfect object of D(O_S), over an arbitrary base. Proved by Noetherian approximation of (f, F), the Noetherian case, base change and stability of perfection under derived pullback; nothing is granted”. References: SGA 6 IV (3.3.2), “3.3.2.3, special case”.

> Let `f : X ⟶ S` be a proper morphism of finite presentation and `ℱ` an `𝒪_X`-module of
> finite presentation, flat over `S`. Then `Rf_*ℱ` is a perfect object of `D(𝒪_S)`.

```lean
theorem perfectDerivedPushforward : PerfectDerivedPushforward.{u}
```

**`AlgebraicGeometry.ProperFlatBaseChange.isIso_derivedBaseChangeMap_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChangeCanonical.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChangeCanonical.lean#L174). The attribute's comment: “clause (1), the base-change half only: for f flat (and quasi-compact and quasi-separated, which a proper morphism of finite presentation is) and E perfect, the canonical map Lg^*Rf_*E --> Rf'_*L(g')^*E of Tag 08HY is an isomorphism for every cartesian square. Nothing is granted. The perfection half of clause (1) is not proved”.

> Let `f : X ⟶ S` be flat, proper and of finite presentation and let `E` be a perfect object
> of `D(𝒪_X)`. For every cartesian square, the formation of `Rf_*E` commutes with base change: the
> canonical map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` of [Stacks, Tag 08HY] is an isomorphism.
>
> Only quasi-compactness and quasi-separatedness of `f` are used, besides flatness, so the
> statement is made under those; a proper morphism of finite presentation has both. That `Rf_*E`
> is perfect is not stated here.

```lean
theorem isIso_derivedBaseChangeMap_of_isPerfect (hsq : IsPullback g' f' f g) [QuasiCompact f]
    [QuasiSeparated f] [Flat f] (E : DerivedCategory X.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E) :
    IsIso (derivedBaseChangeMap g'.toLRSHom.toShHom f'.toLRSHom.toShHom f.toLRSHom.toShHom
      g.toLRSHom.toShHom (comp_toShHom_of_comm hsq.w) E)
```

**`AlgebraicGeometry.ProperFlatBaseChange.isIso_derivedBaseChangeComp_singleDegree_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChangeCanonical.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardBaseChangeCanonical.lean#L197). The attribute's comment: “clause (2), the base-change half only: for f quasi-compact and quasi-separated (which a proper morphism of finite presentation is) and G of finite presentation and flat over S, the canonical map Lg^*Rf_*G --> Rf'_*L(g')^*G --> Rf'_*(g')^*G (Tag 08HY followed by the derived-to-ordinary comparison) is an isomorphism for every cartesian square. Nothing is granted. The perfection half of clause (2) is perfectDerivedPushforward”.

> Let `f : X ⟶ S` be proper of finite presentation and let `𝒢` be an `𝒪_X`-module of finite
> presentation, flat over `S`. For every cartesian square, the formation of `Rf_*𝒢` commutes with
> base change: the canonical map `Lg^*Rf_*𝒢 ⟶ Rf'_*L(g')^*𝒢 ⟶ Rf'_*(g')^*𝒢` — the map of
> [Stacks, Tag 08HY] followed by `Rf'_*` of the derived-to-ordinary comparison,
> `derivedBaseChangeComp` — is an isomorphism.
>
> Only quasi-compactness and quasi-separatedness of `f` are used, so the statement is made under
> those. That `Rf_*𝒢` is perfect is
> `AlgebraicGeometry.ProperFlatFibreEulerCharacteristic.perfectDerivedPushforward`.

```lean
theorem isIso_derivedBaseChangeComp_singleDegree_of_isFinitePresentation
    (hsq : IsPullback g' f' f g) [QuasiCompact f] [QuasiSeparated f] (G : X.Modules)
    [G.IsFinitePresentation] (hGflat : IsFlatOver f.toLRSHom.toShHom G) :
    IsIso (derivedBaseChangeComp f g f' g' hsq.w (DerivedCategory.Q.obj (singleDegreeComplex G))
      (DerivedCategory.Q.obj ((pullbackComplex g'.toLRSHom.toShHom).obj (singleDegreeComplex G)))
      ((derivedPullbackNatTrans g'.toLRSHom.toShHom).app (singleDegreeComplex G)))
```

**`AlgebraicGeometry.isPerfect_derivedPushforward_and_isIso_derivedBaseChangeMap_of_flat_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardPerfect.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardPerfect.lean#L297). The attribute's comment: “clause (1) in full: perfectness of Rf_*E, and invertibility of the canonical base change map Lg^*Rf_*E --> Rf'_*L(g')^*E of Tag 08HY for every cartesian square, which is what 'its formation commutes with arbitrary base change' means; finite presentation of the proper f is spelled LocallyOfFinitePresentation, the quasi-compactness and quasi-separation it adds being part of properness”. References: SGA 6 IV (3.1.1), “special case”.

> **[Stacks, Tag 0B91] (1).** Let `f : X ⟶ S` be a flat proper morphism of finite presentation
> and let `E` be a perfect object of `D(𝒪_X)`. Then `Rf_*E` is a perfect object of `D(𝒪_S)`, and its
> formation commutes with arbitrary base change: for every cartesian square
> ```
> X' --g'--> X
> |          |
> f'         f
> v          v
> S' --g---> S
> ```
> the canonical base change map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` of [Stacks, Tag 08HY] is an
> isomorphism.
>
> Perfectness is `isPerfect_derivedPushforward_of_flat_of_isProper`. For base change, `f` is flat, so
> `X` and `S'` are Tor independent over `S`, and `E` has quasi-coherent cohomology, so the canonical
> map is invertible by [Stacks, Tag 08IB].

```lean
theorem isPerfect_derivedPushforward_and_isIso_derivedBaseChangeMap_of_flat_of_isProper
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [IsProper f] [LocallyOfFinitePresentation f]
    (E : DerivedCategory X.Modules) (hE : IsPerfect (X := X.toRingedSpace) E) :
    IsPerfect (X := S.toRingedSpace) ((derivedPushforwardModules f).obj E) ∧
      ∀ {S' X' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (Stacks.Cohomology.DerivedBaseChange.derivedBaseChangeMap g'.toLRSHom.toShHom
          f'.toLRSHom.toShHom f.toLRSHom.toShHom g.toLRSHom.toShHom
          (comp_toShHom_of_comm sq.w) E)
```

**`AlgebraicGeometry.ProperFlatBaseChange.isPerfect_derivedPushforward_and_isIso_baseChange_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperPushforwardPerfectAndBaseChange.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperPushforwardPerfectAndBaseChange.lean#L90). The attribute's comment: “both clauses in full: for f proper of finite presentation, (1) for f flat and E perfect, Rf_*E is perfect and the canonical map Lg^*Rf_*E --> Rf'_*L(g')^*E of Tag 08HY is an isomorphism for every cartesian square; (2) for G of finite presentation and flat over S, Rf_*G is perfect and the canonical map Lg^*Rf_*G --> Rf'_*(g')^*G is an isomorphism for every cartesian square”.

> **[Stacks, Tag 0B91].** Let `f : X ⟶ S` be a proper morphism of schemes of finite
> presentation.
>
> 1. Let `E ∈ D(𝒪_X)` be perfect and `f` flat. Then `Rf_*E` is a perfect object of `D(𝒪_S)`, and
>    its formation commutes with arbitrary base change: for every cartesian square
>    `X' = X ×_S S'` the canonical map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` of [Stacks, Tag 08HY] is an
>    isomorphism.
> 2. Let `𝒢` be an `𝒪_X`-module of finite presentation, flat over `S`. Then `Rf_*𝒢` is a perfect
>    object of `D(𝒪_S)`, and its formation commutes with arbitrary base change: for every
>    cartesian square the canonical map `Lg^*Rf_*𝒢 ⟶ Rf'_*L(g')^*𝒢 ⟶ Rf'_*(g')^*𝒢` (the map of
>    [Stacks, Tag 08HY] followed by `Rf'_*` of the derived-to-ordinary comparison) is an
>    isomorphism.
>
> Here `𝒢` is placed in degree zero as the complex `singleDegreeComplex 𝒢`, at which the
> base-change map of clause (2) is written.

```lean
theorem isPerfect_derivedPushforward_and_isIso_baseChange_of_isProper {X S : Scheme.{u}}
    (f : X ⟶ S) (hf : FinitePresentation f) (hproper : IsProper f) :
    (Flat f → ∀ E : DerivedCategory X.Modules, RingedSpace.IsPerfect (X := X.toRingedSpace) E →
      RingedSpace.IsPerfect (X := S.toRingedSpace)
          ((derivedPushforward f.toLRSHom.toShHom).obj E) ∧
        ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
          (hsq : IsPullback g' f' f g),
          IsIso (derivedBaseChangeMap g'.toLRSHom.toShHom f'.toLRSHom.toShHom f.toLRSHom.toShHom
            g.toLRSHom.toShHom (comp_toShHom_of_comm hsq.w) E)) ∧
    (∀ G : X.Modules, G.IsFinitePresentation → IsFlatOver f.toLRSHom.toShHom G →
      RingedSpace.IsPerfect (X := S.toRingedSpace)
          ((derivedPushforward f.toLRSHom.toShHom).obj
            (DerivedCategory.Q.obj (singleDegreeComplex G))) ∧
        ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
          (hsq : IsPullback g' f' f g),
          IsIso (derivedBaseChangeComp f g f' g' hsq.w
            (DerivedCategory.Q.obj (singleDegreeComplex G))
            (DerivedCategory.Q.obj ((pullbackComplex g'.toLRSHom.toShHom).obj
              (singleDegreeComplex G)))
            ((derivedPullbackNatTrans g'.toLRSHom.toShHom).app (singleDegreeComplex G))))
```

## Tag 0CSD, a lemma

[Tag 0CSD](https://stacks.math.columbia.edu/tag/0CSD) in the Stacks Project.

**`AlgebraicGeometry.isPseudoCoherent_derivedPushforward_and_isIso_derivedBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardPseudoCoherent.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPushforwardPseudoCoherent.lean#L77).

> **[Stacks, Tag 0CSD].** Let `f : X ⟶ S` be a flat proper morphism of schemes of finite
> presentation and let `E ∈ D(𝒪_X)` be pseudo-coherent. Then `Rf_*E` is a pseudo-coherent object of
> `D(𝒪_S)` and its formation commutes with arbitrary base change: for every cartesian square
> `X' = X ×_S S'` the base change map `Lg^*Rf_*E ⟶ Rf'_*L(g')^*E` of [Stacks, Tag 08HY] is an
> isomorphism.

```lean
theorem isPseudoCoherent_derivedPushforward_and_isIso_derivedBaseChangeMap [Flat f] [IsProper f]
    [LocallyOfFinitePresentation f]
    (E : DerivedCategory X.Modules) (hE : RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E) :
    RingedSpace.IsPseudoCoherent (X := S.toRingedSpace)
        ((derivedPushforward f.toLRSHom.toShHom).obj E) ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (sq : IsPullback g' f' f g),
        IsIso (derivedBaseChangeMap g'.toLRSHom.toShHom f'.toLRSHom.toShHom f.toLRSHom.toShHom
          g.toLRSHom.toShHom (comp_toShHom_of_comm sq.w) E)
```

## Tag 0D2Q, a lemma

[Tag 0D2Q](https://stacks.math.columbia.edu/tag/0D2Q) in the Stacks Project.

**`Stacks.ProperFlatPullbackLimit.bijective_comp_singleFunctor_map_limitPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPullbackInverseLimit.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPullbackInverseLimit.lean#L226). The attribute's comment: “the canonical map O_X ⊗_R lim M_n --> lim O_X ⊗_R M_n induces bijections Hom(E, source) --> Hom(E, target) for every E in D_QCoh(O_X), which is what the source's proof says the statement means; at every model of the derived category”.

> **Stacks Project, Tag 0D2Q**, in the form the source's proof unfolds it. Let `R` be a ring,
> `f : X ⟶ Spec R` proper, flat and of finite presentation, and `(Mₙ)` an inverse system of
> `R`-modules with surjective transition maps. Then for every object `E` of `D_QCoh(𝒪_X)` the
> canonical map `O_X ⊗_R (lim Mₙ) ⟶ lim (O_X ⊗_R Mₙ)` induces a bijection
>
> `Hom(E, O_X ⊗_R (lim Mₙ)) ⟶ Hom(E, lim O_X ⊗_R Mₙ)`.
>
> Here `O_X ⊗_R M` is `f^*M^~`, both modules are placed in degree zero, the limit on the right is
> the limit in `𝒪_X`-modules and the canonical map is `limit.post`. The statement is made at an
> arbitrary model of the derived category of `𝒪_X`-modules.

```lean
theorem bijective_comp_singleFunctor_map_limitPost (R : CommRingCat.{u}) {X : Scheme.{u}}
    (f : X ⟶ Spec R) [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (M : ℕᵒᵖ ⥤ ModuleCat.{u} R) (hsurj : ∀ n : ℕ, Epi (M.map (homOfLE (Nat.le_succ n)).op))
    [HasDerivedCategory.{w} X.Modules] (E : DerivedCategory X.Modules)
    (hE : DerivedCategoryB.derivedCategoryB (A := X.Modules)
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) E) :
    Function.Bijective (fun φ : E ⟶ (DerivedCategory.singleFunctor X.Modules 0).obj
        ((tilde.functor R ⋙ Scheme.Modules.pullback f).obj (limit M)) =>
      φ ≫ (DerivedCategory.singleFunctor X.Modules 0).map
        (limit.post M (tilde.functor R ⋙ Scheme.Modules.pullback f)))
```

**`Stacks.ProperFlatPullbackLimit.isIso_homEquiv_singleFunctor_map_limitPost`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPullbackInverseLimit.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatPullbackInverseLimit.lean#L266).

> **Stacks Project, Tag 0D2Q.** Let `R` be a ring, `f : X ⟶ Spec R` proper, flat and of finite
> presentation, and `(Mₙ)` an inverse system of `R`-modules with surjective transition maps. Then
> the canonical map `O_X ⊗_R (lim Mₙ) ⟶ lim (O_X ⊗_R Mₙ)` induces an isomorphism from the source to
> `DQ_X` applied to the target: for every right adjoint `DQ` of the inclusion
> `D_QCoh(𝒪_X) ⥤ D(𝒪_X)` (one exists by [Stacks, Tag 0CR0]), the morphism
> `O_X ⊗_R (lim Mₙ) ⟶ DQ(lim O_X ⊗_R Mₙ)` adjoint to the canonical map is an isomorphism.

```lean
theorem isIso_homEquiv_singleFunctor_map_limitPost (R : CommRingCat.{u}) {X : Scheme.{u}}
    (f : X ⟶ Spec R) [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (M : ℕᵒᵖ ⥤ ModuleCat.{u} R) (hsurj : ∀ n : ℕ, Epi (M.map (homOfLE (Nat.le_succ n)).op))
    {DQ : DerivedCategory X.Modules ⥤ Stacks.Duality.quasiCoherentDerivedCategory X}
    (adj : Stacks.Duality.Coherator.quasiCoherentι X ⊣ DQ) :
    IsIso (adj.homEquiv (pullbackTildeLimitQCoh f M) _
      ((DerivedCategory.singleFunctor X.Modules 0).map
        (limit.post M (tilde.functor R ⋙ Scheme.Modules.pullback f))))
```

## Tag 0A1J, a lemma

[Tag 0A1J](https://stacks.math.columbia.edu/tag/0A1J) in the Stacks Project.

**`AlgebraicGeometry.isIso_sheafHomFlatBaseChangeMap_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomFinitelyPresentedPushforwardBaseChange.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/BaseChange/SheafHomFinitelyPresentedPushforwardBaseChange.lean#L166). The attribute's comment: “the base-change half of the conclusion ONLY, for the canonical map sheafHomFlatBaseChangeMap of Stacks 08IE, with the ORDINARY pullback (g')^*𝒢^• on the right as the source's boldface demands. The perfection half -- that K is a perfect object of D(O_S) -- is NOT proved and is not stated: the library's result for it is Tag 0DJR, which assumes a Noetherian base, a locally-of-finite-type f and coherent terms, none of which Tag 0A1J grants, and the source closes that gap by a limit descent (Tags 01ZM, 01ZR, 05LY, 081G, 09RF) to a Noetherian stage that is not assembled in this library. Of what Tag 08IE case (1) asks beyond Tag 0A1J's hypotheses, all four are discharged here: quasi-compactness and quasi-separatedness of f from Tag 01TP part (3), commutativity of the square from the cartesian square, boundedness above of the complex from its two-sided boundedness, and quasi-coherence of its terms from their finite presentation by Tag 01BW. The perfectness of E is the source's own hypothesis, stated at the predicate Tag 08IE is written at, not a weaker stand-in. The three steps of the source proof of Tag 08IE are not assumed: Tag 08IE case (1) is proved outright in this library. What remains among this statement's own conditions is hK and hK', the quasi-coherence of the cohomology of the two derived internal homs, which Tag 0DJ9 asks of its complexes and which this library has at a spelling of the derived internal hom that does not line up with the one the comparison map is written at. The proper-support hypothesis on the complex is carried in the bundle and is not used by this half, the source's base-change argument not appealing to it”.

> **[Stacks, Tag 0A1J], the base-change half of the conclusion.** Let `f : X ⟶ S` be a
> morphism of schemes of finite presentation, let `E` be a perfect object of `D(𝒪_X)` and let
> `𝒢^•` be a bounded complex of finitely presented `𝒪_X`-modules, flat over `S`, with support
> proper over `S`. For every cartesian base-change square the canonical map
>
> `Lg^*Rf_*R𝓗om_{𝒪_X}(E, 𝒢^•) ⟶ Rf'_*R𝓗om_{𝒪_{X'}}(L(g')^*E, (g')^*𝒢^•)`
>
> of `AlgebraicGeometry.sheafHomFlatBaseChangeMap` is an isomorphism — note the ordinary pullback
> of `𝒢^•` on the right, as the source's boldface demands.
>
> The perfection half of [Stacks, Tag 0A1J] is not proved; the implementation notes of this file
> say what it would need.
>
> The proof is the reduction the source performs: finite presentation of `f` supplies the
> quasi-compactness and quasi-separatedness that case (1) of [Stacks, Tag 08IE] asks for, and the
> four conditions of `AlgebraicGeometry.FlatProperSupportFinitelyPresented` supply boundedness
> above of `𝒢^•` and quasi-coherence and relative flatness of its terms. The source's
> proper-support hypothesis on `𝒢^•` is part of that bundle and is not used by this half: the
> base-change argument does not appeal to it, and it is kept so that the hypothesis bundle is the
> one [Stacks, Tag 0A1J] states.

```lean
public theorem isIso_sheafHomFlatBaseChangeMap_of_finitePresentation
    {X X' S S' : Scheme.{u}} (f : X ⟶ S) (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
    (hsq : IsPullback g' f' f g)
    (sq : g'.toLRSHom.toShHom ≫ f.toLRSHom.toShHom =
      f'.toLRSHom.toShHom ≫ g.toLRSHom.toShHom)
    (hf : FinitePresentation f)
    (E : DerivedCategory X.Modules)
    (hEperfect : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E)
    (G : CochainComplex X.Modules ℤ)
    (hG : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      FlatProperSupportFinitelyPresented f G)
    (hK : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X.Modules n).obj
      (((derivedSheafHom X.sheaf).obj (op E)).obj
        (DerivedCategory.Q.obj G))).IsQuasicoherent)
    (hK' : ∀ n : ℤ, ((DerivedCategory.homologyFunctor X'.Modules n).obj
      (((derivedSheafHom X'.sheaf).obj
          (op ((derivedPullback g'.toLRSHom.toShHom).obj E))).obj
        (DerivedCategory.Q.obj
          ((pullbackComplex g'.toLRSHom.toShHom).obj G)))).IsQuasicoherent) :
    IsIso (sheafHomFlatBaseChangeMap f g f' g' sq E G)
```

**`AlgebraicGeometry.isPerfect_derivedPushforward_derivedSheafHom_and_isIso_sheafHomFlatBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SheafHomFinitelyPresentedPerfectBaseChange.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SheafHomFinitelyPresentedPerfectBaseChange.lean#L68).

> **[Stacks, Tag 0A1J].** Let `f : X ⟶ S` be a morphism of schemes of finite presentation, let
> `E` be a perfect object of `D(𝒪_X)` and let `𝒢^•` be a bounded complex of finitely presented
> `𝒪_X`-modules, flat over `S`, with support proper over `S`. Then
> `K = Rf_*R𝓗om_{𝒪_X}(E, 𝒢^•)` is a perfect object of `D(𝒪_S)`, and its formation commutes with
> arbitrary base change: for every cartesian square the canonical map
> `Lg^*Rf_*R𝓗om_{𝒪_X}(E, 𝒢^•) ⟶ Rf'_*R𝓗om_{𝒪_{X'}}(L(g')^*E, (g')^*𝒢^•)` of
> `AlgebraicGeometry.sheafHomFlatBaseChangeMap` is an isomorphism.

```lean
theorem isPerfect_derivedPushforward_derivedSheafHom_and_isIso_sheafHomFlatBaseChangeMap
    {X S : Scheme.{u}} (f : X ⟶ S) (hf : FinitePresentation f) (E : DerivedCategory X.Modules)
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E) (G : CochainComplex X.Modules ℤ)
    (hG : letI : LocallyOfFinitePresentation f := hf.locallyOfFinitePresentation
      FlatProperSupportFinitelyPresented f G) :
    RingedSpace.IsPerfect (X := S.toRingedSpace)
        ((derivedPushforward f.toLRSHom.toShHom).obj
          (((derivedSheafHom X.sheaf).obj (op E)).obj (DerivedCategory.Q.obj G))) ∧
      ∀ {X' S' : Scheme.{u}} (g : S' ⟶ S) (f' : X' ⟶ S') (g' : X' ⟶ X)
        (hsq : IsPullback g' f' f g),
        IsIso (sheafHomFlatBaseChangeMap f g f' g' (comp_toShHom_of_comm hsq.w) E G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.30, Tag 0A1G](https://stacks.math.columbia.edu/tag/0A1G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
