---
declaration: module
origin: cited
lean: MvPolynomial.coeff_aeval_diag, MvPolynomial.coeff_eq_zero_of_charge_ne_zero
statement: formalized
proof: formalized
---

# Charge balancing for polynomials

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.ChargeBalance`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/ChargeBalance.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/ChargeBalance.lean): 2 declarations, 2 with a docstring.

> A polynomial invariant under a phase rotation of charged variables has only charge-balanced terms.

## i. Overview

> If the variables of a polynomial carry charges under a phase (here a single element `c` of infinite
> order), then invariance under the simultaneous phase rotation `Xᵢ ↦ c^{wᵢ} Xᵢ` forces every
> monomial to be *charge balanced* (net charge zero). This is the algebraic content of the statement
> that a gauge invariant potential, restricted to a slice on which the gauge torus acts diagonally,
> can only contain charge-balanced monomials.

## ii. Key results

> - `MvPolynomial.coeff_aeval_diag` : rescaling each variable `Xᵢ` by a constant `d i` multiplies the
>   coefficient of a monomial by the corresponding product of the `d i`.
> - `MvPolynomial.coeff_eq_zero_of_charge_ne_zero` : charge balancing, a polynomial invariant under
>   the phase rotation has vanishing coefficients on monomials of nonzero net charge.

## iv. References

> * None.

## A. Rescaling the variables

**`MvPolynomial.coeff_aeval_diag`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/ChargeBalance.lean#L54).

> Rescaling each variable `Xᵢ` by a constant `d i` multiplies the coefficient of the monomial `m`
> by `∏ᵢ (d i) ^ (m i)`.

```lean
lemma coeff_aeval_diag {σ R : Type*} [CommRing R] (d : σ → R) (f : MvPolynomial σ R)
    (m : σ →₀ ℕ) :
    (aeval (fun i => C (d i) * X i) f).coeff m = (m.prod fun i k => d i ^ k) * f.coeff m
```

## B. Charge balancing

**`MvPolynomial.coeff_eq_zero_of_charge_ne_zero`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/ChargeBalance.lean#L96).

> **Charge balancing.** If each variable `Xᵢ` carries an integer charge `w i`, `c` is a phase of
> infinite order, and the polynomial `f` is invariant under the charge rotation
> `Xᵢ ↦ c^{wᵢ} Xᵢ`, then every monomial with nonzero net charge has vanishing coefficient.

```lean
lemma coeff_eq_zero_of_charge_ne_zero {σ K : Type*} [Field K] (w : σ → ℤ) (c : K) (hc : c ≠ 0)
    (hroot : ∀ n : ℤ, c ^ n = 1 → n = 0) {f : MvPolynomial σ K}
    (hf : aeval (fun i => C (c ^ (w i)) * X i) f = f) {m : σ →₀ ℕ}
    (hm : ∑ i ∈ m.support, (m i : ℤ) * w i ≠ 0) :
    f.coeff m = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/ChargeBalance.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/ChargeBalance.lean)
