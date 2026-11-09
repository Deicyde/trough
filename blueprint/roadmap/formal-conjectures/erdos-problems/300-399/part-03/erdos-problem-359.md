---
declaration: theorem
origin: cited
lean: Erdos359.erdos_359.parts.i, Erdos359.erdos_359.parts.ii, Erdos359.erdos_359.variants.isGoodFor_1_asymptotic
statement: formalized
---

# Erdős Problem 359

> *Reference:* [erdosproblems.com/359](https://www.erdosproblems.com/359)

*Quoted from [FormalConjectures/ErdosProblems/359.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/359.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/359](https://www.erdosproblems.com/359).

The file states 3 research or textbook statements: 3 open. It also has 1 test statement, counted here but not shown.

## `Erdos359.erdos_359.parts.i`

Open: stated without proof.

> Let $a_1< a_2 < ⋯ $ be an infinite sequence of integers such that $a_1=1$ and $a_{i+1}$ is the
> least integer which is not a sum of consecutive earlier $a_j$s. Show that $a_k / k \to \infty$.

```lean
theorem erdos_359.parts.i (A : ℕ → ℕ) (hA : IsGoodFor A 1) :
    atTop.Tendsto (fun k ↦ (A k : ℝ) / k) atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/359.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/359.lean#L42).

## `Erdos359.erdos_359.parts.ii`

Open: stated without proof.

> Let $a_1< a_2 < ⋯ $ be an infinite sequence of integers such that $a_1=1$ and $a_{i+1}$ is the
> least integer which is not a sum of consecutive earlier $a_j$s. Show that $a_k / k ^ {1 + c} \to 0$
> for any $c > 0$.

```lean
theorem erdos_359.parts.ii (A : ℕ → ℕ) (hA : IsGoodFor A 1) (c : ℝ) (hc : 0 < c):
    atTop.Tendsto (fun k ↦ A k / (k : ℝ) ^ (1 + c)) (nhds 0)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/359.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/359.lean#L50).

## `Erdos359.erdos_359.variants.isGoodFor_1_asymptotic`

Open: stated without proof.

> Suppose monotone sequence $A$ satisfies the following: `A 0 = 1` and for all `j`, `A (j + 1)` is the
> smallest natural number that cannot be written as a sum of consecutive terms of `A 0, ..., A j`.
> Then it is conjectured that $$a_k ~ \frac{k \log k}{\log \log k}$$.

```lean
theorem erdos_359.variants.isGoodFor_1_asymptotic (A : ℕ → ℕ) (hA : IsGoodFor A 1) :
    (fun k ↦ (A k : ℝ)) ~[atTop] (fun k ↦ k * (k : ℝ).log / (k : ℝ).log.log)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/359.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/359.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/359.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/359.lean)
- [erdosproblems.com/359](https://www.erdosproblems.com/359)
