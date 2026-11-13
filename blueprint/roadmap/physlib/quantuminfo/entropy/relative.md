---
declaration: module
origin: cited
lean: sandwichedRelRentropy_additive, qRelativeEnt_additive, qRelativeEnt_ker, qRelativeEnt_ne_top_iff, qRelativeEnt_eq_top_iff, qRelativeEnt_relabel, qRelativeEnt_rank, qMutualInfo_as_qRelativeEnt
statement: formalized
proof: formalized
---

# QuantumInfo.Entropy.Relative

The module `QuantumInfo.Entropy.Relative`, [QuantumInfo/Entropy/Relative.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean): 54 declarations, 21 with a docstring, 8 listed as significant; 70 private, not shown.

> To do relative entropies, we start with the \_sandwiched Renyi Relative Entropy\_ which is a nice general form.
> Then instead of proving many theorems (like DPI, relabelling, additivity, etc.) several times, we just prove
> it for this one quantity, then it follows for other quantities (like the relative entropy) as a special case.

**`weighted_jensen_rpow`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L51).

> Weighted Jensen inequality: for weights w\_j ≥ 0 with ∑ w\_j = 1, values b\_j ≥ 0,
> and q ≥ 1: (∑\_j w\_j * b\_j)^q ≤ ∑\_j w\_j * b\_j^q.
>
> This is the special case of `Real.rpow_arith_mean_le_arith_mean_rpow` applied to
> `Finset.univ`

```lean
lemma weighted_jensen_rpow (b w : d → ℝ) (q : ℝ)
  (hb : ∀ j, 0 ≤ b j) (hw : ∀ j, 0 ≤ w j) (hsum : ∑ j, w j = 1) (hq : 1 ≤ q) :
    (∑ j, w j * b j) ^ q ≤ ∑ j, w j * b j ^ q
```

**`doubly_stochastic_holder`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L62).

> Doubly stochastic Hölder inequality: for nonneg a, b, doubly stochastic w,
> and conjugate p, q > 1:
> ∑\_\{ij} a\_i * b\_j * w\_\{ij} ≤ (∑ a\_i^p)^\{1/p} * (∑ b\_j^q)^\{1/q}.

```lean
lemma doubly_stochastic_holder (a b : d → ℝ) (w : d → d → ℝ)
    (ha : ∀ i, 0 ≤ a i) (hb : ∀ j, 0 ≤ b j)
    (hw : ∀ i j, 0 ≤ w i j)
    (hrow : ∀ i, ∑ j, w i j = 1) (hcol : ∀ j, ∑ i, w i j = 1)
    (p q : ℝ) (hp : 1 < p) (hpq : 1/p + 1/q = 1) :
    ∑ i, ∑ j, a i * b j * w i j ≤ (∑ i, a i ^ p) ^ (1/p) * (∑ j, b j ^ q) ^ (1/q)
```

**`HermitianMat.inner_le_trace_rpow_mul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L104).

> Hermitian trace Hölder inequality: for PSD A, B and conjugate exponents p, q > 1,
> ⟪A, B⟫ ≤ Tr[A^p]^(1/p) * Tr[B^q]^(1/q).

```lean
lemma HermitianMat.inner_le_trace_rpow_mul
    {A B : HermitianMat d ℂ} (hA : 0 ≤ A) (hB : 0 ≤ B)
    (p q : ℝ) (hp : 1 < p) (hpq : 1/p + 1/q = 1) :
    ⟪A, B⟫_ℝ ≤ (A ^ p).trace ^ (1/p) * (B ^ q).trace ^ (1/q)
```

**`MState.rpow_le_one'`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L129).

```lean
lemma MState.rpow_le_one' {r : ℝ} (hσ : 0 < r) : σ.M ^ r ≤ 1
```

**`HermitianMat.eigenvalues_le_one_of_le_one`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L144).

> If A ≥ 0 and A ≤ 1, then each eigenvalue of A is in [0, 1].

```lean
lemma HermitianMat.eigenvalues_le_one_of_le_one
    (A : HermitianMat d ℂ) (hA1 : A ≤ 1) (i : d) :
    A.H.eigenvalues i ≤ 1
```

