---
declaration: module
origin: cited
lean: sandwichedTraceFunctional_pos, sandwichedTraceFunctional_conj_unitary_MState, H_hat_conj_sigma, f_alpha_le_at_optimizer, traceFunctional_eq_iSup_f_alpha, f_alpha_convex_in_sigma, HermitianMat.ker_weighted_sum_le, sandwichedTraceFunctional_jointly_convex
statement: formalized
proof: formalized
---

# DPI (Data Processing Inequality)

The module `QuantumInfo.Entropy.DPI`, [QuantumInfo/Entropy/DPI.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean): 52 declarations, 31 with a docstring, 21 listed as significant; 18 private, not shown.

> The Data Processing Inequality (DPI) for the sandwiched Rényi relative entropy, and
> as a consequence, the quantum relative entropy.

## Proof structure (for α > 1)

> Following Leditzky–Rouzé–Datta (arXiv:1306.5920), the proof proceeds as follows:
>
> 1. Define the **trace functional** `Q̃_α(ρ‖σ) = Tr[(σ^γ ρ σ^γ)^α]` where `γ = (1 - α) / (2α)`.
>    The sandwiched Rényi divergence satisfies `D̃_α(ρ‖σ) = log(Q̃_α(ρ‖σ)) / (α - 1)`.
>
> 2. The DPI for `D̃_α` reduces to **monotonicity of `Q̃_α` under partial trace**:
>    `Q̃_α(ρ_AB‖σ_AB) ≥ Q̃_α(ρ_A‖σ_A)` for `α > 1`.
>
> 3. This monotonicity is proved via the **twirling argument**:
>    - `Q̃_α` is invariant under joint unitary conjugation.
>    - `Q̃_α` is jointly convex for `α > 1` (Frank–Lieb).
>    - A twirling set of unitaries `{V_i}` averages any state to a product with the
>      maximally mixed state.
>    - `Q̃_α` is invariant under tensoring with a fixed state.
>
> 4. The general DPI for CPTP maps follows via **Stinespring dilation**:
>    any CPTP map can be decomposed as ancilla preparation + unitary + partial trace.

## The Sandwiched Trace Functional

**`sandwichedTraceFunctional`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L65).

> The sandwiched trace functional `Q̃_α(ρ‖σ) = Tr[(σ^γ ρ σ^γ)^α]` where `γ = (1-α)/(2α)`.
> This is the quantity underlying the sandwiched Rényi divergence:
> `D̃_α(ρ‖σ) = log(Q̃_α(ρ‖σ)) / (α - 1)`.
>
> Note: the `conj` operation gives `A.conj B = B * A.mat * B†`, and since `σ^γ` is Hermitian
> (self-adjoint), `B† = B`, so `ρ.M.conj (σ.M ^ γ).mat = σ^γ * ρ * σ^γ`.

```lean
noncomputable def sandwichedTraceFunctional (α : ℝ) (ρ σ : MState d) : ℝ
```

## Properties of the Trace Functional

**`sandwichedRelRentropy_eq_log_traceFunctional`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L77).

```lean
lemma sandwichedRelRentropy_eq_log_traceFunctional (hα₀ : 0 < α) (hα₁ : α ≠ 1)
    (hker : σ.M.ker ≤ ρ.M.ker) :
    D̃_ α(ρ‖σ) = ENNReal.ofReal (Real.log (Q̃_ α(ρ‖σ)) / (α - 1))
```

**`sandwichedTraceFunctional_nonneg`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L89).

```lean
lemma sandwichedTraceFunctional_nonneg (ρ σ : MState d) :
    0 ≤ Q̃_ α(ρ‖σ)
```

**`sandwichedTraceFunctional_pos`**, a theorem, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L99). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace functional is strictly positive when the kernel condition holds. Under
> `σ.M.ker ≤ ρ.M.ker` (i.e. `supp(ρ) ⊆ supp(σ)`), the sandwich `σ^γ ρ σ^γ ≠ 0`
> because ρ has support inside σ's support.

```lean
theorem sandwichedTraceFunctional_pos
    (ρ σ : MState d) (hker : σ.M.ker ≤ ρ.M.ker) :
    0 < Q̃_ α(ρ‖σ)
```

## Unitary Invariance

> `Q̃_α(UρU†‖UσU†) = Q̃_α(ρ‖σ)` for any unitary `U`.
>
> Here, `conj U.val A` denotes `U * A * U†`, so "conjugating ρ and σ by
> the same unitary" means applying `conj U.val` to both.

**`sandwichedTraceFunctional_conj_unitary_hermitian`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L123).

```lean
lemma sandwichedTraceFunctional_conj_unitary_hermitian
    (U : Matrix.unitaryGroup d ℂ) (A B : HermitianMat d ℂ) :
    let γ := (1 - α) / (2 * α)
    ((A.conj U.val).conj ((B.conj U.val) ^ γ).mat ^ α).trace =
      ((A.conj (B ^ γ).mat) ^ α).trace
```

**`sandwichedTraceFunctional_conj_unitary_MState`**, a theorem, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L139). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace functional is invariant under joint unitary conjugation of MStates.

