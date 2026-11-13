---
declaration: module
origin: cited
lean: convex_roof_ne_top, mixed_convex_roof_ne_top, mixed_convex_roof_le_convex_roof, convex_roof_of_pure, mixed_convex_roof_of_pure, EoF_of_MES, convex_roof_ENNReal, mixed_convex_roof_ENNReal
statement: formalized
proof: formalized
---

# QuantumInfo.States.Entanglement

The module `QuantumInfo.States.Entanglement`, [QuantumInfo/States/Entanglement.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean): 22 declarations, 15 with a docstring, 6 listed as significant.

> Entanglement measures. (Mixed) convex roof extensions. Definition of product / separable / entangled states
> are in `Braket.lean` and/or `MState.lean`
>
> Important definitions:
>  * `convex_roof`: Convex roof extension of `g : KetUpToPhase d → ℝ≥0`
>  * `mixed_convex_roof`: Mixed convex roof extension of `f : MState d → ℝ≥0`
>  * `EoF`: Entanglement of Formation
>
> …

**`convex_roof_ENNReal`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L58).

> Convex roof extension of a function `g : KetUpToPhase d → ℝ≥0`, defined as the infimum of all pure-state
> ensembles of a given `ρ` of the average of `g` in that ensemble.
>
> This is valued in the extended nonnegative real numbers `ℝ≥0∞` to have good properties of the infimum, which
> come from the fact that `ℝ≥0∞` is a complete lattice. For example, it is necessary for `le_iInf` and `iInf_le_of_le`.
> However, it is also proven in `convex_roof_ne_top` that the convex roof is never `∞`, so the definition `convex_roof` should
> be used in most applications.

```lean
def convex_roof_ENNReal {d : Type _} [Fintype d] [DecidableEq d] (g : KetUpToPhase d → ℝ≥0) : MState d → ℝ≥0∞
```

**`mixed_convex_roof_ENNReal`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L68).

> Mixed convex roof extension of a function `f : MState d → ℝ≥0`, defined as the infimum of all mixed-state
> ensembles of a given `ρ` of the average of `f` on that ensemble.
>
> This is valued in the extended nonnegative real numbers `ℝ≥0∞` to have good properties of the infimum, which
> come from the fact that `ℝ≥0∞` is a complete lattice (see `ENNReal.instCompleteLinearOrder`). However,
> it is also proven in `mixed_convex_roof_ne_top` that the mixed convex roof is never `∞`, so the definition `mixed_convex_roof` should
> be used in most applications.

```lean
def mixed_convex_roof_ENNReal {d : Type _} [Fintype d] [DecidableEq d] (f : MState d → ℝ≥0) : MState d → ℝ≥0∞
```

**`convex_roof_ne_top`**, a theorem, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L78). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The convex roof extension `convex_roof_ENNReal` is never ∞.

```lean
theorem convex_roof_ne_top : ∀ ρ, convex_roof_ENNReal g ρ ≠ ∞
```

**`mixed_convex_roof_ne_top`**, a theorem, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L91). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The convex roof extension `mixed_convex_roof_ENNReal` is never ∞.

```lean
theorem mixed_convex_roof_ne_top : ∀ ρ, mixed_convex_roof_ENNReal f ρ ≠ ∞
```

**`convex_roof`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L102).

> Convex roof extension of a function `g : KetUpToPhase d → ℝ≥0`, defined as the infimum of all pure-state
> ensembles of a given `ρ` of the average of `g` in that ensemble.
>
> This is valued in the nonnegative real numbers `ℝ≥0` by applying `ENNReal.toNNReal` to `convex_roof_ENNReal`. Hence,
> it should be used in proofs alongside `convex_roof_ne_top`.

```lean
def convex_roof : MState d → ℝ≥0
```

**`mixed_convex_roof`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L109).

> Mixed convex roof extension of a function `f : MState d → ℝ≥0`, defined as the infimum of all mixed-state
> ensembles of a given `ρ` of the average of `f` on that ensemble.
>
> This is valued in the nonnegative real numbers `ℝ≥0` by applying `ENNReal.toNNReal` to `mixed_convex_roof_ENNReal`. Hence,
> it should be used in proofs alongside `mixed_convex_roof_ne_top`.

```lean
def mixed_convex_roof : MState d → ℝ≥0
```

**`convex_roof_of_MState_fun`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L113).

> Auxiliary function. Convex roof of a function `f : MState d → ℝ≥0` defined over mixed states by
> restricting `f` to pure states, via `pureQ : KetUpToPhase d → MState d`.

```lean
def convex_roof_of_MState_fun : MState d → ℝ≥0
```

**`le_mixed_convex_roof`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L119).

```lean
lemma le_mixed_convex_roof (ρ : MState d) :
  (∀ n > 0, ∀ e : MEnsemble d (Fin n), mix e = ρ → c ≤ average_NNReal f e) → (c ≤ mixed_convex_roof f ρ)
```

**`le_convex_roof`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L128).

```lean
lemma le_convex_roof (ρ : MState d) :
  (∀ n > 0, ∀ e : PEnsemble d (Fin n), mix (toMEnsemble e) = ρ → c ≤ pure_average_NNReal (g ∘ KetUpToPhase.mk) e) → (c ≤ convex_roof g ρ)
```

