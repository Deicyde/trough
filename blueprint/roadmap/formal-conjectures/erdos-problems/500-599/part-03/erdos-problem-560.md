---
declaration: theorem
origin: cited
lean: Erdos560.erdos_560, Erdos560.erdos_560.variants.lower_bound, Erdos560.erdos_560.variants.upper_bound, Erdos560.erdos_560.variants.conlon_fox_wigderson
statement: formalized
---

# Erdős Problem 560

> *References:*
> - [erdosproblems.com/560](https://www.erdosproblems.com/560)
> - [EFRS82] Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., Ramsey numbers
>   for brooms. Proceedings of the thirteenth Southeastern conference on combinatorics, graph
>   theory and computing (1982), 283-293.
> - [ErRo93] Erdős, P. and Rousseau, C. C., The size Ramsey number of a complete bipartite graph.
>   Discrete Math. (1993), 259-262.
> - [EFRS78b] Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., The size Ramsey
>   number. Period. Math. Hungar. (1978), 145-161.
> - [NeRo78] Nešetřil, J. and Rödl, V., The structure of critical Ramsey graphs.
>   Acta Math. Acad. Sci. Hungar. (1978), 295-300.
> - [CFW23] Conlon, D. and Fox, J. and Wigderson, Y., Three early problems on size Ramsey numbers.
>   Combinatorica (2023), 743-768.

*Quoted from [FormalConjectures/ErdosProblems/560.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/560.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/560](https://www.erdosproblems.com/560).

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Erdos560.erdos_560`

Open: stated without proof.

> Let $\hat{R}(G)$ denote the size Ramsey number, the minimal number of edges $m$ such that there
> is a graph $H$ with $m$ edges such that in any $2$-colouring of the edges of $H$ there is a
> monochromatic copy of $G$.
>
> Determine
> $$\hat{R}(K_{n,n}),$$
> where $K_{n,n}$ is the complete bipartite graph with $n$ vertices in each component.

```lean
theorem erdos_560 : erdos_560.answer = (fun n : ℕ ↦ r̂(n))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/560.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/560.lean#L61).

## `Erdos560.erdos_560.variants.lower_bound`

Solved: stated here without proof.

> The lower bound (which holds for $n\geq 6$) was proved by Erdős and Rousseau [ErRo93]:
> $$\frac{1}{60}n^22^n\lt \hat{R}(K_{n,n}).$$

```lean
theorem erdos_560.variants.lower_bound :
    ∀ (n : ℕ), 6 ≤ n → (1 / 60 : ℝ) * (n : ℝ) ^ 2 * 2 ^ n < r̂(n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/560.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/560.lean#L69).

## `Erdos560.erdos_560.variants.upper_bound`

Solved: stated here without proof.

> The upper bound was proved by Erdős, Faudree, Rousseau, and Schelp [EFRS78b] and Nešetřil
> and Rödl [NeRo78]:
> $$\hat{R}(K_{n,n})\lt \frac{3}{2}n^32^n.$$
> We require $n\geq 1$ because the strict inequality fails for the empty graph.

```lean
theorem erdos_560.variants.upper_bound :
    ∀ (n : ℕ), 1 ≤ n → (r̂(n) : ℝ) < (3 / 2 : ℝ) * (n : ℝ) ^ 3 * 2 ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/560.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/560.lean#L80).

## `Erdos560.erdos_560.variants.conlon_fox_wigderson`

Open: stated without proof.

> Conlon, Fox, and Wigderson [CFW23] conjecture that
> $$\hat{R}(K_{s,t})\asymp s^2t2^s$$
> for all $s\leq t$, and so in particular we should have
> $$\hat{R}(K_{n,n})\asymp n^32^n.$$

```lean
theorem erdos_560.variants.conlon_fox_wigderson :
    (fun n : ℕ ↦ (r̂(n) : ℝ)) =Θ[atTop] (fun n : ℕ ↦ (n : ℝ) ^ 3 * 2 ^ n)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/560.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/560.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/560.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/560.lean)
- [erdosproblems.com/560](https://www.erdosproblems.com/560)