**`HermitianMat.trace_rpow_le_trace_of_le_one`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L174).

> For positive A ≤ 1 and p ≥ 1, `Tr[A^p] ≤ Tr[A]`.

```lean
lemma HermitianMat.trace_rpow_le_trace_of_le_one
    (A : HermitianMat d ℂ) (hA : 0 ≤ A) (hA1 : A ≤ 1)
    (p : ℝ) (hp : 1 ≤ p) :
    (A ^ p).trace ≤ A.trace
```

**`HermitianMat.rpow_neg_mul_rpow_eq_supportProj`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L249).

> For PSD A and p ≠ 0, `A^{-p} * A^p = HermitianMat.supportProj A`.

```lean
lemma HermitianMat.rpow_neg_mul_rpow_eq_supportProj
    {A : HermitianMat d ℂ} (hA : 0 ≤ A) {p : ℝ} (hp : p ≠ 0) :
    (A ^ (-p)).mat * (A ^ p).mat = A.supportProj.mat
```

**`HermitianMat.supportProj_mul_self`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L264).

```lean
lemma HermitianMat.supportProj_mul_self (A : HermitianMat d ℂ) :
    A.supportProj.mat * A.mat = A.mat
```

**`HermitianMat.inner_supportProj_self`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L292).

```lean
lemma HermitianMat.inner_supportProj_self (A : HermitianMat d ℂ) :
    ⟪A, A.supportProj⟫ = A.trace
```

**`HermitianMat.mul_supportProj_of_ker_le`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L303).

```lean
lemma HermitianMat.mul_supportProj_of_ker_le {A B : HermitianMat d ℂ}
  (h : LinearMap.ker B.lin.toLinearMap ≤ LinearMap.ker A.lin.toLinearMap) :
    A.mat * B.supportProj.mat = A.mat
```

**`HermitianMat.inner_supportProj_of_ker_le`**, a lemma, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L352).

```lean
lemma HermitianMat.inner_supportProj_of_ker_le {A B : HermitianMat d ℂ}
  (h : LinearMap.ker B.lin.toLinearMap ≤ LinearMap.ker A.lin.toLinearMap) :
    ⟪A, B.supportProj⟫ = A.trace
```

**`supportProj_inner_density`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L357).

```lean
lemma supportProj_inner_density (h : σ.M.ker ≤ ρ.M.ker) :
    ⟪σ.M.supportProj, ρ.M⟫_ℝ = 1
```

**`inner_log_sub_log_nonneg`**, a lemma, [line 1154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1154).

```lean
lemma inner_log_sub_log_nonneg (h : σ.M.ker ≤ ρ.M.ker) :
    0 ≤ ⟪ρ.M, ρ.M.log - σ.M.log⟫
```

**`sandwichedRelRentropy_nonneg`**, a lemma, [line 1170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1170).

```lean
lemma sandwichedRelRentropy_nonneg {α : ℝ} (hα : 0 < α) (h : σ.M.ker ≤ ρ.M.ker) :
    0 ≤ if α = 1 then ⟪ρ.M, ρ.M.log - σ.M.log⟫
      else ((ρ.M.conj (σ.M ^ ((1 - α)/(2 * α)) ).mat) ^ α).trace.log / (α - 1)
```

**`ker_kron_le_of_le`**, a lemma, [line 1187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1187).

> If the kernels of the components are contained, then the kernel of the Kronecker product is contained.

```lean
lemma ker_kron_le_of_le {d₁ d₂ : Type*} [Fintype d₁] [Fintype d₂] [DecidableEq d₁] [DecidableEq d₂]
    (A C : Matrix d₁ d₁ ℂ) (B D : Matrix d₂ d₂ ℂ)
    (hA : LinearMap.ker A.toEuclideanLin ≤ LinearMap.ker C.toEuclideanLin)
    (hB : LinearMap.ker B.toEuclideanLin ≤ LinearMap.ker D.toEuclideanLin) :
    LinearMap.ker (A.kronecker B).toEuclideanLin ≤ LinearMap.ker (C.kronecker D).toEuclideanLin
```

