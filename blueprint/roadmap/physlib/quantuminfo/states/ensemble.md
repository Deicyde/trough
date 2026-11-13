---
declaration: module
origin: cited
lean: Ensemble.coe_PEnsemble_iff_pure_states, Ensemble.mix_congrMEnsemble_eq_mix, Ensemble.mix_congrPEnsemble_eq_mix, Ensemble.average_of_pure_ensemble, Ensemble.mix_pEnsemble_pure_average, Ensemble.mix_mEnsemble_pure_average, Ensemble.trivial_mEnsemble_mix, Ensemble.trivial_mEnsemble_average
statement: formalized
proof: formalized
---

# QuantumInfo.States.Ensemble

The module `QuantumInfo.States.Ensemble`, [QuantumInfo/States/Ensemble.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean): 38 declarations (1 instance with no name), 27 with a docstring, 11 listed as significant.

**`MEnsemble`**, an abbrev, [line 21](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L21).

> A mixed-state ensemble is a random variable valued in `MState d`. That is,
> a collection of mixed states `var : α → MState d`, each with their own probability weight
> described by `distr : ProbDistribution α`.

```lean
abbrev MEnsemble (d : Type*) (α : Type*) [Fintype d] [DecidableEq d] [Fintype α]
```

**`PEnsemble`**, an abbrev, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L26).

> A pure-state ensemble is a random variable valued in `Ket d`. That is,
> a collection of pure states `var : α → Ket d`, each with their own probability weight
> described by `distr : ProbDistribution α`.

```lean
abbrev PEnsemble (d : Type*) (α : Type*) [Fintype d] [Fintype α]
```

**`MEnsemble.states`**, an abbrev, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L31).

> Alias for `ProbDistribution.var` for mixed-state ensembles.

```lean
abbrev MEnsemble.states : MEnsemble d α → (α → MState d)
```

**`PEnsemble.states`**, an abbrev, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L34).

> Alias for `ProbDistribution.var` for pure-state ensembles.

```lean
abbrev PEnsemble.states : PEnsemble d α → (α → Ket d)
```

**`Ensemble.toMEnsemble`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L39).

> A pure-state ensemble is a mixed-state ensemble if all kets are interpreted as mixed states.

```lean
def toMEnsemble : PEnsemble d α → MEnsemble d α
```

**An instance with no name**, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L41).

```lean
instance : Coe (PEnsemble d α) (MEnsemble d α)
```

**`Ensemble.toMEnsemble_mk`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L44).

```lean
lemma toMEnsemble_mk : (toMEnsemble ⟨ps, distr⟩ : MEnsemble d α) = ⟨pure ∘ ps, distr⟩
```

**`Ensemble.coe_PEnsemble_iff_pure_states`**, a theorem, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L48). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A mixed-state ensemble comes from a pure-state ensemble if and only if all states are pure.

```lean
theorem coe_PEnsemble_iff_pure_states (me : MEnsemble d α): (∃ pe : PEnsemble d α, ↑pe = me) ↔ (∃ ψ : α → Ket d, me.states = MState.pure ∘ ψ)
```

**`Ensemble.mix`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L64).

> The resulting mixed state after mixing the states in an ensemble with their
> respective probability weights. Note that, generically, a single mixed state has infinitely many
> ensembles that mixes into it.

```lean
def mix (e : MEnsemble d α) : MState d
```

**`Ensemble.mix_of`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L67).

```lean
lemma mix_of (e : MEnsemble d α) : (mix e).m = ∑ i, (e.distr i : ℝ) • (e.states i).m
```

**`Ensemble.congrMEnsemble`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L71).

> Two mixed-state ensembles indexed by `\alpha` and `\beta` are equivalent if `α ≃ β`.

```lean
def congrMEnsemble (σ : α ≃ β) : MEnsemble d α ≃ MEnsemble d β
```

**`Ensemble.congrPEnsemble`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L74).

> Two pure-state ensembles indexed by `\alpha` and `\beta` are equivalent if `α ≃ β`.

```lean
def congrPEnsemble (σ : α ≃ β) : PEnsemble d α ≃ PEnsemble d β
```

**`Ensemble.mix_congrMEnsemble_eq_mix`**, a theorem, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L78). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Equivalence of mixed-state ensembles leaves the resulting mixed state invariant

```lean
theorem mix_congrMEnsemble_eq_mix (σ : α ≃ β) (e : MEnsemble d α) : mix (congrMEnsemble σ e) = mix e
```

**`Ensemble.mix_congrPEnsemble_eq_mix`**, a theorem, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L83). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Equivalence of pure-state ensembles leaves the resulting mixed state invariant

