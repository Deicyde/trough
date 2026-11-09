---
declaration: theorem
origin: cited
lean: Erdos750.erdos_750.variants.stiebitz, Erdos750.erdos_750, Erdos750.erdos_750.variants.epsilon, Erdos750.erdos_750.variants.c_gt_quarter
statement: formalized
---

# Erdős Problem 750

> *References:*
> - [erdosproblems.com/750](https://www.erdosproblems.com/750)
> - [EHS82] Erdős, P. and Hajnal, A. and Szemerédi, E., On almost bipartite large chromatic graphs.
>   Theory and practice of combinatorics (1982), 117-123.
> - [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in Graph
>   Theory (1969), 27-35.
> - [Er94b] Erdős, Paul, _Some problems in number theory, combinatorics and combinatorial geometry_.
>   Math. Pannon. (1994), 261-269.
> - [Er95d] Erdős, Paul, On some problems in combinatorial set theory. Publ. Inst. Math. (Beograd)
>   (N.S.) (1995), 61-65.
> - [ErHa67b] Erdős, P. and Hajnal, András, On chromatic graphs. Mat. Lapok (1967), 1--4.
> - [UlamErdos750](https://www.ulam.ai/research/erdos750.pdf)
> - [St85] Stiebitz, M., _Beiträge zur Theorie der färbungskritischen Graphen_. Habilitation,
>   TH Ilmenau (1985).
> - [SaSt89] Sachs, H. and Stiebitz, M., _On constructive methods in the theory of colour-critical
>   graphs_. Discrete Math. (1989), 287-296.
> - [MuSt19] Müller, T. and Stehlík, M., _Generalised Mycielski graphs and the Borsuk-Ulam theorem_.
>   Electron. J. Combin. (2019), P4.8.

*Quoted from [FormalConjectures/ErdosProblems/750.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/750.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/750](https://www.erdosproblems.com/750).

The file states 4 research or textbook statements: 4 solved. It also has 2 test statements, counted here but not shown.

## `Erdos750.erdos_750.variants.stiebitz`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos750/Stiebitz.lean#L41](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos750/Stiebitz.lean#L41).

> **Stiebitz's theorem** [St85]: every graph in $M_r$ has chromatic number at least $r$. The
> matching upper bound follows from the construction, so the chromatic number is exactly $r$.
>
> See also [SaSt89] and [MuSt19].
>
> The linked formal proof (Alexeev and Codex, via signed-biclique chains and a `ℤ_p`-Tucker
> lemma) uses the same `IsRecursivelyBuiltMr`, except that its `genMyc s G` has `MycAdj s G`
> directly as adjacency relation instead of `SimpleGraph.fromRel (MycAdj s G)`; the two graphs are
> equal since `MycAdj` is symmetric and irreflexive.

```lean
theorem erdos_750.variants.stiebitz {V : Type u} (G : SimpleGraph V) (r : ℕ)
    (h : IsRecursivelyBuiltMr r G) : (r : ℕ∞) ≤ G.chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/750.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/750.lean#L122).

## `Erdos750.erdos_750`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/main/problems/750/Erdos750.lean](https://github.com/Jayyhk/erdos-lean/blob/main/problems/750/Erdos750.lean); a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos750.lean#L50](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos750.lean#L50).

> Let $f(m)$ be some function such that $f(m)\to \infty$ as $m\to \infty$. Does there exist a
> graph $G$ of infinite chromatic number such that every subgraph on $m$ vertices contains
> an independent set of size at least $\frac{m}{2}-f(m)$?
>
> Note that in [Er94b] the function $f$ generalises a (proven) result for $f(m) = \epsilon m$,
> where $\epsilon > 0$. Hence we should assume it is non-negative valued.
>
> The existence of such a graph was proved [UlamErdos750] by GPT 5.5 Pro (prompted by Chojecki).
> Indeed, this constructs a graph with infinite chromatic number such that every subgraph on $m$
> vertices can be made bipartite after deleting at most $f(m)$ many vertices.
>
> The proof in plby/lean-proofs uses the proof of `erdos_750.variants.stiebitz` linked above.
> It produces a graph on a `V : Type`, which gives the statement below in any universe by
> lifting `V`.

```lean
theorem erdos_750 :
    ∀ (f : ℕ → ℝ≥0) (hf : atTop.Tendsto f atTop),
      ∃ (V : Type*) (G : SimpleGraph V), G.chromaticNumber = ⊤ ∧
        ∀ (m : ℕ) (S : Set V), 0 < m → S.ncard = m →
          ∃ I ⊆ S, G.IsIndepSet I ∧ m / 2 - f m ≤ I.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/750.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/750.lean#L148).

## `Erdos750.erdos_750.variants.epsilon`

Solved: stated here without proof.

> In [Er69b] Erdős conjectures this for $f(m)=\epsilon m$ for any fixed $\epsilon>0$. This follows
> from a result of Erdős, Hajnal, and Szemerédi [EHS82], as described by Sellke in the comments.

```lean
theorem erdos_750.variants.epsilon :
    ∀ (ε : ℝ≥0), ε > 0 →
      ∃ (V : Type*) (G : SimpleGraph V), G.chromaticNumber = ⊤ ∧
        ∀ (m : ℕ) (S : Set V), 0 < m → S.ncard = m →
          ∃ I ⊆ S, G.IsIndepSet I ∧ m / 2 - ε * m ≤ I.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/750.lean, line 160](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/750.lean#L160).

## `Erdos750.erdos_750.variants.c_gt_quarter`

Solved: stated here without proof.

> In [ErHa67b] Erdős and Hajnal prove this for $f(m)\geq cm$ for all $c>1/4$.

```lean
theorem erdos_750.variants.c_gt_quarter :
    ∀ (c : ℝ≥0), c > 1 / 4 →
      ∃ (V : Type*) (G : SimpleGraph V), G.chromaticNumber = ⊤ ∧
        ∀ (m : ℕ) (S : Set V), 0 < m → S.ncard = m →
          ∃ I ⊆ S, G.IsIndepSet I ∧ m / 2 - c * m ≤ I.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/750.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/750.lean#L171).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/750.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/750.lean)
- [erdosproblems.com/750](https://www.erdosproblems.com/750)
