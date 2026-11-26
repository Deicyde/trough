---
declaration: module
origin: cited
lean: QuantumMechanics.PoschlTeller.polyDeriv, QuantumMechanics.PoschlTeller.polyRaise, QuantumMechanics.PoschlTeller.polyScattering, QuantumMechanics.PoschlTeller.waveOfPoly, QuantumMechanics.PoschlTeller.waveOfPoly_hasTemperateGrowth, QuantumMechanics.PoschlTeller.conj_waveOfPoly_hasTemperateGrowth, QuantumMechanics.PoschlTeller.scatteringState, QuantumMechanics.PoschlTeller.scatteringState_apply
statement: formalized
proof: formalized
---

# Scattering states of the 1d Pöschl-Teller system

The module `Physlib.QuantumMechanics.PoschlTeller.Scattering`, [Physlib/QuantumMechanics/PoschlTeller/Scattering.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean): 34 declarations, 34 with a docstring.

> The Pöschl-Teller potential is reflectionless.

## i. Overview

> At energy `E = ℏ² k² / (2 m)` the time-independent Schrödinger equation of the Pöschl-Teller
> system has the exact solution `ψₖ(x) = Pₖ(tanh (κ x)) e^{i k x}`, where the polynomial `Pₖ` is
> obtained by applying the operators `-∂ₓ + n κ tanh (κ x)`, for `n = 1, …, N`, to the plane wave
> `e^{i k x}`. The operator `-∂ₓ + n κ tanh (κ x)` intertwines the Hamiltonians of the Pöschl-Teller
> systems with family numbers `n - 1` and `n`, so it maps solutions of the one to solutions of the
> other at the same energy.
>
> Since `tanh (κ x) → ±1` as `x → ±∞`, the solution tends to `Pₖ(±1) e^{i k x}` at both ends.
> For `k ≠ 0` it describes a wave incident from the left (`k > 0`) or from the right (`k < 0`)
> which is fully transmitted: no reflected wave `e^{-i k x}` appears. This is the statement that the
> Pöschl-Teller potential is reflectionless.
>
> The polynomial in `tanh (κ x)` multiplying `e^{i k x}` is tracked as an element of `ℂ[X]`, so that
> the intertwining relation becomes an identity of polynomials.
>
> The scattering wave `ψₖ` is not normalizable, so it does not lie in the Hilbert space. Following
> `momentumState`, the scattering state is instead the bra `⟨ψₖ|` in the strong dual of the Schwartz
> space, and the Schrödinger equation holds in the form `⟨ψₖ| H = E ⟨ψₖ|`, where `H` is the
> Hamiltonian acting on Schwartz maps.

## ii. Key results

> - `scatteringState_comp_hamiltonianCLM` : the scattering state is a generalized eigenvector of the
>   Hamiltonian with energy `ℏ² k² / (2 m)`.
> - `tendsto_exp_mul_scatteringState_translateSchwartz_atTop`,
>   `tendsto_exp_mul_scatteringState_translateSchwartz_atBot` : the scattering state approaches a
>   non-zero multiple of the plane wave bra `⟨k|` as test functions are translated to `±∞`.
> - `isReflectionless` : the Pöschl-Teller potential is reflectionless.

## iv. References

> * https://arxiv.org/pdf/2411.14941. [ref: arxiv\_2411\_14941]

## A. The scattering state

### A.1. The scattering polynomials

**`QuantumMechanics.PoschlTeller.polyDeriv`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L91).

> The derivative acting on the polynomial of a wave `p(tanh (κ x)) e^{i k x}`,
> `p ↦ κ (1 - X²) p' + i k p`, so that
> `∂ₓ (p(tanh (κ x)) e^{i k x}) = (polyDeriv k p)(tanh (κ x)) e^{i k x}`.

```lean
def polyDeriv (k : ℝ) (p : ℂ[X]) : ℂ[X]
```

**`QuantumMechanics.PoschlTeller.polyRaise`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L96).

> The raising operator `-∂ₓ + n κ tanh (κ x)` acting on the polynomial of a wave
> `p(tanh (κ x)) e^{i k x}`.

```lean
def polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) : ℂ[X]
```

**`QuantumMechanics.PoschlTeller.polyScattering`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L101).

