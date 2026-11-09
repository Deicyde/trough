---
declaration: theorem
origin: cited
lean: Sendov.sendov_conjecture, Sendov.sendov_conjecture.variants.le_eight, Sendov.sendov_conjecture.variants.eventually_true
statement: formalized
---

# Sendov's conjecture

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Sendov%27s_conjecture)
> - Lech Mazur, *A Computer-Assisted Proof of Sendov's Conjecture*,
>   [ProofAtlas, August 5, 2026](https://www.proofatlas.ai/papers/sendov-conjecture/SENDOV_CONJECTURE_PROOF_AUGUST_5_2026.pdf).
> - Terence Tao, [*A digestion of the proof of Sendov's conjecture*](https://terrytao.wordpress.com/2026/08/12/a-digestion-of-the-proof-of-sendovs-conjecture/).
> - [Tao's Lean formalization of the digested proof](https://github.com/teorth/sendov).
>
> Tags: Sendov Conjecture, Ilieff's Conjecture.

*Quoted from [FormalConjectures/Wikipedia/Sendov.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Sendov.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `Sendov.sendov_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/teorth/sendov/blob/1ddea92d89f951a0a7cbbffa6c267cf7e6640b1d/Sendov/Conjecture.lean#L156-L167](https://github.com/teorth/sendov/blob/1ddea92d89f951a0a7cbbffa6c267cf7e6640b1d/Sendov/Conjecture.lean#L156-L167).

> **Sendov's conjecture** states that for a polynomial
>
> $$f(z)=(z-r_{1})\cdots (z-r_{n}),\qquad (n\geq 2)$$
>
> with all roots $r_1, ..., r_n$ inside the closed unit disk $|z| ≤ 1$, each of the $n$ roots is at a
> distance no more than $1$ from at least one critical point.

```lean
theorem sendov_conjecture (n : ℕ) (hn : 2 ≤ n) : n.SatisfiesSendovConjecture
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/Sendov.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Sendov.lean#L63).

## `Sendov.sendov_conjecture.variants.le_eight`

Solved: stated here without proof.

> **Sendov's conjecture** states that for a polynomial
>
> $$f(z)=(z-r_{1})\cdots (z-r_{n}),\qquad (n\geq 2)$$
>
> with all roots $r_1, ..., r_n$ inside the closed unit disk $|z| ≤ 1$, each of the $n$ roots is at a
> distance no more than $1$ from at least one critical point.
>
> It has been shown that Sendov's conjecture holds when the degree $n$ is at most $8$.

```lean
theorem sendov_conjecture.variants.le_eight (n : ℕ) (hn : n ∈ Set.Icc 2 8) :
    n.SatisfiesSendovConjecture
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/Sendov.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Sendov.lean#L74).

## `Sendov.sendov_conjecture.variants.eventually_true`

Solved: stated here without proof.

> **Sendov's conjecture** states that for a polynomial
>
> $$f(z)=(z-r_{1})\cdots (z-r_{n}),\qquad (n\geq 2)$$
>
> with all roots $r_1, ..., r_n$ inside the closed unit disk $|z| ≤ 1$, each of the $n$ roots is at a
> distance no more than $1$ from at least one critical point.
>
> It has been shown that Sendov's conjecture holds for polynomials of sufficiently large degree.

```lean
theorem sendov_conjecture.variants.eventually_true :
    ∀ᶠ (n : ℕ) in Filter.atTop, n.SatisfiesSendovConjecture
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/Sendov.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Sendov.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Sendov.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Sendov.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Sendov%27s_conjecture)
