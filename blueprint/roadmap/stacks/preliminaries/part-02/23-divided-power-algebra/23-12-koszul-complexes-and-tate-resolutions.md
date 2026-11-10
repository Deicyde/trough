---
declaration: section
origin: cited
lean: DividedPowers.TateResolution.exists_tateResolution_koszulPowers, DividedPowers.TateResolution.exists_koszulTateProIso, DividedPowers.TateResolution.exact_degreeZeroHomology_oddVariableExtension, DividedPowers.TateResolution.surjective_degreeZeroHomology_oddVariableExtension, DividedPowers.TateResolution.evenVariableSpectralSequence_degree_two, DividedPowers.TateResolution.range_mulOnGradeHomology_eq_ker_toExtension, DividedPowers.TateResolution.range_toExtensionOnGradeHomology_eq_ker_connecting, DividedPowers.TateResolution.range_connectingOnGradeHomology_eq_ker_mul
statement: formalized
proof: formalized
---

# 23.12 Koszul complexes and Tate resolutions

Section 23.12 of the Stacks Project, [Tag 0GZ3](https://stacks.math.columbia.edu/tag/0GZ3). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GZ4, a lemma

[Tag 0GZ4](https://stacks.math.columbia.edu/tag/0GZ4) in the Stacks Project.

**`DividedPowers.TateResolution.exists_tateResolution_koszulPowers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/KoszulTateComparison.lean, line 1156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/KoszulTateComparison.lean#L1156).

> **Tag 0GZ4.** Let `R` be a Noetherian ring and `f₁, …, f_r ∈ R`. Write `K_m` for the Koszul
> divided power algebra `R⟨ξ₁, …, ξ_r⟩` with `ξᵢ` of degree one and `d(ξᵢ) = fᵢ^m`, and `K_M → K_m`
> for the transition map `ξᵢ ↦ fᵢ^(M-m) ξᵢ`. Then for every `n` there is an `N ≥ n` and maps
> `K_N → A → R/(f₁^N, …, f_r^N)` and `A → K_n` such that `(A, d, γ)` is a divided power
> differential graded algebra as in Definition 09PJ, `A → R/(f₁^N, …, f_r^N)` is a
> quasi-isomorphism, the composition `K_N → A → R/(f₁^N, …, f_r^N)` is the canonical map, the
> composition `K_N → A → K_n` is the transition map, `A₀ = R → R/(f₁^N, …, f_r^N)` is the canonical
> surjection, `A` is a graded divided power polynomial algebra over `R` with finitely many
> generators in each degree, and `A → K_n` is a homomorphism of differential graded `R`-algebras
> compatible with divided powers inducing the canonical map
> `R/(f₁^N, …, f_r^N) → R/(f₁^n, …, f_r^n)` on homology in degree zero.

```lean
public theorem exists_tateResolution_koszulPowers [IsNoetherianRing R] (f : Fin r → R) (n : ℕ) :
    ∃ (N : ℕ) (hN : n ≤ N) (A : GradedDPAlgebra.{u, u} R) (d : A.carrier →ₗ[R] A.carrier)
        (ι : R →ₐ[R] A.carrier) (ε : A.carrier →ₐ[R] R ⧸ koszulPowerIdeal f N)
        (α : ExteriorAlgebra R (Fin r → R) →ₐ[R] A.carrier)
        (β : A.carrier →ₐ[R] ExteriorAlgebra R (Fin r → R)),
      -- (1) `(A, d, γ)` is as in Definition 09PJ
      IsDifferentialGradedAlgebra A.grade d ∧ IsCompatibleWithDifferential A.gamma d ∧
      -- (6) a graded divided power polynomial algebra over `R`, degreewise finitely generated
      (∃ P : GradedDividedPowerPolynomial A.grade A.gamma ι, ∀ i : ℕ, Finite (P.indices i)) ∧
      -- (5) `A₀ = R`, and `A₀ → R/(f₁^N, …, f_r^N)` is the canonical surjection
      Function.Injective ι ∧
      (∀ a : A.carrier, a ∈ A.grade 0 ↔ ∃ c : R, ι c = a) ∧
      (∀ c : R, ε (ι c) = Ideal.Quotient.mk (koszulPowerIdeal f N) c) ∧
      -- (2) `ε` is a quasi-isomorphism onto `R/(f₁^N, …, f_r^N)`
      Function.Surjective ε ∧
      (∀ (k : ℕ) (a : A.carrier), 0 < k → a ∈ A.grade k → ε a = 0) ∧
      (∀ a : A.carrier, ε (d a) = 0) ∧
      (∀ a : A.carrier, a ∈ A.grade 0 → ε a = 0 → ∃ b ∈ A.grade 1, d b = a) ∧
      (∀ (k : ℕ) (a : A.carrier), a ∈ A.grade (k + 1) → d a = 0 →
        ∃ b ∈ A.grade (k + 2), d b = a) ∧
      -- `α : K_N → A` is a morphism of differential graded divided power algebras
      (∀ (k : ℕ) (x : ExteriorAlgebra R (Fin r → R)),
        x ∈ exteriorGrade R (Fin r → R) k → α x ∈ A.grade k) ∧
      (∀ x, α (koszulPowerDifferential f N x) = d (α x)) ∧
      (∀ (k : ℕ) (x : ExteriorAlgebra R (Fin r → R)),
        x ∈ positiveEvenPart (exteriorGrade R (Fin r → R)) →
          α ((exteriorDividedPowerStructure R r).dpow k x) = A.gamma.dpow k (α x)) ∧
      -- (7) `β : A → K_n` is a morphism of differential graded divided power algebras
      (∀ (k : ℕ) (a : A.carrier), a ∈ A.grade k → β a ∈ exteriorGrade R (Fin r → R) k) ∧
      (∀ a, β (d a) = koszulPowerDifferential f n (β a)) ∧
      (∀ (k : ℕ) (a : A.carrier), a ∈ positiveEvenPart A.grade →
        β (A.gamma.dpow k a) = (exteriorDividedPowerStructure R r).dpow k (β a)) ∧
      -- (3) the composition `K_N → A → R/(f₁^N, …, f_r^N)` is the canonical map
      (∀ x, ε (α x) = koszulPowerAugmentation f N x) ∧
      -- (4) the composition `K_N → A → K_n` is the transition map
      (∀ x, β (α x) = koszulPowerTransitionHom f N n x) ∧
      -- (7) `β` is the identity of `R` in degree zero, hence induces the canonical map
      -- `R/(f₁^N, …, f_r^N) → R/(f₁^n, …, f_r^n)` on homology in degree zero
      (∀ c : R, β (ι c) = algebraMap R (ExteriorAlgebra R (Fin r → R)) c) ∧
      (∀ a : A.carrier, a ∈ A.grade 0 →
        koszulPowerAugmentation f n (β a) =
          Ideal.Quotient.factor (koszulPowerIdeal_le_of_le f hN) (ε a))
```

## Tag 0GZ5, a remark

[Tag 0GZ5](https://stacks.math.columbia.edu/tag/0GZ5) in the Stacks Project.

**`DividedPowers.TateResolution.exists_koszulTateProIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/KoszulTateProSystem.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/KoszulTateProSystem.lean#L296).

> **Tag 0GZ5.** Let `R` be a Noetherian ring and `f₁, …, f_r ∈ R`. Write `K_m` for the Koszul
> divided power algebra of the `m`-th powers and `K_M → K_m` for its transition maps. Then there
> is a sequence of exponents `1 = n₀ < n₁ < n₂ < ⋯`, cofinal in `ℕ`, and for each `i` maps
> `K_{nᵢ₊₁} → Aᵢ → R/(f₁^{nᵢ₊₁}, …, f_r^{nᵢ₊₁})` and `Aᵢ → K_{nᵢ}` as in Tag 0GZ4, such that with
> `Aᵢ₊₁ → Aᵢ` the composite `Aᵢ₊₁ → K_{nᵢ₊₁} → Aᵢ` the ladder commutes and the two inverse systems
> `(K_n)` and `(Aᵢ)` are pro-isomorphic as differential graded `R`-algebras with compatible divided
> powers: the composite `K_{nᵢ₊₁} → Aᵢ → K_{nᵢ}` is the Koszul transition map, and the composite
> `Aᵢ₊₁ → K_{nᵢ₊₁} → Aᵢ` is the Tate transition map.

```lean
public theorem exists_koszulTateProIso (f : Fin r → R) :
    ∃ (n : ℕ → ℕ) (stage : ∀ i : ℕ, KoszulTateStage f (n i)),
      n 0 = 1 ∧ StrictMono n ∧ (∀ k : ℕ, ∃ i : ℕ, k ≤ n i) ∧
      (∀ i : ℕ, (stage i).topPower = n (i + 1)) ∧
      -- the upper square of the ladder commutes
      (∀ (i : ℕ) (x : ExteriorAlgebra R (Fin r → R)),
        (stage (i + 1)).proTransition (stage i) ((stage (i + 1)).up x) =
          (stage i).up (koszulPowerTransitionHom f (n (i + 2)) (n (i + 1)) x)) ∧
      -- the lower square of the ladder commutes
      (∀ (i : ℕ) (a : (stage (i + 1)).A.carrier),
        (stage i).down ((stage (i + 1)).proTransition (stage i) a) =
          koszulPowerTransitionHom f (n (i + 1)) (n i) ((stage (i + 1)).down a)) ∧
      -- the composite `K_{nᵢ₊₁} → Aᵢ → K_{nᵢ}` is the transition map of the Koszul system
      (∀ (i : ℕ) (x : ExteriorAlgebra R (Fin r → R)),
        (stage i).down ((stage i).up x) =
          koszulPowerTransitionHom f (n (i + 1)) (n i) x) ∧
      -- the composite `Aᵢ₊₁ → K_{nᵢ₊₁} → Aᵢ` is the transition map of the Tate system
      (∀ i : ℕ, (stage (i + 1)).proTransition (stage i) =
        ((stage i).up).comp ((stage (i + 1)).down)) ∧
      -- the transition maps of the Tate system are maps of differential graded `R`-algebras
      -- with compatible divided powers
      (∀ (i k : ℕ) (a : (stage (i + 1)).A.carrier), a ∈ (stage (i + 1)).A.grade k →
        (stage (i + 1)).proTransition (stage i) a ∈ (stage i).A.grade k) ∧
      (∀ (i : ℕ) (a : (stage (i + 1)).A.carrier),
        (stage (i + 1)).proTransition (stage i) ((stage (i + 1)).d a) =
          (stage i).d ((stage (i + 1)).proTransition (stage i) a)) ∧
      (∀ (i k : ℕ) (a : (stage (i + 1)).A.carrier),
        a ∈ positiveEvenPart (stage (i + 1)).A.grade →
          (stage (i + 1)).proTransition (stage i) ((stage (i + 1)).A.gamma.dpow k a) =
            (stage i).A.gamma.dpow k ((stage (i + 1)).proTransition (stage i) a))
```

## Tag 0GZ6, a lemma

[Tag 0GZ6](https://stacks.math.columbia.edu/tag/0GZ6) in the Stacks Project.

**`DividedPowers.TateResolution.exact_degreeZeroHomology_oddVariableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/DegreeZeroHomology.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/DegreeZeroHomology.lean#L205). The attribute's comment: “degree\_one”.

> Multiplication by the cycle followed by the inclusion into the degree-one
> extension is right exact on degree-zero homology.

```lean
public theorem exact_degreeZeroHomology_oddVariableExtension
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (dA : A →ₗ[R] A) [IsDifferentialGradedAlgebra 𝒜 dA]
    (f : A) (hf_grade : f ∈ 𝒜 0)
    (dExt : OddVariableExtension 𝒜 1 →ₗ[R] OddVariableExtension 𝒜 1)
    [IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1) dExt]
    (hdExt : ∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 1 x) =
      OddVariableExtension.inclusion 𝒜 1 (dA x))
    (hT : dExt (OddVariableExtension.generator 𝒜 1) =
      OddVariableExtension.inclusion 𝒜 1 f) :
    LinearMap.range (mulOnDegreeZeroHomology 𝒜 dA f hf_grade) =
      LinearMap.ker (toExtensionOnDegreeZeroHomology 𝒜 dA dExt hdExt)
```

**`DividedPowers.TateResolution.surjective_degreeZeroHomology_oddVariableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/DegreeZeroHomology.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/DegreeZeroHomology.lean#L266). The attribute's comment: “degree\_one”.

> The inclusion onto degree-zero homology of the extension is surjective.

```lean
public theorem surjective_degreeZeroHomology_oddVariableExtension
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜]
    (dA : A →ₗ[R] A)
    (dExt : OddVariableExtension 𝒜 1 →ₗ[R] OddVariableExtension 𝒜 1)
    (hdExt : ∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 1 x) =
      OddVariableExtension.inclusion 𝒜 1 (dA x)) :
    Function.Surjective
      (toExtensionOnDegreeZeroHomology 𝒜 dA dExt hdExt)
```

**`DividedPowers.TateResolution.evenVariableSpectralSequence_degree_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableSpectralSequence.lean, line 883](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/EvenVariableSpectralSequence.lean#L883). The attribute's comment: “degree\_two”.

> **The spectral sequence of a degree-two divided-power variable, Tag 0GZ6 part (2).**
>
> Let `(A, dA)` be a strictly graded-commutative differential graded algebra, let `f` be a cycle of
> degree `1 = 2 - 1`, and let `A⟨T⟩` be the extension by a divided-power variable of degree two with
> `dT = f`, with the differential of Tag 09PM. Filtering `A⟨T⟩` by `Fᵖ = ⨁_{n ≤ p} A T⁽ⁿ⁾` gives a
> spectral sequence, and this records the four assertions of the tag:
>
> * its first page in the bidegree with filtration index `i` and total degree `2 i + q` is the
>   degree-`q` homology of `A`, by an isomorphism carrying the class of a degree-`q` cycle `ξ` to
>   the page class of the representative `ξ T⁽ⁱ⁾`;
> * that bidegree is `(i, j)` with `j - i = q`, so the first page in the bidegree `(i, j)` is
>   `H_{j - i}(A) · T⁽ⁱ⁾`, as the tag writes it;
> * its first differential sends the class of `ξ T⁽ⁱ⁺¹⁾` to the class of
>   `(signRingHom 𝒜 1 ξ * f) T⁽ⁱ⁾ = ((-1) ^ q • (ξ f)) T⁽ⁱ⁾`, that is, it is multiplication by `f`
>   with the Koszul sign of the degree of `ξ`;
> * it converges, the filtration being finite in every degree, and abuts to the homology of the
>   complex of `A⟨T⟩`, whose degree-`k` term is the degree-`k` homology of `A⟨T⟩`.
>
> The sign of the first differential is the one of `evenPolynomialDifferential_monomial`; the tag
> writes `f ξ` unsigned, which is the same up to the unit `(-1) ^ q` of the coefficient ring.

```lean
public theorem evenVariableSpectralSequence_degree_two (hf_grade : f ∈ 𝒜 1) (hf_cycle : dA f = 0)
    (h0 : ∀ p : P, algebraMap P A p ∈ 𝒜 0) :
    letI : IsDifferentialGradedAlgebra (EvenVariableAlgebra.grade 𝒜 2)
        (evenPolynomialDifferential 𝒜 dA f) :=
      evenPolynomialDifferential_two_isDGA 𝒜 dA f hf_grade hf_cycle
    (∀ i q : ℕ, ∃ e : coefficientHomology 𝒜 dA h0 q ≃ₗ[P]
          ((evenVariableSpectralSequence 𝒜 dA f h0).page 1 le_rfl).X
            (filtrationBidegree true (i : ℤ) ((2 * i + q : ℕ) : ℤ)),
        ∀ ξ : ↥(coefficientCycles 𝒜 dA h0 q),
          e (Submodule.Quotient.mk ξ) = evenVariablePageOneRep 𝒜 dA f h0 i q ξ) ∧
      (∀ i q : ℕ, filtrationBidegree true (i : ℤ) ((2 * i + q : ℕ) : ℤ) =
          ((i : ℤ), (i : ℤ) + q)) ∧
      (∀ (i q : ℕ) (ξ : ↥(coefficientCycles 𝒜 dA h0 q)),
          ((evenVariableSpectralSequence 𝒜 dA f h0).page 1 le_rfl).d
              (filtrationBidegree true ((i + 1 : ℕ) : ℤ) ((2 * (i + 1) + q : ℕ) : ℤ))
              (filtrationBidegree true (i : ℤ) ((2 * i + (q + 1) : ℕ) : ℤ))
              (evenVariablePageOneRep 𝒜 dA f h0 (i + 1) q ξ) =
            evenVariablePageOneRep 𝒜 dA f h0 i (q + 1)
              ⟨signRingHom 𝒜 1 (ξ : A) * f,
                signRingHom_mul_mem_coefficientCycles 𝒜 dA f h0 hf_grade hf_cycle q ξ⟩ ∧
            signRingHom 𝒜 1 (ξ : A) * f = (-1 : R) ^ q • ((ξ : A) * f)) ∧
      ((evenVariableFiltrationData 𝒜 dA f h0).Converges ∧
        HomologicalSpectralSequenceAbutsTo (evenVariableSpectralSequence 𝒜 dA f h0)
          (fun n => (evenVariableCochainComplex 𝒜 dA f h0).homology (-n)) ∧
        ∀ k : ℕ, Nonempty ((evenVariableCochainComplex 𝒜 dA f h0).homology (-(k : ℤ)) ≅
          ModuleCat.of P (evenVariableHomology 𝒜 dA f h0 k)))
```

**`DividedPowers.TateResolution.range_mulOnGradeHomology_eq_ker_toExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L570). The attribute's comment: “degree\_one”.

