---
declaration: theorem
origin: cited
lean: SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge, SimpleGraph.nonempty_stNumbering_of_isVertexConnected_two_sup_edge, SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two
statement: formalized
proof: formalized
---

# Lempel–Even–Cederbaum theorem

On a finite vertex type with at least three vertices, a
simple graph `G` admits an `st`-numbering for distinct vertices `s ≠ t` if and only if
`G ⊔ SimpleGraph.edge s t` is `2`-vertex-connected.

```lean
SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge.{u} {V : Type u} [Fintype V]
  {G : SimpleGraph V} (h3 : 3 ≤ Fintype.card V) {s t : V} (hst : s ≠ t) :
  Nonempty (G.STNumbering s t) ↔ (G ⊔ SimpleGraph.edge s t).IsVertexConnected 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Menger's theorem for internally vertex-disjoint paths](mengers-theorem-for-internally-vertex-disjoint-p.md)

## Lean

Formalized in Tau Ceti as [`SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/STNumbering.html#SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge).

## Other forms

**Lempel–Even–Cederbaum theorem (existence).** Formalized in Tau Ceti as [`SimpleGraph.nonempty_stNumbering_of_isVertexConnected_two_sup_edge`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/STNumbering.html#SimpleGraph.nonempty_stNumbering_of_isVertexConnected_two_sup_edge).

```lean
SimpleGraph.nonempty_stNumbering_of_isVertexConnected_two_sup_edge.{u} {V : Type u} [Fintype V]
  {G : SimpleGraph V} {s t : V} (hst : s ≠ t)
  (hG : (G ⊔ SimpleGraph.edge s t).IsVertexConnected 2) : Nonempty (G.STNumbering s t)
```

**Lempel–Even–Cederbaum theorem for adjacent endpoints.** Formalized in Tau Ceti as [`SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/STNumbering.html#SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two).

```lean
SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two.{u} {V : Type u} [Fintype V]
  {G : SimpleGraph V} (h3 : 3 ≤ Fintype.card V) {s t : V} (hst : G.Adj s t) :
  Nonempty (G.STNumbering s t) ↔ G.IsVertexConnected 2
```

## Sources

- [Tau Ceti documentation: `SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge`](https://taucetiproject.org/docs/TauCeti/Combinatorics/SimpleGraph/Connectivity/STNumbering.html#SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge)
- [Source of `SimpleGraph.nonempty_stNumbering_iff_isVertexConnected_two_sup_edge` in TauCeti/Combinatorics/SimpleGraph/Connectivity/STNumbering.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/SimpleGraph/Connectivity/STNumbering.lean#L977)
