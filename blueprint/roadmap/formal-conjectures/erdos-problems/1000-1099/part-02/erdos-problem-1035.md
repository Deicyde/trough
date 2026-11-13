---
declaration: theorem
origin: cited
lean: Erdos1035.erdos_1035
statement: formalized
---

# Erdős Problem 1035

> *References:*
> - [erdosproblems.com/1035](https://www.erdosproblems.com/1035)
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.

*Quoted from [FormalConjectures/ErdosProblems/1035.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1035.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1035](https://www.erdosproblems.com/1035).

The file states 1 research or textbook statement: 1 open.

## `Erdos1035.erdos_1035`

Open: stated without proof.

> Is there a constant $c > 0$ such that every graph on $2^n$ vertices with minimum degree
> $> (1-c) \cdot 2^n$ contains the $n$-dimensional hypercube $Q_n$?
>
> This is Erdős's question [Er93, p. 345].
>
> See also [576] for the extremal number of edges that guarantee a $Q_n$.

```lean
theorem erdos_1035 :
    ∃ c > 0, ∀ n : ℕ, ∀ (G : SimpleGraph (Fin (2 ^ n))) [DecidableRel G.Adj],
      (∀ v, (G.degree v : ℝ) > (1 - c) * 2 ^ n) →
        (SimpleGraph.hypercube n).IsContained G
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1035.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1035.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1035.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1035.lean)
- [erdosproblems.com/1035](https://www.erdosproblems.com/1035)
