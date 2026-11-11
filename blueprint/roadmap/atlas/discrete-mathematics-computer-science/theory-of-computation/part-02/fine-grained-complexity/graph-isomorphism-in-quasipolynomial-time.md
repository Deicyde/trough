---
declaration: section
origin: cited
lean: MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.GraphCode, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.natBits, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.natToBits, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.encode, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.encodePair, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.Isomorphic, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.qpTime, MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.conjecture
statement: formalized
---

# Graph isomorphism in quasipolynomial time

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html).

## Graph codes

A graph code consists of a vertex count $n \in \mathbb{N}$, with vertices
$0, \dots, n-1$, and a Boolean adjacency matrix $A$ on these vertices that is symmetric
($A_{ij} = A_{ji}$ for all $i, j$) and loop-free ($A_{ii}$ is false for every $i$).

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.GraphCode`, a structure declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#graph-code).

## Binary digits of a natural number

The binary digits of $n \in \mathbb{N}$, most
significant first, as a list of bits with the digit $1$ read as true and $0$ as false; for
$n = 0$ this is the single digit $0$.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.natBits`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#nat-bits).

## Prefix-free encoding of a natural number

The prefix-free encoding of $n \in \mathbb{N}$
consists of $k$ true bits, where $k$ is the number of binary digits of $n$, then one false bit,
then the binary digits of $n$, most significant first.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.natToBits`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#nat-to-bits).

## Bit encoding of a graph code

The bit encoding of a graph code with $n$ vertices and
adjacency matrix $A$ is the prefix-free encoding of $n$ followed by the $n^2$ entries of $A$, as
bits, in row-major order: $A_{0,0}, A_{0,1}, \dots, A_{0,n-1}, A_{1,0}, \dots, A_{n-1,n-1}$.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.encode`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#encode).

## Bit encoding of a pair of graph codes

The bit encoding of a pair $(G, H)$ of graph codes
is the bit encoding of $G$ followed by the bit encoding of $H$.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.encodePair`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#encode-pair).

## Isomorphism of graph codes

Graph codes $G$ and $H$ with adjacency matrices $A$ and $B$
are isomorphic when they have the same vertex count $n$ and there is a permutation $\sigma$ of
the vertices $\{0, \dots, n-1\}$ such that $A_{ij} = B_{\sigma(i)\sigma(j)}$ for all $i, j$.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.Isomorphic`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#isomorphic).

## Quasipolynomial time bound

For an exponent $c \in \mathbb{N}$ and an input length
$n \in \mathbb{N}$, the quasipolynomial time bound is
$q_c(n) = 2^{(\lfloor \log_2(n+2) \rfloor + 2)^c}$.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.qpTime`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#qp-time).

## The quasipolynomial graph isomorphism statement

The proposition that graph isomorphism
is decidable in quasipolynomial time: there are a function $D$ from pairs of graph codes to
Booleans, an exponent $c \in \mathbb{N}$, and a deterministic multi-stack Turing machine with a
time function $t : \mathbb{N} \to \mathbb{N}$ that, on the bit encoding of every pair $(G, H)$,
outputs the single bit $D(G, H)$ within $t(\ell)$ steps, where $\ell$ is the length of the
encoding, such that $t(n) \le q_c(n)$ for every $n \in \mathbb{N}$, where $q_c$ is the
quasipolynomial time bound with exponent $c$, and $D(G, H)$ is true if and only if $G$ and $H$
are isomorphic.

## Sources

- ALG-016.

Formalized by `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.conjecture`, a definition declared in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#conjecture).

## Babai's theorem: graph isomorphism in quasipolynomial time

The quasipolynomial graph
isomorphism statement holds: there are a function $D$ from pairs of graph codes to Booleans, an
exponent $c \in \mathbb{N}$, and a deterministic multi-stack Turing machine with a time function
$t : \mathbb{N} \to \mathbb{N}$ that, on the bit encoding of every pair $(G, H)$, outputs the
single bit $D(G, H)$ within $t(\ell)$ steps, where $\ell$ is the length of the encoding, such that
$t(n) \le 2^{(\lfloor \log_2(n+2) \rfloor + 2)^c}$ for every $n \in \mathbb{N}$, and $D(G, H)$ is
true if and only if $G$ and $H$ are isomorphic.

Babai (STOC 2016) gave a deterministic quasipolynomial-time graph-isomorphism algorithm; the
corrected proof retains that complexity.

## Sources

- Babai, L., Graph isomorphism in quasipolynomial time, Proc. 48th ACM Symp. Theory Comput. (STOC 2016), 684-697; arXiv:1512.03547, https://arxiv.org/abs/1512.03547.

Stated but not proved: `MathlibExt.ComputerScience.GraphIsomorphismQuasipolynomialWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/ComputerScience/GraphIsomorphismQuasipolynomialWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph isomorphism in quasipolynomial time](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/fine-grained-complexity/graph-isomorphism-in-quasipolynomial-time)
