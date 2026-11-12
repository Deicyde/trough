---
declaration: section
origin: cited
lean: OAI.SKGap.sk_main, OAI.SKRatio.ratio_cutoff, OAI.CriticalSK.critical_mixing_bounds, OAI.CriticalSK.realized_equilibrium_initial_states, OAI.CriticalSK.covariance_and_linear_tests, OAI.CriticalSK.critical_mixing_lower_bounds, OAI.SK.main
statement: formalized
proof: formalized
---

# 227. Critical SK autocorrelation processes and dynamics across the temperature transition

8 manuscripts and 7 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

For zero-field Gaussian SK heat-bath dynamics with rate-one updates per spin, proves worst-start cutoff on the $\log n$ scale for fixed $0\le\beta\lt 1$, mixing time $n^{2/3+o(1)}$ at *β* = 1, and stretched-exponential mixing from a Gibbs-sampled fixed starting configuration for *β* > 1, in probability over disorder. At criticality, rescaled stationary and quench autocorrelation processes have universal random limits for Gaussian and Rademacher disorder; the quench limit relaxes to the stationary limit.

## Universality of critical quench autocorrelations in the Sherrington–Kirkpatrick model

We prove joint functional convergence of the stationary and quench autocorrelations of zero-field Sherrington–Kirkpatrick heat-bath dynamics at inverse temperature *β* = 1, with the same random limit for Gaussian and Rademacher couplings. Each site has a rate-one clock, mean spin autocorrelations are multiplied by $n^{1/3}$, and waiting times and lags are measured in units $n^{2/3}$. The quench starts from independent fair spins, and convergence is uniform on compact sets of positive waiting times and lags. The quench limit is selected by these initial states and relaxes to the stationary limiting autocorrelation as the waiting time tends to infinity.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Universality-of-critical-quench-autocorrelations-in-the-Sherrington-Kirkpatrick-model-October-5-2026/main.pdf).

## Functional universality of critical SK autocorrelations

We prove that the stationary spin autocorrelation of the zero-field Sherrington–Kirkpatrick model at inverse temperature *β* = 1 has a common functional scaling limit for Gaussian and Rademacher couplings. With rate-one heat-bath clocks at every site, time is scaled by $n^{2/3}$ and the mean spin autocorrelation is multiplied by $n^{1/3}$. The functions converge in law uniformly on compact positive-time intervals. Their limiting law is not a point mass: it retains sample-to-sample randomness, and its functions decay to zero at large times.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Functional-universality-of-critical-SK-autocorrelations-October-5-2026/critical-sk-autocorrelations.pdf).

## A spectral gap throughout the high-temperature Sherrington–Kirkpatrick phase

For every fixed inverse temperature $0\lt \beta\lt 1$, we prove that the unscaled spectral gap of single-site heat-bath dynamics for the zero-field Gaussian Sherrington–Kirkpatrick model is bounded away from zero with probability tending to one over the disorder. Equivalently, the Gibbs law satisfies a dimension-free Poincaré inequality for all functions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-spectral-gap-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/main.pdf); the Lean below formalizes results from it.

## Cutoff throughout the high-temperature Sherrington–Kirkpatrick phase

We prove worst-case total-variation cutoff for the zero-field Gaussian Sherrington–Kirkpatrick heat-bath dynamics at every fixed inverse temperature $0\leq\beta\lt 1$. With rate-one refresh at each spin, the cutoff location is $\log n/(2\lambda(\beta))$ for a positive deterministic rate $\lambda(\beta)$. The location for uniformly chosen single-site update attempts is *n* times as large. Convergence is in probability over the disorder.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Critical slowing down in the Sherrington–Kirkpatrick model

At the critical inverse temperature *β* = 1, we prove slow mixing for zero-field Gaussian Sherrington–Kirkpatrick heat-bath dynamics from typical equilibrium configurations held fixed as initial states. For every deterministic sequence $t_n=o(n^{2/3})$ in rate-one-per-site time, the Gibbs mass of initial states whose time-$t_{n}$ total-variation distance from equilibrium exceeds 1/4 tends to one in probability over the disorder. The same statement holds for every deterministic integer sequence $k_n=o(n^{5/3})$ of uniform-site update attempts.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Stretched-exponential barriers for typical SK initial states

At every fixed inverse temperature *β* > 1, we prove a stretched-exponential obstruction to mixing for the zero-field Sherrington–Kirkpatrick model from typical equilibrium configurations held fixed as initial states. The Gibbs mass of states whose total-variation distance from equilibrium at time $\exp(n^{1/10000})$ exceeds 1/4 tends to one in probability over the disorder. This holds for rate-one-per-site heat-bath dynamics and after the same stated number of discrete update attempts.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Stretched-exponential-barriers-for-typical-SK-initial-states-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## A typical-start upper bound for low-temperature SK Glauber dynamics