**`ker_le_of_ker_kron_le_left`**, a lemma, [line 1240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1240).

> If the kernel of a product state is contained in another, the left component kernel is contained.

```lean
lemma ker_le_of_ker_kron_le_left (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂)
  (h : (σ₁ ⊗ᴹ σ₂).M.ker ≤ (ρ₁ ⊗ᴹ ρ₂).M.ker) :
    σ₁.M.ker ≤ ρ₁.M.ker
```

**`ker_le_of_ker_kron_le_right`**, a lemma, [line 1324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1324).

> If the kernel of a product state is contained in another, the right component kernel is contained.

```lean
lemma ker_le_of_ker_kron_le_right (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂)
  (h : (σ₁ ⊗ᴹ σ₂).M.ker ≤ (ρ₁ ⊗ᴹ ρ₂).M.ker) :
    σ₂.M.ker ≤ ρ₂.M.ker
```

**`ker_prod_le_iff`**, a lemma, [line 1400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1400).

> The kernel of a product state is contained in another product state's kernel iff the individual
> kernels are contained.

```lean
lemma ker_prod_le_iff (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂) :
    (σ₁ ⊗ᴹ σ₂).M.ker ≤ (ρ₁ ⊗ᴹ ρ₂).M.ker ↔ σ₁.M.ker ≤ ρ₁.M.ker ∧ σ₂.M.ker ≤ ρ₂.M.ker
```

**`HermitianMat.inner_kron`**, a lemma, [line 1408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1408).

```lean
lemma HermitianMat.inner_kron
    (A : HermitianMat d₁ ℂ) (B : HermitianMat d₂ ℂ) (C : HermitianMat d₁ ℂ) (D : HermitianMat d₂ ℂ) :
    ⟪A ⊗ₖ B, C ⊗ₖ D⟫ = ⟪A, C⟫ * ⟪B, D⟫
```

**`continuousOn_rpow_uniform`**, a lemma, [line 1430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1430).

```lean
lemma continuousOn_rpow_uniform {K : Set ℝ} (hK : IsCompact K) :
    ContinuousOn (fun r : ℝ ↦ UniformOnFun.ofFun {K} (fun t : ℝ ↦ t ^ r)) (Set.Ioi 0)
```

**`sandwichedRelRentropy_additive_alpha_one_aux`**, a lemma, [line 1453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1453).

```lean
lemma sandwichedRelRentropy_additive_alpha_one_aux (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂)
  (h1 : σ₁.M.ker ≤ ρ₁.M.ker) (h2 : σ₂.M.ker ≤ ρ₂.M.ker) :
    ⟪(ρ₁ ⊗ᴹ ρ₂).M, (ρ₁ ⊗ᴹ ρ₂).M.log - (σ₁ ⊗ᴹ σ₂).M.log⟫ =
    ⟪ρ₁.M, ρ₁.M.log - σ₁.M.log⟫_ℝ + ⟪ρ₂.M, ρ₂.M.log - σ₂.M.log⟫
```

**`SandwichedRelRentropy`**, a def, [line 1471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1471).

> The Sandwiched Renyi Relative Entropy, defined with ln (nits). Note that at `α = 1` this definition
> switch to the standard Relative Entropy, for continuity. For α ≤ 0, this gives junk value 0. (There
> is no conventional value for α < 0; there is a continuous limit at α = 0, but it is complicated and
> unneeded at the moment.)

```lean
def SandwichedRelRentropy (α : ℝ) (ρ σ : MState d) : ENNReal
```

**`qRelativeEnt`**, a def, [line 1488](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1488).

> The quantum relative entropy `𝐃(ρ‖σ) := Tr[ρ (log ρ - log σ)]`. Also called
> the Umegaki quantum relative entropy, when it's necessary to distinguish from other
> relative entropies.

```lean
def qRelativeEnt (ρ σ : MState d) : ENNReal
```

**`sandwiched_term_product`**, a lemma, [line 1518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1518).

