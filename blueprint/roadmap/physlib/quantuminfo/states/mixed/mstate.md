---
declaration: module
origin: cited
lean: MState.Hermitian, MState.m_inj, MState.convex, MState.exp_val_eq_zero_iff, MState.exp_val_eq_one_iff, MState.spectrum_pure_eq_constant, MState.pure_of_constant_spectrum, MState.pure_iff_constant_spectrum
statement: formalized
proof: formalized
---

# QuantumInfo.States.Mixed.MState

The module `QuantumInfo.States.Mixed.MState`, [QuantumInfo/States/Mixed/MState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean): 132 declarations (6 instances with no name), 54 with a docstring, 25 listed as significant.

> Finite dimensional quantum mixed states, ρ.
>
> The same comments apply as in `Braket`:
>
> These could be done with a Hilbert space of Fintype, which would look like
> ```lean4
> (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] [FiniteDimensional ℂ H]
> ```
> or by choosing a particular `Basis` and asserting it is `Fintype`. But frankly it seems easier to
> mostly focus on the basis-dependent notion of `Matrix`, which has the added benefit of an obvious
> "classical" interpretation (as the basis elements, or diagonal elements of a mixed state). In that
> sense, this quantum theory comes with the a particular classical theory always preferred.
>
> Important definitions:
>  * `instMixable`: the `Mixable` instance allowing convex combinations of `MState`s
>  * `ofClassical`: Mixed states representing classical distributions
>  * `purity`: The purity `Tr[ρ^2]` of a state
>  * `spectrum`: The spectrum of the matrix
>  * `uniform`: The maximally mixed state
>  * `mix`: The total state corresponding to an ensemble
>  * `average`: Averages a function over an ensemble, with appropriate weights

**`MState`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L51).

> A **mixed quantum state** is a PSD matrix with trace 1.
>
> We don't `extend (M : HermitianMat d ℂ)` because that gives an annoying thing where
> `M` is actually a `Subtype`, which means `ρ.M.foo` notation doesn't work.

```lean
structure MState (d : Type*) [Fintype d] [DecidableEq d] where
  M : HermitianMat d ℂ
  nonneg : 0 ≤ M
  tr : M.trace = 1
```

**`MState.instCoe`**, an instance, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L66).

```lean
instance instCoe : Coe (MState d) (HermitianMat d ℂ)
```

**`MState.m`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L71).

> The underlying `Matrix` in an MState. Prefer `MState.M` for the `HermitianMat`.

```lean
def m (ρ : MState d) : Matrix d d ℂ
```

**`MState.mat_M`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L74).

```lean
lemma mat_M : ρ.M.mat = ρ.m
```

**`MState.pos`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L77).

```lean
lemma pos (ρ : MState d) : 0 < ρ.M
```

**`MState.evalMStateM`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L88).

> Positivity extension for `MState.M`: it is always positive (`0 < ρ.M`).
> Note: we must not call `whnfR` on `e` because `MState.M` is a structure
> projection (reducible), so `whnfR` would reduce it and destroy the pattern.

```lean
meta def evalMStateM : PositivityExt
```

**`MState.psd`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L100).

```lean
lemma psd : ρ.m.PosSemidef
```

**`MState.Hermitian`**, a theorem, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L105). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Every mixed state is Hermitian.

```lean
theorem Hermitian : ρ.m.IsHermitian
```

**`MState.tr'`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L109).

```lean
lemma tr' : ρ.m.trace = 1
```

**`MState.ext_m`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L113).

```lean
lemma ext_m {ρ₁ ρ₂ : MState d} (h : ρ₁.m = ρ₂.m) : ρ₁ = ρ₂
```

**`MState.m_inj`**, a theorem, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L119). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The map from mixed states to their matrices is injective

```lean
theorem m_inj : (MState.m (d := d)).Injective
```

**`MState.M_Injective`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L122).

```lean
lemma M_Injective : Function.Injective (MState.M (d := d))
```

**`MState.convex`**, a theorem, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L128). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The matrices corresponding to MStates are `Convex ℝ`

```lean
theorem convex : Convex ℝ (Set.range (MState.M (d := d)))
```

**`MState.instMixable`**, an instance, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L136).

```lean
instance instMixable : Mixable (HermitianMat d ℂ) (MState d)
```

**`MState.nonempty`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L146).

> An MState is a witness that d is nonempty.

```lean
lemma nonempty : Nonempty d
```

**`MState.eigenvalue_nonneg`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L151).

```lean
lemma eigenvalue_nonneg : ∀ i, 0 ≤ ρ.Hermitian.eigenvalues i
```

**`MState.eigenvalue_le_one`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L157).

```lean
lemma eigenvalue_le_one : ∀ i, ρ.Hermitian.eigenvalues i ≤ 1
```

