---
declaration: theorem
origin: cited
lean: Erdos926.erdos_926, Erdos926.erdos_926.variants.aks
statement: formalized
---

# Erdős Problem 926

> *References:*
> - [erdosproblems.com/926](https://www.erdosproblems.com/926)
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Er74c] Erdős, Paul, *Extremal problems on graphs and hypergraphs*. (1974), 75-84.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [Fu91] Füredi, Zoltán, *On a Turán type problem of Erdős*. Combinatorica (1991), 75--79.
> - [AKS03] Alon, Noga and Krivelevich, Michael and Sudakov, Benny, *Turán numbers of bipartite
>   graphs and related Ramsey-type questions*. Combin. Probab. Comput. (2003), 477-494.

*Quoted from [FormalConjectures/ErdosProblems/926.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/926.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/926](https://www.erdosproblems.com/926).

The file states 2 research or textbook statements: 2 solved.

## `Erdos926.erdos_926`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos926.lean#L644](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos926.lean#L644).

> Let $k\geq 4$. Is it true that
> $$\mathrm{ex}(n;H_k) \ll_k n^{3/2},$$
> where $H_k$ is the graph on vertices $x,y_1,\ldots,y_k,z_1,\ldots,z_{\binom{k}{2}}$, where $x$ is
> adjacent to all $y_i$ and each pair of $y_i,y_j$ is adjacent to a unique $z_i$.
>
> It is trivial that $\mathrm{ex}(n;H_k)\gg n^{3/2}$ since $H_k$ contians a $C_4$ for $k\geq 3$.
> Erdős [Er71] claimed a proof for $k=3$.
>
> The answer is yes, proved by Füredi [Fu91], who proved that $\mathrm{ex}(n;H_k) \ll (kn)^{3/2}$.
> This was improved to $\mathrm{ex}(n;H_k) \ll kn^{3/2}$ by Alon, Krivelevich, and Sudakov [AKS03].
>
> Since each $H_k$ is 2-degenerate this is a special case of [146](https://www.erdosproblems.com/146).
> The extremal number of the graph $H_k$ with the vertex $x$ omitted is the subject of
> [1021](https://www.erdosproblems.com/1021).

```lean
theorem erdos_926 : ∀ k : ℕ, 4 ≤ k →
    (fun n : ℕ => (extremalNumber n (H k) : ℝ)) =O[atTop] fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/926.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/926.lean#L81).

## `Erdos926.erdos_926.variants.aks`

Solved: stated here without proof.

> Alon, Krivelevich, and Sudakov [AKS03] proved $\mathrm{ex}(n;H_k) \ll kn^{3/2}$ with an
> absolute implied constant.

```lean
theorem erdos_926.variants.aks : ∃ C : ℝ, ∀ k : ℕ, 4 ≤ k → ∀ n : ℕ,
    (extremalNumber n (H k) : ℝ) ≤ C * k * (n : ℝ) ^ (3 / 2 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/926.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/926.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/926.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/926.lean)
- [erdosproblems.com/926](https://www.erdosproblems.com/926)
