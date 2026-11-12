---
declaration: section
origin: cited
lean: OAI.BoltzmannNonuniqueness.nonuniqueness
statement: formalized
proof: formalized
---

# 363. Nonuniqueness with local conservation for the hard-sphere Boltzmann equation

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs two distinct global entropy solutions of the three-dimensional periodic hard-sphere Boltzmann equation from the same nonnegative initial density, with bounded velocity support and finite mass, energy and absolute entropy. Both are strongly continuous in $L^{1}$ and satisfy exact local conservation of mass, momentum and kinetic energy.

## Nonuniqueness with local conservation for the hard-sphere Boltzmann equation

We prove nonuniqueness for the three-dimensional periodic hard-sphere Boltzmann equation among global entropy solutions satisfying exact local conservation of mass, momentum, and kinetic energy. We construct one nonnegative initial density with bounded velocity support and finite mass, energy, and absolute entropy that gives rise to two distinct such solutions. Both are strongly continuous in $L^{1}$, and their collision gain and loss terms are integrable with every polynomial velocity weight on every bounded time interval.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nonuniqueness-with-local-conservation-for-the-hard-sphere-Boltzmann-equation-October-5-2026/paper.pdf).

## Nonuniqueness for the periodic hard-sphere Boltzmann equation

We prove nonuniqueness for the periodic hard-sphere Boltzmann equation by constructing two distinct global renormalized solutions with the same nonnegative initial density on $\mathbb T^3\times\mathbb R^3$. This density has bounded velocity support and finite mass, energy, and absolute entropy. Both solutions conserve local mass and total momentum and satisfy the global energy and entropy-dissipation inequalities. On a common initial interval, they are strongly continuous in $L^{1}$, and their collision gains and losses are integrable.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Nonuniqueness-for-the-periodic-hard-sphere-Boltzmann-equation-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves nonuniqueness for the periodic hard-sphere Boltzmann equation by constructing two distinct global renormalized solutions on $\mathbb T^3\times\mathbb R^3$ with the same nonnegative initial density. The data have bounded velocity support and finite mass, energy, and absolute entropy. Both solutions conserve local mass and total momentum and satisfy the global energy and entropy-dissipation inequalities.

On a common initial interval they are strongly continuous in $L^1$, with integrable collision gains and losses. These are the conditions of the selected periodic result; later local-conservation refinements are outside it.

## Lean: Two periodic hard-sphere Boltzmann solutions with the same data

Stated in [BoltzmannNonuniqueness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BoltzmannNonuniqueness.lean).

```lean
theorem nonuniqueness :
    ∃ f₀ : Density, BoundedVelocitySupport f₀ ∧
      ∃ (F G : Evolution) (T : ℝ), AdmissibleGlobal f₀ F ∧ AdmissibleGlobal f₀ G ∧
        StrongEarly T F ∧ StrongEarly T G ∧
        ∃ t ∈ Set.Icc 0 T, ¬(F t =ᵐ[MeasureTheory.volume] G t)
```

Proved in [lean/OAI/MathematicalPhysics/Boltzmann/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Boltzmann/Main.lean#L13).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/363.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/363.md)
