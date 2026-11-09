---
declaration: theorem
origin: cited
lean: BurningNumberConjecture.burning_number_conjecture, BurningNumberConjecture.burning_number_conjecture.variants.path, BurningNumberConjecture.burning_number_conjecture.variants.norin_turcotte
statement: formalized
---

# The burning number conjecture

> *References:*
> * [BJR16] Bonato, A., Janssen, J., and Roshanbin, E. (2016). "How to burn a graph."
>   *Internet Math.* 12, pp. 85--100.
>   [arXiv:1507.06524](https://arxiv.org/abs/1507.06524)
> * [NT24] Norin, S. and Turcotte, J. (2024). "The burning number conjecture holds
>   asymptotically." *J. Combin. Theory Ser. B* 168, pp. 208--235.
>   [arXiv:2207.04035](https://arxiv.org/abs/2207.04035)

*Quoted from [FormalConjectures/Paper/BurningNumberConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/BurningNumberConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `BurningNumberConjecture.burning_number_conjecture`

Open: stated without proof.

> **The burning number conjecture** (Bonato–Janssen–Roshanbin [BJR16]).
>
> Every connected graph on `n` vertices can be burned in at most `⌈√n⌉` rounds: fires started at
> one new vertex per round, each spreading to all neighbouring vertices every round, can burn
> the whole graph in `⌈√n⌉` rounds.

```lean
theorem burning_number_conjecture {V : Type} [Fintype V] (G : SimpleGraph V)
    (hc : G.Connected) :
    burningNumber G ≤ ⌈Real.sqrt (Fintype.card V)⌉₊
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/BurningNumberConjecture.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/BurningNumberConjecture.lean#L73).

## `BurningNumberConjecture.burning_number_conjecture.variants.path`

Solved: stated here without proof.

> **Paths attain the conjectured bound** (Bonato–Janssen–Roshanbin [BJR16]).
>
> The burning number of the path on `n ≥ 1` vertices is exactly `⌈√n⌉`, so the bound in the
> burning number conjecture cannot be improved.

```lean
theorem burning_number_conjecture.variants.path (n : ℕ) (hn : 1 ≤ n) :
    burningNumber (SimpleGraph.pathGraph n) = ⌈Real.sqrt n⌉₊
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/BurningNumberConjecture.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/BurningNumberConjecture.lean#L85).

## `BurningNumberConjecture.burning_number_conjecture.variants.norin_turcotte`

Solved: stated here without proof.

> **Norin–Turcotte (2024): the burning number conjecture holds asymptotically.**
>
> For every `ε > 0`, every sufficiently large connected graph on `n` vertices can be burned in
> at most `(1 + ε) √n` rounds.
>
> *Reference:* [NT24].

```lean
theorem burning_number_conjecture.variants.norin_turcotte (ε : ℝ) (hε : 0 < ε) :
    ∃ n₀ : ℕ, ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.Connected →
      n₀ ≤ Fintype.card V →
        (burningNumber G : ℝ) ≤ (1 + ε) * Real.sqrt (Fintype.card V)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/BurningNumberConjecture.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/BurningNumberConjecture.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/BurningNumberConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/BurningNumberConjecture.lean)
- [arXiv:1507.06524](https://arxiv.org/abs/1507.06524)
