---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProperFlatGlobalSections.isPerfect_derivedGlobalSections, Stacks.AlgebraicGeometry.ProperFlatGlobalSections.isIso_derivedGlobalSectionsBaseChangeMap, Stacks.AlgebraicGeometry.ProperFlatGlobalSections.exists_finiteProjectiveModel_homology_iso_functorial
statement: formalized
proof: formalized
---

# 30.22 Cohomology and base change, III

Section 30.22 of the Stacks Project, [Tag 07VJ](https://stacks.math.columbia.edu/tag/07VJ). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07VK, a lemma

[Tag 07VK](https://stacks.math.columbia.edu/tag/07VK) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperFlatGlobalSections.isPerfect_derivedGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatGlobalSections.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatGlobalSections.lean#L644). The attribute's comment: “(1)”. References: SGA 6 0 (3.1), “affine-target flat case”; SGA 6 0 (4.1), “special case”; SGA 6 XIV (2.2), “special case”.

> **[Stacks, Tag 07VK] (1).** Let `A` be a Noetherian ring, let `f : X ⟶ Spec A` be proper and
> let `F` be a coherent `𝒪_X`-module flat over `Spec A`. Then `RΓ(X, F)` is a perfect object of
> `D(A)`.
>
> The proof is the source's. Properness makes `X` quasi-compact, so the affine open cover of `X` has
> a finite subcover `𝒰`; properness also makes `f` separated, so the finite intersections of members
> of `𝒰` are affine. The alternating Čech complex of `𝒰` therefore computes `RΓ(X, F)`
> ([Stacks, Tag 01FM] and [Stacks, Tag 01ET]), is bounded, and is termwise flat over `A`
> ([Stacks, Tag 01U4]) — which is finite Tor dimension. Its cohomology modules are finite over `A`,
> which is [Stacks, Tag 02O6], so it is pseudo-coherent ([Stacks, Tag 066E]); [Stacks, Tag 0658]
> concludes.
>
> **Unconditional.** The finiteness input — the affine-base case of [Stacks, Tag 02O5], carried
> through the lemmas above as the `Prop`
> `AlgebraicGeometry.ProperCoherentImage.HigherDirectImageIsCoherentOverAffineBase` — is supplied
> here by `AlgebraicGeometry.ProperCoherenceWitness.higherDirectImageIsCoherentOverAffineBase`, the
> hypothesis-free form of that tag. The finite-Tor-dimension half,
> `hasFlatRepresentative_derivedGlobalSectionsOverBase`, never needed it.

```lean
theorem isPerfect_derivedGlobalSections [IsNoetherianRing A] [IsProper f] [F.IsCoherent]
    (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    StacksDraft.Perfect.IsPerfect (derivedGlobalSectionsOverBase f F)
```

**`Stacks.AlgebraicGeometry.ProperFlatGlobalSections.isIso_derivedGlobalSectionsBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatGlobalSectionsBaseChange.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatGlobalSectionsBaseChange.lean#L257). The attribute's comment: “(2), for the Čech base-change comparison of a finite affine cover”.

> **[Stacks, Tag 07VK] (2).** Let `φ : A ⟶ A'` be a homomorphism of commutative rings, let
> `f : X ⟶ Spec A` be separated, let `g : X' ⟶ X` and `f' : X' ⟶ Spec A'` exhibit `X'` as the base
> change of `X` along `Spec A' ⟶ Spec A`, and let `F` be a quasi-coherent `𝒪_X`-module flat over
> `Spec A`. Then the base-change map
>
> `RΓ(X, F) ⊗^L_A A' ⟶ RΓ(X', g^* F)`
>
> is an isomorphism in `D(A')`.
>
> The proof is the source's. The alternating Čech complex of a finite affine cover whose finite
> intersections are affine computes `RΓ(X, F)` ([Stacks, Tag 01FM] and [Stacks, Tag 01ET]), it is
> bounded, and flatness of `F` over the base makes it termwise flat ([Stacks, Tag 01U4]); for such
> a complex the ordinary extension of scalars is the derived one ([Stacks, Tag 06XY]), and the
> ordinary extension of scalars of the model is the model of the inverse-image cover on `X'`
> ([Stacks, Tag 01XL]), which computes `RΓ(X', g^* F)`.
>
> **Unconditional.** No Noetherian hypothesis, no properness, no coherence, and in particular no
> appeal to `AlgebraicGeometry.ProperCoherentImage.HigherDirectImageIsCoherentOverAffineBase`,
> which clause (1) threads and clause (2) does not need. The hypotheses are weaker than the
> source's: for `A` Noetherian, `f` proper and `F` coherent and flat they hold, a suitable cover
> being supplied by `exists_finiteAffineCover_of_isProper`.

```lean
theorem isIso_derivedGlobalSectionsBaseChangeMap
    (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    IsIso (derivedGlobalSectionsBaseChangeMap φ hsq F U hU hUaff haff)
```

## Tag 07VL, a remark

[Tag 07VL](https://stacks.math.columbia.edu/tag/07VL) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperFlatGlobalSections.exists_finiteProjectiveModel_homology_iso_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatGlobalSectionsFunctorialModel.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProperFlatGlobalSectionsFunctorialModel.lean#L322). The attribute's comment: “Remark 30.22.2 in full: one bounded complex M of finite projective A-modules, the identification H^i(X_{A'}, F_{A'}) = H^i(M ⊗_A A') for every base change given as a family of isomorphisms indexed by the ring map, the cartesian square and the degree and pinned to the single chain-level model over A, and the functoriality in A' as the cocycle square for a second base change A' ⟶ A''; under exactly the source's conditions — A Noetherian, f proper, F coherent and flat over A — with the finite affine cover bound inside the existential and supplied by properness. The closing citation to Hartshorne that flatness is essential is remark-level and appears as documentation in the module docstring.”.

> **[Stacks, Tag 07VL], Remark 30.22.2, both clauses.** Let `A` be a Noetherian ring,
> `f : X ⟶ Spec A` a proper morphism of schemes and `F` a coherent `𝒪_X`-module flat over `A`. Then
> there is a bounded complex `M` of finite projective `A`-modules, a finite affine open cover of `X`
> whose finite intersections are affine, and a family of chain-level comparisons
>
> `Θ(φ, square) : M ⊗_A A' ⟶ Č_alt(g⁻¹U, g^* F)`
>
> indexed by a ring map `φ : A ⟶ A'` and a cartesian square exhibiting `X'` as the base change of
> `X` along `Spec A' ⟶ Spec A`, together with a family of identifications
>
> `c(φ, square, i) : Hⁱ(X', g^* F) ≅ Hⁱ(M ⊗_A A')`
>
> indexed also by the degree, such that
>
> * every `Θ(φ, square)` is a quasi-isomorphism;
> * `c(φ, square, i)` is the identification `Θ(φ, square)` induces on homology, so the family has a
>   single origin over `A` and is not a choice per `A'`;
> * **the comparisons are functorial in `A'`**: for a second ring map `ψ : A' ⟶ A''` and a second
>   cartesian square, the extension of scalars along `ψ` of `Θ(φ, square)`, followed by the Čech
>   base-change isomorphism for `ψ` and by the identification of the model of `g'^* (g^* F)` with
>   that of `(g' ≫ g)^* F`, is `Θ(ψ ∘ φ, pasted square)` read through
>   `(M ⊗_A A') ⊗_{A'} A'' ≅ M ⊗_A A''`.
>
> The conditions are exactly the source's. Separatedness and quasi-coherence follow:
> properness gives the first and coherence the second. The cover is not an input either — it is
> bound inside the existential and produced by `exists_finiteAffineCover_of_isProper` — so the
> statement is about `f` and `F` alone.
>
> The source's closing sentence, that flatness of `F` over `A` is essential with a reference to
> Hartshorne, has been ruled remark-level: it is a citation rather than a clause owing a theorem,
> and the module docstring records it as such.

```lean
theorem exists_finiteProjectiveModel_homology_iso_functorial [IsNoetherianRing A] [IsProper f]
    [F.IsCoherent] (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    haveI : F.IsQuasicoherent := isQuasicoherent_of_isCoherent F
    ∃ (M : CochainComplex (ModuleCat.{u} A) ℤ) (a b : ℤ),
      M.IsStrictlyGE a ∧ M.IsStrictlyLE b ∧
        (∀ i : ℤ, Module.Finite A (M.X i)) ∧ (∀ i : ℤ, Module.Projective A (M.X i)) ∧
        ∃ (I : Type u) (hIfin : Finite I) (hIlin : LinearOrder I) (U : I → X.Opens)
          (hU : (⊤ : X.Opens) = ⨆ i, U i) (hUaff : ∀ i, IsAffineOpen (U i)),
          haveI : Finite I := hIfin
          letI : LinearOrder I := hIlin
          ∃ (_haff : ∀ (r : ℕ) (s : Fin (r + 1) → I), IsAffineOpen (⨅ k, U (s k)))
            (Θ : ∀ {A' : Type u} [CommRing A'] (φ : A →+* A') {X' : Scheme.{u}}
                {f' : X' ⟶ Spec (.of A')} {g : X' ⟶ X},
                IsPullback g f' f (Spec.map (CommRingCat.ofHom φ)) →
                  (extendScalarsComplex φ M ⟶
                    baseAlternatingCechComplex f' (fun j => g ⁻¹ᵁ U j)
                      (top_eq_iSup_preimage g U hU) ((Scheme.Modules.pullback g).obj F)))
            (c : ∀ {A' : Type u} [CommRing A'] (φ : A →+* A') {X' : Scheme.{u}}
                {f' : X' ⟶ Spec (.of A')} {g : X' ⟶ X}
                (_hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ))) (i : ℤ),
                ((DerivedCategory.homologyFunctor (ModuleCat.{u} A') i).obj
                    (derivedGlobalSectionsOverBase f' ((Scheme.Modules.pullback g).obj F)) ≅
                  (extendScalarsComplex φ M).homology i)),
            (∀ {A' : Type u} [CommRing A'] (φ : A →+* A') {X' : Scheme.{u}}
                {f' : X' ⟶ Spec (.of A')} {g : X' ⟶ X}
                (hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ))),
                QuasiIso (Θ φ hsq)) ∧
              (∀ {A' : Type u} [CommRing A'] (φ : A →+* A') {X' : Scheme.{u}}
                  {f' : X' ⟶ Spec (.of A')} {g : X' ⟶ X}
                  (hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ))) (i : ℤ),
                  (c φ hsq i).inv =
                    (DerivedCategory.homologyFunctorFactors (ModuleCat.{u} A') i).inv.app
                        (extendScalarsComplex φ M) ≫
                      (DerivedCategory.homologyFunctor (ModuleCat.{u} A') i).map
                        (DerivedCategory.Q.map (Θ φ hsq) ≫
                          (alternatingCechIsoDerivedGlobalSectionsOverBase f'
                            (fun j => g ⁻¹ᵁ U j) (top_eq_iSup_preimage g U hU)
                            ((Scheme.Modules.pullback g).obj F)
                            (iInf_preimage_isAffineOpen φ hsq U hUaff)).hom)) ∧
              (∀ {A' A'' : Type u} [CommRing A'] [CommRing A''] (φ : A →+* A') (ψ : A' →+* A'')
                  {X' X'' : Scheme.{u}} {f' : X' ⟶ Spec (.of A')} {f'' : X'' ⟶ Spec (.of A'')}
                  {g : X' ⟶ X} {g' : X'' ⟶ X'}
                  (hsq : IsPullback g f' f (Spec.map (CommRingCat.ofHom φ)))
                  (hsq' : IsPullback g' f'' f' (Spec.map (CommRingCat.ofHom ψ))),
                  haveI : IsSeparated f' := isSeparated_of_isPullback φ hsq
                  ((ModuleCat.extendScalars.{u, u, u} ψ).mapHomologicalComplex
                          (ComplexShape.up ℤ)).map (Θ φ hsq) ≫
                      (baseAlternatingCechComplexBaseChangeIso ψ hsq'
                          ((Scheme.Modules.pullback g).obj F) (fun j => g ⁻¹ᵁ U j)
                          (top_eq_iSup_preimage g U hU)
                          (isAffineOpen_preimage φ hsq U hUaff)).hom ≫
                      (baseAlternatingCechComplexMapIso f'' (fun j => (g' ≫ g) ⁻¹ᵁ U j)
                        (top_eq_iSup_preimage (g' ≫ g) U hU)
                        ((Scheme.Modules.pullbackComp g' g).app F)).hom =
                    (extendScalarsComplexCompIso φ ψ).hom.app M ≫
                      Θ (ψ.comp φ)
                        (Stacks.Cech.isPullback_comp_specMap φ ψ f f' f'' g g' hsq hsq'))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.22, Tag 07VJ](https://stacks.math.columbia.edu/tag/07VJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
