---
declaration: module
origin: cited
lean: QuantumMechanics.PoschlTeller.polyDeriv, QuantumMechanics.PoschlTeller.polyRaise, QuantumMechanics.PoschlTeller.polyReducedHamiltonian, QuantumMechanics.PoschlTeller.polyReducedHamiltonian_polyRaise, QuantumMechanics.PoschlTeller.polyDeriv_C, QuantumMechanics.PoschlTeller.polyRaise_C_mul, QuantumMechanics.PoschlTeller.polyScattering, QuantumMechanics.PoschlTeller.polyReducedHamiltonian_polyScattering
statement: formalized
proof: formalized
---

# Scattering states of the 1d Pöschl-Teller system

The module `Physlib.QuantumMechanics.PoschlTeller.Scattering`, [Physlib/QuantumMechanics/PoschlTeller/Scattering.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean): 14 declarations, 14 with a docstring.

> The polynomials describing the scattering states of the Pöschl-Teller system.

## i. Overview

> At energy `E = ℏ² k² / (2 m)` the scattering states of the Pöschl-Teller system are of the form
> `ψₖ(x) = Pₖ(tanh (κ x)) e^{i k x}`, where the polynomial `Pₖ` is obtained by applying the
> operators `-∂ₓ + n κ tanh (κ x)`, for `n = 1, …, N`, to the plane wave `e^{i k x}`. The operator
> `-∂ₓ + n κ tanh (κ x)` intertwines the Hamiltonians of the Pöschl-Teller systems with family
> numbers `n - 1` and `n`, so it maps solutions of the one to solutions of the other at the same
> energy.
>
> This file works with the polynomial in `tanh (κ x)` multiplying `e^{i k x}`, as an element of
> `ℂ[X]`. The derivative, the raising operators and the Hamiltonian become operators on `ℂ[X]`, and
> the intertwining relation becomes an identity of polynomials.

## ii. Key results

> - `polyReducedHamiltonian_polyRaise` : the raising operator intertwines the Hamiltonians with family
>   numbers `n` and `n + 1`.
> - `polyReducedHamiltonian_polyScattering` : the scattering polynomial `Pₖ` is an eigenvector of the
>   reduced Hamiltonian with eigenvalue `k²`.
> - `polyScattering_eval_one`, `polyScattering_eval_neg_one` : the values `Pₖ(1) = ∏ₙ (n κ - i k)`
>   and `Pₖ(-1) = ∏ₙ (-n κ - i k)`.

## iv. References

> * https://arxiv.org/pdf/2411.14941. [ref: arxiv\_2411\_14941]

## A. Polynomials in `tanh (κ x)`

### A.1. Derivative, raising operator and Hamiltonian

**`QuantumMechanics.PoschlTeller.polyDeriv`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L72).

> The derivative acting on the polynomial of a wave `p(tanh (κ x)) e^{i k x}`,
> `p ↦ κ (1 - X²) p' + i k p`, so that
> `∂ₓ (p(tanh (κ x)) e^{i k x}) = (polyDeriv k p)(tanh (κ x)) e^{i k x}`.

```lean
def polyDeriv (k : ℝ) (p : ℂ[X]) : ℂ[X]
```

**`QuantumMechanics.PoschlTeller.polyRaise`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L77).

> The raising operator `-∂ₓ + n κ tanh (κ x)` acting on the polynomial of a wave
> `p(tanh (κ x)) e^{i k x}`.

```lean
def polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) : ℂ[X]
```

**`QuantumMechanics.PoschlTeller.polyReducedHamiltonian`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L82).

> The operator `-∂ₓ² - n (n + 1) κ² / cosh² (κ x)` acting on the polynomial of a wave
> `p(tanh (κ x)) e^{i k x}`. This is `2 m / ℏ²` times the Hamiltonian of the Pöschl-Teller system
> with family number `n`.

```lean
def polyReducedHamiltonian (k : ℝ) (n : ℕ) (p : ℂ[X]) : ℂ[X]
```

### A.2. The intertwining relation

**`QuantumMechanics.PoschlTeller.polyReducedHamiltonian_polyRaise`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L90).