**`MState.le_one`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L162).

```lean
lemma le_one : ρ.M ≤ 1
```

**An instance with no name**, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L173).

> The inner product of two MState's, as a real number between 0 and 1.

```lean
scoped instance : Inner Prob (MState d)
```

**`MState.inner_def`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L178).

```lean
lemma inner_def : ⟪ρ, σ⟫_Prob = ⟨⟪ρ.M, σ.M⟫,
    inner_ge_zero ρ.nonneg σ.nonneg,
    (inner_le_mul_trace ρ.nonneg σ.nonneg).trans (by simp)⟩
```

**`MState.val_inner`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L183).

```lean
lemma val_inner : (⟪ρ, σ⟫_Prob : ℝ) = ⟪ρ.M, σ.M⟫
```

**`MState.exp_val_ℂ`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L188).

```lean
def exp_val_ℂ (T : Matrix d d ℂ) : ℂ
```

**`MState.exp_val`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L193).

> The **expectation value** of an operator on a quantum state.

```lean
def exp_val (T : HermitianMat d ℂ) : ℝ
```

**`MState.exp_val_nonneg`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L196).

```lean
lemma exp_val_nonneg {T : HermitianMat d ℂ} (h : 0 ≤ T) : 0 ≤ ρ.exp_val T
```

**`MState.exp_val_zero`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L203).

```lean
lemma exp_val_zero : ρ.exp_val 0 = 0
```

**`MState.exp_val_one`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L207).

```lean
lemma exp_val_one : ρ.exp_val 1 = 1
```

**`MState.exp_val_le_one`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L210).

```lean
lemma exp_val_le_one {T : HermitianMat d ℂ} (h : T ≤ 1) : ρ.exp_val T ≤ 1
```

**`MState.exp_val_prob`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L214).

```lean
lemma exp_val_prob {T : HermitianMat d ℂ} (h : 0 ≤ T ∧ T ≤ 1) :
    ρ.exp_val T ∈ unitInterval
```

**`MState.exp_val_sub`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L218).

```lean
lemma exp_val_sub (A B : HermitianMat d ℂ) :
    ρ.exp_val (A - B) = ρ.exp_val A - ρ.exp_val B
```

**`MState.exp_val_eq_zero_iff`**, a theorem, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L224). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If a PSD observable `A` has expectation value of 0 on a state `ρ`, it must entirely contain the
> support of `ρ` in its kernel.

```lean
theorem exp_val_eq_zero_iff {A : HermitianMat d ℂ} (hA₁ : 0 ≤ A) :
    ρ.exp_val A = 0 ↔ ρ.M.support ≤ A.ker
```

**`MState.exp_val_eq_one_iff`**, a theorem, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L230). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If an observable `A` has expectation value of 1 on a state `ρ`, it must entirely contain the
> support of `ρ` in its 1-eigenspace.

```lean
theorem exp_val_eq_one_iff {A : HermitianMat d ℂ} (hA₂ : A ≤ 1) :
    ρ.exp_val A = 1 ↔ ρ.M.support ≤ (1 - A).ker
```

**`MState.exp_val_add`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L236).

```lean
lemma exp_val_add (A B : HermitianMat d ℂ) :
    ρ.exp_val (A + B) = ρ.exp_val A + ρ.exp_val B
```

**`MState.exp_val_smul`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L241).

```lean
lemma exp_val_smul (r : ℝ) (A : HermitianMat d ℂ) :
    ρ.exp_val (r • A) = r * ρ.exp_val A
```

**`MState.exp_val_le_exp_val`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L246).

```lean
lemma exp_val_le_exp_val (ρ : MState d) {A B : HermitianMat d ℂ} (h : A ≤ B) :
    ρ.exp_val A ≤ ρ.exp_val B
```

**`MState.pure`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L257).

> A mixed state can be constructed as a pure state arising from a ket.

```lean
def pure (ψ : Ket d) : MState d
```

**`MState.pure_inner`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L270).

```lean
lemma pure_inner : ⟪pure ψ, pure φ⟫_Prob = ‖Braket.dot ψ φ‖^2
```

**`MState.pure_apply`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L284).

```lean
lemma pure_apply {i j : d} : (pure ψ).m i j = (ψ i) * conj (ψ j)
```

**`MState.pure_mul_self`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L288).

```lean
lemma pure_mul_self : (pure ψ).m * (pure ψ).m = (pure ψ : Matrix d d ℂ)
```

**`MState.purity`**, a def, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L294).

> The purity of a state is Tr[ρ^2]. This is a `Prob`, because it is always
> between zero and one.

```lean
def purity (ρ : MState d) : Prob
```

**`MState.spectrum`**, a def, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L297).

