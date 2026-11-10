---
declaration: theorem
origin: cited
lean: Erdos160.erdos_160.known_upper, Erdos160.erdos_160.better_upper, Erdos160.erdos_160.better_lower, Erdos160.erdos_160.variants.known_lower
statement: formalized
---

# Erdős Problem 160

> *Reference:* [erdosproblems.com/160](https://www.erdosproblems.com/160)

*Quoted from [FormalConjectures/ErdosProblems/160.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/160.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/160](https://www.erdosproblems.com/160).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos160.erdos_160.known_upper`

Solved: stated here without proof.

> On [Mathoverflow](https://mathoverflow.net/a/410815) user
> [leechlattice](https://mathoverflow.net/users/125498/leechlattice) shows that
> $h(n) \ll n^{\frac 2 3}$.

```lean
theorem erdos_160.known_upper :
    (fun n => (erdos_160.h n : ℝ)) =O[atTop] fun n => (n : ℝ) ^ ((2 : ℝ) / 3)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/160.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/160.lean#L48).

## `Erdos160.erdos_160.better_upper`

Open: stated without proof.

> Estimate $h(n)$ by finding a better upper bound.

```lean
theorem erdos_160.better_upper :
    (fun n => (erdos_160.h n : ℝ)) =O[atTop] erdos_160.better_upper.answer ∧
    erdos_160.better_upper.answer =o[atTop] fun n => (n : ℝ) ^ ((2 : ℝ) / 3)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/160.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/160.lean#L60).

## `Erdos160.erdos_160.better_lower`

Open: stated without proof.

> Estimate $h(n)$ by finding a better lower bound.

```lean
theorem erdos_160.better_lower:
    (erdos_160.better_lower.answer =O[atTop] fun n => (erdos_160.h n : ℝ)) ∧
    ∀ c > 0,
    (fun (n : ℕ) => exp (c * log n ^ ((1 : ℝ) / 12))) =O[atTop] (fun n => (erdos_160.h n : ℝ)) →
    ∀ c > 0, (fun (n : ℕ) => exp (c * log n ^ ((1 : ℝ) / 12))) =o[atTop]
      erdos_160.better_lower.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/160.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/160.lean#L71).

## `Erdos160.erdos_160.variants.known_lower`

Solved: stated here without proof.

> The observation of Zachary Hunter in [that question](https://mathoverflow.net/q/410808)
> coupled with the bounds of Kelley-Meka [KeMe23](https://arxiv.org/abs/2302.05537) imply that
>
> $$h(N) \gg \exp(c(\log N)^{\frac 1 {12}})$$
>
> for some $c > 0$.

```lean
theorem erdos_160.variants.known_lower :
    ∃ c > 0, (fun (n : ℕ) => exp (c * log (n : ℝ) ^ ((1 : ℝ) / 12)))
    =O[atTop] fun n => (erdos_160.h n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/160.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/160.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/160.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/160.lean)
- [erdosproblems.com/160](https://www.erdosproblems.com/160)