For every fixed inverse temperature *β* > 1, we prove subexponential mixing for rate-one-per-site heat-bath dynamics in the zero-field Gaussian Sherrington–Kirkpatrick model from a typical equilibrium configuration. If one Gibbs-sampled configuration is held fixed as the initial state, its total-variation distance from equilibrium is at most 1/4 by time $\exp(n^{1-1/40000000})$, with joint probability tending to one over the disorder and the sampled state.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-typical-start-upper-bound-for-low-temperature-SK-Glauber-dynamics-September-24-2026/paper.pdf).

## Critical mixing in the Sherrington–Kirkpatrick model

At the critical inverse temperature *β* = 1, we determine the worst-start total-variation mixing exponent for single-site heat-bath dynamics in the zero-field Gaussian Sherrington–Kirkpatrick model. The mixing time is $n^{2/3+o(1)}$ when every site has rate one, or $n^{5/3+o(1)}$ attempted uniform-site updates, in probability over the disorder.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Critical-mixing-in-the-Sherrington-Kirkpatrick-model-September-25-2026/paper.pdf).

## The Lean formalization

For every fixed inverse temperature $0<\beta<1$, the formalization proves a dimension-independent Poincaré inequality for the zero-field Gaussian Sherrington–Kirkpatrick model with probability tending to one over the disorder. Equivalently, the unscaled single-site heat-bath spectral gap stays bounded away from zero. For dynamics that choose one site uniformly at each discrete step, the spectral gap is at least $1/(Cn)$ with probability tending to one, for a constant $C$ depending on $\beta$.

The formalized supporting result proves ratio cutoff for discrete single-site heat-bath dynamics in the zero-field Gaussian Sherrington–Kirkpatrick model for $0\le\beta<1/2$. For every $0<\varepsilon<1/2$ and $\eta>0$, the probability over the disorder that $t_{\mathrm{mix}}(\varepsilon)/t_{\mathrm{mix}}(1-\varepsilon)>1+\eta$ tends to zero as $n\to\infty$. The denominator is positive for all sufficiently large sizes.

The paper's full range $\beta<1$, explicit cutoff location, and continuous-time conclusion are outside this selected statement.

At criticality in the zero-field Sherrington–Kirkpatrick model, the formalization proves that for every fixed $\varepsilon>0$, the continuous-time mixing time lies between $n^{2/3-\varepsilon}$ and $e^{\varepsilon n}$, and the discrete-time mixing count lies between $n^{5/3-\varepsilon}$ and $e^{\varepsilon n}$, with probability tending to one over the Gaussian disorder. The disorder has independent off-diagonal entries of variance $1/n$. Continuous updates have rate one per site; discrete time counts uniformly chosen single-site update attempts. Mixing is worst-start total variation at threshold $1/4$, with holding allowed.

For deterministic times $t_n=o(n^{2/3})$ or update counts $k_n=o(n^{5/3})$, the Gibbs mass of realized starting states still farther than $1/4$ from equilibrium tends to one in probability. For every deterministic positive sequence $M_n\to\infty$, the covariance operator norm and the linear Rayleigh supremum, using the unscaled heat-bath Dirichlet form, both lie between $n^{2/3}/M_n$ and $M_n n^{2/3}$ with probability tending to one. The covariance result does not give an upper bound for the full inverse spectral gap.

The formalization proves a stretched-exponential mixing obstruction for the zero-field Sherrington–Kirkpatrick model at every fixed inverse temperature $\beta>1$. At time $\exp(n^{1/10000})$, the expected Gibbs mass of initial configurations whose total-variation distance from equilibrium exceeds $1/4$ tends to one. Since this mass lies in $[0,1]$, it also tends to one in probability over the disorder.

The result covers both rate-one-per-site continuous-time heat-bath dynamics and the same stated number of discrete update attempts.

## Lean: Spectral-gap bound throughout the high-temperature SK phase

Stated in [SKHighTemperature.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SKHighTemperature.lean).

```lean
theorem sk_main (β : ℝ) (hβ0 : 0 < β) (hβ1 : β < 1) : MainStatement β
```

