---
declaration: lemma
origin: cited
lean: MIPRE.Cost.recursive_compression
statement: formalized
proof: formalized
---

# Recursive compression

Let $f : \{0,1\}^* \to \mathbb{N} \cup \{\infty\}$ be a function and $A \subseteq \{x : f(x) < \infty\}$ a nonempty language. Suppose there is a polynomial-time computable function $\textsc{Compr} : \{0,1\}^* \times \mathbb{N} \to \{0,1\}^*$ such that whenever $\hat{x}$ is a succinct description (Definition [Succinct description](../foundations/part-02/def-succinct.md)) of a string $x$ and $y = \textsc{Compr}(\hat{x}, n)$:

1. $f(y) \geq \max\{ f(x), n \}$, and
2. if $x \in A$ then $y \in A$.

Then there is a polynomial-time computable function $g$ reducing the halting problem to $A$: for every Turing machine $e$, if $\phi_e$ halts on the empty input then $g(e) \in A$, and otherwise $f(g(e)) = \infty$.

## Depends on

- [Succinct description](../foundations/part-02/def-succinct.md)
- [Efficient universal Turing machine](lem-universal-tm.md)
- [Efficient s-m-n](lem-smn.md)
- [Efficient Kleene recursion theorem](lem-kleene.md)

## Proof

The construction of (MNY), with two harmless modifications: the “next level” of the recursion is $2n + 1$ instead of $n + 1$ (prepending a bit to a binary numeral is one step in the list language, an increment is not), and the threshold below is explicit. Let $\beta$ be the fixed *bit-query* program that, on input $(((c', e), n), m)$, runs the universal machine on $c'$ with input $(e, n)$ to obtain a string $y$ and outputs the $m$-th bit of $y$ (or $2$ if $m \geq \left\vert {y} \right\vert$). Let $a$ be the polynomial-time *decider* that on $(c', (e, n))$ outputs a fixed $y_0 \in A$ if $e$ halts on the empty input within $\log n$ steps, and $\textsc{Compr}\bigl((s(\beta, ((c', e), 2n+1)), n), n\bigr)$ otherwise, where $s$ is the s-m-n map of Lemma [Efficient s-m-n](lem-smn.md). By Lemma [Efficient Kleene recursion theorem](lem-kleene.md) there is a program $c$ with $\phi_c(e, n) = \phi_a(c, (e, n)) =: h(e, n)$, running in time polynomial in $\left\vert {e} \right\vert + \log n$. Hence for $n$ above a threshold $r(e) = 2^{K + 1 + \left\vert {e} \right\vert}$ (with $K$ a constant depending only on the polynomial overheads), $(s(\beta, ((c, e), 2n+1)), n)$ is a succinct description of $h(e, 2n+1)$: the string has length at most $2^n$ and the bit-query program answers within the budget of Definition [Succinct description](../foundations/part-02/def-succinct.md). The reduction is $g(e) = h(e, r(e))$. If $e$ does not halt, then for every $n \geq r(e)$ the decider compresses, so $f(h(e, n)) \geq \max\{f(h(e, 2n+1)), n\}$, and iterating gives $f(h(e, n)) \geq n + k$ for all $k$, i.e. $f(g(e)) = \infty$. If $e$ halts in $T$ steps, then $h(e, n) = y_0 \in A$ once $n \geq 2^T$, and by downward induction along the levels $n, 2n+1, 4n + 3, \ldots$ the second property of $\textsc{Compr}$ gives $h(e, n) \in A$ for every $n \geq r(e)$, in particular $g(e) \in A$.

## Lean

Formalized as [`MIPRE.Cost.recursive_compression`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.recursive_compression).

## Sources

- [MIP* = RE blueprint: content/04_computability.tex, line 227](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/04_computability.tex#L227)
