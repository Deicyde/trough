---
declaration: theorem
origin: cited
lean: PetersenColoringConjecture.petersen_coloring_conjecture, PetersenColoringConjecture.petersen_coloring_conjecture.variants.normal_five_edge_coloring
statement: formalized
---

# The Petersen colouring conjecture (Jaeger 1988)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Petersen_graph#Petersen_coloring_conjecture)
> * [Ja88] Jaeger, F. (1988). "Nowhere-zero flow problems." In *Selected Topics in Graph
>   Theory 3*, Academic Press, pp. 71--95.
> * [Mk13] Mkrtchyan, V. V. (2013). "A remark on the Petersen coloring conjecture of Jaeger."
>   *Australas. J. Combin.* 56, pp. 145--151.
> * [HS14] Hägglund, J. and Steffen, E. (2014). "Petersen-colorings and some families of
>   snarks." *Ars Math. Contemp.* 7, pp. 161--173.
> * [Zh97] Zhang, C.-Q. (1997). *Integer flows and cycle covers of graphs.* Marcel Dekker.

*Quoted from [FormalConjectures/Wikipedia/PetersenColoringConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PetersenColoringConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `PetersenColoringConjecture.petersen_coloring_conjecture`

Open: stated without proof.

> **The Petersen colouring conjecture (Jaeger 1988).**
>
> Every bridgeless cubic graph has a Petersen colouring: an edge colouring by the edges of the
> Petersen graph such that the three edges at each vertex are mapped onto the three edges at
> some vertex of the Petersen graph. Jaeger showed that this conjecture implies both the
> Berge–Fulkerson conjecture and the cycle double cover conjecture.

```lean
theorem petersen_coloring_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      (∀ v, G.degree v = 3) → G.IsBridgeless →
      ∃ φ : Sym2 V → Sym2 PetersenVertex, IsPetersenColoring G φ
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/PetersenColoringConjecture.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PetersenColoringConjecture.lean#L63).

## `PetersenColoringConjecture.petersen_coloring_conjecture.variants.normal_five_edge_coloring`

Solved: stated here without proof.

> **Jaeger's reformulation: normal `5`-edge-colourings.**
>
> A proper `5`-edge-colouring of a cubic graph is *normal* if every edge, together with its four
> neighbouring edges, sees either exactly `3` or exactly `5` colours. Jaeger showed that a cubic
> graph has a Petersen colouring iff it has a normal `5`-edge-colouring.
>
> *Reference:* [Ja88].

```lean
theorem petersen_coloring_conjecture.variants.normal_five_edge_coloring
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hcubic : ∀ v, G.degree v = 3) :
    (∃ φ : Sym2 V → Sym2 PetersenVertex, IsPetersenColoring G φ) ↔
    ∃ c : Sym2 V → Fin 5,
      (∀ e ∈ G.edgeFinset, ∀ f ∈ G.edgeFinset, e ≠ f → (∃ v, v ∈ e ∧ v ∈ f) → c e ≠ c f) ∧
      ∀ e ∈ G.edgeFinset,
        ((G.edgeFinset.filter fun f => ∃ v, v ∈ e ∧ v ∈ f).image c).card = 3 ∨
        ((G.edgeFinset.filter fun f => ∃ v, v ∈ e ∧ v ∈ f).image c).card = 5
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/PetersenColoringConjecture.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PetersenColoringConjecture.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PetersenColoringConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PetersenColoringConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Petersen_graph#Petersen_coloring_conjecture)
