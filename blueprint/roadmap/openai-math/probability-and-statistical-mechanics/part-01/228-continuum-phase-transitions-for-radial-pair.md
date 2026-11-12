---
declaration: section
origin: cited
lean: OAI.ContinuumTemperature.main_theorem, OAI.RadialTransition.main, OAI.RadialTransition.densityInterval
statement: formalized
proof: formalized
---

# 228. Continuum phase transitions for radial pair potentials

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs stable distance-dependent pair interactions for three-dimensional classical particles with a first-order phase transition: the canonical free energy has a derivative jump at one inverse temperature throughout an open density interval. One potential has a divergent repulsive core; another is bounded and continuous with an integrable power-law tail, realizing the type of transition sought in Simon's continuum problem.

## A continuum temperature singularity for a radial pair potential

We construct a stable radial pair potential in three dimensions whose canonical free energy has a strict downward derivative jump at one common finite positive inverse temperature throughout an open interval of positive densities. The potential has a divergent repulsive core, a nontrivial attractive interval, and an integrable tail satisfying $\phi(r)=o(r^{-3})$. Its free-cube canonical free energy is finite at every positive inverse temperature and density.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-continuum-temperature-singularity-for-a-radial-pair-potential-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## A radial continuum phase transition with algebraic decay

We construct a bounded, continuous, stable radial pair potential in three dimensions with $|\phi(r)|\le Cr^{-3-1/32}$ for *r* ≥ 1. Throughout an open interval of positive densities, its canonical thermodynamic free energy is finite at every positive inverse temperature and has a strict downward derivative jump at one common finite positive inverse temperature.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-radial-continuum-phase-transition-with-algebraic-decay-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization constructs one stable radial pair potential in three-dimensional continuum space with a divergent repulsive core and an integrable tail that is $o(r^{-3})$. Its canonical free energy exists for every positive inverse temperature and density. At one inverse temperature $\beta_c\in(1/2,3/2)$, the free energy has a strict finite jump between its one-sided derivatives with respect to inverse temperature, for every density in one nonempty open interval.

The formalization constructs a bounded continuous stable radial pair potential in $\mathbb R^3$ satisfying $|\phi(r)|\le Cr^{-3-1/32}$ for $r\ge1$. There is a nonempty open interval of positive densities around $5p/3$, where $p$ is the unit-separated packing-density limit, on which the canonical free energy exists at every positive inverse temperature and has a strict downward derivative jump at one common $\beta_c\in[7/8,9/8]$.

The earlier fixed-density statement at $5p/3$ is also retained. Both statements concern the derivative with respect to inverse temperature.

## Lean: Temperature singularity over a density interval

Stated in [ContinuumTransition.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContinuumTransition.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_theorem : MainStatement
```

Proved in [lean/OAI/Probability/ContinuumTransition/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ContinuumTransition/Main.lean#L21).

## Lean: Fixed-density radial continuum phase transition

Stated in [RadialTransition.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RadialTransition.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main :
    ∃ (p : ℝ) (φ : Potential) (B C : ℝ) (f : ℝ → ℝ) (βc : ℝ),
      0 < p ∧ IsPackingDensity p ∧
      IsBoundedPotential φ ∧ Continuous φ ∧
      0 < B ∧ 0 < C ∧ StableWith φ B ∧ AlgebraicDecayWith φ C ∧
      IsCanonicalFreeEnergy φ (5*p/3) f ∧
      βc ∈ Icc (7/8:ℝ) (9/8) ∧ StrictTemperatureCorner f βc
```

Proved in [lean/OAI/Probability/RadialTransition/Main.lean, line 53](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/RadialTransition/Main.lean#L53).

## Lean: A common radial phase transition over a density interval

Stated in [RadialDensityInterval.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RadialDensityInterval.lean).

```lean
theorem densityInterval :
    ∃ (p : ℝ) (φ : Potential) (B C η βc : ℝ) (f : ℝ → ℝ → ℝ),
      0 < p ∧ IsPackingDensity p ∧
      IsBoundedPotential φ ∧ Continuous φ ∧
      0 < B ∧ 0 < C ∧ StableWith φ B ∧ AlgebraicDecayWith φ C ∧
      0 < η ∧ Ioo (5*p/3 - η) (5*p/3 + η) ⊆ Ioi 0 ∧
      βc ∈ Icc (7/8:ℝ) (9/8) ∧
      ∀ ρ ∈ Ioo (5*p/3 - η) (5*p/3 + η),
        IsCanonicalFreeEnergy φ ρ (fun β => f β ρ) ∧
        StrictTemperatureCorner (fun β => f β ρ) βc
```

Proved in [lean/OAI/Probability/RadialTransition/DensityInterval.lean, line 33](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/RadialTransition/DensityInterval.lean#L33).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/228.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/228.md)
