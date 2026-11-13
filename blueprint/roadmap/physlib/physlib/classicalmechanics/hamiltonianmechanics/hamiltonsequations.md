---
declaration: module
origin: cited
lean: ClassicalMechanics.hamiltons_equations_varGradient, ClassicalMechanics.hamiltonEqOp, ClassicalMechanics.hamiltonEqOp_eq, ClassicalMechanics.hamiltonEqOp_eq_zero_iff_hamiltons_equations
statement: formalized
proof: formalized
---

# Hamilton's equations

The module `Physlib.ClassicalMechanics.HamiltonianMechanics.HamiltonsEquations`, [Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean): 4 declarations, 2 with a docstring, 1 listed as significant.

> In this module, given a Hamiltonian function `H : Time → X → X → ℝ`,
> we define the operator `hamiltonEqOp`
> which when equals zero implies hamilton's equations.
>
> We show that the variational derivative of the action functional
> `∫ ⟪p, dq/dt⟫ - H(t, p, q) dt` is equal to the `hamiltonEqOp`
> applied to `(p, q)`.

## References

> * G. J. Sussman and J. Wisdom, "Structure and Interpretation of Classical Mechanics", Section 3.1.2.
>   <https://groups.csail.mit.edu/mac/users/gjs/6946/sicm-html/book-Z-H-36.html#%_sec_3.1.2>.
>   [ref: sussman\_wisdom\_sicm]

**`ClassicalMechanics.hamiltonEqOp`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean#L39).

> Given a hamiltonian `H : Time → X → X → ℝ` the operator which when
> set to zero implies the Hamilton equations.

```lean
noncomputable def hamiltonEqOp (H : Time → X → X → ℝ) (p : Time → X) (q : Time → X) :
    Time → X × X
```

**`ClassicalMechanics.hamiltonEqOp_eq`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean#L44).

```lean
lemma hamiltonEqOp_eq (H : Time → X → X → ℝ) (p : Time → X) (q : Time → X) :
    hamiltonEqOp H p q = fun t => (∂ₜ q t + -gradient (fun x => H t x (q t)) (p t),
      - ∂ₜ p t + -gradient (fun x => H t (p t) x) (q t))
```

**`ClassicalMechanics.hamiltonEqOp_eq_zero_iff_hamiltons_equations`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean#L49).

```lean
lemma hamiltonEqOp_eq_zero_iff_hamiltons_equations (H : Time → X → X → ℝ)
    (p : Time → X) (q : Time → X) :
    hamiltonEqOp H p q = 0 ↔
    (∀ t, ∂ₜ q t = gradient (fun x => H t x (q t)) (p t)) ∧
    (∀ t, ∂ₜ p t = -gradient (fun x => H t (p t) x) (q t))
```

**`ClassicalMechanics.hamiltons_equations_varGradient`**, a theorem, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean#L58). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The variational derivative of `⟪(pq' t).1, ∂ₜ (Prod.snd ∘ pq') t⟫_ℝ - H t (pq' t).1 (pq' t).2`
> for a hamiltonian `H` is equal to the Hamilton equations operator.

```lean
theorem hamiltons_equations_varGradient
    (H : Time → X → X → ℝ) (pq : Time → X × X) (hp : ContDiff ℝ ∞ pq)
    (hL : ContDiff ℝ ∞ ↿H) :
    (δ (pq':= pq), ∫ t, ⟪(pq' t).1, ∂ₜ (Prod.snd ∘ pq') t⟫_ℝ - H t (pq' t).1 (pq' t).2) =
    fun t => hamiltonEqOp H (fun t => (pq t).1) (fun t => (pq t).2) t
```

## Depends on

- [Variational gradient](../../mathematics/variationalcalculus/hasvargradient.md)
- [Time Derivatives](../../spaceandtime/time/derivatives.md)

## Sources

- [Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ClassicalMechanics/HamiltonianMechanics/HamiltonsEquations.lean)
