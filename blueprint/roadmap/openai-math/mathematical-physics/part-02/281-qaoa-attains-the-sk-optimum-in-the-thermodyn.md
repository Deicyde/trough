---
declaration: section
origin: cited
lean: OAI.SKValue.value_consequences, OAI.ZeroTemperatureSK.full_support
statement: formalized
proof: formalized
---

# 281. QAOA attains the SK optimum in the thermodynamic-first limit

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that QAOA approaches the ground-state energy of the Gaussian zero-field Sherrington–Kirkpatrick model when system size tends to infinity before circuit depth. For every accuracy, finite depth and deterministic angles independent of size and disorder achieve the required limiting expected energy per spin. This also yields leading-order optimal expected MaxCut values on large-degree random regular graphs, with size tending to infinity before degree.

## QAOA attains the SK ground-state energy in the thermodynamic-first limit

We prove that the Quantum Approximate Optimization Algorithm (QAOA) approaches the ground-state energy per spin of the Gaussian zero-field Sherrington–Kirkpatrick model when system size tends to infinity first and circuit depth then increases. For every accuracy, some finite depth and deterministic angles, independent of system size and disorder, achieve that accuracy in the limiting expected energy per spin using the standard cost Hamiltonian and transverse-field mixer. This proves the eventual Parisi-optimality conjecture of Basso, Farhi, Marwaha, Villalonga, and Zhou in its fixed-parameter thermodynamic formulation. We give no quantitative bound on the required depth or efficient angle-selection procedure.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf); the Lean below formalizes results from it.

## Full support of the zero-temperature Sherrington-Kirkpatrick order parameter

We prove that every admissible integrable minimizer of the zero-temperature Parisi functional for the pure, zero-field Sherrington–Kirkpatrick model has full relative Stieltjes support on $[0,1)$. Thus its support has no gaps at any overlap scale below one. We use the covariance normalization $\xi(t)=t^2/2$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The linked formalization supplies variational identities for the Gaussian zero-field Sherrington–Kirkpatrick ground-state energy used in the paper's QAOA argument. Conditional on an admissible Parisi minimizer and its associated diffusion, it proves convergence of the finite-system ground-state energy, identifies its limit with the Parisi value, and gives equivalent terminal-martingale and integrated-curvature formulas.

It also proves convergence of finite Gaussian coefficient sums to the curvature integral, which approaches the ground-state value as the terminal time tends to one. The selected statement covers these value and approximation results; it does not itself assert convergence of QAOA circuit energies.

The formalization proves that every admissible integrable minimizer of the zero-temperature Parisi functional for the pure zero-field Sherrington–Kirkpatrick model has full relative Stieltjes support on $[0,1)$. Equivalently, the order parameter increases strictly between every two overlap values below one, so its support has no gap. The covariance normalization is $\xi(t)=t^2/2$.

The statement also constructs the associated diffusion and proves its selected self-consistency moment identities. It is conditional on the order parameter being a minimizer and does not separately assert existence of a minimizer.

## Lean: Parisi ground-state value identities and finite Gaussian approximation

```lean
theorem value_consequences :
    (∀ (W : BrownianSpace) (γ : OrderParameter) (X : ℝ → W.Ω → ℝ),
      IsMinimizer W γ → IsDiffusion W γ X → ScalarValueConclusion W γ X) ∧
    (∀ (W : BrownianSpace) (γ : OrderParameter) (X : ℝ → W.Ω → ℝ) (T : ℝ),
      0 < T → T < 1 → IsMinimizer W γ → IsDiffusion W γ X →
      FiniteGaussianConclusion W γ X T) ∧
    (∀ (W : BrownianSpace) (γ : OrderParameter),
      IsMinimizer W γ → groundStateValue = parisi W γ)
```

Stated in [SKValue.lean, line 163](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SKValue.lean#L163). Proved in [lean/OAI/Probability/SKValue/Main.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SKValue/Main.lean#L16).

## Lean: Full support of zero-temperature SK minimizers

```lean
theorem full_support (W : BrownianSystem Ω) (γ : OrderParameter)
    (hmin : IsMinimizer W γ) : FullSupportConclusion W γ
```

Stated in [SKFullSupport.lean, line 90](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SKFullSupport.lean#L90). Proved in [lean/OAI/Probability/SKSupport/Main.lean, line 35](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SKSupport/Main.lean#L35).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/281.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/281.md)
