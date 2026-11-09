---
declaration: theorem
origin: cited
lean: Erdos629.erdos_629, Erdos629.erdos_629.variants.ert_bounds, Erdos629.erdos_629.variants.property_b, Erdos629.erdos_629.variants.radhakrishnan_srinivasan, Erdos629.erdos_629.variants.n_two, Erdos629.erdos_629.variants.n_three, Erdos629.erdos_629.variants.hmt_recursion
statement: formalized
---

# Erdős Problem 629

> *References:*
> - [erdosproblems.com/629](https://www.erdosproblems.com/629)
> - [ERT80] Erdős, Paul and Rubin, Arthur L. and Taylor, Herbert, *Choosability in graphs*.
>   Proceedings of the West Coast Conference on Combinatorics, Graph Theory and Computing (1979),
>   Congress. Numer. XXVI (1980), 125-157. [PDF](https://www.renyi.hu/~p_erdos/1980-07.pdf)
> - [HMT96] Hanson, Denis and MacGillivray, Gary and Toft, Bjarne, *Choosability of bipartite
>   graphs*. Ars Combin. (1996), 183-192.
> - [RaSr00] Radhakrishnan, Jaikumar and Srinivasan, Aravind, *Improved bounds and algorithms for
>   hypergraph $2$-coloring*. Random Structures Algorithms (2000), 4-32.

*Quoted from [FormalConjectures/ErdosProblems/629.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/629](https://www.erdosproblems.com/629).

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 1 API statement, counted here but not shown.

## `Erdos629.erdos_629`

Open: stated without proof.

> The list chromatic number $\chi_L(G)$ is defined to be the minimal $k$ such that for any
> assignment of a list of $k$ colours to each vertex of $G$ (perhaps different lists for different
> vertices) a colouring of each vertex by a colour on its list can be chosen such that adjacent
> vertices receive distinct colours.
>
> Determine the minimal number of vertices $n(k)$ of a bipartite graph $G$ such that
> $\chi_L(G)>k$.

```lean
theorem erdos_629 : n = erdos_629.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L64).

## `Erdos629.erdos_629.variants.ert_bounds`

Solved: stated here without proof.

> A problem of Erdős, Rubin, and Taylor [ERT80], who proved that
> $$2^{k-1}\lt n(k) \lt k^22^{k+2}.$$
>
> The chain of inequalities in [ERT80, p. 129] needs $k \geq 2$, since $m(1) = 1 = 2^0$; for
> $k = 1$ the claim holds because $n(1) = 2$. The case $k = 0$ is degenerate ($n(0) = 1$).

```lean
theorem erdos_629.variants.ert_bounds (k : ℕ) (hk : 1 ≤ k) :
    2 ^ (k - 1) < n k ∧ n k < k ^ 2 * 2 ^ (k + 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L75).

## `Erdos629.erdos_629.variants.property_b`

Solved: stated here without proof.

> They also prove that if $m(k)$ is the size of the smallest family of $k$-sets without property B
> (i.e. the smallest number of $k$-sets in a graph with chromatic number $3$) then
> $m(k)\leq n(k)\leq m(k+1)$.
>
> [ERT80, p. 129] prints the upper bound as $2m(k)$; we state that form. Here $m(k)$ is
> `Hypergraph.minChromaticEdges k 3`, as in Erdős Problem 901. We assume $k \geq 2$: for $k = 1$
> this is `⊤`, since singleton edges admit no proper colouring, whereas $m(1) = 1$.

```lean
theorem erdos_629.variants.property_b (k : ℕ) (hk : 2 ≤ k) :
    (Hypergraph.minChromaticEdges k 3).toNat ≤ n k ∧
      n k ≤ 2 * (Hypergraph.minChromaticEdges k 3).toNat
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L89).

## `Erdos629.erdos_629.variants.radhakrishnan_srinivasan`

Solved: stated here without proof.

> The lower bounds on $m(k)$ by Radhakrishnan and Srinivasan [RaSr00] imply that
> $$2^k \left(\frac{k}{\log k}\right)^{1/2}\ll n(k).$$

```lean
theorem erdos_629.variants.radhakrishnan_srinivasan :
    ∃ c > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      c * 2 ^ k * Real.sqrt (k / Real.log k) ≤ (n k : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L99).

## `Erdos629.erdos_629.variants.n_two`

Solved: stated here without proof.

> Erdős, Rubin, and Taylor [ERT80] proved $n(2)=6$.

```lean
theorem erdos_629.variants.n_two : n 2 = 6
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L108).

## `Erdos629.erdos_629.variants.n_three`

Solved: stated here without proof.

> Hanson, MacGillivray, and Toft [HMT96] proved $n(3)=14$.

```lean
theorem erdos_629.variants.n_three : n 3 = 14
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L115).

## `Erdos629.erdos_629.variants.hmt_recursion`

Solved: stated here without proof.

> Hanson, MacGillivray, and Toft [HMT96] proved
> $$n(k) \leq kn(k-2)+2^k.$$

```lean
theorem erdos_629.variants.hmt_recursion (k : ℕ) (hk : 2 ≤ k) :
    n k ≤ k * n (k - 2) + 2 ^ k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/629.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/629.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/629.lean)
- [erdosproblems.com/629](https://www.erdosproblems.com/629)
