---
declaration: theorem
origin: cited
lean: Erdos567.erdos_567.parts.i, Erdos567.erdos_567.parts.ii, Erdos567.erdos_567.parts.iii
statement: formalized
---

# Erdős Problem 567

> Let $G$ be either $Q_3$ or $K_{3,3}$ or $H_5$ (the last formed by adding two vertex-disjoint chords
> to $C_5$). Is it true that, if $H$ has $m$ edges and no isolated vertices, then
>
> $$ R(G,H) \ll m? $$
>
> In other words, is $G$ Ramsey size linear? A special case of Problem 566.
>
> *Reference:* [erdosproblems.com/567](https://www.erdosproblems.com/567)
>
> [EFRS93] Erdős, Faudree, Rousseau and Schelp, _Ramsey size linear graphs_.
> Combin. Probab. Comput. (1993), 389-399.

*Quoted from [FormalConjectures/ErdosProblems/567.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/567.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/567](https://www.erdosproblems.com/567).

The file states 3 research or textbook statements: 3 open.

## `Erdos567.erdos_567.parts.i`

Open: stated without proof.

> **Erdős Problem 567 (Q3)**
>
> Is $Q_3$ (the 3-dimensional hypercube) Ramsey size linear?

```lean
theorem erdos_567.parts.i : IsRamseySizeLinear Q3
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/567.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/567.lean#L60).

## `Erdos567.erdos_567.parts.ii`

Open: stated without proof.

> **Erdős Problem 567 (K33)**
>
> Is $K_{3,3}$ Ramsey size linear?

```lean
theorem erdos_567.parts.ii : IsRamseySizeLinear K33
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/567.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/567.lean#L69).

## `Erdos567.erdos_567.parts.iii`

Open: stated without proof.

> **Erdős Problem 567 (H5)**
>
> Is $H_5$ ($C_5$ with two vertex-disjoint chords) Ramsey size linear?

```lean
theorem erdos_567.parts.iii : IsRamseySizeLinear H5
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/567.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/567.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/567.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/567.lean)
- [erdosproblems.com/567](https://www.erdosproblems.com/567)