Proved in [lean/OAI/Probability/SKGap/Main.lean, line 112](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SKGap/Main.lean#L112).

## Lean: Discrete mixing-time ratio cutoff for $\beta<1/2$

Stated in [SKRatio.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SKRatio.lean).

```lean
theorem ratio_cutoff (β ε η : ℝ)
    (hβ0 : 0 ≤ β) (hβhalf : β < 1 / 2)
    (hε0 : 0 < ε) (hεhalf : ε < 1 / 2) (hη : 0 < η) :
    Tendsto
      (fun n : ℕ => disorderLaw β n
        {g : Disorder n | 1 + η <
          (mixingTime g ε : ℝ) / (mixingTime g (1 - ε) : ℝ)})
      atTop (𝓝 0) ∧
    (∀ᶠ n : ℕ in atTop, ∀ g : Disorder n, 0 < mixingTime g (1 - ε))
```

Proved in [lean/OAI/Probability/SKRatio/Main.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SKRatio/Main.lean#L19).

## Lean: Critical SK mixing bounds

Stated in [CriticalSKMixing.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CriticalSKMixing.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem critical_mixing_bounds (ε : ℝ) (hε : 0 < ε) :
    Tendsto (fun n : ℕ => (disorderLaw n {W |
      (n : ℝ) ^ ((2 : ℝ) / 3 - ε) ≤ continuousMixingTime W ∧
      continuousMixingTime W ≤ Real.exp (ε * n)}).toReal) atTop (𝓝 1) ∧
    Tendsto (fun n : ℕ => (disorderLaw n {W |
      (n : ℝ) ^ ((5 : ℝ) / 3 - ε) ≤ (discreteMixingTime W : ℝ) ∧
      (discreteMixingTime W : ℝ) ≤ Real.exp (ε * n)}).toReal) atTop (𝓝 1)
```

Proved in [lean/OAI/MathematicalPhysics/CriticalMixing/Main.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/CriticalMixing/Main.lean#L23).

## Lean: Equilibrium starts, covariance, and mixing lower bounds

Stated in [CriticalSK.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CriticalSK.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem realized_equilibrium_initial_states :
    (∀ t : ℕ → ℝ, (∀ n, 0 ≤ t n) →
      Tendsto (fun n => t n / (n : ℝ) ^ ((2 : ℝ) / 3)) atTop (𝓝 0) →
      ∀ δ : ℝ, 0 < δ →
        Tendsto (fun n => (disorderLaw n {W |
          δ ≤ |continuousGoodMass W (t n) - 1|}).toReal) atTop (𝓝 0)) ∧
    (∀ k : ℕ → ℕ,
      Tendsto (fun n => (k n : ℝ) / (n : ℝ) ^ ((5 : ℝ) / 3)) atTop (𝓝 0) →
      ∀ δ : ℝ, 0 < δ →
        Tendsto (fun n => (disorderLaw n {W |
          δ ≤ |discreteGoodMass W (k n) - 1|}).toReal) atTop (𝓝 0))
```

Proved in [lean/OAI/MathematicalPhysics/CriticalSK/Equilibrium.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/CriticalSK/Equilibrium.lean#L103).

```lean
theorem covariance_and_linear_tests (M : ℕ → ℝ)
    (hMpos : ∀ n, 0 < M n) (hM : Tendsto M atTop atTop) :
    Tendsto (fun n : ℕ => (disorderLaw n {W |
      (n : ℝ) ^ ((2 : ℝ) / 3) / M n ≤ covarianceNorm W ∧
      covarianceNorm W ≤ M n * (n : ℝ) ^ ((2 : ℝ) / 3) ∧
      (n : ℝ) ^ ((2 : ℝ) / 3) / M n ≤ linearRayleigh W ∧
      linearRayleigh W ≤ M n * (n : ℝ) ^ ((2 : ℝ) / 3)}).toReal) atTop (𝓝 1)
```

Proved in [lean/OAI/MathematicalPhysics/CriticalSK/Rayleigh.lean, line 607](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/CriticalSK/Rayleigh.lean#L607).

```lean
theorem critical_mixing_lower_bounds (ε : ℝ) (hε : 0 < ε) :
    Tendsto (fun n => (disorderLaw n).real {W |
      (n : ℝ) ^ (2 / 3 - ε) ≤ continuousMixingTime W}) atTop (𝓝 1) ∧
    Tendsto (fun n => (disorderLaw n).real {W |
      (n : ℝ) ^ (5 / 3 - ε) ≤ (discreteMixingTime W : ℝ)}) atTop (𝓝 1)
```

Proved in [lean/OAI/MathematicalPhysics/CriticalSK/Mixing.lean, line 284](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/CriticalSK/Mixing.lean#L284).

## Lean: Stretched-exponential barriers from typical equilibrium initial states

Stated in [SKBarriers.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SKBarriers.lean).

```lean
theorem main (β : ℝ) (hβ : 1 < β) :
    Tendsto (continuousBadMass β) atTop (𝓝 1) ∧
    Tendsto (discreteBadMass β) atTop (𝓝 1)
```

Proved in [lean/OAI/Probability/SKBarriers/Main.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SKBarriers/Main.lean#L36).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/227.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/227.md)