> The eigenvalue spectrum of a mixed quantum state, as a `Distribution`.

```lean
def spectrum (ρ : MState d) : ProbDistribution d
```

**`MState.spectrum_pure_eq_constant`**, a theorem, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L304). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The spectrum of a pure state is (1,0,0,...), i.e. a constant distribution.

```lean
theorem spectrum_pure_eq_constant :
    ∃ i, (pure ψ).spectrum = ProbDistribution.constant i
```

**`MState.pure_of_constant_spectrum`**, a theorem, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L371). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If the spectrum of a mixed state is (1,0,0...) i.e. a constant distribution, it is
> a pure state.

```lean
theorem pure_of_constant_spectrum (h : ∃ i, ρ.spectrum = ProbDistribution.constant i) :
    ∃ ψ, ρ = pure ψ
```

**`MState.pure_iff_constant_spectrum`**, a theorem, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L417). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A state ρ is pure iff its spectrum is (1,0,0,...) i.e. a constant distribution.

```lean
theorem pure_iff_constant_spectrum : (∃ ψ, ρ = pure ψ) ↔
    ∃ i, ρ.spectrum = ProbDistribution.constant i
```

**`MState.pure_iff_purity_one`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L423).

```lean
lemma pure_iff_purity_one : (∃ ψ, ρ = pure ψ) ↔ ρ.purity = 1
```

**`MState.spectralDecomposition`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L469).

```lean
lemma spectralDecomposition (ρ : MState d) :
    ∃ (ψs : d → Ket d), ρ.M = ∑ i, (ρ.spectrum i : ℝ) • (MState.pure (ψs i)).M
```

**`MState.prod`**, a def, [line 491](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L491).

```lean
def prod (ρ₁ : MState d₁) (ρ₂ : MState d₂) : MState (d₁ × d₂)
```

**`MState.prod_inner_prod`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L498).

```lean
lemma prod_inner_prod (ξ1 ψ1 : MState d₁) (ξ2 ψ2 : MState d₂) :
    ⟪ξ1 ⊗ᴹ ξ2, ψ1 ⊗ᴹ ψ2⟫_Prob = ⟪ξ1, ψ1⟫_Prob * ⟪ξ2, ψ2⟫_Prob
```

**`MState.pure_prod_pure`**, a theorem, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L509). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The product of pure states is a pure product state , `Ket.prod`.

```lean
theorem pure_prod_pure (ψ₁ : Ket d₁) (ψ₂ : Ket d₂) : pure (ψ₁ ⊗ᵠ ψ₂) = (pure ψ₁) ⊗ᴹ (pure ψ₂)
```

**`MState.ofClassical`**, a def, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L518).

> A representation of a classical distribution as a quantum state, diagonal in the given basis.

```lean
def ofClassical (dist : ProbDistribution d) : MState d
```

**`MState.coe_ofClassical`**, a lemma, [line 524](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L524).

```lean
lemma coe_ofClassical (dist : ProbDistribution d) :
    (ofClassical dist).M = diagonal ℂ (dist ·)
```

**`MState.ofClassical_pow`**, a lemma, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L528).

```lean
lemma ofClassical_pow (dist : ProbDistribution d) (p : ℝ) :
    (ofClassical dist).M ^ p = diagonal ℂ (fun i ↦ (dist i) ^ p)
```

**`MState.uniform`**, a def, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L533).

> The maximally mixed state.

```lean
def uniform [Nonempty d] : MState d
```

**`MState.instUnique`**, an instance, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L540).

> There is exactly one state on a dimension-1 system.

```lean
instance instUnique [Unique d] : Unique (MState d)
```

**`MState.instInhabited`**, an instance, [line 554](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L554).

> There exists a mixed state for every nonempty `d`.
> Here, the maximally mixed one is chosen.

```lean
instance instInhabited [Nonempty d] : Inhabited (MState d)
```

**`MState.default_eq`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L557).

```lean
lemma default_eq [Nonempty d] : (default : MState d) = uniform
```

**`MState.M_default`**, a lemma, [line 560](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L560).

```lean
lemma M_default [Unique d] : (default : MState d).M = 1
```

**`MState.traceLeft`**, a def, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L568).

> Partial tracing out the left half of a system.

```lean
def traceLeft (ρ : MState (d₁ × d₂)) : MState d₂
```

**`MState.traceRight`**, a def, [line 575](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L575).

> Partial tracing out the right half of a system.

```lean
def traceRight (ρ : MState (d₁ × d₂)) : MState d₁
```

**`MState.traceLeft_prod_eq`**, a theorem, [line 582](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L582). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Taking the direct product on the left and tracing it back out gives the same state.

```lean
theorem traceLeft_prod_eq (ρ₁ : MState d₁) (ρ₂ : MState d₂) : (ρ₁ ⊗ᴹ ρ₂).traceLeft = ρ₂
```

