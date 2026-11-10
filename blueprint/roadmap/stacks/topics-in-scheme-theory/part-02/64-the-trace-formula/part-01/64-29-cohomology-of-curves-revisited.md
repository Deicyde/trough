---
declaration: section
origin: cited
lean: AlgebraicGeometry.compactSupportCanonicalTwistEquiv_galois, Stacks.EtaleCohomology.compactlySupportedCohomologyTwo_galoisIso_tateTwistCoinvariants, AlgebraicGeometry.isZero_curveCompactlySupportedCohomologyZero_of_not_isProjective, AlgebraicGeometry.geometricGlobalSectionsInvariantsEquiv, AlgebraicGeometry.geometricGlobalSectionsInvariantsEquiv_naturality, AlgebraicGeometry.geometricGlobalSectionsInvariantsEquiv_galois, Stacks.EtaleCohomology.LAdicSheaf.subsingleton_rationalGeometricCompactlySupportedCohomology_zero_of_not_isProper, Stacks.EtaleCohomology.compactlySupportedSections_eq_bot_of_not_isProper
statement: formalized
proof: formalized
---

# 64.29 Cohomology of curves, revisited

Section 64.29 of the Stacks Project, [Tag 03VJ](https://stacks.math.columbia.edu/tag/03VJ). 3 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03VK, a lemma

[Tag 03VK](https://stacks.math.columbia.edu/tag/03VK) in the Stacks Project.

**`AlgebraicGeometry.compactSupportCanonicalTwistEquiv_galois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCanonicalTwistGalois.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportCanonicalTwistGalois.lean#L315).

> **`H²_c(X_k̄, ℱ_ρ) = M_{π₁(X_k̄, η̄)}(-1)` canonically, as `Gal(k^{sep}/k)`-modules.**
> Let `X` be a geometrically connected smooth curve over a field `k` (`f : X ⟶ Spec k`), `k̄` an
> algebraic closure of `k`, `Λ` a finite ring with `n = #Λ` invertible (in `k̄`, equivalently in
> `k`), `η̄` a geometric point of `X_k̄`, and `ℱ_ρ` the sheaf on `X_étale` attached to a finite
> `Λ`-module `M` with a continuous action `ρ` of `π₁(X, η̄)`
> (`AlgebraicGeometry.representationSheaf`). The canonical `Λ`-linear isomorphism
> `Ψ = AlgebraicGeometry.compactSupportCanonicalTwistEquiv : H²_c(X_k̄, ℱ_ρ) ≃ Hom(μ_n(k̄), M_N)`
> carries the action of every `σ ∈ Aut_k(k̄)` on `H²_c` (induced by `id × Spec σ`) to the action
> `g ↦ σ ∘ g ∘ σ⁻¹` on `Hom(μ_n(k̄), M_N) = M_N(-1)`
> (`Stacks.EtaleCohomology.rootsOfUnityHomRepresentation`).
>
> Here `M_N` is the module of `ρ_N = AlgebraicGeometry.geometricNormalCoinvariants`, which is on the
> nose the coinvariants of `M` under the image `N` of `π₁(X_k̄, η̄)` in `π₁(X, η̄)`
> (`AlgebraicGeometry.geometricNormalCoinvariantsEquiv`), that is `M_{π₁(X_k̄, η̄)}`
> (`AlgebraicGeometry.geometricCoinvariantsRangeEquiv`); `σ` acts on it through
> `π₁(X, η̄)/N ≅ Aut_k(k̄)` (`AlgebraicGeometry.geometricNormalCoinvariantsGaloisRepresentation`,
> which is `AlgebraicGeometry.geometricCoinvariantsGaloisRepresentation` on the coinvariants by
> `AlgebraicGeometry.geometricNormalCoinvariantsEquiv_galoisRepresentation`). `Hom(μ_n(k̄), M_N)`
> with this action is the Tate twist `M_N(-1)`: evaluation at any primitive `n`-th root of unity
> turns it into `σ ↦ χ_cycl(σ)⁻¹ σ`
> (`Stacks.EtaleCohomology.rootsOfUnityHomRepresentation_apply_ofMul`, into
> `Stacks.EtaleCohomology.tateTwistNegOne`).
>
> Conventions: `Aut_k(k̄) ≅ Gal(k^{sep}/k)` by restriction
> (`AlgebraicGeometry.separableClosureRestrictMulEquiv`); `H²_c` is that of Remark 03UI (2),
> `RΓ(X̄_k̄, (j_! ℱ)|_{X̄_k̄})` for a compactification `j : X ⟶ X̄` over `k`, independent of `j`
> (`geometricCompactSupportGroupCanonicalComparison`, Tag 03UI); `Λ : Type`, a finite ring being
> isomorphic to one in `Type`.
>
> Canonicity: `Ψ` is the source's own reformulation (Deligne), `H²_c` of the largest quotient
> `ℱ_ρ ⟶ ℱ_{ρ_N}` constant on `X_k̄` followed by the trace on the smooth projective model of `X_k̄`
> and evaluation at `η̄`; its values involve no choice, in particular no root of unity
> (`AlgebraicGeometry.compactSupportCanonicalTwistEquiv_apply_ofMul`). The isomorphism `θ` of
> `AlgebraicGeometry.compactSupportGeometricCoinvariantsMap` (and
> `AlgebraicGeometry.compactSupportGaloisTwistEquiv` built on it) is not used: it goes through
> `AlgebraicGeometry.representationSheafPullbackIso`, a *chosen* isomorphism
> `ℱ_ρ|_{X_k̄} ≅ ℱ_{ρ|π₁(X_k̄)}` (Tag 0DV6 only gives its existence). Two choices differ by a
> natural automorphism of restriction to `π₁(X_k̄)`, such as `ρ(c)` for `c` centralising the image
> of `π₁(X_k̄)`, which changes `θ` by the action of `c` on `M_π`; so Galois equivariance holds for
> `θ` only for suitable choices and cannot be proved for `θ` as defined.

```lean
theorem compactSupportCanonicalTwistEquiv_galois (σ : kbar ≃ₐ[k] kbar)
    (ρ : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{0, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f kbar
          (contains_fieldBaseChange_of_isCurve B X f kbar)).hom)))
    (x : letI := connectedSpace_of_isCurve B X f
      galoisCompactSupportCohomologyGroup.{u, 0} Λ f j kbar
        ((Stacks.DerivedIndexing.singlePlusFunctor _ 0).obj
          ((representationSheaf B X _ Λ).obj ρ)) ((2 : ℕ) : ℤ)) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f kbar
    compactSupportCanonicalTwistEquiv B X f kbar Λ y j hn ρ
        ((galoisCompactSupportGroupAction Λ f j kbar σ
          ((Stacks.DerivedIndexing.singlePlusFunctor _ 0).obj
            ((representationSheaf B X _ Λ).obj ρ)) ((2 : ℕ) : ℤ)).hom x) =
      rootsOfUnityHomRepresentation k kbar (Fintype.card Λ) Λ
        (geometricNormalCoinvariantsGaloisRepresentation B X f kbar Λ y ρ) σ
        (compactSupportCanonicalTwistEquiv B X f kbar Λ y j hn ρ x)
```

**`Stacks.EtaleCohomology.compactlySupportedCohomologyTwo_galoisIso_tateTwistCoinvariants`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportTateTwistCoinvariants.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportTateTwistCoinvariants.lean#L472). The attribute's comment: “the Galois-module conclusion, obtained from an equivariant nondegenerate pairing with μ\_n coefficients. The right-hand side (M)\_\{π₁(X\_k̄,η̄)}(-1) is constructed: coinvariants of Tag 03UD for the geometric fundamental group, the residual Gal(k^sep/k)-action through the fundamental exact sequence, and the Tate twist by -1 as the source defines it, χ\_cycl(σ)⁻¹ composed with σ; the left-hand side is H²\_c of Tag 0GJZ. Four inputs are explicit hypotheses because this library has no statement for them: the sheaf ℱ\_ρ attached to ρ, which is Tag 0DV5 part (1), that is Tag 03RV and hence Tag 0245, so the sheaf is a variable and its link to ρ is carried by the pairing; the Galois action on H²\_c and its compatibility, Tag 03ST in degree two and Tag 03Q9, of which only degree zero is available here; the fundamental exact sequence, Tags 03VJ, 0BTX and 0BNE, carried by the normal subgroup N and the isomorphism φ; and the trace isomorphism H²\_c(X\_k̄, μ\_n) = ℤ/nℤ quoted inside the source's proof, carried by the nondegeneracy of the pairing. Tag 0F7I being absent, the compactification is an explicit argument as in Tag 0GJZ, and Xbar is pinned as the base change X ×\_k k^sep by hbase. What is proved is that these inputs produce the twisted equivariant isomorphism: the Tate twist and the Galois equivariance of the identification”.

> **Stacks Project, Tag 03VK, as an isomorphism of `Gal(k^{sep}/k)`-modules.**
>
> The right-hand side is built here: `Stacks.Trace.coinvariants` of the restriction of `ρ` to the
> geometric fundamental group `N`, carrying the residual Galois action of
> `Stacks.EtaleCohomology.galoisCoinvariantsRepresentation` through the fundamental exact sequence
> `φ`, Tate-twisted by `-1` as the source defines the twist.  The left-hand side is the compactly
> supported cohomology module of Tag 0GJZ in degree two, carrying the Galois action `galois`.
>
> The geometric input is a pairing of `H²_c` with the `n`-th roots of unity, taking values in the
> coinvariants, equivariant for the Galois actions on all three of its arguments and nondegenerate
> at one root of unity `ζ₀`.  That is the shape in which the source supplies it: the twist in the
> conclusion is not assumed anywhere, it comes out of the computation of the Galois action on
> `μ_n`, which is the cyclotomic character.  See the module docstring for the inputs carried as
> hypotheses and the tags they belong to.
>
> `hbase` pins `Xbar` as the geometric curve `X_{k̄} = X ×_k k^{sep}`, so that the cohomology on
> the left is that of the base change and not of an unrelated scheme over `k^{sep}`; both the
> projection `gbar` and the structure morphism `fbar` are determined by that one isomorphism, so
> neither is an unconstrained choice.  The identification itself plays no part in the twist
> bookkeeping, which is why the proof only destructures it.

```lean
public theorem compactlySupportedCohomologyTwo_galoisIso_tateTwistCoinvariants
    [LocallyOfFiniteType fbar] [QuasiCompact fbar] [IsSeparated fbar]
    [IsCurve k fX] [Smooth fX] [GeometricallyConnected fX]
    (gbar : Xbar ⟶ X)
    (hbase : ∃ e : Xbar ≅ pullback fX (Spec.map (CommRingCat.ofHom (algebraMap k ksep))),
      gbar = e.hom ≫ pullback.fst fX (Spec.map (CommRingCat.ofHom (algebraMap k ksep))) ∧
        fbar = e.hom ≫ pullback.snd fX (Spec.map (CommRingCat.ofHom (algebraMap k ksep))))
    (etabar : AlgebraicGeometry.GeometricPoint X)
    (ρ : Representation Λ (EtaleFundamentalGroup X etabar) M)
    (N : Subgroup (EtaleFundamentalGroup X etabar)) [N.Normal]
    (φ : EtaleFundamentalGroup X etabar ⧸ N ≃* (ksep ≃ₐ[k] ksep))
    (galois : Representation Λ (ksep ≃ₐ[k] ksep)
      (compactlySupportedCohomologyTwo.{u, r} ksep fbar jbar Λ F))
    (pair : Additive (rootsOfUnity n ksep) →+
      (compactlySupportedCohomologyTwo.{u, r} ksep fbar jbar Λ F →ₗ[Λ]
        Stacks.Trace.coinvariants (ρ.comp N.subtype)))
    (hpair : ∀ (σ : ksep ≃ₐ[k] ksep) (ζ : rootsOfUnity n ksep)
        (x : compactlySupportedCohomologyTwo.{u, r} ksep fbar jbar Λ F),
      pair (Additive.ofMul (galoisRootsOfUnity k ksep n σ ζ)) (galois σ x) =
        galoisCoinvariantsRepresentation ρ N φ σ (pair (Additive.ofMul ζ) x))
    (ζ₀ : rootsOfUnity n ksep)
    (hζ₀ : Function.Bijective (pair (Additive.ofMul ζ₀))) :
    ∃ θ : compactlySupportedCohomologyTwo.{u, r} ksep fbar jbar Λ F ≃ₗ[Λ]
        Stacks.Trace.coinvariants (ρ.comp N.subtype),
      ∀ (σ : ksep ≃ₐ[k] ksep)
        (x : compactlySupportedCohomologyTwo.{u, r} ksep fbar jbar Λ F),
        θ (galois σ x) =
          tateTwistNegOne k ksep n Λ (galoisCoinvariantsRepresentation ρ N φ) σ (θ x)
```

## Tag 03VL, a remark

[Tag 03VL](https://stacks.math.columbia.edu/tag/03VL) in the Stacks Project.

**`AlgebraicGeometry.isZero_curveCompactlySupportedCohomologyZero_of_not_isProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveRepresentationCohomology.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveRepresentationCohomology.lean#L130). The attribute's comment: “H⁰\_c(X\_k̄, ℱ\_ρ) = 0 if X is not projective, H\_c in the sense of Tag 0GJZ, for every algebraic extension K of k in place of k̄”. References: SGA 5 VII (7.1.1), “b), special case”.

> **Stacks Project, Tag 03VL, last assertion: `H⁰_c(X_K, ℱ_ρ) = 0` if `X` is not
> projective.** For a geometrically connected smooth curve `X` over `k` which is not projective,
> an algebraic extension `K` of `k`, a finite ring `Λ` and a finite `Λ`-module `M` with a continuous
> action `ρ` of `π₁(X, η̄)`, the zeroth compactly supported cohomology module, in the sense of
> Tag 0GJZ, of the restriction of `ℱ_ρ` to `X_K` vanishes, through any compactification of `X_K`
> over `K`.

```lean
theorem isZero_curveCompactlySupportedCohomologyZero_of_not_isProjective
    (hnp : ¬ IsProjective f)
    (jbar : CompactificationOf (Over.mk (pullback.snd (Over.mk f).hom (specAlgebraMap k K))))
    (y : GeometricPoint (fieldBaseChange (Over.mk f) K))
    (M : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{r, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f K
          (contains_fieldBaseChange_of_isCurve B X f K)).hom))) :
    letI := connectedSpace_of_isCurve B X f
    IsZero ((compactlySupportedCohomologyGroup.{u, r} K
        (pullback.snd (Over.mk f).hom (specAlgebraMap k K)) jbar Λ 0).obj
      ((DerivedCategory.Plus.singleFunctor
        (EtaleModules.{u, r} Λ (fieldBaseChange (Over.mk f) K)) 0).obj
          ((geometricRepresentationSheaf B X
            (y.map (fieldBaseChangeObjProj B X f K
              (contains_fieldBaseChange_of_isCurve B X f K)).hom) Λ f K).obj M)))
