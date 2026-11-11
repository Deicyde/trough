---
declaration: section
origin: cited
lean: exists_uniform_tor_transition_eq_zero_of_pow_smul_eq_bot, Stacks.Blowup.exists_pow_le_annihilator_tor_affineBlowupAlgebra, Stacks.Blowup.exists_threshold_nonempty_derivedGlobalSectionsTwistedPullback_iso_derivedTensorIdealPow, Stacks.Blowup.exists_pow_le_annihilator_homology_derivedPullback, Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow_blowup, Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow, Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow_of_card_le_one, exists_uniform_tor_transition_eq_zero_of_pow_le_annihilator_tor'
statement: formalized
proof: formalized
---

# 51.21 A bit of uniformity, II

Section 51.21 of the Stacks Project, [Tag 0G9W](https://stacks.math.columbia.edu/tag/0G9W). 9 tags here are carried by 31 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G9X, a lemma

[Tag 0G9X](https://stacks.math.columbia.edu/tag/0G9X) in the Stacks Project.

**`exists_uniform_tor_transition_eq_zero_of_pow_smul_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorTransition.lean, line 816](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorTransition.lean#L816).

> **Stacks Project, Tag 0G9X.** For a fixed power `I ^ m` and a positive Tor degree, there is
> a uniform shift such that the transition from `A / I ^ n` to `A / I ^ (n - c)` induces the zero
> map on Tor against every module annihilated by `I ^ m`.

```lean
theorem exists_uniform_tor_transition_eq_zero_of_pow_smul_eq_bot
    {A : Type u} [CommRing A] [IsNoetherianRing A] (I : Ideal A) (m i : ℕ) (hi : 0 < i) :
    ∃ c : ℕ, ∀ (M : ModuleCat.{u} A),
      I ^ m • (⊤ : Submodule A M) = ⊥ → ∀ n : ℕ, c ≤ n →
        ((Tor (ModuleCat.{u} A) i).obj M).map
          (ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
            (Ideal.pow_le_pow_right (Nat.sub_le n c)))) = 0
```

## Tag 0G9Y, a lemma

[Tag 0G9Y](https://stacks.math.columbia.edu/tag/0G9Y) in the Stacks Project.

**`Stacks.Blowup.exists_pow_le_annihilator_tor_affineBlowupAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Blowup/TorAnnihilation.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Blowup/TorAnnihilation.lean#L485).

> **Uniform annihilation of the high `Tor` modules of an affine blowup algebra.**
> Let `I = (a₁, …, a_t)` be an ideal of a Noetherian ring `A`, let `a = a₁`, and let `B = A[I/a]`
> be the affine blowup algebra. There is a `c > 0` such that `Iᶜ` annihilates `Torᴬᵢ(B, M)` for
> every `A`-module `M` and every `i ≥ t`.

```lean
public theorem exists_pow_le_annihilator_tor_affineBlowupAlgebra
    {A : Type u} [CommRing A] [IsNoetherianRing A] {n : ℕ} (g : Fin (n + 1) → A)
    (I : Ideal A) (hI : I = Ideal.span (Set.range g))
    (S : Type u) [CommRing S] [Algebra A S] [IsLocalization.Away (g 0) S] :
    ∃ c : ℕ, 0 < c ∧ ∀ (M : ModuleCat.{u} A) (i : ℕ), n + 1 ≤ i →
      I ^ c ≤ Module.annihilator A
        (((Tor (ModuleCat.{u} A) i).obj
          (ModuleCat.of A ↥(affineBlowupAlgebra I (g 0) S))).obj M)
```

## Tag 0G9Z, a lemma

[Tag 0G9Z](https://stacks.math.columbia.edu/tag/0G9Z) in the Stacks Project.

**`Stacks.Blowup.exists_threshold_nonempty_derivedGlobalSectionsTwistedPullback_iso_derivedTensorIdealPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/TwistedSectionsIdealPow.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/TwistedSectionsIdealPow.lean#L168).

> **Cohomology of the twisted derived pullback along the affine blowup, unconditionally.** Let
> `A` be a Noetherian ring, `I ⊆ A` an ideal and `p : X ⟶ Spec A` the blowup of `Spec A` in `I`.
> There is a `q₀` such that for every `n ≥ q₀` and **any** `A`-module `M`,
>
> `RΓ(X, Lp^*(M̃) ⊗^𝐋_{𝒪_X} 𝒪_X(n)) ≅ M ⊗^𝐋_A Iⁿ`  in `D(A)`.

```lean
theorem exists_threshold_nonempty_derivedGlobalSectionsTwistedPullback_iso_derivedTensorIdealPow
    [IsNoetherianRing A] :
    ∃ q₀ : ℕ, ∀ n : ℕ, q₀ ≤ n →
      ∀ M : ModuleCat.{u} (CommRingCat.of A),
        Nonempty ((AlgebraicGeometry.derivedGlobalSectionsOver (toSpec I)).obj
            (((Stacks.Cohomology.TorAmplitude.derTensor (blowUpRingedSpace I)).tensor.obj
                ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
                  (toSpecRingedSpace I)).obj (DerivedCategory.Q.obj (tildeComplex
                    ((CochainComplex.singleFunctor (ModuleCat.{u} (CommRingCat.of A)) 0).obj
                      M))))).obj
              (DerivedCategory.Q.obj
                ((CochainComplex.singleFunctor (BlowUpModules I) 0).obj
                  (blowUpTwist I (n : ℤ))))) ≅
          ((CochainComplex.DerivedTensor.canonicalDerivedTensorProduct A).tensor.obj
              (DerivedCategory.Q.obj
                ((CochainComplex.singleFunctor (ModuleCat.{u} A) 0).obj M))).obj
            (DerivedCategory.Q.obj
              ((CochainComplex.singleFunctor (ModuleCat.{u} A) 0).obj
                (ModuleCat.of A (I ^ n : Ideal A)))))