**`MState.traceRight_prod_eq`**, a theorem, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L588). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Taking the direct product on the right and tracing it back out gives the same state.

```lean
theorem traceRight_prod_eq (ρ₁ : MState d₁) (ρ₂ : MState d₂) : (ρ₁ ⊗ᴹ ρ₂).traceRight = ρ₁
```

**`MState.spectrum_prod`**, a theorem, [line 600](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L600). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Spectrum of direct product. There is a permutation σ so that the spectrum of the direct product of
> ρ₁ and ρ₂, as permuted under σ, is the pairwise products of the spectra of ρ₁ and ρ₂.

```lean
theorem spectrum_prod (ρ₁ : MState d₁) (ρ₂ : MState d₂) : ∃(σ : d₁ × d₂ ≃ d₁ × d₂),
    ∀i, ∀j, (ρ₁ ⊗ᴹ ρ₂).spectrum (σ (i, j)) = (ρ₁.spectrum i) * (ρ₂.spectrum j)
```

**`MState.sInf_spectrum_prod`**, a lemma, [line 639](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L639).

```lean
lemma sInf_spectrum_prod (ρ : MState d) (σ : MState d₂) :
    sInf (_root_.spectrum ℝ (ρ ⊗ᴹ σ).m) = sInf (_root_.spectrum ℝ ρ.m) * sInf (_root_.spectrum ℝ σ.m)
```

**`MState.IsSeparable`**, a def, [line 657](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L657).

> A mixed state is separable iff it can be written as a convex combination of product mixed states.

```lean
def IsSeparable (ρ : MState (d₁ × d₂)) : Prop
```

**`MState.IsSeparable_prod`**, a theorem, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L663). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A product state `MState.prod` is separable.

```lean
theorem IsSeparable_prod (ρ₁ : MState d₁) (ρ₂ : MState d₂) : IsSeparable (ρ₁ ⊗ᴹ ρ₂)
```

**`MState.eq_of_sum_eq_pure`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L669).

```lean
lemma eq_of_sum_eq_pure {d : Type*} [Fintype d] [DecidableEq d]
    {ι : Type*} {s : Finset ι} {p : ι → ℝ} {ρs : ι → MState d}
    {ρ : MState d} (h_pure : ρ.purity = 1) (h_sum : ρ.M = ∑ i ∈ s, p i • (ρs i).M)
    (hp_nonneg : ∀ i ∈ s, 0 ≤ p i) (hp_sum : ∑ i ∈ s, p i = 1) (i : ι) (hi : i ∈ s) (hpi : 0 < p i) :
    ρs i = ρ
```

**`MState.purity_prod`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L722).

```lean
lemma purity_prod {d₁ d₂ : Type*} [Fintype d₁] [Fintype d₂] [DecidableEq d₁] [DecidableEq d₂]
    (ρ₁ : MState d₁) (ρ₂ : MState d₂) : (ρ₁ ⊗ᴹ ρ₂).purity = ρ₁.purity * ρ₂.purity
```

**`MState.pure_eq_pure_iff`**, a lemma, [line 726](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L726).

```lean
lemma pure_eq_pure_iff {d : Type*} [Fintype d] [DecidableEq d] (ψ φ : Ket d) :
    pure ψ = pure φ ↔ ∃ z : ℂ, ‖z‖ = 1 ∧ ψ.vec = z • φ.vec
```

**`MState.PhaseEquiv_iff_pure_eq`**, a theorem, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L760). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Two kets are phase-equivalent if and only if their pure states are equal.

```lean
theorem PhaseEquiv_iff_pure_eq {d : Type*} [Fintype d] [DecidableEq d] (ψ φ : Ket d) :
    Ket.PhaseEquiv.r ψ φ ↔ MState.pure ψ = MState.pure φ
```

**`MState.pureQ`**, a def, [line 765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L765).

> `MState.pure` descends to the quotient `KetUpToPhase`.

```lean
def pureQ {d : Type*} [Fintype d] [DecidableEq d] : KetUpToPhase d → MState d
```

**`MState.pureQ_mk`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L769).

```lean
lemma pureQ_mk {d : Type*} [Fintype d] [DecidableEq d] (ψ : Ket d) :
    pureQ (Quotient.mk Ket.PhaseEquiv ψ) = MState.pure ψ
```

**`MState.pureQ_injective`**, a lemma, [line 772](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L772).

```lean
lemma pureQ_injective {d : Type*} [Fintype d] [DecidableEq d] : Function.Injective (pureQ (d := d))
```

**`MState.pure_separable_imp_IsProd`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L780).

