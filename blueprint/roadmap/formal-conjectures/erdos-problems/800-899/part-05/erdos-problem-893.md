---
declaration: theorem
origin: cited
lean: Erdos893.erdos_893, Erdos893.erdos_893.variants.unbounded
statement: formalized
---

# Erdős Problem 893

> *References:*
> - [erdosproblems.com/893](https://www.erdosproblems.com/893)
> - [KoLu25] V. Kovač and F. Luca, On the number of divisors of Mersenne numbers. arXiv:2506.04883 (2025).

*Quoted from [FormalConjectures/ErdosProblems/893.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/893.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/893](https://www.erdosproblems.com/893).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos893.erdos_893`

Open: stated without proof.

> Does the limit $\lim_{n\to\infty} \frac{f(2n)}{f(n)}$ tend to infinity?
>
> (Other finite limits have been ruled out by [KoLu25], see below)

```lean
theorem erdos_893 :
    Tendsto (fun n : ℕ => (f (2 * n) : ℝ) / (f n : ℝ)) atTop atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/893.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/893.lean#L47).

## `Erdos893.erdos_893.variants.unbounded`

Solved: stated here without proof.

> Kovač and Luca [KoLu25] (building on a heuristic independently found by
> Cambie (personal communication)) have shown that there is no finite limit, in that
> $\lim_{n\to\infty} \frac{f(2n)}{f(n)}$ is unbounded.

```lean
theorem erdos_893.variants.unbounded :
   ¬ BddAbove (Set.range fun n : ℕ => (f (2 * n) : ℝ) / f n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/893.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/893.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/893.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/893.lean)
- [erdosproblems.com/893](https://www.erdosproblems.com/893)