> The polynomial `Pₖ` of the scattering state `Pₖ(tanh (κ x)) e^{i k x}` of the Pöschl-Teller
> system with family number `n`, obtained by applying the raising operators with
> `1, …, n` to `1`.

```lean
def polyScattering (k : ℝ) : ℕ → ℂ[X]
```

### A.2. Waves modulated by polynomials in `tanh (κ x)`

**`QuantumMechanics.PoschlTeller.waveOfPoly`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L110).

> The wave `x ↦ p(tanh (κ x)) e^{i k x}`.

```lean
def waveOfPoly (k : ℝ) (p : ℂ[X]) (x : ℝ) : ℂ
```

**`QuantumMechanics.PoschlTeller.waveOfPoly_hasTemperateGrowth`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L114).

> The wave `p(tanh (κ x)) e^{i k x}` has temperate growth.

```lean
lemma waveOfPoly_hasTemperateGrowth (k : ℝ) (p : ℂ[X]) :
    (Q.waveOfPoly k p).HasTemperateGrowth
```

**`QuantumMechanics.PoschlTeller.conj_waveOfPoly_hasTemperateGrowth`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L126).

> The complex conjugate of `p(tanh (κ x)) e^{i k x}`, as a function on `Space 1`, has temperate
> growth.

```lean
lemma conj_waveOfPoly_hasTemperateGrowth (k : ℝ) (p : ℂ[X]) :
    (fun x : Space 1 => conj (Q.waveOfPoly k p (x 0))).HasTemperateGrowth
```

### A.3. The scattering state as a bra

**`QuantumMechanics.PoschlTeller.scatteringState`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L139).

> The scattering state with wavenumber `k` as a member of the strong dual of the Schwartz space.
>
> This is the bra `⟨ψₖ|` of the non-normalizable scattering wave `ψₖ`, that is
> `φ ↦ ⟨ψₖ, φ⟩ = ∫ ψ̄ₖ φ`.

```lean
def scatteringState (k : ℝ) : StrongDual ℂ 𝓢(Space 1, ℂ)
```

**`QuantumMechanics.PoschlTeller.scatteringState_apply`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L144).

> The defining property of the scattering state.

```lean
lemma scatteringState_apply (k : ℝ) (φ : 𝓢(Space 1, ℂ)) :
    Q.scatteringState k φ = ∫ x, conj (Q.waveOfPoly k (Q.polyScattering k Q.N) (x 0)) * φ x
```

## B. Polynomial identities

### B.1. The intertwining relation

**`QuantumMechanics.PoschlTeller.polyReducedHamiltonian`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L161).

> The operator `-∂ₓ² - n (n + 1) κ² / cosh² (κ x)` acting on the polynomial of a wave
> `p(tanh (κ x)) e^{i k x}`. This is `2 m / ℏ²` times the Hamiltonian of the Pöschl-Teller system
> with family number `n`.

```lean
def polyReducedHamiltonian (k : ℝ) (n : ℕ) (p : ℂ[X]) : ℂ[X]
```

**`QuantumMechanics.PoschlTeller.polyReducedHamiltonian_polyRaise`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L165).

> The raising operator intertwines the Hamiltonians with family numbers `n` and `n + 1`.

```lean
lemma polyReducedHamiltonian_polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) :
    Q.polyReducedHamiltonian k (n + 1) (Q.polyRaise k (n + 1) p) =
      Q.polyRaise k (n + 1) (Q.polyReducedHamiltonian k n p)
```

**`QuantumMechanics.PoschlTeller.polyDeriv_C`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L176).

> The derivative of a constant multiple of the plane wave `c e^{i k x}` is `i k c e^{i k x}`.

```lean
lemma polyDeriv_C (k : ℝ) (c : ℂ) : Q.polyDeriv k (C c) = C (k * I * c)
```

**`QuantumMechanics.PoschlTeller.polyRaise_C_mul`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L180).

> The raising operator is linear with respect to constant multiples.

```lean
lemma polyRaise_C_mul (k : ℝ) (n : ℕ) (c : ℂ) (p : ℂ[X]) :
    Q.polyRaise k n (C c * p) = C c * Q.polyRaise k n p
```

**`QuantumMechanics.PoschlTeller.polyReducedHamiltonian_polyScattering`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L187).

