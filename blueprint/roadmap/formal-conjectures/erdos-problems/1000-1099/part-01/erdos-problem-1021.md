---
declaration: theorem
origin: cited
lean: Erdos1021.erdos_1021, Erdos1021.erdos_1021.variants.janzer
statement: formalized
---

# Erdős Problem 1021

> *References:*
> - [erdosproblems.com/1021](https://www.erdosproblems.com/1021)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Er74c] Erdős, Paul, *Extremal problems on graphs and hypergraphs*. (1974), 75-84.
> - [CoLe21] Conlon, David and Lee, Joonkyung, *On the extremal number of subdivisions*. Int. Math.
>   Res. Not. IMRN (2021), 9122--9145.
> - [Ja19] Janzer, Oliver, *Improved bounds for the extremal number of subdivisions*. Electron. J.
>   Combin. (2019), Paper No. 3.3, 6.

*Quoted from [FormalConjectures/ErdosProblems/1021.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1021.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1021](https://www.erdosproblems.com/1021).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1021.erdos_1021`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1021.lean#L2359](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1021.lean#L2359).

> Is it true that, for every $k \geq 3$, there is a constant $c_k > 0$ such that
>
> $$\mathrm{ex}(n, G_k) \ll n^{3/2 - c_k},$$
>
> where $G_k$ is the bipartite graph between $\{y_1, \ldots, y_k\}$ and
> $\{z_1, \ldots, z_{\binom{k}{2}}\}$, with each $z_j$ joined to a unique pair of $y_i$?
>
> A conjecture of Erdős and Simonovits [Er71, Er74c], who proved (in unpublished work) that one must
> have $c_k \to 0$ as $k \to \infty$. The graph $G_k$ is the $1$-subdivision of $K_k$; for $k = 3$
> it is the $6$-cycle. This was proved by Conlon and Lee [CoLe21] with $c_k = 6^{-k}$, improved to
> $c_k = \frac{1}{4k - 6}$ by Janzer [Ja19]; see `erdos_1021.variants.janzer`.

```lean
theorem erdos_1021 :
    ∀ k : ℕ, 3 ≤ k → ∃ c : ℝ, 0 < c ∧
      (fun n : ℕ ↦ (SimpleGraph.extremalNumber n (cliqueSubdivision k) : ℝ)) =O[atTop]
        fun n : ℕ ↦ (n : ℝ) ^ (3 / 2 - c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1021.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1021.lean#L73).

## `Erdos1021.erdos_1021.variants.janzer`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1021.lean#L2336](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1021.lean#L2336).

> Janzer [Ja19] proved that one can take $c_k = \frac{1}{4k - 6}$.

```lean
theorem erdos_1021.variants.janzer (k : ℕ) (hk : 3 ≤ k) :
    (fun n : ℕ ↦ (SimpleGraph.extremalNumber n (cliqueSubdivision k) : ℝ)) =O[atTop]
      fun n : ℕ ↦ (n : ℝ) ^ (3 / 2 - 1 / (4 * (k : ℝ) - 6))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1021.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1021.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1021.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1021.lean)
- [erdosproblems.com/1021](https://www.erdosproblems.com/1021)
