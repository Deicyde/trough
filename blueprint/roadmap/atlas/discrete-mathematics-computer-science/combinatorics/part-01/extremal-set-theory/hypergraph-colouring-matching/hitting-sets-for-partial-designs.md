---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosBlockDesignHittingSetWanted.conjecture, MathlibExt.Combinatorics.ErdosBlockDesignHittingSetWanted.conjecture_refuted
statement: formalized
---

# Hitting sets for partial designs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hitting-sets-for-partial-designs/index.html).

## Bounded hitting sets for large partial designs (Erdős Problem 664)

The proposition that
for every real $c$ with $0 < c < 1$ there is a natural number $C$ such that for every natural
number $n$ and every family $\mathcal{B}$ of subsets of $\{0, \dots, n - 1\}$ in which each member
has more than $c\sqrt{n}$ elements and any two distinct members share at most one element, some
set $B \subseteq \{0, \dots, n - 1\}$ meets every member of $\mathcal{B}$ in at least $1$ and at
most $C$ elements.

Formalized by `MathlibExt.Combinatorics.ErdosBlockDesignHittingSetWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/ErdosBlockDesignHittingSetWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosBlockDesignHittingSetWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hitting-sets-for-partial-designs/index.html#conjecture).

## Large partial designs need not have uniformly bounded hitting sets

It is not true that for
every real $c$ with $0 < c < 1$ there is a natural number $C$ such that for every natural number
$n$ and every family $\mathcal{B}$ of subsets of $\{0, \dots, n - 1\}$ in which each member has more
than $c\sqrt{n}$ elements and any two distinct members share at most one element, some set
$B \subseteq \{0, \dots, n - 1\}$ meets every member of $\mathcal{B}$ in at least $1$ and at most
$C$ elements.

Alon answered the question negatively in the source report (Oberwolfach Report 42/2025,
pp. 2249-2250, Theorem 3; also Theorem 2.1 of his note 'Blocking partial designs and
block-compatible sequences'), recorded on erdosproblems.com/664 (DISPROVED): for large prime
powers $q$ and $n = m = q^2 + q + 1$ there is a partial design of $m$ blocks of size
$> 0.4\sqrt{n}$ on $n$ points such that every set meeting all blocks meets some block in at least
$0.1 \log n$ points, so no constant $C$ works for $c \le 0.4$.

## Sources

- N. Alon, On designs and partial designs, extended abstract in Oberwolfach Report 42/2025 (Combinatorics, Probability and Computing), pp. 2249-2250, Theorem 3, https://doi.org/10.4171/owr/2025/42; N. Alon, Blocking partial designs and block-compatible sequences, note, Theorem 2.1, https://web.math.princeton.edu/~nalon/PDFS/remark191.pdf; T. F. Bloom, Erdős Problem #664, erdosproblems.com (status DISPROVED), https://www.erdosproblems.com/664.

Stated but not proved: `MathlibExt.Combinatorics.ErdosBlockDesignHittingSetWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosBlockDesignHittingSetWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosBlockDesignHittingSetWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hitting-sets-for-partial-designs/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hitting sets for partial designs](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hitting-sets-for-partial-designs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/hitting-sets-for-partial-designs)
