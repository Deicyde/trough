---
declaration: theorem
origin: cited
lean: Exponentials.four_exponentials_conjecture, Exponentials.two_pow_three_pow_transcendental
statement: formalized
---

# Exponentials conjectures and theorems

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Four_exponentials_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Exponentials.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Exponentials.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `Exponentials.four_exponentials_conjecture`

Open: stated without proof.

> **Four exponentials conjecture**
> Let $x_0, x_1$ and $y_0, y_1$ be $\mathbb Q$-linearly independent pairs of complex numbers,
> then some $e^{x_i y_j}$ is transcendental.

```lean
theorem four_exponentials_conjecture (x : Fin 2 → ℂ) (y : Fin 2 → ℂ)
    (h1 : LinearIndependent ℚ x) (h2 : LinearIndependent ℚ y) :
    ∃ i j : Fin 2, Transcendental ℚ (exp (x i * y j))
```

Category `research open`; AMS [33 Special functions](../../by-subject/part-02/33-special-functions/README.md). Declared in [FormalConjectures/Wikipedia/Exponentials.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Exponentials.lean#L38).

## `Exponentials.two_pow_three_pow_transcendental`

Open: stated without proof.

> The four exponential conjecture would imply that for any irrational number $t$,
> at least one of the numbers $2^t$ and $3^t$ is transcendental.

```lean
theorem two_pow_three_pow_transcendental (t : ℝ) (h : Irrational t) :
    Transcendental ℚ (2 ^ t : ℝ) ∨ Transcendental ℚ (3 ^ t : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Exponentials.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Exponentials.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Exponentials.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Exponentials.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Four_exponentials_conjecture)
