---
declaration: lemma
origin: cited
lean: MIPRE.Cost.compressibility_criterion, MIPRE.Cost.compressibility_criterion_levels
statement: formalized
proof: formalized
---

# Compressibility criterion

Let $A, B \subseteq \{0,1\}^*$ be languages with distinguished elements $y_{\mathrm{yes}} \in A$ and $y_{\mathrm{no}} \in B$, and suppose that the complement of $B$ is recursively enumerable: there is a program $S$ that halts on input $x$ if and only if $x \notin B$. Suppose there is a polynomial-time computable function $\textsc{Compr} : \{0,1\}^* \times \mathbb{N} \to \{0,1\}^*$ such that whenever $\hat{x}$ is a succinct description (Definition [Succinct description](../foundations/part-02/def-succinct.md)) of a string $x$ with $\left\vert {x} \right\vert \leq n + 1$ and $y = \textsc{Compr}(\hat{x}, n)$:

1. if $x \in A$ then $y \in A$, and
2. if $x \in B$ then $y \in B$.

Then there is a polynomial-time computable function $g$ reducing the halting problem to $(A, B)$: for every Turing machine $e$, if $\phi_e$ halts on the empty input then $g(e) \in A$, and otherwise $g(e) \in B$.

## Depends on

- [Succinct description](../foundations/part-02/def-succinct.md)
- [Efficient universal Turing machine](lem-universal-tm.md)
- [Efficient s-m-n](lem-smn.md)
- [Efficient Kleene recursion theorem](lem-kleene.md)
- [Compressibility criterion, nested classes](lem-compressible-criterion-nested.md)

## Proof

The construction of Lemma [Recursive compression](lem-recursive-compression.md), with a third branch. Let $\beta$ be the bit-query program of that proof, and let $\sigma$ be the program that, on $((c', (e, (m, m))), \cdot)$, runs the universal machine on $c'$ with input $(e, (m, m))$ to obtain a string $x$ and then runs $S$ on $x$. Let $a$ be the polynomial-time decider that on $(c', (e, (m, n)))$ outputs $y_{\mathrm{yes}}$ if $e$ halts on the empty input within $\log n$ steps; otherwise $y_{\mathrm{no}}$ if $s(\sigma, (c', (e, (m, m))))$ halts within $\log n$ steps; and otherwise $\textsc{Compr}\bigl((s(\beta, ((c', e), (m, 2n+1))), n), n\bigr)$, where $s$ is the s-m-n map of Lemma [Efficient s-m-n](lem-smn.md). By Lemma [Efficient Kleene recursion theorem](lem-kleene.md) there is a program $c$ with $\phi_c(e, (m, n)) = \phi_a(c, (e, (m, n))) =: h(e, m, n)$, running in time polynomial in $\left\vert {e} \right\vert + \log m + \log n$. As before, for $n$ above a threshold $r(e) = 2^{K + 1 + \left\vert {e} \right\vert}$ and $m = r(e)$, the pair $(s(\beta, ((c, e), (m, 2n+1))), n)$ is a succinct description of $h(e, m, 2n+1)$; the start level $m$ is carried as data so that the threshold can be chosen from the running time of $a$ afterwards. The reduction is $g(e) = h(e, r(e), r(e)) =: x_e$; the second branch tests, at each level it is run at, whether $S$ halts on $x_e$. Two facts are used implicitly below and hold along the chain: $\left\vert {m} \right\vert \leq \left\vert {n} \right\vert$ at levels $n \geq r(e) \geq m$, which is what keeps $K$ out of its own defining polynomial; and “$e$ halts within $\log n$ steps” is monotone in $n$, so the first branch, once it fires, fires at every higher level.

If $e$ does not halt, suppose $x_e \notin B$. Then $S$ halts on $x_e$ in some time $T$, so at every level $n$ with $\log n \geq T$ the decider outputs $y_{\mathrm{no}} \in B$, and by downward induction along the levels $r(e), 2r(e)+1, 4r(e)+3, \ldots$ from such a level, property 2 of $\textsc{Compr}$ gives $h(e, r(e), n) \in B$ at every level of the chain, in particular $x_e \in B$, a contradiction. If $e$ halts in $T$ steps, then $h(e, r(e), n) = y_{\mathrm{yes}} \in A$ once $\log n \geq T$, and by downward induction property 1 gives $h(e, r(e), n) \in A$ at every level of the chain, provided the second branch never fires at a level where the first has not. If it fired at such a level $n_1$, then $S$ halts on $x_e$, so $x_e \notin B$; but the output $y_{\mathrm{no}} \in B$ at level $n_1$ and property 2, by downward induction along the levels between $r(e)$ and $n_1$ (at which the first branch does not fire either), give $x_e \in B$, a contradiction. Hence $g(e) = x_e \in A$.

## Lean

Formalized as [`MIPRE.Cost.compressibility_criterion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.compressibility_criterion), [`MIPRE.Cost.compressibility_criterion_levels`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.compressibility_criterion_levels).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 293](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L293)
