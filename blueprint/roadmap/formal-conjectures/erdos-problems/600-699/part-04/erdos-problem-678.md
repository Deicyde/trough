---
declaration: theorem
origin: cited
lean: Erdos678.erdos_678, Erdos678.erdos_678.variants.infinitely_many_triples, Erdos678.erdos_678.variants.not_infinitely_many_pairs
statement: formalized
---

# Erdős Problem 678

> *References:*
> - [erdosproblems.com/678](https://www.erdosproblems.com/678)
> - [Ca24] S. Cambie, Resolution of an Erdős' problem on least common multiples. arXiv:2410.09138
>   (2024).
> - [Er79] Erdős, Paul, Some unconventional problems in number theory. Math. Mag. (1979), 67-70.
> - [Er92e] Erdős, Pál, Some Unsolved problems in Geometry, Number Theory and Combinatorics. Eureka
>   (1992), 44-48.

*Quoted from [FormalConjectures/ErdosProblems/678.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/678.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/678](https://www.erdosproblems.com/678).

The file states 3 research or textbook statements: 3 solved. It also has 4 test statements, counted here but not shown.

## `Erdos678.erdos_678`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos678.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos678.lean).

> Write $M(n, k)$ be the least common multiple of $\{n+1, \dotsc, n+k\}$.
> Let $k$ be sufficiently large. Are there infinitely many $m, n$ with $m \geq n + k$ such that
>
> $$
> M(n, k) > M(m, k + 1)
> $$
>
> ?
> The answer is yes, as proved in a strong form by Cambie [Ca24].
> [Ca24] S. Cambie, Resolution of an Erdős' problem on least common multiples. arXiv:2410.09138 (2024).
>
> This was formalized in Lean by Alexeev using Aristotle, on top of the PNT+ project.
>
> For a fixed $k$ there are only finitely many such pairs, so "infinitely many" is read here as
> ranging over $k$ as well: for every sufficiently large $k$ at least one pair $(m, n)$ occurs.
> See `erdos_678.variants.infinitely_many_triples` for the reading in which the infinitude is
> stated directly, and `erdos_678.variants.not_infinitely_many_pairs` for why it cannot be asked
> of a single $k$.

```lean
theorem erdos_678 :
    ∀ᶠ k in atTop, {(m, n) | n + k ≤ m ∧ lcmInterval m (k + 1) < lcmInterval n k}.Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/678.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/678.lean#L86).

## `Erdos678.erdos_678.variants.infinitely_many_triples`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos678.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos678.lean).

> The pairs $(m, n)$ with $m \geq n + k$ and $M(n, k) > M(m, k + 1)$ are infinite in number once
> $k$ is allowed to vary, which is the sense in which Cambie's result answers the question.

```lean
theorem erdos_678.variants.infinitely_many_triples :
    {(k, m, n) | 3 ≤ k ∧ n + k ≤ m ∧ lcmInterval m (k + 1) < lcmInterval n k}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/678.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/678.lean#L96).

## `Erdos678.erdos_678.variants.not_infinitely_many_pairs`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos678.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos678.lean).

> For a fixed sufficiently large $k$ only finitely many pairs occur: $M(m, k + 1) \geq m + 1$
> bounds $m$ by $M(n, k)$, and for large $n$ the inequality reverses. So the question cannot be
> read as asking for infinitely many pairs at a single $k$.

```lean
theorem erdos_678.variants.not_infinitely_many_pairs :
    ¬ ∀ᶠ k in atTop, {(m, n) | n + k ≤ m ∧ lcmInterval m (k + 1) < lcmInterval n k}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/678.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/678.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/678.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/678.lean)
- [erdosproblems.com/678](https://www.erdosproblems.com/678)
