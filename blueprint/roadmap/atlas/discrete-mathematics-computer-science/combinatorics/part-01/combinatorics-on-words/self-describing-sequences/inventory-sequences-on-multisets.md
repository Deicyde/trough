---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MultisetSequenceLoopWanted.step, MathlibExt.Combinatorics.MultisetSequenceLoopWanted.conjecture, MathlibExt.Combinatorics.MultisetSequenceLoopWanted.conjecture_holds
statement: formalized
---

# Inventory sequences on multisets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/inventory-sequences-on-multisets/index.html).

## Inventory step

The inventory step sends a pair of finite lists of natural numbers (the two
rows of an array) to the pair consisting of the increasing list of the distinct numbers occurring
in either list and the list of how many times each of these numbers occurs in the two lists
together.

Formalized by `MathlibExt.Combinatorics.MultisetSequenceLoopWanted.step`, a definition declared in [WantedExt/Combinatorics/MultisetSequenceLoopWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MultisetSequenceLoopWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/inventory-sequences-on-multisets/index.html#step).

## Inventory loop conjecture

Let $a_1 < \dots < a_n$ and $b_1, \dots, b_n$ be positive
integers, and iterate the inventory step starting from the pair of rows $(a_1, \dots, a_n)$ and
$(b_1, \dots, b_n)$, where the inventory step replaces a pair of rows by the increasing list of the
distinct integers occurring in either row together with the list of the number of times each of
them occurs in the two rows combined. Then there are a natural number $t$ and a
$p \in \{1, 2, 3\}$ such that the $(t + p)$-th iterate equals the $t$-th iterate.

Formalized by `MathlibExt.Combinatorics.MultisetSequenceLoopWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/MultisetSequenceLoopWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MultisetSequenceLoopWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/inventory-sequences-on-multisets/index.html#conjecture).

## Inventory sequences end in short loops

Let $a_1 < \dots < a_n$ and $b_1, \dots, b_n$ be
positive integers, and iterate the inventory step starting from the pair of rows
$(a_1, \dots, a_n)$ and $(b_1, \dots, b_n)$, where the inventory step replaces a pair of rows by the
increasing list of the distinct integers occurring in either row together with the list of the
number of times each of them occurs in the two rows combined. Then there are a natural number
$t$ and a $p \in \{1, 2, 3\}$ such that the $(t + p)$-th iterate equals the $t$-th iterate.

Resolved in the affirmative: the process is the counting (inventory) map on multisets. Bronstein
and Fraenkel proved that every start is ultimately periodic, and the enumeration of all cycles
(Sauerberg and Shu, re-derived by Cain and Enin) shows that every cycle has length 1, 2 or 3.

## Sources

- V. Bronstein and A. S. Fraenkel, On a curious property of counting sequences, Amer. Math. Monthly 101 (1994), https://doi.org/10.1080/00029890.1994.11996991; J. Sauerberg and L. Shu, The long and the short on counting sequences, Amer. Math. Monthly 104 (1997), https://doi.org/10.1080/00029890.1997.11990642; O. M. Cain and S. T. Enin, Inventory loops (i.e. counting sequences) have pre-period 2 max S_1 + 60, arXiv:2004.00209 (2020), https://arxiv.org/abs/2004.00209.

Stated but not proved: `MathlibExt.Combinatorics.MultisetSequenceLoopWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MultisetSequenceLoopWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MultisetSequenceLoopWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/inventory-sequences-on-multisets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inventory sequences on multisets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/inventory-sequences-on-multisets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/inventory-sequences-on-multisets)
