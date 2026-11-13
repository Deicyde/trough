---
declaration: theorem
origin: cited
lean: Erdos1053.erdos_1053, Erdos1053.erdos_1053.variants.guy
statement: formalized
---

# Erdős Problem 1053

> *References:*
> - [erdosproblems.com/1053](https://www.erdosproblems.com/1053)
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. Springer-Verlag, New York (2004).

*Quoted from [FormalConjectures/ErdosProblems/1053.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1053.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1053](https://www.erdosproblems.com/1053).

The file states 2 research or textbook statements: 2 open.

## `Erdos1053.erdos_1053`

Open: stated without proof.

> Call a number $k$-perfect if $\sigma(n)=kn$, where $\sigma(n)$ is the sum of the divisors
> of $n$. Must $k=o(\log\log n)$?
>
> A question of Erdős, as reported in problem B2 of Guy's collection [Gu04].
> The little-$o$ relation is taken as $n \to \infty$ within the positive integers for which
> $\sigma(n) = kn$ for some $k$; on this set, $\sigma(n)/n$ is precisely that multiplier $k$.

```lean
theorem erdos_1053 :
    (fun n : ℕ ↦ (σ 1 n : ℝ) / (n : ℝ)) =o[atTop ⊓ 𝓟 {n : ℕ | ∃ k, Nat.IsPerfectFor n 1 k}]
      (fun n : ℕ ↦ Real.log (Real.log (n : ℝ)))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1053.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1053.lean#L44).

## `Erdos1053.erdos_1053.variants.guy`

Open: stated without proof.

> Guy further writes 'It has even been suggested that there may be only finitely many $k$-perfect
> numbers with $k\geq 3$.'

```lean
theorem erdos_1053.variants.guy :
    ∀ k ≥ 3, {n : ℕ | Nat.IsPerfectFor n 1 k}.Finite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1053.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1053.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1053.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1053.lean)
- [erdosproblems.com/1053](https://www.erdosproblems.com/1053)