```lean
lemma sandwiched_term_product (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂) (α β : ℝ) :
    (((ρ₁ ⊗ᴹ ρ₂).M.conj ((σ₁ ⊗ᴹ σ₂).M ^ β).mat) ^ α).trace =
    ((ρ₁.M.conj (σ₁.M ^ β).mat) ^ α).trace * ((ρ₂.M.conj (σ₂.M ^ β).mat) ^ α).trace
```

**`sandwichedRelRentropy_additive_alpha_ne_one`**, a lemma, [line 1531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1531).

```lean
lemma sandwichedRelRentropy_additive_alpha_ne_one {α : ℝ} (hα : α ≠ 1) (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂) :
    D̃_ α(ρ₁ ⊗ᴹ ρ₂‖σ₁ ⊗ᴹ σ₂) = D̃_ α(ρ₁‖σ₁) + D̃_ α(ρ₂‖σ₂)
```

**`sandwichedRelRentropy_additive`**, a theorem, [line 1557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1557). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Sandwiched Renyi Relative entropy is additive when the inputs are product states

```lean
theorem sandwichedRelRentropy_additive (α) (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂) :
    D̃_ α(ρ₁ ⊗ᴹ ρ₂‖σ₁ ⊗ᴹ σ₂) = D̃_ α(ρ₁‖σ₁) + D̃_ α(ρ₂‖σ₂)
```

**`qRelativeEnt_additive`**, a theorem, [line 1565](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1565). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum relative entropy is additive when the inputs are product states

```lean
theorem qRelativeEnt_additive (ρ₁ σ₁ : MState d₁) (ρ₂ σ₂ : MState d₂) :
    𝐃(ρ₁ ⊗ᴹ ρ₂‖σ₁ ⊗ᴹ σ₂) = 𝐃(ρ₁‖σ₁) + 𝐃(ρ₂‖σ₂)
```

**`sandwichedRelRentropy_relabel`**, a lemma, [line 1572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1572).

```lean
lemma sandwichedRelRentropy_relabel (ρ σ : MState d) (e : d₂ ≃ d) :
    D̃_ α(ρ.relabel e‖σ.relabel e) = D̃_ α(ρ‖σ)
```

**`sandwichedRelRentropy_self`**, a lemma, [line 1580](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1580).

```lean
lemma sandwichedRelRentropy_self (hα : 0 < α) (ρ : MState d) :
  --Technically this holds for all α except for `-1` and `0`. But those are stupid.
  --TODO: Maybe SandwichedRelRentropy should actually be defined differently for α = 0?
    D̃_ α(ρ‖ρ) = 0
```

**`sandwichedRelEntropy_ne_top`**, a lemma, [line 1608](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1608).

```lean
lemma sandwichedRelEntropy_ne_top {ρ σ : MState d} [σ.M.NonSingular] : D̃_ α(ρ‖σ) ≠ ⊤
```

**`continuousOn_exponent`**, a lemma, [line 1614](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1614).

```lean
lemma continuousOn_exponent : ContinuousOn (fun α : ℝ => (1 - α) / (2 * α)) (Set.Ioi 0)
```

**`Complex.continuousOn_cpow_const_Ioi`**, a lemma, [line 1618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1618).

```lean
lemma Complex.continuousOn_cpow_const_Ioi (z : ℂ) :
    ContinuousOn (fun r : ℝ => z ^ (r : ℂ)) (Set.Ioi 0)
```

**`maps_to_Iio_of_Ioi_1`**, a lemma, [line 1627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1627).

> The function α ↦ (1 - α) / (2 * α) maps the interval (1, ∞) to (-∞, 0).

```lean
lemma maps_to_Iio_of_Ioi_1 : Set.MapsTo (fun α : ℝ => (1 - α) / (2 * α)) (Set.Ioi 1) (Set.Iio 0)
```

**`frontier_singleton`**, a lemma, [line 1637](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1637).

```lean
lemma frontier_singleton {X : Type*} [TopologicalSpace X] [T1Space X] [PerfectSpace X]
    (p : X) : frontier {p} = {p}
```

