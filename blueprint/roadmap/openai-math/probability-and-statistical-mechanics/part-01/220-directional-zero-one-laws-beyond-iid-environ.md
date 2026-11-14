---
declaration: section
origin: cited
lean: OAI.DirectionalZeroOne.directional_zero_one, OAI.DirectionalTransience.directional_transience_implies_ballisticity, OAI.DirectionalTransience.positive_probability_transience_velocity_hemisphere
statement: formalized
proof: formalized
---

# 220. Directional zero–one laws beyond iid environments and iid ballisticity

3 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

On ℤ$^{d}$, *d* ≥ 3, directional escape has probability zero or one for iid strictly elliptic nearest-neighbor environments, and for stationary ergodic finite-range-dependent environments under uniform ellipticity. In iid uniformly elliptic environments with *d* ≥ 2, almost-sure directional transience implies a deterministic limiting velocity with positive projection in that direction, resolving the ballisticity conjecture.

## A directional zero–one law for finite-range-dependent random environments

We prove a directional zero–one law for uniformly elliptic nearest-neighbor random walks in stationary, ergodic, finite-range-dependent environments on ℤ$^{d}$, *d* ≥ 3. For every fixed nonzero real direction, the probability of escape in that direction, averaged over the environment, is either zero or one. Finite-range dependence is imposed on the full transition rows: collections of rows at distance greater than a fixed range are independent, including collections indexed by infinite deterministic sets.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-directional-zero-one-law-for-finite-range-dependent-random-environments-October-5-2026/directional-zero-one-finite-range.pdf).

## A directional zero–one law under strict ellipticity

We prove the directional zero–one conjecture for nearest-neighbor random walks in independent and identically distributed strictly elliptic environments on ℤ$^{d}$, *d* ≥ 3: the probability of escape in each fixed nonzero real direction is zero or one. Only strict positivity of the transition probabilities is required; no uniform lower bound or moment assumption is imposed.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-directional-zero-one-law-under-strict-ellipticity-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Directional transience implies ballisticity

We prove that almost-sure transience in a fixed direction implies a deterministic limiting velocity with positive projection in that direction for nearest-neighbor random walks in independent and identically distributed uniformly elliptic environments on ℤ$^{d}$, *d* ≥ 2. This resolves the ballisticity conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Directional-transience-implies-ballisticity-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The directional zero–one conjecture asks whether a random walk's probability of escape in a fixed direction must be zero or one. The formalization proves this for nearest-neighbor walks in independent identically distributed strictly elliptic environments on $\mathbb Z^d$, for every $d\ge3$ and every nonzero real direction. Strict ellipticity means that every allowed transition probability is positive almost surely; no uniform positive lower bound or moment condition is assumed. The probability is the annealed law from the origin.

For an i.i.d. uniformly elliptic nearest-neighbor random environment on $\mathbb Z^d$, the formalization proves that almost-sure directional transience implies convergence of $X_n/n$ to a deterministic velocity with positive projection in that direction for every $d\ge2$.

For $d\ge3$, positive probability of transience in any nonzero direction already suffices. The limiting velocity is unique, and the unit directions with positive transience probability are exactly the open hemisphere having positive inner product with that velocity; transience has probability one on that hemisphere and zero on its complement. The environment is sampled once and retained along the walk, and the probabilities use the annealed law from the origin.

## Lean: Directional zero–one law under strict ellipticity

```lean
theorem directional_zero_one (d : ℕ) (hd : 3 ≤ d)
    (μ : Measure (Row d)) [IsProbabilityMeasure μ]
    (hell : StrictEllipticity μ) (ℓ : Fin d → ℝ) (hℓ : ℓ ≠ 0) :
    annealed μ 0 (escape ℓ) = 0 ∨ annealed μ 0 (escape ℓ) = 1
```

Stated in [DirectionalWalk.lean, line 85](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DirectionalWalk.lean#L85). Proved in [lean/OAI/Probability/DirectionalWalk/Main.lean, line 121](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/DirectionalWalk/Main.lean#L121).

## Lean: Directional transience implies ballisticity

```lean
theorem directional_transience_implies_ballisticity : MainStatement
```

Stated in [DirectionalBallisticity.lean, line 95](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DirectionalBallisticity.lean#L95). Proved in [lean/OAI/Probability/Ballisticity/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/Ballisticity/Main.lean#L25). formalization.yaml lists it as one of the repository's main results.

## Lean: Positive-probability transience and the velocity hemisphere

```lean
theorem positive_probability_transience_velocity_hemisphere
    {d : ℕ} (hd : 3 ≤ d) (ν : Measure (Row d)) [IsProbabilityMeasure ν]
    (hue : UniformElliptic ν) (ℓ : Vector d) (hℓ : ℓ ≠ 0)
    (hpos : 0 < annealedLaw ν (TransientPaths ℓ)) :
    ∃ v : Vector d,
      v ≠ 0 ∧ 0 < dot v ℓ ∧ annealedLaw ν (VelocityPaths v) = 1 ∧
      (∀ w : Vector d, annealedLaw ν (VelocityPaths w) = 1 → w = v) ∧
      {u : Vector d | dot u u = 1 ∧ annealedLaw ν (TransientPaths u) = 1} =
        {u : Vector d | dot u u = 1 ∧ 0 < annealedLaw ν (TransientPaths u)} ∧
      {u : Vector d | dot u u = 1 ∧ 0 < annealedLaw ν (TransientPaths u)} =
        {u : Vector d | dot u u = 1 ∧ 0 < dot v u} ∧
      (∀ u : Vector d, dot u u = 1 → dot v u ≤ 0 →
        annealedLaw ν (TransientPaths u) = 0)
```

Stated in [VelocityHemisphere.lean, line 85](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/VelocityHemisphere.lean#L85). Proved in [lean/OAI/Probability/Ballisticity/VelocityHemisphere.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/Ballisticity/VelocityHemisphere.lean#L10).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/220.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/220.md)
