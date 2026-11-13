---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.neg_one_pow_congr_nat, PhyslibAlpha.Sl2.wigner3j_swap, PhyslibAlpha.Sl2.cgCoefficient_swap, PhyslibAlpha.Sl2.stringVec_eq_smul_embed, PhyslibAlpha.Sl2.invForm_cgProj, PhyslibAlpha.Sl2.IsTensorOperator.exists_normVec_eq, PhyslibAlpha.Sl2.IsTensorOperator.sum_sq_normVec
statement: formalized
proof: formalized
---

# The Wigner–Eckart theorem with Clebsch–Gordan coefficients

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.WignerEckartNormalized`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean): 7 declarations, 5 with a docstring.

> The matrix elements of a tensor operator in the orthonormal bases are a reduced matrix element
> times the Clebsch–Gordan coefficients, and the total rate out of a substate does not depend on
> the substate.

## i. Overview

> `WignerEckart` shows that a tensor operator `T` of rank `κ = k/2` from `V(m)` to
> `V(k + m - 2j)` is `T x y = c • cgProj (x ⊗ y)`. Here the projection is written in the
> orthonormal bases: `⟨u_s, cgProj x⟩ = ⟨w_j, w_j⟩^(-1/2) ⟨|J', J' - s⟩, x⟩` (`invForm_cgProj`),
> because the component `V(k + m - 2j)` sits isometrically inside `V(k) ⊗ V(m)` (`embed`) and is
> orthogonal to the other components. With `J = m/2`, `M = J - r`, `μ = κ - q`, `J' = J + κ - j`
> and `M' = J' - s` this gives
>
> `⟨J' M' | T^κ_μ | J M⟩ = R · ⟨κ μ J M | J' M'⟩`
>
> with one reduced matrix element `R` (`IsTensorOperator.exists_normVec_eq`). The coefficient is
> coupled in the order `κ ⊗ J`; `cgCoefficient_swap` relates it to the order `J ⊗ κ` by the phase
> `(-1)^(J + κ - J')`.
>
> Combined with the sum rule of `MultipoleSumRule`, the total transition strength out of
> `|J M⟩`,
>
> `Σ_{μ M'} |⟨J' M' | T^κ_μ | J M⟩|² = R² (2J' + 1) / (2J + 1)`,
>
> does not depend on `M` (`IsTensorOperator.sum_sq_normVec`).

## ii. Key results

> - `wigner3j_swap`, `cgCoefficient_swap`: exchanging the two coupled angular momenta.
> - `invForm_cgProj`: the Clebsch–Gordan projection in the orthonormal bases.
> - `IsTensorOperator.exists_normVec_eq`: the Wigner–Eckart theorem with Clebsch–Gordan
>   coefficients.
> - `IsTensorOperator.sum_sq_normVec`: the total strength out of a substate.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.11.
> - A. R. Edmonds, *Angular Momentum in Quantum Mechanics*, Princeton University Press (1957),
>   section 5.4.

## A. Exchanging the coupled angular momenta

**`PhyslibAlpha.Sl2.neg_one_pow_congr_nat`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L77).

```lean
lemma neg_one_pow_congr_nat {p q : ℕ} (h : p % 2 = q % 2) : (-1 : ℝ) ^ p = (-1) ^ q
```

**`PhyslibAlpha.Sl2.wigner3j_swap`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L85).

> `(j₂ j₁ J; m₂ m₁ -M) = (-1)^(j₁ + j₂ + J) (j₁ j₂ J; m₁ m₂ -M)`.

```lean
lemma wigner3j_swap {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n) (hl : l ≤ m + n - 2 * k)
    (hα : α ≤ m) (hβ : β ≤ n) :
    wigner3j n m k l β α = (-1) ^ (m + n - k) * wigner3j m n k l α β
```

**`PhyslibAlpha.Sl2.cgCoefficient_swap`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L107).

