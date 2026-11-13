---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosProblem794Wanted.conjecture, MathlibExt.Combinatorics.ErdosProblem794Wanted.conjecture_refuted
statement: formalized
---

# Dense 3-uniform hypergraphs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/dense-3-uniform-hypergraphs/index.html).

## Erdős Problem 794 on dense 3-uniform hypergraphs

The proposition asserts that for every
natural number $n$ and every family $H$ of $3$-element subsets of $\{0, 1, \dots, 3n - 1\}$ with
at least $n^3 + 1$ members, there is a $4$-element set $S$ such that at least $3$ members of $H$
are subsets of $S$, or there is a $5$-element set $S$ such that at least $7$ members of $H$ are
subsets of $S$.

This is Erdős's original question in its positive form; it is known to be false.

Formalized by `MathlibExt.Combinatorics.ErdosProblem794Wanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosProblem794Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem794Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/dense-3-uniform-hypergraphs/index.html#conjecture).

## Refutation of Erdős Problem 794

It is not true that for every natural number $n$ and every
family $H$ of $3$-element subsets of $\{0, 1, \dots, 3n - 1\}$ with at least $n^3 + 1$ members,
there is a $4$-element set $S$ such that at least $3$ members of $H$ are subsets of $S$, or there
is a $5$-element set $S$ such that at least $7$ members of $H$ are subsets of $S$.

Phillip Harris gave an explicit counterexample on $9$ vertices.

## Sources

- Phillip Harris counterexample, formalized by Aristotle, ChatGPT, and Boris Alexeev at plby/lean-proofs, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos794.lean.

Stated but not proved: `MathlibExt.Combinatorics.ErdosProblem794Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosProblem794Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ErdosProblem794Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/dense-3-uniform-hypergraphs/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dense 3-uniform hypergraphs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/dense-3-uniform-hypergraphs/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-turan/dense-3-uniform-hypergraphs)
