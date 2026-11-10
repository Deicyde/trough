---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.CoherenceFromPointClosures.isCoherent_pushforward_iff_forall_isAssociatedPoint, Stacks.AlgebraicGeometry.CoherenceFromPointClosures.isCoherent_pushforward_of_forall_isAssociatedPoint', Stacks.LocalCohomology.exact_lowDegreeSequence_and_nonempty_complementCohomology_iso, Stacks.LocalCohomology.coherent_complement_affine, Stacks.LocalCohomologySequence.moduleFinite_complementCohomologyBase_iff_isCoherent, Stacks.LocalCohomologySequence.isCoherent_rightDerived_iff_finite_localCohomology, AlgebraicGeometry.exists_finiteModule_tilde_restrict_zeroLocusCompl, Stacks.LocalCohomologySequence.exact_localCohomology_sequence_span_singleton
statement: formalized
proof: formalized
---

# 51.8 Finiteness of pushforwards, I

Section 51.8 of the Stacks Project, [Tag 0BL8](https://stacks.math.columbia.edu/tag/0BL8). 9 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BJZ, a lemma

[Tag 0BJZ](https://stacks.math.columbia.edu/tag/0BJZ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherenceFromPointClosures.isCoherent_pushforward_iff_forall_isAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/CoherenceEquivalence.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/CoherenceEquivalence.lean#L154).

> **[Stacks, Tag 0BJZ].** Let `X` be a locally Noetherian scheme, let `j : U ⟶ X` be the
> inclusion of an open subscheme and let `F` be a coherent `𝒪_U`-module. For `x ∈ U` let
> `i_x : W_x → U` be the integral closed subscheme with generic point `x`. Then the following are
> equivalent:
>
> 1. for all `x ∈ Ass(F)` the `𝒪_X`-module `j_* i_{x,*} 𝒪_{W_x}` is coherent;
> 2. `j_* F` is coherent.

```lean
theorem isCoherent_pushforward_iff_forall_isAssociatedPoint {U X : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j] (F : U.Modules) [F.IsCoherent] :
    (∀ x ∈ Stacks.Divisors.associatedPoints F,
        ((Scheme.Modules.pushforward j).obj (pointClosureStructureSheaf x)).IsCoherent) ↔
      ((Scheme.Modules.pushforward j).obj F).IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherenceFromPointClosures.isCoherent_pushforward_of_forall_isAssociatedPoint'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/CoherenceFromPointClosures.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/CoherenceFromPointClosures.lean#L571). The attribute's comment: “(1) implies (2)”.

> **[Stacks, Tag 0BJZ], the implication (1) ⇒ (2).** Let `X` be a locally Noetherian scheme,
> let `j : U ⟶ X` be the inclusion of an open subscheme and let `F` be a coherent `𝒪_U`-module. If
> `j_* i_{x,*} 𝒪_{W_x}` is coherent for every `x ∈ Ass(F)`, then `j_* F` is coherent.
>
> Coherence of a direct image is local on the target, and over an affine open of `X` the open
> subscheme becomes Noetherian and quasi-affine, which is what the induction needs.
>
> This is one direction of [Stacks, Tag 0BJZ]; the tag sits on the full equivalence
> `isCoherent_pushforward_iff_forall_isAssociatedPoint`, in
> `StacksFrontier.AlgebraicGeometry.LocalCohomology.CoherentPushforwardCriterion.CoherenceEquivalence`.

```lean
theorem isCoherent_pushforward_of_forall_isAssociatedPoint' {U X : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j] (F : U.Modules) [F.IsCoherent]
    (h : ∀ x ∈ Stacks.Divisors.associatedPoints F,
      ((Scheme.Modules.pushforward j).obj (pointClosureStructureSheaf x)).IsCoherent) :
    ((Scheme.Modules.pushforward j).obj F).IsCoherent
```

## Tag 0BK0, a lemma

[Tag 0BK0](https://stacks.math.columbia.edu/tag/0BK0) in the Stacks Project.

**`Stacks.LocalCohomology.exact_lowDegreeSequence_and_nonempty_complementCohomology_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentComplementAffine.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentComplementAffine.lean#L98). The attribute's comment: “(2)”. References: EGA III (1.4.3), “special case”; SGA 2 II (Corollary4), “special case”; SGA 4 V (6.5), “special case”.

> **[Stacks, Tag 0BK0] (2).** Let `R` be a Noetherian ring, let `I ⊆ R` be an ideal, let
> `X = Spec R`, let `Z = V(I)` and let `U = X ∖ Z`.  Let `M` be an `R`-module and let `F` be a
> sheaf of modules on `U` identified with `M̃|_U`.  Then the four-term sequence
> `0 ⟶ H⁰_Z(M) ⟶ M ⟶ Γ(U, F) ⟶ H¹_Z(M) ⟶ 0`
> built from the canonical map out of local cohomology, the restriction map and the connecting map
> of the localization triangle is exact, and `H^p(U, F) ≅ H^{p+1}_Z(M)` as `R`-modules for every
> `p ≥ 1`, with `H^p(U, F)` the cohomology of `F` on `U` read over `R`
> (`Stacks.LocalCohomology.complementSheafCohomology`).
>
> Neither half needs `M` finite or `F` coherent, which the source assumes.

```lean
theorem exact_lowDegreeSequence_and_nonempty_complementCohomology_iso
    (R : Type u) [CommRing R] [IsNoetherianRing R] (I : Ideal R) (hI : I.FG)
    (M : ModuleCat.{u} R) (F : (complementZeroLocus R I : Scheme).Modules)
    (e : F ≅ complementTilde R I M) :
    (∃ D : LocalizationTriangleData.{u, u} R I hI,
        Function.Injective (localCohomologyZeroToModule R I hI M) ∧
        Function.Exact (localCohomologyZeroToModule R I hI M)
          (restrictionToComplement D M F e) ∧
        Function.Exact (restrictionToComplement D M F e) (localizationBoundary D M F e) ∧
        Function.Surjective (localizationBoundary D M F e)) ∧
      ∀ p : ℕ, 1 ≤ p →
        Nonempty ((complementSheafCohomology R I p).obj F ≅
          localCohomologyModule R I hI M ((p + 1 : ℕ) : ℤ))
```

**`Stacks.LocalCohomology.coherent_complement_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentComplementAffine.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentComplementAffine.lean#L140).

> **[Stacks, Tag 0BK0].** Let `R` be a Noetherian ring, let `I ⊆ R` be an ideal, let
> `X = Spec R`, let `Z = V(I)`, let `U = X ∖ Z` and let `j : U → X` be the inclusion.  Let `F` be a
> coherent `𝒪_U`-module.  Then
>
> 1. there is a finite `R`-module `M` such that `F` is the restriction of `M̃` to `U`;
> 2. given `M` there is an exact sequence
>    `0 ⟶ H⁰_Z(M) ⟶ M ⟶ Γ(U, F) ⟶ H¹_Z(M) ⟶ 0`
>    and isomorphisms `H^p(U, F) ≅ H^{p+1}_Z(M)` for `p ≥ 1`;
> 3. given `M` and `p ≥ 0` the following are equivalent: `R^pj_*F` is coherent, `H^p(U, F)` is a
>    finite `R`-module, and `H^{p+1}_Z(M)` is a finite `R`-module;
> 4. if the equivalent conditions of (3) hold for `p = 0` then `M` may be taken to be `Γ(U, F)`,
>    which is then a finite `R`-module whose associated sheaf restricts to `F` on `U` and which
>    satisfies `H⁰_Z(Γ(U, F)) = H¹_Z(Γ(U, F)) = 0`.
>
> Clauses (2), (3) and (4) are stated for every finite `M` identifying `F` with `M̃|_U`, which is
> what "given `M`" means: the identification is part of the data and clause (1) produces one.
> `H^p(U, F)` is the cohomology of `F` on `U` read over `R`
> (`Stacks.LocalCohomology.complementSheafCohomology`) and `j` is the inclusion of `U`; clause
> (4)'s hypothesis is condition (c) of clause (3) in degree zero.  The
> hypothesis `hI : I.FG` is implied by `[IsNoetherianRing R]` through
> `Ideal.fg_of_isNoetherianRing`.
>
> Each clause is also registered on the declaration that proves it; nothing new is proved here.

```lean
theorem coherent_complement_affine
    (R : Type u) [CommRing R] [IsNoetherianRing R] (I : Ideal R) (hI : I.FG)
    (F : (complementZeroLocus R I : Scheme).Modules) [F.IsCoherent] :
    (∃ M : ModuleCat.{u} R, Module.Finite R M ∧ Nonempty (F ≅ complementTilde R I M)) ∧
      ∀ M : ModuleCat.{u} R, Module.Finite R M → ∀ e : F ≅ complementTilde R I M,
        ((∃ D : LocalizationTriangleData.{u, u} R I hI,
              Function.Injective (localCohomologyZeroToModule R I hI M) ∧
              Function.Exact (localCohomologyZeroToModule R I hI M)
                (restrictionToComplement D M F e) ∧
              Function.Exact (restrictionToComplement D M F e)
                (localizationBoundary D M F e) ∧
              Function.Surjective (localizationBoundary D M F e)) ∧
            ∀ p : ℕ, 1 ≤ p →
              Nonempty ((complementSheafCohomology R I p).obj F ≅
                localCohomologyModule R I hI M ((p + 1 : ℕ) : ℤ))) ∧
          (∀ p : ℕ,
            [(((Scheme.Modules.pushforward (complementZeroLocus R I).ι).rightDerived p).obj
                F).IsCoherent,
              Module.Finite R ((complementSheafCohomology R I p).obj F),
              Module.Finite R (localCohomologyModule R I hI M ((p + 1 : ℕ) : ℤ))].TFAE) ∧
          (Module.Finite R (localCohomologyModule R I hI M 1) →
            Module.Finite R (complementGlobalSections R I F) ∧
              Nonempty (F ≅ complementTilde R I (complementGlobalSections R I F)) ∧
              IsZero (localCohomologyModule R I hI (complementGlobalSections R I F) 0) ∧
              IsZero (localCohomologyModule R I hI (complementGlobalSections R I F) 1))
```

**`Stacks.LocalCohomologySequence.moduleFinite_complementCohomologyBase_iff_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FiniteLocallyFreeComplementAffine.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FiniteLocallyFreeComplementAffine.lean#L161). The attribute's comment: “(3), (a) ⟺ (b)”.

> **[Stacks, Tag 0BK0] (3), the equivalence of (a) and (b).** Let `A` be a Noetherian ring,
> `I ⊆ A` an ideal, `X = Spec A`, `Z = V(I)`, `U = X ∖ Z` and `j : U → X` the inclusion.  For an
> `A`-module `M` and any `p ≥ 0` the higher direct image `R^pj_*(M̃|_U)` is coherent if and only if
> `H^p(U, M̃)` is a finite `A`-module.
>
> By clause (1) of the same tag every coherent `𝒪_U`-module is isomorphic to a restriction `M̃|_U`
> with `M` finite, so this is that clause's equivalence; no finiteness of `M` is needed for the
> equivalence itself.
>
> The cohomology of `U` as computed by `complementCohomology` — the derived functor of the sections
> over `U` of sheaves of modules on the *ambient* `X` — is identified with the cohomology of the
> restriction on the open subscheme `U` by `derivedSectionsOnOpenIso`, which is [Stacks, Tag 01E1]
> (2); the latter is what [Stacks, Tag 01XK] over the affine base `X` turns into coherence of the
> higher direct image.

```lean
public theorem moduleFinite_complementCohomologyBase_iff_isCoherent [IsNoetherianRing A]
    (I : Ideal (ToType A)) (M : ModuleCat.{u} A) (p : ℕ) :
    Module.Finite A (complementCohomologyBase I M p) ↔
      (((Scheme.Modules.pushforward (zeroLocusCompl I).ι).rightDerived p).obj
        ((tilde M).restrict (zeroLocusCompl I).ι)).IsCoherent
```

**`Stacks.LocalCohomologySequence.isCoherent_rightDerived_iff_finite_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/CutoffCriterionAffine.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/CutoffCriterionAffine.lean#L87). The attribute's comment: “(3), (a) ⟺ (c)”.

> **[Stacks, Tag 0BK0] (3), the equivalence of (a) and (c).** Let `A` be a Noetherian ring,
> `I ⊆ A` an ideal, `X = Spec A`, `Z = V(I)`, `U = X ∖ Z` and `j : U → X` the inclusion. For a
> finite `A`-module `M` and any `p ≥ 0` the higher direct image `R^pj_*(M̃|_U)` is coherent if and
> only if the local cohomology `H^{p+1}_Z(M)` is a finite `A`-module.
>
> This is the composite of the tag's (a) ⟺ (b), which is
> `moduleFinite_complementCohomologyBase_iff_isCoherent`, with its (b) ⟺ (c), which is
> `finite_complementCohomologyBase_iff_finite_localCohomology`; the intermediate module is
> `H^p(U, M̃)` in both.

```lean
public theorem isCoherent_rightDerived_iff_finite_localCohomology [IsNoetherianRing A]
    (I : Ideal A) (M : ModuleCat.{u} A) [Module.Finite A M] (p : ℕ) :
    (((Scheme.Modules.pushforward (zeroLocusCompl I).ι).rightDerived p).obj
        ((tilde M).restrict (zeroLocusCompl I).ι)).IsCoherent ↔
      Module.Finite A (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
        (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M) ((p + 1 : ℕ) : ℤ))
```

**`AlgebraicGeometry.exists_finiteModule_tilde_restrict_zeroLocusCompl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/FiniteModule.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/FiniteModule.lean#L115). The attribute's comment: “(1)”. References: EGA I (1.5.1), “(a) => (c)”.

> **Stacks Project, Tag 0BK0 (1).** Let `A` be a Noetherian ring, let `I ⊆ A` be an ideal and
> let `U = Spec A \ V(I)`. A coherent `𝒪_U`-module is the restriction to `U` of the sheaf `M̃`
> attached to a finite `A`-module `M`.

```lean
theorem exists_finiteModule_tilde_restrict_zeroLocusCompl {A : CommRingCat.{u}}
    [IsNoetherianRing A] (I : Ideal A) (F : (zeroLocusCompl I).toScheme.Modules)
    [F.IsCoherent] :
    ∃ M : ModuleCat.{u} A, Module.Finite A M ∧
      Nonempty ((tilde M).restrict (zeroLocusCompl I).ι ≅ F)
```

**`Stacks.LocalCohomologySequence.exact_localCohomology_sequence_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyDegreewise.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyDegreewise.lean#L158). The attribute's comment: “(2), principal ideal”.

> **Stacks Project, Tag 0BK0 (2) for a principal ideal.**  Let `A` be a Noetherian ring, let
> `f : A` and write `X = Spec A`, `Z = V(f)` and `U = X ∖ Z`.  For an `A`-module `M` there is a
> connecting map `H⁰(U, M̃) ⟶ H¹_Z(M)` for which the sequence
>
> `0 ⟶ H⁰_Z(M) ⟶ H⁰(X, M̃) ⟶ H⁰(U, M̃) ⟶ H¹_Z(M) ⟶ 0`
>
> is exact, and `H^p(U, M̃) ≅ H^{p+1}_Z(M)` for every `p ≥ 1`, with `H^i_Z(M)` the algebraic
> local cohomology of `M`.

```lean
theorem exact_localCohomology_sequence_span_singleton [IsNoetherianRing A] (f : A)
    (M : ModuleCat.{u} A) :
    ∃ (d : (globalToBase A).obj
          ((complementCohomology (Ideal.span {f}) 0).obj (tildeSheaf M)) ⟶
        (localCohomologySpanSingleton A f 1).obj M)
      (hir : localCohomologyToGlobalSections f M ≫ (globalToBase A).map
        ((complementRestriction (Ideal.span {f}) 0).app (tildeSheaf M)) = 0)
      (hrd : (globalToBase A).map
        ((complementRestriction (Ideal.span {f}) 0).app (tildeSheaf M)) ≫ d = 0),
      Mono (localCohomologyToGlobalSections f M) ∧ (ShortComplex.mk _ _ hir).Exact ∧
        (ShortComplex.mk _ _ hrd).Exact ∧ Epi d ∧
        ∀ p : ℕ, 0 < p → Nonempty ((globalToBase A).obj
          ((complementCohomology (Ideal.span {f}) p).obj (tildeSheaf M)) ≅
            (localCohomologySpanSingleton A f (p + 1)).obj M)
```

**`Stacks.LocalCohomologySequence.finite_complementCohomologyBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean#L120). The attribute's comment: “(3), (b) ⟺ (c), with cohomology with support in place of local cohomology”.

> **Stacks Project, Tag 0BK0 (3), the equivalence of (b) and (c)**, with cohomology with
> support in place of local cohomology.  Let `I` be an ideal of a ring `A`, let `X = Spec A`, let
> `Z = V(I)` and let `U = X ∖ Z`.  For a finite `A`-module `M` and any `p ≥ 0` the `A`-module
> `H^p(U, M̃)` is finite if and only if `H^{p+1}_Z(X, M̃)` is.

```lean
theorem finite_complementCohomologyBase_iff (I : Ideal A) (M : ModuleCat.{u} A)
    [Module.Finite A M] (p : ℕ) :
    Module.Finite A (complementCohomologyBase I M p) ↔
      Module.Finite A (cohomologyWithSupportBase I M (p + 1))
```

**`Stacks.LocalCohomologySequence.finite_localCohomology_iff_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean#L148). The attribute's comment: “(3), (b) ⟺ (c), principal ideal”.

> **Stacks Project, Tag 0BK0 (3) for a principal ideal, the equivalence of (b) and (c).**  Let
> `A` be a Noetherian ring, let `f : A`, let `X = Spec A`, let `Z = V(f)` and let `U = X ∖ Z`.  For
> a finite `A`-module `M` and any `p ≥ 0` the `A`-module `H^p(U, M̃)` is finite if and only if the
> local cohomology `H^{p+1}_Z(M)` is.

```lean
theorem finite_localCohomology_iff_span_singleton [IsNoetherianRing A] (f : A)
    (M : ModuleCat.{u} A) [Module.Finite A M] (p : ℕ) :
    Module.Finite A (complementCohomologyBase (Ideal.span {f}) M p) ↔
      Module.Finite A ((localCohomologySpanSingleton A f (p + 1)).obj M)
```

**`Stacks.LocalCohomologySequence.isZero_cohomologyWithSupport_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean#L164). The attribute's comment: “(4), the vanishing, for a module whose canonical map to the sections over the complement is an isomorphism”.

> **Stacks Project, Tag 0BK0 (4), the vanishing.**  Let `I` be an ideal of a ring `A`, let
> `X = Spec A`, let `Z = V(I)` and let `U = X ∖ Z`.  If the canonical map `M ⟶ Γ(U, M̃)` is an
> isomorphism — which is what taking `M = Γ(U, ℱ)` achieves — then `H⁰_Z(X, M̃) = 0` and
> `H¹_Z(X, M̃) = 0`.

```lean
theorem isZero_cohomologyWithSupport_of_isIso (I : Ideal A) (M : ModuleCat.{u} A)
    (h : IsIso (toComplementSections I M)) :
    IsZero (cohomologyWithSupportBase I M 0) ∧ IsZero (cohomologyWithSupportBase I M 1)
```

**`Stacks.LocalCohomologySequence.isZero_localCohomology_of_isIso_span_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologyFiniteness.lean#L202). The attribute's comment: “(4), the vanishing, principal ideal, for a module whose canonical map to the sections over the complement is an isomorphism”.

> **Stacks Project, Tag 0BK0 (4) for a principal ideal, the vanishing.**  Let `A` be a
> Noetherian ring, let `f : A`, let `X = Spec A`, let `Z = V(f)` and let `U = X ∖ Z`.  If the
> canonical map `M ⟶ Γ(U, M̃)` is an isomorphism then the local cohomology modules `H⁰_Z(M)` and
> `H¹_Z(M)` are zero.

```lean
theorem isZero_localCohomology_of_isIso_span_singleton [IsNoetherianRing A] (f : A)
    (M : ModuleCat.{u} A) (h : IsIso (toComplementSections (Ideal.span {f}) M)) :
    IsZero ((localCohomologySpanSingleton A f 0).obj M) ∧
      IsZero ((localCohomologySpanSingleton A f 1).obj M)
```

**`Stacks.LocalCohomologySequence.exact_cohomologyWithSupport_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologySequence.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/LocalCohomologySequence.lean#L164). The attribute's comment: “(2), with cohomology with support in place of local cohomology”. References: SGA 2 II (Corollary4), “(4.2), (4.3)”.

> **Stacks Project, Tag 0BK0 (2)**, with cohomology with support in place of local cohomology.
> For an ideal `I` of a ring `A` and an `A`-module `M`, write `X = Spec A`, `Z = V(I)` and
> `U = X ∖ Z`.  There is a connecting map `H^n(U, M̃) ⟶ H^{n+1}_Z(X, M̃)` for which the sequence
>
> `0 ⟶ H⁰_Z(X, M̃) ⟶ Γ(X, M̃) ⟶ Γ(U, M̃) ⟶ H¹_Z(X, M̃) ⟶ 0`
>
> is exact and `H^p(U, M̃) ⟶ H^{p+1}_Z(X, M̃)` is an isomorphism for every `p ≥ 1`.

```lean
theorem exact_cohomologyWithSupport_sequence (I : Ideal A) (M : ModuleCat.{u} A) :
    ∃ delta : ∀ n : ℕ, complementCohomology I n ⟶ cohomologyWithSupport I (n + 1),
      Mono ((supportInclusion I 0).app (tildeSheaf M)) ∧
      (ComposableArrows.mk₃ ((supportInclusion I 0).app (tildeSheaf M))
        ((complementRestriction I 0).app (tildeSheaf M))
        ((delta 0).app (tildeSheaf M))).Exact ∧
      Epi ((delta 0).app (tildeSheaf M)) ∧
      ∀ p : ℕ, 0 < p → IsIso ((delta p).app (tildeSheaf M))
```

**`Stacks.LocalCohomologySequence.finite_complementCohomologyBase_iff_finite_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/HigherDegree/CohomologyWithSupportComparison.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/HigherDegree/CohomologyWithSupportComparison.lean#L385). The attribute's comment: “(3), (b) ⟺ (c)”.

> **The finiteness consequence of Stacks 0DWR, in every degree.** For a finite module `M` over
> a Noetherian ring the `A`-module `H^p(U, M̃)` on `U = Spec A ∖ V(I)` is finite exactly when the
> local cohomology `H^{p+1}_{V(I)}(M)` is, for every `p ≥ 0`.
>
> In degree zero this is the four-term exact sequence of Stacks 0DWR, which presents `Γ(U, M̃)` as
> an extension of `H¹_{V(I)}(M)` by a quotient of `M`; in degrees above zero it is the isomorphism
> above.
>
> This is **Stacks 0BK0 (3), the equivalence of (b) and (c)**, for an arbitrary ideal `I` of a
> Noetherian ring `A` (the tag's own hypothesis on `A`, not an additional one) and every `p ≥ 0`:
> no finite generation of `I` beyond what `A` Noetherian already gives, and no restriction to a
> principal ideal, is needed.

```lean
theorem finite_complementCohomologyBase_iff_finite_localCohomology
    [IsNoetherianRing A] (I : Ideal A) (M : ModuleCat.{u} A) [Module.Finite A M] (p : ℕ) :
    Module.Finite A (complementCohomologyBase I M p) ↔
      Module.Finite A (Stacks.LocalCohomology.localCohomologyWithSupportIn.{u, u} A
        (PrimeSpectrum.zeroLocus (I : Set A))
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj M) ((p + 1 : ℕ) : ℤ))
```

**`Stacks.LocalCohomology.exact_lowDegreeSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/LowDegree/CechSectionsComparison.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/LowDegree/CechSectionsComparison.lean#L373). The attribute's comment: “low_degree_sequence”. References: EGA III (1.4.3), “(1.4.3.2), special case”; SGA 2 II (Corollary4), “(4.2)”; SGA 4 V (6.5), “(6.5.3), special case”.

> **Stacks 0BK0, the low-degree sequence.** Let `I` be a finitely generated ideal of a
> commutative ring `A`, let `U = Spec A \ V(I)`, let `M` be an `A`-module and let `F` be a sheaf of
> modules on `U` identified with the restriction to `U` of the sheaf associated to `M`. Then the
> four-term sequence
> `0 ⟶ H⁰_I(M) ⟶ M ⟶ Γ(U, F) ⟶ H¹_I(M) ⟶ 0`
> is exact: the map out of degree-zero local cohomology is injective, the sequence is exact at `M`
> and at `Γ(U, F)`, and the connecting map onto `H¹_I(M)` is surjective.
>
> Every ideal of a Noetherian ring is finitely generated, by `Ideal.fg_of_isNoetherianRing`, so
> this covers the Noetherian hypothesis of the source; and it does not assume `M` finite or `F`
> coherent, which the source does.
>
> The same four-term sequence is the first half of clause (2) of Stacks 0DWR, which assumes only
> that `I` is finitely generated. The second half of that clause, the comparison
> `H^p(U, F) ≅ H^{p+1}_I(M)` in degrees `p ≥ 1`, `A`-linearly and for the same `F` and `M`, is
> `Stacks.LocalCohomology.nonempty_complementSheafCohomology_iso_localCohomologyModule`, under the
> same hypothesis `I.FG`.

```lean
theorem exact_lowDegreeSequence (M : ModuleCat.{max u v} A)
    (F : SheafOfModules.{max u v} (complementZeroLocus A I : Scheme).ringCatSheaf)
    (e : F ≅ complementTilde A I M) :
    Function.Injective (localCohomologyZeroToModule A I hI M).hom ∧
      Function.Exact (localCohomologyZeroToModule A I hI M)
        (restrictionToComplement (localizationTriangleData.{v} A I hI) M F e) ∧
      Function.Exact (restrictionToComplement (localizationTriangleData.{v} A I hI) M F e)
        (localizationBoundary (localizationTriangleData.{v} A I hI) M F e) ∧
      Function.Surjective (localizationBoundary (localizationTriangleData.{v} A I hI) M F e)
```

**`Stacks.LocalCohomology.finite_iso_restrict_and_isZero_localCohomology_globalSectionsModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsFinite.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/LowDegree/GlobalSectionsFinite.lean#L78). The attribute's comment: “(4)”.

> **[Stacks, Tag 0BK0] (4).** Let `I` be a finitely generated ideal of `A`, let
> `U = Spec A \ V(I)`, let `F` be a quasi-coherent `𝒪_U`-module and let `M` be a finite `A`-module
> with `F ≅ M̃|_U`.  If the equivalent conditions of clause (3) hold in degree zero, in the form
> `H¹_{V(I)}(M)` finite, then `N = Γ(U, F)` is itself an admissible choice for `M`: it is a finite
> `A`-module, `F` is the restriction of `Ñ` to `U`, and `H⁰_{V(I)}(N) = H¹_{V(I)}(N) = 0`.
>
> Finiteness of `N` comes from the four-term sequence of clause (2), which presents `Γ(U, F)` as an
> extension of `H¹_{V(I)}(M)` by a quotient of `M`.  The isomorphism `F ≅ Ñ|_U` is the counit of
> the tilde–Gamma adjunction, and the two vanishing statements are the degeneration of the
> four-term sequence at the extension `N`, whose restriction map `N ⟶ Γ(U, F)` is the identity.

```lean
theorem finite_iso_restrict_and_isZero_localCohomology_globalSectionsModule
    (F : (complementZeroLocus A I : Scheme).Modules) [F.IsQuasicoherent]
    (M : ModuleCat.{u} A) [Module.Finite A M] (e : F ≅ complementTilde A I M)
    (hfin : Module.Finite A (localCohomologyModule A I hI M 1)) :
    Module.Finite A (complementGlobalSections A I F) ∧
      Nonempty (F ≅ complementTilde A I (complementGlobalSections A I F)) ∧
      IsZero (localCohomologyModule A I hI (complementGlobalSections A I F) 0) ∧
      IsZero (localCohomologyModule A I hI (complementGlobalSections A I F) 1)
```

## Tag 0AWA, a lemma

[Tag 0AWA](https://stacks.math.columbia.edu/tag/0AWA) in the Stacks Project.

**`Stacks.LocalCohomology.isCoherent_pushforward_of_isNagataScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/NagataCatenaryCoherence.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/NagataCatenaryCoherence.lean#L195). References: EGA IV (5.11.1), “c) ⇒ a), special case”.

> **[Stacks, Tag 0AWA].** Let `X` be a locally Noetherian scheme, let `j : U ⟶ X` be the
> inclusion of an open subscheme with complement `Z`, and let `F` be a coherent `𝒪_U`-module.
> Assume (1) `X` is Nagata, (2) `X` is universally catenary, and
> (3) `dim(𝒪_{closure{x}, z}) ≥ 2` for `x ∈ Ass(F)` and `z ∈ Z ∩ closure{x}`. Then `j_*F` is
> coherent.
>
> The proof runs the source's argument on the tag's own three assumptions. Assumption (1) makes
> the normalization `π : Y ⟶ X` of `X` in `Spec κ(x)` finite, hence `G = π_*𝒪_Y` coherent;
> `Stacks.LocalCohomology.exists_mono_pullback_residueFieldNormalizationPushforward` supplies the
> comparison monomorphism `i_{x,*}𝒪_{W_x} ⟶ G|_U`; assumptions (2) and (3) give `depth(G_z) ≥ 2`
> on `Z` through
> `AlgebraicGeometry.hasDepthTwoOutside_pushforwardUnitModule_fromSpecResidueField`; the depth-two
> theorem `AlgebraicGeometry.isCoherent_pushforward_of_mono_of_depth_ge_two` then makes
> `j_*i_{x,*}𝒪_{W_x}` coherent at each associated point, which is the hypothesis of the
> implication (1) ⇒ (2) of [Stacks, Tag 0BJZ].

```lean
theorem isCoherent_pushforward_of_isNagataScheme {X : Scheme.{u}} [IsLocallyNoetherian X]
    (V : X.Opens) (F : V.toScheme.Modules) [F.IsCoherent]
    (hNagata : IsNagataScheme X)
    (hCat : X.IsUniversallyCatenary)
    (hdim : ∀ x : V.toScheme, x ∈ Stacks.Divisors.associatedPoints F →
      TwoLePointClosureDim V x) :
    ((Scheme.Modules.pushforward V.ι).obj F).IsCoherent
```

## Tag 0BK1, a lemma

[Tag 0BK1](https://stacks.math.columbia.edu/tag/0BK1) in the Stacks Project.

**`Stacks.LocalCohomology.isCoherent_pushforward_structureSheaf_of_completion_associatedPrime_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/PuncturedSpectrumCoherentPushforward.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/PuncturedSpectrumCoherentPushforward.lean#L336). References: EGA I (1.5.2), “special case”; EGA IV (7.2.2), “(b) ⇒ (a)”.

> **[Stacks, Tag 0BK1].** Let `X` be an integral locally Noetherian scheme and let `j : U ⟶ X`
> be the inclusion of a nonempty open subscheme with complement `Z`. Assume that for every `z ∈ Z`
> and every associated prime `𝔭` of the completed local ring `𝒪^∧_{X,z}` one has
> `dim(𝒪^∧_{X,z} ⧸ 𝔭) ≥ 2`. Then `j_*𝒪_U` is coherent.
>
> The proof is the source's. The reduction to the punctured spectra of the local rings along the
> complement is `Stacks.LocalCohomology.puncturedSpectrumReduction`, and at a point `z` of the
> complement the punctured spectrum of `𝒪_{X,z}` has coherent direct image by
> `isCoherent_pushforward_structureSheaf_puncturedSpectrum`, whose hypothesis is `hdim` at `z`.

```lean
theorem isCoherent_pushforward_structureSheaf_of_completion_associatedPrime_dim
    {U X : Scheme.{u}} [IsIntegral X] [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    [Nonempty U]
    (hdim : ∀ z : X, z ∉ Set.range j.base →
      ∀ p : Ideal (AdicCompletion (maximalIdeal (X.presheaf.stalk z)) (X.presheaf.stalk z)),
        IsAssociatedPrimeStacks
          (AdicCompletion (maximalIdeal (X.presheaf.stalk z)) (X.presheaf.stalk z))
          (AdicCompletion (maximalIdeal (X.presheaf.stalk z)) (X.presheaf.stalk z)) p →
        (2 : WithBot ℕ∞) ≤ ringKrullDim (AdicCompletion
          (maximalIdeal (X.presheaf.stalk z)) (X.presheaf.stalk z) ⧸ p)) :
    ((Scheme.Modules.pushforward j).obj (SheafOfModules.unit.{u} U.ringCatSheaf)).IsCoherent
```

## Tag 0BK2, a remark

[Tag 0BK2](https://stacks.math.columbia.edu/tag/0BK2) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ClosedImmersionCoherence.isCoherent_pushforward_pointClosure_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/ClosedImmersionCoherence.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/ClosedImmersionCoherence.lean#L342). The attribute's comment: “coherence equivalence”.

> **Stacks Project, Tag 0BK2.** Coherence of the direct image to `X` of the structure sheaf of
> the reduced closure of `{x}` in `U` is equivalent to coherence of its direct image to the reduced
> closure of `{j x}` in `X`: the two iterated direct images agree, and the remaining vertical arrow
> is a closed immersion.

```lean
theorem isCoherent_pushforward_pointClosure_iff {U X : Scheme.{u}} (j : U ⟶ X)
    [IsOpenImmersion j] [IsLocallyNoetherian U] [IsLocallyNoetherian X] (x : U)
    (j' : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({x} : Set U))).subscheme ⟶
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subscheme)
    (comm : j' ≫ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subschemeι =
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({x} : Set U))).subschemeι ≫ j) :
    ((Scheme.Modules.pushforward j).obj
      ((Scheme.Modules.pushforward
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({x} : Set U))).subschemeι).obj
        (SheafOfModules.unit
          (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({x} : Set U))).subscheme.ringCatSheaf))).IsCoherent ↔
    ((Scheme.Modules.pushforward j').obj
      (SheafOfModules.unit
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({x} : Set U))).subscheme.ringCatSheaf)).IsCoherent
```

**`AlgebraicGeometry.Scheme.IdealSheafData.exists_isOpenImmersion_pointClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean#L121). The attribute's comment: “commutative square of closures”. References: EGA I (5.2.3), “special case”.

