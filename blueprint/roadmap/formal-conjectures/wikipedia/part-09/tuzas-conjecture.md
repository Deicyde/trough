---
declaration: theorem
origin: cited
lean: TuzaConjecture.tuza_conjecture, TuzaConjecture.tuza_conjecture.variants.haxell
statement: formalized
---

# Tuza's conjecture

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Tuza%27s_conjecture)
> * [Tu90] Tuza, Zs. (1990). "A conjecture on triangles of graphs." *Graphs Combin.* 6,
>   pp. 373--380.
> * [Ha99] Haxell, P. E. (1999). "Packing and covering triangles in graphs." *Discrete Math.*
>   195, pp. 251--254.

*Quoted from [FormalConjectures/Wikipedia/TuzaConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TuzaConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `TuzaConjecture.tuza_conjecture`

Open: stated without proof.

> Tuza's conjecture (1981): every finite graph $G$ satisfies $\tau(G) \le 2\nu(G)$,
> where $\tau(G)$ is its triangle covering number and $\nu(G)$ is its triangle packing number.
> The bound would be sharp, for example for $K_4$ and $K_5$.

```lean
theorem tuza_conjecture {V : Type} [Fintype V] (G : SimpleGraph V) :
    triangleCoverNumber G ≤ 2 * trianglePackingNumber G
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/TuzaConjecture.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TuzaConjecture.lean#L78).

## `TuzaConjecture.tuza_conjecture.variants.haxell`

Solved: stated here without proof.

> Haxell (1999): every finite graph satisfies $\tau(G) \le (66/23)\nu(G)$.
>
> *Reference:* [Ha99].

```lean
theorem tuza_conjecture.variants.haxell {V : Type} [Fintype V] (G : SimpleGraph V) :
    (triangleCoverNumber G : ℝ) ≤ 66 / 23 * trianglePackingNumber G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/TuzaConjecture.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TuzaConjecture.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/TuzaConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TuzaConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Tuza%27s_conjecture)
