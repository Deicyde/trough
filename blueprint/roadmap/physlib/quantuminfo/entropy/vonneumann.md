---
declaration: module
origin: cited
lean: Sᵥₙ_nonneg, Sᵥₙ_le_log_d, Sᵥₙ_of_pure_zero, Sᵥₙ_eq_trace_cfc_negMulLog, Sᵥₙ_relabel, Sᵥₙ_of_SWAP_eq, Sᵥₙ_of_assoc_eq, Sᵥₙ_of_assoc'_eq
statement: formalized
proof: formalized
---

# QuantumInfo.Entropy.VonNeumann

The module `QuantumInfo.Entropy.VonNeumann`, [QuantumInfo/Entropy/VonNeumann.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean): 24 declarations, 18 with a docstring, 12 listed as significant; 10 private, not shown.

> Quantum notions of information and entropy.
>
> We start with quantities of \_entropy\_, namely the von Neumann entropy and its derived quantities:
>  * Quantum conditional entropy, `qConditionalEnt`
>  * Quantum mutual information, `qMutualInfo`
>  * Coherent information, `coherentInfo`
>  * Quantum conditional mutual information, `qcmi`.
> and then prove facts about them.

**`Sᵥₙ`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L72).

> Von Neumann entropy of a mixed state.

```lean
def Sᵥₙ (ρ : MState d) : ℝ
```

**`qConditionalEnt`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L76).

> The Quantum Conditional Entropy S(ρᴬ|ρᴮ) is given by S(ρᴬᴮ) - S(ρᴮ).

```lean
def qConditionalEnt (ρ : MState (dA × dB)) : ℝ
```

**`qMutualInfo`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L80).

> The Quantum Mutual Information I(A:B) is given by S(ρᴬ) + S(ρᴮ) - S(ρᴬᴮ).

```lean
def qMutualInfo (ρ : MState (dA × dB)) : ℝ
```

**`coherentInfo`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L85).

> The Coherent Information of a state ρ passing through a channel Λ is the negative conditional
> entropy of the image under Λ of the purification of ρ.

```lean
def coherentInfo (ρ : MState d₁) (Λ : CPTPMap d₁ d₂) : ℝ
```

**`qcmi`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L91).

> The Quantum Conditional Mutual Information, I(A;C|B) = S(A|B) - S(A|BC).

```lean
def qcmi (ρ : MState (dA × dB × dC)) : ℝ
```

**`Sᵥₙ_nonneg`**, a theorem, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L95). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> von Neumman entropy is nonnegative.

```lean
theorem Sᵥₙ_nonneg (ρ : MState d) : 0 ≤ Sᵥₙ ρ
```

**`Sᵥₙ_le_log_d`**, a theorem, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L99). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> von Neumman entropy is at most log d.

```lean
theorem Sᵥₙ_le_log_d (ρ : MState d) : Sᵥₙ ρ ≤ Real.log (Finset.card Finset.univ (α := d))
```

**`Sᵥₙ_of_pure_zero`**, a theorem, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L104). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> von Neumman entropy of pure states is zero.

```lean
theorem Sᵥₙ_of_pure_zero (ψ : Ket d) : Sᵥₙ (MState.pure ψ) = 0
```

**`Sᵥₙ_eq_neg_trace_log`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L108).

```lean
lemma Sᵥₙ_eq_neg_trace_log (ρ : MState d) : Sᵥₙ ρ = -⟪ρ.M.log, ρ.M⟫
```

**`Sᵥₙ_eq_trace_cfc_negMulLog`**, a theorem, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L123). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Von Neumann entropy is the trace of the matrix function `x ↦ -x log x`.

```lean
theorem Sᵥₙ_eq_trace_cfc_negMulLog (ρ : MState d) :
    Sᵥₙ ρ = (ρ.M.cfc Real.negMulLog).trace
```

**`Sᵥₙ_unit_zero`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L135).

```lean
lemma Sᵥₙ_unit_zero [Unique d] (ρ : MState d) : Sᵥₙ ρ = 0
```

**`Sᵥₙ_relabel`**, a theorem, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L141). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Von Neumann entropy is invariant under relabeling of the basis.