> **Stacks Project, Tag 0BK2.** For an open immersion `j : U ⟶ X` and a point `x` of `U`, the
> reduced closure of `{x}` in `U` is an open subscheme of the reduced closure of `{j x}` in `X`,
> compatibly with the two closed immersions: there is an open immersion `j'` making the square of
> canonical inclusions commute.

```lean
theorem exists_isOpenImmersion_pointClosure {U X : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j]
    [IsLocallyNoetherian U] [IsLocallyNoetherian X] (x : U) :
    let W := (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({x} : Set U))).subscheme
    let Z := (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({j x} : Set X))).subscheme
    ∃ j' : W ⟶ Z, IsOpenImmersion j' ∧
      j' ≫ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subschemeι =
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({x} : Set U))).subschemeι ≫ j
```

**`AlgebraicGeometry.Scheme.IdealSheafData.range_of_pointClosureSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean#L214). The attribute's comment: “cartesianness of the square of closures”.

> **Stacks Project, Tag 0BK2.** The square of point closures is cartesian: the reduced closure
> of `{x}` in `U` is exactly the part of the reduced closure of `{j x}` in `X` lying over `U`.

```lean
theorem range_of_pointClosureSquare {U X : Scheme.{u}} (j : U ⟶ X) [IsOpenImmersion j] (x : U)
    (j' : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({x} : Set U))).subscheme ⟶
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subscheme)
    (comm : j' ≫ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subschemeι =
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({x} : Set U))).subschemeι ≫ j) :
    Set.range j'.base = (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({j x} : Set X))).subschemeι.base ⁻¹' Set.range j.base
