---
declaration: theorem
origin: cited
lean: Erdos1212.erdos_1212
statement: formalized
---

# Erdős Problem 1212

> *References:*
> - [erdosproblems.com/1212](https://www.erdosproblems.com/1212)
> - [Er80] Erdős, P., _Some notes on problems and results in number theory_ (1980), p. 114.
>
> This file also records machine-checked cores of verified partial results (2026):
> a composite-anchor sufficient reduction and an impossibility theorem for periodic
> certificates; see the corresponding lemmas below.

*Quoted from [FormalConjectures/ErdosProblems/1212.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1212.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1212](https://www.erdosproblems.com/1212).

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement and 6 API statements, counted here but not shown.

## `Erdos1212.erdos_1212`

Solved: stated here; a Lean proof is at [https://github.com/crabsatellite/erdos-1212-visible-lattice-path/blob/400001f0847afe36a26c588d34445210dbdc116e/kernel/Erdos1212Kernel/AlgebraicCorridorKernelAudit.lean](https://github.com/crabsatellite/erdos-1212-visible-lattice-path/blob/400001f0847afe36a26c588d34445210dbdc116e/kernel/Erdos1212Kernel/AlgebraicCorridorKernelAudit.lean).

> Let $G$ be the graph with vertex set those pairs $(x,y)\in \mathbb{N}^2$ with
> $\mathrm{gcd}(x,y)=1$, in which we join two vertices if the differ in only one coordinate, and
> there by $\pm 1$.
>
> Is there a path going to infinity on $G$, say $P$, such that for all $(x,y)\in P$ both
> $\min(x,y)>1$ and at least one of $x$ or $y$ is composite?
>
> The weaker version (only $\min(x,y) > 1$) was solved by C. Stewart via the prime-pair path
> $(p_k, p_{k+1}) \to (p_{k+1}, p_{k+2})$, as recounted in [Er80]; the compositeness condition
> forbids those anchors.
>
> The strengthened problem was solved by Alex Chengyu Li; see
> [Li's construction](https://crabresearch.com/research/erdos-1212-algebraic-corridors)
> and the accompanying
> [Lean formalization](https://github.com/crabsatellite/erdos-1212-visible-lattice-path).

```lean
theorem erdos_1212 :
    ∃ f : ℕ → ℕ × ℕ, Function.Injective f ∧ (∀ n, Adj (f n) (f (n + 1))) ∧
      (∀ n, Valid (f n)) ∧
      Tendsto (fun n => (f n).1 + (f n).2) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1212.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1212.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1212.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1212.lean)
- [erdosproblems.com/1212](https://www.erdosproblems.com/1212)