```

## Tag 0GA0, a lemma

[Tag 0GA0](https://stacks.math.columbia.edu/tag/0GA0) in the Stacks Project.

**`Stacks.Blowup.exists_pow_le_annihilator_homology_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/DerivedPullbackAnnihilation.lean, line 505](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/DerivedPullbackAnnihilation.lean#L505).

> **Stacks Project, Tag 0GA0.** Let `A` be a Noetherian ring and `I = (a₀, …, a_n) ⊆ A` an
> ideal with `t = n + 1` generators, and let `p : X ⟶ Spec A` be the blowup of `Spec A` in `I`,
> that is `X = Proj(⨁_{m ≥ 0} Iᵐ)`. There is an integer `c > 0`, depending only on `A` and `I`,
> such that for every `A`-module `M` the cohomology sheaves `H^j(Lp^*M̃)` are annihilated by `Iᶜ`
> for all `j ≤ -t`.
>
> Annihilation is expressed on sections: an element `r ∈ Iᶜ`, viewed as a global section of `X`
> through `p` and restricted to an open `U`, kills every section of `H^j(Lp^*M̃)` over `U`.

```lean
theorem exists_pow_le_annihilator_homology_derivedPullback {n : ℕ} (g : Fin (n + 1) → A)
    (I : Ideal A) (hI : I = Ideal.span (Set.range g)) :
    ∃ c : ℕ, 0 < c ∧ ∀ (M : ModuleCat.{u} (CommRingCat.of A)) (j : ℤ), j ≤ -((n : ℤ) + 1) →
      ∀ (U : (blowUpSpec I).Opens) (r : A), r ∈ I ^ c →
        ∀ s : Γ((DerivedCategory.homologyFunctor (blowUpSpec I).Modules j).obj
            ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
              (toSpecRingedSpace I)).obj (DerivedCategory.Q.obj (tildeComplex
              ((CochainComplex.singleFunctor (ModuleCat.{u} (CommRingCat.of A)) 0).obj M)))), U),
          (blowUpSpec I).presheaf.map (homOfLE (show U ≤ ⊤ from le_top)).op
            ((toSpec I).appTop ((Scheme.ΓSpecIso (CommRingCat.of A)).inv r)) • s = 0
```

## Tag 0GA1, a lemma

[Tag 0GA1](https://stacks.math.columbia.edu/tag/0GA1) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow_blowup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/TorAnnihilationBlowup.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/TorAnnihilationBlowup.lean#L211).

> **Stacks Project, Tag 0GA1.** Let `A` be a Noetherian ring and let `I = (g 0, …, g (t-1))` be
> an ideal of `A` generated by at most `t` elements, as in the Situation of [Stacks, Tag 0G9W].
> There is an integer `m`, depending only on `A` and `I`, such that for *every* `A`-module `M` the
> modules `Tor_i^A(M, A/I^q)` are annihilated by `I^m` for all `i > t` and all `q ≥ 0`.
>
> Nothing is assumed. The spectral sequence the source's proof runs on is produced by
> `Stacks.Blowup.exists_hypercohomologySpectralSequence_abutsTo_tor_idealPow` on the blowup of
> `Spec A` in `I`, and the step from it to the filtration of `Tor_i^A(M, Iᑫ)` that
> `Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow` asks for is
> `Stacks.LocalCohomology.UniformityII`
> `.exists_pow_le_annihilator_tor_quotient_pow_of_abutsTo_restrictScalars`.

```lean
theorem exists_pow_le_annihilator_tor_quotient_pow_blowup [IsNoetherianRing A] {I : Ideal A}
    {t : ℕ} (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) :
    ∃ m : ℕ, ∀ (M : ModuleCat.{u} A) (i q : ℕ), t < i →
      I ^ m ≤ Module.annihilator A
        (((Tor' (ModuleCat.{u} A) i).obj M).obj (ModuleCat.of A (A ⧸ I ^ q)))
```

**`Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorAnnihilation.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorAnnihilation.lean#L208).

> **Stacks Project, Tag 0GA1.** Let `A` be a Noetherian ring and let `I = (g 0, …, g (t-1))` be
> an ideal of `A` generated by at most `t` elements, as in the Situation of [Stacks, Tag 0G9W].
> There is an integer `m`, depending only on `A` and `I`, such that for *every* `A`-module `M` the
> modules `Tor_i^A(M, A/I^q)` are annihilated by `I^m` for all `i > t` and all `q ≥ 0`.
>
> The hypothesis `hfilt` is the geometric input of the source's proof, which is not formalized
> here: for all `i ≥ t` and all `q ≥ q₀`, the module `Tor_i^A(M, I^q)` carries a filtration
> `⊤ = F 0, …, F d = ⊥` in `d` steps whose graded pieces are annihilated by `Iᶜ`. The source
> produces it from the hypercohomology spectral sequence [Stacks, Tag 0G9Q] of
> `Lp^*M̃(q)` on the blowup `p : X ⟶ Spec A` of `Spec A` in `I`, with `q₀ = q(A, I)`, with `d = t`
> by the vanishing [Stacks, Tag 071L] for the cover of `X` by the `t` affine charts, and with
> `c = c(A, I)` the exponent of [Stacks, Tag 0GA0]; the identification of the abutment with
> `Tor_i^A(M, I^q)` is [Stacks, Tag 0G9Z].
>
> Given `hfilt`, the exponent `m = max (d * c) q₀ + 1` works: above the threshold the filtration
> gives `I^{dc} • Tor_i^A(M, I^q) = 0` for `i ≥ t`, which the sequence `0 → I^q → A → A/I^q → 0`
> shifts to `A/I^q` for `i > t`, and for the remaining `q ≤ m` already `I^m ≤ I^q` annihilates
> `A/I^q` and hence `Tor_i^A(M, A/I^q)`.

```lean
theorem exists_pow_le_annihilator_tor_quotient_pow [IsNoetherianRing A] {I : Ideal A} {t : ℕ}
    (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) (q₀ d c : ℕ)
    (hfilt : ∀ (M : ModuleCat.{u} A) (i q : ℕ), t ≤ i → q₀ ≤ q →
      ∃ F : ℕ → Submodule A
          (((Tor' (ModuleCat.{u} A) i).obj M).obj (ModuleCat.of A ↥(I ^ q))),
        F 0 = ⊤ ∧ F d = ⊥ ∧ ∀ k, I ^ c • F k ≤ F (k + 1)) :
    ∃ m : ℕ, ∀ (M : ModuleCat.{u} A) (i q : ℕ), t < i →
      I ^ m ≤ Module.annihilator A
        (((Tor' (ModuleCat.{u} A) i).obj M).obj (ModuleCat.of A (A ⧸ I ^ q)))
```

**`Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow_of_card_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorAnnihilation.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorAnnihilation.lean#L295). The attribute's comment: “for an ideal generated by at most one element”.

> **Stacks Project, Tag 0GA1 for an ideal generated by at most one element.** Let `A` be a
> Noetherian ring and let `I = (g 0, …, g (t-1))` be an ideal generated by at most `t ≤ 1` elements.
> There is an integer `m`, depending only on `A` and `I`, such that for *every* `A`-module `M` the
> modules `Tor_i^A(M, A/I^q)` are annihilated by `I^m` for all `i > t` and all `q ≥ 0`. Nothing is
> assumed: the geometric input of `exists_pow_le_annihilator_tor_quotient_pow` is not needed here.
>
> For `t = 1` and `I = (a)` take `m = q₀`, an index at which the ascending chain of annihilators
> `ann(a) ⊆ ann(a²) ⊆ ⋯` stabilizes. For `q ≤ q₀` already `I^{q₀} ≤ I^q` annihilates `A/I^q`. For
> `q > q₀` the ideal `I^q = (a^q)` is the cyclic module `A ⧸ ann(a^q)` with `ann(a^q) = ann(a^{q₀})`
> annihilated by `a^{q₀}`, so one dimension shift gives `a^{q₀} · Tor_i^A(M, I^q) = 0` for `i ≥ 1`
> and a second, along `0 → I^q → A → A/I^q → 0`, gives the claim for `i > 1`. The case `t = 0`,
> where `I = 0`, is the degenerate case of `exists_pow_le_annihilator_tor_quotient_pow`.

```lean
theorem exists_pow_le_annihilator_tor_quotient_pow_of_card_le_one [IsNoetherianRing A]
    {I : Ideal A} {t : ℕ} (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) (ht : t ≤ 1) :
    ∃ m : ℕ, ∀ (M : ModuleCat.{u} A) (i q : ℕ), t < i →
      I ^ m ≤ Module.annihilator A
        (((Tor' (ModuleCat.{u} A) i).obj M).obj (ModuleCat.of A (A ⧸ I ^ q)))
```

## Tag 0GA2, a lemma

[Tag 0GA2](https://stacks.math.columbia.edu/tag/0GA2) in the Stacks Project.

**`exists_uniform_tor_transition_eq_zero_of_pow_le_annihilator_tor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorTransition.lean, line 1227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformTorTransition.lean#L1227).

> **Stacks Project, Tag 0GA2.** Let `I = (g 0, …, g (t - 1))` be an ideal of a Noetherian ring
> `A` generated by at most `t` elements. There are `N` and `c`, depending only on `A`, `I` and `t`,
> such that the surjection `A / I ^ n ↠ A / I ^ (n - c)` induces the zero map
> `Tor_{t+1}^A(M, A/I^n) → Tor_{t+1}^A(M, A/I^{n-c})` for *every* `A`-module `M` and every
> `n ≥ N`. That `N` and `c` are produced before the module is seen is the whole content of the
> source's lemma.
>
> The power `I ^ c₁` annihilating `Tor_i^A(M, A/I^q)` for all `M`, all `i > t` and all `q`, which
> the source's induction starts from, is [Stacks, Tag 0GA1],
> `Stacks.LocalCohomology.UniformityII.exists_pow_le_annihilator_tor_quotient_pow_blowup`.

```lean
theorem exists_uniform_tor_transition_eq_zero_of_pow_le_annihilator_tor'
    {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A} {t : ℕ}
    (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) :
    ∃ N c : ℕ, ∀ (M : ModuleCat.{u} A) (n : ℕ), N ≤ n →
      ((Tor (ModuleCat.{u} A) (t + 1)).obj M).map
        (ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
          (Ideal.pow_le_pow_right (Nat.sub_le n c)))) = 0
```

## Tag 0GA3, a proposition

[Tag 0GA3](https://stacks.math.columbia.edu/tag/0GA3) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityII.exists_uniform_torMapVanishesAtSucc_quotientFactor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean#L142). The attribute's comment: “condition (7) of Tag 0G9V”.

> **Stacks Project, Tag 0GA3, condition (7) of Tag 0G9V.** Let `I = (g 0, …, g (t - 1))` be an
> ideal of a Noetherian ring `A` generated by at most `t` elements. There are `N` and `c`,
> depending only on `A`, `I` and `t`, such that for every `n ≥ N` the transition
> `A / I ^ n ↠ A / I ^ (n - c)` induces the zero map on `Tor _ (t + 1)` against every module.
>
> This is [Stacks, Tag 0GA2], `exists_uniform_tor_transition_eq_zero_of_pow_le_annihilator_tor'`,
> read through the braiding of the two models of `Tor`.

```lean
theorem exists_uniform_torMapVanishesAtSucc_quotientFactor [IsNoetherianRing A]
    {I : Ideal A} {t : ℕ} (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) :
    ∃ N c : ℕ, ∀ n : ℕ, N ≤ n →
      TorMapVanishesAtSucc
        (ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
          (Ideal.pow_le_pow_right (Nat.sub_le n c)))) t
```

**`Stacks.LocalCohomology.UniformityII.exists_uniform_extMapVanishesAbove_quotientFactor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean#L162). The attribute's comment: “condition (3) of Tag 0G9V”.

> **Stacks Project, Tag 0GA3, condition (3) of Tag 0G9V.** Let `I = (g 0, …, g (t - 1))` be an
> ideal of a Noetherian ring `A` generated by at most `t` elements. There are `N` and `c`,
> depending only on `A`, `I` and `t`, such that for every `n ≥ N` the transition
> `A / I ^ n ↠ A / I ^ (n - c)` induces the zero map
> `Ext ^ i (A / I ^ (n - c), M) → Ext ^ i (A / I ^ n, M)` for every module `M` and every `i > t`.
>
> As `A` is Noetherian and `A / I ^ n` is a finite `A`-module, all seven conditions of
> [Stacks, Tag 0G9V] are equivalent for the transition (`tfae_of_isNoetherianRing_of_finite`), so
> this is the assertion that the transition satisfies them; it is obtained from condition (7),
> `exists_uniform_torMapVanishesAtSucc_quotientFactor`.

```lean
theorem exists_uniform_extMapVanishesAbove_quotientFactor [IsNoetherianRing A]
    {I : Ideal A} {t : ℕ} (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) :
    ∃ N c : ℕ, ∀ n : ℕ, N ≤ n →
      ExtMapVanishesAbove
        (ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
          (Ideal.pow_le_pow_right (Nat.sub_le n c)))) t
```

**`Stacks.LocalCohomology.UniformityII.exists_uniform_hasLiftVanishingAbove_quotientFactor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean#L181). The attribute's comment: “condition (1) of Tag 0G9V”.

> **Stacks Project, Tag 0GA3, condition (1) of Tag 0G9V.** Let `I = (g 0, …, g (t - 1))` be an
> ideal of a Noetherian ring `A` generated by at most `t` elements. There are `N` and `c`,
> depending only on `A`, `I` and `t`, such that for every `n ≥ N` and every choice of projective
> resolutions of `A / I ^ n` and of `A / I ^ (n - c)`, the transition `A / I ^ n ↠ A / I ^ (n - c)`
> lifts to a map of resolutions whose components vanish in all homological degrees above `t`.
>
> It is obtained from condition (7), `exists_uniform_torMapVanishesAtSucc_quotientFactor`, by the
> equivalence of the conditions of [Stacks, Tag 0G9V] for a finite module over a Noetherian ring,
> `tfae_of_isNoetherianRing_of_finite`.

```lean
theorem exists_uniform_hasLiftVanishingAbove_quotientFactor [IsNoetherianRing A]
    {I : Ideal A} {t : ℕ} (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) :
    ∃ N c : ℕ, ∀ n : ℕ, N ≤ n →
      ∀ {P P' : CochainComplex (ModuleCat.{u} A) ℤ}
        (p : P ⟶ singleComplex (ModuleCat.of A (A ⧸ I ^ n)))
        (p' : P' ⟶ singleComplex (ModuleCat.of A (A ⧸ I ^ (n - c))))
        [CochainComplex.IsProjectiveResolution p]
        [CochainComplex.IsProjectiveResolution p'],
        HasLiftVanishingAbove p p'
          (ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
            (Ideal.pow_le_pow_right (Nat.sub_le n c)))) t
```

**`Stacks.LocalCohomology.UniformityII.exists_uniform_vanishingConditions_quotientFactor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingConditions.lean#L208). The attribute's comment: “all seven conditions of Tag 0G9V at e = t”.

> **Stacks Project, Tag 0GA3.** Let `I = (g 0, …, g (t - 1))` be an ideal of a Noetherian ring
> `A` generated by at most `t` elements. There are `N` and `c`, depending only on `A`, `I` and `t`,
> such that for every `n ≥ N` and every choice of projective resolutions of `A / I ^ n` and of
> `A / I ^ (n - c)`, the transition `A / I ^ n ↠ A / I ^ (n - c)` satisfies all seven conditions of
> [Stacks, Tag 0G9V] with `e = t`, in the order of the source: (1) a lift vanishing in all degrees
> above `t`, (2) a lift vanishing in degree `t + 1`, (3) the zero map on `Ext ^ i` for all `i > t`,
> (4) the zero map on `Ext ^ (t + 1)`, (5) the canonical class of degree `t + 1` pulls back to zero,
> (6) the zero map on `Tor _ i` for all `i > t`, (7) the zero map on `Tor _ (t + 1)`.
>
> All seven follow from condition (7), `exists_uniform_torMapVanishesAtSucc_quotientFactor`, by
> `tfae_of_isNoetherianRing_of_finite`.

```lean
theorem exists_uniform_vanishingConditions_quotientFactor [IsNoetherianRing A]
    {I : Ideal A} {t : ℕ} (g : Fin t → A) (hg : I = Ideal.span (Set.range g)) :
    ∃ N c : ℕ, ∀ n : ℕ, N ≤ n →
      ∀ {P P' : CochainComplex (ModuleCat.{u} A) ℤ}
        (p : P ⟶ singleComplex (ModuleCat.of A (A ⧸ I ^ n)))
        (p' : P' ⟶ singleComplex (ModuleCat.of A (A ⧸ I ^ (n - c))))
        [CochainComplex.IsProjectiveResolution p]
        [CochainComplex.IsProjectiveResolution p'],
        let α := ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
          (Ideal.pow_le_pow_right (Nat.sub_le n c)))
        HasLiftVanishingAbove p p' α t ∧ HasLiftVanishingAtSucc p p' α t ∧
          ExtMapVanishesAbove α t ∧ ExtMapVanishesAtSucc α t ∧
          CanonicalExtClassPullbackVanishes p p' α t ∧ TorMapVanishesAbove α t ∧
          TorMapVanishesAtSucc α t
```

## Tag 0GA4, a remark

[Tag 0GA4](https://stacks.math.columbia.edu/tag/0GA4) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityII.exists_uniform_vanishingConditions_quotientFactor_of_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingKrullDimension.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/UniformVanishingKrullDimension.lean#L142). The attribute's comment: “Tag 0GA3 with e = dim A for a local ring: all seven conditions of Tag 0G9V; the cd(A, I) question the remark raises is open in the source and is not stated”.

> **Stacks Project, Tag 0GA4.** Let `A` be a Noetherian local ring of Krull dimension `d` and
> let `I` be an ideal of `A`. There are `N` and `c` such that for every `n ≥ N` and every choice of
> projective resolutions of `A / I ^ n` and of `A / I ^ (n - c)`, the transition
> `A / I ^ n ↠ A / I ^ (n - c)` satisfies all seven conditions of [Stacks, Tag 0G9V] with `e = d`,
> in the order of the source: (1) a lift vanishing in all degrees above `d`, (2) a lift vanishing in
> degree `d + 1`, (3) the zero map on `Ext ^ i` for all `i > d`, (4) the zero map on
> `Ext ^ (d + 1)`, (5) the canonical class of degree `d + 1` pulls back to zero, (6) the zero map on
> `Tor _ i` for all `i > d`, (7) the zero map on `Tor _ (d + 1)`.
>
> This is the conclusion of [Stacks, Tag 0GA3] with `e = t` replaced by `e = dim A`; no bound on
> the number of generators of `I` enters the statement. All seven conditions follow from condition
> (7), `exists_uniform_torMapVanishesAtSucc_quotientFactor_of_ringKrullDim`, by
> `tfae_of_isNoetherianRing_of_finite`.

```lean
theorem exists_uniform_vanishingConditions_quotientFactor_of_ringKrullDim
    [IsNoetherianRing A] [IsLocalRing A] (I : Ideal A) (d : ℕ) (hdim : ringKrullDim A = d) :
    ∃ N c : ℕ, ∀ n : ℕ, N ≤ n →
      ∀ {P P' : CochainComplex (ModuleCat.{u} A) ℤ}
        (p : P ⟶ singleComplex (ModuleCat.of A (A ⧸ I ^ n)))
        (p' : P' ⟶ singleComplex (ModuleCat.of A (A ⧸ I ^ (n - c))))
        [CochainComplex.IsProjectiveResolution p]
        [CochainComplex.IsProjectiveResolution p'],
        let α := ModuleCat.ofHom (Submodule.factor (p := I ^ n) (p' := I ^ (n - c))
          (Ideal.pow_le_pow_right (Nat.sub_le n c)))
        HasLiftVanishingAbove p p' α d ∧ HasLiftVanishingAtSucc p p' α d ∧
          ExtMapVanishesAbove α d ∧ ExtMapVanishesAtSucc α d ∧
          CanonicalExtClassPullbackVanishes p p' α d ∧ TorMapVanishesAbove α d ∧
          TorMapVanishesAtSucc α d
```

## Tag 0GA5, a remark

[Tag 0GA5](https://stacks.math.columbia.edu/tag/0GA5) in the Stacks Project.

**`Stacks.LocalCohomology.UniformityII.nonempty_strictProIso_systemFour_systemOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/NoetherianSystemFour.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/NoetherianSystemFour.lean#L119). The attribute's comment: “if `P` is Noetherian, the system (4) is strictly pro-isomorphic to the system (1)”.

> **If `P` is Noetherian, the system (4) is strictly pro-isomorphic to the system (1).**
> Let `φ : P → A` be a ring map of Noetherian rings, `J ⊆ P` an ideal, `I = JA`, and `M` a
> bounded complex of finite `A`-modules. Then the inverse system `n ↦ M ⊗ᴸ_P P/Jⁿ⁺¹` in `D(A)` is
> isomorphic, in the strict pro-category of `D(A)`, to the system `n ↦ M/Iⁿ⁺¹M`. An isomorphism
> of the strict pro-category is in particular an isomorphism of pro-objects.

```lean
theorem nonempty_strictProIso_systemFour_systemOne [IsNoetherianRing P] [IsNoetherianRing A]
    (J : Ideal P) (I : Ideal A) (hI : I = J.map φ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i)) :
    Nonempty (proObj (systemFour φ M J) ≅
      proObj (Stacks.AdicSystem.DerivedReductionProIso.reductionComplexSystem I M ⋙
        DerivedCategory.Q))
```

**`Stacks.LocalCohomology.UniformityII.nonempty_proIso_systemFour_systemOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/NoetherianSystemFour.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/NoetherianSystemFour.lean#L136). The attribute's comment: “if `P` is Noetherian, the system (4) is pro-isomorphic to the system (1)”.

> **If `P` is Noetherian, the system (4) is pro-isomorphic to the system (1).**
> Let `φ : P → A` be a ring map of Noetherian rings, `J ⊆ P` an ideal, `I = JA`, and `M` a bounded
> complex of finite `A`-modules. Then the inverse systems `n ↦ M ⊗ᴸ_P P/Jⁿ⁺¹` and `n ↦ M/Iⁿ⁺¹M`
> in `D(A)` are pro-isomorphic.

```lean
theorem nonempty_proIso_systemFour_systemOne [IsNoetherianRing P] [IsNoetherianRing A]
    (J : Ideal P) (I : Ideal A) (hI : I = J.map φ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i)) :
    Nonempty (_root_.InverseSequence.ProIso (systemFour φ M J)
      (Stacks.AdicSystem.DerivedReductionProIso.reductionComplexSystem I M ⋙
        DerivedCategory.Q))
```

**`Stacks.LocalCohomology.UniformityII.isZero_tor_quotient_pow_idealOfVars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/PolynomialQuotientTorDimension.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/PolynomialQuotientTorDimension.lean#L228). The attribute's comment: “in the standard example, `A[x₁, …, x_r]/(x₁, …, x_r)ⁿ` has tor dimension at most `r` for all `n`”.

> `A[x₁, …, x_r]/(x₁, …, x_r)ⁿ` has Tor dimension at most `r` for all `n`: for every module `N`
> over `R = A[x₁, …, x_r]` and every `p > r`, `Tor_p^R(R/(x₁, …, x_r)ⁿ, N) = 0`.

```lean
theorem isZero_tor_quotient_pow_idealOfVars (n : ℕ) (N : ModuleCat.{u} (MvPolynomial (Fin r) A))
    {p : ℕ} (hp : r < p) :
    IsZero (((Tor' (ModuleCat.{u} (MvPolynomial (Fin r) A)) p).obj
      (ModuleCat.of _ (MvPolynomial (Fin r) A ⧸ idealOfVars (Fin r) A ^ n))).obj N)
```

**`Stacks.LocalCohomology.UniformityII.polynomialSystemFourIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/PolynomialSystemFour.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/PolynomialSystemFour.lean#L222). The attribute's comment: “the standard example: `M ⊗ᴸ_P P/Jⁿ = M ⊗ᴸ_{A[x]} A[x]/(x)ⁿ` for `P = ℤ[x₁, …, x_r]`”.

> **`M ⊗ᴸ_P P/Jⁿ = M ⊗ᴸ_{A[x]} A[x]/(x)ⁿ`.**  Let `P = R₀[x₁, …, x_r]` (the source takes
> `R₀ = ℤ`; at a universe `u` other than `0` one takes `R₀ = ULift ℤ`), let `P → A` send `xᵢ` to
> `gᵢ`, and `J = (x₁, …, x_r)`.  Then the system (4) `n ↦ M ⊗ᴸ_P P/Jⁿ⁺¹` is isomorphic, as an
> inverse system in `D(A)`, to the system `n ↦ M ⊗ᴸ_{A[x]} A[x]/(x)ⁿ⁺¹`, i.e. to the system (4)
> for `A[x] → A`, `xᵢ ↦ gᵢ`.

```lean
noncomputable def polynomialSystemFourIso :
    systemFour (polyEval R₀ g) M (MvPolynomial.idealOfVars (Fin r) R₀) ≅
      systemFour (polyEvalBase g) M (MvPolynomial.idealOfVars (Fin r) A)
```

**`Stacks.LocalCohomology.UniformityII.nonempty_proIso_polynomialSystemFour_systemTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/PolynomialSystemFour.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/PolynomialSystemFour.lean#L236). The attribute's comment: “the standard example `P = ℤ[x₁, …, x_r]`: the system (4) is strictly pro-isomorphic to the system (2), by reduction to the finite map `A[x] → A`”.

> In the situation of `polynomialSystemFourIso`, with `A` Noetherian and `I = (g₁, …, g_r)`,
> the system (4) `n ↦ M ⊗ᴸ_P P/Jⁿ⁺¹` for `P = R₀[x₁, …, x_r]` is strictly pro-isomorphic to the
> system (2) `n ↦ M ⊗ᴸ_A A/Iⁿ⁺¹`.

```lean
theorem nonempty_proIso_polynomialSystemFour_systemTwo [IsNoetherianRing A] :
    Nonempty (proObj (systemFour (polyEval R₀ g) M (MvPolynomial.idealOfVars (Fin r) R₀)) ≅
      proObj (systemTwo (polyEval R₀ g) M (Ideal.span (Set.range g))))
```

**`Stacks.LocalCohomology.UniformityII.isIso_proHom_derivedReductionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictDerivedReduction.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictDerivedReduction.lean#L135). The attribute's comment: “the natural map from (2) to (1) is a strict pro-isomorphism”.

> **The natural map from system (2) to system (1) is a strict pro-isomorphism.** Let `I` be an
> ideal of a Noetherian ring `A`, let `M` be a bounded complex of finite `A`-modules and
> `p : P ⟶ M` a quasi-isomorphism from a bounded above complex of finite flat modules, so that
> `P/IⁿP` computes `M ⊗ᴸ_A A/Iⁿ`. Then the natural map from the inverse system `n ↦ P/I^(n+1)P` to
> the inverse system `n ↦ M/I^(n+1)M` in `D(A)` is an isomorphism in the strict pro-category of
> `D(A)`.

```lean
theorem isIso_proHom_derivedReductionComparison [IsNoetherianRing A] (I : Ideal A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i))
    {P : CochainComplex (ModuleCat.{u} A) ℤ} (p : P ⟶ M) (hPbounded : ∃ b : ℤ, P.IsStrictlyLE b)
    (hPfinite : ∀ i : ℤ, Module.Finite A (P.X i) ∧ Module.Flat A (P.X i))
    (hp : IsIso (DerivedCategory.Q.map p)) :
    IsIso (proHom (⟨0, Functor.whiskerRight (reductionComplexSystemMap I p) DerivedCategory.Q⟩ :
      StrictProHomRep (reductionComplexSystem I P ⋙ DerivedCategory.Q)
        (reductionComplexSystem I M ⋙ DerivedCategory.Q)))
```

**`Stacks.LocalCohomology.UniformityII.derivedReductionComparison_hasEventualInverses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictDerivedReduction.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictDerivedReduction.lean#L154). The attribute's comment: “the systems (1) and (2) are pro-isomorphic, via Lemma 15.102.3”.

> **The systems (1) and (2) are pro-isomorphic.** Let `I` be an ideal of a Noetherian ring `A`,
> let `M` be a bounded complex of finite `A`-modules and `p : P ⟶ M` a quasi-isomorphism from a
> bounded above complex of finite flat modules, so that `P/IⁿP` computes `M ⊗ᴸ_A A/Iⁿ`. Then the
> natural map from the system (2) `n ↦ P/I^(n+1)P` to the system (1) `n ↦ M/I^(n+1)M` in `D(A)` is
> a pro-isomorphism.

```lean
theorem derivedReductionComparison_hasEventualInverses [IsNoetherianRing A] (I : Ideal A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i))
    {P : CochainComplex (ModuleCat.{u} A) ℤ} (p : P ⟶ M) (hPbounded : ∃ b : ℤ, P.IsStrictlyLE b)
    (hPfinite : ∀ i : ℤ, Module.Finite A (P.X i) ∧ Module.Flat A (P.X i))
    (hp : IsIso (DerivedCategory.Q.map p)) :
    NoetherianAdicCompletion.HasEventualInverses
      (Functor.whiskerRight (reductionComplexSystemMap I p) DerivedCategory.Q)
```

**`Stacks.LocalCohomology.UniformityII.proIso_koszulToAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean#L150). The attribute's comment: “the pro-isomorphism, in the category of modules, between the system `H⁰(Kₙ) = A/(f₀ⁿ, …, f_{r-1}ⁿ)` and the system `A/Iⁿ`, which is the comparison the remark makes by comparing with Koszul complexes and whose strictness the remark then denies”.

> **The two systems are isomorphic as pro-objects.** The comparison `koszulToAdic` admits, at
> every level `n`, a two-sided inverse defined on a later level `m`: both triangles it forms with
> the transition maps commute.

```lean
public theorem proIso_koszulToAdic {A : Type u} [CommRing A] {r : ℕ} (f : Fin r → A) (n : ℕ) :
    ∃ (m : ℕ) (h : n ≤ m)
      (s : (AdicCompletionTor.idealPowerQuotientModuleSystem
              (Ideal.span (Set.range f))).obj (op m) ⟶
        (Koszul.powQuotientSystem f).obj (op n)),
      (koszulToAdic f).app (op m) ≫ s = (Koszul.powQuotientSystem f).map (homOfLE h).op ∧
        s ≫ (koszulToAdic f).app (op n)
          = (AdicCompletionTor.idealPowerQuotientModuleSystem
              (Ideal.span (Set.range f))).map (homOfLE h).op
```

**`Stacks.LocalCohomology.UniformityII.not_annihilator_pow_mul_pred`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean#L285). The attribute's comment: “the computation the remark performs on its example: for `A = ℤ[x₀, …, x_{r-1}]` and `f i = x i`, the module `H⁰(Kₙ) = A/(x₀ⁿ, …, x_{r-1}ⁿ)` is not annihilated by `I^{r(n-1)}`, witnessed by the monomial `x₀^(n-1) ⋯ x_{r-1}^(n-1)`”.

> In `ℤ[x₀, …, x_{r-1}]` the module
> `H⁰(Kₙ) = ℤ[x]/(x₀ⁿ, …, x_{r-1}ⁿ)` is not annihilated by `I^{r(n-1)}`.

```lean
public theorem not_annihilator_pow_mul_pred (r n : ℕ) (hn : 1 ≤ n) :
    ¬ (monomialIdeal r ^ (r * (n - 1)) ≤
        Module.annihilator (MvPolynomial (Fin r) ℤ)
          (MvPolynomial (Fin r) ℤ ⧸
            Ideal.span (Set.range fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ) ^ n)))
```

**`Stacks.LocalCohomology.UniformityII.not_strictProIso_monomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean#L317). The attribute's comment: “the failure of strictness the remark asserts for systems (1) and (3) at `M = A[0]`: the system `H⁰(Kₙ) = A/(x₀ⁿ, …, x_{r-1}ⁿ)` over `A = ℤ[x₀, …, x_{r-1}]` admits no strict pro-isomorphism with the system `A/Iⁿ`, proved as the negation it is”.

> **Failure of strictness.** For `r ≥ 2` the inverse system
> `H⁰(Kₙ) = ℤ[x]/(x₀ⁿ, …, x_{r-1}ⁿ)` of the Koszul complexes on the powers of the variables and
> the adic system `ℤ[x]/Iⁿ` of the ideal `I = (x₀, …, x_{r-1})` they generate are *not* strictly
> pro-isomorphic: there is no pair of strict pro-morphisms between them, in either direction,
> whose composite is eventually the identity of the Koszul system.

```lean
public theorem not_strictProIso_monomial (r : ℕ) (hr : 2 ≤ r) :
    ¬ ∃ (φ : StrictProHomRep
          (AdicCompletionTor.idealPowerQuotientModuleSystem
            (Ideal.span (Set.range fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ))))
          (Koszul.powQuotientSystem fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ)))
        (ψ : StrictProHomRep
          (Koszul.powQuotientSystem fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ))
          (AdicCompletionTor.idealPowerQuotientModuleSystem
            (Ideal.span (Set.range fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ))))),
      (ψ.comp φ).Equivalent
        (StrictProHomRep.id (Koszul.powQuotientSystem fun i : Fin r =>
          (X i : MvPolynomial (Fin r) ℤ)))
```

**`Stacks.LocalCohomology.UniformityII.not_nonempty_iso_proObj_monomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailure.lean#L341). The attribute's comment: “the failure of strictness for systems (1) and (3) at `M = A[0]`, stated as non-isomorphism of the two inverse sequences in the strict pro-category itself”.

> **Failure of strictness, in the strict pro-category.**  For `r ≥ 2` the inverse sequence
> `A/Iⁿ` and the inverse sequence `H⁰(Kₙ) = A/(x₀ⁿ, …, x_{r-1}ⁿ)` over `A = ℤ[x₀, …, x_{r-1}]`
> are not isomorphic as objects of the strict pro-category.

```lean
public theorem not_nonempty_iso_proObj_monomial (r : ℕ) (hr : 2 ≤ r) :
    ¬ Nonempty
      (proObj (AdicCompletionTor.idealPowerQuotientModuleSystem
          (Ideal.span (Set.range fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ)))) ≅
        proObj (Koszul.powQuotientSystem fun i : Fin r =>
          (X i : MvPolynomial (Fin r) ℤ)))
```

**`Stacks.LocalCohomology.UniformityII.not_nonempty_iso_proObj_derived_monomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailureDerived.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictnessFailureDerived.lean#L120). The attribute's comment: “systems (1) and (3) are not strictly pro-isomorphic, even for `M = A[0]`: the example `A = ℤ[x₁, …, x_r]`, `fᵢ = xᵢ`, read in the strict pro-category of `D(A)`”.

> **Stacks 0GA5, failure of strictness for (1) and (3), in `D(A)`.**  Let
> `A = ℤ[x₀, …, x_{r-1}]` with `r ≥ 2`, `fᵢ = xᵢ` and `I = (x₀, …, x_{r-1})`.  For `M = A[0]` the
> system (1) is `n ↦ (A/I^(n+1))[0]` and the system (3) is `n ↦ A ⊗ᴸ K_{n+1} = K_{n+1}`, the
> Koszul complex on `x₀^(n+1), …, x_{r-1}^(n+1)`.  These two inverse systems of `D(A)` are not
> isomorphic in the strict pro-category of `D(A)`.
>
> Applying `H⁰` to an isomorphism of the strict pro-category gives one between the systems
> `A/I^(n+1)` and `H⁰(K_{n+1}) = A/(x₀^(n+1), …, x_{r-1}^(n+1))` of modules, which
> `not_nonempty_iso_proObj_monomial` rules out.

```lean
theorem not_nonempty_iso_proObj_derived_monomial {r : ℕ}
    [HasDerivedCategory.{w} (ModuleCat.{0} (MvPolynomial (Fin r) ℤ))] (hr : 2 ≤ r) :
    ¬ Nonempty
      (proObj (AdicCompletionTor.idealPowerQuotientModuleSystem
          (Ideal.span (Set.range fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ))) ⋙
          DerivedCategory.singleFunctor (ModuleCat.{0} (MvPolynomial (Fin r) ℤ)) 0) ≅
        proObj (Koszul.powDerivedSystem fun i : Fin r => (X i : MvPolynomial (Fin r) ℤ)))
```

**`CategoryTheory.StrictProCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictProCategory.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictProCategory.lean#L32). The attribute's comment: “strict\_pro\_category”.

> The strict pro-category of `C`. Its objects are inverse sequences in `C`; its morphisms are
> uniformly shifted compatible maps modulo eventual agreement after passing to a common shift.

```lean
abbrev StrictProCategory (C : Type u) [Category.{v} C]
```

**`Stacks.LocalCohomology.UniformityII.derivedTensorKoszulSystem_hasEventualInverses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictProFourSystems.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictProFourSystems.lean#L70). The attribute's comment: “the pro-isomorphism between the systems (2) and (3), via Lemma 15.96.1”.

> **Systems (2) and (3) are pro-isomorphic.**  For an ideal `I = (f₀, …, f_{r-1})` of a
> Noetherian ring `A`, the inverse system `n ↦ M ⊗ᴸ K_{n+1}` of derived tensor products with the
> Koszul complexes on the positive powers of the generators is pro-isomorphic to the inverse
> system `n ↦ M ⊗ᴸ A/Iⁿ⁺¹`, via the derived tensor product with `M` of the comparison
> `Kₙ → A/Iⁿ` of [Stacks, Tag 0921].

```lean
public theorem derivedTensorKoszulSystem_hasEventualInverses
    [IsNoetherianRing A] {r : ℕ} (f : Fin r → A) (I : Ideal A)
    (hI : I = Ideal.span (Set.range f))
    (T : CochainComplex.DerivedTensor.DerivedTensorProduct A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    NoetherianAdicCompletion.HasEventualInverses
      (Functor.whiskerRight (NoetherianAdicCompletion.koszulIdealPowerComparison f I hI)
        (T.tensor.obj (DerivedCategory.Q.obj M)))
```

**`Stacks.LocalCohomology.UniformityII.derivedTensorKoszulSystem_hasEventualInverses_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictProFourSystems.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictProFourSystems.lean#L84). The attribute's comment: “the pro-isomorphism between the systems (2) and (3), for the canonical derived tensor product”.

> `derivedTensorKoszulSystem_hasEventualInverses` for the canonical derived tensor product
> of [Stacks, Tag 0BYI].

```lean
public theorem derivedTensorKoszulSystem_hasEventualInverses_canonical
    [IsNoetherianRing A] {r : ℕ} (f : Fin r → A) (I : Ideal A)
    (hI : I = Ideal.span (Set.range f))
    (M : CochainComplex (ModuleCat.{u} A) ℤ) :
    NoetherianAdicCompletion.HasEventualInverses
      (Functor.whiskerRight (NoetherianAdicCompletion.koszulIdealPowerComparison f I hI)
        ((CochainComplex.DerivedTensor.canonicalDerivedTensorProduct A).tensor.obj
          (DerivedCategory.Q.obj M)))
```

**`Stacks.LocalCohomology.UniformityII.isIso_proHom_systemFourToTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictSystemFour.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictSystemFour.lean#L156). The attribute's comment: “if `P → A` is finite, the system (4) is strictly pro-isomorphic to the system (2)”.

> **Stacks 0GA5: if `P → A` is finite, system (4) is strictly pro-isomorphic to system
> (2).**  Let `P` be Noetherian, `f : P → A` a finite ring map, `J ⊆ P` an ideal with `I = JA`,
> and `M` a complex of `A`-modules.  Then the comparison from the system `n ↦ M ⊗ᴸ_P P/Jⁿ⁺¹` to
> the system `n ↦ M ⊗ᴸ_A A/Iⁿ⁺¹` is an isomorphism of the strict pro-category of `D(A)`.
>
> The source states the remark for a bounded complex `M` of finite modules over a Noetherian
> ring `A`; neither hypothesis is used here.

```lean
theorem isIso_proHom_systemFourToTwo [IsNoetherianRing P] (hf : f.Finite) (J : Ideal P)
    (I : Ideal A) (hI : I = J.map f) :
    IsIso (proHom (⟨0, systemFourToTwo f M J I hI⟩ :
      StrictProHomRep (systemFour f M J) (systemTwo f M I)))
```

**`Stacks.LocalCohomology.UniformityII.hasUniformInverses_systemTwoToOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictSystemTwo.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/BitUniformityII/StrictSystemTwo.lean#L257). The attribute's comment: “the natural map from (2) to (1) is a strict pro-isomorphism, for (2) formed with the derived tensor product”.

> **The natural map from (2) to (1) is a strict pro-isomorphism**, for the derived-tensor model
> of (2). Let `I` be an ideal of a Noetherian ring `A` and `M` a bounded complex of finite
> `A`-modules. The counits `M ⊗ᴸ_A A/Iⁿ⁺¹ ⟶ M/Iⁿ⁺¹M` have inverses over a shift independent of
> `n`.

```lean
theorem hasUniformInverses_systemTwoToOne [IsNoetherianRing A] (I : Ideal A)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i)) :
    HasUniformInverses (systemTwoToOne f M I)
```

**`Stacks.AdicSystem.DerivedReductionProIso.derivedReduction_exists_uniform_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/UniformDerivedReduction.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/AdicSystem/UniformDerivedReduction.lean#L499). The attribute's comment: “the natural map from (2) to (1) is a strict pro-isomorphism: inverses over a uniform shift”.

> **[Stacks, Tag 0GA5], explicitly.**  In the situation of
> `derivedReduction_hasUniformInverses`, there is a shift `c` such that for all `n + c ≤ m` the
> comparison maps `adicReductionComparison` acquire an inverse from level `m` to level `n` whose
> two round trips are the transition maps.

```lean
theorem derivedReduction_exists_uniform_inverse [IsNoetherianRing A] (I : Ideal A)
    (M : CochainComplex (ModuleCat.{u} A) ℤ)
    (hMbounded : ∃ a b : ℤ, M.IsStrictlyGE a ∧ M.IsStrictlyLE b)
    (hMfinite : ∀ i : ℤ, Module.Finite A (M.X i))
    {P : CochainComplex (ModuleCat.{u} A) ℤ} (p : P ⟶ M) (hPbounded : ∃ b : ℤ, P.IsStrictlyLE b)
    (hPfinite : ∀ i : ℤ, Module.Finite A (P.X i) ∧ Module.Flat A (P.X i))
    (hp : IsIso (DerivedCategory.Q.map p)) :
    ∃ c : ℕ, ∀ n m : ℕ, n + c ≤ m →
      ∃ (h : n ≤ m) (s : DerivedCategory.Q.obj ((reduceComplex (I ^ (m + 1))).obj M) ⟶
          DerivedCategory.Q.obj ((reduceComplex (I ^ (n + 1))).obj P)),
        adicReductionComparison I p m ≫ s = adicReductionTransition I P h ∧
          s ≫ adicReductionComparison I p n = adicReductionTransition I M h
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.21, Tag 0G9W](https://stacks.math.columbia.edu/tag/0G9W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
