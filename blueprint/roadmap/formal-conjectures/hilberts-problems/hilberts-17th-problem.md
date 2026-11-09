---
declaration: theorem
origin: cited
lean: Hilbert17.hilbert_17th_problem, Hilbert17.f_nonneg, Hilbert17.f_not_sum_of_squares, Hilbert17.hilbert_17th_problem_poly
statement: formalized
---

# Hilbert's 17th problem

> Let $f(x_1, \dots, x_n)$ be a multivariable polynomial with real coefficients that takes only
> nonnegative values for all real inputs.
> Hilbert's 17th problem asks whether there exist rational functions $g_1, \dots, g_m$ such that
> $f = g_1^2 + g_2^2 + \cdots + g_m^2$. Resolved affirmatively by Artin in 1927.
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_seventeenth_problem)
> - Motzkin, "The arithmetic-geometric inequality". In Shisha, Oved (ed.). Inequalities. Academic Press. pp. 205–224.

*Quoted from [FormalConjectures/HilbertProblems/17.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/HilbertProblems/17.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 solved and 2 textbook results. It also has 2 test statements, counted here but not shown.

## `Hilbert17.hilbert_17th_problem`

Solved: stated here without proof.

> Hilbert's 17th problem: every non-negative multivariate polynomial is a sum of
> squares of rational functions.

```lean
theorem hilbert_17th_problem {n : ℕ} (hn : 0 < n) (f : MvPolynomial (Fin n) ℝ)
    (h : ∀ x : Fin n → ℝ, 0 ≤ f.eval x) :
    ∃ (m : ℕ) (g : Fin m → MvRatFunc (Fin n) ℝ), algebraMap _ _ f = ∑ i, (g i) ^ 2
```

Category `research solved`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/HilbertProblems/17.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/HilbertProblems/17.lean#L43).

## `Hilbert17.f_nonneg`

Textbook result, proved here.

> The Motzkin polynomial is non-negative everywhere.

```lean
theorem f_nonneg : ∀ x y : ℝ, 0 ≤ f.eval ![x, y]
```

Category `textbook`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/HilbertProblems/17.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/HilbertProblems/17.lean#L59).

## `Hilbert17.f_not_sum_of_squares`

Textbook result, stated without proof.

> The Motzkin polynomial cannot be written as a sum of squares of polynomials.

```lean
theorem f_not_sum_of_squares :
    ¬∃ (n : ℕ) (hn : 0 < n) (S : Fin n → MvPolynomial (Fin 2) ℝ), f = ∑ i, S i ^ 2
```

Category `textbook`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/HilbertProblems/17.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/HilbertProblems/17.lean#L73).

## `Hilbert17.hilbert_17th_problem_poly`

Solved: stated here without proof.

> Hilbert's 17th problem for homogeneous polynomials: characterization of dimensions and degrees
> where non-negative polynomials are sums of squares of polynomials.

```lean
theorem hilbert_17th_problem_poly {n d : ℕ} (hn : 0 < n) (hd : 0 < d) :
    Hilbert17thProblemHomogenousPoly n d ↔ n = 1 ∨ n = 2 ∨ d = 1 ∨ n = 3 ∧ d = 2
```

Category `research solved`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/HilbertProblems/17.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/HilbertProblems/17.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/HilbertProblems/17.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/HilbertProblems/17.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hilbert%27s_seventeenth_problem)
