---
declaration: section
origin: cited
lean: OAI.DefocusingNLS.stable_blowup, OAI.DefocusingNLS.gaussian_blowup, OAI.DefocusingNLS.gaussian_not_almost_sure_global
statement: formalized
proof: formalized
---

# 371. Stable blowup for the defocusing Schrödinger equation

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For a sufficiently large odd nonlinearity power, constructs a nonempty open set of initial data in $H^k(\mathbb T^{12})$, with *k* > 8, whose solutions of the scalar defocusing nonlinear Schrödinger equation blow up in finite time. Thus finite-time blowup is stable under Sobolev perturbations in this supercritical regime.

## Stable self-similar blowup for a supercritical defocusing Schrödinger equation on the torus

We prove stable self-similar finite-time blowup for a supercritical defocusing nonlinear Schrödinger equation on the twelve-dimensional torus. For a sufficiently large odd power, the blowup initial data contain a nonempty open set in a high Sobolev space. As a consequence, Gaussian Fourier initial data of arbitrarily high Sobolev regularity can have positive probability of finite-time blowup.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Stable-Self-Similar-Blowup-for-a-Supercritical-Defocusing-Schrodinger-Equation-on-the-Torus-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization constructs stable self-similar finite-time blowup for defocusing nonlinear Schrödinger equations on the twelve-dimensional torus. For every prescribed lower bound on the power, it selects an odd power at least that large and a Sobolev index $k>8$ for which a nonempty open set of $H^k$ initial data has the stated classical blowup behavior. The selected quantifier gives arbitrarily large odd powers, rather than every sufficiently large odd power.

For each such construction, Gaussian Fourier data with decay exponent $\alpha>k+6$ assign positive probability to the blowup set, and almost-sure global existence fails. The exponent $\alpha$ may be arbitrarily large.

## Lean: Stable self-similar blowup and positive-probability Gaussian blowup

Stated in [DefocusingNLS.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DefocusingNLS.lean).

```lean
theorem stable_blowup (p₀ : ℕ) :
    ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ 3 ≤ p ∧ ∃ hk : 8 < (k : ℝ),
      ∃ U : Set FourierL2, U.Nonempty ∧ IsOpen U ∧ ∀ f ∈ U,
        IsClassicalDefocusingFlow k (by linarith) ((p - 1) / 2) f ∧
        HasFiniteTimeSelfSimilarBlowup k (by linarith) ((p - 1) / 2)
          (1 / ((p : ℝ) - 1)) f
```

Proved in [lean/OAI/MathematicalPhysics/DefocusingNLS/MainTheorems.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/DefocusingNLS/MainTheorems.lean#L20).

```lean
theorem gaussian_blowup (p₀ : ℕ) :
    ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ 3 ≤ p ∧ ∃ hk : 8 < (k : ℝ),
      ∃ U : Set FourierL2, U.Nonempty ∧ IsOpen U ∧
      (∀ f ∈ U, IsClassicalDefocusingFlow k (by linarith) ((p - 1) / 2) f ∧
        HasFiniteTimeSelfSimilarBlowup k (by linarith) ((p - 1) / 2)
          (1 / ((p : ℝ) - 1)) f) ∧
      ∀ α : ℝ, (k : ℝ) + 6 < α →
        (∀ᵐ g ∂fourierGaussianLaw, Memℓp (weightedGaussianCoefficient k α g) 2) ∧
        (∀ᵐ g ∂fourierGaussianLaw, ∀ n,
          sobolevFourierCoefficient k (weightedGaussianVector k α g) n =
            (1 + ‖n‖ ^ 2) ^ (-α / 2) • g n) ∧
        0 < weightedGaussianLaw k α U
```

Proved in [lean/OAI/MathematicalPhysics/DefocusingNLS/MainTheorems.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/DefocusingNLS/MainTheorems.lean#L30).

```lean
theorem gaussian_not_almost_sure_global (p₀ : ℕ) :
    ∃ p k : ℕ, p₀ ≤ p ∧ Odd p ∧ 3 ≤ p ∧ ∃ hk : 8 < (k : ℝ),
      ∀ α : ℝ, (k : ℝ) + 6 < α →
        ¬ ∀ᵐ f ∂weightedGaussianLaw k α,
          maximalSobolevInteractionDomain k (by linarith) ((p - 1) / 2) f = univ
```

Proved in [lean/OAI/MathematicalPhysics/DefocusingNLS/MainTheorems.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/DefocusingNLS/MainTheorems.lean#L45).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/371.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/371.md)