```lean
theorem Sᵥₙ_relabel (ρ : MState d₁) (e : d₂ ≃ d₁) :
    Sᵥₙ (ρ.relabel e) = Sᵥₙ ρ
```

**`Sᵥₙ_of_SWAP_eq`**, a theorem, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L147). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

```lean
theorem Sᵥₙ_of_SWAP_eq (ρ : MState (d₁ × d₂)) : Sᵥₙ ρ.SWAP = Sᵥₙ ρ
```

**`Sᵥₙ_of_assoc_eq`**, a theorem, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L153). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Von Neumann entropy is unchanged under assoc.

```lean
theorem Sᵥₙ_of_assoc_eq (ρ : MState ((d₁ × d₂) × d₃)) : Sᵥₙ ρ.assoc = Sᵥₙ ρ
```

**`Sᵥₙ_of_assoc'_eq`**, a theorem, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L159). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Von Neumann entropy is unchanged under assoc'.

```lean
theorem Sᵥₙ_of_assoc'_eq (ρ : MState (d₁ × (d₂ × d₃))) : Sᵥₙ ρ.assoc' = Sᵥₙ ρ
```

**`selfAdjointMap_Continuous`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L163).

```lean
lemma selfAdjointMap_Continuous {𝕜 : Type*} [RCLike 𝕜] :
    Continuous (IsMaximalSelfAdjoint.selfadjMap : 𝕜 →+ ℝ)
```

**`HermitianMat.trace_Continuous`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L169).

```lean
lemma HermitianMat.trace_Continuous {d 𝕜 : Type*} [Fintype d] [RCLike 𝕜]  :
    Continuous (HermitianMat.trace : HermitianMat d 𝕜 → ℝ)
```

**`Sᵥₙ_continuous`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L175).

```lean
lemma Sᵥₙ_continuous : Continuous (Sᵥₙ (d := d))
```

**`vecToMat`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L185).

> Convert a vector on a product space to a matrix.

```lean
def vecToMat {d₁ d₂ : Type*} [Fintype d₁] [Fintype d₂] (v : d₁ × d₂ → ℂ) : Matrix d₁ d₂ ℂ
```

**`traceLeft_eq_transpose_mul_conj`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L200).

```lean
lemma traceLeft_eq_transpose_mul_conj (ψ : Ket (d₁ × d₂)) :
    (MState.pure ψ).traceLeft.M.val = (vecToMat ψ.vec).transpose * (vecToMat ψ.vec).map star
```

**`Sᵥₙ_of_partial_eq`**, a theorem, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L316). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> von Neumman entropies of the left- and right- partial trace of pure states are equal.

```lean
theorem Sᵥₙ_of_partial_eq (ψ : Ket (d₁ × d₂)) :
    Sᵥₙ (MState.pure ψ).traceLeft = Sᵥₙ (MState.pure ψ).traceRight
```

**`qConditionalEnt_of_pure_symm`**, a theorem, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L325). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Quantum conditional entropy is symmetric for pure states.

```lean
theorem qConditionalEnt_of_pure_symm (ψ : Ket (d₁ × d₂)) :
    qConditionalEnt (MState.pure ψ).SWAP = qConditionalEnt (MState.pure ψ)
```

**`qMutualInfo_symm`**, a theorem, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L331). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Quantum mutual information is symmetric.

```lean
theorem qMutualInfo_symm (ρ : MState (d₁ × d₂)) :
    qMutualInfo ρ.SWAP = qMutualInfo ρ
```

**`Sᵥₙ_pure_complement`**, a theorem, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean#L338). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For a pure state, the entropy of one subsystem equals the entropy of its complement,
> even after relabeling.

```lean
theorem Sᵥₙ_pure_complement (ψ : Ket d₁) (e : d₂ × d₃ ≃ d₁) :
    Sᵥₙ ((MState.pure ψ).relabel e).traceLeft = Sᵥₙ ((MState.pure ψ).relabel e).traceRight
```

## Depends on

- [Completely Positive Trace Preserving maps](../channels/cptp.md)
- [Shannon entropy](../classicalinfo/entropy.md)
- [Properties of the matrix logarithm and exponential](../formathlib/hermitianmat/logexp.md)

## Sources

- [QuantumInfo/Entropy/VonNeumann.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Entropy/VonNeumann.lean)
