---
declaration: theorem
origin: cited
lean: Erdos365.erdos_365.parts.i, Erdos365.erdos_365.parts.ii
statement: formalized
---

# Erdős Problem 365

> *References:*
> - [erdosproblems.com/365](https://www.erdosproblems.com/365)
> - [Go70] Golomb, S. W., *Powerful numbers*. Amer. Math. Monthly (1970), 848-855.
> - [Gu04] Guy, R. K., *Unsolved problems in number theory* (2004), Problem B16.
> - [Wa76] Walker, D. T., *Consecutive integer pairs of powerful numbers and related
>   Diophantine equations*. Fibonacci Quart. (1976), 111-116.

*Quoted from [FormalConjectures/ErdosProblems/365.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/365.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/365](https://www.erdosproblems.com/365).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos365.erdos_365.parts.i`

Proved here.

> Do all pairs of consecutive powerful numbers $n$ and $n+1$ come from solutions to Pell
> equations? In other words, must either $n$ or $n+1$ be a square?
>
> The answer to the first question is no: Golomb [Go70] observed that both $12167=23^3$ and
> $12168=2^3 3^2 13^2$ are powerful.
>
> We require $n>0$ since `Nat.Powerful` also includes $0$.

```lean
theorem erdos_365.parts.i :
    ¬ ∀ n : ℕ, 0 < n → Nat.Powerful n → Nat.Powerful (n + 1) →
      IsSquare n ∨ IsSquare (n + 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/365.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/365.lean#L80).

## `Erdos365.erdos_365.parts.ii`

Open: stated without proof.

> Is the number of positive $n\leq x$ such that $n$ and $n+1$ are both powerful bounded
> by $(\log x)^{O(1)}$?

```lean
theorem erdos_365.parts.ii :
    ∃ C : ℝ, 0 < C ∧ ∃ k : ℕ, ∀ᶠ x : ℕ in Filter.atTop,
      ({n : ℕ | 0 < n ∧ n ≤ x ∧ Nat.Powerful n ∧ Nat.Powerful (n + 1)}.ncard : ℝ) ≤
        C * (Real.log x) ^ k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/365.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/365.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/365.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/365.lean)
- [erdosproblems.com/365](https://www.erdosproblems.com/365)
