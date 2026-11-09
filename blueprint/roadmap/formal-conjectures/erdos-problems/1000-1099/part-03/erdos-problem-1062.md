---
declaration: theorem
origin: cited
lean: Erdos1062.erdos_1062.parts.ii, Erdos1062.erdos_1062.variants.lower_bound, Erdos1062.erdos_1062.variants.lebensold_bounds
statement: formalized
---

# Erdős Problem 1062

> *Reference:* [erdosproblems.com/1062](https://www.erdosproblems.com/1062)

*Quoted from [FormalConjectures/ErdosProblems/1062.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1062.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1062](https://www.erdosproblems.com/1062).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos1062.erdos_1062.parts.ii`

Open: stated without proof.

> Erdős asked whether the limiting density `f n / n` exists and, if so, whether it is
> irrational.

```lean
theorem erdos_1062.parts.ii :
    ∃ l, Tendsto (fun n => (f n : ℝ) / n) atTop (𝓝 l) ∧ Irrational l
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1062.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1062.lean#L49).

## `Erdos1062.erdos_1062.variants.lower_bound`

Proved here.

> The interval `[⌊n/3⌋, n]` is fork-free, and therefore `f n` is at least `⌈2n / 3⌉`.

```lean
theorem erdos_1062.variants.lower_bound (n : ℕ) : ⌈(2 * n / 3 : ℝ)⌉₊ ≤ f n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1062.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1062.lean#L55).

## `Erdos1062.erdos_1062.variants.lebensold_bounds`

Solved: stated here without proof.

> Lebensold proved that for large `n`, the function `f n` lies between `0.6725 n` and
> `0.6736 n`.

```lean
theorem erdos_1062.variants.lebensold_bounds :
    ∀ᶠ n in atTop, (0.6725 : ℝ) * n ≤ f n ∧ f n ≤ (0.6736 : ℝ) * n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1062.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1062.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1062.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1062.lean)
- [erdosproblems.com/1062](https://www.erdosproblems.com/1062)
