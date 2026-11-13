---
declaration: section
origin: cited
lean: StacksDraft.Perfect.exists_away_bounded_free_complex_representing_of_fibre_vanishing_below, StacksDraft.Perfect.isPerfect_and_torAmplitude_iff_fibreCohomologyVanishes, StacksDraft.Perfect.isPerfect_iff_isPerfect_at_primes_of_isBoundedBelow_and_stalkwise_criteria, StacksDraft.ProjectiveAmplitude.hasProjectiveAmplitude_iff_perfect_iff_ext_vanishing, StacksDraft.Perfect.isPerfect_and_torAmplitude_of_flat_of_fibre_globalDimension_le, StacksDraft.Perfect.isPerfect_and_torAmplitude_of_flat_local_of_regular_closedFibre
statement: formalized
proof: formalized
---

# 15.79 Recognizing perfect complexes

Section 15.79 of the Stacks Project, [Tag 0G99](https://stacks.math.columbia.edu/tag/0G99). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BYP, a lemma

[Tag 0BYP](https://stacks.math.columbia.edu/tag/0BYP) in the Stacks Project.

**`StacksDraft.Perfect.exists_away_bounded_free_complex_representing_of_fibre_vanishing_below`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/MinimalRepresentative/PrincipalNeighbourhood.lean, line 756](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/MinimalRepresentative/PrincipalNeighbourhood.lean#L756).

> **Stacks 0BYP.** Let `R` be a commutative ring, `p` a prime of `R` and `K` a pseudo-coherent
> object of `D(R)` which is bounded below. Set `dᵢ = dim_{κ(p)} Hⁱ(K ⊗ᴸ_R κ(p))`. If `dᵢ = 0` for
> all `i < a`, then there is an `f ∈ R` outside `p` such that `K ⊗ᴸ_R R_f` is perfect and is
> represented by a complex over `R_f` concentrated in degrees `[a, b]` whose term in degree `i` is
> free of rank exactly `dᵢ`.

```lean
theorem exists_away_bounded_free_complex_representing_of_fibre_vanishing_below
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (K : DerivedCategory (ModuleCat.{max v u} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hbounded : ∃ c : ℤ, K.IsGE c) (a : ℤ) :
    let k := p.ResidueField
    let H := fun i : ℤ =>
      (DerivedCategory.homologyFunctor (ModuleCat.{max v u} k) i).obj
        ((totalDerivedExtensionScalars.{u, u, v} (algebraMap R k)).functor.obj K)
    (∀ i : ℤ, i < a → IsZero (H i)) →
      ∃ f : R, f ∉ p ∧
        let Kf := (totalDerivedExtensionScalars.{u, u, v}
          (algebraMap R (Localization.Away f))).functor.obj K
        IsPerfect Kf ∧
          ∃ (P : CochainComplex (ModuleCat.{max v u} (Localization.Away f)) ℤ) (b : ℤ),
            P.IsStrictlyGE a ∧ P.IsStrictlyLE b ∧
              (∀ i : ℤ, Nonempty (P.X i ≅ ModuleCat.of (Localization.Away f)
                (ULift.{v} (Fin (Module.finrank k (H i)) → Localization.Away f)))) ∧
              Nonempty (DerivedCategory.Q.obj P ≅ Kf)
```

## Tag 068V, a lemma

[Tag 068V](https://stacks.math.columbia.edu/tag/068V) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_and_torAmplitude_iff_fibreCohomologyVanishes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Local.lean, line 854](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Local.lean#L854).

> Let `R` be a commutative ring, let `a, b : ℤ` and let `K` be a pseudo-coherent object of the
> derived category of `R`-modules. Then `K` is perfect of Tor amplitude in `[a, b]` if and only if
> the cohomology of the derived fibre `K ⊗_R^L κ(p)` vanishes outside `[a, b]` for every prime ideal
> `p`, and it is enough to test this at the maximal ideals.
>
> Tor amplitude in `[a, b]` is expressed, as in [stacks 0658], by the existence of a flat
> representative supported in `[a, b]`; by [stacks 0654] this is exactly Tor amplitude in `[a, b]`,
> and the third clause spells that out: every bounded above flat representative of `K` — which is
> what computes `K ⊗_R^L M` — has vanishing cohomology outside `[a, b]` after tensoring with an
> arbitrary module.

```lean
theorem isPerfect_and_torAmplitude_iff_fibreCohomologyVanishes {R : Type u} [CommRing R]
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (a b : ℤ) :
    let perfectWithTorAmplitude :=
      IsPerfect K ∧ HasFlatRepresentative K a b ∧
        ∀ E : CochainComplex (ModuleCat.{max u v} R) ℤ, TorAmplitude.BoundedAbove E →
          TorAmplitude.IsComplexOfFlats E → Nonempty (K ≅ DerivedCategory.Q.obj E) →
            TorAmplitude.HasTorAmplitudeIn E a b
    let primeVanishes := ∀ q : PrimeSpectrum R, ∀ i : ℤ, i < a ∨ b < i →
      FibreCohomologyVanishes.{u, v} q.asIdeal K i
    let maximalVanishes := ∀ m : MaximalSpectrum R, ∀ i : ℤ, i < a ∨ b < i →
      FibreCohomologyVanishes.{u, v} m.asIdeal K i
    (perfectWithTorAmplitude ↔ primeVanishes) ∧ (primeVanishes ↔ maximalVanishes)
```

## Tag 068W, a lemma

[Tag 068W](https://stacks.math.columbia.edu/tag/068W) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_iff_isPerfect_at_primes_of_isBoundedBelow_and_stalkwise_criteria`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Local.lean, line 1250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Local.lean#L1250).

> Let `R` be a commutative ring and let `K` be a pseudo-coherent object of the derived category
> of `R`-modules. Then `K` perfect implies that every stalk `K ⊗_R^L R_p` is perfect; perfectness at
> all prime stalks, perfectness at all maximal stalks, and the vanishing of the cohomology of the
> derived fibre `K ⊗_R^L κ(p)` in all sufficiently low degrees at every prime or at every maximal
> ideal are equivalent; and if `K` is bounded below these are also equivalent to perfectness of `K`
> itself.
>
> The derived base change is the canonical one of [stacks 064H],
> `CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars`.

```lean
theorem isPerfect_iff_isPerfect_at_primes_of_isBoundedBelow_and_stalkwise_criteria
    {R : Type u} [CommRing R] (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) :
    let perfect := IsPerfect K
    let perfectAtPrimes := ∀ q : PrimeSpectrum R,
      IsPerfect ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, v}
        (algebraMap R (Localization.AtPrime q.asIdeal))).functor.obj K)
    let perfectAtMaximals := ∀ m : MaximalSpectrum R,
      IsPerfect ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, v}
        (algebraMap R (Localization.AtPrime m.asIdeal))).functor.obj K)
    let fibreVanishesBelowAtPrimes := ∀ q : PrimeSpectrum R,
      ∃ a : ℤ, ∀ i : ℤ, i < a →
        IsZero ((DerivedCategory.homologyFunctor
          (ModuleCat.{max u v} q.asIdeal.ResidueField) i).obj
            ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, v}
              (algebraMap R q.asIdeal.ResidueField)).functor.obj K))
    let fibreVanishesBelowAtMaximals := ∀ m : MaximalSpectrum R,
      ∃ a : ℤ, ∀ i : ℤ, i < a →
        IsZero ((DerivedCategory.homologyFunctor
          (ModuleCat.{max u v} m.asIdeal.ResidueField) i).obj
            ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, v}
              (algebraMap R m.asIdeal.ResidueField)).functor.obj K))
    (perfect → perfectAtPrimes) ∧
      (perfectAtPrimes ↔ perfectAtMaximals) ∧
      (perfectAtPrimes ↔ fibreVanishesBelowAtPrimes) ∧
      (perfectAtMaximals ↔ fibreVanishesBelowAtMaximals) ∧
      ((∃ a : ℤ, K.IsGE a) → (perfect ↔ perfectAtPrimes))
```

## Tag 0G9A, a lemma

[Tag 0G9A](https://stacks.math.columbia.edu/tag/0G9A) in the Stacks Project.

**`StacksDraft.ProjectiveAmplitude.hasProjectiveAmplitude_iff_perfect_iff_ext_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean, line 989](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean#L989).

> **Stacks 0G9A.** Let `K` be a pseudo-coherent object of `D(R)` and let `a, b` be integers.
> The following are equivalent:
> (1) `K` has projective amplitude in `[a, b]`;
> (2) `K` is perfect and has Tor amplitude in `[a, b]`, recorded by the existence of a flat
> representative supported in `[a, b]`;
> (3) `Ext^i(K, N) = 0` for every finitely presented `R`-module `N` and every `i ∉ [-b, -a]`;
> (4) `H^n(K) = 0` for `n > b` and `Ext^i(K, N) = 0` for every finitely presented `N` and every
> `i > -a`;
> (5) `H^n(K) = 0` for `n ∉ [a - 1, b]` and `Ext^{-a + 1}(K, N) = 0` for every finitely presented
> `N`.

```lean
theorem hasProjectiveAmplitude_iff_perfect_iff_ext_vanishing
    {R : Type u} [CommRing R] (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (a b : ℤ) :
    let moduleObject := fun N : ModuleCat.{max u v} R ↦
      (DerivedCategory.singleFunctor (ModuleCat.{max u v} R) 0).obj N
    let projectiveAmplitude := HasProjectiveAmplitude K a b
    let perfectTorAmplitude := Perfect.IsPerfect K ∧ Perfect.HasFlatRepresentative K a b
    let extOutsideVanishes := ∀ N : ModuleCat.{max u v} R, Module.FinitePresentation R N →
      ∀ i : ℤ, i ∉ Set.Icc (-b) (-a) →
        Subsingleton (DerivedCategory.Ext K (moduleObject N) i)
    let upperVanishing :=
      (∀ n : ℤ, b < n →
          IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) n).obj K)) ∧
        ∀ N : ModuleCat.{max u v} R, Module.FinitePresentation R N →
          ∀ i : ℤ, -a < i → Subsingleton (DerivedCategory.Ext K (moduleObject N) i)
    let endpointVanishing :=
      (∀ n : ℤ, n ∉ Set.Icc (a - 1) b →
          IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) n).obj K)) ∧
        ∀ N : ModuleCat.{max u v} R, Module.FinitePresentation R N →
          Subsingleton (DerivedCategory.Ext K (moduleObject N) (-a + 1))
    (projectiveAmplitude ↔ perfectTorAmplitude) ∧
      (perfectTorAmplitude ↔ extOutsideVanishes) ∧
      (extOutsideVanishes ↔ upperVanishing) ∧
      (upperVanishing ↔ endpointVanishing)