> Exactness at the second copy of `Hₙ(A)`: the image of multiplication by `f` is the kernel of
> the map induced by the inclusion into the odd degree-one extension.

```lean
public theorem range_mulOnGradeHomology_eq_ker_toExtension {R : Type u} {A : Type v}
    [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] (f : A) (hf : f ∈ 𝒜 0)
    (dExt : OddVariableExtension 𝒜 1 →ₗ[R] OddVariableExtension 𝒜 1)
    [IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1) dExt]
    (hdExt : ∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 1 x) =
      OddVariableExtension.inclusion 𝒜 1 (dA x))
    (hT : dExt (OddVariableExtension.generator 𝒜 1) = OddVariableExtension.inclusion 𝒜 1 f)
    (n : ℕ) :
    LinearMap.range (mulOnGradeHomology 𝒜 dA f hf n) =
      LinearMap.ker (toExtensionOnGradeHomology 𝒜 dA dExt hdExt n)
```

**`DividedPowers.TateResolution.range_toExtensionOnGradeHomology_eq_ker_connecting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 640](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L640). The attribute's comment: “degree\_one”.

> Exactness at `Hₙ₊₁(A⟨T⟩)`: the image of the map induced by the inclusion in degree `n + 1` is
> the kernel of the connecting map out of degree `n + 1`.

```lean
public theorem range_toExtensionOnGradeHomology_eq_ker_connecting {R : Type u} {A : Type v}
    [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA]
    (dExt : OddVariableExtension 𝒜 1 →ₗ[R] OddVariableExtension 𝒜 1)
    [IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1) dExt]
    (hdExt : ∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 1 x) =
      OddVariableExtension.inclusion 𝒜 1 (dA x)) (n : ℕ) :
    LinearMap.range (toExtensionOnGradeHomology 𝒜 dA dExt hdExt (n + 1)) =
      LinearMap.ker (connectingOnGradeHomology 𝒜 dA dExt hdExt n)
