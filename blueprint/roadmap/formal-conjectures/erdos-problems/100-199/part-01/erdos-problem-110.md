---
declaration: theorem
origin: cited
lean: Erdos110.erdos_110, Erdos110.erdos_110.variants.lambie_hanson, Erdos110.erdos_110.variants.de_bruijn_erdos
statement: formalized
---

# Erdős Problem 110

> *References:*
> - [erdosproblems.com/110](https://www.erdosproblems.com/110)
> - [EHS82] Erdős, P. and Hajnal, A. and Szemerédi, E., *On almost bipartite large chromatic graphs*.
>   Theory and practice of combinatorics (1982), 117-123.
>   [PDF](https://www.renyi.hu/~p_erdos/1982-11.pdf)
> - [Er87] Erdős, P., *Some problems on finite and infinite graphs*. Logic and combinatorics
>   (Arcata, Calif., 1985) (1987), 223-228. [PDF](https://www.renyi.hu/~p_erdos/1987-28.pdf)
> - [Er95d] Erdős, Paul, *On some problems in combinatorial set theory*. Publ. Inst. Math.
>   (Beograd) (N.S.) (1995), 61-65.
> - [KoSh05] Komjáth, Péter and Shelah, Saharon, *Finite subgraphs of uncountably chromatic graphs*.
>   J. Graph Theory (2005), 28--38.
> - [La20] Lambie-Hanson, Chris, *On the growth rate of chromatic numbers of finite subgraphs*.
>   Adv. Math. (2020), 107176, 13. [arXiv:1902.08177](https://arxiv.org/abs/1902.08177)
> - [dBEr51] de Bruijn, N. G. and Erdős, P., *A colour problem for infinite graphs and a problem in
>   the theory of relations*. Indag. Math. (1951), 369--373.

*Quoted from [FormalConjectures/ErdosProblems/110.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/110.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/110](https://www.erdosproblems.com/110).

The file states 3 research or textbook statements: 3 solved.

## `Erdos110.erdos_110`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos110.lean#L161](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos110.lean#L161).

> Is there some $F(n)$ such that every graph with chromatic number $\aleph_1$ has, for all large
> $n$, a subgraph with chromatic number $n$ on at most $F(n)$ vertices?
>
> A question of Erdős, Hajnal, and Szemerédi (see [EHS82], [Er87, p. 225, Problem 6], [Er95d]).
> The answer is no: Komjáth and Shelah [KoSh05] proved that it is consistent that the answer is no,
> and Lambie-Hanson [La20, Theorem A] constructed a counterexample in ZFC. The statement below is
> therefore the negation. Subgraphs need not be induced, and finiteness of `H.verts` is explicit
> because `Set.ncard` is `0` on infinite sets. Graphs are taken in `Type 1`, the universe of the
> vertex type in the linked proof's construction. A counterexample in `Type` would give one in
> `Type 1` by `ULift`; conversely, Lambie-Hanson's graph has $2^{\aleph_1}$ vertices, so it also
> exists in `Type`.

```lean
theorem erdos_110 :
    ¬ ∃ F : ℕ → ℕ, ∀ (V : Type 1) (G : SimpleGraph V), Erdos737.ChromaticNumberAlephOne G →
      ∀ᶠ n : ℕ in atTop, ∃ H : G.Subgraph,
        H.verts.Finite ∧ H.verts.ncard ≤ F n ∧ H.coe.chromaticNumber = (n : ℕ∞)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/110.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/110.lean#L63).

## `Erdos110.erdos_110.variants.lambie_hanson`

Solved: stated here without proof.

> Lambie-Hanson's quantitative theorem [La20, Theorem A], of which `erdos_110` is a consequence:
> for every $f : \mathbb{N} \to \mathbb{N}$ there is a graph with chromatic number $\aleph_1$ such
> that, for every $k \geq 3$, every finite subgraph with fewer than $f(k)$ vertices has chromatic
> number less than $k$. (The graph constructed in [La20] has $2^{\aleph_1}$ vertices.)

```lean
theorem erdos_110.variants.lambie_hanson (f : ℕ → ℕ) :
    ∃ (V : Type 1) (G : SimpleGraph V), Erdos737.ChromaticNumberAlephOne G ∧
      ∀ k : ℕ, 3 ≤ k → ∀ H : G.Subgraph, H.verts.Finite → H.verts.ncard < f k →
        H.coe.chromaticNumber < (k : ℕ∞)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/110.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/110.lean#L76).

## `Erdos110.erdos_110.variants.de_bruijn_erdos`

Solved: stated here without proof.

> A theorem of de Bruijn and Erdős [dBEr51] implies that, if $G$ has infinite chromatic number,
> then $G$ has a finite subgraph of chromatic number $n$ for every $n\geq 1$.
>
> Infinite chromatic number is `G.chromaticNumber = ⊤`.

```lean
theorem erdos_110.variants.de_bruijn_erdos {V : Type*} (G : SimpleGraph V)
    (hG : G.chromaticNumber = ⊤) (n : ℕ) (hn : 1 ≤ n) :
    ∃ H : G.Subgraph, H.verts.Finite ∧ H.coe.chromaticNumber = (n : ℕ∞)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/110.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/110.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/110.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/110.lean)
- [erdosproblems.com/110](https://www.erdosproblems.com/110)
