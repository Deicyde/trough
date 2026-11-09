---
declaration: theorem
origin: cited
lean: Erdos562.erdos_562
statement: formalized
---

# Erdős Problem 562

> *Reference:* [erdosproblems.com/562](https://www.erdosproblems.com/562)

*Quoted from [FormalConjectures/ErdosProblems/562.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/562.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/562](https://www.erdosproblems.com/562).

The file states 1 research or textbook statement: 1 open.

## `Erdos562.erdos_562`

Open: stated without proof.

> Let $R_r(n)$ denote the $r$-uniform hypergraph Ramsey number: the minimal $m$ such that if we
> $2$-colour all edges of the complete $r$-uniform hypergraph on $m$ vertices then there must be some
> monochromatic copy of the complete $r$-uniform hypergraph on $n$ vertices.
>
> Prove that, for $r \ge 3$,
>
> $$ \log_{r-1} R_r(n) \asymp_r n, $$
>
> where $\log_{r-1}$ denotes the $(r-1)$-fold iterated logarithm.

```lean
theorem erdos_562 :
    ∀ r ≥ 3, (fun n ↦ log^[r - 1] (hypergraphRamsey r n)) =Θ[atTop] (fun n ↦ (n : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/562.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/562.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/562.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/562.lean)
- [erdosproblems.com/562](https://www.erdosproblems.com/562)