```lean
theorem sandwichedTraceFunctional_conj_unitary_MState
    (U : Matrix.unitaryGroup d ℂ) (ρ σ : MState d) :
    Q̃_ α(ρ.uConj U‖σ.uConj U) = Q̃_ α(ρ‖σ)
```

## Joint Convexity for α > 1

> The trace functional `Q̃_α` is jointly convex for `α > 1`. This is proved by
> Frank and Lieb via a variational formula and strict convexity of trace functions.

### Trace functions convexity

> The following result is used in the proof: for a convex function `g : ℝ → ℝ`,
> the map `A ↦ Tr[g(A)]` on Hermitian matrices is convex (Carlen, Theorem 2.10).

### Variational formula for the trace functional

> Following Frank–Lieb, for `α > 1` we define
>   `f_α(H, ρ, σ) = α · Tr[ρ · H] − (α−1) · Tr[(σ^{−γ} H σ^{−γ})^{α/(α−1)}]`
> where `γ = (1−α)/(2α)` (so `−γ = (α−1)/(2α) > 0`).
> Key facts (each stated as a lemma below):
> 1. `Q̃_α(ρ‖σ) = sup_{H ≥ 0} f_α(H, ρ, σ)` for α > 1.
> 2. For fixed `H`, `f_α` is linear in `ρ` (hence convex).
> 3. For fixed `H`, `f_α` is convex in `σ` (uses Lieb concavity).
> 4. Therefore `f_α` is jointly convex in `(ρ, σ)` for fixed `H`.
> 5. The supremum of jointly convex functions is jointly convex.

**`f_alpha`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L174).

> The variational function `f_α(H, ρ, σ) = α · ⟪ρ, H⟫ − (α−1) · Tr[(σ^{−γ} H σ^{−γ})^{α/(α−1)}]`
> where `γ = (1−α)/(2α)`. For fixed `H ≥ 0`, this is linear in `ρ` and convex in `σ`.
> Frank–Lieb show that `Q̃_α(ρ‖σ) = sup_{H ≥ 0} f_α(H, ρ, σ)` for `α > 1`.

```lean
noncomputable def f_alpha (α : ℝ) (H : HermitianMat d ℂ) (ρ σ : MState d) : ℝ
```

**`H_hat`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L180).

> The optimizer in the variational formula: `H_hat = σ^γ (σ^γ ρ σ^γ)^{α−1} σ^γ`
> where `γ = (1−α)/(2α)`.

```lean
noncomputable def H_hat (α : ℝ) (ρ σ : MState d) : HermitianMat d ℂ
```

**`H_hat_nonneg`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L187).

```lean
lemma H_hat_nonneg (ρ σ : MState d) : 0 ≤ H_hat α ρ σ
```

**`H_hat_conj_sigma`**, a theorem, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L220). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Sub-lemma for Step 1b: the conj of H\_hat by σ^\{−γ} simplifies to (ρ.M.conj (σ^γ).mat)^\{α−1}.
> This uses σ^\{−γ} · σ^γ = identity (on support) to cancel the outer σ^γ factors.

```lean
theorem H_hat_conj_sigma (hα : 1 < α) (ρ σ : MState d) :
    let γ := (1 - α) / (2 * α)
    (H_hat α ρ σ).conj (σ.M ^ (-γ)).mat = (ρ.M.conj (σ.M ^ γ).mat) ^ (α - 1)
```

**`inner_rho_H_hat`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L238).

```lean
lemma inner_rho_H_hat (hα : 1 < α) (ρ σ : MState d) :
    let γ := (1 - α) / (2 * α)
    ⟪ρ.M, H_hat α ρ σ⟫_ℝ = ((ρ.M.conj (σ.M ^ γ).mat) ^ α).trace
```

**`f_alpha_at_optimizer`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L268).

```lean
lemma f_alpha_at_optimizer (hα : 1 < α) (ρ σ : MState d) :
    f_alpha α (H_hat α ρ σ) ρ σ = Q̃_ α(ρ‖σ)
```

**`rpow_mul_neg_rpow_eq_supportProj`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L287).

> For PSD `A` and `γ ≠ 0`, the product `A^γ * A^{-γ}` equals the support projection
> of `A`. This is because `x^γ * x^{-γ} = if x = 0 then 0 else 1` for `x ≥ 0`.

```lean
lemma rpow_mul_neg_rpow_eq_supportProj {A : HermitianMat d ℂ}
    (hA : 0 ≤ A) (γ : ℝ) (hγ : γ ≠ 0) :
    (A ^ γ).mat * (A ^ (-γ)).mat = A.supportProj.mat
```

**`supportProj_mul_of_ker_le`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L305).

> The support projection of `A` acts as identity on `B` when `A.ker ≤ B.ker`.
> Since `A.supportProj` projects onto `ker(A)⊥` and `B` is zero on `ker(A)`,
> the projection preserves `B`.

```lean
lemma supportProj_mul_of_ker_le {A B : HermitianMat d ℂ}
    (hker : A.ker ≤ B.ker) :
    A.supportProj.mat * B.mat = B.mat
```

**`inner_eq_inner_conj_of_ker_le`**, a lemma, [line 361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L361).

