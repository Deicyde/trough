---
declaration: theorem
origin: cited
lean: Erdos228.erdos_228
statement: formalized
---

# Erdős Problem 228

> *Reference:* [erdosproblems.com/228](https://www.erdosproblems.com/228)

*Quoted from [FormalConjectures/ErdosProblems/228.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/228.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/228](https://www.erdosproblems.com/228).

The file states 1 research or textbook statement: 1 solved.

## `Erdos228.erdos_228`

Solved: stated here without proof.

> Does there exist, for all large $n$, a polynomial $P$ of degree $n$, with coefficients $\pm1$, such
> that
>
> $$\sqrt n \ll |P(z)| \ll \sqrt n$$
>
> for all $|z|=1$, with the implied constants independent of
> $z$ and $n$?
>
> The answer is yes, proved by Balister, Bollobás, Morris, Sahasrabudhe, and Tiba [BBMST19].
>
> [BBMST19] Balister, P. and Bollob\'{A}s, B. and Morris, R. and Sahasrabudhe, J. and Tiba, M., _Flat Littlewood Polynomials Exist_. arXiv:1907.09464 (2019).

```lean
theorem erdos_228 :
    ∃ (c₁ : ℝ) (c₂ : ℝ), ∀ᶠ n : ℕ in Filter.atTop,
    ∃ p : Polynomial ℂ, p.degree = n ∧
    (∀ i ≤ n, p.coeff i = 1 ∨ p.coeff i = -1) ∧
    ∀ z : ℂ, ‖z‖ = 1 →
    ( √n < c₁ * ‖p.eval z‖ ∧ ‖p.eval z‖ < c₂ * √n )
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/228.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/228.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/228.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/228.lean)
- [erdosproblems.com/228](https://www.erdosproblems.com/228)
