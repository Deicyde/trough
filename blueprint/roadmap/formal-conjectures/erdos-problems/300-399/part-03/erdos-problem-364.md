---
declaration: theorem
origin: cited
lean: Erdos364.erdos_364, Erdos364.erdos_364.variants.strong, Erdos364.erdos_364.variants.weak
statement: formalized
---

# Erdős Problem 364

> *Reference:* [erdosproblems.com/364](https://www.erdosproblems.com/364)

*Quoted from [FormalConjectures/ErdosProblems/364.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/364.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/364](https://www.erdosproblems.com/364).

The file states 3 research or textbook statements: 2 open and 1 textbook result.

## `Erdos364.erdos_364`

Open: stated without proof.

> There is no consecutive triple of powerful numbers.

```lean
theorem erdos_364 :
    ¬ ∃ (n : ℕ), Powerful n ∧ Powerful (n + 1) ∧ Powerful (n + 2)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/364.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/364.lean#L34).

## `Erdos364.erdos_364.variants.strong`

Open: stated without proof.

> Erdős [Er76d] conjectured a stronger statement: if $n_k$ is the $k$th powerful number,
> then $n_{k+2} - n_k > n_k^c$ for some constant $c > 0$.
>
> [Er76d] Erdős, P., Problems and results on number theoretic properties of consecutive integers and related questions. Proceedings of the Fifth Manitoba Conference on Numerical Mathematics (Univ. Manitoba, Winnipeg, Man., 1975) (1976), 25-44.

```lean
theorem erdos_364.variants.strong :
    ∃ (c : ℝ) (h : c > 0), ∀ (k : ℕ),
    Nat.nth Powerful (k + 2) - Nat.nth Powerful k > (Nat.nth Powerful k : ℝ) ^ c
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/364.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/364.lean#L45).

## `Erdos364.erdos_364.variants.weak`

Textbook result, proved here.

> There is no quadruple of powerful numbers, since at least one of the four numbers must be
> $2 \pmod{4}$, which cannot be powerful (since $2$ divides it, but $2^2$ does not).

```lean
theorem erdos_364.variants.weak :
    ¬ ∃ (n : ℕ), Powerful n ∧ Powerful (n + 1) ∧ Powerful (n + 2) ∧ Powerful (n + 3)
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/364.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/364.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/364.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/364.lean)
- [erdosproblems.com/364](https://www.erdosproblems.com/364)