```lean
lemma pure_separable_imp_IsProd {d₁ d₂ : Type*} [Fintype d₁] [Fintype d₂] [DecidableEq d₁] [DecidableEq d₂]
    (ψ : Ket (d₁ × d₂)) (h : IsSeparable (pure ψ)) : ψ.IsProd
```

**`MState.pure_separable_iff_IsProd`**, a theorem, [line 846](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L846). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A pure state is separable iff the ket is a product state.

```lean
theorem pure_separable_iff_IsProd (ψ : Ket (d₁ × d₂)) :
    IsSeparable (pure ψ) ↔ ψ.IsProd
```

**`MState.pure_iff_rank_eq_one`**, a theorem, [line 857](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L857). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A mixed state is pure if and only if its rank is 1.

```lean
theorem pure_iff_rank_eq_one {d : Type*} [Fintype d] [DecidableEq d] (ρ : MState d) :
    (∃ ψ, ρ = pure ψ) ↔ ρ.m.rank = 1
```

**`MState.Ket.IsProd_iff_rank_eq_one`**, a theorem, [line 921](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L921). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A ket on a product space is a product state if and only if its coefficient matrix has rank 1.

```lean
theorem Ket.IsProd_iff_rank_eq_one {d₁ d₂ : Type*} [Fintype d₁] [Fintype d₂] [DecidableEq d₁] [DecidableEq d₂]
    (ψ : Ket (d₁ × d₂)) :
    ψ.IsProd ↔ (Matrix.of (fun i j => ψ (i, j))).rank = 1
```

**`MState.pure_separable_iff_traceLeft_pure`**, a theorem, [line 973](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L973). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A pure state is separable iff the partial trace on the left is pure.

```lean
theorem pure_separable_iff_traceLeft_pure (ψ : Ket (d₁ × d₂)) : IsSeparable (pure ψ) ↔
    ∃ ψ₁, pure ψ₁ = (pure ψ).traceLeft
```

**`MState.purify`**, a def, [line 994](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L994).

> The purification of a mixed state. Always uses the full dimension of the Hilbert space (d) to
> purify, so e.g. an existing pure state with d=4 still becomes d=16 in the purification. The defining
> property is `MState.traceRight_of_purify`; see also `MState.purify'` for the bundled version.

```lean
def purify (ρ : MState d) : Ket (d × d)
```

**`MState.purify_spec`**, a theorem, [line 1013](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1013). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The defining property of purification, that tracing out the purifying system gives the
> original mixed state.

```lean
theorem purify_spec (ρ : MState d) : (pure ρ.purify).traceRight = ρ
```

**`MState.purifyX`**, a def, [line 1039](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1039).

> `MState.purify` bundled with its defining property `MState.traceRight_of_purify`.

```lean
def purifyX (ρ : MState d) : { ψ : Ket (d × d) // (pure ψ).traceRight = ρ }
```

**`MState.relabel`**, a def, [line 1045](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1045).

```lean
def relabel (ρ : MState d₁) (e : d₂ ≃ d₁) : MState d₂
```

**`MState.relabel_m`**, a lemma, [line 1051](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1051).

```lean
lemma relabel_m (ρ : MState d₁) (e : d₂ ≃ d₁) :
    (ρ.relabel e).m = ρ.m.submatrix e e
```

**`MState.relabel_refl`**, a lemma, [line 1056](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1056).

```lean
lemma relabel_refl {d : Type*} [Fintype d] [DecidableEq d] (ρ : MState d) :
    ρ.relabel (Equiv.refl d) = ρ
```

**`MState.relabel_pure`**, a lemma, [line 1064](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1064).

> Relabeling the pure state associated to a ket gives the pure state associated to the
> relabeled ket.

```lean
lemma relabel_pure (ψ : Ket d₁) (e : d₂ ≃ d₁) :
    (pure ψ).relabel e = pure (ψ.relabel e)
```

**`MState.relabel_pure_exists`**, a theorem, [line 1069](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1069). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Relabeling a pure state along an equivalence of basis index types yields another pure state.

```lean
theorem relabel_pure_exists (ψ : Ket d₁) (e : d₂ ≃ d₁) :
    ∃ ψ' : Ket d₂, (pure ψ).relabel e = pure ψ'
```

**`MState.relabel_relabel`**, a lemma, [line 1074](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1074).

```lean
lemma relabel_relabel {d d₂ d₃ : Type*}
    [Fintype d] [DecidableEq d] [Fintype d₂] [DecidableEq d₂] [Fintype d₃] [DecidableEq d₃]
    (ρ : MState d) (e : d₂ ≃ d) (e₂ : d₃ ≃ d₂) : (ρ.relabel e).relabel e₂ = ρ.relabel (e₂.trans e)
```

**`MState.eq_relabel_iff`**, a lemma, [line 1079](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1079).

