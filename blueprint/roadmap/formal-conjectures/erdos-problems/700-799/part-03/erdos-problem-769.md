---
declaration: theorem
origin: cited
lean: Erdos769.erdos_769, Erdos769.erdos_769.variants.growth_rate
statement: formalized
---

# Erdős Problem 769

> *Reference:* [erdosproblems.com/769](https://www.erdosproblems.com/769)

*Quoted from [FormalConjectures/ErdosProblems/769.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/769.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/769](https://www.erdosproblems.com/769).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos769.erdos_769`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-769/Research/Solution.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-769/Research/Solution.lean).

> Let $c(n)$ be minimal such that if $k\geq c(n)$ then the $n$-dimensional unit
> cube can be decomposed into $k$ homothetic $n$-dimensional cubes. Give good
> bounds for $c(n)$ — in particular, is it true that $c(n)\gg n^n$?
>
> The `c(n) \gg n^n` conjecture is **false**: for odd `n`, one can tile the unit
> `n`-cube into `k` homothetic cubes for every `k ≥ U(n)` with `U(n)/n^n → 0`, so
> `c(n)/n^n → 0` along odd dimensions and no absolute constant lower-bounds it.
>
> Determining good bounds for `c(n)` in general remains open.

```lean
theorem erdos_769 : ¬ Erdos769LowerBound
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/769.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/769.lean#L85).

## `Erdos769.erdos_769.variants.growth_rate`

Open: stated without proof.

> What refuting $c(n)\gg n^n$ leaves open: give good bounds for $c(n)$. Asked here on the
> scale the problem itself sets, $n^n$: does $c$ have a well-defined order
>
> $$\lim_{n\to\infty}\frac{\log c(n)}{n\log n}?$$
>
> The refuted conjecture would have forced this limit to be at least $1$.
> The cutoff condition is restricted to positive dimensions: in dimension zero,
> exact coverage permits only one tile, so no cutoff exists.

```lean
theorem erdos_769.variants.growth_rate :
    ∃ c : ℕ → ℕ, (∀ n, 0 < n → IsCutoff n (c n)) ∧
      ∃ γ : ℝ, Tendsto (fun n : ℕ => Real.log (c n) / (n * Real.log n)) atTop (𝓝 γ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/769.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/769.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/769.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/769.lean)
- [erdosproblems.com/769](https://www.erdosproblems.com/769)
