---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.NPGate, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.npCircuitEval, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.truthTable, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.NaturalProperty, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.langOfFamily, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.UsefulAgainstPPoly, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.PRFInPPoly, MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.PRFSecure
statement: formalized
---

# Natural proofs barrier

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html).

## Encoded gates

An encoded gate of a flat Boolean circuit is a pair $(k, r)$ of a natural
number $k$ (its kind) and a list $r$ of natural numbers (its references), in the shared encoding
of gates as (kind, references) pairs.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.NPGate`, an abbreviation declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#npgate).

## Evaluation of an encoded circuit

Given a list of encoded gates $g_0, \dots, g_{m-1}$,
each a (kind, references) pair, and a list of Booleans $a = (a_0, \dots, a_{n-1})$, this is the
list of the values of all $m$ gates, in order: each pair is decoded to a gate of a flat Boolean
circuit on $n$ inputs, and the resulting circuit is evaluated with input $i$ set to $a_i$. An
input pair $(0, [i])$ with $i \ge n$ decodes to the constant false, so it reads as false.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.npCircuitEval`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#np-circuit-eval).

## Truth table

The truth table of a Boolean function $g$ on $n$ bits is the list of the
$2^n$ values $g(x^{(0)}), g(x^{(1)}), \dots, g(x^{(2^n - 1)})$, where for $i < 2^n$ the input
$x^{(i)}$ has bit $j$ equal to the $j$-th binary digit $\lfloor i / 2^j \rfloor \bmod 2$ of $i$
(bit $0$ being the least significant), for every $j < n$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.truthTable`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#truth-table).

## Natural property

Let $C = (C_n)_{n \in \mathbb{N}}$, where $C_n$ is a set of Boolean
functions on $n$ bits. Then $C$ is natural when it is constructive and large. Constructive: there
are a polynomial $q$ with natural-number coefficients and, for every $n$, a circuit given as a
list of at most $q(2^n)$ encoded gates, such that a Boolean function $g$ on $n$ bits lies in $C_n$
if and only if the evaluation of the circuit on the truth table of $g$ has last gate value true.
Large: there is a natural number $c$ such that $|C_n| \ge 2^{2^n} / 2^{cn}$ for every $n$, that is,
$C_n$ contains at least a $2^{-cn}$ fraction of the $2^{2^n}$ Boolean functions on $n$ bits.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.NaturalProperty`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#natural-property).

## The decision problem of a family of Boolean functions

For a family
$f = (f_n)_{n \in \mathbb{N}}$, where $f_n$ is a Boolean function on $n$ bits, this is the decision
problem that maps a bitstring $x = x_0 x_1 \cdots x_{n-1}$ of length $n$ to
$f_n(x_0, \dots, x_{n-1})$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.langOfFamily`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#lang-of-family).

## Usefulness against P/poly

Let $C = (C_n)_{n \in \mathbb{N}}$, where $C_n$ is a set of
Boolean functions on $n$ bits. Then $C$ is useful against P/poly when, for every family
$f = (f_n)_{n \in \mathbb{N}}$ of Boolean functions $f_n$ on $n$ bits such that $f_n \in C_n$ for
infinitely many $n$, the decision problem of $f$ is not in P/poly. Equivalently, if the decision
problem of a family $f$ is in P/poly, then $f_n \in C_n$ for only finitely many $n$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.UsefulAgainstPPoly`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#useful-against-ppoly).

## Keyed function families in P/poly

Let $F = (F_n)_{n \in \mathbb{N}}$ be a keyed family of
Boolean functions: $F_n(k, x)$ is a Boolean value for every key $k \in \{0,1\}^{n^2}$ and every
input $x \in \{0,1\}^n$. Then $F$ is in P/poly when there is a polynomial $p$ with natural-number
coefficients such that for every $n$ some circuit, given as a list of at most $p(n)$ encoded
gates, computes $F_n$: for all $k$ and $x$, the evaluation of the circuit on the bitstring $kx$ of
length $n^2 + n$ (the bits of $k$ followed by the bits of $x$) has last gate value $F_n(k, x)$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.PRFInPPoly`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#prfin-ppoly).

## Security of a keyed function family against truth-table distinguishers

Let
$F = (F_n)_{n \in \mathbb{N}}$ be a keyed family of Boolean functions: $F_n(k, x)$ is a Boolean
value for every key $k \in \{0,1\}^{n^2}$ and every input $x \in \{0,1\}^n$. Write $F_{n,k}$ for the
Boolean function $x \mapsto F_n(k, x)$ on $n$ bits and $T(g)$ for the truth table of a Boolean
function $g$. Then $F$ is secure when the following holds for every polynomial $q$ with
natural-number coefficients and every sequence $(D_n)_{n \in \mathbb{N}}$ of functions from
bitstrings to Booleans such that, for each $n$, some circuit given as a list of at most $q(2^n)$
encoded gates has last gate value $D_n(t)$ on every bitstring $t$: for every natural number $c$
there is a natural number $N$ such that for every $n \ge N$

$$\left| \frac{|\{k \in \{0,1\}^{n^2} : D_n(T(F_{n,k})) = \mathrm{true}\}|}{2^{n^2}} -
\frac{|\{g : D_n(T(g)) = \mathrm{true}\}|}{2^{2^n}} \right| \le \frac{1}{2^{nc}},$$

where $g$ ranges over all $2^{2^n}$ Boolean functions on $n$ bits. That is, a distinguisher
computed by circuits of size polynomial in the truth-table size $2^n$ tells a uniformly random
member of the family from a uniformly random Boolean function with advantage at most $2^{-cn}$
for all large $n$, for every $c$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.PRFSecure`, a definition declared in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#prfsecure).

## Razborov-Rudich: the natural proofs barrier

Let $F = (F_n)_{n \in \mathbb{N}}$ be a keyed
family of Boolean functions, where $F_n(k, x)$ is a Boolean value for every key
$k \in \{0,1\}^{n^2}$ and every input $x \in \{0,1\}^n$. If $F$ is in P/poly (computed by circuits
of size polynomial in $n$) and is secure against truth-table distinguishers, then there is no
property $C = (C_n)_{n \in \mathbb{N}}$, with $C_n$ a set of Boolean functions on $n$ bits, that
is both natural and useful against P/poly.

## Sources

- A. A. Razborov and S. Rudich, "Natural proofs", Journal of Computer and System Sciences 55 (1997), 24-35 (Proceedings of the Twenty-Sixth Annual ACM Symposium on Theory of Computing, STOC 1994, 18-27).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NaturalProofs.razborov_rudich_natural_proofs` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NaturalProofsWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html#razborov-rudich-natural-proofs).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Natural proofs barrier](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/natural-proofs-barrier)
