---
declaration: theorem
origin: cited
lean: Erdos91.erdos_91, Erdos91.erdos_91.variants.three, Erdos91.erdos_91.variants.four, Erdos91.erdos_91.variants.five, Erdos91.erdos_91.variants.six, Erdos91.erdos_91.variants.seven, Erdos91.erdos_91.variants.eight, Erdos91.erdos_91.variants.nine
statement: formalized
---

# Erdős Problem 91

> *Reference:*
> - [Er87b] Erdős, P., Some combinatorial and metric problems in geometry.
>   Intuitive geometry (Siófok, 1985) (1987), 167-177.
> - [Ko24c] Z. Kovács, A note on Erdős's mysterious remark. arXiv:2412.05190 (2024).
> - [erdosproblems.com/91](https://www.erdosproblems.com/91)

*Quoted from [FormalConjectures/ErdosProblems/91.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/91](https://www.erdosproblems.com/91).

The file states 8 research or textbook statements: 1 open and 7 solved. It also has 6 test statements, counted here but not shown.

## `Erdos91.erdos_91`

Open: stated without proof.

> Suppose $A\subset \mathbb{R}^2$ has $\lvert A\rvert=n$ and minimises the number of distinct
> distances between points in $A$. Prove that for large $n$ there are at least two
> (and probably many) such $A$ which are non-similar.

```lean
theorem erdos_91 :
    ∀ᶠ n : ℕ in atTop, ¬ UniqueMinimizer n
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L150).

## `Erdos91.erdos_91.variants.three`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L159](https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L159).

> For $n = 3$ the equilateral triangle is the only such set.

```lean
theorem erdos_91.variants.three : UniqueMinimizer 3
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L161).

## `Erdos91.erdos_91.variants.four`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L162](https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L162).

> For $n=4$ the square or two equilateral triangles sharing an edge give two
> non-similar examples.

```lean
theorem erdos_91.variants.four : ¬ UniqueMinimizer 4
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L172).

## `Erdos91.erdos_91.variants.five`

Solved: stated here without proof.

> For $n = 5$ the regular pentagon is the unique such set (which has two distinct distances).
> Erdős mysteriously remarks in [Er90] this was proved by 'a colleague'. (In [Er87b] this is
> described as 'a colleague from Zagreb (unfortunately I do not have his letter)'.)
> A published proof of this fact is provided by Kovács [Ko24c].

```lean
theorem erdos_91.variants.five : UniqueMinimizer 5
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L183).

## `Erdos91.erdos_91.variants.six`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L165](https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L165).

> In [Er87b] on p.171 Erdős says that there are at least two non-similar examples for $n = 6$.

```lean
theorem erdos_91.variants.six: ¬ UniqueMinimizer 6
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 192](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L192).

## `Erdos91.erdos_91.variants.seven`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L168](https://github.com/linrock/math-proofs/blob/cd3cf0b176e95209584bf35555a7c0e501255f6e/erdos-91/Solution.lean#L168).

> In [Er87b] on p.171 Erdős says that there are at least two non-similar examples for $n = 7$.

```lean
theorem erdos_91.variants.seven: ¬ UniqueMinimizer 7
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L202).

## `Erdos91.erdos_91.variants.eight`

Solved: stated here without proof.

> In [Er87b] on p.171 Erdős says that there are at least two non-similar examples for $n = 8$.

```lean
theorem erdos_91.variants.eight: ¬ UniqueMinimizer 8
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 210](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L210).

## `Erdos91.erdos_91.variants.nine`

Solved: stated here without proof.

> In [Er87b] on p.171 Erdős says that there are at least two non-similar examples for $n = 9$.

```lean
theorem erdos_91.variants.nine: ¬ UniqueMinimizer 9
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/91.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean#L218).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/91.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/91.lean)
- [erdosproblems.com/91](https://www.erdosproblems.com/91)
