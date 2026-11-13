---
declaration: theorem
origin: cited
lean: Erdos80.erdos_80.parts.i, Erdos80.erdos_80.parts.ii
statement: formalized
---

# Erdős Problem 80

> *References:*
> - [erdosproblems.com/80](https://www.erdosproblems.com/80)
> - [erdosproblems.com/600](https://www.erdosproblems.com/600), stated in
>   `FormalConjectures/ErdosProblems/600.lean`
> - [FoLo12] Fox, Jacob and Loh, Po-Shen, On a problem of Erdős and Rothschild on edges in
>   triangles. Combinatorica (2012), 619--628.
>
> 600 asks the same question from the other side. `Erdos600.eFunction n r` is the least edge
> count forcing some edge into `r` triangles; `f c n` here is the largest book forced once the
> edge count is at least $cn^2$. So `r ≤ f c n` and `Erdos600.eFunction n r ≤ c * n^2` say the
> same thing, and the two functions are inverse to each other in that sense. Both are built on
> `SimpleGraph.trianglesContaining`, which 600 introduced.

*Quoted from [FormalConjectures/ErdosProblems/80.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/80.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/80](https://www.erdosproblems.com/80).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `Erdos80.erdos_80.parts.i`

Solved: stated here without proof.

> Let $c>0$ and let $f_c(n)$ be the maximal $m$ such that every graph $G$ with $n$ vertices and
> at least $cn^2$ edges, where each edge is contained in at least one triangle, must contain a
> book of size $m$, that is, an edge shared by at least $m$ different triangles. Estimate
> $f_c(n)$. In particular, is it true that $f_c(n)>n^\epsilon$ for some $\epsilon>0$?
>
> The answer is no. Fox and Loh [FoLo12] proved that $f_c(n) \leq n^{O(1/\log\log n)}$ for every
> fixed $c < 1/4$, so no $\epsilon > 0$ works for, say, $c = 1/8$. For $c > 1/4$ the situation is
> different: $f_c(n) \geq n/6$, see [erdosproblems.com/80](https://www.erdosproblems.com/80).
>
> The bound $c < 1/2$ is what makes the hypothesis satisfiable: a simple graph on $n$ vertices
> has at most $n(n-1)/2$ edges, so no graph has $cn^2$ of them once $c \geq 1/2$.

```lean
theorem erdos_80.parts.i :
    ¬ ∀ c : ℝ, 0 < c → c < 1 / 2 →
      ∃ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (n : ℝ) ^ ε < f c n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/80.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/80.lean#L86).

## `Erdos80.erdos_80.parts.ii`

Open: stated without proof.

> The weaker question from the same problem: is $f_c(n) \gg \log n$?
>
> Same feasibility bound on `c` as above.

```lean
theorem erdos_80.parts.ii :
    ∀ c : ℝ, 0 < c → c < 1 / 2 →
      (fun n : ℕ ↦ (f c n : ℝ)) ≫ (fun n : ℕ ↦ Real.log n)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/80.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/80.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/80.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/80.lean)
- [erdosproblems.com/80](https://www.erdosproblems.com/80)
