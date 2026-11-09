---
declaration: theorem
origin: cited
lean: Erdos113.erdos_113
statement: formalized
---

# Erdős Problem 113

> *References:*
> - [erdosproblems.com/113](https://www.erdosproblems.com/113)
> - [ErSi84] Erdős, P. and Simonovits, M., *Cube-supersaturated graphs and related problems*.
>   Progress in graph theory (Waterloo, Ont., 1982) (1984), 203-218.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [Ja23b] Janzer, Oliver, *Disproof of a conjecture of Erdős and Simonovits on the Turán number
>   of graphs with minimum degree 3*. Int. Math. Res. Not. IMRN (2023), 8478--8494.

*Quoted from [FormalConjectures/ErdosProblems/113.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/113.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/113](https://www.erdosproblems.com/113).

The file states 1 research or textbook statement: 1 solved.

## `Erdos113.erdos_113`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos113.lean#L4902](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos113.lean#L4902).

> If $G$ is bipartite then $\mathrm{ex}(n;G)\ll n^{3/2}$ if and only $G$ is $2$-degenerate, that
> is, $G$ contains no induced subgraph with minimal degree at least 3.
>
> Conjectured by Erdős and Simonovits [ErSi84]. Erdős first offered \$250 for a proof and \$100 for
> a counterexample, but in [Er93] offered \$500 for a counterexample. Disproved by Janzer [Ja23b]
> who constructed, for any $\epsilon>0$, a $3$-regular bipartite graph $H$ such that
> $$\mathrm{ex}(n;H)\ll n^{\frac{4}{3}+\epsilon}.$$
>
> See also [146](https://www.erdosproblems.com/146) and [147](https://www.erdosproblems.com/147).
>
> The linked formal proof refutes the "only if" direction via Janzer's construction.

```lean
theorem erdos_113 : ¬ ∀ (V : Type) [Fintype V] (G : SimpleGraph V), G.IsBipartite →
    (((fun n : ℕ => (extremalNumber n G : ℝ)) =O[atTop] fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ)) ↔
      G.IsDegenerate 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/113.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/113.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/113.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/113.lean)
- [erdosproblems.com/113](https://www.erdosproblems.com/113)