**`convex_roof_le`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L137).

```lean
lemma convex_roof_le (ρ : MState d):
(∃ n > 0, ∃ e : PEnsemble d (Fin n), mix (toMEnsemble e) = ρ ∧ pure_average_NNReal (g ∘ KetUpToPhase.mk) e ≤ c) → (convex_roof g ρ ≤ c)
```

**`mixed_convex_roof_le`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L148).

```lean
lemma mixed_convex_roof_le (ρ : MState d):
(∃ n > 0, ∃ e : MEnsemble d (Fin n), mix e = ρ ∧ average_NNReal f e ≤ c) → (mixed_convex_roof f ρ ≤ c)
```

**`mixed_convex_roof_le_convex_roof`**, a theorem, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L159). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The mixed convex roof extension of `f` is smaller than or equal to its convex roof extension, since
> the former minimizes over a larger set of ensembles.

```lean
theorem mixed_convex_roof_le_convex_roof : mixed_convex_roof f ≤ convex_roof_of_MState_fun f
```

**`convex_roof_of_pure`**, a theorem, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L172). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The convex roof extension of `g : KetUpToPhase d → ℝ≥0` applied to a pure state `ψ` is `g (KetUpToPhase.mk ψ)`.

```lean
theorem convex_roof_of_pure (ψ : Ket d) : convex_roof g (pure ψ) = g (KetUpToPhase.mk ψ)
```

**`mixed_convex_roof_of_pure`**, a theorem, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L200). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The mixed convex roof extension of `f : MState d → ℝ≥0` applied to a pure state `ψ` is `f (pure ψ)`.

```lean
theorem mixed_convex_roof_of_pure (ψ : Ket d) : mixed_convex_roof f (pure ψ) = f (pure ψ)
```

**`convex_roof_eq_zero_of_mix`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L224).

> If `g` vanishes on every state in a pure-state ensemble whose mixture is `ρ`,
> then `convex_roof g ρ = 0`.

```lean
lemma convex_roof_eq_zero_of_mix {n : ℕ} (hnpos : 0 < n) (e : PEnsemble d (Fin n))
    {ρ : MState d} (hmix : mix (toMEnsemble e) = ρ)
    (hg : ∀ i, g (KetUpToPhase.mk (e.states i)) = 0) :
    convex_roof g ρ = 0
```

**`convex_roof_eq_zero_of_isSeparable`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L236).

> The convex roof of a function that vanishes on pure product states
> vanishes on every separable state.

```lean
lemma convex_roof_eq_zero_of_isSeparable (g : KetUpToPhase (d₁ × d₂) → ℝ≥0)
    (hg : ∀ (ξ : Ket d₁) (η : Ket d₂), g (KetUpToPhase.mk (ξ ⊗ᵠ η)) = 0)
    {ρ : MState (d₁ × d₂)} (hρ : ρ.IsSeparable) :
    convex_roof g ρ = 0
```

**`EoF`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L251).

> Entanglement of Formation of bipartite systems. It is the convex roof extension of the
> von Neumann entropy of one of the subsystems (here chosen to be the left one, but see `Entropy.Sᵥₙ_of_partial_eq`).
>
> The function `Sᵥₙ ∘ traceRight ∘ pure` is phase-invariant because `pure` maps phase-equivalent kets to the
> same mixed state, so it descends to `KetUpToPhase` via `pureQ`.

```lean
def EoF : MState (d₁ × d₂) → ℝ≥0
```

**`traceRight_pure_MES`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L262).

```lean
lemma traceRight_pure_MES (d : Type*) [Fintype d] [DecidableEq d] [Nonempty d] :
    (MState.pure (Ket.MES d)).traceRight = MState.uniform
```

**`Sᵥₙ_eq_trace_cfc`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L288).

```lean
lemma Sᵥₙ_eq_trace_cfc {d : Type*} [Fintype d] [DecidableEq d] (ρ : MState d) :
    Sᵥₙ ρ = (HermitianMat.cfc ρ.M Real.negMulLog).trace
```

**`Sᵥₙ_ofClassical`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L307).

```lean
lemma Sᵥₙ_ofClassical {d : Type*} [Fintype d] [DecidableEq d] (dist : ProbDistribution d) :
    Sᵥₙ (MState.ofClassical dist) = Hₛ dist
```

**`EoF_of_MES`**, a theorem, [line 320](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L320). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The entanglement of formation of the maximally entangled state with on-site dimension 𝕕 is log(𝕕).

```lean
theorem EoF_of_MES : EoF (pure <| Ket.MES d) = Real.log (Finset.card Finset.univ (α := d))
```

**`EoF_eq_zero_of_isSeparable`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean#L330).

> The entanglement of formation vanishes on separable states.

```lean
lemma EoF_eq_zero_of_isSeparable {ρ : MState (d₁ × d₂)} (hρ : ρ.IsSeparable) : EoF ρ = 0
```

## Depends on

- [QuantumInfo.Entropy.VonNeumann](../entropy/vonneumann.md)
- [QuantumInfo.States.Ensemble](ensemble.md)

## Sources

- [QuantumInfo/States/Entanglement.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Entanglement.lean)