> **Exchange symmetry.** `⟨j₁ m₁ j₂ m₂ | J M⟩ = (-1)^(j₁ + j₂ - J) ⟨j₂ m₂ j₁ m₁ | J M⟩`.

```lean
lemma cgCoefficient_swap (hmn : 0 < m + n) {k l α β : ℕ} (hkm : k ≤ m) (hkn : k ≤ n)
    (hl : l ≤ m + n - 2 * k) (hα : α ≤ m) (hβ : β ≤ n) :
    cgCoefficient m n k l α β = (-1) ^ k * cgCoefficient n m k l β α
```

## B. The projections in the orthonormal bases

**`PhyslibAlpha.Sl2.stringVec_eq_smul_embed`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L131).

```lean
lemma stringVec_eq_smul_embed (hmn : 0 < m + n) (j : Fin (min m n + 1)) (l : ℕ) :
    stringVec m n j l = Real.sqrt (hwNormSq m n j) • embed hmn j (vNat _ l)
```

**`PhyslibAlpha.Sl2.invForm_cgProj`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L139).

> `⟨u, cgProj x⟩ = ⟨w_j, w_j⟩^(-1/2) ⟨embed u, x⟩`.

```lean
lemma invForm_cgProj (hmn : 0 < m + n) (j : Fin (min m n + 1))
    (y : StandardSl2Module ℝ (m + n - 2 * (j : ℕ)))
    (x : StandardSl2Module ℝ m ⊗[ℝ] StandardSl2Module ℝ n) :
    invForm ℝ _ y (cgProj hmn j x) =
      (Real.sqrt (hwNormSq m n j))⁻¹ * tensorForm m n (embed hmn j y) x
```

## C. The Wigner–Eckart theorem

**`PhyslibAlpha.Sl2.IsTensorOperator.exists_normVec_eq`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L180).

> **Wigner–Eckart theorem with Clebsch–Gordan coefficients.** With `κ = k/2`, `μ = κ - q`,
> `J = m/2`, `M = J - r`, `J' = (k + m)/2 - j` and `M' = J' - s`, there is a reduced matrix element
> `R` with `⟨J' M' | T^κ_μ | J M⟩ = R · ⟨κ μ J M | J' M'⟩` for all `q, r, s`.

```lean
lemma exists_normVec_eq (hT : IsTensorOperator T) :
    ∃ R : ℝ, ∀ q r s : ℕ, invForm ℝ _ (normVec _ s) (T (normVec k q) (normVec m r)) =
      R * cgCoefficient k m j s q r
```

## D. The total strength out of a substate

**`PhyslibAlpha.Sl2.IsTensorOperator.sum_sq_normVec`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean#L197).

> **The total strength out of a substate.** If `⟨J' M' | T^κ_μ | J M⟩ = R · ⟨κ μ J M | J' M'⟩`,
> then `Σ_{μ M'} |⟨J' M' | T^κ_μ | J M⟩|² = R² (2J' + 1) / (2J + 1)` for every `M`.

```lean
lemma sum_sq_normVec (R : ℝ)
    (hR : ∀ q r s : ℕ, invForm ℝ _ (normVec _ s) (T (normVec k q) (normVec m r)) =
      R * cgCoefficient k m j s q r) {r : ℕ} (hr : r ≤ m) :
    ∑ q ∈ Finset.range (k + 1), ∑ s ∈ Finset.range (k + m - 2 * (j : ℕ) + 1),
      (invForm ℝ _ (normVec _ s) (T (normVec k q) (normVec m r))) ^ 2 =
        R ^ 2 * (((k + m - 2 * (j : ℕ) + 1 : ℕ) : ℝ) / ((m + 1 : ℕ) : ℝ))
```

## Depends on

- [The two coupling schemes of three angular momenta](couplingschemes.md)
- [Wigner 3j symbols](wigner3j.md)
- [The Wigner–Eckart theorem for sl₂](wignereckart.md)

## Proof depends on

- [A sum rule for multipole transitions](multipolesumrule.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/WignerEckartNormalized.lean)