```

**`AlgebraicGeometry.geometricGlobalSectionsInvariantsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricGlobalSectionsCanonical.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricGlobalSectionsCanonical.lean#L294). The attribute's comment: “H⁰(X\_k̄, ℱ\_ρ) = M^\{π₁(X\_k̄,η̄)}: the canonical identification, by evaluation at η̄”.

> **Stacks Project, Tag 03VL, degree zero, canonically: `H⁰(X_k̄, ℱ_ρ) = M^{π₁(X_k̄, η̄)}`.** The
> evaluation at the geometric point `η̄` of `X_k̄` identifies the global sections of the restriction
> of `ℱ_ρ` to `X_k̄` with the `π₁(X_k̄, η̄)`-invariants of `M`. It involves no choice: it is built
> from the explicit sheaf `ℱ_ρ` of Tag 0DV5 and evaluation, not from the existence-only comparison
> of Tag 0DV6. Its naturality in `ρ` is `geometricGlobalSectionsInvariantsEquiv_naturality` and its
> Galois equivariance `geometricGlobalSectionsInvariantsEquiv_galois`. The source states this for `X`
> projective and `#Λ ∈ k^*`; neither is used.

```lean
def geometricGlobalSectionsInvariantsEquiv (ρ : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{0, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f kbar
          (contains_fieldBaseChange_of_isCurve B X f kbar)).hom))) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f kbar
    ↑((etaleModuleGlobalSections.{u, 0} Λ (fieldBaseChange (Over.mk f) kbar)).obj
        (geometricRepresentationRestriction B X f kbar Λ y ρ)) ≃ₗ[Λ]
      ↑((finiteTypeContinuousModuleInvariants Λ
        (EtaleFundamentalGroup (fieldBaseChange (Over.mk f) kbar) y)).obj
          ((finiteTypeContinuousModuleRes Λ (etaleFundamentalGroupMap
            (fieldBaseChangeObjProj B X f kbar (contains_fieldBaseChange_of_isCurve B X f kbar)).hom
              y)).obj ρ))
```

