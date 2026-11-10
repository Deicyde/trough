---
declaration: theorem
origin: cited
lean: Erdos1060.erdos_1060.parts.i, Erdos1060.erdos_1060.parts.ii
statement: formalized
---

# Erdős Problem 1060

> *Reference:* [erdosproblems.com/1060](https://www.erdosproblems.com/1060)

*Quoted from [FormalConjectures/ErdosProblems/1060.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1060.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1060](https://www.erdosproblems.com/1060).

The file states 2 research or textbook statements: 2 open.

## `Erdos1060.erdos_1060.parts.i`

Open: stated without proof.

> The conjecture is about the function $f(n)$ which counts the number of solutions to
> $k\sigma(k)=n$, where $\sigma(k)$ is the sum of divisors of $k$. The first bound is that $f(n)$ grows slower
> than any power of $n^(\frac{1}{\log\log n})$. The second bound is that $f(n)$ is at most a power of
> $\log n$.

```lean
theorem erdos_1060.parts.i :
    ∃ h : ℕ → ℝ,
      h =o[atTop] (fun n ↦ 1 / log (log n)) ∧ ∀ᶠ n in atTop, #{k ≤ n | k * σ 1 k = n} ≤ (n : ℝ) ^ h n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1060.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1060.lean#L40).

## `Erdos1060.erdos_1060.parts.ii`

Open: stated without proof.

> Part (ii) of Erdős Problem 1060: bound on the number of $k \le n$ with $k \sigma_1(k) = n$.

```lean
theorem erdos_1060.parts.ii :
    ∃ (C : ℝ), (fun n ↦ (#{k ≤ n | k * σ 1 k = n} : ℝ)) =O[atTop]
      (fun n ↦ log n ^ C)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1060.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1060.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1060.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1060.lean)
- [erdosproblems.com/1060](https://www.erdosproblems.com/1060)
