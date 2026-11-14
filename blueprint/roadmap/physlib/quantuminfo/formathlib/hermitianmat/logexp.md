---
declaration: module
origin: cited
lean: Commute.exp_left', Commute.exp_right', HermitianMat.exp_nonneg, HermitianMat.exp_pos, HermitianMat.logApprox_mono, HermitianMat.logApprox_eq_cfc_scalar, HermitianMat.logApprox_eq_log_add_error, HermitianMat.log_mono
statement: formalized
proof: formalized
---

# Properties of the matrix logarithm and exponential

The module `QuantumInfo.ForMathlib.HermitianMat.LogExp`, [QuantumInfo/ForMathlib/HermitianMat/LogExp.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean): 42 declarations, 25 with a docstring, 12 listed as significant; 1 private, not shown.

> In particular, operator monotonicity and concavity of the matrix logarithm.
> These are proved using `inv_antitone`, so, first showing that the matrix inverse
> is operator antitone for positive definite matrices.

**`Matrix.IsHermitian.log_smul_of_ne_zero`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L28).

```lean
lemma Matrix.IsHermitian.log_smul_of_ne_zero {A : Matrix d d 𝕜} (hA : A.IsHermitian) (hx : x ≠ 0) :
    cfc Real.log (x • A) = (Real.log x) • cfc (if · = 0 then (0 : ℝ) else 1) A + cfc Real.log A
```

**`HermitianMat.exp`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L45).

> Matrix exponential of a Hermitian matrix, as given by the continuous
> functional calculus with `Real.exp`

```lean
def exp (A : HermitianMat d 𝕜) : HermitianMat d 𝕜
```

**`Commute.exp_left'`**, a theorem, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L50). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Primed because `Commute.exp_left` refers to `NormedSpace.exp` instead of `HermitianMat.exp`.

```lean
theorem _root_.Commute.exp_left' (hAB : Commute A.mat B.mat) :
    Commute (A.exp).mat B.mat
```

**`Commute.exp_right'`**, a theorem, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L56). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Primed because `Commute.exp_right` refers to `NormedSpace.exp` instead of `HermitianMat.exp`.

```lean
theorem _root_.Commute.exp_right' (hAB : Commute A.mat B.mat) :
    Commute A.mat (B.exp).mat
```

**`HermitianMat.reindex_exp`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L61).

```lean
lemma reindex_exp (e : d ≃ d₂) : (A.reindex e).exp = A.exp.reindex e
```

**`HermitianMat.nonSingular_exp`**, an instance, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L65).

```lean
instance nonSingular_exp : NonSingular A.exp
```

**`HermitianMat.exp_nonneg`**, a theorem, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L69). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrix exponential of a Hermitian matrix is nonnegative.

```lean
theorem exp_nonneg (A : HermitianMat d 𝕜) : 0 ≤ A.exp
```

**`HermitianMat.exp_pos`**, a theorem, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L76). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrix exponential of a Hermitian matrix is strictly positive (Loewner order).
> Requires `Nonempty` since over an empty index type every matrix equals zero and `0 < 0`
> is false.

```lean
theorem exp_pos [i : Nonempty d] (A : HermitianMat d 𝕜) : 0 < A.exp
```

**`HermitianMat.evalHermitianMatExp`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L87).

> Positivity extension for `HermitianMat.exp`: always strictly positive if `Nonempty d`.
> …

```lean
meta def evalHermitianMatExp : PositivityExt
```

**`HermitianMat.log`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L103).

> Matrix logarithm (base e) of a Hermitian matrix, as given by the elementwise
> real logarithm of the diagonal in a diagonalized form, using `Real.log`
>
> Note that this means that the nullspace of the image includes all of the nullspace of the
> original matrix. This contrasts to the standard definition, which is typically defined for
> positive *definite* matrices, and the nullspace of the image is exactly the
> (λ=1)-eigenspace of the original matrix. (We also get the (λ=-1)-eigenspace here!)
>
> It coincides with a standard definition if A is positive definite.

```lean
def log (A : HermitianMat d 𝕜) : HermitianMat d 𝕜
```

**`Commute.log_left'`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L108).

> Primed because `Commute.log_left` refers to `NormedSpace.log` instead of `HermitianMat.log`.

```lean
lemma _root_.Commute.log_left' (hAB : Commute A.mat B.mat) :
    Commute (A.log).mat B.mat
```

**`Commute.log_right'`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L114).

> Primed because `Commute.log_right` refers to `NormedSpace.log` instead of `HermitianMat.log`.

```lean
lemma _root_.Commute.log_right' (hAB : Commute A.mat B.mat) :
    Commute A.mat (B.log).mat
```

**`HermitianMat.reindex_log`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L119).

```lean
lemma reindex_log (e : d ≃ d₂) : (A.reindex e).log = A.log.reindex e
```

**`HermitianMat.log_zero`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L123).

```lean
lemma log_zero : (0 : HermitianMat d 𝕜).log = 0
```

**`HermitianMat.log_one`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L127).

```lean
lemma log_one : (1 : HermitianMat d 𝕜).log = 0
```

