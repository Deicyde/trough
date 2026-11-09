---
declaration: theorem
origin: cited
lean: Erdos706.erdos_706
statement: formalized
---

# Erdős Problem 706

> *References:*
> - [erdosproblems.com/706](https://www.erdosproblems.com/706)
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.

*Quoted from [FormalConjectures/ErdosProblems/706.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/706.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/706](https://www.erdosproblems.com/706).

The file states 1 research or textbook statement: 1 open.

## `Erdos706.erdos_706`

Open: stated without proof.

> Let $L(r)$ be such that if $G$ is a graph formed by taking a finite set of points $P$ in
> $\mathbb{R}^2$ and some set $A\subset (0,\infty)$ of size $r$, where the vertex set is $P$ and
> there is an edge between two points if and only if their distance is a member of $A$, then
> $\chi(G)\leq L(r)$.
>
> Estimate $L(r)$. In particular, is it true that $L(r)\leq r^{O(1)}$?
>
> The case $r=1$ is the Hadwiger-Nelson problem, for which it is known that
> $5\leq L(1)\leq 7$.
>
> See also [508](https://www.erdosproblems.com/508), [704](https://www.erdosproblems.com/704),
> and [705](https://www.erdosproblems.com/705).
>
> Here $L(r)\leq r^{O(1)}$ is read as: there is $C$ with $\chi(G)\leq r^C$ for all large $r$. Small
> $r$ must be excluded, since $L(1)\geq 5 > 1^C$.

```lean
theorem erdos_706 :
    ∃ C : ℕ, ∀ᶠ r : ℕ in atTop, ∀ (P : Finset ℝ²) (A : Finset ℝ), A.card = r →
      (∀ a ∈ A, 0 < a) →
      (SimpleGraph.DistancePlaneGraph (A : Set ℝ) (P : Set ℝ²)).chromaticNumber ≤
        (r ^ C : ℕ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/706.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/706.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/706.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/706.lean)
- [erdosproblems.com/706](https://www.erdosproblems.com/706)