```

**`AlgebraicGeometry.Scheme.Modules.pushforwardPointClosureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean#L253). The attribute's comment: “direct-image comparison”.

> **Stacks Project, Tag 0BK2.** The canonical comparison of the two iterated direct images of
> the structure sheaf of the reduced closure of `{x}` around the commutative square of point
> closures: pushing forward first to `U` and then to `X` agrees with pushing forward first to the
> closure of `{j x}` and then to `X`.

```lean
noncomputable def pushforwardPointClosureIso {U X : Scheme.{u}} (j : U ⟶ X) (x : U)
    (j' : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({x} : Set U))).subscheme ⟶
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subscheme)
    (comm : j' ≫ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subschemeι =
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({x} : Set U))).subschemeι ≫ j) :
    (Scheme.Modules.pushforward j).obj
      ((Scheme.Modules.pushforward
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({x} : Set U))).subschemeι).obj
        (SheafOfModules.unit
          (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({x} : Set U))).subscheme.ringCatSheaf)) ≅
    (Scheme.Modules.pushforward
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({j x} : Set X))).subschemeι).obj
      ((Scheme.Modules.pushforward j').obj
        (SheafOfModules.unit
          (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({x} : Set U))).subscheme.ringCatSheaf))
```

**`AlgebraicGeometry.Scheme.Modules.pullbackPointClosureIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/CoherentPushforwardCriteria/PointClosureSquare.lean#L325). The attribute's comment: “inverse-image comparison”.

> **Stacks Project, Tag 0BK2.** The comparison of direct images of the structure sheaf of a
> point closure in the inverse image direction: the restriction to the open subscheme `V` of the
> direct image of `𝒪_Z` along the closure of `{V.ι x}` in `X` is the direct image of `𝒪_W` along
> the closure of `{x}` in `V`.

```lean
noncomputable def pullbackPointClosureIso {X : Scheme.{u}} [IsLocallyNoetherian X]
    (V : X.Opens) (x : V.toScheme)
    (j' : (Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({x} : Set V.toScheme))).subscheme ⟶
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({V.ι.base x} : Set X))).subscheme)
    (comm : j' ≫ (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({V.ι.base x} : Set X))).subschemeι =
      (Scheme.IdealSheafData.vanishingIdeal
        (Closeds.closure ({x} : Set V.toScheme))).subschemeι ≫ V.ι) :
    (Scheme.Modules.pullback V.ι).obj ((Scheme.Modules.pushforward
        (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({V.ι.base x} : Set X))).subschemeι).obj
        (SheafOfModules.unit.{u} (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({V.ι.base x} : Set X))).subscheme.ringCatSheaf)) ≅
      (Scheme.Modules.pushforward (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({x} : Set V.toScheme))).subschemeι).obj
        (SheafOfModules.unit.{u} (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({x} : Set V.toScheme))).subscheme.ringCatSheaf)
