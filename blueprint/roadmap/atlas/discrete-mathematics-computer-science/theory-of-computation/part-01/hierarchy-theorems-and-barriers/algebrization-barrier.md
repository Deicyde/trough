---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.Algebrization.multilinearExt, MetaMathlibExt.Complexity.KeyTheorems.Algebrization.baseAt, MetaMathlibExt.Complexity.KeyTheorems.Algebrization.polyBits, MetaMathlibExt.Complexity.KeyTheorems.Algebrization.extAnswer, MetaMathlibExt.Complexity.KeyTheorems.Algebrization.IsAlgebraicExtension, MetaMathlibExt.Complexity.KeyTheorems.Algebrization.aaronson_wigderson_algebrization
statement: formalized
---

# Algebrization barrier

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html).

## Multilinear extension of a Boolean function

Identify the booleans true and false with $1$
and $0$. Let $F$ be a field, $n$ a natural number and $f : \{0,1\}^n \to \{0,1\}$.
The multilinear extension of $f$ at a point $x = (x_0, \dots, x_{n-1}) \in F^n$ is

$$\sum_{a \in \{0,1\}^n} f(a) \prod_{i=0}^{n-1} \ell_{a_i}(x_i),$$

where $f(a) \in \{0, 1\}$ is read in $F$, $\ell_1(t) = t$ and $\ell_0(t) = 1 - t$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Algebrization.multilinearExt`, a definition declared in [WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html#multilinear-ext).

## Restriction of an oracle to inputs of length $n$

For a function $B$ from bitstrings to
booleans and a natural number $n$, the restriction of $B$ to inputs of length $n$ is the function
on $\{0,1\}^n$ sending $a = (a_0, \dots, a_{n-1})$ to $B(a_0 a_1 \cdots a_{n-1})$, the value of
$B$ at the bitstring $a$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Algebrization.baseAt`, a definition declared in [WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html#base-at).

## Coefficient bitstring of a polynomial over $\mathbb{F}_2$

For a polynomial $q$ over
$\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$ and a natural number $n$, the coefficient bitstring of $q$
with parameter $n$ is the bitstring $b_0 b_1 \cdots b_{n+1}$ of length $n + 2$ in which $b_i$ is
true exactly when the coefficient of $X^i$ in $q$ equals $1$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Algebrization.polyBits`, a definition declared in [WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html#poly-bits).

## Answer bits of the algebraic extension oracle

Let $n$ be a natural number, let $p$ be a
monic irreducible polynomial of degree $n + 1$ over $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, let
$F = \mathbb{F}_2[X]/(p)$ with $\alpha$ the class of $X$, let $B$ be a function from bitstrings to
booleans, and let $\tilde B_n$ be the multilinear extension over $F$ of the restriction of $B$ to
inputs of length $n$. Given a list $(e_0, e_1, \ldots)$ of bitstrings and an index $j$ with
$0 \le j \le n$, let $e_{i,k} \in \{0, 1\}$ be the bit of $e_i$ at position $k$, counting from
$0$, where a missing list entry or a missing bit counts as $0$, and let $x \in F^n$ be the point
with coordinates $x_i = \sum_{k=0}^{n} e_{i,k} \alpha^k$ for $i < n$. The answer bit is true
exactly when the coefficient of $\alpha^j$ in $\tilde B_n(x)$, written in the basis
$1, \alpha, \dots, \alpha^n$ of $F$ over $\mathbb{F}_2$, equals $1$.

The index $j$ ranges over $0, \dots, n$ only: an out-of-range index must be rejected by the
caller, not reduced modulo $n + 1$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Algebrization.extAnswer`, a definition declared in [WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html#ext-answer).

## Algebraic extension oracles

Let $B$ and $O$ be oracles, that is, functions from
bitstrings to booleans. Then $O$ is an algebraic extension of $B$ when there are polynomials
$\pi_0, \pi_1, \pi_2, \ldots$ over $\mathbb{F}_2 = \mathbb{Z}/2\mathbb{Z}$, each $\pi_n$ monic and
irreducible of degree $n + 1$, with the following two properties, where $F_n$ is the field
$\mathbb{F}_2[X]/(\pi_n)$, $\alpha_n$ is the class of $X$ in $F_n$, and $\tilde B_n$ is the
multilinear extension over $F_n$ of the restriction of $B$ to inputs of length $n$. First, the
map sending a bitstring $u$ to the coefficient bitstring of $\pi_{|u|}$ with parameter $|u|$
(whose bits say which of the coefficients of $X^0, \dots, X^{|u|+1}$ equal $1$) is
polynomial-time computable. Second, let $y$ be a bitstring. If $y$ decodes, under the canonical
bitstring encoding of triples, to a triple $(u, (e_0, \dots, e_{m-1}), j)$ of a bitstring $u$, a
list of bitstrings and a natural number $j$ such that, writing $n = |u|$, we have $m = n$, every
$e_i$ has length $n + 1$ and $j \le n$, then $O(y)$ is true exactly when the coefficient of
$\alpha_n^j$ in $\tilde B_n(x)$, written in the basis $1, \alpha_n, \dots, \alpha_n^n$ of $F_n$
over $\mathbb{F}_2$, equals $1$. Here $x \in F_n^n$ is the point with coordinates
$x_i = \sum_{k=0}^{n} e_{i,k} \alpha_n^k$, where $e_{i,k} \in \{0, 1\}$ is the bit of $e_i$ at
position $k$, counting from $0$. Otherwise, in particular when $y$ does not decode, $O(y)$ is
false.

Every malformed query is answered false, so an oracle machine cannot route around the algebraic
structure through invalid encodings, and an out-of-range $j$ does not wrap around to
coordinate $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.Algebrization.IsAlgebraicExtension`, a definition declared in [WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html#is-algebraic-extension).

## Aaronson-Wigderson: the algebrization barrier

Call an oracle a function from bitstrings
to booleans. There are oracles $B$ and $\tilde B$ such that $\tilde B$ is an algebraic extension
of $B$ and $\mathsf{P}^B = \mathsf{NP}^{\tilde B}$. There are also oracles $B$ and $\tilde B$ such
that $\tilde B$ is an algebraic extension of $B$ and $\mathsf{NP}^B$ is not contained in
$\mathsf{P}^{\tilde B}$.

## Sources

- S. Aaronson and A. Wigderson, "Algebrization: A new barrier in complexity theory", Proceedings of the Fortieth Annual ACM Symposium on Theory of Computing (STOC 2008), 731-740 (journal version in ACM Transactions on Computation Theory 1 (2009)).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.Algebrization.aaronson_wigderson_algebrization` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/AlgebrizationWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html#aaronson-wigderson-algebrization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Algebrization barrier](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/algebrization-barrier)