```lean
theorem mix_congrPEnsemble_eq_mix (σ : α ≃ β) (e : PEnsemble d α) : mix (toMEnsemble (congrPEnsemble σ e)) = mix (↑e : MEnsemble d α)
```

**`Ensemble.average`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L90).

> The average of a function `f : MState d → T`, where `T` is of `Mixable U T` instance, on a mixed-state ensemble `e`
> is the expectation value of `f` acting on the states of `e`, with the corresponding probability weights from `e.distr`.

```lean
def average {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U] [inst : Mixable U T] (f : MState d → T) (e : MEnsemble d α) : T
```

**`Ensemble.average_NNReal`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L95).

> A version of `average` conveniently specialized for functions `f : MState d → ℝ≥0` returning nonnegative reals.
> Notably, the average is also a nonnegative real number.

```lean
def average_NNReal {d : Type _} [Fintype d] [DecidableEq d] (f : MState d → NNReal) (e : MEnsemble d α) : NNReal
```

**`Ensemble.pure_average`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L101).

> The average of a function `f : Ket d → T`, where `T` is of `Mixable U T` instance, on a pure-state ensemble `e`
> is the expectation value of `f` acting on the states of `e`, with the corresponding probability weights from `e.distr`.

```lean
def pure_average {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U] [inst : Mixable U T] (f : Ket d → T) (e : PEnsemble d α) : T
```

**`Ensemble.pure_average_NNReal`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L106).

> A version of `average` conveniently specialized for functions `f : Ket d → ℝ≥0` returning nonnegative reals.
> Notably, the average is also a nonnegative real number.

```lean
def pure_average_NNReal {d : Type _} [Fintype d] (f : Ket d → NNReal) (e : PEnsemble d α) : NNReal
```

**`Ensemble.average_of_pure_ensemble`**, a theorem, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L112). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The average of `f : MState d → T` on a coerced pure-state ensemble `↑e : MEnsemble d α`
> is equal to averaging the restricted function over Kets `f ∘ pure : Ket d → T` on `e`.

```lean
theorem average_of_pure_ensemble {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U] [inst : Mixable U T]
  (f : MState d → T) (e : PEnsemble d α) :
  average f (toMEnsemble e) = pure_average (f ∘ pure) e
```

**`Ensemble.distr_toMEnsemble`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L120).

```lean
lemma distr_toMEnsemble (e : PEnsemble d α) : (toMEnsemble e).distr = e.distr
```

**`Ensemble.mix_pEnsemble_pure_iff_pure`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L128).

```lean
lemma mix_pEnsemble_pure_iff_pure {e : PEnsemble d α} :
    mix (toMEnsemble e) = MState.pure ψ ↔
    ∀ i : α, e.distr i ≠ 0 → MState.pure (e.states i) = MState.pure ψ
```

**`Ensemble.mix_pEnsemble_pure_average`**, a theorem, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L149). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The average of `f : Ket d → T` on an ensemble that mixes to a pure state `ψ` is `f ψ`

```lean
theorem mix_pEnsemble_pure_average {e : PEnsemble d α} {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U]
    [inst : Mixable U T] (f : Ket d → T) (hf : ∀ ψ φ, Ket.PhaseEquiv.r ψ φ → f ψ = f φ)
    (hmix : mix (toMEnsemble e) = MState.pure ψ) :
  pure_average f e = f ψ
```

**`Ensemble.sum_prob_mul_eq_one_iff`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L169).

```lean
lemma sum_prob_mul_eq_one_iff {ι : Type*} [Fintype ι] (p : ι → ℝ) (x : ι → ℝ)
    (hp : ∀ i, 0 ≤ p i) (hsum : ∑ i, p i = 1) (hx : ∀ i, x i ≤ 1) :
    (∑ i, p i * x i = 1) ↔ ∀ i, p i ≠ 0 → x i = 1
```

**`Ensemble.MState.exp_val_pure_eq_one_iff`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L190).

```lean
lemma MState.exp_val_pure_eq_one_iff {d : Type*} [Fintype d] [DecidableEq d]
    (ρ : MState d) (ψ : Ket d) :
    ρ.exp_val (pure ψ) = 1 ↔ ρ = pure ψ
```

**`Ensemble.mix_mEnsemble_pure_iff_pure`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L212).

```lean
lemma mix_mEnsemble_pure_iff_pure {e : MEnsemble d α} :
    mix e = pure ψ ↔ ∀ i : α, e.distr i ≠ 0 → e.states i = MState.pure ψ
```

**`Ensemble.mix_mEnsemble_pure_average`**, a theorem, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L225). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The average of `f : MState d → T` on an ensemble that mixes to a pure state `ψ` is `f (pure ψ)`