**`AlgebraicGeometry.geometricGlobalSectionsInvariantsEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricGlobalSectionsCanonical.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricGlobalSectionsCanonical.lean#L326). The attribute's comment: “H⁰(X\_k̄, ℱ\_ρ) = M^\{π₁(X\_k̄,η̄)} functorially in ρ”.

> **Stacks Project, Tag 03VL, degree zero: the identification is natural in `ρ`.** For
> `φ : ρ ⟶ ρ'`, it carries the map induced by `φ` on global sections to `φ` on invariants.

```lean
theorem geometricGlobalSectionsInvariantsEquiv_naturality
    {ρ ρ' : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{0, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f kbar
          (contains_fieldBaseChange_of_isCurve B X f kbar)).hom))} (φ : ρ ⟶ ρ')
    (z : letI := connectedSpace_of_isCurve B X f
      ↑((etaleModuleGlobalSections.{u, 0} Λ (fieldBaseChange (Over.mk f) kbar)).obj
        (geometricRepresentationRestriction B X f kbar Λ y ρ))) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f kbar
    (geometricGlobalSectionsInvariantsEquiv B X f kbar Λ y ρ'
        ((etaleModuleGlobalSections.{u, 0} Λ (fieldBaseChange (Over.mk f) kbar)).map
          ((etaleModuleInverseImage.{u, 0} Λ (fieldBaseChangeProj (Over.mk f) kbar)).map
            ((representationSheaf B X (y.map (fieldBaseChangeObjProj B X f kbar
              (contains_fieldBaseChange_of_isCurve B X f kbar)).hom) Λ).map φ)) z)).1 =
      φ.hom.hom.hom.hom.hom (geometricGlobalSectionsInvariantsEquiv B X f kbar Λ y ρ z).1
```

**`AlgebraicGeometry.geometricGlobalSectionsInvariantsEquiv_galois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricGlobalSectionsCanonical.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricGlobalSectionsCanonical.lean#L350). The attribute's comment: “H⁰(X\_k̄, ℱ\_ρ) = M^\{π₁(X\_k̄,η̄)} as Gal(k̄/k) = π₁(X,η̄)/π₁(X\_k̄,η̄)-modules”.

> **Stacks Project, Tag 03VL, degree zero: the identification is Galois-equivariant.** For
> `γ ∈ π₁(X, η̄)` with image `σ ∈ Aut(k̄/k) = π₁(X, η̄)/π₁(X_k̄, η̄)`, it carries the action of `σ`
> on `H⁰(X_k̄, ℱ_ρ)` (through `id × Spec σ` on `X_k̄`) to the action of `ρ(γ)` on
> `M^{π₁(X_k̄, η̄)}`.

```lean
theorem geometricGlobalSectionsInvariantsEquiv_galois (ρ : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{0, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f kbar
          (contains_fieldBaseChange_of_isCurve B X f kbar)).hom)))
    (γ : letI := connectedSpace_of_isCurve B X f
      EtaleFundamentalGroup X.1 (y.map (fieldBaseChangeObjProj B X f kbar
        (contains_fieldBaseChange_of_isCurve B X f kbar)).hom))
    (z : letI := connectedSpace_of_isCurve B X f
      ↑((etaleModuleGlobalSections.{u, 0} Λ (fieldBaseChange (Over.mk f) kbar)).obj
        (geometricRepresentationRestriction B X f kbar Λ y ρ))) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f kbar
    (geometricGlobalSectionsInvariantsEquiv B X f kbar Λ y ρ
        ((fieldBaseChangeGlobalSectionsGaloisAction Λ (Over.mk f) kbar
          (geometricQuotientGaloisEquiv B X f kbar y (QuotientGroup.mk γ)) _).hom z)).1 =
      (finiteTypeContinuousModuleRepresentation Λ _ ρ) γ
        (geometricGlobalSectionsInvariantsEquiv B X f kbar Λ y ρ z).1
```

**`Stacks.EtaleCohomology.LAdicSheaf.subsingleton_rationalGeometricCompactlySupportedCohomology_zero_of_not_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LisseCompactSupportZero.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LisseCompactSupportZero.lean#L201). The attribute's comment: “last assertion: H^0\_c(X\_kbar, F\_rho) = 0 when X is not projective (here: not proper over k)”.