```

## Tag 0AWC, a remark

[Tag 0AWC](https://stacks.math.columbia.edu/tag/0AWC) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CodimensionOneObstruction.not_isCoherent_pushforward_of_isAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CodimensionOneObstruction/AssociatedPointObstruction.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CodimensionOneObstruction/AssociatedPointObstruction.lean#L188). The attribute's comment: “first paragraph”. References: EGA IV (5.10.10), “Clause (ii) for closed Z”; EGA IV (5.11.1), “a) ⇒ c), for Z closed”; EGA IV (5.11.4), “more general”; EGA IV (7.8.3), “(ix), partial”.

> **First paragraph of [Stacks, Tag 0AWC].** Let `X` be a locally Noetherian scheme, `U` an open
> subscheme with complement `Z`, and `𝓕` an `𝒪_U`-module. Let `x` be a point of `U` associated to
> `𝓕`, let `X'` be the reduced closed subscheme of `X` supported on the closure of `{x}`, and let
> `z'` be a point of `X'` whose image lies in `Z` and at which `dim 𝒪_{X', z'} ≤ 1`. Then the direct
> image of `𝓕` along `U → X` is not coherent.
>
> `X'` is integral with generic point `x` by
> `AlgebraicGeometry.Scheme.IdealSheafData.isIntegral_subscheme_vanishingIdeal_closure` and
> `AlgebraicGeometry.Scheme.IdealSheafData.subschemeι_genericPoint_vanishingIdeal_closure`, so a
> point of `X'` whose image avoids `U` is exactly a point `z ∈ Z ∩ \overline{\{x\}}` of the cited
> remark, and `𝒪_{X', z'}` is its `𝒪_{\overline{\{x\}}, z}`.
>
> The remark assumes `𝓕` coherent; no hypothesis on `𝓕` is needed here.