> The raising operator intertwines the Hamiltonians with family numbers `n` and `n + 1`.

```lean
lemma polyReducedHamiltonian_polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) :
    Q.polyReducedHamiltonian k (n + 1) (Q.polyRaise k (n + 1) p) =
      Q.polyRaise k (n + 1) (Q.polyReducedHamiltonian k n p)
```

**`QuantumMechanics.PoschlTeller.polyDeriv_C`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L101).

> The derivative of a constant multiple of the plane wave `c e^{i k x}` is `i k c e^{i k x}`.

```lean
lemma polyDeriv_C (k : ℝ) (c : ℂ) : Q.polyDeriv k (C c) = C (k * I * c)
```

**`QuantumMechanics.PoschlTeller.polyRaise_C_mul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L105).

> The raising operator is linear with respect to constant multiples.

```lean
lemma polyRaise_C_mul (k : ℝ) (n : ℕ) (c : ℂ) (p : ℂ[X]) :
    Q.polyRaise k n (C c * p) = C c * Q.polyRaise k n p
```

### A.3. The scattering polynomials

**`QuantumMechanics.PoschlTeller.polyScattering`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L117).

> The polynomial `Pₖ` of the scattering state `Pₖ(tanh (κ x)) e^{i k x}` of the Pöschl-Teller
> system with family number `n`, obtained by applying the raising operators with
> `1, …, n` to `1`.

```lean
def polyScattering (k : ℝ) : ℕ → ℂ[X]
```

**`QuantumMechanics.PoschlTeller.polyReducedHamiltonian_polyScattering`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L123).

> The scattering polynomial with family number `n` is an eigenvector of the reduced Hamiltonian
> with eigenvalue `k²`.

```lean
lemma polyReducedHamiltonian_polyScattering (k : ℝ) (n : ℕ) :
    Q.polyReducedHamiltonian k n (Q.polyScattering k n) =
      C ((k : ℂ) ^ 2) * Q.polyScattering k n
```

### A.4. Values at `±1`

**`QuantumMechanics.PoschlTeller.eval_one_polyRaise`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L139).

> At `tanh (κ x) = 1` the raising operator acts as multiplication by `n κ - i k`.

```lean
lemma eval_one_polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) :
    (Q.polyRaise k n p).eval 1 = (n * Q.κ - k * I) * p.eval 1
```

**`QuantumMechanics.PoschlTeller.eval_neg_one_polyRaise`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L147).

> At `tanh (κ x) = -1` the raising operator acts as multiplication by `-n κ - i k`.

```lean
lemma eval_neg_one_polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) :
    (Q.polyRaise k n p).eval (-1) = (-(n * Q.κ) - k * I) * p.eval (-1)
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_one`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L155).

> The value at `1` of the scattering polynomial is `∏ₙ (n κ - i k)`.

```lean
lemma polyScattering_eval_one (k : ℝ) (n : ℕ) :
    (Q.polyScattering k n).eval 1 = ∏ j ∈ Finset.range n, ((j + 1) * Q.κ - k * I)
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_neg_one`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L165).

> The value at `-1` of the scattering polynomial is `∏ₙ (-n κ - i k)`.

```lean
lemma polyScattering_eval_neg_one (k : ℝ) (n : ℕ) :
    (Q.polyScattering k n).eval (-1) = ∏ j ∈ Finset.range n, (-((j + 1) * Q.κ) - k * I)
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_one_ne_zero`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L175).

> The value at `1` of the scattering polynomial is non-zero.

```lean
lemma polyScattering_eval_one_ne_zero (k : ℝ) (n : ℕ) : (Q.polyScattering k n).eval 1 ≠ 0
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_neg_one_ne_zero`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L185).

> The value at `-1` of the scattering polynomial is non-zero.

```lean
lemma polyScattering_eval_neg_one_ne_zero (k : ℝ) (n : ℕ) :
    (Q.polyScattering k n).eval (-1) ≠ 0
```

## Depends on

- [1d Pöschl-Teller](basic.md)

## Sources

- [Physlib/QuantumMechanics/PoschlTeller/Scattering.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean)
