---
declaration: theorem
origin: cited
lean: Erdos959.erdos_959, Erdos959.erdos_959.lower_bound
statement: formalized
---

# Erdős Problem 959

> *Reference:* [erdosproblems.com/959](https://www.erdosproblems.com/959)

*Quoted from [FormalConjectures/ErdosProblems/959.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/959.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/959](https://www.erdosproblems.com/959).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos959.erdos_959`

Open: stated without proof.

> Let $A\subseteq \mathbb{R}^2$ be a set of size $n$ and let $\{d_1,\ldots,d_k\}$ be
> the set of distinct distances determined by $A$. Let $f(d)$ be the number of times
> the distance $d$ is determined, ordered so that
> $f(d_1)\geq f(d_2)\geq \cdots \geq f(d_k)$. Estimate
>
> $$\max (f(d_1)-f(d_2)),$$
>
> where the maximum is taken over all $A$ of size $n$ (this is `extremalGap n`).

```lean
theorem erdos_959 :
    (fun n ↦ (extremalGap n : ℝ)) =Θ[atTop] erdos_959.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/959.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/959.lean#L85).

## `Erdos959.erdos_959.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-959/Research/FinalLowerBound.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-959/Research/FinalLowerBound.lean).

> A superlinear lower bound: there is a $c>0$ with
>
> $$\text{extremalGap}(n)\geq n^{1 + c/\log\log n}$$
>
> for all large $n$, so $\max (f(d_1)-f(d_2))$ grows faster than any linear function
> of $n$. Determining the exact order remains open, which is `erdos_959`.

```lean
theorem erdos_959.lower_bound :
    ∃ c : ℝ, 0 < c ∧ ∃ N : ℕ, ∀ n ≥ N,
      (n : ℝ) ^ (1 + c / Real.log (Real.log n)) ≤ extremalGap n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/959.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/959.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/959.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/959.lean)
- [erdosproblems.com/959](https://www.erdosproblems.com/959)