```

**`DividedPowers.TateResolution.range_connectingOnGradeHomology_eq_ker_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L730). The attribute's comment: “degree\_one”.

> Exactness at the first copy of `Hₙ(A)`: the image of the connecting map out of degree `n + 1`
> is the kernel of multiplication by `f`.

```lean
public theorem range_connectingOnGradeHomology_eq_ker_mul {R : Type u} {A : Type v}
    [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] (f : A) (hf : f ∈ 𝒜 0)
    (dExt : OddVariableExtension 𝒜 1 →ₗ[R] OddVariableExtension 𝒜 1)
    [IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1) dExt]
    (hdExt : ∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 1 x) =
      OddVariableExtension.inclusion 𝒜 1 (dA x))
    (hT : dExt (OddVariableExtension.generator 𝒜 1) = OddVariableExtension.inclusion 𝒜 1 f)
    (n : ℕ) :
    LinearMap.range (connectingOnGradeHomology 𝒜 dA dExt hdExt n) =
      LinearMap.ker (mulOnGradeHomology 𝒜 dA f hf n)
```

**`DividedPowers.TateResolution.surjective_toExtensionOnGradeHomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 841](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L841). The attribute's comment: “degree\_one”.

> The right end of the long exact sequence: the map to the degree-zero homology of the odd
> degree-one extension is surjective. This is
> `surjective_degreeZeroHomology_oddVariableExtension` transported along the identification
> `gradeHomologyZeroEquiv` of degree-zero graded homology with the degree-zero quotient of the
> previous file, rather than a second proof of it.

```lean
public theorem surjective_toExtensionOnGradeHomology_zero {R : Type u} {A : Type v}
    [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA]
    (dExt : OddVariableExtension 𝒜 1 →ₗ[R] OddVariableExtension 𝒜 1)
    [IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1) dExt]
    (hdExt : ∀ x : A, dExt (OddVariableExtension.inclusion 𝒜 1 x) =
      OddVariableExtension.inclusion 𝒜 1 (dA x)) :
    Function.Surjective (toExtensionOnGradeHomology 𝒜 dA dExt hdExt 0)