```lean
lemma eq_relabel_iff {d₁ d₂ : Type u} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
    (ρ : MState d₁) (σ : MState d₂) (h : d₁ ≃ d₂) :
    ρ = σ.relabel h ↔ ρ.relabel h.symm = σ
```

**`MState.relabel_comp`**, a lemma, [line 1085](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1085).

```lean
lemma relabel_comp {d₁ d₂ d₃ : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
      [Fintype d₃] [DecidableEq d₃] (ρ : MState d₁) (e : d₂ ≃ d₁) (f : d₃ ≃ d₂) :
    (ρ.relabel e).relabel f = ρ.relabel (f.trans e)
```

**`MState.relabel_cast`**, a lemma, [line 1091](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1091).

```lean
lemma relabel_cast {d₁ d₂ : Type u} [Fintype d₁] [DecidableEq d₁]
    [Fintype d₂] [DecidableEq d₂]
       (ρ : MState d₁) (e : d₂ = d₁) :
    ρ.relabel (Equiv.cast e) = cast (by have := e.symm; congr <;> (apply Subsingleton.helim; congr)) ρ
```

**`MState.spectrum_relabel`**, a lemma, [line 1104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1104).

```lean
lemma spectrum_relabel {ρ : MState d} (e : d₂ ≃ d) :
    _root_.spectrum ℝ (ρ.relabel e).m = _root_.spectrum ℝ ρ.m
```

**`MState.purity_relabel`**, a theorem, [line 1117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1117). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The purity of a state is invariant under relabeling of the basis.

```lean
theorem purity_relabel (ρ : MState d₁) (e : d₂ ≃ d₁) : (ρ.relabel e).purity = ρ.purity
```

**`MState.SWAP`**, a def, [line 1125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1125).

> The heterogeneous SWAP gate that exchanges the left and right halves of a quantum system.
> This can apply even when the two "halves" are of different types, as opposed to (say) the SWAP
> gate on quantum circuits that leaves the qubit dimensions unchanged. Notably, it is not unitary.

```lean
def SWAP (ρ : MState (d₁ × d₂)) : MState (d₂ × d₁)
```

**`MState.multiset_spectrum_relabel_eq`**, a lemma, [line 1131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1131).

> The multiset of values in the spectrum of a relabeled state is the same as the multiset of values in the spectrum of the original state.

```lean
lemma multiset_spectrum_relabel_eq {d₁ d₂ : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
    (ρ : MState d₁) (e : d₂ ≃ d₁) :
    Multiset.map (ρ.relabel e).spectrum Finset.univ.val = Multiset.map ρ.spectrum Finset.univ.val
```

**`MState.spectrum_SWAP`**, a lemma, [line 1159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1159).

```lean
lemma spectrum_SWAP (ρ : MState (d₁ × d₂)) : ∃ e, ρ.SWAP.spectrum.relabel e = ρ.spectrum
```

**`MState.SWAP_SWAP`**, a lemma, [line 1169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1169).

```lean
lemma SWAP_SWAP (ρ : MState (d₁ × d₂)) : ρ.SWAP.SWAP = ρ
```

**`MState.traceLeft_SWAP`**, a lemma, [line 1173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1173).

```lean
lemma traceLeft_SWAP (ρ : MState (d₁ × d₂)) : ρ.SWAP.traceLeft = ρ.traceRight
```

**`MState.traceRight_SWAP`**, a lemma, [line 1177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1177).

```lean
lemma traceRight_SWAP (ρ : MState (d₁ × d₂)) : ρ.SWAP.traceRight = ρ.traceLeft
```

**`MState.assoc`**, a def, [line 1181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1181).

> The associator that re-clusters the parts of a quantum system.

```lean
def assoc (ρ : MState ((d₁ × d₂) × d₃)) : MState (d₁ × d₂ × d₃)
```

**`MState.assoc'`**, a def, [line 1185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1185).

> The associator that re-clusters the parts of a quantum system.

```lean
def assoc' (ρ : MState (d₁ × d₂ × d₃)) : MState ((d₁ × d₂) × d₃)
```

**`MState.assoc_assoc'`**, a lemma, [line 1189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1189).

```lean
lemma assoc_assoc' (ρ : MState (d₁ × d₂ × d₃)) : ρ.assoc'.assoc = ρ
```

**`MState.assoc'_assoc`**, a lemma, [line 1193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1193).

```lean
lemma assoc'_assoc (ρ : MState ((d₁ × d₂) × d₃)) : ρ.assoc.assoc' = ρ
```

**`MState.traceLeft_right_assoc`**, a lemma, [line 1197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1197).

```lean
lemma traceLeft_right_assoc (ρ : MState ((d₁ × d₂) × d₃)) :
    ρ.assoc.traceLeft.traceRight = ρ.traceRight.traceLeft
```

