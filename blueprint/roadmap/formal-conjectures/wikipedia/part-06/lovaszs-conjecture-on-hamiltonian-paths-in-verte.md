---
declaration: theorem
origin: cited
lean: LovaszConjecture.lovasz_conjecture, LovaszConjecture.lovasz_conjecture.variants.babai, LovaszConjecture.lovasz_conjecture.variants.dense
statement: formalized
---

# Lovász's conjecture on Hamiltonian paths in vertex-transitive graphs (1970)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Lov%C3%A1sz_conjecture)
> * [Lo70] Lovász, L. (1970). Problem 11, in *Combinatorial Structures and their Applications*
>   (Proc. Calgary Internat. Conf. 1969), Gordon and Breach, p. 497.
> * [Ba79] Babai, L. (1979). "Long cycles in vertex-transitive graphs." *J. Graph Theory* 3,
>   pp. 301--304.
> * [CHM14] Christofides, D., Hladký, J. and Máthé, A. (2014). "Hamilton cycles in dense
>   vertex-transitive graphs." *J. Combin. Theory Ser. B* 109, pp. 34--72.
>   [arXiv:1008.2193](https://arxiv.org/abs/1008.2193)
> * [KM09] Kutnar, K. and Marušič, D. (2009). "Hamilton cycles and paths in vertex-transitive
>   graphs — current directions." *Discrete Math.* 309, pp. 5491--5500.

*Quoted from [FormalConjectures/Wikipedia/LovaszConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `LovaszConjecture.lovasz_conjecture`

Open: stated without proof.

> **Lovász's conjecture (1970).**
>
> Every finite connected vertex-transitive graph has a Hamiltonian path.

```lean
theorem lovasz_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      G.Connected → IsVertexTransitive G → HasHamiltonianPath G
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszConjecture.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszConjecture.lean#L60).

## `LovaszConjecture.lovasz_conjecture.variants.babai`

Solved: stated here without proof.

> **Babai (1979): long cycles in vertex-transitive graphs.**
>
> Every finite connected vertex-transitive graph on $n \ge 3$ vertices contains a cycle of length
> at least $\sqrt{3n}$.
>
> *Reference:* [Ba79].

```lean
theorem lovasz_conjecture.variants.babai
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hconn : G.Connected) (htrans : IsVertexTransitive G) (hcard : 3 ≤ Fintype.card V) :
    ∃ (v : V) (c : G.Walk v v), c.IsCycle ∧
      Real.sqrt (3 * Fintype.card V) ≤ (c.length : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszConjecture.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszConjecture.lean#L74).

## `LovaszConjecture.lovasz_conjecture.variants.dense`

Solved: stated here without proof.

> **Christofides–Hladký–Máthé (2014): Hamiltonian-path corollary of the dense case.**
>
> For every $\varepsilon > 0$ there is $n_0$ such that every connected vertex-transitive graph on
> $n \ge n_0$ vertices with minimum degree at least $\varepsilon n$ has a Hamiltonian path.
> This is a corollary of the Hamiltonian-cycle result in [CHM14, Theorem 2].
>
> *Reference:* [CHM14].

```lean
theorem lovasz_conjecture.variants.dense :
    ∀ ε : ℝ, 0 < ε → ∃ n₀ : ℕ, ∀ {V : Type} [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj], n₀ ≤ Fintype.card V →
      G.Connected → IsVertexTransitive G → ε * Fintype.card V ≤ G.minDegree →
      HasHamiltonianPath G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/LovaszConjecture.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszConjecture.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LovaszConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/LovaszConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Lov%C3%A1sz_conjecture)