```

**`DividedPowers.TateResolution.range_mulOnGradeHomology_eq_ker_toExtension_oddExtensionDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 874](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L874). The attribute's comment: “degree\_one”.

> Exactness at the second copy of `Hₙ(A)` for the differential of Tag 09PM: no differential on
> the extension is assumed, the one of Tag 09PM being used.

```lean
public theorem range_mulOnGradeHomology_eq_ker_toExtension_oddExtensionDifferential
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] (f : A) (hf : f ∈ 𝒜 0) (n : ℕ) :
    letI : IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1)
        (oddExtensionDifferential 𝒜 dA 1 f) := oddExtensionDifferential_one_isDGA 𝒜 dA f hf
    LinearMap.range (mulOnGradeHomology 𝒜 dA f hf n) =
      LinearMap.ker (toExtensionOnGradeHomology 𝒜 dA (oddExtensionDifferential 𝒜 dA 1 f)
        (oddExtensionDifferential_inclusion 𝒜 dA 1 f) n)
```

**`DividedPowers.TateResolution.range_toExtensionOnGradeHomology_eq_ker_connecting_oddExtensionDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 891](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L891). The attribute's comment: “degree\_one”.

> Exactness at `Hₙ₊₁(A⟨T⟩)` for the differential of Tag 09PM: no differential on the extension
> is assumed, the one of Tag 09PM being used.

```lean
public theorem range_toExtensionOnGradeHomology_eq_ker_connecting_oddExtensionDifferential
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] (f : A) (hf : f ∈ 𝒜 0) (n : ℕ) :
    letI : IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1)
        (oddExtensionDifferential 𝒜 dA 1 f) := oddExtensionDifferential_one_isDGA 𝒜 dA f hf
    LinearMap.range (toExtensionOnGradeHomology 𝒜 dA (oddExtensionDifferential 𝒜 dA 1 f)
        (oddExtensionDifferential_inclusion 𝒜 dA 1 f) (n + 1)) =
      LinearMap.ker (connectingOnGradeHomology 𝒜 dA (oddExtensionDifferential 𝒜 dA 1 f)
        (oddExtensionDifferential_inclusion 𝒜 dA 1 f) n)
