---
declaration: theorem
origin: cited
lean: Erdos733.erdos_733, Erdos733.erdos_733.variants.limit_exists
statement: formalized
---

# Erdős Problem 733

> *References:*
> - [erdosproblems.com/733](https://www.erdosproblems.com/733)
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42. [PDF](https://www.renyi.hu/~p_erdos/1981-16.pdf)
> - [SzTr83] Szemerédi, E. and Trotter, Jr., W. T., *Extremal problems in discrete geometry*.
>   Combinatorica (1983), 381-392.

*Quoted from [FormalConjectures/ErdosProblems/733.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/733.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/733](https://www.erdosproblems.com/733).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos733.erdos_733`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos733.lean#L41](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos733.lean#L41).

> Call a sequence $1\lt X_1\leq\cdots\leq X_m\leq n$ line-compatible if there is a set of $n$ points in
> $\mathbb{R}^2$ such that there are $m$ lines $\ell_1,\ldots,\ell_m$ containing at least two
> points, and the number of points on $\ell_i$ is exactly $X_i$.
>
> Prove that there are at most
>
> $$\exp(O(n^{1/2}))$$
>
> many line-compatible sequences.
>
> Asked by Erdős [Er81] and proved by Szemerédi and Trotter [SzTr83]. We take the lines $\ell_i$ to
> be distinct but not necessarily all the lines determined by the points, as on erdosproblems.com;
> [Er81] uses all the determined lines (`allLinesSequences`), so this bound implies his. Finiteness
> of the set is part of the statement, since `Set.ncard` of an infinite set is $0$.

```lean
theorem erdos_733 :
    ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ,
      (compatibleSequences n).Finite ∧
        ((compatibleSequences n).ncard : ℝ) ≤ Real.exp (C * Real.sqrt n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/733.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/733.lean#L103).

## `Erdos733.erdos_733.variants.limit_exists`

Open: stated without proof.

> Erdős [Er81] writes that it is 'easy' to prove there are at least
>
> $$\exp(cn^{1/2})$$
>
> many such sequences for some constant $c>0$, but expected proving the upper bound to be
> difficult. Once it is done, he asked for the existence and value of
>
> $$\lim_{n\to \infty}\frac{\log f(n)}{n^{1/2}},$$
>
> where $f(n)$ counts the number of line-compatible sequences. Does this limit exist?
>
> In [Er81], $f(n)$ counts the sequences of the numbers of points on all the lines determined by
> $n$ points, i.e. `(allLinesSequences n).ncard`; this set is finite, as a subset of
> `compatibleSequences n`.

```lean
theorem erdos_733.variants.limit_exists :
    ∃ c : ℝ, Tendsto
      (fun n : ℕ ↦ Real.log ((allLinesSequences n).ncard : ℝ) / Real.sqrt n)
      atTop (𝓝 c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/733.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/733.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/733.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/733.lean)
- [erdosproblems.com/733](https://www.erdosproblems.com/733)
