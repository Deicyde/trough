---
declaration: section
origin: cited
lean: OAI.ClassicalON.main
statement: formalized
proof: formalized
---

# 215. Canonical $O(3)$ continuum limit and exact $O(4)$ mass asymptotics

5 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs the canonical continuum limit of the two-dimensional nearest-neighbor $O(3)$ model: a non-Gaussian local relativistic theory with a unique vacuum and a positive mass gap. For the square-lattice $O(4)$ model, determines the exact leading asymptotic of the full transfer gap, $m_{\mathrm{lat}}(\beta)\sim32e^{\pi/4-1/2}\sqrt\beta\,e^{-\pi\beta}$. The family also proves exponential spin-correlation decay for two-dimensional nearest-neighbor $O(n)$ models with *n* ≥ 3 at every positive temperature.

## The canonical massive continuum limit of the two-dimensional O(3) model

We construct a canonical interacting massive continuum limit of the two-dimensional nearest-neighbor $O(3)$ model with unit-length spins, no external field, and no topological term. Normalized by susceptibility and second-moment correlation length, the limit exists as the bare coupling tends to infinity through all positive real values, without selecting subsequences. The limiting fields satisfy the Osterwalder–Schrader axioms and have a nonzero connected four-point correlation on separated time supports. Their reconstructed theory has a unique vacuum, a nonzero vacuum complement, and a positive Hamiltonian gap on that entire complement.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-canonical-massive-continuum-limit-of-the-two-dimensional-O3-model-October-4-2026/massive-continuum-o3.pdf).

## An Isolated Particle Pole for the Two-Dimensional O(3) Spin Field

We consider the continuum spin field constructed from the nearest-neighbor two-dimensional $O(3)$ model by the fixed prescription of the companion paper. We prove that its vector two-point spectral measure has a positive atom corresponding to the lowest mass, separated by a positive gap from all remaining mass support.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-Isolated-Particle-Pole-for-the-Two-Dimensional-O3-Spin-Field-October-4-2026/o3-particle-pole.pdf).

## Exact mass asymptotics for the two-dimensional O(4) lattice model

For the nearest-neighbor $O(4)$ model on the square lattice at inverse temperature *β*, we prove the exact low-temperature asymptotic

$\displaystyle m_{\mathrm{lat}}(\beta)\sim 32\exp(\pi/4-1/2)\sqrt\beta\,\exp(-\pi\beta) \qquad (\beta\to\infty).$

Here the mass is the gap of the full Osterwalder–Schrader transfer operator, including rotation-invariant local-observable sectors, in units of one original lattice time step.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-mass-asymptotics-for-the-two-dimensional-O4-lattice-model-October-5-2026/exact-mass-o4.pdf).

## Sharp mass bounds for the two-dimensional O(4) model

We prove sharp mass bounds for the two-dimensional nearest-neighbor $O(4)$ model. For all sufficiently large inverse couplings *β*, the full transfer gap, including rotation-invariant local-observable sectors, is bounded above and below by positive multiples of $\sqrt\beta e^{-\pi\beta}$. We also prove that the model has a unique periodic local limit and a positive full gap at every finite *β* > 0, resolving the all-temperature lattice mass-generation conjecture for this periodic state. Under the stated cutoff scaling, the mass bounds are uniform in independently fixed physical units. A continuum spectral interpretation requires separate convergence hypotheses for the transfer semigroup and the block observables.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf).

## Exponential decay in two-dimensional classical O(n) models

We prove exponential decay of two-point correlations for the classical nearest-neighbor $O(n)$ model on the square lattice, for every *n* ≥ 3 and every finite positive inverse temperature. The estimate is uniform over finite free-boundary subgraphs and bounded nonnegative edge strengths. This resolves positively the all-temperature exponential spin-decay conjecture for these models.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result proves exponential decay of spin correlations for the two-dimensional classical $O(n)$ model at every temperature when $n\ge3$. For each interaction bound $\beta>0$, constants $A$ and $m>0$ work for every finite square-lattice subgraph with free boundary and nonnegative edge strengths at most $\beta$: the correlation between sites $x,y$ is at most $Ae^{-m|x-y|}$. The infinite-volume limit and the separate $O(4)$ spectral-gap claim are not included.

## Lean: Exponential correlation decay for classical $O(n)$ models

Stated in [ClassicalON.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ClassicalON.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : ExponentialDecay
```

Proved in [lean/OAI/Probability/ClassicalON/Main.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ClassicalON/Main.lean#L19).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/215.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/215.md)
