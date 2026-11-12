---
declaration: section
origin: cited
lean: OAI.IsingPerceptron.variationalValue_real_of_continuous, OAI.SphericalPerceptronFreeEnergy.main, OAI.SphericalPerceptron.spherical_linear_field_formula
statement: formalized
proof: formalized
---

# 222. Perceptron free energies and microscopic jamming exponents

4 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines finite-temperature variational free energies for Gaussian Ising perceptrons with bounded Borel log-potentials and Gaussian spherical perceptrons with bounded continuous potentials, at every positive pattern density. A spherical extension treats bi-orthogonally invariant disorder with compact limiting singular-value distributions and no outliers. At margin −1, the quadratic-penalty spherical model has a sharp feasibility threshold and limiting gap and force laws, with system size, zero temperature, and critical density taken in that order.

## The free energy of the Ising random perceptron

We determine the limiting free energy of the Ising perceptron with independent Gaussian patterns for every bounded Borel log-potential, at every fixed positive temperature and pattern density. We give an explicit variational formula for the limit and prove convergence in expectation and probability.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-free-energy-of-the-Ising-random-perceptron-September-24-2026/The-free-energy-of-the-Ising-random-perceptron-September-24-2026.pdf); the Lean below formalizes results from it.

## Microscopic jamming in the negative spherical perceptron

We prove a sharp feasibility threshold and limiting gap and force laws for the spherical perceptron with margin −1 and quadratic penalty. The limits are taken successively in system size, inverse temperature, and density approaching the threshold from above. They agree for Gaussian coordinates and for the equal mixture of centered Gaussian coordinates with variances $1-\varepsilon$ and $1+\varepsilon$, for every sufficiently small fixed *ε*. The contact-removed gap cumulative law and the mean-one force cumulative law satisfy

$\displaystyle G_J(u)=u^{1-\gamma+o(1)},\qquad F_J(s)=s^{1+\theta+o(1)},$

as $u\downarrow0$ and $s\downarrow0$, with $\gamma=(2+\theta)^{-1}$, $0.4126930\lt \gamma\lt 0.4126934$, and $0.4231063\lt \theta\lt 0.4231088$. A finite numerical certificate for these exponent intervals, together with its mathematical error bounds, is included.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026/Microscopic-jamming-in-the-negative-spherical-perceptron-September-24-2026.pdf).

## The spherical perceptron with bi-orthogonally invariant disorder

We determine the limiting free energy of a spherical perceptron with a bounded continuous activation and a bi-orthogonally invariant disorder matrix. The singular values may have any compact limiting distribution, provided there are no outliers. We give an explicit variational formula for this limit.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026/The-spherical-perceptron-with-bi-orthogonally-invariant-disorder-September-24-2026.pdf).

## The free energy of the spherical random perceptron

We prove an exact variational formula for the limiting pressure of the spherical random perceptron with an arbitrary bounded continuous single-pattern potential. The formula holds at every fixed positive density and inverse temperature, with convergence in expectation and in probability.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-free-energy-of-the-spherical-random-perceptron-September-24-2026/The-free-energy-of-the-spherical-random-perceptron-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The linked formalization proves finiteness of the variational value used for the Ising random perceptron. For every nonnegative pattern density and every bounded continuous log-potential, the infimum over admissible overlap paths is a finite real number.

This is a supporting well-definedness result. It does not assert convergence of the finite-system pressure or the paper's extension to all bounded Borel log-potentials.

The formalization proves the variational formula for the spherical random perceptron's limiting pressure for every positive pattern density and inverse temperature and every bounded continuous single-pattern potential. It shows that the variational value is finite and that the pressure converges to it both in expectation and in probability.

The linked spherical-field result supplies a supporting dual formula: finite hierarchy field values converge uniformly on compact parameter sets to an attained dual minimum, and the corresponding bounded stationary-field approximation holds for monotone overlap quantiles bounded away from one.

## Lean: Finiteness of the Ising-perceptron variational value

Stated in [IsingFiniteness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IsingFiniteness.lean).

```lean
theorem variationalValue_real_of_continuous {α : ℝ} (hα : 0 ≤ α)
    {f : ℝ → ℝ} (hf : Continuous f) (hbounded : ∃ K : ℝ, ∀ x, |f x| ≤ K) :
    ∃ p : ℝ, variationalValue α f = (p : EReal)
```

Proved in [lean/OAI/Probability/IsingPerceptron/VariationalFiniteness.lean, line 196](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/IsingPerceptron/VariationalFiniteness.lean#L196).

## Lean: Variational formula for spherical-perceptron pressure

Stated in [PerceptronFreeEnergy.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PerceptronFreeEnergy.lean).

```lean
theorem main (P : Measure BrownianPath) [IsProbabilityMeasure P]
    (hB : IsBrownianReal brownianEval P)
    (α β : ℝ) (hα : 0 < α) (hβ : 0 < β) (φ : ℝ →ᵇ ℝ) :
    ∃ p : ℝ, variationalValue P α β φ = (p : EReal) ∧
      Tendsto (fun N : ℕ => expectedPressure α β φ (N + 1)) atTop (𝓝 p) ∧
      ∀ ε : ℝ, 0 < ε →
        Tendsto (fun N : ℕ => patternLaw α (N + 1)
          {g | ε < |pressure α β φ (N + 1) g - p|}) atTop (𝓝 0)
```

Proved in [lean/OAI/Probability/Perceptron/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/Perceptron/Main.lean#L21).

## Lean: Spherical linear-field dual formula and approximation

Stated in [SphericalField.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SphericalField.lean).

```lean
theorem spherical_linear_field_formula : SphericalLinearFieldFormula
```

Proved in [lean/OAI/Probability/SphericalField/Main.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SphericalField/Main.lean#L26).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/222.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/222.md)