```lean
theorem not_isCoherent_pushforward_of_isAssociatedPoint [IsLocallyNoetherian X]
    {U : X.Opens} (𝓕 : U.toScheme.Modules) {x : X} (hxU : x ∈ U)
    (hass : Stacks.Divisors.IsAssociatedPoint 𝓕 ⟨x, hxU⟩)
    {I : X.IdealSheafData}
    (hI : I = Scheme.IdealSheafData.vanishingIdeal (Closeds.closure ({x} : Set X)))
    (z' : I.subscheme) (hzU : I.subschemeι z' ∉ U)
    (hdim : ringKrullDim (I.subscheme.presheaf.stalk z') ≤ 1) :
    ¬ ((Scheme.Modules.pushforward U.ι).obj 𝓕).IsCoherent
```

**`Stacks.AlgebraicGeometry.CodimensionOneObstruction.not_isCoherent_pushforward_structureSheaf_of_isAssociatedPrime_completedStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CodimensionOneObstruction/CompletedLocalBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CodimensionOneObstruction/CompletedLocalBaseChange.lean#L187). The attribute's comment: “second paragraph”. References: EGA IV (7.2.4), “(e) ⇒ (f)”.

> **A one-dimensional associated prime of the completed local ring obstructs coherence of the
> direct image of the structure sheaf.** Let `j : U → X` be an open immersion of integral locally
> Noetherian schemes and let `z` be a point of `X` outside `U`. If the completion `𝒪^∧_{X, z}` has an
> associated prime `𝔭` — a prime which is the annihilator of one of its elements — with
> `dim(𝒪^∧_{X, z} ⧸ 𝔭) = 1`, then `j_* 𝒪_U` is not coherent.

```lean
theorem not_isCoherent_pushforward_structureSheaf_of_isAssociatedPrime_completedStalk
    {X : Scheme.{u}} [IsIntegral X] [IsLocallyNoetherian X] {U : X.Opens}
    [Nonempty U.toScheme] {z : X} (hzU : z ∉ U)
    {p : PrimeSpectrum (X.completedLocalRingCat z)}
    (hp : IsAssociatedPrimeStacks (X.completedLocalRingCat z) (X.completedLocalRingCat z)
      p.asIdeal)
    (hdim : ringKrullDim (X.completedLocalRingCat z ⧸ p.asIdeal) = 1) :
    ¬ ((Scheme.Modules.pushforward U.ι).obj (SheafOfModules.unit _)).IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentPushforwardCriterion.not_isCoherent_pushforward_structureSheaf_of_isAssociatedPrime_completedStalk_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/CompletedStalkAssociatedDimension.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/CompletedStalkAssociatedDimension.lean#L131). The attribute's comment: “second paragraph, for an associated quotient of the completion of dimension at most one”. References: EGA IV (7.2.4), “(e) ⇒ (f)”.

