---
declaration: theorem
origin: cited
lean: Erdos71.erdos_71
statement: formalized
---

# Erdős Problem 71

> *References:*
> - [erdosproblems.com/71](https://www.erdosproblems.com/71)
> - [Bo77] Bollobás, Béla, *Cycles modulo $k$*. Bull. London Math. Soc. (1977), 97-98.
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*.
>   (1982), 59--79.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*.
>   Discrete Math. (1997), 227-231.

*Quoted from [FormalConjectures/ErdosProblems/71.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/71.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/71](https://www.erdosproblems.com/71).

The file states 1 research or textbook statement: 1 solved.

## `Erdos71.erdos_71`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/71/Erdos71.lean](https://github.com/Jayyhk/erdos-lean/blob/110d489ed5c07e5b216453e092e9113127c98c9a/problems/71/Erdos71.lean).

> Is it true that for every infinite arithmetic progression $P$ which contains even numbers
> there is some constant $c=c(P)$ such that every graph with average degree at least $c$
> contains a cycle whose length is in $P$?
>
> In [Er82e] Erdős credits this conjecture to himself and Burr. This has been proved by
> Bollobás [Bo77]. The best dependence of the constant $c(P)$ is unknown.
>
> The infinite arithmetic progression is encoded as a set $P \subseteq \mathbb{N}$ satisfying
> `P.IsAPOfLength ⊤` (which forces a positive common difference), and "contains even numbers"
> as the existence of an even element. The average degree of a finite simple graph is
> `SimpleGraph.averageDegree`, i.e. $(\sum_v \deg v)/|V| \in \mathbb{Q}$, and a cycle whose
> length is in $P$ is a cycle walk `w` with `w.length ∈ P`.

```lean
theorem erdos_71 :
    ∀ P : Set ℕ, P.IsAPOfLength ⊤ → (∃ n ∈ P, Even n) →
      ∃ c : ℚ, ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
        [DecidableRel G.Adj], c ≤ G.averageDegree →
          ∃ (v : V) (w : G.Walk v v), w.IsCycle ∧ w.length ∈ P
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/71.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/71.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/71.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/71.lean)
- [erdosproblems.com/71](https://www.erdosproblems.com/71)
