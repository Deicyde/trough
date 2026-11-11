---
declaration: section
origin: cited
lean: MetaMathlibExt.GesselAlphabet, MetaMathlibExt.gesselUnbarredCount, MetaMathlibExt.gesselBarredCount, MetaMathlibExt.gesselBalance, MetaMathlibExt.IsGesselWord, MetaMathlibExt.IsCompleteGesselWord, MetaMathlibExt.isCompleteGesselWord_iff_balance_eq_zero
statement: formalized
proof: formalized
---

# Gessel words

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html).

## Gessel alphabet

For a natural number $n$, the Gessel alphabet over
$S = [n] = \{1, \dots, n\}$ is the disjoint union of an unbarred copy and a barred copy of $[n]$:
it has an unbarred letter $i$ and a barred letter $\bar{i}$ for each $i \in [n]$.

Each copy is indexed by $\{0, \dots, n - 1\}$, the index $j$ standing for the label $j + 1$.

Formalized by `MetaMathlibExt.GesselAlphabet`, an abbreviation declared in [MathlibExt/NumberTheory/GesselWord.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GesselWord.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#gessel-alphabet).

## Unbarred occurrences of a label

Let $n$ be a natural number, let $w$ be a word (a finite
sequence of letters) over the Gessel alphabet over $[n] = \{1, \dots, n\}$ and let $m$ be a
natural number. The unbarred count of $m$ in $w$ is the number of positions of $w$ that hold the
unbarred letter $m$; it is $0$ when $m \notin [n]$.

Formalized by `MetaMathlibExt.gesselUnbarredCount`, a definition declared in [MathlibExt/NumberTheory/GesselWord.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GesselWord.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#gessel-unbarred-count).

## Barred occurrences of a label

Let $n$ be a natural number, let $w$ be a word (a finite
sequence of letters) over the Gessel alphabet over $[n] = \{1, \dots, n\}$ and let $m$ be a
natural number. The barred count of $m$ in $w$ is the number of positions of $w$ that hold the
barred letter $\bar{m}$; it is $0$ when $m \notin [n]$.

Formalized by `MetaMathlibExt.gesselBarredCount`, a definition declared in [MathlibExt/NumberTheory/GesselWord.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GesselWord.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#gessel-barred-count).

## Signed balance of a label

Let $n$ be a natural number, let $w$ be a word over the Gessel
alphabet over $[n] = \{1, \dots, n\}$ and let $m$ be a natural number. The signed balance of $m$
in $w$ is the integer obtained by subtracting the number of occurrences of the barred letter
$\bar{m}$ in $w$ from the number of occurrences of the unbarred letter $m$ in $w$; it is $0$ when
$m \notin [n]$.

Formalized by `MetaMathlibExt.gesselBalance`, a definition declared in [MathlibExt/NumberTheory/GesselWord.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GesselWord.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#gessel-balance).

## Gessel word

Let $n$ be a natural number. For a word $u$ over the Gessel alphabet over
$S = [n] = \{1, \dots, n\}$ and a natural number $m$, write $\beta_u(m)$ for the signed balance of
$m$ in $u$: the number of occurrences of the unbarred letter $m$ in $u$ minus the number of
occurrences of the barred letter $\bar{m}$ in $u$. A word $w$ over this alphabet is a Gessel word
when, for every prefix $w'$ of $w$ (including the empty word and $w$ itself) and every $k$ with
$1 \le k \le n$, we have $\sum_{i=1}^{k} \beta_{w'}(n + 1 - i) \ge 0$, that is, the signed
balances in $w'$ of the $k$ largest labels $n, n - 1, \dots, n + 1 - k$ have nonnegative sum.

Formalized by `MetaMathlibExt.IsGesselWord`, a definition declared in [MathlibExt/NumberTheory/GesselWord.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GesselWord.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#is-gessel-word).

## Complete Gessel words

A word $w$ over the Gessel alphabet of $S = [n] = \{1, \dots, n\}$
is a complete Gessel word when it is a Gessel word and, for every $m \in [n]$, the unbarred
letter $m$ and the barred letter $\bar m$ occur the same number of times in $w$.

Formalized by `MetaMathlibExt.IsCompleteGesselWord`, a definition declared in [MathlibExt/NumberTheory/CompleteGesselWord.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CompleteGesselWord.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#is-complete-gessel-word).

## Complete Gessel words are the Gessel words of zero balance

A word $w$ over the Gessel
alphabet of $[n] = \{1, \dots, n\}$ is a complete Gessel word if and only if it is a Gessel word
and, for every $m \in [n]$, the signed balance of $m$ in $w$ (the number of occurrences of the
unbarred letter $m$ minus the number of occurrences of the barred letter $\bar m$) is zero.

Formalized by `MetaMathlibExt.isCompleteGesselWord_iff_balance_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/CompleteGesselWord.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CompleteGesselWord.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html#is-complete-gessel-word-iff-balance-eq-z).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gessel words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/gessel-words)