> **`j_* 𝒪_U` is not coherent when a completed local ring outside `U` has an associated prime
> of dimension at most one.** Let `j : U → X` be the inclusion of a nonempty open subscheme of an
> integral locally Noetherian scheme and let `z` be a point of `X` outside `U`. If the completion
> `𝒪^∧_{X, z}` has an associated prime `𝔭` — a prime which is the annihilator of one of its
> elements — with `dim(𝒪^∧_{X, z} ⧸ 𝔭) ≤ 1`, then `j_* 𝒪_U` is not coherent.

```lean
theorem not_isCoherent_pushforward_structureSheaf_of_isAssociatedPrime_completedStalk_le_one
    {X : Scheme.{u}} [IsIntegral X] [IsLocallyNoetherian X] {U : X.Opens}
    [Nonempty U.toScheme] {z : X} (hzU : z ∉ U)
    {p : PrimeSpectrum (X.completedLocalRingCat z)}
    (hp : IsAssociatedPrimeStacks (X.completedLocalRingCat z) (X.completedLocalRingCat z)
      p.asIdeal)
    (hdim : ringKrullDim (X.completedLocalRingCat z ⧸ p.asIdeal) ≤ 1) :
    ¬ ((Scheme.Modules.pushforward U.ι).obj (SheafOfModules.unit _)).IsCoherent
```

**`Stacks.LocalCohomology.not_isCoherent_pushforward_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CompletedLocalObstruction.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CompletedLocalObstruction.lean#L402). The attribute's comment: “completed_local_ring_obstruction”. References: EGA IV (7.2.4), “(e) ⇒ (f)”.

> **[Stacks, Tag 0AWC], the completed-local-ring obstruction to coherence.** Let `j : U ⟶ X` be
> an open immersion of integral locally Noetherian schemes and suppose some point `z` outside the
> image of `j` has an associated prime `𝔭` of the completed local ring `𝒪^∧_{X,z}` with
> `dim(𝒪^∧_{X,z} ⧸ 𝔭) = 1`. Then `j_*𝒪_U` is not coherent.
>
> This is the second paragraph of the remark, its `completed_local_ring_obstruction` clause, the
> converse to [Stacks, Tag 0E9I].

```lean
theorem not_isCoherent_pushforward_structureSheaf {U X : Scheme.{u}} (j : U ⟶ X)
    [IsOpenImmersion j] [IsIntegral U] [IsIntegral X] [IsLocallyNoetherian X]
    (h : ∃ (z : X) (p : Ideal (AdicCompletion
        (IsLocalRing.maximalIdeal (ToType (X.presheaf.stalk z)))
        (ToType (X.presheaf.stalk z)))),
      z ∉ Set.range j.base ∧
      IsAssociatedPrimeStacks
        (AdicCompletion (IsLocalRing.maximalIdeal (ToType (X.presheaf.stalk z)))
          (ToType (X.presheaf.stalk z)))
        (AdicCompletion (IsLocalRing.maximalIdeal (ToType (X.presheaf.stalk z)))
          (ToType (X.presheaf.stalk z))) p ∧
      ringKrullDim (AdicCompletion (IsLocalRing.maximalIdeal (ToType (X.presheaf.stalk z)))
        (ToType (X.presheaf.stalk z)) ⧸ p) = 1) :
    ¬ ((Scheme.Modules.pushforward j).obj
      (SheafOfModules.unit.{u} U.ringCatSheaf)).IsCoherent