> Under the support condition `σ.M.ker ≤ ρ.M.ker` (i.e., supp(ρ) ⊆ supp(σ)),
> conjugation by `σ^γ` and `σ^{-γ}` preserves the inner product:
> `⟪ρ.M, H⟫ = ⟪σ^γ ρ σ^γ, σ^{-γ} H σ^{-γ}⟫`. This holds because the kernel condition
> ensures `ρ` is supported on `supp(σ)`, where `σ^γ σ^{-γ}` acts as the identity.

```lean
lemma inner_eq_inner_conj_of_ker_le (ρ σ : MState d)
    (H : HermitianMat d ℂ) (hker : σ.M.ker ≤ ρ.M.ker) (γ : ℝ) (hγ : γ ≠ 0) :
    ⟪ρ.M, H⟫_ℝ = ⟪ρ.M.conj (σ.M ^ γ).mat, H.conj (σ.M ^ (-γ)).mat⟫_ℝ
```

**`f_alpha_le_at_optimizer`**, a theorem, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L394). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Step 1c**: `H_hat` is a maximizer: for all `H ≥ 0`, `f_α(H) ≤ f_α(H_hat)`.
> This uses the trace Young inequality: for PSD `A, B` and conjugate exponents `p, q > 1`,
> `⟪A, B⟫ ≤ Tr[A^p]/p + Tr[B^q]/q`.
> Applied with `A = σ^γ ρ σ^γ`, `B = σ^{-γ} H σ^{-γ}`, `p = α`, `q = α/(α-1)`,
> the inner product identity `⟪ρ, H⟫ = ⟪A, B⟫` (under the support condition) yields
> `f_α(H) ≤ Tr[A^α] = Q̃_α(ρ‖σ) = f_α(H_hat)`.
> Note: the support condition `σ.M.ker ≤ ρ.M.ker` (i.e., supp(ρ) ⊆ supp(σ)) is necessary.
> Without it, the theorem is false: taking ρ orthogonal to σ gives Q̃\_α = 0 but
> `f_α(H) = α · Tr[ρH] > 0` for appropriate H.

```lean
theorem f_alpha_le_at_optimizer (hα : 1 < α) (ρ σ : MState d)
    (H : HermitianMat d ℂ) (hH : 0 ≤ H) (hker : σ.M.ker ≤ ρ.M.ker) :
    f_alpha α H ρ σ ≤ f_alpha α (H_hat α ρ σ) ρ σ
```

**`traceFunctional_eq_iSup_f_alpha`**, a theorem, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L434). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Step 1 (Variational formula)**: For `α > 1`, the trace functional equals the
> supremum of `f_α` over all PSD `H`:
>   `Q̃_α(ρ‖σ) = ⨆ (H : HermitianMat d ℂ) (_ : 0 ≤ H), f_alpha α H ρ σ`.
> The optimizer is `H_hat = σ^γ (σ^γ ρ σ^γ)^{α−1} σ^γ`.

```lean
theorem traceFunctional_eq_iSup_f_alpha (hα : 1 < α) (ρ σ : MState d) (hker : σ.M.ker ≤ ρ.M.ker) :
    Q̃_ α(ρ‖σ) = ⨆ (H : {H : HermitianMat d ℂ // 0 ≤ H}), f_alpha α H.1 ρ σ
```

**`f_alpha_convex_in_sigma`**, a theorem, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L452). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> (Convexity in σ): For fixed `H ≥ 0` and `ρ`, and `α > 1`, the map
> `σ ↦ f_alpha α H ρ σ` is convex. The key is that for `p = α/(α−1) > 1`:
> • `A ↦ Tr[A^p]` is convex on PSD matrices (trace function convexity, Theorem 2.10 of Carlen),
> • `σ ↦ σ^{−γ} H σ^{−γ}` is *concave* in `σ` by Lieb concavity (since `−γ = (α−1)/(2α) ∈ (0,½)`),
> • The composition of a convex non-decreasing function with a concave function is convex,
>   but we actually need the sign: the second term has a factor `−(α−1) < 0` which
>   flips concave → convex.
> More precisely: `σ ↦ Tr[(σ^{−γ} H σ^{−γ})^p]` is concave (by Lieb + trace function convexity),
> so `σ ↦ −(α−1) · Tr[(σ^{−γ} H σ^{−γ})^p]` is convex.

```lean
theorem f_alpha_convex_in_sigma (hα : 1 < α) (H : HermitianMat d ℂ) (hH : 0 ≤ H)
    (ρ : MState d) {ι : Type*} [Fintype ι]
    (w : ι → ℝ) (hw_nonneg : ∀ i, 0 ≤ w i) (hw_sum : ∑ i, w i = 1)
    (σs : ι → MState d) (σ_mix : MState d)
    (hσ_mix : σ_mix.M = ∑ i, w i • (σs i).M) :
    f_alpha α H ρ σ_mix ≤ ∑ i, w i * f_alpha α H ρ (σs i)
```

**`f_alpha_jointly_convex`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L494).

```lean
lemma f_alpha_jointly_convex (hα : 1 < α) (H : HermitianMat d ℂ) (hH : 0 ≤ H)
    {ι : Type*} [Fintype ι]
    (w : ι → ℝ) (hw_nonneg : ∀ i, 0 ≤ w i) (hw_sum : ∑ i, w i = 1)
    (ρs σs : ι → MState d) (ρ_mix σ_mix : MState d)
    (hρ_mix : ρ_mix.M = ∑ i, w i • (ρs i).M)
    (hσ_mix : σ_mix.M = ∑ i, w i • (σs i).M) :
    f_alpha α H ρ_mix σ_mix ≤ ∑ i, w i * f_alpha α H (ρs i) (σs i)
```

