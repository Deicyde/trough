---
declaration: theorem
origin: cited
lean: Erdos911.erdos_911
statement: formalized
---

# Erdős Problem 911

> *References:*
> - [erdosproblems.com/911](https://www.erdosproblems.com/911)
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
>   (1982), 59--79.

*Quoted from [FormalConjectures/ErdosProblems/911.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/911.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/911](https://www.erdosproblems.com/911).

The file states 1 research or textbook statement: 1 open.

## `Erdos911.erdos_911`

Open: stated without proof.

> Let $\hat{R}(G)$ denote the size Ramsey number, the minimal number of edges $m$ such that there is
> a graph $H$ with $m$ edges that is Ramsey for $G$.
>
> Is there a function $f$ such that $f(x)/x\to \infty$ as $x\to \infty$ such that, for all large $C$,
> if $G$ is a graph with $n$ vertices and $e\geq Cn$ edges then
> $$\hat{R}(G) > f(C) e?$$
>
> Here $\hat{R}(G)$ is `sizeRamsey G G`, and $G$ has at least one vertex (for $n = 0$ the
> inequality fails trivially).

```lean
theorem erdos_911 :
    ∃ f : ℝ → ℝ, Tendsto (fun x ↦ f x / x) atTop atTop ∧
      ∃ C₀ : ℝ, ∀ C ≥ C₀, ∀ (n : ℕ) (G : SimpleGraph (Fin n)), 0 < n →
        C * n ≤ (G.edgeSet.ncard : ℝ) →
          f C * G.edgeSet.ncard < (sizeRamsey G G : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/911.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/911.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/911.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/911.lean)
- [erdosproblems.com/911](https://www.erdosproblems.com/911)