```

## Tag 0BK3, a proposition

[Tag 0BK3](https://stacks.math.columbia.edu/tag/0BK3) in the Stacks Project.

**`Stacks.AlgebraicGeometry.CoherentPushforwardCriterion.not_isCoherent_pushforward_of_isAssociatedPrime_completedStalk_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/PointClosureCompletionDimension.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/PointClosureCompletionDimension.lean#L87). The attribute's comment: “(1) implies (2), contrapositive at one point, given a monomorphism from the structure sheaf of the point closure”. References: EGA IV (5.11.4), “necessity”.

> **[Stacks, Tag 0BK3], the implication (1) ⇒ (2), in contrapositive form at a single point,
> for an associated quotient of dimension at most one.** Let `j : U ⟶ X` be an open immersion of
> schemes with `X` locally Noetherian, let `F` be a quasi-coherent `𝒪_U`-module and let `x` be a
> point of `U`. Suppose there is a monomorphism `i_{x,*} 𝒪_{W_x} ⟶ F`, and suppose `z` is a point
> of the reduced closure of `{j x}` whose image in `X` lies outside `U` such that the completion
> `𝒪^∧_{closure {x}, z}` has an associated prime `𝔭` with
> `dim(𝒪^∧_{closure {x}, z} ⧸ 𝔭) ≤ 1`. Then `j_* F` is not coherent.
>
> This is the failure of clause (2) of the source at `x` and `z` obstructing clause (1), with the
> dimension hypothesis exactly as the negation of that clause delivers it. The monomorphism still
> replaces the source's `x ∈ Ass(F)`.

```lean
theorem not_isCoherent_pushforward_of_isAssociatedPrime_completedStalk_le_one {U X : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j] (x : U)
    {F : U.Modules} [F.IsQuasicoherent]
    (φ : pointClosureStructureSheaf x ⟶ F) [Mono φ]
    {I : X.IdealSheafData}
    (hI : I = Scheme.IdealSheafData.vanishingIdeal (Closeds.closure ({j x} : Set X)))
    (z : I.subscheme) (hz : I.subschemeι z ∉ j.opensRange)
    {p : PrimeSpectrum (I.subscheme.completedLocalRingCat z)}
    (hp : IsAssociatedPrimeStacks (I.subscheme.completedLocalRingCat z)
      (I.subscheme.completedLocalRingCat z) p.asIdeal)
    (hdim : ringKrullDim (I.subscheme.completedLocalRingCat z ⧸ p.asIdeal) ≤ 1) :
    ¬ ((Scheme.Modules.pushforward j).obj F).IsCoherent
```