**`f_alpha_bddAbove`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L517).

```lean
lemma f_alpha_bddAbove (hα : 1 < α) (ρ σ : MState d) (hker : σ.M.ker ≤ ρ.M.ker) :
    BddAbove (Set.range (fun H : {H : HermitianMat d ℂ // 0 ≤ H} => f_alpha α H.1 ρ σ))
```

**`iSup_f_alpha_jointly_convex`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L527).

```lean
lemma iSup_f_alpha_jointly_convex (hα : 1 < α)
    {ι : Type*} [Fintype ι]
    (w : ι → ℝ) (hw_nonneg : ∀ i, 0 ≤ w i) (hw_sum : ∑ i, w i = 1)
    (ρs σs : ι → MState d) (ρ_mix σ_mix : MState d)
    (hρ_mix : ρ_mix.M = ∑ i, w i • (ρs i).M)
    (hσ_mix : σ_mix.M = ∑ i, w i • (σs i).M)
    (hker : ∀ i, (σs i).M.ker ≤ (ρs i).M.ker) :
    (⨆ (H : {H : HermitianMat d ℂ // 0 ≤ H}), f_alpha α H.1 ρ_mix σ_mix) ≤
      ∑ i, w i * (⨆ (H : {H : HermitianMat d ℂ // 0 ≤ H}), f_alpha α H.1 (ρs i) (σs i))
```

**`HermitianMat.ker_weighted_sum_le`**, a theorem, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L545). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If for all i, ker(σs i) ≤ ker(ρs i), then ker(∑ w i • σs i) ≤ ker(∑ w i • ρs i),
> provided all weights are nonneg and all matrices are PSD.

```lean
theorem HermitianMat.ker_weighted_sum_le {ι : Type*} [Fintype ι]
    (w : ι → ℝ) (hw_nonneg : ∀ i, 0 ≤ w i)
    (ρs σs : ι → HermitianMat d ℂ)
    (hρs_nonneg : ∀ i, 0 ≤ ρs i)
    (hσs_nonneg : ∀ i, 0 ≤ σs i)
    (hker : ∀ i, (σs i).ker ≤ (ρs i).ker) :
    (∑ i, w i • σs i).ker ≤ (∑ i, w i • ρs i).ker
```

**`sandwichedTraceFunctional_jointly_convex`**, a theorem, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L568). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace functional `Q̃_α` is jointly convex for `α > 1`.
> This is Proposition 3 of the paper, originally from Frank–Lieb.
> The proof uses the variational formula:
>   `Q̃_α(ρ‖σ) = sup_{H ≥ 0} f_α(H, ρ, σ)`
> where `f_α(H, ρ, σ) = α · Tr[ρ H] - (α-1) · Tr[(σ^{-γ} H σ^{-γ})^{α/(α-1)}]`
> is jointly convex in `(ρ, σ)` for fixed `H` (since the first term is linear and
> the second uses the convexity of trace functions). The supremum of jointly convex
> functions is jointly convex.

```lean
theorem sandwichedTraceFunctional_jointly_convex (hα : 1 < α) {ι : Type*} [Fintype ι]
    (w : ι → ℝ) (hw_nonneg : ∀ i, 0 ≤ w i) (hw_sum : ∑ i, w i = 1)
    (ρs σs : ι → MState d) (ρ_mix σ_mix : MState d)
    (hρ_mix : ρ_mix.M = ∑ i, w i • (ρs i).M)
    (hσ_mix : σ_mix.M = ∑ i, w i • (σs i).M)
    (hker : ∀ i, (σs i).M.ker ≤ (ρs i).M.ker) :
    Q̃_ α(ρ_mix‖σ_mix) ≤ ∑ i, w i * Q̃_ α(ρs i‖σs i)
```

### Twirling Construction Helpers

> We construct a twirling set using κ = Perm dB × (dB → Bool).
> For each (σ, f), the unitary V(σ,f) is the product of a sign-diagonal matrix
> (with entries ±1 determined by f) and a permutation matrix.
> The averaging property follows from:
> 1. Sign averaging: summing over f kills off-diagonal entries
> 2. Permutation averaging: summing over σ uniformizes diagonal entries

## Twirling Set

> A twirling set for a finite-dimensional system `dB` is a set of unitary matrices
> `{V_i}` on `dB` (indexed by some finite type `κ`) such that the average
> `(1/|κ|) Σ_i V_i X V_i†` equals `Tr(X) · (1/dim(dB))` for all `X`.
> When applied as `1_A ⊗ V_i` on a bipartite system `dA × dB`, this gives:
> `(1/|κ|) Σ_i (1_A ⊗ V_i) ρ_AB (1_A ⊗ V_i)† = ρ_A ⊗ π_B`
> where `π_B = 1/dim(dB)` is the maximally mixed state.
>
> The standard construction uses the Heisenberg–Weyl (discrete Weyl) operators.

## Tensor Invariance