> The scattering polynomial with family number `n` is an eigenvector of the reduced Hamiltonian
> with eigenvalue `k²`.

```lean
lemma polyReducedHamiltonian_polyScattering (k : ℝ) (n : ℕ) :
    Q.polyReducedHamiltonian k n (Q.polyScattering k n) =
      C ((k : ℂ) ^ 2) * Q.polyScattering k n
```

### B.2. Values at `±1`

**`QuantumMechanics.PoschlTeller.eval_one_polyRaise`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L203).

> At `tanh (κ x) = 1` the raising operator acts as multiplication by `n κ - i k`.

```lean
lemma eval_one_polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) :
    (Q.polyRaise k n p).eval 1 = (n * Q.κ - k * I) * p.eval 1
```

**`QuantumMechanics.PoschlTeller.eval_neg_one_polyRaise`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L211).

> At `tanh (κ x) = -1` the raising operator acts as multiplication by `-n κ - i k`.

```lean
lemma eval_neg_one_polyRaise (k : ℝ) (n : ℕ) (p : ℂ[X]) :
    (Q.polyRaise k n p).eval (-1) = (-(n * Q.κ) - k * I) * p.eval (-1)
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_one`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L219).

> The value at `1` of the scattering polynomial is `∏ₙ (n κ - i k)`.

```lean
lemma polyScattering_eval_one (k : ℝ) (n : ℕ) :
    (Q.polyScattering k n).eval 1 = ∏ j ∈ Finset.range n, ((j + 1) * Q.κ - k * I)
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_neg_one`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L229).

> The value at `-1` of the scattering polynomial is `∏ₙ (-n κ - i k)`.

```lean
lemma polyScattering_eval_neg_one (k : ℝ) (n : ℕ) :
    (Q.polyScattering k n).eval (-1) = ∏ j ∈ Finset.range n, (-((j + 1) * Q.κ) - k * I)
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_one_ne_zero`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L239).

> The value at `1` of the scattering polynomial is non-zero.

```lean
lemma polyScattering_eval_one_ne_zero (k : ℝ) (n : ℕ) : (Q.polyScattering k n).eval 1 ≠ 0
```

**`QuantumMechanics.PoschlTeller.polyScattering_eval_neg_one_ne_zero`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L249).

> The value at `-1` of the scattering polynomial is non-zero.

```lean
lemma polyScattering_eval_neg_one_ne_zero (k : ℝ) (n : ℕ) :
    (Q.polyScattering k n).eval (-1) ≠ 0
```

## C. The wave equation and asymptotics

### C.1. Derivatives

**`QuantumMechanics.PoschlTeller.hasDerivAt_waveOfPoly`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L268).

> The derivative of `p(tanh (κ x)) e^{i k x}` is `(polyDeriv k p)(tanh (κ x)) e^{i k x}`.

```lean
lemma hasDerivAt_waveOfPoly (k : ℝ) (p : ℂ[X]) (x : ℝ) :
    HasDerivAt (Q.waveOfPoly k p) (Q.waveOfPoly k (Q.polyDeriv k p) x) x
```

**`QuantumMechanics.PoschlTeller.deriv_conj_waveOfPoly`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L283).

> The derivative of the complex conjugate of `p(tanh (κ x)) e^{i k x}` on `Space 1`.

```lean
lemma deriv_conj_waveOfPoly (k : ℝ) (p : ℂ[X]) :
    ∂[0] (fun x : Space 1 => conj (Q.waveOfPoly k p (x 0))) =
      fun x => conj (Q.waveOfPoly k (Q.polyDeriv k p) (x 0))
```

### C.2. The Hamiltonian

**`QuantumMechanics.PoschlTeller.waveOfPoly_C_mul`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L303).

> Multiplying the polynomial by a constant multiplies the wave by that constant.

```lean
lemma waveOfPoly_C_mul (k : ℝ) (c : ℂ) (p : ℂ[X]) :
    Q.waveOfPoly k (C c * p) = c • Q.waveOfPoly k p
```

**`QuantumMechanics.PoschlTeller.waveOfPoly_polyReducedHamiltonian`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L311).

> The Hamiltonian `-ℏ² / (2 m) ∂ₓ² + V` acts on `p(tanh (κ x)) e^{i k x}` through the reduced
> Hamiltonian with family number `N`.

