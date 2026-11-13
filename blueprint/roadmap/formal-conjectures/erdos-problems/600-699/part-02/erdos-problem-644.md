---
declaration: theorem
origin: cited
lean: Erdos644.erdos_644.variants.elementary_upper_bound, Erdos644.erdos_644.parts.i, Erdos644.erdos_644.parts.ii
statement: formalized
---

# Erdős Problem 644

> *References:*
> - [erdosproblems.com/644](https://www.erdosproblems.com/644)
> - [EFKT92] Erdős, P. and Fon-Der-Flaass, D. and Kostochka, A. V. and Tuza, Zs., Small transversals in
>   uniform hypergraphs. Siberian Adv. Math. (1992), 82-88.

*Quoted from [FormalConjectures/ErdosProblems/644.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/644.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/644](https://www.erdosproblems.com/644).

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 1 test statement, counted here but not shown.

## `Erdos644.erdos_644.variants.elementary_upper_bound`

Textbook result, proved here.

> For $r \geq 3$, the transversal bound satisfies $f(k,r) \leq 2k$.

```lean
theorem erdos_644.variants.elementary_upper_bound (k r : ℕ) (hr : 3 ≤ r) :
    Hypergraph.subfamilyTransversalBound k r 2 ≤ ((2 * k : ℕ) : ℕ∞)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/644.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/644.lean#L37).

## `Erdos644.erdos_644.parts.i`

Open: stated without proof.

> Let $f(k,r)$ be minimal such that if $A_1,A_2,\ldots$ is a family of sets, all of size $k$, such
> that for every collection of $r$ of the $A_is$ there is some pair $\{x,y\}$ which intersects all of
> the $A_j$, then there is some set of size $f(k,r)$ which intersects all of the sets $A_i$. Is it
> true that
>
> $$f(k,7)=(1+o(1))\frac{3}{4}k?$$

```lean
theorem erdos_644.parts.i :
    (fun k ↦ ((Hypergraph.subfamilyTransversalBound k 7 2).toNat : ℝ)) ~[atTop]
      (fun k ↦ (3 / 4 : ℝ) * k)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/644.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/644.lean#L95).

## `Erdos644.erdos_644.parts.ii`

Open: stated without proof.

> Is it true that for any $r\geq 3$ there exists some constant $c_r$ such that
>
> $$f(k,r)=(1+o(1))c_rk?$$

```lean
theorem erdos_644.parts.ii :
    ∀ r : ℕ, 3 ≤ r → ∃ c : ℝ, 0 < c ∧
    (fun k ↦ ((Hypergraph.subfamilyTransversalBound k r 2).toNat : ℝ)) ~[atTop]
      (fun k ↦ c * k)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/644.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/644.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/644.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/644.lean)
- [erdosproblems.com/644](https://www.erdosproblems.com/644)