**`sandwichedRelRentropy.continuousOn`**, a lemma, [line 1765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1765).

```lean
lemma sandwichedRelRentropy.continuousOn (ρ σ : MState d) :
    ContinuousOn (fun α => D̃_ α(ρ‖σ)) (Set.Ioi 0)
```

**`qRelativeEnt_ker`**, a theorem, [line 1778](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1778). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Quantum relative entropy as `Tr[ρ (log ρ - log σ)]` when supports are contained.

```lean
theorem qRelativeEnt_ker {ρ σ : MState d} (h : σ.M.ker ≤ ρ.M.ker) :
    𝐃(ρ‖σ).toEReal = ⟪ρ.M, ρ.M.log - σ.M.log⟫
```

**`qRelativeEnt_ne_top_iff`**, a theorem, [line 1786](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1786). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum relative entropy is finite exactly when the support condition
> `σ.M.ker ≤ ρ.M.ker` holds.

```lean
theorem qRelativeEnt_ne_top_iff {ρ σ : MState d} : 𝐃(ρ‖σ) ≠ ⊤ ↔ σ.M.ker ≤ ρ.M.ker
```

**`qRelativeEnt_eq_top_iff`**, a theorem, [line 1792](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1792). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum relative entropy is `⊤` exactly when the support condition fails.

```lean
theorem qRelativeEnt_eq_top_iff {ρ σ : MState d} : 𝐃(ρ‖σ) = ⊤ ↔ ¬ σ.M.ker ≤ ρ.M.ker
```

**`qRelativeEnt_eq_neg_Sᵥₙ_add`**, a lemma, [line 1796](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1796).

```lean
lemma qRelativeEnt_eq_neg_Sᵥₙ_add (ρ σ : MState d) :
    (qRelativeEnt ρ σ).toEReal = -(Sᵥₙ ρ : EReal) +
      if σ.M.ker ≤ ρ.M.ker then (-⟪ρ.M, σ.M.log⟫ : EReal) else (⊤ : EReal)
```

**`qRelativeEnt_relabel`**, a theorem, [line 1806](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1806). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The quantum relative entropy is unchanged by `MState.relabel`

```lean
theorem qRelativeEnt_relabel (ρ σ : MState d) (e : d₂ ≃ d) :
    𝐃(ρ.relabel e‖σ.relabel e) = 𝐃(ρ‖σ)
```

**`sandwichedRelRentropy_of_unique`**, a lemma, [line 1811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1811).

```lean
lemma sandwichedRelRentropy_of_unique [Unique d] (ρ σ : MState d) :
    D̃_α(ρ‖σ) = 0
```

**`qRelEntropy_of_unique`**, a lemma, [line 1820](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1820).

```lean
lemma qRelEntropy_of_unique [Unique d] (ρ σ : MState d) :
    𝐃(ρ‖σ) = 0
```

**`sandwichedRelRentropy_heq_congr`**, a lemma, [line 1824](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1824).

```lean
lemma sandwichedRelRentropy_heq_congr
      {d₁ d₂ : Type u} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
      {ρ₁ σ₁ : MState d₁} {ρ₂ σ₂ : MState d₂} (hd : d₁ = d₂) (hρ : ρ₁ ≍ ρ₂) (hσ : σ₁ ≍ σ₂) :
    D̃_ α(ρ₁‖σ₁) = D̃_ α(ρ₂‖σ₂)
```

**`sandwichedRelRentropy_congr`**, a lemma, [line 1837](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1837).

```lean
lemma sandwichedRelRentropy_congr {α : ℝ}
      {d₁ d₂ : Type u} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
      {ρ₁ σ₁ : MState d₁} {ρ₂ σ₂ : MState d₂} (hd : d₁ = d₂)
        (hρ : ρ₁ = ρ₂.relabel (Equiv.cast hd)) (hσ : σ₁ = σ₂.relabel (Equiv.cast hd)) :
    D̃_ α(ρ₁‖σ₁) = D̃_ α(ρ₂‖σ₂)
```

