---
declaration: theorem
origin: cited
lean: Erdos483.erdos_483
statement: formalized
---

# Erdős Problem 483

> *References:*
> - [erdosproblems.com/483](https://www.erdosproblems.com/483)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl.
>   (1961), 221-254, p.233, Problem 20.

*Quoted from [FormalConjectures/ErdosProblems/483.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/483.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/483](https://www.erdosproblems.com/483).

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `Erdos483.erdos_483`

Open: stated without proof.

> Let $f(k)$ be the minimal $N$ such that if $\{1,\ldots,N\}$ is $k$-coloured then
> there is a monochromatic solution to $a+b=c$. Estimate $f(k)$. In particular, is it true
> that $f(k) < c^k$ for some constant $c>0$?
>
> The exponential bound is stated directly: for every positive number of colours, there is
> a forcing interval of length strictly below $c^k$. This is equivalent to the bound on the
> least forcing threshold and avoids choosing a default value for that threshold.

```lean
theorem erdos_483 :
    ∃ C : ℝ, 0 < C ∧ ∀ k : ℕ, 0 < k →
      ∃ N : ℕ, (N : ℝ) < C ^ k ∧ Forces k N
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/483.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/483.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/483.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/483.lean)
- [erdosproblems.com/483](https://www.erdosproblems.com/483)