**`MState.traceRight_left_assoc'`**, a lemma, [line 1203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1203).

```lean
lemma traceRight_left_assoc' (ρ : MState (d₁ × d₂ × d₃)) :
    ρ.assoc'.traceRight.traceLeft = ρ.traceLeft.traceRight
```

**`MState.traceRight_assoc`**, a lemma, [line 1208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1208).

```lean
lemma traceRight_assoc (ρ : MState ((d₁ × d₂) × d₃)) :
    ρ.assoc.traceRight = ρ.traceRight.traceRight
```

**`MState.traceLeft_assoc'`**, a lemma, [line 1214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1214).

```lean
lemma traceLeft_assoc' (ρ : MState (d₁ × d₂ × d₃)) :
    ρ.assoc'.traceLeft = ρ.traceLeft.traceLeft
```

**`MState.traceLeft_left_assoc`**, a lemma, [line 1220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1220).

```lean
lemma traceLeft_left_assoc (ρ : MState ((d₁ × d₂) × d₃)) :
    ρ.assoc.traceLeft.traceLeft = ρ.traceLeft
```

**`MState.traceRight_right_assoc'`**, a lemma, [line 1225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1225).

```lean
lemma traceRight_right_assoc' (ρ : MState (d₁ × d₂ × d₃)) :
    ρ.assoc'.traceRight.traceRight = ρ.traceRight
```

**`MState.traceNorm_eq_one`**, a lemma, [line 1230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1230).

```lean
lemma traceNorm_eq_one (ρ : MState d) : ρ.m.traceNorm = 1
```

**`MState.relabel_kron`**, a lemma, [line 1238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1238).

```lean
lemma relabel_kron (ρ : MState d₁) (σ : MState d₂) (e : d₃ ≃ d₁) :
    ((ρ.relabel e) ⊗ᴹ σ) = (ρ ⊗ᴹ σ).relabel (e.prodCongr (Equiv.refl d₂))
```

**`MState.kron_relabel`**, a lemma, [line 1242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1242).

```lean
lemma kron_relabel (ρ : MState d₁) (σ : MState d₂) (e : d₃ ≃ d₂) :
    (ρ ⊗ᴹ σ.relabel e) = (ρ ⊗ᴹ σ).relabel ((Equiv.refl d₁).prodCongr e)
```

**`MState.prod_assoc`**, a lemma, [line 1246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1246).

```lean
lemma prod_assoc (ρ : MState d₁) (σ : MState d₂) (τ : MState d₃) :
    (ρ ⊗ᴹ (σ ⊗ᴹ τ)) = (ρ ⊗ᴹ σ ⊗ᴹ τ).relabel (Equiv.prodAssoc d₁ d₂ d₃).symm
```

**An instance with no name**, [line 1255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1255).

> Mixed states inherit the subspace topology from matrices

```lean
instance : TopologicalSpace (MState d)
```

**`MState.toMat_IsEmbedding`**, a theorem, [line 1259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1259). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The projection from mixed states to their Hermitian matrices is an embedding

```lean
theorem toMat_IsEmbedding : Topology.IsEmbedding (MState.M (d := d))
```

**An instance with no name**, [line 1263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1263).

```lean
instance : T3Space (MState d)
```

**An instance with no name**, [line 1266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1266).

```lean
instance : CompactSpace (MState d)
```

**An instance with no name**, [line 1281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1281).

```lean
noncomputable instance : MetricSpace (MState d)
```

**`MState.dist_eq`**, a lemma, [line 1284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1284).

```lean
lemma dist_eq (x y : MState d) : dist x y = dist x.M y.M
```

**An instance with no name**, [line 1288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1288).

```lean
instance : BoundedSpace (MState d)
```

**`MState.Continuous_HermitianMat`**, a lemma, [line 1293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1293).

```lean
lemma Continuous_HermitianMat : Continuous (MState.M (d := d))
```

**`MState.Continuous_Matrix`**, a lemma, [line 1297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1297).

```lean
lemma Continuous_Matrix : Continuous (MState.m (d := d))
```

**`MState.image_M_isBounded`**, a lemma, [line 1301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1301).

```lean
lemma image_M_isBounded (S : Set (MState d)) : Bornology.IsBounded (MState.M '' S)
```

**`MState.piProd`**, a def, [line 1313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1313).

```lean
def piProd (ρi : (i:ι) → MState (dI i)) : MState ((i:ι) → dI i)
```

**`MState.pure_piProd`**, a lemma, [line 1325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1325).

> The pure state of `Ket.piProd ψ` is `MState.piProd` of the pure states `pure (ψ i)`,
> generalizing `MState.pure_prod_pure`.

