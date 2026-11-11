---
declaration: section
origin: cited
lean: MetaMathlibExt.raney_cycle_lemma_sum_neg_one_general, MetaMathlibExt.raney_cycle_lemma_sum_neg_one
statement: formalized
proof: formalized
---

# Raney's cycle lemma

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/raney-s-cycle-lemma/index.html).

## Raney's cycle lemma for arbitrary integer lists

Let $a = (a_0, \dots, a_{n-1})$ be a
list of integers whose entries sum to $-1$. Then there is exactly one index $r$ with $0 \le r < n$
such that every proper prefix of the rotation $(a_r, \dots, a_{n-1}, a_0, \dots, a_{r-1})$ has
nonnegative sum: for every $t$ with $0 \le t < n$, the sum of the first $t$ entries of this
rotation is at least $0$.

Formalized by `MetaMathlibExt.raney_cycle_lemma_sum_neg_one_general`, a theorem declared in [MathlibExt/Combinatorics/Lists/RaneyCycleLemma.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Lists/RaneyCycleLemma.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/raney-s-cycle-lemma/index.html#raney-cycle-lemma-sum-neg-one-general).

## Raney's cycle lemma

Let $a = (a_0, \dots, a_{n-1})$ be a list of integers, each at least
$-1$, whose entries sum to $-1$. Then there is exactly one index $r$ with $0 \le r < n$ such that
every proper prefix of the rotation $(a_r, \dots, a_{n-1}, a_0, \dots, a_{r-1})$ has nonnegative
sum: for every $t$ with $0 \le t < n$, the sum of the first $t$ entries of this rotation is at
least $0$.

The hypothesis that every entry is at least $-1$ is not needed; Raney's cycle lemma for arbitrary
integer lists proves the same conclusion without it.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL24/Haupt/haupt4.tex>, lines 804-807. Lean's zero-based left rotation is a bijective reindexing of the source's cut after `a_r`; `t < a.length` ranges over every proper prefix, with `t = 0` giving the true empty-prefix condition. The lower bound `hlower` is not needed; see `raney_cycle_lemma_sum_neg_one_general`.

Formalized by `MetaMathlibExt.raney_cycle_lemma_sum_neg_one`, a theorem declared in [MathlibExt/Combinatorics/Lists/RaneyCycleLemma.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Lists/RaneyCycleLemma.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/raney-s-cycle-lemma/index.html#raney-cycle-lemma-sum-neg-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Raney's cycle lemma](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/raney-s-cycle-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/raney-s-cycle-lemma)