> **Stacks Project, Tag 03VL, last assertion: if `X` is not projective, then
> `H⁰_c(X_k̄, ℱ_ρ) = 0`.** Here `X` is a smooth geometrically connected curve over the finite field
> `k`, `ρ = τ : π₁(X, x̄) → GL_r(Q_ℓ)` is continuous, `H⁰_c(X_k̄, ℱ_ρ)` is the compactly supported
> cohomology of `ℱ_τ ⊗ Q_ℓ` on `X_k̄` for an algebraic closure `k̄` (for any compactification), and
> "not projective" is `¬ IsProper f` (a projective curve is proper over `k`, so this is the weaker
> hypothesis). A connected smooth curve which is not proper is affine (Tag 0A28).

```lean
theorem LAdicSheaf.subsingleton_rationalGeometricCompactlySupportedCohomology_zero_of_not_isProper
    [ConnectedSpace X.1] [SmoothOfRelativeDimension 1 f] [IsAlgClosure k kbar]
    (hf : ¬ IsProper f) (x : GeometricPoint X.1) {r : ℕ}
    (τ : EtaleFundamentalGroup X.1 x →* GL (Fin r) ℚ_[ℓ]) (hτ : Continuous τ) :
    Subsingleton (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar
      (LAdicSheaf.representationSheaf B X x τ hτ) 0)
```

**`Stacks.EtaleCohomology.compactlySupportedSections_eq_bot_of_not_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LocallyConstantCompactSupport.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LocallyConstantCompactSupport.lean#L321). The attribute's comment: “the non-projective assertion H^0\_c = 0, at the level of the sections of proper support of Tag 0F72: for an arbitrary locally constant abelian sheaf in place of the sheaf ℱ\_ρ attached to a representation, which needs part (1) of Tag 0DV5 and hence Tag 0245, and on an integral scheme not proper over the base field in place of a non-projective geometrically connected smooth curve. The identification of these sections with H^0\_c is Tag 0GK1, not available here; the two projective assertions of the tag are not proved, nor is the Tate twist they carry”. References: SGA 4½ Sommes trig (1.18), “Clause b)”.

> On an integral scheme which is not proper over the base field, a global section of a locally
> constant abelian sheaf on the small étale site whose support is proper over the base field is
> zero.

```lean
public theorem compactlySupportedSections_eq_bot_of_not_isProper [IsIntegral X]
    (hf : ¬ IsProper f) [IsLocallyConstant (SmallEtale.topology B X hX) F] :
    compactlySupportedSections k X f B hX F = ⊥
```

**`AlgebraicGeometry.properCurveCompactSupportTwoEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/Remark03VL.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/Remark03VL.lean#L113). The attribute's comment: “H²\_c(X\_k̄, ℱ\_ρ) = M\_\{π₁(X\_k̄,η̄)}(-1) for X projective (here: proper): the root-of-unity free (ζ-independent) Λ-linear identification, M(-1) being Hom(μ\_n, M); functoriality in ρ is properCurveCompactSupportTwoEquiv\_naturality”.

> **Stacks Project, Tag 03VL, degree two: `H²_c(X_k̄, ℱ_ρ) = M_{π₁(X_k̄, η̄)}(-1)` for `X`
> projective.** For a geometrically connected smooth proper curve `X` over a field `k`, an
> algebraic closure `k̄`, a finite ring `Λ` with `#Λ` invertible, and a finite `Λ`-module `M` with a
> continuous action `ρ` of `π₁(X, η̄)`, the compactly supported cohomology `H²_c(X_k̄, ℱ_ρ)`, `X`
> being its own compactification, is `M_{π₁(X_k̄, η̄)}(-1) = Hom(μ_n(k̄), M_{π₁(X_k̄, η̄)})`,
> `n = #Λ`, with no choice of a root of unity. The source assumes `X` projective; a projective
> morphism is proper (`AlgebraicGeometry.isProper_of_isProjectiveMorphism`), and for a curve the two
> are equivalent (Tag 0A26), so properness is the hypothesis. Its functoriality in `ρ` is
> `AlgebraicGeometry.properCurveCompactSupportTwoEquiv_naturality`.

```lean
def properCurveCompactSupportTwoEquiv [IsProper f]
    (ρ : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{0, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f kbar
          (contains_fieldBaseChange_of_isCurve B X f kbar)).hom))) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f kbar
    galoisCompactSupportCohomologyGroup.{u, 0} Λ f (CompactificationOf.ofProper f) kbar
        ((Stacks.DerivedIndexing.singlePlusFunctor _ 0).obj
          ((representationSheaf B X _ Λ).obj ρ)) ((2 : ℕ) : ℤ) ≃ₗ[Λ]
      (Additive (_root_.rootsOfUnity (Fintype.card Λ) kbar) →+
        Stacks.Trace.coinvariants (geometricRepresentation B X f kbar Λ y ρ))
```

**`AlgebraicGeometry.properCurveCompactSupportTwoEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/Remark03VL.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/Remark03VL.lean#L131). The attribute's comment: “H²\_c(X\_k̄, ℱ\_ρ) = M\_\{π₁(X\_k̄,η̄)}(-1) is functorial in ρ”.

> **Stacks Project, Tag 03VL, degree two, functoriality in `ρ`.** For `v : ρ ⟶ ρ'`, the
> identification `H²_c(X_k̄, ℱ_ρ) = M_{π₁(X_k̄, η̄)}(-1)` carries the map induced by `v` on `H²_c` to
> the map induced by `v` on coinvariants.

```lean
theorem properCurveCompactSupportTwoEquiv_naturality [IsProper f]
    {ρ ρ' : letI := connectedSpace_of_isCurve B X f
      FiniteTypeContinuousModule.{0, u + 1, u + 1} Λ (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f kbar
          (contains_fieldBaseChange_of_isCurve B X f kbar)).hom))} (v : ρ ⟶ ρ')
    (x : letI := connectedSpace_of_isCurve B X f
      letI := connectedSpace_fieldBaseChange f kbar
      galoisCompactSupportCohomologyGroup.{u, 0} Λ f (CompactificationOf.ofProper f) kbar
        ((Stacks.DerivedIndexing.singlePlusFunctor _ 0).obj
          ((representationSheaf B X _ Λ).obj ρ)) ((2 : ℕ) : ℤ)) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f kbar
    properCurveCompactSupportTwoEquiv B X f kbar Λ y hn ρ'
        (((DerivedCategory.Plus.homologyFunctor (ModuleCat.{u + 1} Λ) ((2 : ℕ) : ℤ)).map
          (galoisCompactSupportCohomologyMap Λ f (CompactificationOf.ofProper f) kbar
            ((Stacks.DerivedIndexing.singlePlusFunctor _ 0).map
              ((representationSheaf B X _ Λ).map v)))).hom x) =
      (geometricCoinvariantsMap B X f kbar Λ y v).toAddMonoidHom.comp
        (properCurveCompactSupportTwoEquiv B X f kbar Λ y hn ρ x)
```

## Tag 03VM, a proposition

