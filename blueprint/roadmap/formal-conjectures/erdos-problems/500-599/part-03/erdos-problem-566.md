---
declaration: theorem
origin: cited
lean: Erdos566.erdos_566
statement: formalized
---

# Erdős Problem 566

> *References*:
> - [erdosproblems.com/566](https://www.erdosproblems.com/566)
> - [EFRS93] Erdős, Faudree, Rousseau and Schelp, _Ramsey size linear graphs_.
> Combin. Probab. Comput. (1993), 389-399.

*Quoted from [FormalConjectures/ErdosProblems/566.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/566.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/566](https://www.erdosproblems.com/566).

The file states 1 research or textbook statement: 1 open.

## `Erdos566.erdos_566`

Open: stated without proof.

> Let $G$ be such that any subgraph on $k$ vertices has at most $2k-3$ edges.
> Is it true that, if $H$ has $m$ edges and no isolated vertices, then $R(G,H) \ll m$?
>
> In other words: if $G$ is sparse (every induced subgraph on $k$ vertices has $≤ 2k-3$ edges),
> is $G$ Ramsey size linear?

```lean
theorem erdos_566 :
    ∀ (p : ℕ) (G : SimpleGraph (Fin p)),
      (∀ S : Finset (Fin p), 2 ≤ S.card → (G.induce S).edgeSet.ncard ≤ 2 * S.card - 3) →
      G.IsRamseySizeLinear
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/566.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/566.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/566.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/566.lean)
- [erdosproblems.com/566](https://www.erdosproblems.com/566)
