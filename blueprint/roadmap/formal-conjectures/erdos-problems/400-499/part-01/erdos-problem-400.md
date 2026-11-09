---
declaration: theorem
origin: cited
lean: Erdos400.erdos_400.parts.i, Erdos400.erdos_400.parts.ii, Erdos400.erdos_400.variants.upper_bound
statement: formalized
---

# Erdős Problem 400

> *Reference:* [erdosproblems.com/400](https://www.erdosproblems.com/400)

*Quoted from [FormalConjectures/ErdosProblems/400.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/400.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/400](https://www.erdosproblems.com/400).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos400.erdos_400.parts.i`

Open: stated without proof.

> Can one show that $\sum_{n\leq x}g_k(n) \sim c_k x\log x$ for some constant $c_k$?

```lean
theorem erdos_400.parts.i :
    ∀ᵉ (k ≥ 2), ∃ c : ℝ,
      (fun x : ℕ ↦ (∑ n ∈ Icc 1 x, (g k n : ℝ))) ~[atTop]
      (fun x : ℕ ↦ c * x * Real.log x)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/400.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/400.lean#L44).

## `Erdos400.erdos_400.parts.ii`

Open: stated without proof.

> Is it true that there is a constant $c_k$ such that for almost all $n < x$ we have
> $g_k(n)=c_k\log x+o(\log x)$?

```lean
theorem erdos_400.parts.ii :
    ∀ᵉ (k ≥ 2), ∃ c : ℝ, ∀ ε > 0,
      Tendsto (fun x : ℕ ↦
        (((Icc 1 x).filter (fun n ↦
          |(g k n : ℝ) - c * Real.log x| ≤ ε * Real.log x)).card : ℝ) / x)
        atTop (𝓝 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/400.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/400.lean#L55).

## `Erdos400.erdos_400.variants.upper_bound`

Solved: stated here without proof.

> Erdős and Graham write that it is easy to show that $g_k(n) \ll_k \log n$ always, but the best
> possible constant is unknown.

```lean
theorem erdos_400.variants.upper_bound (k : ℕ) (hk : k ≥ 2) :
    (fun n : ℕ ↦ (g k n : ℝ)) ≪ (fun n : ℕ ↦ Real.log (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/400.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/400.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/400.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/400.lean)
- [erdosproblems.com/400](https://www.erdosproblems.com/400)
