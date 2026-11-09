---
declaration: theorem
origin: cited
lean: Erdos814.erdos_814, Erdos814.erdos_814.variants.at_least, Erdos814.erdos_814.variants.sauermann
statement: formalized
---

# Erdős Problem 814

> *References:*
> - [erdosproblems.com/814](https://www.erdosproblems.com/814)
> - [EFRS90] Erdős, P. and Faudree, R. J. and Rousseau, C. C. and Schelp, R. H., _Subgraphs of
>   minimal degree k_. Discrete Math. (1990), 53--58.
> - [Er91] Erdős, P., _Problems and results in combinatorial analysis and combinatorial number
>   theory_. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [Er93] Erdős, Paul, _Some of my favorite solved and unsolved problems in graph theory_.
>   Quaestiones Math. (1993), 333-350.
> - [MNS17] Mousset, Frank and Noever, Andreas and Škorić, Nemanja, _Smaller subgraphs of minimum
>   degree k_. Electron. J. Combin. (2017), Paper No. 4.9, 8.
> - [Sa19] Sauermann, Lisa, _A proof of a conjecture of Erdős, Faudree, Rousseau and Schelp on
>   subgraphs of minimum degree k_. J. Combin. Theory Ser. B (2019), 36--75.

*Quoted from [FormalConjectures/ErdosProblems/814.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/814.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/814](https://www.erdosproblems.com/814).

The file states 3 research or textbook statements: 3 solved.

## `Erdos814.erdos_814`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos814.lean#L81](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos814.lean#L81).

> Let $k\geq 2$ and $G$ be a graph with $n\geq k-1$ vertices and
> $$(k-1)(n-k+2)+\binom{k-2}{2}+1$$
> edges. Does there exist some $c_k>0$ such that $G$ must contain an induced subgraph on at most
> $(1-c_k)n$ vertices with minimum degree at least $k$?
>
> The case $k=3$ was a problem of Erdős and Hajnal [Er91]. The question for general $k$ was a
> conjecture of Erdős, Faudree, Rousseau, and Schelp [EFRS90], who proved that such a subgraph
> exists with at most $n-c_k\sqrt{n}$ vertices. Mousset, Noever, and Skorić [MNS17] improved
> this to $n-c_k\frac{n}{\log n}$. The full conjecture was proved by Sauermann [Sa19], who proved
> this with $c_k \gg 1/k^3$.

```lean
theorem erdos_814 :
    ∀ k ≥ 2, ∃ c > 0, ∀ n ≥ k - 1, ∀ G : SimpleGraph (Fin n),
      G.edgeFinset.card = (k - 1) * (n + 2 - k) + (k - 2).choose 2 + 1 →
        ∃ S : Finset (Fin n), S.Nonempty ∧ (S.card : ℝ) ≤ (1 - c) * n ∧
          k ≤ (G.induce (S : Set (Fin n))).minDegree
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/814.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/814.lean#L60).

## `Erdos814.erdos_814.variants.at_least`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos814.lean#L59](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos814.lean#L59).

> The conclusion holds as soon as $G$ has at least $(k-1)(n-k+2)+inom{k-2}{2}+1$ edges
> (Sauermann [Sa19]).

```lean
theorem erdos_814.variants.at_least :
    ∀ k ≥ 2, ∃ c > 0, ∀ n ≥ k - 1, ∀ G : SimpleGraph (Fin n),
      (k - 1) * (n + 2 - k) + (k - 2).choose 2 + 1 ≤ G.edgeFinset.card →
        ∃ S : Finset (Fin n), S.Nonempty ∧ (S.card : ℝ) ≤ (1 - c) * n ∧
          k ≤ (G.induce (S : Set (Fin n))).minDegree
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/814.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/814.lean#L73).

## `Erdos814.erdos_814.variants.sauermann`

Solved: stated here without proof.

> Sauermann [Sa19] proved this with $c_k \gg 1/k^3$.

```lean
theorem erdos_814.variants.sauermann :
    ∃ C > 0, ∀ k ≥ 2, ∀ n ≥ k - 1, ∀ G : SimpleGraph (Fin n),
      (k - 1) * (n + 2 - k) + (k - 2).choose 2 + 1 ≤ G.edgeFinset.card →
        ∃ S : Finset (Fin n), S.Nonempty ∧ (S.card : ℝ) ≤ (1 - C / k ^ 3) * n ∧
          k ≤ (G.induce (S : Set (Fin n))).minDegree
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/814.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/814.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/814.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/814.lean)
- [erdosproblems.com/814](https://www.erdosproblems.com/814)
