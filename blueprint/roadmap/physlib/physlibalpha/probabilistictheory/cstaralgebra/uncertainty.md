---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.smul_one_comm, ProbabilisticTheory.UnitalPositiveLinearMap.bracket_centered, ProbabilisticTheory.UnitalPositiveLinearMap.apply_centered_mul_centered, ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsRep_gnsCyclicVector_gnsRep_gnsCyclicVector, ProbabilisticTheory.UnitalPositiveLinearMap.gns_cauchy_schwarz, ProbabilisticTheory.UnitalPositiveLinearMap.centered_gns_cauchy_schwarz, ProbabilisticTheory.UnitalPositiveLinearMap.centered_cauchy_schwarz, ProbabilisticTheory.UnitalPositiveLinearMap.robertson_schrodinger
statement: formalized
proof: formalized
---

# Uncertainty relations

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.Uncertainty`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean): 36 declarations, 34 with a docstring.

> Cauchy–Schwarz for states and the Robertson and Robertson–Schrödinger uncertainty relations.

## i. Overview

> A state gives the sesquilinear form `(x, y) ↦ ω(x⋆ y)`, which is the inner product of the GNS
> vectors of `x` and `y`. Cauchy–Schwarz for it, applied to centered observables, gives the
> Robertson–Schrödinger relation, and from it the Robertson relation `|ω⟨⁅a, b⁆⟩| ≤ σ_a σ_b` and the
> bound on the covariance.
>
> For a family of observables `a : ι → Observable A`, the covariance matrix `Σ` and the matrix `Ω`
> of expectations of brackets give the matrix `Σ + iΩ` of GNS inner products of the centered
> observables. It is a Gram matrix, and with its transpose `Σ − iΩ` it gives Robertson's relation
> for several observables, `|det Ω| ≤ det Σ`.
>
> The equality case: if `A` is positive definite and `‖det B‖ = det A`, the normalized `B` has all
> its eigenvalues equal to `±1`, so `(A + B) A⁻¹ (A − B) = 0`, and the kernels of `A + B` and
> `A − B` together span everything. For `A ± B = Σ ± iΩ` the two kernels have the same dimension.
> This extends to `n` observables the equality case of two, `robertson_schrodinger_eq_iff_gram_zero`.

## ii. Key results

> - `UnitalPositiveLinearMap.gns_cauchy_schwarz` : Cauchy–Schwarz for a state.
> - `UnitalPositiveLinearMap.robertson_schrodinger` : **the Robertson–Schrödinger uncertainty
>   relation.**
> - `UnitalPositiveLinearMap.robertson` : **the Robertson uncertainty relation.**
> - `UnitalPositiveLinearMap.covariance_cauchy_schwarz` : `|cov(a, b)| ≤ σ_a σ_b`.
> - `Matrix.PosDef.norm_det_le_re_det` : `‖det B‖ ≤ det A` when `A ± B` are positive semidefinite.
> - `Matrix.PosDef.add_mul_inv_mul_sub_eq_zero` : at equality, `(A + B) A⁻¹ (A − B) = 0`.
> - `Matrix.card_le_two_mul_finrank_ker` : at equality `|det W| = det S ≠ 0`, the kernel of
>   `S + iW` has at least half the dimension.
> - `UnitalPositiveLinearMap.robertson_det` : **Robertson's uncertainty relation for several
>   observables**, `|det Ω| ≤ det Σ`.

## iv. References

> * None.

**`ProbabilisticTheory.UnitalPositiveLinearMap.smul_one_comm`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L83).

> A real multiple of `1` commutes with everything: the algebraic fact making `commutator`
> insensitive to shifting by a constant.

```lean
lemma smul_one_comm (r : ℝ) (x : A) : (r • (1 : A)) * x = x * (r • (1 : A))
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bracket_centered`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L89).

> The commutator only sees fluctuations, not means: centering `a` and `b` changes nothing about
> how badly they fail to commute, since scalar multiples of `1` commute with everything and so
> contribute nothing to `ab - ba`.

```lean
lemma bracket_centered (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    ⁅centered ω a, centered ω b⁆ = ⁅a, b⁆
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.apply_centered_mul_centered`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L107).

> The expectation of a raw product of two fluctuations splits into a real symmetric part
> (covariance) and an imaginary antisymmetric part (the commutator's expectation). This is what
> turns the Cauchy–Schwarz bound below into simultaneous control on covariance and commutator.

```lean
lemma apply_centered_mul_centered (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    ω ((centered ω a : A) * centered ω b) =
      (covariance ω a b : ℂ) + Complex.I * (ω⟨⁅a, b⁆⟩ : ℂ)
```

## A. Cauchy–Schwarz

**`ProbabilisticTheory.UnitalPositiveLinearMap.inner_gnsRep_gnsCyclicVector_gnsRep_gnsCyclicVector`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L130).

> `⟪π_ω(x) Ω_ω, π_ω(y) Ω_ω⟫ = ω(x⋆ y)`.

```lean
lemma inner_gnsRep_gnsCyclicVector_gnsRep_gnsCyclicVector (ω : 𝓢[ℂ, A]) (x y : A) :
    ⟪ω.gnsRep x ω.gnsCyclicVector, ω.gnsRep y ω.gnsCyclicVector⟫_ℂ = ω (star x * y)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gns_cauchy_schwarz`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L136).

> **Cauchy–Schwarz for a state**: `|ω(x⋆ y)|² ≤ ω(x⋆ x) ω(y⋆ y)`.

```lean
lemma gns_cauchy_schwarz (ω : 𝓢[ℂ, A]) (x y : A) :
    ‖ω (star x * y)‖ * ‖ω (star y * x)‖ ≤
      (ω (star x * x)).re * (ω (star y * y)).re
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.centered_gns_cauchy_schwarz`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L149).

> No state can correlate two fluctuations more strongly than the product of their spreads
> allows — the GNS-Cauchy–Schwarz seed of every uncertainty relation below, before splitting the
> left side via `apply_centered_mul_centered`.

```lean
lemma centered_gns_cauchy_schwarz (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    ‖ω ((centered ω a : A) * centered ω b)‖ *
        ‖ω ((centered ω b : A) * centered ω a)‖ ≤
      variance ω a * variance ω b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.centered_cauchy_schwarz`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L159).

> The squared-magnitude form of `centered_gns_cauchy_schwarz`, ready to be split via
> `apply_centered_mul_centered` into `robertson_schrodinger`.

```lean
lemma centered_cauchy_schwarz (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    Complex.normSq (ω ((centered ω a : A) * centered ω b)) ≤
      variance ω a * variance ω b
```

## B. Uncertainty relations

**`ProbabilisticTheory.UnitalPositiveLinearMap.robertson_schrodinger`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L174).

> **The Robertson–Schrödinger uncertainty relation**, bounding the squared covariance plus the
> squared expectation of the commutator by the product of the variances.

```lean
lemma robertson_schrodinger (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    covariance ω a b ^ 2 + ω⟨⁅a, b⁆⟩ ^ 2 ≤
      variance ω a * variance ω b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.covariance_cauchy_schwarz`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L184).

> Two observables cannot be more correlated than the product of their uncertainties allows —
> the familiar `|correlation| ≤ σ_a · σ_b`, from dropping the commutator term in
> `robertson_schrodinger`.

```lean
lemma covariance_cauchy_schwarz (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    covariance ω a b ^ 2 ≤ variance ω a * variance ω b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.robertson`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L191).

> Heisenberg's uncertainty relation: observables that fail to commute cannot both be measured
> with arbitrary precision. For position and momentum, `⁅x, p⁆ = iℏ` gives `ΔxΔp ≥ ℏ/2`. Obtained
> from `robertson_schrodinger` by dropping the covariance term.

```lean
lemma robertson (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    ω⟨⁅a, b⁆⟩ ^ 2 ≤ variance ω a * variance ω b
```

## C. Equality in the uncertainty relations

**`ProbabilisticTheory.UnitalPositiveLinearMap.centeredGramDefect`**, a def, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L199).

> The Cauchy–Schwarz defect of two centered observables, the slack in the Robertson–Schrödinger
> relation.

```lean
noncomputable def centeredGramDefect (ω : 𝓢[ℂ, A]) (a b : Observable A) : ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.centeredGramDefect_nonneg`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L204).

> Positivity of the state makes the centered Gram defect nonnegative.

```lean
lemma centeredGramDefect_nonneg (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    0 ≤ centeredGramDefect ω a b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.normSq_centered_pairing`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L210).

> The squared centered pairing consists of squared covariance and squared
> expectation of the observable Lie bracket.

```lean
lemma normSq_centered_pairing (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    Complex.normSq (ω ((centered ω a : A) * centered ω b)) =
      covariance ω a b ^ 2 + ω⟨⁅a, b⁆⟩ ^ 2
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.robertson_gap_decomposition`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L217).

> The slack in the Robertson relation is the Cauchy–Schwarz defect plus the squared covariance.

```lean
lemma robertson_gap_decomposition (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    variance ω a * variance ω b - ω⟨⁅a, b⁆⟩ ^ 2 =
      centeredGramDefect ω a b + covariance ω a b ^ 2
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.robertson_schrodinger_eq_iff_gram_zero`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L225).

> Robertson–Schrödinger saturates exactly when the centered Gram defect vanishes.

```lean
lemma robertson_schrodinger_eq_iff_gram_zero (ω : 𝓢[ℂ, A]) (a b : Observable A) :
    covariance ω a b ^ 2 + ω⟨⁅a, b⁆⟩ ^ 2 = variance ω a * variance ω b ↔
      centeredGramDefect ω a b = 0
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.robertson_eq_iff_gram_zero_and_covariance_zero`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L234).

> Robertson saturates exactly when Cauchy–Schwarz saturates for the centered
> pairing and the covariance is zero. Includes zero-variance cases without division.

```lean
lemma robertson_eq_iff_gram_zero_and_covariance_zero (ω : 𝓢[ℂ, A])
    (a b : Observable A) :
    ω⟨⁅a, b⁆⟩ ^ 2 = variance ω a * variance ω b ↔
      centeredGramDefect ω a b = 0 ∧ covariance ω a b = 0
```

## D. Normalized variance bounds

**`ProbabilisticTheory.UnitalPositiveLinearMap.normalized_variance_product`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L253).

> A raw commutator expectation of magnitude one yields the normalized variance
> product bound for arbitrary states, with no extra positivity hypotheses.

```lean
lemma normalized_variance_product (ω : 𝓢[ℂ, A]) (a b : Observable A)
    (hnorm : ω⟨⁅a, b⁆⟩ ^ 2 = (1 : ℝ) / 4) :
    1 ≤ 4 * variance ω a * variance ω b
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.variances_pos_of_normalized_pairing`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L261).

> Normalization itself forces both variances to be positive.

```lean
lemma variances_pos_of_normalized_pairing (ω : 𝓢[ℂ, A]) (a b : Observable A)
    (hnorm : ω⟨⁅a, b⁆⟩ ^ 2 = (1 : ℝ) / 4) :
    0 < variance ω a ∧ 0 < variance ω b
```

## E. A determinant bound for positive matrices

**`Matrix.PosDef.normalizer`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L284).

> A matrix `T` with `T A Tᴴ = 1` for a positive definite `A`: the inverse square roots of the
> eigenvalues of `A` times the adjoint of its eigenvector unitary.

```lean
noncomputable def PosDef.normalizer {A : Matrix n n ℂ} (hA : A.PosDef) : Matrix n n ℂ
```

**`Matrix.PosDef.normalizer_mul_mul_conjTranspose`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L288).

```lean
lemma PosDef.normalizer_mul_mul_conjTranspose {A : Matrix n n ℂ} (hA : A.PosDef) :
    hA.normalizer * A * hA.normalizerᴴ = 1
```

**`Matrix.IsHermitian.abs_eigenvalues_le_one`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L319).

> The eigenvalues of a hermitian `K` with `1 − K` and `1 + K` positive semidefinite lie in
> `[−1, 1]`.

```lean
lemma IsHermitian.abs_eigenvalues_le_one {K : Matrix n n ℂ} (hK : K.IsHermitian)
    (hm : (1 - K).PosSemidef) (hp : (1 + K).PosSemidef) (i : n) : |hK.eigenvalues i| ≤ 1
```

**`Matrix.PosDef.norm_det_le_re_det`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L337).

> If `A` is positive definite, `B` hermitian and `A − B`, `A + B` positive semidefinite, then
> `‖det B‖ ≤ re (det A)`: conjugating by the normalizer of `A` puts `B` between `−1` and `1`.

```lean
lemma PosDef.norm_det_le_re_det {A B : Matrix n n ℂ} (hA : A.PosDef) (hB : B.IsHermitian)
    (h₁ : (A - B).PosSemidef) (h₂ : (A + B).PosSemidef) : ‖B.det‖ ≤ (A.det).re
```

**`Matrix.map_ofReal_add_smul_one`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L370).

```lean
lemma map_ofReal_add_smul_one (S : Matrix n n ℝ) (ε : ℝ) :
    (S + ε • 1).map ((↑) : ℝ → ℂ) = S.map ((↑) : ℝ → ℂ) + (ε : ℂ) • 1
```

**`Matrix.abs_det_le_det_of_posSemidef`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L377).

> For real `S` and `W`, if `S − iW` and `S + iW` are positive semidefinite then
> `|det W| ≤ det S`.

```lean
lemma abs_det_le_det_of_posSemidef {S W : Matrix n n ℝ}
    (h₁ : (S.map ((↑) : ℝ → ℂ) - Complex.I • W.map ((↑) : ℝ → ℂ)).PosSemidef)
    (h₂ : (S.map ((↑) : ℝ → ℂ) + Complex.I • W.map ((↑) : ℝ → ℂ)).PosSemidef) :
    |W.det| ≤ S.det
```

### E.1. The equality case

**`Matrix.IsHermitian.mul_self_eq_one`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L420).

> A hermitian `K` with eigenvalues in `[−1, 1]` and `‖det K‖ = 1` squares to the identity.

```lean
lemma IsHermitian.mul_self_eq_one {K : Matrix n n ℂ} (hK : K.IsHermitian)
    (hle : ∀ i, |hK.eigenvalues i| ≤ 1) (h1 : ‖K.det‖ = 1) : K * K = 1
```

**`Matrix.PosDef.inv_eq_conjTranspose_normalizer_mul`**, a lemma, [line 450](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L450).

> The normalizer of a positive definite `A` is invertible, and `A⁻¹ = Tᴴ T`.

```lean
lemma PosDef.inv_eq_conjTranspose_normalizer_mul {A : Matrix n n ℂ} (hA : A.PosDef) :
    A⁻¹ = hA.normalizerᴴ * hA.normalizer
```

**`Matrix.PosDef.add_mul_inv_mul_sub_eq_zero`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L466).

> **The equality case.** If `A` is positive definite, `B` hermitian, `A ∓ B` positive
> semidefinite and `‖det B‖ = re (det A)`, then `(A + B) A⁻¹ (A − B) = 0`: every eigenvalue of the
> normalized `B` is `±1`.

```lean
lemma PosDef.add_mul_inv_mul_sub_eq_zero {A B : Matrix n n ℂ} (hA : A.PosDef)
    (hB : B.IsHermitian) (h₁ : (A - B).PosSemidef) (h₂ : (A + B).PosSemidef)
    (heq : ‖B.det‖ = (A.det).re) : (A + B) * A⁻¹ * (A - B) = 0
```

**`Matrix.PosDef.card_le_finrank_ker_add_finrank_ker`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L512).

> At equality the kernels of `A + B` and `A − B` together have dimension at least `n`: every
> vector is `A⁻¹ (A − B) x / 2 + A⁻¹ (A + B) x / 2`.

```lean
lemma PosDef.card_le_finrank_ker_add_finrank_ker {A B : Matrix n n ℂ} (hA : A.PosDef)
    (hB : B.IsHermitian) (h₁ : (A - B).PosSemidef) (h₂ : (A + B).PosSemidef)
    (heq : ‖B.det‖ = (A.det).re) :
    Fintype.card n ≤ Module.finrank ℂ (LinearMap.ker (A + B).mulVecLin) +
      Module.finrank ℂ (LinearMap.ker (A - B).mulVecLin)
```

**`Matrix.finrank_ker_transpose`**, a lemma, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L539).

> `G` and `Gᵀ` have kernels of the same dimension.

```lean
lemma finrank_ker_transpose (G : Matrix n n ℂ) :
    Module.finrank ℂ (LinearMap.ker Gᵀ.mulVecLin) =
      Module.finrank ℂ (LinearMap.ker G.mulVecLin)
```

**`Matrix.card_le_two_mul_finrank_ker`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L551).

> **Equality in Robertson's determinant relation.** Let `G = S + iW` be positive semidefinite
> with `Gᵀ = S − iW`, for real `S` and `W`. If `|det W| = det S ≠ 0`, the kernel of `G` has at
> least half the dimension.

```lean
lemma card_le_two_mul_finrank_ker {G : Matrix n n ℂ} {S W : Matrix n n ℝ} (hG : G.PosSemidef)
    (hGS : G = S.map ((↑) : ℝ → ℂ) + Complex.I • W.map ((↑) : ℝ → ℂ))
    (hGT : Gᵀ = S.map ((↑) : ℝ → ℂ) - Complex.I • W.map ((↑) : ℝ → ℂ)) (hW : W.det ≠ 0)
    (heq : |W.det| = S.det) :
    Fintype.card n ≤ 2 * Module.finrank ℂ (LinearMap.ker G.mulVecLin)
```

## F. Several observables

**`ProbabilisticTheory.UnitalPositiveLinearMap.covarianceMatrix`**, a def, [line 598](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L598).

> The covariance matrix `Σ_jk = cov(a_j, a_k)` of a family of observables.

```lean
noncomputable def covarianceMatrix (ω : 𝓢[ℂ, A]) (a : ι → Observable A) : Matrix ι ι ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.bracketMatrix`**, a def, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L602).

> The matrix `Ω_jk = ω⟨⁅a_j, a_k⁆⟩` of expectations of brackets of a family of observables.

```lean
noncomputable def bracketMatrix (ω : 𝓢[ℂ, A]) (a : ι → Observable A) : Matrix ι ι ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.centeredGNSVector`**, a def, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L606).

> The GNS vectors of the centered observables.

```lean
noncomputable def centeredGNSVector (ω : 𝓢[ℂ, A]) (a : Observable A)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.gram_centeredGNSVector`**, a lemma, [line 610](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L610).

> `Σ + iΩ` is the Gram matrix of the GNS vectors of the centered observables.

```lean
lemma gram_centeredGNSVector (ω : 𝓢[ℂ, A]) (a : ι → Observable A) :
    gram ℂ (fun j => centeredGNSVector ω (a j)) =
      (covarianceMatrix ω a).map ((↑) : ℝ → ℂ) +
        Complex.I • (bracketMatrix ω a).map ((↑) : ℝ → ℂ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.transpose_gram_centeredGNSVector`**, a lemma, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L621).

> `Σ − iΩ` is the transpose of the Gram matrix.

```lean
lemma transpose_gram_centeredGNSVector (ω : 𝓢[ℂ, A]) (a : ι → Observable A) :
    (gram ℂ (fun j => centeredGNSVector ω (a j)))ᵀ =
      (covarianceMatrix ω a).map ((↑) : ℝ → ℂ) -
        Complex.I • (bracketMatrix ω a).map ((↑) : ℝ → ℂ)
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.robertson_det`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean#L633).

> **Robertson's uncertainty relation for several observables**: for every state and every
> finite family of observables, `|det Ω| ≤ det Σ`.

```lean
lemma robertson_det [Fintype ι] [DecidableEq ι] (ω : 𝓢[ℂ, A]) (a : ι → Observable A) :
    |(bracketMatrix ω a).det| ≤ (covarianceMatrix ω a).det
```

## Depends on

- [The GNS construction](gns.md)
- [The Lie bracket of observables](../staralgebra/lie.md)
- [Expectation, variance and covariance](../staralgebra/statistics.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Uncertainty.lean)