```

## Tag 068X, a lemma

[Tag 068X](https://stacks.math.columbia.edu/tag/068X) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_and_torAmplitude_of_flat_of_fibre_globalDimension_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FibreDescent.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FibreDescent.lean#L530). References: SGA 6 III (4.4), “(ii), special case”.

> **Stacks 068X.** Let `A → B` be a flat map of commutative rings, let `a, b : ℤ` and let `d ≥ 0`
> be an integer such that for every prime `p` of `A` the fibre ring `B ⊗_A κ(p)` has global dimension
> at most `d`. Let `K` be an object of the derived category of `B`-modules which is pseudo-coherent
> as a complex of `B`-modules and has Tor amplitude in `[a, b]` as a complex of `A`-modules. Then `K`
> is perfect as a complex of `B`-modules with Tor amplitude in `[a - d, b]`.
>
> Tor amplitude is recorded as in [stacks 068V]: by a flat representative supported in the window,
> which by [stacks 0654] is exactly Tor amplitude, together with the termwise condition on every
> bounded above flat representative. The hypothesis over `A` is the same condition for the complex of
> `A`-modules underlying `K`, and `hasTorAmplitudeIn_flatRepresentative_of_hasTorAmplitude` derives
> it from derived Tor amplitude against any certified derived tensor product.

```lean
theorem isPerfect_and_torAmplitude_of_flat_of_fibre_globalDimension_le [Module.Flat A B]
    (a b : ℤ) (d : ℕ)
    (hfibre : ∀ p : PrimeSpectrum A,
      ringGlobalDimension (TensorProduct A B p.asIdeal.ResidueField) ≤ (d : ℕ))
    (K : DerivedCategory (ModuleCat.{u} B))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hamp : ∀ F : CochainComplex (ModuleCat.{u} A) ℤ, TorAmplitude.BoundedAbove F →
      TorAmplitude.IsComplexOfFlats F →
      Nonempty ((ModuleCat.restrictScalars (algebraMap A B)).mapDerivedCategory.obj K ≅
        DerivedCategory.Q.obj F) → TorAmplitude.HasTorAmplitudeIn F a b) :
    IsPerfect K ∧ HasFlatRepresentative.{u, u} K (a - (d : ℤ)) b ∧
      ∀ E : CochainComplex (ModuleCat.{u} B) ℤ, TorAmplitude.BoundedAbove E →
        TorAmplitude.IsComplexOfFlats E → Nonempty (K ≅ DerivedCategory.Q.obj E) →
          TorAmplitude.HasTorAmplitudeIn E (a - (d : ℤ)) b
