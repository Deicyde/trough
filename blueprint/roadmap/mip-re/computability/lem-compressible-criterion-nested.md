---
declaration: lemma
origin: cited
lean: MIPRE.Cost.compressibility_criterion_nested
statement: formalized
proof: formalized
---

# Compressibility criterion, nested classes

Let $A$ and $B_0 \subseteq B_1$ be families of languages indexed by the level $n$, with distinguished elements $y_{\mathrm{yes}} \in A(n)$ and $y_{\mathrm{no}} \in B_0(n)$ at every level $n \geq n_0$, and suppose that the complement of $B_1$ is recursively enumerable uniformly in the level: there is a program $S$ that halts on $(x, n)$ if and only if $x \notin B_1(n)$. Suppose there is a polynomial-time computable $\textsc{Compr}$ such that whenever $c$ is a succinct description with parameter $n \geq n_0$ of a string $x$ with $\left\vert {x} \right\vert \leq n + 1$ and $2\left\vert {c} \right\vert \leq n$, and $y = \textsc{Compr}(c, n)$:

1. if $x \in A(2n+1)$ then $y \in A(n)$, and
2. if $x \in B_0(2n+1)$ then $y \in B_0(n)$.

Then there are a polynomial-time computable $g$ and a constant $K$ such that, with $r(e) = 2^{K + 1 + \left\vert {e} \right\vert} \geq n_0$, for every machine $e$: if $\phi_e$ halts on the empty input then $g(e) \in A(r(e))$, and otherwise $g(e) \in B_1(r(e))$.

## Depends on

- [Succinct description](../foundations/part-02/def-succinct.md)
- [Efficient universal Turing machine](lem-universal-tm.md)
- [Efficient s-m-n](lem-smn.md)
- [Efficient Kleene recursion theorem](lem-kleene.md)

## Proof

The proof of Lemma [Compressibility criterion](lem-compressible-criterion.md) unchanged, with the two roles of $B$ separated. The search branch of the self-referential decider runs $S$ on the string at the start level, so it fires only if that string is outside $B_1$, and eventually fires if it is. The downward induction that puts every level of the recursion in the class of $y_{\mathrm{no}}$ runs inside $B_0$, from $y_{\mathrm{no}} \in B_0$ by item 2. In the halting case the search cannot fire before $e$ halts, since firing at a level would put the start string in $B_0 \subseteq B_1$, against its firing at all; so preservation of $A$ applies from the level where $e$ halts. In the non-halting case, if the start string were outside $B_1$ the search would fire, and the induction would put it in $B_0 \subseteq B_1$. Lemma [Compressibility criterion](lem-compressible-criterion.md) is the case $B_0 = B_1$, and the Lean proves it that way.

This is the form the $\mathrm{coRE}$ direction of $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$ needs (Section [The commuting-operator class](../downstream-results/README.md)): the compressor is asked to preserve a class of perfect strategies that compression completeness supplies, while the search recognizes the complement of the larger class of value $1$, which no compression theorem preserves.

## Lean

Formalized as [`MIPRE.Cost.compressibility_criterion_nested`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.compressibility_criterion_nested).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 349](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L349)