> `Q̃_α(ρ ⊗ τ ‖ σ ⊗ τ) = Q̃_α(ρ ‖ σ)` for any state `τ`.
> This corresponds to equation (2.4) in the paper.

**`sandwichedTraceFunctional_mul`**, a lemma, [line 827](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L827).

```lean
lemma sandwichedTraceFunctional_mul
    (ρ₁ σ₁ : MState dA) (ρ₂ σ₂ : MState dB) :
    Q̃_ α(ρ₁ ⊗ᴹ ρ₂‖σ₁ ⊗ᴹ σ₂) = Q̃_ α(ρ₁‖σ₁) * Q̃_ α(ρ₂‖σ₂)
```

**`sandwichedTraceFunctional_self`**, a lemma, [line 838](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L838).

```lean
lemma sandwichedTraceFunctional_self (hα : 0 < α) (ρ : MState d) :
    Q̃_ α(ρ‖ρ) = 1
```

**`sandwichedTraceFunctional_tensor_invariant`**, a theorem, [line 861](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L861). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace functional is invariant under tensoring with a fixed state.
> This follows from multiplicativity (`sandwichedTraceFunctional_mul`) and
> the self-trace-functional being 1 (`sandwichedTraceFunctional_self`).

```lean
theorem sandwichedTraceFunctional_tensor_invariant (hα : 0 < α)
    (ρ σ : MState dA) (τ : MState dB) :
    Q̃_ α(ρ ⊗ᴹ τ‖σ ⊗ᴹ τ) = Q̃_ α(ρ‖σ)
```

## Twirling MState Helpers

> Helper lemmas for constructing MStates via the twirling argument.

**`MState.conjTensorUnitary`**, a def, [line 872](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L872).

> The MState obtained by conjugating a bipartite state by `1_A ⊗ V` where `V` is a unitary
> on the `B` system. This is `(1_A ⊗ V) ρ_AB (1_A ⊗ V)†`.

```lean
def MState.conjTensorUnitary (ρ : MState (dA × dB)) (V : Matrix.unitaryGroup dB ℂ) :
    MState (dA × dB)
```

**`MState.conjTensorUnitary_M`**, a theorem, [line 879](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L879). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The twirled MState: averaging conjugation by `1_A ⊗ V_i` over all elements of
> the twirling set gives `ρ_A ⊗ uniform_B`. We state the HermitianMat-level
> equality needed for the joint convexity argument.

```lean
theorem MState.conjTensorUnitary_M (ρ : MState (dA × dB)) (V : Matrix.unitaryGroup dB ℂ) :
    (ρ.conjTensorUnitary V).M = ρ.M.conj ((1 : Matrix.unitaryGroup dA ℂ) ⊗ᵤ V).val
```

**`sandwichedTraceFunctional_conj_tensorUnitary`**, a theorem, [line 884](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L884). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trace functional is invariant under `1_A ⊗ V` conjugation.

```lean
theorem sandwichedTraceFunctional_conj_tensorUnitary
    (ρ σ : MState (dA × dB)) (V : Matrix.unitaryGroup dB ℂ) :
    Q̃_ α(ρ.conjTensorUnitary V‖σ.conjTensorUnitary V) = Q̃_ α(ρ‖σ)
```

**`conj_kron_one_entry`**, a lemma, [line 899](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L899).

```lean
lemma conj_kron_one_entry (M : Matrix (dA × dB) (dA × dB) ℂ)
    (V : Matrix dB dB ℂ) (a₁ a₂ : dA) (b₁ b₂ : dB) :
    (Matrix.kroneckerMap (· * ·) (1 : Matrix dA dA ℂ) V * M *
     (Matrix.kroneckerMap (· * ·) (1 : Matrix dA dA ℂ) V).conjTranspose) (a₁, b₁) (a₂, b₂) =
    (V * (Matrix.of fun b₁' b₂' => M (a₁, b₁') (a₂, b₂')) * V.conjTranspose) b₁ b₂
```

**`twirling_hermitian_entry`**, a lemma, [line 923](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L923).

```lean
lemma twirling_hermitian_entry
    (κ : Type) [Fintype κ] (V : κ → Matrix.unitaryGroup dB ℂ)
    (hV : ∀ (X : HermitianMat dB ℂ),
      (Fintype.card κ : ℝ)⁻¹ • ∑ i : κ, X.conj (V i : Matrix dB dB ℂ) =
        (X.trace / Fintype.card dB) • (1 : HermitianMat dB ℂ))
    (X : HermitianMat dB ℂ) (b₁ b₂ : dB) :
    ∑ i : κ, ((V i).val * X.val * (V i).val.conjTranspose) b₁ b₂ =
    (X.val.trace / (Fintype.card dB : ℂ)) * (Fintype.card κ : ℂ) *
      (if b₁ = b₂ then 1 else 0)
```

**`twirling_general_matrix`**, a lemma, [line 948](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L948).

```lean
lemma twirling_general_matrix
    (κ : Type) [Fintype κ] (V : κ → Matrix.unitaryGroup dB ℂ)
    (hV : ∀ (X : HermitianMat dB ℂ),
      (Fintype.card κ : ℝ)⁻¹ • ∑ i : κ, X.conj (V i : Matrix dB dB ℂ) =
        (X.trace / Fintype.card dB) • (1 : HermitianMat dB ℂ))
    (X : Matrix dB dB ℂ) (b₁ b₂ : dB) :
    ∑ i : κ, ((V i).val * X * (V i).val.conjTranspose) b₁ b₂ =
    (X.trace / (Fintype.card dB : ℂ)) * (Fintype.card κ : ℂ) *
      (if b₁ = b₂ then 1 else 0)
```

