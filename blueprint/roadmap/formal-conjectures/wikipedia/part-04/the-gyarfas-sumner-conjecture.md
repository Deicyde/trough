---
declaration: theorem
origin: cited
lean: GyarfasSumnerConjecture.gyarfas_sumner_conjecture, GyarfasSumnerConjecture.gyarfas_sumner_conjecture.variants.path, GyarfasSumnerConjecture.gyarfas_sumner_conjecture.variants.radius_two
statement: formalized
---

# The Gyárfás–Sumner conjecture

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Gy%C3%A1rf%C3%A1s%E2%80%93Sumner_conjecture)
> * [Gy75] Gyárfás, A. (1975). "On Ramsey covering-numbers." *Infinite and finite sets*,
>   Colloq. Math. Soc. János Bolyai 10, pp. 801--816.
> * [Su81] Sumner, D. P. (1981). "Subtrees of a graph and the chromatic number." *The theory
>   and applications of graphs (Kalamazoo, 1980)*, Wiley, pp. 557--576.
> * [Gy87] Gyárfás, A. (1987). "Problems from the world surrounding perfect graphs."
>   *Zastos. Mat.* 19, pp. 413--441.
> * [KP94] Kierstead, H. A. and Penrice, S. G. (1994). "Radius two trees specify χ-bounded
>   classes." *J. Graph Theory* 18, pp. 119--129.
> * [SS20] Scott, A. and Seymour, P. (2020). "A survey of χ-boundedness." *J. Graph Theory* 95,
>   pp. 473--504. [arXiv:1812.07500](https://arxiv.org/abs/1812.07500)

*Quoted from [FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `GyarfasSumnerConjecture.gyarfas_sumner_conjecture`

Open: stated without proof.

> **The Gyárfás–Sumner conjecture (Gyárfás 1975, Sumner 1981).**
>
> For every finite tree $T$ the class of $T$-free graphs (graphs with no induced subgraph
> isomorphic to $T$) is $\chi$-bounded: there is a function $f$ such that every $T$-free graph
> $G$ satisfies $\chi(G) \le f(\omega(G))$.

```lean
theorem gyarfas_sumner_conjecture :
    ∀ {W : Type} [Fintype W] [DecidableEq W] (T : SimpleGraph W) [DecidableRel T.Adj],
      T.IsTree → ∃ f : ℕ → ℕ, IsChiBoundedBy T f
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean#L58).

## `GyarfasSumnerConjecture.gyarfas_sumner_conjecture.variants.path`

Solved: stated here without proof.

> **Paths (Gyárfás 1987).**
>
> For every $n$, the class of $P_n$-free graphs is $\chi$-bounded. For $n \ge 2$ and
> nonempty $G$, Gyárfás's argument gives $\chi(G) \le (n-1)^{\omega(G) - 1}$.
>
> *Reference:* [Gy87].

```lean
theorem gyarfas_sumner_conjecture.variants.path (n : ℕ) :
    ∃ f : ℕ → ℕ, IsChiBoundedBy (pathGraph n) f
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean#L72).

## `GyarfasSumnerConjecture.gyarfas_sumner_conjecture.variants.radius_two`

Solved: stated here without proof.

> **Trees of radius two (Kierstead–Penrice 1994).**
>
> Every tree of radius at most $2$ (i.e. with a vertex within distance $2$ of every other vertex)
> specifies a $\chi$-bounded class.
>
> *Reference:* [KP94].

```lean
theorem gyarfas_sumner_conjecture.variants.radius_two
    {W : Type} [Fintype W] [DecidableEq W] (T : SimpleGraph W) [DecidableRel T.Adj]
    (hT : T.IsTree) (hrad : ∃ c : W, ∀ w : W, T.dist c w ≤ 2) :
    ∃ f : ℕ → ℕ, IsChiBoundedBy T f
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GyarfasSumnerConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Gy%C3%A1rf%C3%A1s%E2%80%93Sumner_conjecture)