**`Stacks.AlgebraicGeometry.CoherentPushforwardCriterion.two_le_ringKrullDim_quotient_completedStalk_of_isCoherent_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/PointClosureCompletionDimension.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/PointClosureCompletionDimension.lean#L146). The attribute's comment: “(1) implies (2), given a monomorphism from the structure sheaf of the point closure”. References: EGA IV (7.2.3), “b) => c)”; EGA IV (5.11.4), “necessity”; EGA IV (7.2.2), “a) => b)”.

> **[Stacks, Tag 0BK3], the implication (1) ⇒ (2).** Let `j : U ⟶ X` be an open immersion of
> schemes with `X` locally Noetherian and let `F` be a quasi-coherent `𝒪_U`-module whose direct
> image `j_* F` is coherent. Then for every point `x` of `U` admitting a monomorphism
> `i_{x,*} 𝒪_{W_x} ⟶ F`, every point `z` of the reduced closure of `{j x}` whose image in `X` lies
> outside `U`, and every associated prime `𝔭` of the completion `𝒪^∧_{closure {x}, z}`, one has
> `dim(𝒪^∧_{closure {x}, z} ⧸ 𝔭) ≥ 2`.
>
> This is clause (2) of the source, asserted at every triple rather than at one fixed in advance,
> and with the source's own dimension bound. The monomorphism replaces the source's
> `x ∈ Ass(F)`, which enters the argument only through the map it produces; it is the one
> hypothesis of the source's statement that is not yet discharged.

```lean
theorem two_le_ringKrullDim_quotient_completedStalk_of_isCoherent_pushforward
    {U X : Scheme.{u}} [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    {F : U.Modules} [F.IsQuasicoherent]
    (hF : ((Scheme.Modules.pushforward j).obj F).IsCoherent) :
    ∀ (x : U) (φ : pointClosureStructureSheaf x ⟶ F), Mono φ →
      ∀ I : X.IdealSheafData,
        I = Scheme.IdealSheafData.vanishingIdeal (Closeds.closure ({j x} : Set X)) →
        ∀ z : I.subscheme, I.subschemeι z ∉ j.opensRange →
          ∀ p : PrimeSpectrum (I.subscheme.completedLocalRingCat z),
            IsAssociatedPrimeStacks (I.subscheme.completedLocalRingCat z)
              (I.subscheme.completedLocalRingCat z) p.asIdeal →
            2 ≤ ringKrullDim (I.subscheme.completedLocalRingCat z ⧸ p.asIdeal)
```

**`Stacks.AlgebraicGeometry.CoherentPushforwardCriterion.not_isCoherent_pushforward_of_isAssociatedPrime_completedStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/PointClosureCompletionObstruction.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/PointClosureCompletionObstruction.lean#L129). The attribute's comment: “(1) implies (2), contrapositive at one point, for a one-dimensional associated quotient of the completion and given a monomorphism from the structure sheaf of the point closure”. References: EGA IV (5.11.4), “necessity”.

> **[Stacks, Tag 0BK3], the implication (1) ⇒ (2), in contrapositive form at a single point.**
> Let `j : U ⟶ X` be an open immersion of schemes with `X` locally Noetherian, let `F` be a
> quasi-coherent `𝒪_U`-module and let `x` be a point of `U`. Write `W_x` for the reduced closure
> of `{x}` in `U` and `closure {x}` for the reduced closure of `{j x}` in `X`. Suppose there is a
> monomorphism `i_{x,*} 𝒪_{W_x} ⟶ F`, and suppose `z` is a point of `closure {x}` whose image in
> `X` lies outside `U` such that the completion `𝒪^∧_{closure {x}, z}` has an associated prime `𝔭`
> with `dim(𝒪^∧_{closure {x}, z} ⧸ 𝔭) = 1`. Then `j_* F` is not coherent.
>
> This is the failure of clause (2) of the source at `x` and `z` obstructing clause (1). The
> monomorphism replaces the source's `x ∈ Ass(F)`, which enters the argument only through the map
> it produces; and the associated quotient is assumed one-dimensional rather than at most
> one-dimensional. See the module documentation for why neither restriction is avoidable here.

```lean
theorem not_isCoherent_pushforward_of_isAssociatedPrime_completedStalk {U X : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j] (x : U)
    {F : U.Modules} [F.IsQuasicoherent]
    (φ : pointClosureStructureSheaf x ⟶ F) [Mono φ]
    {I : X.IdealSheafData}
    (hI : I = Scheme.IdealSheafData.vanishingIdeal (Closeds.closure ({j x} : Set X)))
    (z : I.subscheme) (hz : I.subschemeι z ∉ j.opensRange)
    {p : PrimeSpectrum (I.subscheme.completedLocalRingCat z)}
    (hp : IsAssociatedPrimeStacks (I.subscheme.completedLocalRingCat z)
      (I.subscheme.completedLocalRingCat z) p.asIdeal)
    (hdim : ringKrullDim (I.subscheme.completedLocalRingCat z ⧸ p.asIdeal) = 1) :
    ¬ ((Scheme.Modules.pushforward j).obj F).IsCoherent
```

**`Stacks.LocalCohomology.isCoherent_pushforward_iff_forall_two_le_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/KollarCriterionAssembled.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/KollarCriterionAssembled.lean#L126).

> **Kollár's criterion.** Let `j : U ⟶ X` be an open immersion with `X`
> locally Noetherian and let `F` be a coherent `𝒪_U`-module. Then `j_*F` is coherent if and only
> if for every associated point `x` of `F`, every point `w` of the reduced closure of `{j x}` in
> `X` whose image lies outside the image of `j`, and every associated prime `𝔭` of the completed
> local ring of that closure at `w`, one has `2 ≤ dim` of the corresponding quotient.

```lean
theorem isCoherent_pushforward_iff_forall_two_le_ringKrullDim
    {U X : Scheme.{u}} [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    (F : U.Modules) [F.IsCoherent] :
    ((Scheme.Modules.pushforward j).obj F).IsCoherent ↔
      ∀ x : U, x ∈ Stacks.Divisors.associatedPoints F →
        ∀ w : (Scheme.IdealSheafData.vanishingIdeal
          (Closeds.closure ({j x} : Set X))).subscheme,
          (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({j x} : Set X))).subschemeι.base w ∉ Set.range j.base →
          ∀ p : Ideal (AdicCompletion (maximalIdeal ((Scheme.IdealSheafData.vanishingIdeal
              (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w))
            ((Scheme.IdealSheafData.vanishingIdeal
              (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w)),
            IsAssociatedPrimeStacks
              (AdicCompletion (maximalIdeal ((Scheme.IdealSheafData.vanishingIdeal
                  (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w))
                ((Scheme.IdealSheafData.vanishingIdeal
                  (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w))
              (AdicCompletion (maximalIdeal ((Scheme.IdealSheafData.vanishingIdeal
                  (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w))
                ((Scheme.IdealSheafData.vanishingIdeal
                  (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w)) p →
            (2 : WithBot ℕ∞) ≤ ringKrullDim (AdicCompletion
              (maximalIdeal ((Scheme.IdealSheafData.vanishingIdeal
                (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w))
              ((Scheme.IdealSheafData.vanishingIdeal
                (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk w) ⧸ p)
```

## Tag 0BL9, a lemma

[Tag 0BL9](https://stacks.math.columbia.edu/tag/0BL9) in the Stacks Project.

**`Stacks.LocalCohomology.finite_localCohomologyModule_one_iff_forall_ringKrullDim_ne_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/FirstLocalCohomologyKollar.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/FirstLocalCohomologyKollar.lean#L62).

> **[Stacks, Tag 0BL9].** Let `A` be a Noetherian ring, `I` an ideal, `Z = V(I)` and `M` a
> finite `A`-module. Then `H¹_Z(M)` is a finite `A`-module if and only if for every prime `𝔭`
> associated to `M` with `I ⊄ 𝔭`, and every prime `𝔮 ⊇ 𝔭 + I`, the completion of `(A/𝔭)_𝔮` has no
> associated prime `𝔯` with `dim((A/𝔭)^∧_𝔮 / 𝔯) = 1`.
>
> Kollár's criterion, [Stacks, Tag 0BK3], enters at the open immersion `U = Spec A \ Z ⟶ Spec A`
> and the coherent module `M̃|_U`, as `isCoherent_pushforward_iff_forall_two_le_ringKrullDim`. The
> rest of the proof is the composite of
> `finite_localCohomologyModule_one_iff_isCoherent_pushforward`, which turns finiteness of
> `H¹_Z(M)` into coherence of the direct image, and the translation of the geometric condition:
> `isAssociatedPoint_tilde_iff` together with `isAssociatedPoint_restrict_iff` identifies the
> associated points of `M̃|_U` with the associated primes of `M` outside `Z`,
> `forall_adicCompletion_pointClosure_iff` and `forall_quotientPrime_iff` rewrite the condition at
> the reduced closure of such a point as a condition on the completions of `(A/𝔭)_𝔮`, and
> `one_le_ringKrullDim_quotient_adicCompletion_localization` trades `2 ≤ dim` for `dim ≠ 1`.

```lean
theorem finite_localCohomologyModule_one_iff_forall_ringKrullDim_ne_one (A : Type u) [CommRing A]
    [IsNoetherianRing A] (I : Ideal A) (M : ModuleCat.{u} A) [Module.Finite A M] :
    Module.Finite A (localCohomologyModule A I I.fg_of_isNoetherianRing M 1) ↔
      ∀ (p q : PrimeSpectrum A), IsAssociatedPrimeStacks A M p.asIdeal → ¬ I ≤ p.asIdeal →
        ∀ hpq : p.asIdeal ≤ q.asIdeal, I ≤ q.asIdeal →
        let J := q.asIdeal.map (Ideal.Quotient.mk p.asIdeal)
        letI : J.IsPrime := Ideal.isPrime_map_quotientMk_of_isPrime hpq
        let B := Localization.AtPrime J
        let R := AdicCompletion (J.map (algebraMap (A ⧸ p.asIdeal) B)) B
        ∀ r : Ideal R, IsAssociatedPrimeStacks R R r → ringKrullDim (R ⧸ r) ≠ 1
```

## Tag 0AWB, a lemma

[Tag 0AWB](https://stacks.math.columbia.edu/tag/0AWB) in the Stacks Project.

**`AlgebraicGeometry.isCoherent_pushforward_iff_two_le_ringKrullDim_stalk_pointClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/UniversallyCatenaryDimension.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/CoherentPushforwardCriterion/UniversallyCatenaryDimension.lean#L129). References: EGA IV (5.11.4), “(ii)”.

> **[Stacks, Tag 0AWB].** Let `j : U ⟶ X` be an open immersion with `X` locally Noetherian and
> universally catenary, and suppose the formal fibres of `𝒪_{X, z}` satisfy `(S₁)` for every point
> `z` outside `U`. For a coherent `𝒪_U`-module `ℱ`, the direct image `j_* ℱ` is coherent exactly
> when `dim(𝒪_{closure {x}, z}) ≥ 2` for every associated point `x` of `ℱ` and every point `z` of
> the reduced closure of `{j x}` lying outside `U`.
>
> The associated-prime criterion of [Stacks, Tag 0BK3] is supplied by
> `Stacks.LocalCohomology.isCoherent_pushforward_iff_forall_two_le_ringKrullDim`, and
> `two_le_ringKrullDim_quotient_completedStalk_iff_two_le_ringKrullDim_stalk` collapses its
> condition pointwise to the dimension of the local ring itself.

```lean
theorem isCoherent_pushforward_iff_two_le_ringKrullDim_stalk_pointClosure
    {U X : Scheme.{u}} [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j]
    {F : U.Modules} [F.IsCoherent]
    (hX : Scheme.IsUniversallyCatenary X)
    (hFibres : ∀ z : X, z ∉ j.opensRange →
      ∀ q : PrimeSpectrum (X.presheaf.stalk z),
        HasSerreCondition
          (X.completedLocalRing z ⊗[X.presheaf.stalk z] q.asIdeal.ResidueField) 1) :
    ((Scheme.Modules.pushforward j).obj F).IsCoherent ↔
      ∀ x : U, x ∈ Stacks.Divisors.associatedPoints F →
        ∀ y : (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({j x} : Set X))).subscheme,
          (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({j x} : Set X))).subschemeι y ∉ j.opensRange →
          2 ≤ ringKrullDim ((Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({j x} : Set X))).subscheme.presheaf.stalk y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.8, Tag 0BL8](https://stacks.math.columbia.edu/tag/0BL8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