**`MState.conjTensorUnitary'`**, a def, [line 980](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L980).

> The MState obtained by conjugating a bipartite state by `1_A ⊗ V`.

```lean
def MState.conjTensorUnitary' (ρ : MState (dA × dB)) (V : Matrix.unitaryGroup dB ℂ) :
    MState (dA × dB)
```

**`conjTensorUnitary'_entry`**, a lemma, [line 985](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L985).

```lean
lemma conjTensorUnitary'_entry (ρ : MState (dA × dB)) (V : Matrix.unitaryGroup dB ℂ)
    (a₁ a₂ : dA) (b₁ b₂ : dB) :
    (ρ.conjTensorUnitary' V).M.val (a₁, b₁) (a₂, b₂) =
    ((V : Matrix dB dB ℂ) * (Matrix.of fun b₁' b₂' => ρ.M.val (a₁, b₁') (a₂, b₂')) *
     (V : Matrix dB dB ℂ).conjTranspose) b₁ b₂
```

**`prod_traceRight_uniform_entry`**, a lemma, [line 993](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L993).

```lean
lemma prod_traceRight_uniform_entry [Nonempty dB] (ρ : MState (dA × dB))
    (a₁ a₂ : dA) (b₁ b₂ : dB) :
    (ρ.traceRight ⊗ᴹ MState.uniform).M.val (a₁, b₁) (a₂, b₂) =
    ρ.M.val.traceRight a₁ a₂ * ((Fintype.card dB : ℂ)⁻¹ * if b₁ = b₂ then 1 else 0)
```

**`twirling_average_eq`**, a lemma, [line 1006](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1006).

```lean
lemma twirling_average_eq [Nonempty dB]
    (κ : Type) [Fintype κ] (V : κ → Matrix.unitaryGroup dB ℂ)
    (hV : ∀ (X : HermitianMat dB ℂ),
      (Fintype.card κ : ℝ)⁻¹ • ∑ i : κ, X.conj (V i : Matrix dB dB ℂ) =
        (X.trace / Fintype.card dB) • (1 : HermitianMat dB ℂ))
    (ρ : MState (dA × dB)) :
    ∑ i : κ, ((Fintype.card κ : ℝ)⁻¹ • (ρ.conjTensorUnitary' (V i)).M) =
      (ρ.traceRight ⊗ᴹ MState.uniform).M
```

## Monotonicity Under Partial Trace (α > 1)

> The main intermediate result: for `α > 1`, the trace functional `Q̃_α` is monotone
> under partial trace:
> `Q̃_α(ρ_AB ‖ σ_AB) ≥ Q̃_α(ρ_A ‖ σ_A)`.
>
> The proof uses the twirling argument:
> 1. By unitary invariance, `Q̃_α(ρ_AB‖σ_AB) = Q̃_α(V_i ρ_AB V_i†‖V_i σ_AB V_i†)` for each `i`.
> 2. Averaging: `Q̃_α(ρ_AB‖σ_AB) = (1/|κ|) Σ_i Q̃_α(V_i ρ_AB V_i†‖V_i σ_AB V_i†)`.
> 3. By joint convexity (α > 1): `≥ Q̃_α((1/|κ|) Σ_i V_i ρ_AB V_i†‖(1/|κ|) Σ_i V_i σ_AB V_i†)`.
> 4. By twirling: `= Q̃_α(ρ_A ⊗ π_B ‖ σ_A ⊗ π_B)`.
> 5. By tensor invariance: `= Q̃_α(ρ_A ‖ σ_A)`.

**`ker_conj_le_of_ker_le`**, a lemma, [line 1065](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1065).

> If `σ.M.ker ≤ ρ.M.ker`, then `(σ.conj B).ker ≤ (ρ.conj B).ker` for any matrix `B`.
> This follows from `ker_conj` (which expresses `(A.conj B).ker` as a `comap`) and
> `Submodule.comap_mono`.

```lean
lemma ker_conj_le_of_ker_le {n : Type*} [Fintype n] [DecidableEq n]
    {A B : HermitianMat n ℂ} (hA : 0 ≤ A) (hB : 0 ≤ B) (h : A.ker ≤ B.ker)
    (C : Matrix n n ℂ) : (A.conj C).ker ≤ (B.conj C).ker
```

**`MState.ker_conjTensorUnitary_le`**, a lemma, [line 1073](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1073).

> Unitary conjugation preserves the kernel ordering between MStates.
> If `σ.M.ker ≤ ρ.M.ker`, then `(σ.conjTensorUnitary V).M.ker ≤ (ρ.conjTensorUnitary V).M.ker`.

```lean
lemma MState.ker_conjTensorUnitary_le {dA dB : Type*} [Fintype dA] [Fintype dB]
    [DecidableEq dA] [DecidableEq dB]
    (ρ σ : MState (dA × dB)) (V : Matrix.unitaryGroup dB ℂ)
    (hker : σ.M.ker ≤ ρ.M.ker) :
    (σ.conjTensorUnitary V).M.ker ≤ (ρ.conjTensorUnitary V).M.ker
```