```

**`DividedPowers.TateResolution.range_connectingOnGradeHomology_eq_ker_mul_oddExtensionDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 908](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L908). The attribute's comment: “degree\_one”.

> Exactness at the first copy of `Hₙ(A)` for the differential of Tag 09PM: no differential on
> the extension is assumed, the one of Tag 09PM being used.

```lean
public theorem range_connectingOnGradeHomology_eq_ker_mul_oddExtensionDifferential
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] (f : A) (hf : f ∈ 𝒜 0) (n : ℕ) :
    letI : IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1)
        (oddExtensionDifferential 𝒜 dA 1 f) := oddExtensionDifferential_one_isDGA 𝒜 dA f hf
    LinearMap.range (connectingOnGradeHomology 𝒜 dA (oddExtensionDifferential 𝒜 dA 1 f)
        (oddExtensionDifferential_inclusion 𝒜 dA 1 f) n) =
      LinearMap.ker (mulOnGradeHomology 𝒜 dA f hf n)
```

**`DividedPowers.TateResolution.surjective_toExtensionOnGradeHomology_zero_oddExtensionDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DividedPowers/TateResolution/OddVariableHomologySequence.lean#L925). The attribute's comment: “degree\_one”.

> The right end of the long exact sequence for the differential of Tag 09PM: no differential on
> the extension is assumed, the one of Tag 09PM being used.

```lean
public theorem surjective_toExtensionOnGradeHomology_zero_oddExtensionDifferential
    {R : Type u} {A : Type v} [CommRing R] [Ring A] [Algebra R A]
    (𝒜 : ℕ → Submodule R A) [GradedAlgebra 𝒜] [IsStrictlyGradedComm 𝒜] (dA : A →ₗ[R] A)
    [IsDifferentialGradedAlgebra 𝒜 dA] (f : A) (hf : f ∈ 𝒜 0) :
    letI : IsDifferentialGradedAlgebra (OddVariableExtension.grade 𝒜 1)
        (oddExtensionDifferential 𝒜 dA 1 f) := oddExtensionDifferential_one_isDGA 𝒜 dA f hf
    Function.Surjective (toExtensionOnGradeHomology 𝒜 dA (oddExtensionDifferential 𝒜 dA 1 f)
      (oddExtensionDifferential_inclusion 𝒜 dA 1 f) 0)
