---
declaration: theorem
origin: cited
lean: Erdos1161.erdos_1161, Erdos1161.erdos_1161.variants.max_asymptotic, Erdos1161.erdos_1161.variants.threshold
statement: formalized
---

# Erdős Problem 1161

> *References:*
> - [erdosproblems.com/1161](https://www.erdosproblems.com/1161)
> - [Be25d] Beker, Adrian, *The most probable order of a random permutation*.
>   [arXiv:2510.11698](https://arxiv.org/abs/2510.11698) (2025).
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1161.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1161.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1161](https://www.erdosproblems.com/1161).

The file states 3 research or textbook statements: 3 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1161.erdos_1161`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1161.lean#L50](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1161.lean#L50).

> Let $f_k(n)$ count the number of elements of $S_n$ of order $k$. For which values of $k$ will
> $f_k(n)$ be maximal? [Va99, 5.72]
>
> Beker [Be25d, Theorem 1.2] proved that, for all large $n$, $f_k(n)$ is maximal if and only if
> $k\geq 1$ is minimal such that $[1,\ldots,n-k]\mid k$, where $[\cdot]$ is the least common
> multiple. The last clause on erdosproblems.com/1161 reads "$f_k(n)=(n-1)!$" instead of "$f_k(n)$
> is maximal"; we follow [Be25d]. For $k > n$ we read $n-k$ as $0$, which does not change the
> least such $k$, because $k = n$ qualifies.

```lean
theorem erdos_1161 :
    ∀ᶠ n : ℕ in atTop, {k : ℕ | ∀ j : ℕ, f j n ≤ f k n} = erdos_1161.answer n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1161.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1161.lean#L78).

## `Erdos1161.erdos_1161.variants.max_asymptotic`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1161.lean#L50](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1161.lean#L50).

> Beker [Be25d, Theorem 1.1] proved that
>
> $$\max_{k\geq 1} f_k(n)\sim (n-1)!.$$

```lean
theorem erdos_1161.variants.max_asymptotic :
    (fun n : ℕ ↦ (maxF n : ℝ)) ~[atTop] (fun n : ℕ ↦ ((n - 1).factorial : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1161.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1161.lean#L89).

## `Erdos1161.erdos_1161.variants.threshold`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1161.lean#L50](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1161.lean#L50).

> Beker [Be25d, Theorem 1.1] also proved that, if $n$ is sufficiently large and
> $f_k(n)\geq (n-1)!$, then $[1,\ldots,n-k]\mid k$. The statement also records $1\leq k\leq n$,
> since [Be25d] writes such $k$ as $n-k'$ with $0\leq k'\leq n-1$.

```lean
theorem erdos_1161.variants.threshold :
    ∀ᶠ n : ℕ in atTop, ∀ k : ℕ, (n - 1).factorial ≤ f k n →
      k ≤ n ∧ 0 < k ∧ Nat.lcmUpto (n - k) ∣ k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1161.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1161.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1161.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1161.lean)
- [erdosproblems.com/1161](https://www.erdosproblems.com/1161)