[Tag 03VM](https://stacks.math.columbia.edu/tag/03VM) in the Stacks Project.

**`AlgebraicGeometry.compactSupportDerivedHomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportDerivedHomologyIso.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportDerivedHomologyIso.lean#L163). The attribute's comment: “third assertion (the derived version of the homological half): `RΓ_c(X_k̄, ℱ_ρ) ≅ LH₀(π₁(X_k̄, η̄), M(-1))[-2]` in the derived category of `Λ[[Aut(k̄/k)]]`-modules, natural in `(M, ρ)`”.

> **Tag 03VM, homological derived clause: `RΓ_c(X_k̄, ℱ_ρ) ≅ LH₀(π₁(X_k̄, η̄), M(-1))[-2]`** in
> the derived category of `Λ[[Aut(k̄/k)]]`-modules (`Aut(k̄/k) ≅ Ẑ` for `k` finite), naturally in
> the finite `Λ`-module `M` with continuous action `ρ` of `π₁(X, η̄)`. Here `X` is a geometrically
> connected smooth curve over `k` with `X_k̄ ≇ 𝐏¹_k̄`, `k̄` is an algebraic closure of `k` separable
> over `k` (automatic for `k` finite), and `Λ` is a finite ring with `#Λ` invertible in `k`. The left
> side is the Galois-equivariant `RΓ_c` of Remark 03UI (2), `M(-1) = Hom(μ_n(k̄), M)`, and `LH₀` is
> the derived functor of the coinvariants in the continuous sense, `M ⊗^L_{Λ[[π₁(X_k̄)]]} Λ` computed
> on pseudocompact modules (see the module docstring).

```lean
def compactSupportDerivedHomologyIso (hΛ : IsUnit ((Nat.card Λ : ℕ) : k))
    (hP : ¬ ∃ e : fieldBaseChange (Over.mk f) K ≅ projectiveSpaceOver 1 (Spec (.of K)),
      e.hom ≫ (projectiveSpaceOver 1 (Spec (.of K)) ↘ Spec (.of K)) =
        pullback.snd (Over.mk f).hom (specAlgebraMap k K)) :
    letI := connectedSpace_of_isCurve B X f
    haveI : IsAlgClosed K := IsAlgClosure.isAlgClosed k
    haveI : Algebra.IsAlgebraic k K := IsAlgClosure.isAlgebraic
    geometricGaloisCompactSupportDerived B X f K y Λ j ≅
      (geometricTateTwist B X f K y Λ ⋙ geometricDerivedHomology B X f K y Λ) ⋙
        shiftFunctor _ (-2 : ℤ)
```

**`AlgebraicGeometry.compactSupportGroupHomologyTwistIsoOfNotIsoProjectiveLine`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportGroupHomologyGaloisNotProjectiveLine.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportGroupHomologyGaloisNotProjectiveLine.lean#L46). The attribute's comment: “second assertion: `H_c^{2-i}(X_k̄, ℱ_ρ) ≅ H_i(π₁(X_k̄, η̄), M)(-1)` as homological δ-functors in `(M, ρ)`”.

> When `X_k̄ ≇ ℙ¹_k̄`, the isomorphism `H_c^{2-i}(X_k̄, ℱ_ρ) ≅ H_i(π₁(X_k̄, η̄), M)(-1)` of
> homological δ-functors, extending the choice-free identification
> `H²_c(X_k̄, ℱ_ρ) = Hom(μ_n(k̄), M_{π₁(X_k̄, η̄)})` of Tag 03VK.

```lean
def compactSupportGroupHomologyTwistIsoOfNotIsoProjectiveLine :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f K
    haveI : IsAlgClosed K := IsAlgClosure.isAlgClosed k
    letI : Fintype Λ := Fintype.ofFinite Λ
    compactSupportRepresentationHomology B X
        (y.map (fieldBaseChangeObjProj B X f K (contains_fieldBaseChange_of_isCurve B X f K)).hom)
        Λ f j K ≅
      geometricGroupHomologyTwist B X f K Λ y (isUnit_card_fieldBaseChange K Λ hΛ)
```

**`AlgebraicGeometry.compactSupportGroupHomologyTwistIsoOfNotIsoProjectiveLine_galois`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportGroupHomologyGaloisNotProjectiveLine.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportGroupHomologyGaloisNotProjectiveLine.lean#L76). The attribute's comment: “second assertion, Galois action: the isomorphism `H_c^{2-i}(X_k̄, ℱ_ρ) ≅ H_i(π₁(X_k̄, η̄), M)(-1)` commutes with every `σ ∈ Aut_k(k̄)`”.

> The isomorphism `H_c^{2-i}(X_k̄, ℱ_ρ) ≅ H_i(π₁(X_k̄, η̄), M)(-1)` is
> `Gal(k^{sep}/k)`-equivariant: for every `σ ∈ Aut_k(k̄)` the action of `σ` on `H_c^{2-i}(X_k̄, ℱ_ρ)`
> (`AlgebraicGeometry.compactSupportRepresentationHomologyGalois`) corresponds, in every degree, to
> the action of `σ` on `H_i(π₁(X_k̄, η̄), M)(-1)`
> (`AlgebraicGeometry.geometricGroupHomologyTwistGalois`), which in degree zero is
> `f ↦ σ ∘ f ∘ σ⁻¹` on `Hom(μ_n(k̄), M_{π₁(X_k̄, η̄)})`.

```lean
theorem compactSupportGroupHomologyTwistIsoOfNotIsoProjectiveLine_galois (σ : K ≃ₐ[k] K) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f K
    letI := QuasiCompact.compactSpace_of_compactSpace f
    letI := quasiSeparatedSpace_of_quasiSeparated f
    haveI : IsAlgClosed K := IsAlgClosure.isAlgClosed k
    haveI : Algebra.IsAlgebraic k K := IsAlgClosure.isAlgebraic
    letI : Fintype Λ := Fintype.ofFinite Λ
    compactSupportRepresentationHomologyGalois B X
        (y.map (fieldBaseChangeObjProj B X f K (contains_fieldBaseChange_of_isCurve B X f K)).hom)
        Λ f j K σ ≫
        (compactSupportGroupHomologyTwistIsoOfNotIsoProjectiveLine B X f K Λ y j hΛ hP).hom =
      (compactSupportGroupHomologyTwistIsoOfNotIsoProjectiveLine B X f K Λ y j hΛ hP).hom ≫
        geometricGroupHomologyTwistGalois B X f K Λ y σ j (isUnit_card_fieldBaseChange K Λ hΛ)
          (isIso_geometricComparison_of_not_iso_projectiveLine B X f K Λᵐᵒᵖ y
            (isUnit_natCard_mulOpposite Λ hΛ) hP)
```

**`AlgebraicGeometry.isUniversal_compactSupportRepresentationHomology_of_not_iso_projectiveLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportGroupHomologyNotProjectiveLine.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CompactSupportGroupHomologyNotProjectiveLine.lean#L59). The attribute's comment: “first assertion: `(M, ρ) ↦ H_c^{2-i}(X_k̄, ℱ_ρ)` is a universal homological δ-functor, i.e. the left derived functors of `(M, ρ) ↦ H_c^2(X_k̄, ℱ_ρ)`”.

> **`(M, ρ) ↦ H_c^{2-i}(X_k̄, ℱ_ρ)` are the left derived functors of
> `(M, ρ) ↦ H_c^2(X_k̄, ℱ_ρ)`**: they form a universal homological δ-functor, for `X_k̄ ≇ ℙ¹_k̄` and
> `#Λ` invertible in `k`.

```lean
theorem isUniversal_compactSupportRepresentationHomology_of_not_iso_projectiveLine :
    letI := connectedSpace_of_isCurve B X f
    haveI : IsAlgClosed K := IsAlgClosure.isAlgClosed k
    (compactSupportRepresentationHomology B X
      (y.map (fieldBaseChangeObjProj B X f K (contains_fieldBaseChange_of_isCurve B X f K)).hom)
      Λ f j K).IsUniversal
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.deltaFunctorIsoLeftDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L146). The attribute's comment: “first assertion, by the source's own proof (both sides are universal δ-functors): a homological δ-functor whose positive degrees vanish on projectives IS the left derived functor of its degree-zero part. The compactly supported cohomology δ-functor `i ↦ H_c^{2-i}(X_k̄, F_ρ)` of the pair `(M, ρ)` is the hypothesis `Hc` and its vanishing on projectives the hypothesis `hvanish`, since the étale input (0GIY, 03QW, 0GK1, 03VL) is not available; no Tate twist is constructed”.

> **[Stacks, Tag 03VM], first assertion.**  A homological δ-functor `Hc` whose positive-degree
> parts vanish on projective objects, and whose degree-zero part is identified with the
> degree-zero left derived functor of an additive `T`, *is* the left derived functor of `T`: the
> identification extends uniquely to an isomorphism of homological δ-functors.
>
> In the source `Hc` is `i ↦ H_c^{2-i}(X_{k̄}, F_ρ)` on the category of pairs `(M, ρ)` and `T` is
> `(M, ρ) ↦ H_c^2(X_{k̄}, F_ρ)`; the proof is the source's, that both sides are universal
> δ-functors.

```lean
def deltaFunctorIsoLeftDerived (Hc : HomologicalDeltaFunctor A B) (T : A ⥤ B) [T.Additive]
    (hvanish : ∀ (n : ℕ) (P : A) [Projective P], IsZero ((Hc.functor (n + 1)).obj P))
    (base : Hc.functor 0 ≅ T.leftDerived 0) :
    Hc ≅ T.leftDerivedHomologicalDeltaFunctor
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoLeftDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L158). The attribute's comment: “first assertion read degreewise: `H_c^{2-i} ≅ L_i(H_c^2)`, with the compactly supported cohomology δ-functor and its vanishing on projectives as hypotheses”.

