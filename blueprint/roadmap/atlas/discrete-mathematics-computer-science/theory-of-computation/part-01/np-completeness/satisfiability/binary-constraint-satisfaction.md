---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.NPComplete.BinaryCsp.BinaryCspInstance, MetaMathlibExt.Complexity.NPComplete.BinaryCsp.WellFormed, MetaMathlibExt.Complexity.NPComplete.BinaryCsp.BinaryCspFeasible, MetaMathlibExt.Complexity.NPComplete.BinaryCsp.binaryCspDec, MetaMathlibExt.Complexity.NPComplete.BinaryCsp.binaryCsp_npComplete
statement: formalized
---

# Binary constraint satisfaction

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html).

## Binary CSP instances

A binary CSP instance is a pair consisting of a list
$(D_0, \dots, D_{n-1})$ of lists of natural numbers, where $D_j$ is the domain of variable $j$,
and a list of constraints, each a triple $(j, k, P)$ of two variable indices $j, k \in \mathbb{N}$
and a list $P$ of allowed value pairs in $\mathbb{N} \times \mathbb{N}$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinaryCsp.BinaryCspInstance`, an abbreviation declared in [WantedExt/Complexity/NPComplete/BinaryCspWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BinaryCspWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html#binary-csp-instance).

## Well-formed binary CSP instances

A binary CSP instance with domain list
$(D_0, \dots, D_{n-1})$ and constraint list $C$ is well formed when every constraint
$(j, k, P) \in C$ has $j < n$ and $k < n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinaryCsp.WellFormed`, a definition declared in [WantedExt/Complexity/NPComplete/BinaryCspWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BinaryCspWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html#well-formed).

## Feasible binary CSP instances

A binary CSP instance with domain list
$(D_0, \dots, D_{n-1})$ and constraint list $C$ is feasible when there is a list
$(a_0, \dots, a_{n-1})$ of natural numbers with $a_j \in D_j$ for every $j < n$ and
$(a_j, a_k) \in P$ for every constraint $(j, k, P) \in C$, where $a_i$ is read as $0$ for every
index $i \ge n$.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinaryCsp.BinaryCspFeasible`, a definition declared in [WantedExt/Complexity/NPComplete/BinaryCspWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BinaryCspWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html#binary-csp-feasible).

## Binary constraint satisfaction as a decision problem

The decision problem BINARY
CONSTRAINT SATISFACTION accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of binary CSP instances, to an instance that is well formed and feasible; it
rejects every other bitstring, including every bitstring that does not decode.

Formalized by `MetaMathlibExt.Complexity.NPComplete.BinaryCsp.binaryCspDec`, a definition declared in [WantedExt/Complexity/NPComplete/BinaryCspWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BinaryCspWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html#binary-csp-dec).

## BINARY CONSTRAINT SATISFACTION is NP-complete

The decision problem BINARY CONSTRAINT
SATISFACTION over bitstrings belongs to NP, and every decision problem in NP has a
polynomial-time many-one reduction to it.

## Sources

- M. R. Garey and D. S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness* (1979), CONSTRAINT SATISFACTION; R. Dechter, *Constraint Processing* (2003).

Stated but not proved: `MetaMathlibExt.Complexity.NPComplete.BinaryCsp.binaryCsp_npComplete` is written with `theorem_wanted` in [WantedExt/Complexity/NPComplete/BinaryCspWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/NPComplete/BinaryCspWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html#binary-csp-np-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary constraint satisfaction](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/np-completeness/satisfiability/binary-constraint-satisfaction)
