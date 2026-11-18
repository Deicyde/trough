---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.wigner3j_cycle, PhyslibAlpha.Sl2.sum_sq_cgCoefficient_initial
statement: formalized
proof: formalized
---

# A sum rule for multipole transitions

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.MultipoleSumRule`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/MultipoleSumRule.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/MultipoleSumRule.lean): 2 declarations, 2 with a docstring.

> `Σ_{μ M_f} ⟨J_i M_i λ μ | J_f M_f⟩² = (2J_f + 1) / (2J_i + 1)`, independent of `M_i`.

## i. Overview

> A multipole operator `T^λ_μ` of rank `λ` connects an initial level `J_i` with a final level
> `J_f`. By the Wigner–Eckart theorem its matrix elements are
> `⟨J_f M_f | T^λ_μ | J_i M_i⟩ = ⟨J_i M_i λ μ | J_f M_f⟩ · ⟨J_f ‖ T^λ ‖ J_i⟩ / √(2J_f + 1)`,
> so the total transition rate out of the substate `|J_i M_i⟩`, summed over all final substates and
> all components `μ`, is proportional to
>
> `Σ_{μ M_f} ⟨J_i M_i λ μ | J_f M_f⟩² = (2J_f + 1) / (2J_i + 1)`.
>
> The right-hand side does not depend on `M_i`: an unpolarised and a fully polarised initial state
> decay at the same total rate, and `|⟨J_f ‖ T^λ ‖ J_i⟩|² / (2J_i + 1)` is the rate of every
> substate.
>
> The sum runs over the first and the third column of the Clebsch–Gordan coefficient, which the
> orthogonality relations of `ClebschGordanCoefficients` do not cover. It follows from the cyclic
> symmetry of the 3j symbols (`threeJR_cycle_columns`), which moves `J_i` into the third column,
> and the orthogonality of the 3j symbols.

## ii. Key results

> - `wigner3j_cycle`: the cyclic symmetry in the parameters of `ClebschGordanCoefficients`.
> - `sum_sq_cgCoefficient_initial`: the sum rule.

## iv. References

> - A. Bohr and B. R. Mottelson, *Nuclear Structure*, Vol. I, Benjamin (1969), appendix 1A.
> - A. R. Edmonds, *Angular Momentum in Quantum Mechanics*, Princeton University Press (1957),
>   section 5.4.

## A. The cyclic symmetry

**`PhyslibAlpha.Sl2.wigner3j_cycle`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/MultipoleSumRule.lean#L66).

> `(j₁ j₂ J; m₁ m₂ -M) = (j₂ J j₁; m₂ -M m₁)` in the parameters of
> `ClebschGordanCoefficients`: the new triple is `(n, m + n - 2k)` with `k' = n - k`, `l' = m - α`,
> `α' = β` and `β' = m + n - 2k - l`.

```lean
lemma wigner3j_cycle {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (hl : l ≤ m + n - 2 * k)
    (hα : α ≤ m) (hβ : β ≤ n) :
    wigner3j m n k l α β =
      wigner3j n (m + n - 2 * k) (n - k) (m - α) β (m + n - 2 * k - l)
```

## B. The sum rule

**`PhyslibAlpha.Sl2.sum_sq_cgCoefficient_initial`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/MultipoleSumRule.lean#L89).

> **Sum rule for multipole transitions.** With `j₁ = m/2 = J_i`, `j₂ = n/2 = λ`,
> `J = (m + n)/2 - k = J_f` and `m₁ = j₁ - α = M_i`,
> `Σ_{μ M_f} ⟨J_i M_i λ μ | J_f M_f⟩² = (2J_f + 1) / (2J_i + 1)`.

```lean
lemma sum_sq_cgCoefficient_initial (hmn : 0 < m + n) {k α : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hα : α ≤ m) :
    ∑ b ∈ Finset.range (n + 1), ∑ l ∈ Finset.range (m + n - 2 * k + 1),
      cgCoefficient m n k l α b ^ 2 = ((m + n - 2 * k + 1 : ℕ) : ℝ) / ((m + 1 : ℕ) : ℝ)
```

## Depends on

- [Wigner 3j symbols](wigner3j.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/MultipoleSumRule.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/MultipoleSumRule.lean)