**`sandwichedTraceFunctional_mono_traceRight`**, a theorem, [line 1083](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1083). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Monotonicity of the trace functional under partial trace for `α > 1`.
> Equation (2.8) of the paper (second line).

```lean
theorem sandwichedTraceFunctional_mono_traceRight [Nonempty dB]
    (hα : 1 < α) (ρ σ : MState (dA × dB)) (hker : σ.M.ker ≤ ρ.M.ker) :
    Q̃_ α(ρ.traceRight‖σ.traceRight) ≤ Q̃_ α(ρ‖σ)
```

## DPI for Sandwiched Rényi Divergence Under Partial Trace

**`ker_le_traceRight`**, a theorem, [line 1177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1177). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The kernel condition `σ.M.ker ≤ ρ.M.ker` is preserved under partial trace.
> This follows because `supp(ρ) ⊆ supp(σ)` implies `supp(Tr_B ρ) ⊆ supp(Tr_B σ)`:
> if `v ∈ supp(Tr_B ρ)`, then `⟨v, (Tr_B ρ) v⟩ > 0`, so for some basis vector `e_b`
> we have `v ⊗ e_b ∈ supp(ρ) ⊆ supp(σ)`, hence `⟨v, (Tr_B σ) v⟩ ≥ ⟨v ⊗ e_b, σ (v ⊗ e_b)⟩ > 0`.

```lean
theorem ker_le_traceRight {ρ σ : MState (dA × dB)}
    (hker : σ.M.ker ≤ ρ.M.ker) :
    σ.traceRight.M.ker ≤ ρ.traceRight.M.ker
```

**`sandwichedRenyiEntropy_mono_traceRight`**, a theorem, [line 1209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1209). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The sandwiched Rényi divergence is monotone under partial trace for `α > 1`.
> This follows from monotonicity of the trace functional together with the fact that
> `D̃_α = log(Q̃_α) / (α - 1)` and both `log` and `1/(α-1)` are order-preserving for α > 1.

```lean
theorem sandwichedRenyiEntropy_mono_traceRight [Nonempty dB]
    (hα : 1 < α) (ρ σ : MState (dA × dB))
    (hker : σ.M.ker ≤ ρ.M.ker) :
    D̃_ α(ρ.traceRight‖σ.traceRight) ≤ D̃_ α(ρ‖σ)
```

## DPI via Stinespring Dilation

**`sandwichedRenyiEntropy_conj_unitary`**, a lemma, [line 1231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1231).

```lean
lemma sandwichedRenyiEntropy_conj_unitary (hα : 0 < α) (ρ σ : MState d)
    (U : Matrix.unitaryGroup d ℂ) :
    D̃_ α(ρ.uConj U‖σ.uConj U) = D̃_ α(ρ‖σ)
```

**`sandwichedRenyiEntropy_tensor_pure`**, a lemma, [line 1287](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1287).

```lean
lemma sandwichedRenyiEntropy_tensor_pure (hα : 0 < α) (ρ σ : MState d₁) (ψ : Ket d₂) :
    D̃_ α(ρ ⊗ᴹ MState.pure ψ‖σ ⊗ᴹ MState.pure ψ) = D̃_ α(ρ‖σ)
```

**`sandwichedRenyiEntropy_SWAP`**, a theorem, [line 1293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1293). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The sandwiched Rényi divergence is invariant under SWAP.

```lean
theorem sandwichedRenyiEntropy_SWAP (ρ σ : MState (dA × dB)) :
    D̃_ α(ρ.SWAP‖σ.SWAP) = D̃_ α(ρ‖σ)
```

**`sandwichedRenyiEntropy_mono_traceRight'`**, a lemma, [line 1302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1302).

```lean
lemma sandwichedRenyiEntropy_mono_traceRight' [Nonempty dB]
    (hα : 1 < α) (ρ σ : MState (dA × dB)) :
    D̃_ α(ρ.traceRight‖σ.traceRight) ≤ D̃_ α(ρ‖σ)
```

**`sandwichedRenyiEntropy_mono_traceLeft`**, a theorem, [line 1314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1314). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Monotonicity of the sandwiched Rényi divergence under `traceLeft` for `α > 1`.
> Follows from `sandwichedRenyiEntropy_mono_traceRight'` + SWAP invariance.

```lean
theorem sandwichedRenyiEntropy_mono_traceLeft [Nonempty dA]
    (hα : 1 < α) (ρ σ : MState (dA × dB)) :
    D̃_ α(ρ.traceLeft‖σ.traceLeft) ≤ D̃_ α(ρ‖σ)
```

**`prep_append_eq_tensor_pure`**, a theorem, [line 1327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1327). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Helper: The Stinespring preparation `prep ∘ append` equals tensoring with a fixed pure state.
> `append = ofEquiv (Equiv.prodPUnit d₁).symm`.
> …

