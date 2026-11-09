---
declaration: theorem
origin: cited
lean: Erdos188.erdos_188, Erdos188.erdos_188.variants.nonempty, Erdos188.erdos_188.variants.estimate
statement: formalized
---

# Erdős Problem 188

> *References:*
> - [erdosproblems.com/188](https://www.erdosproblems.com/188)
> - [EGMRSS75] Erdős, P. and Graham, R. L. and Montgomery, P. and Rothschild, B. L. and Spencer, J.
>   and Straus, E. G., Euclidean {R}amsey theorems. {II}. (1975), 529--557.
> - [Ts17] Tsaturian, Sergei, A {E}uclidean {R}amsey result in the plane. Electron. J. Combin. (2017),
>   Paper No. 4.35, 9.

*Quoted from [FormalConjectures/ErdosProblems/188.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/188.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/188](https://www.erdosproblems.com/188).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos188.erdos_188`

Open: stated without proof.

> What is the smallest $k$ such that $\mathbb{R}^2$ can be red/blue coloured with no pair of red
> points unit distance apart, and no $k$-term arithmetic progression of blue points with distance 1?

```lean
theorem erdos_188 : IsLeast s erdos_188.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/188.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/188.lean#L50).

## `Erdos188.erdos_188.variants.nonempty`

Solved: stated here without proof.

> Old and new problems and results in combinatorial number theory by Erdős & Graham (Page 14, 15):
>
> It has been shown that there is a large $M$ so that it is possible to partition $\mathbb{E}^2$ into
> two sets $A$ and $B$ so that $A$ contains no pair of points with distance 1 and $B$ contains no A.P.
> of length $M$.

```lean
theorem erdos_188.variants.nonempty : s.Nonempty
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/188.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/188.lean#L61).

## `Erdos188.erdos_188.variants.estimate`

Solved: stated here without proof.

> Old and new problems and results in combinatorial number theory by Erdős & Graham (Page 15):
>
> How small can $M$ be made? The only estimate currently known is that $M \le 10000000$ (more or less).
> In the other direction, it has just been shown by R. Juhász [Ju (79)] that we must have $M \ge 5$.

```lean
theorem erdos_188.variants.estimate : (∀ k, k ∈ s → 5 ≤ k) ∧ (∃ k ∈ s, k ≤ 10000000)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/188.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/188.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/188.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/188.lean)
- [erdosproblems.com/188](https://www.erdosproblems.com/188)