> **[Stacks, Tag 03VM], first assertion, degree by degree:** `Hcᵢ ≅ Lᵢ T`.

```lean
def isoLeftDerived (Hc : HomologicalDeltaFunctor A B) (T : A ⥤ B) [T.Additive]
    (hvanish : ∀ (n : ℕ) (P : A) [Projective P], IsZero ((Hc.functor (n + 1)).obj P))
    (base : Hc.functor 0 ≅ T.leftDerived 0) (i : ℕ) :
    Hc.functor i ≅ T.leftDerived i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoLeftDerivedOfRightExact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L172). The attribute's comment: “first assertion with a right exact degree-zero part: from `H_c^2 ≅ T` with `T` right exact, `H_c^{2-i} ≅ L_i T` for every `i`. The δ-functor and the vanishing on projectives are hypotheses”.

> **[Stacks, Tag 03VM], first assertion with the degree-zero hypothesis in its usable form.**
> When `T` is right exact — as `(M, ρ) ↦ H_c^2(X_{k̄}, F_ρ)` is, being the final term of the long
> exact sequence — the degree-zero input is an identification `Hc₀ ≅ T` itself, because
> `L₀ T ≅ T`.

```lean
def isoLeftDerivedOfRightExact (Hc : HomologicalDeltaFunctor A B) (T : A ⥤ B) [T.Additive]
    [PreservesFiniteColimits T]
    (hvanish : ∀ (n : ℕ) (P : A) [Projective P], IsZero ((Hc.functor (n + 1)).obj P))
    (base : Hc.functor 0 ≅ T) (i : ℕ) :
    Hc.functor i ≅ T.leftDerived i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.compactSupportIsoGroupHomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L193). The attribute's comment: “second assertion: two homological δ-functors that both vanish on projectives in positive degree and agree in degree zero agree in every degree, which is the source's proof of `H_c^{2-i} = H_i(π₁(X_k̄, η̄), M)(-1)`. The twisted group homology side is the hypothesis `Hgp` (group homology of a profinite group is the absent homological half of 03VI, and no Tate twist is formalized) and the degree-zero base case is the hypothesis `base` (03VK)”.

> **[Stacks, Tag 03VM], second assertion.**  Two homological δ-functors whose positive-degree
> parts vanish on projective objects and whose degree-zero parts are identified are identified in
> every degree.
>
> This is the "so" of the proposition: with `Hc` the compactly supported cohomology
> `i ↦ H_c^{2-i}(X_{k̄}, F_ρ)`, with `Hgp` the twisted group homology
> `i ↦ H_i(π₁(X_{k̄}, η̄), M)(-1)`, and with `base` the isomorphism of [Stacks, Tag 03VK], both
> sides are universal δ-functors and therefore agree in all degrees.  Neither side is constructed
> here — see the module docstring.

```lean
def compactSupportIsoGroupHomology (Hc Hgp : HomologicalDeltaFunctor A B)
    (hHc : ∀ (n : ℕ) (P : A) [Projective P], IsZero ((Hc.functor (n + 1)).obj P))
    (hHgp : ∀ (n : ℕ) (P : A) [Projective P], IsZero ((Hgp.functor (n + 1)).obj P))
    (base : Hc.functor 0 ≅ Hgp.functor 0) (i : ℕ) :
    Hc.functor i ≅ Hgp.functor i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.deltaFunctorIsoRightDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L231). The attribute's comment: “fourth assertion, by the source's own proof: a cohomological δ-functor whose positive degrees vanish on injectives IS the right derived functor of its degree-zero part, so `H^i(X_k̄, F_ρ) = H^i(π₁(X_k̄, η̄), M)`. The étale δ-functor `Het` and its vanishing on injectives are hypotheses, since the étale input 0GIY is not available”.

> **[Stacks, Tag 03VM], fourth assertion.**  A cohomological δ-functor `Het` whose
> positive-degree parts vanish on injective objects, and whose degree-zero part is identified
> with the degree-zero right derived functor of an additive `T`, *is* the right derived functor of
> `T`.
>
> In the source `Het` is `i ↦ H^i(X_{k̄}, F_ρ)` on the category of pairs `(M, ρ)` and `T` is
> `(M, ρ) ↦ M^{π₁(X_{k̄}, η̄)}`.

```lean
def deltaFunctorIsoRightDerived (Het : DeltaFunctor A B) (T : A ⥤ B) [T.Additive]
    (hvanish : ∀ (n : ℕ) (I : A) [Injective I], IsZero ((Het.functor (n + 1)).obj I))
    (base : Het.functor 0 ≅ T.rightDerived 0) :
    Het ≅ Stacks.DerivedIndexing.rightDerivedDeltaFunctorOfEnoughInjectives T
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoRightDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L245). The attribute's comment: “fourth assertion read degreewise: `H^i(X_k̄, F_ρ) ≅ R^i(M ↦ M^{π₁})`, with the étale δ-functor and its vanishing on injectives as hypotheses”.

> **[Stacks, Tag 03VM], fourth assertion, degree by degree:** `Hetⁱ ≅ R ⁱT`.