**`HermitianMat.log_smul_of_pos`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L130).

```lean
lemma log_smul_of_pos (A : HermitianMat d 𝕜) (hx : x ≠ 0) :
    (x • A).log = Real.log x • A.supportProj + A.log
```

**`HermitianMat.log_smul`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L136).

```lean
lemma log_smul {A : HermitianMat d 𝕜} {x : ℝ} (hx : x ≠ 0) [NonSingular A] :
    (x • A).log = Real.log x • 1 + A.log
```

**`HermitianMat.inv_antitone`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L144).

```lean
lemma inv_antitone (hA : A.mat.PosDef) (h : A ≤ B) : B⁻¹ ≤ A⁻¹
```

**`HermitianMat.Real.integral_inv_sub_inv_finite`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L182).

```lean
lemma Real.integral_inv_sub_inv_finite (x T : ℝ) (hx : 0 < x) (hT : 0 < T) :
    ∫ t in (0)..T, (1 / (1 + t) - 1 / (x + t)) = Real.log x + Real.log ((1 + T) / (x + T))
```

**`HermitianMat.Real.tendsto_log_div_add_atTop`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L202).

> The limit of $\log((1+T)/(x+T))$ as $T \to \infty$ is 0, for $x > 0$.

```lean
lemma Real.tendsto_log_div_add_atTop (x : ℝ) :
    Filter.Tendsto (fun T => Real.log ((1 + T) / (x + T))) .atTop (nhds 0)
```

**`HermitianMat.logApprox_mono`**, a theorem, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L215). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Monotonicity of the finite integral approximation of the logarithm.

```lean
theorem logApprox_mono {x y : HermitianMat d 𝕜} (hx : x.mat.PosDef) (hy : y.mat.PosDef)
    (hxy : x ≤ y) (T : ℝ) (hT : 0 < T) :
    ∫ t in (0)..T, ((1 + t)⁻¹ • (1 : HermitianMat d 𝕜) - (x + t • 1)⁻¹) ≤
    ∫ t in (0)..T, ((1 + t)⁻¹ • (1 : HermitianMat d 𝕜) - (y + t • 1)⁻¹)
```

**`HermitianMat.logApprox`**, a def, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L308).

```lean
noncomputable def logApprox {n 𝕜 : Type*} [Fintype n] [DecidableEq n] [RCLike 𝕜]
    (x : HermitianMat n 𝕜) (T : ℝ) : HermitianMat n 𝕜
```

**`HermitianMat.scalarLogApprox`**, a def, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L315).

```lean
noncomputable def scalarLogApprox (T : ℝ) (u : ℝ) : ℝ
```

**`HermitianMat.scalarLogApprox_eq`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L318).

```lean
lemma scalarLogApprox_eq (x T : ℝ) (hx : 0 < x) (hT : 0 < T) :
    scalarLogApprox T x = Real.log x + Real.log ((1 + T) / (x + T))
```

**`HermitianMat.logApprox_eq_cfc_scalar`**, a theorem, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L343). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrix log approximation is the CFC of the scalar log approximation.

```lean
theorem logApprox_eq_cfc_scalar
    (x : HermitianMat d 𝕜) (hx : x.mat.PosDef) (T : ℝ) (hT : 0 < T) :
    logApprox x T = x.cfc (scalarLogApprox T)
```

**`HermitianMat.logApprox_eq_log_add_error`**, a theorem, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L365). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The log approximation is the log plus an error term.

```lean
theorem logApprox_eq_log_add_error
    (x : HermitianMat d 𝕜) (hx : x.mat.PosDef) (T : ℝ) (hT : 0 < T) :
    logApprox x T = x.log + x.cfc (fun u => Real.log ((1 + T) / (u + T)))
```

**`HermitianMat.tendsto_cfc_log_div_add_atTop`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L382).

> The error term in the log approximation tends to 0 as T goes to infinity.

```lean
lemma tendsto_cfc_log_div_add_atTop (x : HermitianMat d 𝕜) :
    Tendsto (fun T => x.cfc (fun u => Real.log ((1 + T) / (u + T)))) atTop (nhds 0)
```

**`HermitianMat.tendsto_logApprox`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L401).

> The log approximation converges to the matrix logarithm.

```lean
lemma tendsto_logApprox {x : HermitianMat d 𝕜} (hx : x.mat.PosDef) :
  Tendsto (fun T => logApprox x T) atTop (nhds x.log)
```

**`HermitianMat.posDef_of_posDef_le`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L411).

```lean
lemma posDef_of_posDef_le (hA : A.mat.PosDef) (hAB : A ≤ B) : B.mat.PosDef
```

**`HermitianMat.log_mono`**, a theorem, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L420). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrix logarithm is operator monotone.

```lean
theorem log_mono (hA : A.mat.PosDef) (hAB : A ≤ B) : A.log ≤ B.log
```

**`HermitianMat.le_of_exp_commute`**, a theorem, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L427). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Monotonicity of exp on commuting operators.

```lean
theorem le_of_exp_commute (hAB₂ : A.exp ≤ B.exp) :
    A ≤ B
```

