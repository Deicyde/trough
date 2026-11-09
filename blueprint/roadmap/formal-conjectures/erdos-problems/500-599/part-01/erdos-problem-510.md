---
declaration: theorem
origin: cited
lean: Erdos510.erdos_510, Erdos510.erdos_510.variants.ruzsa, Erdos510.erdos_510.variants.bedert
statement: formalized
---

# Erdős Problem 510

> *References:*
> - [erdosproblems.com/510](https://www.erdosproblems.com/510)
> - [Ben Green's Open Problem 81](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.11)
> - [Ru04] Ruzsa, Imre Z., Negative values of cosine sums. Acta Arith. (2004), 179-186.
> - [Be25c] B. Bedert, Polynomial bounds for the Chowla Cosine Problem. arXiv:2509.05260 (2025).

*Quoted from [FormalConjectures/ErdosProblems/510.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/510.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/510](https://www.erdosproblems.com/510).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos510.erdos_510`

Open: stated without proof.

> **Chowla's cosine problem**
>
> If $A\subset \mathbb{N}$ is a finite set of positive integers of size $N > 0$ then is there some
> absolute constant $c>0$ and $\theta$ such that
> $$\sum_{n\in A}\cos(n\theta) < -cN^{1/2}?$$

```lean
theorem erdos_510 :
    ∃ (c : ℝ) (hc : 0 < c),
      ∀ᶠ N in atTop, ∀ (A : Finset ℕ), 0 ∉ A → #A = N →
      ∃ θ, ∑ n ∈ A, cos (n * θ) < -c * sqrt N
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/510.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/510.lean#L45).

## `Erdos510.erdos_510.variants.ruzsa`

Solved: stated here without proof.

> Ruzsa [Ru04] proved an upper bound of $-\exp(O(\sqrt{\log N})$.

```lean
theorem erdos_510.variants.ruzsa :
    ∃ (c : ℝ) (hc : 0 < c),
      ∀ᶠ N in atTop, ∀ (A : Finset ℕ), 0 ∉ A → #A = N →
      ∃ θ, ∑ n ∈ A, cos (n * θ) < - exp (c * sqrt (log N))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/510.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/510.lean#L55).

## `Erdos510.erdos_510.variants.bedert`

Solved: stated here without proof.

> Bedert [Be25c] proved an upper bound of $-c N^{1/7}$.

```lean
theorem erdos_510.variants.bedert :
    ∃ (c : ℝ) (hc : 0 < c),
      ∀ᶠ N in atTop, ∀ (A : Finset ℕ), 0 ∉ A → #A = N →
      ∃ θ, ∑ n ∈ A, cos (n * θ) < - c * N ^ (1 / 7 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/510.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/510.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/510.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/510.lean)
- [erdosproblems.com/510](https://www.erdosproblems.com/510)