```lean
def isoRightDerived (Het : DeltaFunctor A B) (T : A ⥤ B) [T.Additive]
    (hvanish : ∀ (n : ℕ) (I : A) [Injective I], IsZero ((Het.functor (n + 1)).obj I))
    (base : Het.functor 0 ≅ T.rightDerived 0) (i : ℕ) :
    Het.functor i ≅ T.rightDerived i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoRightDerivedOfLeftExact`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L259). The attribute's comment: “fourth assertion with a left exact degree-zero part: from `H^0(X_k̄, F_ρ) ≅ T` with `T` left exact (invariants), `H^i(X_k̄, F_ρ) ≅ R^i T` for every `i`. The étale δ-functor and its vanishing on injectives are hypotheses”.

> **[Stacks, Tag 03VM], fourth assertion with the degree-zero hypothesis in its usable form.**
> When `T` is left exact — as `M ↦ M^{π₁(X_{k̄}, η̄)}` is — the degree-zero input is an
> identification `Het₀ ≅ T` itself, because `R ⁰T ≅ T`.

```lean
def isoRightDerivedOfLeftExact (Het : DeltaFunctor A B) (T : A ⥤ B) [T.Additive]
    [PreservesFiniteLimits T]
    (hvanish : ∀ (n : ℕ) (I : A) [Injective I], IsZero ((Het.functor (n + 1)).obj I))
    (base : Het.functor 0 ≅ T) (i : ℕ) :
    Het.functor i ≅ T.rightDerived i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoContinuousGroupCohomologyRightDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L293). The attribute's comment: “fourth assertion with the group-cohomology side CONCRETE: for a cohomological δ-functor on discrete continuous `G`-modules vanishing on injectives in positive degree and agreeing with `R^0` of invariants in degree zero, every degree agrees with the right derived functors of invariants, i.e. with the continuous group cohomology `H^i(G, M)` of 04JR. The étale δ-functor is still a hypothesis (0GIY is not available)”. References: SGA 3 I (5.2.1), “special case”.

> **[Stacks, Tag 03VM], fourth assertion with the group side concrete.**  A cohomological
> δ-functor on discrete continuous `G`-modules whose positive degrees vanish on injectives and
> whose degree-zero part is `H⁰` of the invariants functor agrees, in every degree, with the
> higher right derived functors of invariants — the continuous group cohomology `H^i(G, M)` of
> [Stacks, Tag 04JR].
>
> Taking `G = π₁(X_{k̄}, η̄)` and the δ-functor `i ↦ H^i(X_{k̄}, F_ρ)`, this is the fourth
> assertion of [Stacks, Tag 03VM].

```lean
def isoContinuousGroupCohomologyRightDerived
    (Het : DeltaFunctor (ContinuousGModule.{u, max u v} G) AddCommGrpCat.{max u v})
    (hvanish : ∀ (n : ℕ) (I : ContinuousGModule.{u, max u v} G) [Injective I],
      IsZero ((Het.functor (n + 1)).obj I))
    (base : Het.functor 0 ≅ (continuousGModuleInvariants.{u, max u v} G).rightDerived 0)
    (i : ℕ) :
    Het.functor i ≅ (continuousGModuleInvariants.{u, max u v} G).rightDerived i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoContinuousGroupCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L310). The attribute's comment: “fourth assertion with the right-hand side spelled as the continuous group cohomology functor of 04JR itself. The étale δ-functor and its vanishing on injectives are hypotheses”. References: SGA 3 I (5.2.1), “special case”.

> **[Stacks, Tag 03VM], fourth assertion against `Stacks.continuousGroupCohomologyFunctor`.**
> The same identification, with the right-hand side spelled as the cohomology functor of
> [Stacks, Tag 04JR] (`CategoryTheory.Functor.rightDerivedPlus` of invariants) rather than as
> Mathlib's `ℕ`-indexed `CategoryTheory.Functor.rightDerived`; the two agree by
> `Stacks.DerivedIndexing.rightDerivedIso`.

```lean
def isoContinuousGroupCohomology
    (Het : DeltaFunctor (ContinuousGModule.{u, max u v} G) AddCommGrpCat.{max u v})
    (hvanish : ∀ (n : ℕ) (I : ContinuousGModule.{u, max u v} G) [Injective I],
      IsZero ((Het.functor (n + 1)).obj I))
    (base : Het.functor 0 ≅ (continuousGModuleInvariants.{u, max u v} G).rightDerived 0)
    (i : ℕ) :
    Het.functor i ≅ continuousGroupCohomologyFunctor.{u, v} G i
```

**`Stacks.EtaleCohomology.CurveFundamentalGroup.isoContinuousGroupCohomologyOfInvariants`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/CurveFundamentalGroupCohomology.lean#L336). The attribute's comment: “fourth assertion with BOTH sides in the source's own form: from `H^0(X_k̄, F_ρ) ≅ M^{π₁}` (the invariants functor itself) the étale δ-functor agrees in every degree with the continuous group cohomology `H^i(G, M)` of 04JR. Left exactness of the invariants functor is an instance hypothesis — true, but Mathlib gives no `PreservesFiniteLimits` instance for a full-subcategory inclusion — and the étale δ-functor with its vanishing on injectives is a hypothesis (0GIY is not available)”.

> **[Stacks, Tag 03VM], fourth assertion with both sides in the source's own form.**  From the
> degree-zero identification `H^0(X_{k̄}, F_ρ) ≅ M^{π₁(X_{k̄}, η̄)}` — invariants themselves, not
> `R ⁰` of invariants — the étale δ-functor agrees in every degree with the continuous group
> cohomology `H^i(G, M)` of [Stacks, Tag 04JR].
>
> Left exactness of `Stacks.continuousGModuleInvariants` is an instance *hypothesis*: it is true
> (invariants are a right adjoint, and the two full-subcategory inclusions involved are exact),
> but `CategoryTheory.ObjectProperty.ι` carries no `PreservesFiniteLimits` instance in Mathlib,
> so there is nothing here to discharge it with.  The variant without it is
> `isoContinuousGroupCohomology`, whose degree-zero input is phrased against `R ⁰`.

```lean
def isoContinuousGroupCohomologyOfInvariants
    [PreservesFiniteLimits (continuousGModuleInvariants.{u, max u v} G)]
    (Het : DeltaFunctor (ContinuousGModule.{u, max u v} G) AddCommGrpCat.{max u v})
    (hvanish : ∀ (n : ℕ) (I : ContinuousGModule.{u, max u v} G) [Injective I],
      IsZero ((Het.functor (n + 1)).obj I))
    (base : Het.functor 0 ≅ continuousGModuleInvariants.{u, max u v} G) (i : ℕ) :
    Het.functor i ≅ continuousGroupCohomologyFunctor.{u, v} G i
```

