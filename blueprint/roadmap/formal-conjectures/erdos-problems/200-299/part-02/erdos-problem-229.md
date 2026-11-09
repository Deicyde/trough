---
declaration: theorem
origin: cited
lean: Erdos229.erdos_229, Erdos229.theorem_1
statement: formalized
---

# Erdős Problem 229

> *References:*
> - [erdosproblems.com/229](https://www.erdosproblems.com/229)
> - [BaSc72] Barth, K. F. and Schneider, W. J., On a problem of Erd\H{o}s concerning the zeros of the
>   derivatives of an entire function. Proc. Amer. Math. Soc. (1972), 229--232.
> - [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.

*Quoted from [FormalConjectures/ErdosProblems/229.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/229.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/229](https://www.erdosproblems.com/229).

The file states 2 research or textbook statements: 2 solved.

## `Erdos229.erdos_229`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos229.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos229.lean).

> Let $(S_n)_{n \ge 1}$ be a sequence of sets of complex numbers, none of which have a finite
> limit point. Does there exist an entire transcendental function $f(z)$ such that, for all $n \ge 1$, there
> exists some $k_n \ge 0$ such that $f^{(k_n)}(z) = 0$ for all $z \in S_n$.
>
> This is Problem 2.30 in [Ha74], where it is attributed to Erdős.
>
> Solved in the affirmative by Barth and Schneider [BaSc72].
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_229 :
    letI := Polynomial.algebraPi ℂ ℂ ℂ
    ∀ (S : ℕ → Set ℂ), (∀ n, derivedSet (S n) = ∅) →
    ∃ (f : ℂ → ℂ), Transcendental (Polynomial ℂ) f ∧ Differentiable ℂ f ∧ ∀ n ≥ 1,
      ∃ k, ∀ z ∈ S n, iteratedDeriv k f z = 0
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/229.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/229.lean#L47).

## `Erdos229.theorem_1`

Solved: stated here without proof.

> Let $\{S_k\}$ be any sequence of sets in the complex plane, each of which has no finite
> limit point. Then there exists a sequence $\{n_k\}$ of positive integers and a
> transcendental entire function $f(z)$ such that $f^{(n_k)}(z) = 0$ if $z \in S_k$.

```lean
theorem theorem_1
    {S : ℕ → Set ℂ}
    (h : ∀ (k), derivedSet (S k) = ∅) :
  letI := Polynomial.algebraPi ℂ ℂ ℂ
  ∃ (f : ℂ → ℂ) (n : ℕ → ℕ),
    Differentiable ℂ f ∧ Transcendental (Polynomial ℂ) f ∧ ∀ k, 0 < n k ∧ ∀ {z} (_: z ∈ S k),
      iteratedDeriv (n k) f z = 0
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/229.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/229.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/229.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/229.lean)
- [erdosproblems.com/229](https://www.erdosproblems.com/229)