```lean
lemma waveOfPoly_polyReducedHamiltonian (k : ℝ) (p : ℂ[X]) (x : Space 1) :
    ((ℏ ^ 2 / (2 * Q.m) : ℝ) : ℂ) * Q.waveOfPoly k (Q.polyReducedHamiltonian k Q.N p) (x 0) =
      -((ℏ ^ 2 / (2 * Q.m) : ℝ) : ℂ) * Q.waveOfPoly k (Q.polyDeriv k (Q.polyDeriv k p)) (x 0) +
        Q.potential x * Q.waveOfPoly k p (x 0)
```

### C.3. Asymptotics

**`QuantumMechanics.PoschlTeller.waveOfPoly_mul_exp`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L325).

> Removing the plane wave factor from `p(tanh (κ x)) e^{i k x}` leaves `p(tanh (κ x))`.

```lean
lemma waveOfPoly_mul_exp (k : ℝ) (p : ℂ[X]) (x : ℝ) :
    Q.waveOfPoly k p x * exp (-(k * x * I)) = p.eval (Real.tanh (Q.κ * x) : ℂ)
```

**`QuantumMechanics.PoschlTeller.tendsto_waveOfPoly_mul_exp_atTop`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L330).

> As `x → ∞`, `p(tanh (κ x)) e^{i k x}` approaches `p(1) e^{i k x}`.

```lean
lemma tendsto_waveOfPoly_mul_exp_atTop (k : ℝ) (p : ℂ[X]) :
    Tendsto (fun x => Q.waveOfPoly k p x * exp (-(k * x * I))) atTop (𝓝 (p.eval 1))
```

**`QuantumMechanics.PoschlTeller.tendsto_waveOfPoly_mul_exp_atBot`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L339).

> As `x → -∞`, `p(tanh (κ x)) e^{i k x}` approaches `p(-1) e^{i k x}`.

```lean
lemma tendsto_waveOfPoly_mul_exp_atBot (k : ℝ) (p : ℂ[X]) :
    Tendsto (fun x => Q.waveOfPoly k p x * exp (-(k * x * I))) atBot (𝓝 (p.eval (-1)))
```

## D. Scattering states as generalized eigenvectors

**`QuantumMechanics.PoschlTeller.integral_conj_waveOfPoly_polyScattering_mul_hamiltonianCLM`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L354).

> The scattering wave `ψₖ = waveOfPoly k (polyScattering k N)` solves the time-independent
> Schrödinger equation at energy `ℏ² k² / (2 m)` against all Schwartz maps,
> `∫ ψ̄ₖ (H φ) = E ∫ ψ̄ₖ φ`.

```lean
lemma integral_conj_waveOfPoly_polyScattering_mul_hamiltonianCLM (k : ℝ) (φ : 𝓢(Space 1, ℂ)) :
    ∫ x, conj (Q.waveOfPoly k (Q.polyScattering k Q.N) (x 0)) *
        Q.toSpaceDQuantumSystem.hamiltonianCLM φ x =
      ((ℏ ^ 2 * k ^ 2 / (2 * Q.m) : ℝ) : ℂ) *
        ∫ x, conj (Q.waveOfPoly k (Q.polyScattering k Q.N) (x 0)) * φ x
```

**`QuantumMechanics.PoschlTeller.scatteringState_comp_hamiltonianCLM`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L406).

> The scattering state `scatteringState k` is a generalized eigenvector of the Hamiltonian with
> energy `ℏ² k² / (2 m)`, in the bra form `⟨ψₖ| H = E ⟨ψₖ|` as functionals on Schwartz space.

```lean
lemma scatteringState_comp_hamiltonianCLM (k : ℝ) :
    Q.scatteringState k ∘L Q.toSpaceDQuantumSystem.hamiltonianCLM =
      ((ℏ ^ 2 * k ^ 2 / (2 * Q.m) : ℝ) : ℂ) • Q.scatteringState k
```

## E. Reflectionlessness

**`QuantumMechanics.PoschlTeller.exists_norm_waveOfPoly_le`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L418).

> The wave `p(tanh (κ x)) e^{i k x}` is bounded.

```lean
lemma exists_norm_waveOfPoly_le (k : ℝ) (p : ℂ[X]) : ∃ M, ∀ x, ‖Q.waveOfPoly k p x‖ ≤ M
```

