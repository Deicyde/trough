---
declaration: theorem
origin: cited
lean: Kourovka.«20.76».kourovka_20_76
statement: formalized
---

# Conjecture 20.76

> by L. Pyber
> *Reference:* [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
> *Solution:* K. Muliarchyk, [Abelian subgroups of finite 2-groups: counterexamples to
> Problems 20.75 and 20.76](https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka_20_75-20_76_solution.pdf), Proposition 6.1.
> !

*Quoted from [FormalConjectures/Kourovka/20_76.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/20_76.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Kourovka.«20.76».kourovka_20_76`

Solved: stated here without proof.

> Let $G$ be a finite $p$-group and assume that all abelian normal subgroups of $G$
> have order at most $p^k$. Is it true that every abelian subgroup of $G$ has order at most
> $p^{2k}$?
>
> The answer is no. Muliarchyk's Proposition 6.1 gives a finite $2$-group of order
> $2^{145}$ whose abelian normal subgroups have order at most $2^{42}$, but which
> contains an elementary abelian subgroup of order $2^{85} > 2^{84}$.

```lean
theorem kourovka_20_76 :
    ¬ (∀ᵉ (p : ℕ) (hp : p.Prime) (G : Type) (_ : Group G) (hg : IsPGroup p G) (_ : Finite G) (k : ℕ)
    (h : ∀ H: Subgroup G, H.Normal ∧ IsMulCommutative H → Nat.card H ≤ p ^ k),
    (∀ H : Subgroup G, IsMulCommutative H → Nat.card H ≤ p ^ (2 * k)))
```

Category `research solved`; AMS [20 Group theory and generalizations](../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Kourovka/20_76.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/20_76.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Kourovka/20_76.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Kourovka/20_76.lean)
- [The Kourovka Notebook](https://arxiv.org/abs/1401.0300v40)
