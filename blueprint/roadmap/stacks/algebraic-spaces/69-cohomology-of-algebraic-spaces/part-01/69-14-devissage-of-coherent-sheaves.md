---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_shortExact_coherent_supportOfSheaf_subset, AlgebraicGeometry.Space.exists_mono_modulePushforward_idealSum_of_schemeTheoreticSupport, AlgebraicGeometry.Space.hasIdealDevissage_of_isCoherent, AlgebraicGeometry.Space.property_of_ideal_pushforward_and_extensions, AlgebraicGeometry.Space.property_of_isCoherent_of_hasGenericSubsheaves, AlgebraicGeometry.Space.property_of_isCoherent_of_integralWitness
statement: formalized
proof: formalized
---

# 69.14 Devissage of coherent sheaves

Section 69.14 of the Stacks Project, [Tag 07UN](https://stacks.math.columbia.edu/tag/07UN). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07UP, a lemma

[Tag 07UP](https://stacks.math.columbia.edu/tag/07UP) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_shortExact_coherent_supportOfSheaf_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentSupportSeparation.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentSupportSeparation.lean#L180).

> **Stacks 07UP.** Let `X` be a Noetherian algebraic space over a scheme `S` and let `F` be a
> coherent `𝒪_X`-module whose support is the union `Z ∪ Z'` of two closed subsets of `|X|`.  Then
> there is a short exact sequence `0 → 𝒢' → F → 𝒢 → 0` of coherent `𝒪_X`-modules with `𝒢'`
> supported in `Z'` and `𝒢` supported in `Z`.
>
> The sequence produced is the canonical one: `𝒢'` is the subsheaf of sections of `F` supported
> in `Z'` and `𝒢` is the quotient of `F` by it.  Quasi-coherence of `𝒢'` is part (3) of
> Stacks 0859, whose hypotheses hold because the complement of `Z'` is an open subspace of `X`
> and its inclusion is quasi-compact, `X` being Noetherian; `𝒢'` is then coherent by Stacks 07UD
> and `𝒢` by Stacks 07UC.

```lean
theorem exists_shortExact_coherent_supportOfSheaf_subset
    (hTop : B.Contains (⊤_ Scheme.{u})) (hN : IsNoetherian B S hS hTop X.1)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (Z Z' : Set (points B S hS X.1)) (hZ : IsClosed Z) (hZ' : IsClosed Z')
    (hsupp : supportOfSheaf B S hS X.1 (moduleAddSheaf B S hS X.1 X.2 F) = Z ∪ Z') :
    ∃ (G' G : Modules.{u, u} B S hS X.1 X.2) (i : G' ⟶ F) (p : F ⟶ G) (w : i ≫ p = 0),
      (ShortComplex.mk i p w).ShortExact ∧ IsCoherent B S hS X.1 X.2 G' ∧
        IsCoherent B S hS X.1 X.2 G ∧
        supportOfSheaf B S hS X.1 (moduleAddSheaf B S hS X.1 X.2 G') ⊆ Z' ∧
        supportOfSheaf B S hS X.1 (moduleAddSheaf B S hS X.1 X.2 G) ⊆ Z
```

## Tag 07UQ, a lemma

[Tag 07UQ](https://stacks.math.columbia.edu/tag/07UQ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_mono_modulePushforward_idealSum_of_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentIrreducibleIdealInjection.lean, line 674](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentIrreducibleIdealInjection.lean#L674).

> **[Stacks, Tag 07UQ].**  Let `X` be a Noetherian algebraic space over `S` and let `ℱ` be a
> coherent `𝒪_X`-module whose scheme-theoretic support `i : Z → X` is reduced with `|Z|`
> irreducible.  Then there are an integer `r > 0`, a nonzero quasi-coherent sheaf of ideals
> `ℐ ⊆ 𝒪_Z` and an injective map of coherent modules `i_*(ℐ^{⊕ r}) → ℱ` whose cokernel is
> supported on a proper closed subspace of `Z`, namely on the image of a closed `T ⊊ |Z|`.
>
> The scheme-theoretic support is a closed subspace (it is part of the conclusion), `ℱ = i_*𝒢` for
> a quasi-coherent `𝒪_Z`-module `𝒢` by [Stacks, Tag 07U0], `𝒢` is coherent by
> [Stacks, Tag 07UG], and its support is all of `|Z|` because the support of `ℱ` is the image of
> `|Z|` and `i` is injective on points.  The case `Z = X`,
> `AlgebraicGeometry.Space.exists_mono_biproduct_idealSheaf_cokernel_support_subset`, applies to
> `𝒢` on the Noetherian space `Z`; the direct image is exact, so it keeps the injection and
> carries the cokernel to the cokernel, whose support is then in the image of `T`.  The source
> `i_*(ℐ^{⊕ r})` is quasi-coherent, the direct image along a closed immersion preserving
> quasi-coherence, and it is a submodule of the coherent `ℱ`, hence coherent by
> [Stacks, Tag 07UD].

```lean
theorem exists_mono_modulePushforward_idealSum_of_schemeTheoreticSupport
    (noeth : IsNoetherian B S hS hZt X.1) (F : Modules.{u, u} B S hS X.1 X.2)
    (coh : IsCoherent B S hS X.1 X.2 F)
    (redIrr : IsReducedIrreducible B S hS (schemeTheoreticSupport B S hS X F)) :
    ∃ hZ : IsClosedSubspace B S hS (schemeTheoreticSupport B S hS X F),
      ∃ (r : ℕ) (I : (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS
          (closedSubfunctorSpace B S hS hZ).1 (closedSubfunctorSpace B S hS hZ).2).O))).Submodule),
        I.toSheafOfModules.IsQuasicoherentOnSite ∧ 0 < r ∧ I ≠ ⊥ ∧
        IsCoherent B S hS X.1 X.2 ((modulePushforward B S hS (closedSubfunctorι B S hS hZ)).obj
          (⨁ fun _ : Fin r => I.toSheafOfModules)) ∧
        ∃ φ : (modulePushforward B S hS (closedSubfunctorι B S hS hZ)).obj
            (⨁ fun _ : Fin r => I.toSheafOfModules) ⟶ F, Mono φ ∧
          ∃ (Q : Modules.{u, u} B S hS X.1 X.2) (q : F ⟶ Q) (w : φ ≫ q = 0),
            Nonempty (IsColimit (CokernelCofork.ofπ q w)) ∧
            ∃ T : Set (points B S hS (schemeTheoreticSupport B S hS X F).toFunctor),
              IsClosed T ∧ T ≠ Set.univ ∧
              supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj Q) ⊆
                pointsMap B S hS _ (closedSubfunctorι B S hS hZ).hom '' T
```

## Tag 07UR, a lemma

[Tag 07UR](https://stacks.math.columbia.edu/tag/07UR) in the Stacks Project.

**`AlgebraicGeometry.Space.hasIdealDevissage_of_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageFiltration.lean, line 872](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageFiltration.lean#L872).

> **Stacks Project, Tag 07UR.**  Let `X` be a Noetherian algebraic space over a scheme `S`
> and let `F` be a coherent `𝒪_X`-module.  Then `F` carries a filtration
>
> `0 = F₀ ⊆ F₁ ⊆ … ⊆ F_m = F`
>
> by coherent submodules such that for each `j` there are a reduced closed subspace `Z_j ⊆ X`
> with `|Z_j|` irreducible and a quasi-coherent sheaf of ideals `I_j ⊆ 𝒪_{Z_j}` with
> `F_j / F_{j-1} ≅ (Z_j → X)_* I_j`.
>
> The filtration is produced as a structure by
> `AlgebraicGeometry.Space.hasTagFiltration_of_isCoherent` and read in this existential form by
> `AlgebraicGeometry.Space.hasIdealDevissage_of_hasTagFiltration`.

```lean
theorem hasIdealDevissage_of_isCoherent (terminal : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (noeth : IsNoetherian B S hS terminal X.1)
    (M : Modules.{u, u} B S hS X.1 X.2) (coh : IsCoherent B S hS X.1 X.2 M) :
    HasIdealDevissage B S hS X M
```

## Tag 07US, a lemma

[Tag 07US](https://stacks.math.columbia.edu/tag/07US) in the Stacks Project.

**`AlgebraicGeometry.Space.property_of_ideal_pushforward_and_extensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageInduction.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageInduction.lean#L131).

> Let `X` be a Noetherian algebraic space over `S` and let `P` be a property of `𝒪_X`-modules
> such that
>
> 1. for a short exact sequence `0 → F₁ → F → F₂ → 0` of coherent modules, if `F₁` and `F₂` have
>    `P` then so does `F`;
> 2. for every reduced closed subspace `i : Z → X` with `|Z|` irreducible and every quasi-coherent
>    sheaf of ideals `I ⊆ 𝒪_Z`, `P` holds for `i_*I`.
>
> Suppose moreover that `X` has a point or that `P` holds for every zero module.  Then `P` holds
> for every coherent module on `X`.
>
> Without the alternative the statement fails when `|X|` is empty
> (`AlgebraicGeometry.Space.exists_isNoetherian_not_forall_property`).

```lean
theorem property_of_ideal_pushforward_and_extensions (X : AlgebraicSpaces B S hS)
    (noetherian : IsNoetherian B S hS B.contains_terminal X.1)
    (P : Modules.{u, u} B S hS X.1 X.2 → Prop)
    (nonempty_or_zero : Nonempty (points B S hS X.1) ∨
      ∀ M : Modules.{u, u} B S hS X.1 X.2, IsZero M → P M)
    (extensions : ClosedUnderCoherentExtensions B S hS X P)
    (idealPushforward : ∀ (Z : Subfunctor X.1) (closed : IsClosedSubspace B S hS Z),
      IsReducedIrreducible B S hS Z →
      ∀ I : QuasicoherentIdeals B S hS (closedSubfunctorSpace B S hS closed),
        P ((modulePushforward B S hS (closedSubfunctorι B S hS closed)).obj
          I.1.toSheafOfModules))
    (M : Modules.{u, u} B S hS X.1 X.2) (coherent : IsCoherent B S hS X.1 X.2 M) : P M
```

## Tag 07UT, a lemma

[Tag 07UT](https://stacks.math.columbia.edu/tag/07UT) in the Stacks Project.

**`AlgebraicGeometry.Space.property_of_isCoherent_of_hasGenericSubsheaves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageCriterion.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageCriterion.lean#L621).

> **Stacks Project, Tag 07UT.**  Let `X` be a Noetherian algebraic space over a scheme `S` and
> let `P` be a property of coherent `𝒪_X`-modules such that
>
> 1. for a short exact sequence `0 → F₁ → F → F₂ → 0` of coherent modules, if `F₁` and `F₂` have
>    `P` then so does `F`;
> 2. if `P` holds for `F^{⊕ r}` for some `r ≥ 1`, then it holds for `F`;
> 3. for every reduced closed subspace `i : Z → X` with `|Z|` irreducible there is a coherent
>    `𝒪_Z`-module `𝒢` with `Supp(𝒢) = Z` such that for every nonzero quasi-coherent sheaf of ideals
>    `ℐ ⊆ 𝒪_Z` there is a quasi-coherent `𝒢' ⊆ ℐ𝒢` with `Supp(𝒢/𝒢')` a proper closed subset of `|Z|`
>    and `P(i_*𝒢')`
>
> and such that `P` holds for the zero module.  Then `P` holds for every coherent `𝒪_X`-module.
>
> The source does not list the zero module among its hypotheses, and its conclusion fails without
> it: the property "is nonzero" satisfies (1), (2) and (3) — in (3) take `𝒢 = 𝒪_Z` and `𝒢' = ℐ𝒪_Z`
> — and does not hold for the zero module.  The source's proof runs over the nonempty supports
> only.
>
> The proof is the source's Noetherian induction on the support of `F`, run over the closed
> subsets of `|X|`, a Noetherian topological space by Stacks 04ZF.  A module with empty support is
> zero; a reducible support is split by Stacks 07UP and (1) concludes; an irreducible support is
> `AlgebraicGeometry.Space.property_of_isIrreducible`.

```lean
theorem property_of_isCoherent_of_hasGenericSubsheaves
    (noeth : IsNoetherian B S hS B.contains_terminal X.1)
    (zero : ∀ M : Modules.{u, u} B S hS X.1 X.2, IsZero M → P M)
    (extension : ClosedUnderCoherentExtensions B S hS X P)
    (ofSum : ∀ F : Modules.{u, u} B S hS X.1 X.2, IsCoherent B S hS X.1 X.2 F →
      ∀ r : ℕ, 1 ≤ r → P (⨁ fun _ : Fin r => F) → P F)
    (generic : HasGenericSubsheaves B S hS X P)
    (F : Modules.{u, u} B S hS X.1 X.2) (coherent : IsCoherent B S hS X.1 X.2 F) : P F
```

## Tag 08AN, a lemma

[Tag 08AN](https://stacks.math.columbia.edu/tag/08AN) in the Stacks Project.

**`AlgebraicGeometry.Space.property_of_isCoherent_of_integralWitness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageHigherRankNoetherian.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CoherentDevissageHigherRankNoetherian.lean#L295). The attribute's comment: “corrected: |X| is also required to be nonempty, or P to hold on zero modules; without this the statement fails on an algebraic space with no points, for the property False”.

> **Stacks Project, Tag 08AN**, corrected as recorded in the errata.  Let `X` be a Noetherian
> algebraic space over a scheme `S` and let `P` be a property of coherent `𝒪_X`-modules such that
>
> 1. for a short exact sequence of coherent modules, if two out of three terms have `P` then so
>    does the third;
> 2. if `P` holds for the direct sum of `r ≥ 1` copies of a coherent module then it holds for that
>    module;
> 3. for every reduced closed subspace `Z ⊆ X` with `|Z|` irreducible there is a coherent module
>    on `X` whose scheme-theoretic support is `Z` and which has `P`.
>
> Then `P` holds for every coherent module on `X`, provided `|X|` is nonempty or `P` holds on zero
> modules (`h0`).
>
> The alternative `h0` is the correction: the source's statement fails on an algebraic space with
> no points (`AlgebraicGeometry.Space.not_forall_false_of_isEmpty_points`), and on such a space the
> zero module is the one coherent module, so `P` on zero modules is exactly what is missing there.
> On a space with a point `h0` holds by its first alternative and the statement is the source's.
> No result of another tag is carried: Stacks 07UR, the coherence of `i_*I` and Stacks 07UQ are
> theorems of the library, used through
> `AlgebraicGeometry.Space.property_of_integralWitness_and_twoOutOfThree_of_isNoetherian`, and on a
> space with a point `P` on zero modules follows from (1) and (3) by
> `AlgebraicGeometry.Space.forall_isZero_property_of_nonempty`.

```lean
theorem property_of_isCoherent_of_integralWitness (hZtop : B.Contains (⊤_ Scheme.{u}))
    (X : AlgebraicSpaces B S hS) (hX : IsNoetherian B S hS hZtop X.1)
    (P : Modules.{u, u} B S hS X.1 X.2 → Prop)
    (h0 : Nonempty (points B S hS X.1) ∨ ∀ M : Modules.{u, u} B S hS X.1 X.2, IsZero M → P M)
    (h1 : TwoOutOfThreeCoherent B S hS X P) (h2 : ClosedUnderCoherentDirectSumDescent B S hS X P)
    (h3 : HasCoherentWitnessOnIntegralSubspaces B S hS X P)
    (M : Modules.{u, u} B S hS X.1 X.2) (hM : IsCoherent B S hS X.1 X.2 M) : P M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.14, Tag 07UN](https://stacks.math.columbia.edu/tag/07UN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
