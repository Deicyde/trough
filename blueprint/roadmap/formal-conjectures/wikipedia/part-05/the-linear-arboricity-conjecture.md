---
declaration: theorem
origin: cited
lean: LinearArboricityConjecture.linear_arboricity_conjecture, LinearArboricityConjecture.linear_arboricity_conjecture.variants.regular, LinearArboricityConjecture.linear_arboricity_conjecture.variants.cubic, LinearArboricityConjecture.linear_arboricity_conjecture.variants.alon
statement: formalized
---

# The linear arboricity conjecture

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Linear_arboricity)
> * [AEH81] Akiyama, J., Exoo, G., and Harary, F. (1981). "Covering and packing in graphs. IV.
>   Linear arboricity." *Networks* 11, pp. 69--72.
> * [EP84] Enomoto, H. and Péroche, B. (1984). "The linear arboricity of some regular graphs."
>   *J. Graph Theory* 8, pp. 309--324.
> * [Al88] Alon, N. (1988). "The linear arboricity of graphs." *Israel J. Math.* 62,
>   pp. 311--325.

*Quoted from [FormalConjectures/Wikipedia/LinearArboricityConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LinearArboricityConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `LinearArboricityConjecture.linear_arboricity_conjecture`

Open: stated without proof.

> **The linear arboricity conjecture** (Akiyama–Exoo–Harary [AEH81]).
>
> The edges of every graph of maximum degree `Δ` can be partitioned into at most `⌈(Δ + 1) / 2⌉`
> linear forests.

```lean
theorem linear_arboricity_conjecture {V : Type} [Fintype V] (G : SimpleGraph V)
    [DecidableRel G.Adj] :
    linearArboricity G ≤ (G.maxDegree + 2) / 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LinearArboricityConjecture.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LinearArboricityConjecture.lean#L77).

## `LinearArboricityConjecture.linear_arboricity_conjecture.variants.regular`

Open: stated without proof.

> **The linear arboricity conjecture for regular graphs.**
>
> Every nonempty `Δ`-regular graph with `0 < Δ` has linear arboricity exactly
> `⌈(Δ + 1) / 2⌉`. Since a nonempty `Δ`-regular
> graph is easily seen to have linear arboricity strictly greater than `Δ / 2`, this form of
> the conjecture is equivalent to the general upper bound; see [AEH81].

```lean
theorem linear_arboricity_conjecture.variants.regular {V : Type} [Fintype V] [Nonempty V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (Δ : ℕ) (hΔ : 0 < Δ)
    (hreg : ∀ v, G.degree v = Δ) :
    linearArboricity G = (Δ + 2) / 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LinearArboricityConjecture.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LinearArboricityConjecture.lean#L91).

## `LinearArboricityConjecture.linear_arboricity_conjecture.variants.cubic`

Solved: stated here without proof.

> **Cubic graphs have linear arboricity two** (Akiyama–Exoo–Harary [AEH81]).
>
> The edges of every nonempty `3`-regular graph can be partitioned into two linear forests, and one
> linear forest is not enough.

```lean
theorem linear_arboricity_conjecture.variants.cubic {V : Type} [Fintype V] [Nonempty V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hreg : ∀ v, G.degree v = 3) :
    linearArboricity G = 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LinearArboricityConjecture.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LinearArboricityConjecture.lean#L104).

## `LinearArboricityConjecture.linear_arboricity_conjecture.variants.alon`

Solved: stated here without proof.

> **Alon (1988): the linear arboricity conjecture holds asymptotically.**
>
> For every `ε > 0` there is a `Δ₀` such that every graph of maximum degree `Δ ≥ Δ₀` has linear
> arboricity at most `(1 / 2 + ε) Δ`.
>
> *Reference:* [Al88].

```lean
theorem linear_arboricity_conjecture.variants.alon (ε : ℝ) (hε : 0 < ε) :
    ∃ Δ₀ : ℕ, ∀ Δ : ℕ, Δ₀ ≤ Δ → ∀ (V : Type) [Fintype V] (G : SimpleGraph V),
      ∀ [DecidableRel G.Adj], G.maxDegree ≤ Δ →
        (linearArboricity G : ℝ) ≤ (1 / 2 + ε) * Δ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LinearArboricityConjecture.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LinearArboricityConjecture.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LinearArboricityConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LinearArboricityConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Linear_arboricity)