```lean
theorem mix_mEnsemble_pure_average {e : MEnsemble d α} {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U] [inst : Mixable U T] (f : MState d → T) (hmix : mix e = pure ψ) :
  average f e = f (pure ψ)
```

**`Ensemble.trivial_mEnsemble`**, a def, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L255).

> The trivial mixed-state ensemble of `ρ` consists of copies of `rho`, with the `i`-th one having
> probability 1.

```lean
def trivial_mEnsemble (ρ : MState d) (i : α) : MEnsemble d α
```

**`Ensemble.trivial_mEnsemble_mix`**, a theorem, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L258). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trivial mixed-state ensemble of `ρ` mixes to `ρ`

```lean
theorem trivial_mEnsemble_mix (ρ : MState d) : ∀ i : α, mix (trivial_mEnsemble ρ i) = ρ
```

**`Ensemble.trivial_mEnsemble_average`**, a theorem, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L266). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The average of `f : MState d → T` on a trivial ensemble of `ρ` is `f ρ`

```lean
theorem trivial_mEnsemble_average {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U] [inst : Mixable U T] (f : MState d → T) (ρ : MState d):
  ∀ i : α, average f (trivial_mEnsemble ρ i) = f ρ
```

**`Ensemble.MEnsemble.instInhabited`**, an instance, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L272).

```lean
instance MEnsemble.instInhabited [Nonempty d] [Inhabited α] : Inhabited (MEnsemble d α)
```

**`Ensemble.trivial_pEnsemble`**, a def, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L277).

> The trivial pure-state ensemble of `ψ` consists of copies of `ψ`, with the `i`-th one having
> probability 1.

```lean
def trivial_pEnsemble (ψ : Ket d) (i : α) : PEnsemble d α
```

**`Ensemble.trivial_pEnsemble_mix`**, a theorem, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L283). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The trivial pure-state ensemble of `ψ` mixes to `ψ`

```lean
theorem trivial_pEnsemble_mix : ∀ i : α, mix (toMEnsemble (trivial_pEnsemble ψ i)) = MState.pure ψ
```

**`Ensemble.trivial_pEnsemble_average`**, a theorem, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L292). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The average of `f : Ket d → T` on a trivial ensemble of `ψ` is `f ψ`

```lean
theorem trivial_pEnsemble_average {T : Type _} {U : Type*} [AddCommGroup U] [Module ℝ U] [inst : Mixable U T] (f : Ket d → T) :
  ∀ i : α, pure_average f (trivial_pEnsemble ψ i) = f ψ
```

**`Ensemble.PEnsemble.instInhabited`**, an instance, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L298).

```lean
instance PEnsemble.instInhabited [Nonempty d] [Inhabited α] : Inhabited (PEnsemble d α)
```

**`Ensemble.spectral_ensemble`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L302).

> The spectral pure-state ensemble of `ρ`. The states are its eigenvectors, and the probabilities, eigenvalues.

```lean
def spectral_ensemble (ρ : MState d) : PEnsemble d d
```

**`Ensemble.spectral_decomposition_sum`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L315).

```lean
lemma spectral_decomposition_sum {d 𝕜 : Type*} [Fintype d] [DecidableEq d] [RCLike 𝕜]
    {A : Matrix d d 𝕜} (hA : A.IsHermitian) :
    A = ∑ i, (hA.eigenvalues i) • (Matrix.vecMulVec (hA.eigenvectorBasis i) (star (hA.eigenvectorBasis i)))
```

**`Ensemble.spectral_ensemble_mix`**, a theorem, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L329). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The spectral pure-state ensemble of `ρ` mixes to `ρ`

```lean
theorem spectral_ensemble_mix {ρ : MState d} : mix (↑(spectral_ensemble ρ) : MEnsemble d d) = ρ
```

**`MState.IsSeparable.exists_pEnsemble_isProd`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean#L348).

> Every separable bipartite mixed state is a mixture of finitely many
> pure product states. The ensemble is indexed by `Fin n` for some `n > 0`.

```lean
lemma MState.IsSeparable.exists_pEnsemble_isProd {ρ : MState (d₁ × d₂)}
    (hρ : ρ.IsSeparable) :
    ∃ (n : ℕ) (e : PEnsemble (d₁ × d₂) (Fin n)), 0 < n ∧ mix (toMEnsemble e) = ρ ∧
      ∀ i, (e.states i).IsProd
```

## Depends on

- [QuantumInfo.States.Mixed.MState](mixed/mstate.md)

## Sources

- [QuantumInfo/States/Ensemble.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Ensemble.lean)
