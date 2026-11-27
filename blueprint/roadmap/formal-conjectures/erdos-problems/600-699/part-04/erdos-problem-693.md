---
declaration: theorem
origin: cited
lean: Erdos693.erdos_693
statement: formalized
---

# Erdős Problem 693

> *References:*
> - [erdosproblems.com/693](https://www.erdosproblems.com/693)
> - [Er79e] Erdős, Paul, *Some unconventional problems in number theory*.
>   Astérisque **61** (1979), 73–82.
>   https://www.numdam.org/article/AST_1979__61__73_0.pdf
>
> See also [Erdős problem 446](https://www.erdosproblems.com/446).

*Quoted from [FormalConjectures/ErdosProblems/693.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/693.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/693](https://www.erdosproblems.com/693).

The file states 1 research or textbook statement: 1 open. It also has 3 test statements, counted here but not shown.

## `Erdos693.erdos_693`

Open: stated without proof.

> Let $k \geq 2$ and let $n$ be sufficiently large depending on $k$. Let
> $A = \{a_1 < a_2 < \cdots\}$ be the set of integers in $[n,n^k]$ which have a divisor in
> $(n,2n)$. Is $\max_i (a_{i+1} - a_i) \leq (\log n)^{O(1)}$?
>
> The exponent is independent of $k$, while the threshold for $n$ may depend on $k$
> [Er79e, p. 78].

```lean
theorem erdos_693 : ∃ C : ℕ, ∀ k ≥ 2, ∀ᶠ n in atTop,
    MaxGapAtMost (divisorWindowSet k n) ((Real.log (n : ℝ)) ^ C)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/693.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/693.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/693.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/693.lean)
- [erdosproblems.com/693](https://www.erdosproblems.com/693)
