---
declaration: theorem
origin: cited
lean: PierceBirkhoff.pierce_birkhoff_conjecture, PierceBirkhoff.pierce_birkhoff_conjecture_dim_one, PierceBirkhoff.pierce_birkhoff_conjecture_dim_two
statement: formalized
---

# Pierce–Birkhoff conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Pierce%E2%80%93Birkhoff_conjecture)
>
> The Pierce-Birkhoff conjecture asserts that any piecewise-polynomial function can be expressed
> as a maximum of finite minima of finite collections of polynomials. It was first stated in 1956
> by Garrett Birkhoff and Richard S. Pierce, though the modern rigorous formulation is due to
> Melvin Henriksen and John R. Isbell.
>
> The conjecture has been proved for `n = 1` and `n = 2` by Louis Mahé.

*Quoted from [FormalConjectures/Wikipedia/PierceBirkhoff.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PierceBirkhoff.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `PierceBirkhoff.pierce_birkhoff_conjecture`

Open: stated without proof.

> The Pierce-Birkhoff conjecture states that for every real piecewise-polynomial function
> `f : ℝⁿ → ℝ`, there exists a finite set of polynomials `gᵢⱼ ∈ ℝ[x₁, ..., xₙ]` such that
> `f = supᵢ infⱼ(gᵢⱼ)`.

```lean
theorem pierce_birkhoff_conjecture {n : ℕ} (f : (Fin n → ℝ) → ℝ)
    (hf : IsPiecewiseMvPolynomial f) :
    ∃ (ι κ : Type) (g : ι → κ → MvPolynomial (Fin n) ℝ), Finite ι ∧ Finite κ ∧
      ∀ x, f x = ⨆ i, ⨅ j, MvPolynomial.eval x (g i j)
```

Category `research open`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Wikipedia/PierceBirkhoff.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PierceBirkhoff.lean#L90).

## `PierceBirkhoff.pierce_birkhoff_conjecture_dim_one`

Solved: stated here without proof.

> The Pierce-Birkhoff conjecture holds for `n = 1`.
> This was proved by Louis Mahé.

```lean
theorem pierce_birkhoff_conjecture_dim_one (f : ℝ → ℝ)
    (hf : IsPiecewisePolynomial f) :
    ∃ (ι κ : Type) (g : ι → κ → Polynomial ℝ), Finite ι ∧ Finite κ ∧
      ∀ x, f x = ⨆ i, ⨅ j, Polynomial.eval x (g i j)
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Wikipedia/PierceBirkhoff.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PierceBirkhoff.lean#L101).

## `PierceBirkhoff.pierce_birkhoff_conjecture_dim_two`

Solved: stated here without proof.

> The Pierce-Birkhoff conjecture holds for `n = 2`.
> This was proved by Louis Mahé.

```lean
theorem pierce_birkhoff_conjecture_dim_two
    (f : (Fin 2 → ℝ) → ℝ) (hf : IsPiecewiseMvPolynomial f) :
    ∃ (ι κ : Type) (g : ι → κ → MvPolynomial (Fin 2) ℝ), Finite ι ∧ Finite κ ∧
      ∀ x, f x = ⨆ i, ⨅ j, MvPolynomial.eval x (g i j)
```

Category `research solved`; AMS [13 Commutative algebra](../../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/Wikipedia/PierceBirkhoff.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PierceBirkhoff.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PierceBirkhoff.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PierceBirkhoff.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Pierce%E2%80%93Birkhoff_conjecture)
