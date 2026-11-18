---
declaration: section
origin: cited
lean: OAI.CubicFirstMoment.patterson_firstMoment, OAI.CubicFirstMoment.patterson_angularComparison, OAI.CubicFirstMoment.patterson_angularCancellation
statement: formalized
proof: formalized
---

# 023. Patterson's first moment for cubic Gauss sums

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves unconditionally the all-primary-prime form of Patterson’s first-moment asymptotic: normalized cubic Gauss sums over primary Eisenstein primes of norm at most *X*, including both conjugates, have an explicit positive main term of order $X^{5/6}/\log X$. Every fixed nonzero prime-angle Fourier mode has smaller order.

## An unconditional first moment for cubic Gauss sums

We prove Patterson's first-moment conjecture for normalized cubic Gauss sums over all primary Eisenstein primes, unconditionally. The sharp-cutoff main term is $(6/5)c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. For every fixed nonzero angular Fourier mode of the prime argument, we also prove cancellation at the first-moment scale.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Patterson's first-moment conjecture concerns the average of normalized cubic Gauss sums over primary Eisenstein primes. The formalization proves the sharp-cutoff asymptotic with main term $\frac65c_*X^{5/6}/\log X$, where $c_*=(2\pi)^{2/3}/(3\Gamma(2/3))$. It also proves the corresponding angular comparison for every integer Fourier mode and cancellation of order $o(X^{5/6}/\log X)$ for each fixed nonzero mode. All primary Eisenstein primes are included, without an extra conjectural premise.

## Lean: Patterson first moment and angular cancellation

```lean
theorem patterson_firstMoment : FirstMomentStatement
```

Stated in [PattersonFirstMoment.lean, line 84](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PattersonFirstMoment.lean#L84). Proved in [lean/OAI/NumberTheory/CubicMoment/Theta/CubicThetaMains.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/CubicMoment/Theta/CubicThetaMains.lean#L17).

```lean
theorem patterson_angularComparison : AngularComparisonStatement
```

Stated in [PattersonFirstMoment.lean, line 88](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PattersonFirstMoment.lean#L88). Proved in [lean/OAI/NumberTheory/CubicMoment/Theta/CubicThetaMains.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/CubicMoment/Theta/CubicThetaMains.lean#L10).

```lean
theorem patterson_angularCancellation : AngularCancellationStatement
```

Stated in [PattersonFirstMoment.lean, line 92](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PattersonFirstMoment.lean#L92). Proved in [lean/OAI/NumberTheory/CubicMoment/Theta/CubicThetaMains.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/CubicMoment/Theta/CubicThetaMains.lean#L13).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/023.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/023.md)
