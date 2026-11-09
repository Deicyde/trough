---
declaration: theorem
origin: cited
lean: Green82.green_82, Green82.green_82_lower_bound, Green82.green_82_upper_bound
statement: formalized
---

# Ben Green's Open Problem 82

> *References:*
> - [Ben Green's Open Problem 82](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.82)
> - [An improved lower bound for a problem of Littlewood on the zeros of cosine polynomials](https://arxiv.org/abs/2407.16075) (Bedert, 2025)
> - [Cosine polynomials with few zeros](https://arxiv.org/abs/2005.01695) (Juškevičius & Sahasrabudhe, 2020)

*Quoted from [FormalConjectures/GreensOpenProblems/82.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/82.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Green82.green_82`

Open: stated without proof.

> Let $A \subset \mathbb{Z}$ be a set of size $n$. For how many $\theta \in \mathbb{R}/\mathbb{Z}$
> must we have $\sum_{a \in A} \cos(2\pi a\theta) = 0$? The answer is the function `minZeros`.

```lean
theorem green_82 : green_82.answer = minZeros
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/82.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/82.lean#L47).

## `Green82.green_82_lower_bound`

Solved: stated here without proof.

> Lower bound: every set has at least $(\log \log n)^{1-o(1)}$ zeros.

```lean
theorem green_82_lower_bound :
    ∃ o : ℕ → ℝ, o =o[atTop] (fun _ ↦ (1 : ℝ)) ∧
      ∀ᶠ n in atTop, ∀ A : Finset ℤ, A.card = n →
        (⌊(Real.log (Real.log n)) ^ (1 - |o n|)⌋₊ : ℕ∞) ≤
        ({θ : ℝ | θ ∈ Ico 0 1 ∧ ∑ a ∈ A, cos (2 * π * a * θ) = 0} : Set ℝ).ncard
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/82.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/82.lean#L52).

## `Green82.green_82_upper_bound`

Solved: stated here without proof.

> Upper bound: there exists $A$ with at most $C(n \log n)^{2/3}$ zeros.

```lean
theorem green_82_upper_bound :
    ∃ C > 0, ∀ n ≥ 1, ∃ A : Finset ℤ, A.card = n ∧
      ({θ : ℝ | θ ∈ Ico 0 1 ∧ ∑ a ∈ A, cos (2 * π * a * θ) = 0} : Set ℝ).ncard ≤
      (⌊C * (n * Real.log n) ^ (2 / 3 : ℝ)⌋₊ : ℕ∞)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/82.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/82.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/82.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/82.lean)
- [Ben Green's Open Problem 82](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.82)
