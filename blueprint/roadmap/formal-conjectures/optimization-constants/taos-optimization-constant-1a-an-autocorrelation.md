---
declaration: theorem
origin: cited
lean: Constant1a.c1a_lower_bound, Constant1a.c1a_upper_bound, Constant1a.mem_Ico_c1a, Constant1a.mem_Ioc_c1a, Constant1a.c1a_eq
statement: formalized
---

# Tao's Optimization constant 1a / An autocorrelation constant related to Sidon sets

> *References:*
> - [Tao's optimization constant 1a](https://teorth.github.io/optimizationproblems/constants/1a.html)
> - [M2010] Matolcsi, Máté, and Carlos Vinuesa. "Improved bounds on the supremum of autoconvolutions."
>   Journal of mathematical analysis and applications 372.2 (2010): 439-447. [arXiv:0907.1379](https://arxiv.org/abs/0907.1379)
> - [Y2026] Yuksekgonul, Mert et al., "Learning to Discover at Test Time," 2026, [arXiv:2601.16175](https://arxiv.org/abs/2601.16175)
> - [T2026] Together AI, "EinsteinArena-new-SOTA: State-of-the-art results on open math problems,"
>   2026, [GitHub](https://github.com/togethercomputer/EinsteinArena-new-SOTA)
> - [PBV2026] Piterbarg, Andrei, Jai Bajaj, and Derrick Vincent. "A multi-scale arcsine lower bound
>   for the Sidon autocorrelation constant $C_{1a}$," 2026,
>   [GitHub](https://github.com/AndreiPiterbarg/sidon-autocorrelation)

*Quoted from [FormalConjectures/OptimizationConstants/1a.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open and 2 solved.

## `Constant1a.c1a_lower_bound`

Solved: stated here without proof.

> A lower bound, proven by Matolcsi-Vinuesa in [M2010].

```lean
theorem c1a_lower_bound : 1.2748 ≤ C1a
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/1a.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean#L58).

## `Constant1a.c1a_upper_bound`

Solved: stated here without proof.

> An upper bound, proven by Yuksekgonul et al. in [Y2026].

```lean
theorem c1a_upper_bound : C1a ≤ 1.5029
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/1a.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean#L63).

## `Constant1a.mem_Ico_c1a`

Open: stated without proof.

> How can the best known upper bound $1.5028628587\ldots$ of [T2026] be improved?
>
> The step function published with [T2026] gives $1.50286285870\ldots$. The figure $1.502862$ in
> the table of the first reference is this value truncated, so it is not a known upper bound.

```lean
theorem mem_Ico_c1a : mem_Ico_c1a.answer ∈ Set.Ico C1a 1.5028628587
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/1a.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean#L73).

## `Constant1a.mem_Ioc_c1a`

Open: stated without proof.

> How can the best known lower bound $1.292$ of [PBV2026] be improved?

```lean
theorem mem_Ioc_c1a : mem_Ioc_c1a.answer ∈ Set.Ioc 1.292 C1a
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/1a.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean#L80).

## `Constant1a.c1a_eq`

Open: stated without proof.

> What is the exact value of the constant?

```lean
theorem c1a_eq : C1a = c1a_eq.answer
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/OptimizationConstants/1a.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OptimizationConstants/1a.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/1a.lean)
- [Tao's optimization constant 1a](https://teorth.github.io/optimizationproblems/constants/1a.html)
