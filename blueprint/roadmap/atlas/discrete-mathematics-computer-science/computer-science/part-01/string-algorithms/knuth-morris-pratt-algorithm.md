---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.kmpSearch, Array.mkPrefixTable_size, Array.mkPrefixTable_symbols, Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_some_iff, Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_none_iff, Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_none_iff_not_isInfix, Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_dropInfix?_map_length, Cslib.Algorithms.Lean.TimeM.kmpSearch_time_le
statement: formalized
proof: formalized
---

# Knuth–Morris–Pratt algorithm

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html).

## Time M

## Knuth–Morris–Pratt search

For lists $p$ (the pattern) and $t$ (the text) over a type
with a boolean equality, KMP search for $p$ in $t$ returns either a zero-based offset or no
offset, together with a cost: the number of symbol comparisons it makes. If $p$ is empty, it
returns the offset $0$ at cost $0$. Otherwise it first builds the prefix table of $p$, a list of
entries each pairing a symbol with a failure value. The transition of a table from a state $s$
on a symbol $x$ is defined as follows. If $s$ is less than the number of entries and $x$ equals the
symbol of entry $s$ (counting from $0$), the result is $s + 1$. Otherwise the result is $0$ when
$s = 0$, and when $s > 0$ it is the transition from the failure value of entry $s - 1$ on $x$.
Starting from the empty table, each symbol $x$ of $p$ in turn is appended as a new entry, with
failure value the transition of the current table on $x$ from the state equal to its number of
entries. The search then reads $t$ from the left, starting in state $0$ and moving to the
transition of the table on each symbol read. The first time the state equals $|p|$, after $j$
symbols have been read, it returns the offset $j - |p|$. If this never happens, it returns no
offset. The cost counts every equality test between two symbols, both while the table is built
and while $t$ is scanned. List operations, array access and arithmetic cost nothing.

When the boolean equality is lawful, the returned offset is the least offset at which $p$ occurs
in $t$, and no offset is returned exactly when $p$ does not occur in $t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search).

## Size of the KMP prefix table

For every pattern $p$, the KMP prefix table of $p$ has
exactly as many entries as $p$ has symbols, one for each symbol of $p$.

Formalized by `Array.mkPrefixTable_size`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#mk-prefix-table-size).

## The KMP prefix table stores the pattern

Each entry of the Knuth–Morris–Pratt prefix
table is a pair consisting of a symbol and a failure length. For every type with a Boolean
equality test and every list $p$ over it, the list of first components of the entries of the
prefix table built from $p$, read in order, equals $p$.

Formalized by `Array.mkPrefixTable_symbols`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#mk-prefix-table-symbols).

## KMP returns the first match

Let $p$ and $t$ be lists over a type with a lawful boolean
equality, and write $|t|$ for the length of $t$. For every natural number $i$, KMP search for
$p$ in $t$ returns the offset $i$ if and only if $p$ matches $t$ at $i$ and at no $j < i$, where
$p$ matches $t$ at $i$ when $i \le |t|$ and $p$ is a prefix of the list obtained from $t$ by
dropping its first $i$ elements.

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search-eq-some-iff).

## KMP finds no match exactly when no offset matches

For lists $p$ and $t$ over a type
with a lawful boolean equality, write $|t|$ for the length of $t$. KMP search for $p$ in $t$
returns no offset if and only if there is no natural number $i$ at which $p$ matches $t$, where
$p$ matches $t$ at $i$ when $i \le |t|$ and $p$ is a prefix of the list obtained from $t$ by
dropping its first $i$ elements.

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_none_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search-eq-none-iff).

## KMP finds no match exactly when the pattern does not occur

For lists $p$ (the pattern)
and $t$ (the text) over a type with a lawful boolean equality, KMP search for $p$ in $t$ returns
no offset if and only if $p$ is not a contiguous sublist of $t$, that is, there are no lists
$u$, $v$ with $t = u \, p \, v$ (concatenation).

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_none_iff_not_isInfix`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search-eq-none-iff-not-is-infix).

## KMP search agrees with the first-infix split

Let $p$ and $t$ be lists over a type
with a lawful boolean equality, with $p$ nonempty. Let the first-infix split of $t$ by $p$ be
the pair $(u, v)$ with $t = u \, p \, v$ (concatenation) and $u$ as short as possible, or
nothing if $p$ does not occur in $t$. Then the value returned by KMP search for $p$ in $t$ is
the length of $u$ if the split exists, and no offset otherwise.

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch_eq_dropInfix?_map_length`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 791](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L791). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search-eq-drop-infix-map-length).

## KMP search makes linearly many comparisons

For any pattern $p$ and text $t$, lists over
a type with a boolean equality, KMP search for $p$ in $t$ makes at most $2|p| + 2|t|$ symbol
comparisons in total, those made while building the prefix table included, where $|p|$ and
$|t|$ are the lengths of $p$ and $t$.

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 942](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L942). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search-time-le).

## The KMP failure function

Let $p$ be a pattern of length $n$ over a type with a lawful
boolean equality, and write $p_{\lt k}$ for its prefix of length $k$. Each entry of the KMP prefix
table of $p$ pairs a symbol of $p$ with a failure value. For every $q < n$, the failure value
$f$ of entry $q$ (counting from $0$) is the length of the longest proper prefix of $p_{\lt q+1}$
that is also a suffix of $p_{\lt q+1}$: $f \le q$, $p_{\lt f}$ is a suffix of $p_{\lt q+1}$, and every
$k \le q$ such that $p_{\lt k}$ is a suffix of $p_{\lt q+1}$ satisfies $k \le f$.

Formalized by `Array.mkPrefixTable_failure_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 966](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L966). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#mk-prefix-table-failure-spec).

## Correctness of the KMP transition

Let $p$ be a pattern of length $n$ over a type with
a lawful boolean equality, and write $p_{\lt k}$ for its prefix of length $k$. Let $c$ be a list,
$x$ a symbol, and $cx$ the list $c$ followed by $x$. Suppose the state $s \le n$ is the length
of the longest prefix of $p$ that is a suffix of $c$: $p_{\lt s}$ is a suffix of $c$, and every
$k \le n$ such that $p_{\lt k}$ is a suffix of $c$ satisfies $k \le s$. Then the state $s'$ that
the transition of the KMP prefix table of $p$ produces from $s$ on reading $x$ is the length of
the longest prefix of $p$ that is a suffix of $cx$: $s' \le n$, $p_{\lt s'}$ is a suffix of $cx$,
and every $k \le n$ such that $p_{\lt k}$ is a suffix of $cx$ satisfies $k \le s'$.

Formalized by `Array.mkPrefixTable_step_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 979](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L979). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#mk-prefix-table-step-spec).

## KMP search on the empty pattern

For every text $t$, KMP search for the empty pattern in
$t$ returns offset $0$ at cost $0$, that is, without any symbol comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.kmpSearch_nil_pattern`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean, line 1004](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/KnuthMorrisPratt.lean#L1004). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html#kmp-search-nil-pattern).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knuth–Morris–Pratt algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/string-algorithms/knuth-morris-pratt-algorithm)