**`qRelEntropy_heq_congr`**, a lemma, [line 1845](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1845).

```lean
lemma qRelEntropy_heq_congr {d₁ d₂ : Type u} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
      {ρ₁ σ₁ : MState d₁} {ρ₂ σ₂ : MState d₂} (hd : d₁ = d₂) (hρ : ρ₁ ≍ ρ₂) (hσ : σ₁ ≍ σ₂) :
    𝐃(ρ₁‖σ₁) = 𝐃(ρ₂‖σ₂)
```

**`qRelativeEnt_rank`**, a theorem, [line 1851](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1851). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Quantum relative entropy when σ has full rank

```lean
theorem qRelativeEnt_rank {ρ σ : MState d} [σ.M.NonSingular] :
    (𝐃(ρ‖σ) : EReal) = ⟪ρ.M, ρ.M.log - σ.M.log⟫
```

**`inner_log_bounded_near`**, a lemma, [line 1918](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L1918).

```lean
lemma inner_log_bounded_near (hx : σ.M.ker ≤ ρ.M.ker) {y : ℝ} (hy : ⟪ρ.M, σ.M.log⟫ < y) :
    ∀ᶠ x in nhds σ, x.M.ker ≤ ρ.M.ker → ⟪ρ.M, x.M.log⟫ < y
```

**`qRelativeEnt_lowerSemicontinuous_2`**, a lemma, [line 2046](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2046).

```lean
lemma qRelativeEnt_lowerSemicontinuous_2 (ρ x : MState d) (hx : ¬(x.M.ker ≤ ρ.M.ker)) (y : ENNReal) (hy : y < ⊤) :
    ∀ᶠ (x' : MState d) in nhds x,
      y < (if x'.M.ker ≤ ρ.M.ker then ⟪ρ.M, ρ.M.log - x'.M.log⟫ else ⊤ : EReal)
```

**`qRelativeEnt.lowerSemicontinuous`**, a lemma, [line 2088](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2088).

```lean
lemma qRelativeEnt.lowerSemicontinuous (ρ : MState d) : LowerSemicontinuous fun σ => 𝐃(ρ‖σ)
```

**`qRelEntropy_self`**, a lemma, [line 2119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2119).

```lean
lemma qRelEntropy_self (ρ : MState d) : 𝐃(ρ‖ρ) = 0
```

**`qRelativeEnt_ne_top`**, a lemma, [line 2123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2123).

```lean
lemma qRelativeEnt_ne_top {ρ σ : MState d} [σ.M.NonSingular] : 𝐃(ρ‖σ) ≠ ⊤
```

**`qMutualInfo_as_qRelativeEnt`**, a theorem, [line 2190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2190). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `I(A:B) = 𝐃(ρᴬᴮ‖ρᴬ ⊗ ρᴮ)`

```lean
theorem qMutualInfo_as_qRelativeEnt (ρ : MState (dA × dB)) :
    qMutualInfo ρ = (𝐃(ρ‖ρ.traceRight ⊗ᴹ ρ.traceLeft) : EReal)
```

**`qRelEntropy_le_add_of_le_smul`**, a lemma, [line 2417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2417).

```lean
lemma qRelEntropy_le_add_of_le_smul (ρ : MState d) {σ₁ σ₂ : MState d} (hσ : σ₂.M ≤ α • σ₁.M) :
    𝐃(ρ‖σ₁) ≤ 𝐃(ρ‖σ₂) + ENNReal.ofReal (Real.log α)
```

**`qRelativeEnt_op_le`**, a lemma, [line 2448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean#L2448).

```lean
lemma qRelativeEnt_op_le {ρ σ : MState d} (h : ρ.M ≤ α • σ.M) :
    𝐃(ρ‖σ) ≤ .ofReal (Real.log α)
```

## Depends on

- [QuantumInfo.Entropy.VonNeumann](vonneumann.md)

## Proof depends on

- [Schatten norms](../formathlib/hermitianmat/schatten.md)

## Sources

- [QuantumInfo/Entropy/Relative.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/Relative.lean)