```

## Tag 0GZ7, a lemma

[Tag 0GZ7](https://stacks.math.columbia.edu/tag/0GZ7) in the Stacks Project.

**`Koszul.exists_derivedComparisonArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Koszul/DerivedComparison.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Koszul/DerivedComparison.lean#L243).

> **Tag 0GZ7.** *"For all `n ≥ t ≥ 1` there exists an `N > n` and a map
> `K_t → K_n ⊗_R K_t` in `D(K_N, d)` whose composition with the multiplication map is the
> transition map (in either direction)."*
>
> Both composites are asserted: postcomposition with the multiplication map
> `μ_n : K_n ⊗_R K_t → K_t` is the transition map `K_t → K_t`, which is the identity, and
> precomposition with the multiplication map `μ_N : K_N ⊗_R K_t → K_t` is the transition map
> `τ_{N,n} ⊗ id`. Here `K_t` carries the left `K_N`-action through `τ_{N,t}` and `K_n ⊗_R K_t`
> carries it through `ξᵢ ↦ fᵢ^{N-n} ξᵢ ⊗ 1`; left differential graded modules are recorded as
> right modules over the graded opposite algebra.

```lean
theorem exists_derivedComparisonArrow (f : Fin r → R) {n t : ℕ} (ht : 1 ≤ t) (htn : t ≤ n) :
    ∃ (N : ℕ) (hnN : n < N),
      ∃ σ : (powDerived f N).obj (powRestrictedModule f ht (htn.trans hnN.le)) ⟶
            (powDerived f N).obj (powTensorRestrictedModule f t (ht.trans htn) hnN.le),
        σ ≫ (powDerived f N).map (powMulHom f ht htn hnN.le) =
            CategoryStruct.id
              ((powDerived f N).obj (powRestrictedModule f ht (htn.trans hnN.le))) ∧
          (powDerived f N).map (powMulBaseHom f ht (htn.trans hnN.le)) ≫ σ =
            (powDerived f N).map (powTransitionTensorHom f t (ht.trans htn) hnN.le)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 23.12, Tag 0GZ3](https://stacks.math.columbia.edu/tag/0GZ3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