```lean
lemma pure_piProd (ψ : (i : ι) → Ket (dI i)) :
    pure (Ket.piProd ψ) = piProd (fun i ↦ pure (ψ i))
```

**`MState.isPiProd_iff_exists_pure_eq_piProd`**, a lemma, [line 1332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1332).

> With at least one party, a ket satisfies `Ket.IsPiProd` if and only if its associated
> pure state `MState.pure ψ` is an `MState.piProd` of pure states.

```lean
lemma isPiProd_iff_exists_pure_eq_piProd [Nonempty ι] (ψ : Ket ((i : ι) → dI i)) :
    ψ.IsPiProd ↔ ∃ φ : (i : ι) → Ket (dI i), pure ψ = piProd (fun i ↦ pure (φ i))
```

**`MState.isPiProd_iff_exists_pureQ_eq_piProd`**, a lemma, [line 1343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1343).

> A ket up to global phase is a product state if and only if its density matrix is an
> `MState.piProd` of pure states. This also holds when `ι` is empty.

```lean
lemma isPiProd_iff_exists_pureQ_eq_piProd (q : KetUpToPhase ((i : ι) → dI i)) :
    q.IsPiProd ↔ ∃ φ : (i : ι) → Ket (dI i), pureQ q = piProd (fun i ↦ pure (φ i))
```

**`MState.npow`**, a def, [line 1353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1353).

> The n-copy "power" of a mixed state, with the standard basis indexed by pi types.

```lean
def npow (ρ : MState d) (n : ℕ) : MState (Fin n → d)
```

**`MState.PosDef.kron`**, a lemma, [line 1363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1363).

```lean
lemma PosDef.kron {d₁ d₂ : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
    {σ₁ : MState d₁} {σ₂ : MState d₂} (hσ₁ : σ₁.m.PosDef) (hσ₂ : σ₂.m.PosDef) : (σ₁ ⊗ᴹ σ₂).m.PosDef
```

**`MState.PosDef.relabel`**, a lemma, [line 1367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1367).

```lean
lemma PosDef.relabel {d₁ d₂ : Type*} [Fintype d₁] [DecidableEq d₁] [Fintype d₂] [DecidableEq d₂]
    {ρ : MState d₁} (hρ : ρ.m.PosDef) (e : d₂ ≃ d₁) : (ρ.relabel e).m.PosDef
```

**`MState.PosDef_mix`**, a theorem, [line 1372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1372). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If both states positive definite, so is their mixture.

```lean
theorem PosDef_mix {d : Type*} [Fintype d] [DecidableEq d] {σ₁ σ₂ : MState d}
    (hσ₁ : σ₁.m.PosDef) (hσ₂ : σ₂.m.PosDef) (p : Prob) : (p [σ₁ ↔ σ₂]).m.PosDef
```

**`MState.PosDef_mix_of_ne_zero`**, a theorem, [line 1377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1377). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If one state is positive definite and the mixture is nondegenerate, their mixture is also positive definite.

```lean
theorem PosDef_mix_of_ne_zero {d : Type*} [Fintype d] [DecidableEq d] {σ₁ σ₂ : MState d}
    (hσ₁ : σ₁.m.PosDef) (p : Prob) (hp : p ≠ 0) : (p [σ₁ ↔ σ₂]).m.PosDef
```

**`MState.PosDef_mix_of_ne_one`**, a theorem, [line 1383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1383). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If the second state is positive definite and the mixture is nondegenerate, their mixture is also positive definite.

```lean
theorem PosDef_mix_of_ne_one {d : Type*} [Fintype d] [DecidableEq d] {σ₁ σ₂ : MState d}
    (hσ₂ : σ₂.m.PosDef) (p : Prob) (hp : p ≠ 1) : (p [σ₁ ↔ σ₂]).m.PosDef
```

**`MState.uniform_posDef`**, a lemma, [line 1397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1397).

```lean
lemma uniform_posDef {d : Type*} [Nonempty d] [Fintype d] [DecidableEq d] :
    (uniform (d := d)).m.PosDef
```

**`MState.posDef_of_unique`**, a lemma, [line 1402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean#L1402).

```lean
lemma posDef_of_unique {d : Type*} [Fintype d] [DecidableEq d] (ρ : MState d) [Unique d] : ρ.m.PosDef
```

## Depends on

- [Distributions on finite sets](../../classicalinfo/distribution.md)
- [Matrix Powers With Real Exponents](../../formathlib/hermitianmat/rpow.md)
- [QuantumInfo.ForMathlib.MatrixNorm.TraceNorm](../../formathlib/matrixnorm/tracenorm.md)
- [QuantumInfo.States.Pure.Braket](../pure/braket.md)

## Sources

- [QuantumInfo/States/Mixed/MState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Mixed/MState.lean)