**`HermitianMat.inv_convex`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L443).

> The inverse function is operator convex on positive definite matrices.

```lean
lemma inv_convex {x y : HermitianMat d 𝕜} (hx : x.mat.PosDef) (hy : y.mat.PosDef)
    ⦃a b : ℝ⦄ (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
    (a • x + b • y)⁻¹ ≤ a • x⁻¹ + b • y⁻¹
```

**`HermitianMat.inv_shift_convex`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L536).

> The shifted inverse function is operator convex on positive definite matrices.

```lean
lemma inv_shift_convex {x y : HermitianMat d 𝕜} (hx : x.mat.PosDef) (hy : y.mat.PosDef)
    ⦃a b : ℝ⦄ (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) (t : ℝ) (ht : 0 ≤ t) :
    (a • x + b • y + t • 1)⁻¹ ≤ a • (x + t • 1)⁻¹ + b • (y + t • 1)⁻¹
```

**`HermitianMat.integrable_inv_shift`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L552).

> Definition of the approximation of the matrix logarithm.

```lean
lemma integrable_inv_shift {A : HermitianMat d 𝕜} (hA : A.mat.PosDef) (b : ℝ) (hb : 0 ≤ b) :
    IntervalIntegrable (fun t => (A + t • 1)⁻¹) volume 0 b
```

**`HermitianMat.logApprox_concave`**, a theorem, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L587). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The finite integral approximation of the matrix logarithm is operator concave.

```lean
theorem logApprox_concave {n 𝕜 : Type*} [Fintype n] [DecidableEq n] [RCLike 𝕜]
    {x y : HermitianMat n 𝕜} (hx : x.mat.PosDef) (hy : y.mat.PosDef)
    ⦃a b : ℝ⦄ (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) (T : ℝ) (hT : 0 ≤ T) :
    a • x.logApprox T + b • y.logApprox T ≤ (a • x + b • y).logApprox T
```

**`HermitianMat.log_concave`**, a theorem, [line 621](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L621). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrix logarithm is operator concave.

```lean
theorem log_concave {x y : HermitianMat d 𝕜} (hx : x.mat.PosDef) (hy : y.mat.PosDef)
    ⦃a b : ℝ⦄ (ha : 0 ≤ a) (hb : 0 ≤ b) (hab : a + b = 1) :
    a • x.log + b • y.log ≤ (a • x + b • y).log
```

**`HermitianMat.log_kron_diagonal`**, a lemma, [line 635](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L635).

```lean
lemma log_kron_diagonal {m n 𝕜 : Type*} [Fintype m] [DecidableEq m] [Fintype n] [DecidableEq n] [RCLike 𝕜]
    {d₁ : m → ℝ} {d₂ : n → ℝ} (h₁ : ∀ i, 0 < d₁ i) (h₂ : ∀ j, 0 < d₂ j) :
    (diagonal 𝕜 d₁ ⊗ₖ diagonal 𝕜 d₂).log =
    (diagonal 𝕜 d₁).log ⊗ₖ 1 + 1 ⊗ₖ (diagonal 𝕜 d₂).log
```

**`HermitianMat.log_conj_unitary`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L669).

> The logarithm of a Hermitian matrix conjugated by a unitary matrix is the conjugate of the logarithm.

```lean
lemma log_conj_unitary (A : HermitianMat d 𝕜) (U : Matrix.unitaryGroup d 𝕜) :
    (A.conj U.val).log = A.log.conj U.val
```

**`HermitianMat.inner_log_smul_of`**, a lemma, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L674).

```lean
lemma inner_log_smul_of [NonSingular A] {x : ℝ} (hx : x ≠ 0) :
    ⟪(x • A).log, B⟫ = Real.log x * B.trace + ⟪A.log, B⟫
```

**`HermitianMat.log_kron_diagonal_with_proj`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L680).

```lean
lemma log_kron_diagonal_with_proj {f : d → ℝ} {g : d₂ → ℝ}  :
    (diagonal 𝕜 f ⊗ₖ diagonal 𝕜 g).log =
    (diagonal 𝕜 f).log ⊗ₖ (diagonal 𝕜 g).supportProj +
    (diagonal 𝕜 f).supportProj ⊗ₖ (diagonal 𝕜 g).log
```

**`HermitianMat.log_kron_with_proj`**, a lemma, [line 701](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L701).

> Generalization of `HermitianMat.log_kron` for possibly singular matrices.

```lean
lemma log_kron_with_proj : (A ⊗ₖ B).log = A.log ⊗ₖ B.supportProj + A.supportProj ⊗ₖ B.log
```

**`HermitianMat.log_kron`**, a theorem, [line 715](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean#L715). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrix logarithm of the Kronecker product of two nonsingular Hermitian matrices is
> the sum of the Kronecker products of their logarithms with the identity matrix.

```lean
theorem log_kron [NonSingular A] [NonSingular B] : (A ⊗ₖ B).log = A.log ⊗ₖ 1 + 1 ⊗ₖ B.log
```

## Depends on

- [Projectors associated to Hermitian matrices](proj.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/LogExp.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LogExp.lean)
