---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.inner_energyFluctuation_maxCurrentState, CondensedMatter.TightBindingChain.inner_positionFluctuation_maxCurrentState, CondensedMatter.TightBindingChain.centeredGramDefect_maxCurrentState_eq_zero_iff, CondensedMatter.TightBindingChain.robertson_schrodinger_maxCurrentState_eq_iff, CondensedMatter.TightBindingChain.robertson_schrodinger_maxCurrentState_lt
statement: formalized
proof: formalized
---

# Saturation of the uncertainty relation in the maximal current state

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.MaxCurrentState.Saturation`, [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean): 5 declarations, 5 with a docstring; 1 private, not shown.

## i. Overview

> The energy–position uncertainty relation is an equality exactly when the centered Gram defect
> vanishes, that is when the energy and position fluctuations of the state are parallel. In the
> maximal current state of an open chain with `N ≥ 2` sites and hopping `t ≠ 0` this happens only
> for `N = 2` and `N = 3`: the first two sites force `4 cos² (π / (N + 1)) = N - 1`. From four
> sites on, the relation is strict.

## ii. Key results

> - `inner_energyFluctuation_maxCurrentState` : the energy fluctuation, site by site.
> - `inner_positionFluctuation_maxCurrentState` : the position fluctuation, site by site.
> - `centeredGramDefect_maxCurrentState_eq_zero_iff` : the defect vanishes iff `N = 2, 3`.
> - `robertson_schrodinger_maxCurrentState_eq_iff` : the relation is an equality iff `N = 2, 3`.
> - `robertson_schrodinger_maxCurrentState_lt` : the relation is strict for `N ≥ 4`.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The fluctuations

**`CondensedMatter.TightBindingChain.inner_energyFluctuation_maxCurrentState`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean#L55).

> The energy fluctuation of the maximal current state, site by site.

```lean
lemma inner_energyFluctuation_maxCurrentState (m : Fin T.N) :
    ⟪|m⟩, (T.openHamiltonianObservable : T.HilbertSpace →L[ℂ] T.HilbertSpace) T.maxCurrentState -
      T.maxCurrentVectorState⟨T.openHamiltonianObservable⟩ • T.maxCurrentState⟫_ℂ =
      -((√(2 / (T.N + 1)) : ℝ) * (2 * T.t * Real.sin (Real.pi / (T.N + 1)) *
        Complex.I ^ ((m : ℕ) + 1) * Real.cos (((m : ℕ) + 1) * (Real.pi / (T.N + 1))))) := by
  rw [expectation_openHamiltonian_maxCurrentState, inner_sub_right, ← Complex.coe_smul,
    inner_smul_right]
  change ⟪|m⟩, T.openHamiltonian T.maxCurrentState⟫_ℂ - _ = _
  rw [inner_openHamiltonian_maxCurrentState]
  ring
```

**`CondensedMatter.TightBindingChain.inner_positionFluctuation_maxCurrentState`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean#L67).

> The position fluctuation of the maximal current state, site by site.

```lean
lemma inner_positionFluctuation_maxCurrentState (m : Fin T.N) :
    ⟪|m⟩, (T.positionObservable : T.HilbertSpace →L[ℂ] T.HilbertSpace) T.maxCurrentState -
      T.maxCurrentVectorState⟨T.positionObservable⟩ • T.maxCurrentState⟫_ℂ =
      (T.a * ((m : ℕ) - (T.N - 1) / 2) : ℝ) * ⟪|m⟩, T.maxCurrentState⟫_ℂ := by
  rw [expectation_position_maxCurrentState, inner_sub_right, ← Complex.coe_smul,
    inner_smul_right]
  change ⟪|m⟩, T.position T.maxCurrentState⟫_ℂ - _ = _
  rw [← position_hermitian, position_apply_localizedState, inner_smul_left, Complex.conj_ofReal]
  push_cast
  ring
```

## B. Saturation

**`CondensedMatter.TightBindingChain.centeredGramDefect_maxCurrentState_eq_zero_iff`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean#L106).

> In the maximal current state of a chain with `N ≥ 2` sites and hopping `t ≠ 0`, the centered
> Gram defect of `H` and `X` vanishes exactly for `N = 2` and `N = 3`.

```lean
lemma centeredGramDefect_maxCurrentState_eq_zero_iff (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    centeredGramDefect T.maxCurrentVectorState T.openHamiltonianObservable
      T.positionObservable = 0 ↔ T.N = 2 ∨ T.N = 3
```

**`CondensedMatter.TightBindingChain.robertson_schrodinger_maxCurrentState_eq_iff`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean#L198).

> **Saturation.** In the maximal current state of a chain with `N ≥ 2` sites and hopping
> `t ≠ 0`, the energy–position uncertainty relation is an equality exactly for `N = 2, 3`.

```lean
lemma robertson_schrodinger_maxCurrentState_eq_iff (ht : T.t ≠ 0) (hN : 2 ≤ T.N) :
    covariance T.maxCurrentVectorState T.openHamiltonianObservable T.positionObservable ^ 2 +
        (T.a * T.t * Real.cos (Real.pi / (T.N + 1))) ^ 2 =
      variance T.maxCurrentVectorState T.openHamiltonianObservable *
        variance T.maxCurrentVectorState T.positionObservable ↔ T.N = 2 ∨ T.N = 3
```

**`CondensedMatter.TightBindingChain.robertson_schrodinger_maxCurrentState_lt`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean#L208).

> From four sites on, the uncertainty relation of the maximal current state is strict.

```lean
lemma robertson_schrodinger_maxCurrentState_lt (ht : T.t ≠ 0) (hN : 4 ≤ T.N) :
    covariance T.maxCurrentVectorState T.openHamiltonianObservable T.positionObservable ^ 2 +
        (T.a * T.t * Real.cos (Real.pi / (T.N + 1))) ^ 2 <
      variance T.maxCurrentVectorState T.openHamiltonianObservable *
        variance T.maxCurrentVectorState T.positionObservable
```

## Depends on

- [The maximal current state of the open tight binding chain](maxcurrentstate-basic.md)
- [Uncertainty relations](../../../probabilistictheory/cstaralgebra/uncertainty.md)

## Proof depends on

- [Uncertainty in vector states](../../../probabilistictheory/hilbertspace/part-01/state-vectoruncertainty.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/MaxCurrentState/Saturation.lean)