```

## Tag 09PC, a lemma

[Tag 09PC](https://stacks.math.columbia.edu/tag/09PC) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_and_torAmplitude_of_flat_local_of_regular_closedFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FibreDescent.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FibreDescent.lean#L620).

> **Stacks 09PC.** Let `A → B` be a flat local homomorphism of local rings, let `a, b : ℤ` and
> let `d ≥ 0` be an integer such that the closed fibre `B/m_A B` is regular of dimension `d`. Let `K`
> be an object of the derived category of `B`-modules which is pseudo-coherent as a complex of
> `B`-modules and whose derived fibre `K ⊗_A^L κ(m_A)` has cohomology only in the degrees `[a, b]`.
> Then `K` is perfect as a complex of `B`-modules with Tor amplitude in `[a - d, b]`.
>
> The source states the hypothesis over `A` as Tor amplitude in `[a, b]` and remarks that the weaker
> condition on the derived fibre suffices; it is that weaker hypothesis which is used here. Tor
> amplitude in the conclusion is recorded as in [stacks 068V]: by a flat representative supported in
> the window, which by [stacks 0654] is exactly Tor amplitude, together with the termwise condition
> on every bounded above flat representative. The derived fibre over `A` is computed on a bounded
> above flat representative of the complex of `A`-modules underlying `K`, which is what the termwise
> tensor product with `κ(m_A)` of such a representative is.

```lean
theorem isPerfect_and_torAmplitude_of_flat_local_of_regular_closedFibre [IsLocalRing B]
    [IsLocalHom (algebraMap A B)] [Module.Flat A B] (a b : ℤ) (d : ℕ)
    [IsRegularLocalRing (B ⧸ Ideal.map (algebraMap A B) (maximalIdeal A))]
    (hdim : ringKrullDim (B ⧸ Ideal.map (algebraMap A B) (maximalIdeal A)) = (d : WithBot ℕ∞))
    (K : DerivedCategory (ModuleCat.{u} B))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K)
    (hfibre : ∀ F : CochainComplex (ModuleCat.{u} A) ℤ, TorAmplitude.BoundedAbove F →
      TorAmplitude.IsComplexOfFlats F →
      Nonempty ((ModuleCat.restrictScalars (algebraMap A B)).mapDerivedCategory.obj K ≅
        DerivedCategory.Q.obj F) →
      ∀ i : ℤ, (i < a ∨ b < i) →
        IsZero ((TorAmplitude.tensorComplex F
          (ModuleCat.of A (maximalIdeal A).ResidueField)).homology i)) :
    IsPerfect K ∧ HasFlatRepresentative.{u, u} K (a - (d : ℤ)) b ∧
      ∀ E : CochainComplex (ModuleCat.{u} B) ℤ, TorAmplitude.BoundedAbove E →
        TorAmplitude.IsComplexOfFlats E → Nonempty (K ≅ DerivedCategory.Q.obj E) →
          TorAmplitude.HasTorAmplitudeIn E (a - (d : ℤ)) b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.79, Tag 0G99](https://stacks.math.columbia.edu/tag/0G99)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