```lean
theorem prep_append_eq_tensor_pure [Inhabited d₂] (ρ : MState d₁) :
    let ψ₀ : Ket (d₂ × d₂) := Ket.basis default
    let τ := MState.pure ψ₀
    let zero_prep : CPTPMap Unit (d₂ × d₂) := CPTPMap.replacement τ
    let prep := (CPTPMap.id ⊗ᶜᵖ zero_prep)
    let append : CPTPMap d₁ (d₁ × Unit) := CPTPMap.ofEquiv (Equiv.prodPUnit d₁).symm
    (prep ∘ₘ append) ρ = ρ ⊗ᴹ τ
```

**`sandwichedRenyiEntropy_DPI_gt_one`**, a theorem, [line 1349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1349). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Data Processing Inequality for the Sandwiched Rényi relative entropy (α > 1).
> Every CPTP map `Φ` satisfies `D̃_α(Φρ‖Φσ) ≤ D̃_α(ρ‖σ)`.
>
> The proof uses the Stinespring representation (see `CPTPMap.exists_purify`):
> every CPTP map can be written as ancilla preparation + unitary conjugation + partial trace.
> Since the sandwiched Rényi divergence is invariant under the first two operations
> (by additivity and relabel invariance) and monotone under partial trace
> (by `sandwichedRenyiEntropy_mono_traceRight`), the DPI follows.

```lean
theorem sandwichedRenyiEntropy_DPI_gt_one (hα : 1 < α) (ρ σ : MState d₁) (Φ : CPTPMap d₁ d₂) :
    D̃_ α(Φ ρ‖Φ σ) ≤ D̃_ α(ρ‖σ)
```

**`sandwichedRenyiEntropy_DPI_eq_one`**, a lemma, [line 1385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1385).

```lean
lemma sandwichedRenyiEntropy_DPI_eq_one (ρ σ : MState d₁) (Φ : CPTPMap d₁ d₂) :
    D̃_ 1(Φ ρ‖Φ σ) ≤ D̃_ 1(ρ‖σ)
```

**`sandwichedRenyiEntropy_DPI`**, a theorem, [line 1401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1401). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Data Processing Inequality for the Sandwiched Renyi relative entropy.
> Proved following the approach of Frank–Lieb and Leditzky–Rouzé–Datta.

```lean
theorem sandwichedRenyiEntropy_DPI (hα : 1 ≤ α) (ρ σ : MState d₁) (Φ : CPTPMap d₁ d₂) :
    D̃_ α(Φ ρ‖Φ σ) ≤ D̃_ α(ρ‖σ)
```

## Joint Convexity of the Relative Entropy

> Joint convexity of the (Umegaki) quantum relative entropy is derived from joint convexity
> of the trace functional `Q̃_α` (`sandwichedTraceFunctional_jointly_convex`) by letting
> `α → 1⁺`, in the same way that `sandwichedRenyiEntropy_DPI_eq_one` follows from the
> `α > 1` case.
>
> For `α > 1` and states with compatible kernels, `log x ≤ x - 1` gives
> `D̃_α(ρ‖σ) = log (Q̃_α(ρ‖σ)) / (α - 1) ≤ (Q̃_α(ρ‖σ) - 1) / (α - 1)`, and the difference
> quotient on the right is jointly convex in `(ρ, σ)` because `Q̃_α` is. As `α → 1⁺`, the
> left-hand side tends to `𝐃(ρ‖σ)` (by `sandwichedRelRentropy.continuousOn`), and the
> difference quotient tends to `𝐃(ρ‖σ)` as well (since `Q̃_α = exp ((α - 1) D̃_α)` and
> `exp x ≤ 1 + x + x²` for `|x| ≤ 1`), so the convex combination passes to the limit.

**`sandwichedRelRentropy_tendsto_qRelativeEnt`**, a theorem, [line 1424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1424). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> As `α → 1⁺`, the sandwiched Rényi relative entropy `D̃_α(ρ‖σ)` tends to the relative
> entropy `𝐃(ρ‖σ) = D̃_1(ρ‖σ)`, by continuity of `α ↦ D̃_α` on `(0, ∞)`.

```lean
theorem sandwichedRelRentropy_tendsto_qRelativeEnt (ρ σ : MState d) :
    Filter.Tendsto (fun α : ℝ => D̃_ α(ρ‖σ)) (𝓝[>] 1) (𝓝 𝐃(ρ‖σ))
```

**`qRelativeEnt_joint_convexity`**, a theorem, [line 1523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean#L1523). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Joint convexity of the quantum relative entropy.
>
> This is stated using `Mixable`, rather than `ConvexOn`, because `MState d`
> is not an `AddCommMonoid`.

```lean
theorem qRelativeEnt_joint_convexity :
    ∀ (ρ₁ ρ₂ σ₁ σ₂ : MState d), ∀ (p : Prob),
      𝐃(p [ρ₁ ↔ ρ₂]‖p [σ₁ ↔ σ₂]) ≤ p * 𝐃(ρ₁‖σ₁) + (1 - p) * 𝐃(ρ₂‖σ₂)
```

## Depends on

- [QuantumInfo.Entropy.Relative](relative.md)
- [QuantumInfo.ForMathlib.HermitianMat.Unitary](../formathlib/hermitianmat/unitary.md)

## Proof depends on

- [QuantumInfo.ForMathlib.HermitianMat.LiebConcavity](../formathlib/hermitianmat/liebconcavity.md)

## Sources

- [QuantumInfo/Entropy/DPI.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/DPI.lean)
