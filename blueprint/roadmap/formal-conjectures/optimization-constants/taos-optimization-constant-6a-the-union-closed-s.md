---
declaration: theorem
origin: cited
lean: Constant6a.c6a_eq_half, Constant6a.c6a_upper_bound, Constant6a.c6a_upper_bound_improved, Constant6a.c6a_lower_bound_first, Constant6a.c6a_lower_bound_intermediate, Constant6a.c6a_lower_bound, Constant6a.c6a_lower_bound_improved
statement: formalized
---

# Tao's Optimization Constant 6a / The Union-Closed Sets Conjecture

> *References:*
> - [Tao's Optimization Constant 6a](https://teorth.github.io/optimizationproblems/constants/6a.html)
> - [F1995] Frankl, P., *Extremal set systems*. Handbook of Combinatorics (1995).
> - [AHS2022] Alweiss, R., Huang, B. and Sellke, M., *Improved lower bound for the union-closed sets
>   conjecture*. [arXiv:2211.11731](https://arxiv.org/abs/2211.11731)
> - [CL2022] Chase, Z. and Lovett, S., *Approximate union closed conjecture*.
>   [arXiv:2211.11689](https://arxiv.org/abs/2211.11689)
> - [S2022] Sawin, W., *An improved lower bound for the union-closed set conjecture*.
>   [arXiv:2211.11504](https://arxiv.org/abs/2211.11504)
> - [C2022] Cambie, S., *Better bounds for the union-closed sets conjecture using the entropy
>   approach*. [arXiv:2212.12500](https://arxiv.org/abs/2212.12500)
> - [Y2022] Yu, L., *Dimension-free bounds for the union-closed sets conjecture*.
>   [arXiv:2212.00658](https://arxiv.org/abs/2212.00658)
> - [L2023] Liu, J., *Improving the lower bound for the union-closed sets conjecture via
>   conditionally IID coupling*. [arXiv:2306.08824](https://arxiv.org/abs/2306.08824)

*Quoted from [FormalConjectures/OptimizationConstants/6a.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 3 open and 4 solved.

## `Constant6a.c6a_eq_half`

Open: stated without proof.

> The union-closed sets conjecture of Frankl: $C_{6a} = 1/2$.

```lean
theorem c6a_eq_half : C6a = 1 / 2
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L56).

## `Constant6a.c6a_upper_bound`

Solved: stated here without proof.

> The upper bound $C_{6a} \le 1/2$ [F1995]. It holds because in the family of all subsets of a
> finite set, every element belongs to exactly half of the sets.

```lean
theorem c6a_upper_bound : C6a ≤ 1 / 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L62).

## `Constant6a.c6a_upper_bound_improved`

Open: stated without proof.

> Can the best known upper bound $1/2$ be improved?

```lean
theorem c6a_upper_bound_improved : C6a < 1 / 2
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L67).

## `Constant6a.c6a_lower_bound_first`

Solved: stated here without proof.

> The first lower bound, $(3 - \sqrt 5) / 2$, proved independently in [AHS2022], [CL2022] and
> [S2022].

```lean
theorem c6a_lower_bound_first : (3 - Real.sqrt 5) / 2 ≤ C6a
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L73).

## `Constant6a.c6a_lower_bound_intermediate`

Solved: stated here without proof.

> An intermediate lower bound, proved in [C2022] and [Y2022].

```lean
theorem c6a_lower_bound_intermediate : 0.38234 ≤ C6a
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L78).

## `Constant6a.c6a_lower_bound`

Solved: stated here without proof.

> The best known lower bound, proved by Liu in [L2023].

```lean
theorem c6a_lower_bound : 0.38271 ≤ C6a
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L83).

## `Constant6a.c6a_lower_bound_improved`

Open: stated without proof.

> Can the best known lower bound $0.38271$ of [L2023] be improved?

```lean
theorem c6a_lower_bound_improved : 0.38272 < C6a
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/OptimizationConstants/6a.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OptimizationConstants/6a.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OptimizationConstants/6a.lean)
- [Tao's Optimization Constant 6a](https://teorth.github.io/optimizationproblems/constants/6a.html)
