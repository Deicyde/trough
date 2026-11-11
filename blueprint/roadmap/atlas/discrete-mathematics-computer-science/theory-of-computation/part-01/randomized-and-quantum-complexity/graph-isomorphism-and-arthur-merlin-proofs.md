---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.GIInNPCoAM.graphIsoDec, MetaMathlibExt.Complexity.KeyTheorems.GIInNPCoAM.graph_iso_in_np_coam, MetaMathlibExt.Complexity.KeyTheorems.GNIInAM.graphNonIsoDec, MetaMathlibExt.Complexity.KeyTheorems.GNIInAM.graph_noniso_in_am
statement: formalized
---

# Graph isomorphism and Arthur–Merlin proofs

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs/index.html).

## Directed graph isomorphism as a decision problem

The decision problem accepts a bitstring
$x$ exactly when $x$ decodes, under the canonical bitstring encoding, to a triple $(n, E_1, E_2)$
of a natural number $n$ and two lists $E_1$ and $E_2$ of pairs of natural numbers for which
there is a bijection $f$ of $\{0, \dots, n - 1\}$ such that for all $a, b < n$, $(a, b) \in E_1$
if and only if $(f(a), f(b)) \in E_2$. Bitstrings that do not decode to such a triple are
rejected.

Pairs in $E_1$ or $E_2$ with an entry at least $n$ play no role.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GIInNPCoAM.graphIsoDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/GIInNPCoAMWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GIInNPCoAMWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs/index.html#graph-iso-dec).

## Graph isomorphism is in NP and coAM

The directed graph isomorphism decision problem
belongs to NP and to coAM.

## Sources

- O. Goldreich, "On the complexity of graph isomorphism" and the Goldreich-Micali-Wigderson interactive proof for graph non- isomorphism; see J. Köbler, U. Schöning, and J. Torán, The Graph Isomorphism Problem: Its Structural Complexity, Birkhäuser, 1993.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.GIInNPCoAM.graph_iso_in_np_coam` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/GIInNPCoAMWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GIInNPCoAMWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs/index.html#graph-iso-in-np-coam).

## Directed graph non-isomorphism as a decision problem

The decision problem accepts a
bitstring $x$ exactly when $x$ decodes, under the canonical bitstring encoding of triples
$(n, E_1, E_2)$ of a natural number and two lists of pairs of natural numbers, to a triple for
which there is no bijection $f$ from $\{0, \ldots, n - 1\}$ to itself such that, for all
$a, b < n$, $(a, b) \in E_1$ if and only if $(f(a), f(b)) \in E_2$. Bitstrings that do not
decode are rejected.

Pairs in $E_1$ or $E_2$ with an entry at least $n$ play no role, so $E_1$ and $E_2$ are read as
directed graphs on the vertex set $\{0, \ldots, n - 1\}$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.GNIInAM.graphNonIsoDec`, a definition declared in [WantedExt/Complexity/KeyTheorems/GNIInAMWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GNIInAMWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs/index.html#graph-non-iso-dec).

## Graph non-isomorphism is in AM

The directed graph non-isomorphism decision problem
belongs to the class $\mathsf{AM}$ of decision problems decided by Arthur–Merlin protocols.

## Sources

- O. Goldreich, S. Micali, and A. Wigderson, "Proofs that yield nothing but their validity, or all languages in NP have zero-knowledge proof systems", Journal of the ACM 38 (1991), 691-729 (FOCS 1986); O. Goldwasser and M. Sipser, "Private coins versus public coins in interactive proof systems", Advances in Computing Research 5 (1989), 73-90.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.GNIInAM.graph_noniso_in_am` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/GNIInAMWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/GNIInAMWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs/index.html#graph-noniso-in-am).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Graph isomorphism and Arthur–Merlin proofs](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/randomized-and-quantum-complexity/graph-isomorphism-and-arthur-merlin-proofs)
