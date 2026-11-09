---
declaration: theorem
origin: cited
lean: Erdos659.erdos_659
statement: formalized
---

# Erdős Problem 659

> *References:*
> - [erdosproblems.com/659](https://www.erdosproblems.com/659)
> - [MoOs06] Moree, Pieter and Osburn, Robert, Two-dimensional lattices with few distances. Enseign. Math. (2) (2006), 361--380
> - [ErFi96] Erdős, Paul and Fishburn, Peter, Maximum planar sets that determine {$k$} distances. Discrete Math. (1996), 115--125.
> - [Gr26](https://arxiv.org/abs/2601.09102): Benjamin Grayzel, Solution to a Problem of Erdős Concerning Distances and Points

*Quoted from [FormalConjectures/ErdosProblems/659.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/659.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/659](https://www.erdosproblems.com/659).

The file states 1 research or textbook statement: 1 solved.

## `Erdos659.erdos_659`

Solved: stated here without proof.

> Is there a set of $n$ points in $\mathbb{R}^2$ such that every subset of $4$ points determines at
> least $3$ distances, yet the total number of distinct distances is $\ll \frac{n}{\sqrt{\log n}}$?
>
> There does exist such a set: a suitable truncation of the lattice
> $\{(a,b\sqrt{2}): a,b\in\mathbb{Z}\}$ suffices. This construction appears to have been first
> considered by Moree and Osburn \cite{MoOs06}, who proved that it has
>  $\ll \frac{n}{\sqrt{\log n}}$ many distinct distances. This construction was independently found by
>  [Lund and Sheffer](https://adamsheffer.wordpress.com/2014/07/16/point-sets-with-few-distinct-distances/),
>  who further noted that this configuration contains no squares or equilateral triangles.
>
> There are only six possible configurations of $4$ points which determine only $2$ distances
> (first noted by Erdős and Fishburn [ErFi96]), and five of them contain either a square or an
> equilateral triangle. The remaining configuration contains four points from a regular pentagon,
> and Grayzel [Gr26] (using Gemini) has noted in the comments that this configuration can also be
> ruled out, thus giving a complete solution to this problem.
>
> Boris Alexeev provides a formalisation of the reduction, which is conditional on Bernays' theorem
> (assumed as an axiom in the proof to obtain the $O(n/\sqrt{\log n})$ bound).
> See the [formal proof](https://github.com/plby/lean-proofs/blob/226d5fad7143dcebea2bbb5ec87f18a3a1dcea69/src/v4.24.0/ErdosProblems/Erdos659.lean).

```lean
theorem erdos_659 : ∃ A : ℕ → Finset ℝ²,
   (∀ n, #(A n) = n ∧ ∀ S ⊆ A n, #S = 4 → 3 ≤ distinctDistances S) ∧
    (fun n ↦ distinctDistances (A n)) ≪ fun n ↦ n / sqrt (log n)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/659.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/659.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/659.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/659.lean)
- [erdosproblems.com/659](https://www.erdosproblems.com/659)