**`QuantumMechanics.PoschlTeller.integral_conj_waveOfPoly_mul_translateSchwartz`**, a lemma, [line 426](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L426).

> Translating a Schwartz map by `a` shifts the argument of the wave by `a`.

```lean
lemma integral_conj_waveOfPoly_mul_translateSchwartz (k a : ℝ) (p : ℂ[X]) (φ : 𝓢(Space 1, ℂ)) :
    ∫ x, conj (Q.waveOfPoly k p (x 0)) * translateSchwartz (EuclideanSpace.single 0 a) φ x =
      ∫ x, conj (Q.waveOfPoly k p (x 0 + a)) * φ x
```

**`QuantumMechanics.PoschlTeller.tendsto_exp_mul_integral_conj_waveOfPoly_mul_translateSchwartz`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L438).

> If `ψ(x) e^{-i k x}` tends to `c` far along the filter `l`, then translating a test function
> along `l` pairs it with `c̄ ⟨k|`, up to the phase `e^{-i k a}`.

```lean
lemma tendsto_exp_mul_integral_conj_waveOfPoly_mul_translateSchwartz {l : Filter ℝ}
    [l.IsCountablyGenerated] (k : ℝ) (p : ℂ[X]) (c : ℂ) (φ : 𝓢(Space 1, ℂ))
    (h : ∀ x, Tendsto (fun a => Q.waveOfPoly k p (x + a) * exp (-(k * (x + a : ℝ) * I))) l (𝓝 c)) :
    Tendsto (fun a : ℝ => exp (k * a * I) * ∫ x, conj (Q.waveOfPoly k p (x 0)) *
        translateSchwartz (EuclideanSpace.single 0 a) φ x) l
      (𝓝 (conj c * momentumState (oneEquiv.symm k) φ))
```

**`QuantumMechanics.PoschlTeller.tendsto_exp_mul_scatteringState_translateSchwartz_atTop`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L474).

> Far to the right the scattering state looks like the bra of the transmitted plane wave:
> `e^{i k a} ⟨ψₖ|τₐ φ⟩ → conj (∏ₙ (n κ - i k)) ⟨k|φ⟩` as `a → ∞`.

```lean
lemma tendsto_exp_mul_scatteringState_translateSchwartz_atTop (k : ℝ) (φ : 𝓢(Space 1, ℂ)) :
    Tendsto (fun a : ℝ => exp (k * a * I) *
        Q.scatteringState k (translateSchwartz (EuclideanSpace.single 0 a) φ)) atTop
      (𝓝 (conj (∏ j ∈ Finset.range Q.N, ((j + 1) * Q.κ - k * I)) *
        momentumState (oneEquiv.symm k) φ))
```

**`QuantumMechanics.PoschlTeller.tendsto_exp_mul_scatteringState_translateSchwartz_atBot`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L486).

> Far to the left the scattering state looks like the bra of the same plane wave, with no
> reflected part: `e^{i k a} ⟨ψₖ|τₐ φ⟩ → conj (∏ₙ (-n κ - i k)) ⟨k|φ⟩` as `a → -∞`.

```lean
lemma tendsto_exp_mul_scatteringState_translateSchwartz_atBot (k : ℝ) (φ : 𝓢(Space 1, ℂ)) :
    Tendsto (fun a : ℝ => exp (k * a * I) *
        Q.scatteringState k (translateSchwartz (EuclideanSpace.single 0 a) φ)) atBot
      (𝓝 (conj (∏ j ∈ Finset.range Q.N, (-((j + 1) * Q.κ) - k * I)) *
        momentumState (oneEquiv.symm k) φ))
```

**`QuantumMechanics.PoschlTeller.isReflectionless`**, a lemma, [line 498](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean#L498).

> The Pöschl-Teller potential is reflectionless: for every wavenumber `k ≠ 0` the scattering
> state passes the well with no reflected wave `e^{-i k x}`.

```lean
lemma isReflectionless : Q.toSpaceDQuantumSystem.IsReflectionless
```

## Depends on

- [1d Pöschl-Teller](basic.md)

## Sources

- [Physlib/QuantumMechanics/PoschlTeller/Scattering.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/PoschlTeller/Scattering.lean)