**`AlgebraicGeometry.geometricGaloisDerivedInvariantsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedGaloisInvariants.lean, line 957](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedGaloisInvariants.lean#L957). The attribute's comment: “sixth assertion (the derived version of the cohomological half) with the Galois action: `RH⁰(π₁(X_k̄, η̄), M) ≅ RΓ^{Gal}(X_k̄, ℱ_ρ)` in the derived category of discrete `Λ`-modules with continuous `Aut(k̄/k)`-action, natural in `(M, ρ)`”.

> **The derived version of `H^i(X_{k̄}, ℱ_ρ) = H^i(π₁(X_{k̄}), M)` with its Galois action**
> ([Stacks, Tag 03VM], "Moreover, in this case there is a derived version too"): for a geometrically
> connected smooth curve `X` over `k`, `k̄` an algebraic closure of `k`, separable over `k`, `Λ` a
> finite ring with `#Λ` invertible in `k`, and `X_{k̄} ≇ 𝐏¹_{k̄}`, there is an isomorphism
>
> `RH⁰(π₁(X_{k̄}), M) ≅ RΓ^{Gal}(X_{k̄}, ℱ_ρ)`
>
> in the bounded below derived category of discrete `Λ`-modules with a continuous action of
> `Aut(k̄/k)`, natural in the finite `Λ`-module `M` with continuous action `ρ` of `π₁(X)`. Here
> `RH⁰(π₁(X_{k̄}), -)` is the right derived functor of the invariants under `π₁(X_{k̄})` with their
> residual action of `π₁(X)/π₁(X_{k̄}) = Aut(k̄/k)`
> (`Stacks.GroupCohomology.derivedKernelInvariants`), and `RΓ^{Gal}(X_{k̄}, -)` that of global
> sections on `X_{k̄}` with their Galois action
> (`Stacks.EtaleCohomology.galoisDerivedGlobalSections`). The degree-zero identification is the
> canonical one of Tag 03VL.

```lean
def geometricGaloisDerivedInvariantsIso
    (y : GeometricPoint (Stacks.Frobenius.fieldBaseChange (Over.mk f) K))
    (hΛ : IsUnit ((Nat.card Λ : ℕ) : k))
    (hP : ¬ ∃ e : Stacks.Frobenius.fieldBaseChange (Over.mk f) K ≅
        projectiveSpaceOver 1 (Spec (.of K)),
      e.hom ≫ (projectiveSpaceOver 1 (Spec (.of K)) ↘ Spec (.of K)) =
        pullback.snd (Over.mk f).hom (Stacks.Frobenius.specAlgebraMap k K)) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f K
    haveI : IsAlgClosed K := IsAlgClosure.isAlgClosed k
    haveI : Algebra.IsAlgebraic k K := IsAlgClosure.isAlgebraic
    (finiteTypeContinuousModuleι.{0, u + 1, u + 1} Λ
        (EtaleFundamentalGroup X.1
        (y.map (fieldBaseChangeObjProj B X f K
        (contains_fieldBaseChange_of_isCurve B X f K)).hom))) ⋙
        DerivedCategory.Plus.singleFunctor _ 0 ⋙
        derivedKernelInvariants.{0, u + 1, u, 0} Λ (geometricGaloisProjection B X f K y)
          (surjective_geometricGaloisProjection B X f K y) ≅
      representationSheaf.{u, 0} B X
          (y.map (fieldBaseChangeObjProj B X f K (contains_fieldBaseChange_of_isCurve B X f K)).hom)
          Λ ⋙ DerivedCategory.Plus.singleFunctor _ 0 ⋙
        Stacks.EtaleCohomology.galoisDerivedGlobalSections Λ (Over.mk f) K
```

**`AlgebraicGeometry.geometricDerivedInvariantsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedInvariants.lean, line 1074](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedInvariants.lean#L1074). The attribute's comment: “sixth assertion (the derived version of the cohomological half): `RΓ(π₁(X_k̄, η̄), M) ≅ RΓ(X_k̄, ℱ_ρ)`, natural in `(M, ρ)`”.

> **The derived version of `H^i(X_{k̄}, ℱ_ρ) = H^i(π₁(X_{k̄}), M)`** ([Stacks, Tag 03VM],
> "Moreover, in this case there is a derived version too"): for a geometrically connected smooth
> curve `X` over `k`, `k̄` an algebraic closure of `k`, `Λ` a finite ring with `#Λ` invertible in
> `k`, and `X_{k̄} ≇ 𝐏¹_{k̄}`, there is an isomorphism
>
> `RΓ(π₁(X_{k̄}), M) ≅ RΓ(X_{k̄}, ℱ_ρ)`
>
> in the bounded below derived category of `Λ`-modules, natural in the finite `Λ`-module `M` with
> continuous action `ρ` of `π₁(X)`. Here `RΓ(π₁(X_{k̄}), -)` is the right derived functor of the
> invariants on all continuous discrete `π₁(X_{k̄})`-modules, and `RΓ(X_{k̄}, -)` that of global
> sections on `(X_{k̄})_{étale}`. The source's hypotheses and nothing else.

```lean
def geometricDerivedInvariantsIso
    (y : GeometricPoint (Stacks.Frobenius.fieldBaseChange (Over.mk f) K))
    (hΛ : IsUnit ((Nat.card Λ : ℕ) : k))
    (hP : ¬ ∃ e : Stacks.Frobenius.fieldBaseChange (Over.mk f) K ≅
        projectiveSpaceOver 1 (Spec (.of K)),
      e.hom ≫ (projectiveSpaceOver 1 (Spec (.of K)) ↘ Spec (.of K)) =
        pullback.snd (Over.mk f).hom (Stacks.Frobenius.specAlgebraMap k K)) :
    letI := connectedSpace_of_isCurve B X f
    letI := connectedSpace_fieldBaseChange f K
    finiteTypeContinuousModuleToRes Λ
        (geometricFundamentalGroupMap B X f K (contains_fieldBaseChange_of_isCurve B X f K) y) ⋙
        DerivedCategory.Plus.singleFunctor _ 0 ⋙
        (continuousModuleRingInvariants.{0, u + 1, u + 1} Λ
          (EtaleFundamentalGroup (Stacks.Frobenius.fieldBaseChange (Over.mk f) K)
            y)).rightDerivedFunctorPlus ≅
      geometricRepresentationSheaf.{u, 0} B X
          (y.map (fieldBaseChangeObjProj B X f K (contains_fieldBaseChange_of_isCurve B X f K)).hom)
          Λ f K ⋙
        DerivedCategory.Plus.singleFunctor _ 0 ⋙
        (Stacks.EtaleCohomology.etaleModuleGlobalSections.{u, 0} Λ
          (Stacks.Frobenius.fieldBaseChange (Over.mk f) K)).rightDerivedFunctorPlus
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isIso_geometricComparison_of_not_iso_projectiveLine`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricRepresentationCohomologyNotProjectiveLine.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedInvariants.lean, line 1173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedInvariants.lean#L1173) (StacksFrontier): “fifth assertion: `H^i(X_k̄, ℱ_ρ) = H^i(π₁(X_k̄, η̄), M)`, the comparison of δ-functors being an isomorphism”.
- [`AlgebraicGeometry.isUniversal_geometricRepresentationCohomology_of_not_iso_projectiveLine`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricRepresentationCohomologyNotProjectiveLine.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedInvariants.lean, line 1177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricDerivedInvariants.lean#L1177) (StacksFrontier): “fourth assertion: `(M, ρ) ↦ H^i(X_k̄, ℱ_ρ)` is a universal δ-functor, i.e. the right derived functors of `(M, ρ) ↦ M^{π₁(X_k̄, η̄)}`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.29, Tag 03VJ](https://stacks.math.columbia.edu/tag/03VJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
