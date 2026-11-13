---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess, Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_time_le, Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_badCharacter, Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_goodSuffix, Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_fullMatch, Cslib.Algorithms.Lean.TimeM.boyerMooreMatches, Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_nil_pattern, Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_of_length_lt
statement: formalized
proof: formalized
---

# Boyer–Moore string-search algorithm

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html).

## Boyer–Moore preprocessing

Given a pattern $p = p_0 \cdots p_{m-1}$ over the alphabet
$\{0, \dots, \sigma - 1\}$, this computes a bad-character table $B$ of length $\sigma$ and a
strong good-suffix table $G$ of length $m$. The table $B$ starts with every entry equal to $m$,
and then for $k = 0, 1, \dots, m - 2$ in turn the entry $B_{p_k}$ is set to $m - 1 - k$. For
$G$, let $s_i$ be the length of the longest common suffix of $p_0 \cdots p_i$ and $p$, computed
with the Z algorithm on the reversed pattern. The table $G$ starts with every entry equal to
$m$; then for $i = m - 1, \dots, 0$ in turn, if $s_i = i + 1$, every entry $G_j$ with
$j < m - 1 - i$ that still equals $m$ is set to $m - 1 - i$; finally, for
$i = 0, 1, \dots, m - 2$ in turn, the entry $G_{m - 1 - s_i}$ is set to $m - 1 - i$.

The event cost includes table slots, copies, fill iterations and canonical Z events;
it does not count machine instructions or unbounded-integer bit operations.

Formalized by `Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#preprocess).

## Cost of Boyer–Moore preprocessing

For a pattern of length $m$ over an alphabet of size
$\sigma$, the event cost of the Boyer–Moore preprocessing is at most $\sigma$ when $m = 0$ and at
most $\sigma + 10m - 6$ when $m \ge 1$.

The cost counts the selected events of the preprocessor, including initialization of the
alphabet table; it is not a word-RAM or bit-cost bound.

Formalized by `Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#preprocess-time-le).

## Bad-character table of Boyer–Moore preprocessing

Let $p = p_0 \cdots p_{m-1}$ be a
pattern over the alphabet $\{0, \dots, \sigma - 1\}$ and let $B$ be the bad-character table
computed by the Boyer–Moore preprocessing of $p$. For every symbol $c$, either $B_c = m$ and
$p_k \ne c$ for every $k$ with $k + 1 < m$, or there is $j$ with $j + 1 < m$ and $p_j = c$ such
that $B_c = m - 1 - j$ and every $k$ with $k + 1 < m$ and $p_k = c$ satisfies $k \le j$.

Thus $B_c$ is the distance from the last position of $p$ to the rightmost occurrence of $c$
before that position, or $m$ if $c$ does not occur there.

Formalized by `Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_badCharacter`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#preprocess-bad-character).

## Good-suffix table of Boyer–Moore preprocessing

Let $p = p_0 \cdots p_{m-1}$ be a
pattern over the alphabet $\{0, \dots, \sigma - 1\}$, let $G$ be the good-suffix table computed
by the Boyer–Moore preprocessing of $p$, and let $i < m$. Call a positive integer $e$ an
admissible shift at $i$ if $p_{t - e} = p_t$ for every $t < m$ with $i < t$ and $e \le t$, and
$p_{i - e} \ne p_i$ whenever $e \le i$. Then $1 \le G_i \le m$ and $G_i$ is the least
admissible shift at $i$.

After a mismatch at position $i$, shifting by $G_i$ keeps the matched suffix
$p_{i+1} \cdots p_{m-1}$ aligned where it overlaps and, when $G_i \le i$, places the symbol
$p_{i - G_i} \ne p_i$ under the mismatched position.

Formalized by `Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_goodSuffix`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean, line 693](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean#L693). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#preprocess-good-suffix).

## The full-match shift is the least period of the pattern

Let $p = p_0 \cdots p_{m-1}$
be a nonempty pattern over the alphabet $\{0, \dots, \sigma - 1\}$ and let $G$ be the good-suffix
table computed by the Boyer–Moore preprocessing of $p$. Then $1 \le G_0 \le m$,
$p_{t - G_0} = p_t$ for every $t < m$ with $G_0 \le t$, and $G_0 \le e$ for every positive
integer $e$ such that $p_{t - e} = p_t$ for every $t < m$ with $e \le t$. That is, $G_0$ is the
least positive period of $p$.

So after a full match the matcher may shift by $G_0$ without discarding overlapping
occurrences.

Formalized by `Cslib.Algorithms.Lean.StringMatching.BoyerMoore.preprocess_fullMatch`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Preprocessing.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#preprocess-full-match).

## Boyer–Moore matcher for all occurrences

Let $p = p_0 \cdots p_{m-1}$ and
$t = t_0 \cdots t_{n-1}$ be words over the alphabet $\{0, \dots, \sigma - 1\}$. The matcher
returns a list of offsets together with a cost. If $m = 0$ it returns $0, 1, \dots, n$ at cost
$n + 1$, and if $n < m$ it returns the empty list at cost $0$. Otherwise it charges $m + n$ for
converting $p$ and $t$ to arrays, computes the bad-character table $B$ and the strong
good-suffix table $G$ of $p$ with the Boyer–Moore preprocessing and charges the cost of that
preprocessing, and then visits alignments $s$, starting from $s = 0$, as long as
$s + m \le n$. At each alignment it charges $1$ and compares $p_r$ with $t_{s + r}$ for
$r = m - 1, m - 2, \dots, 0$, charging $1$ per comparison and stopping at the first mismatch.
If all $m$ letters agree, it records $s$, charges $2$ and moves to the alignment $s + G_0$. If
the first mismatch is at position $i$, it charges $1$ and moves to the alignment
$s + \max(G_i, B_c - m + 1 + i)$, where $c = t_{s + i}$ and the maximum is taken in the
integers. Finally it charges $1$ for each recorded offset and returns the recorded offsets in
the order they were found.

The result is every occurrence of $p$ in $t$, in increasing order and including overlaps. The
cost counts these selected events, not machine instructions.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches).

## Boyer–Moore with the empty pattern

For every text $t$ of length $n$ over the alphabet
$\{0, \dots, \sigma - 1\}$, the Boyer–Moore matcher with the empty pattern and text $t$ returns
the list $0, 1, \dots, n$ of all offsets from $0$ to $n$ in increasing order, at cost $n + 1$.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_nil_pattern`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-nil-pattern).

## Boyer–Moore with a pattern longer than the text

Let $p$ and $t$ be words over the
alphabet $\{0, \dots, \sigma - 1\}$. If $t$ is strictly shorter than $p$, then the Boyer–Moore
matcher with pattern $p$ and text $t$ returns the empty list at cost $0$: no preprocessing or
search events are charged.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_of_length_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-of-length-lt).

## Boyer–Moore returns exactly the occurrences

For all words $p$ and $t$ over the alphabet
$\{0, \dots, \sigma - 1\}$ and every natural number $k$, the offset $k$ belongs to the list
returned by the Boyer–Moore matcher with pattern $p$ and text $t$ if and only if $p$ occurs in
$t$ at offset $k$, that is, $k \le |t|$ and $p$ is a prefix of the word obtained from $t$ by
deleting its first $k$ letters. In particular, overlapping occurrences are all returned.

Formalized by `Cslib.Algorithms.Lean.TimeM.mem_boyerMooreMatches_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#mem-boyer-moore-matches-iff).

## Boyer–Moore returns offsets in strictly increasing order

For all words $p$ and $t$ over
the alphabet $\{0, \dots, \sigma - 1\}$, the list of offsets returned by the Boyer–Moore matcher
with pattern $p$ and text $t$ is strictly increasing: each entry is smaller than every entry
after it.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-pairwise).

## Boyer–Moore agrees with the naive matcher

For all words $p$ and $t$ over the alphabet
$\{0, \dots, \sigma - 1\}$, the list of offsets returned by the Boyer–Moore matcher with pattern
$p$ and text $t$ equals the list returned by the naive matcher with pattern $p$ and text $t$,
entry by entry and in the same order. Only the returned lists are compared, not the costs.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_eq_naiveMatches`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-eq-naive-matches).

## Worst-case cost of Boyer–Moore matching

Let $p$ and $t$ be words over the alphabet
$\{0, \dots, \sigma - 1\}$ of lengths $m$ and $n$. The cost of the Boyer–Moore matcher with
pattern $p$ and text $t$ is at most $n + 1$ if $m = 0$, at most $0$ if $n < m$, and at most
$\sigma + n + 11m - 6 + (m + 4)(n - m + 1)$ if $1 \le m \le n$.

The cost counts the matcher's selected events, not machine instructions. The bound is quadratic
and does not assert linear all-match comparison complexity or machine runtime.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean, line 542](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Basic.lean#L542). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-time-le).

## Exact Boyer–Moore cost when pattern and text repeat the same letter

Let $x$ be a letter
of the alphabet $\{0, \dots, \sigma - 1\}$, let $m$ and $n$ be natural numbers with
$0 < m \le n$, and write $x^k$ for the word of $k$ copies of $x$. The cost of the Boyer–Moore
matcher with pattern $x^m$ and text $x^n$ equals $m + n + P + (m + 4)(n - m + 1)$, where $P$ is
the cost of the Boyer–Moore preprocessing of the pattern $x^m$.

Of this cost, $m(n - m + 1)$ counts character tests: every alignment is a match and compares all
$m$ pattern letters.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_time_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Complexity.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Complexity.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-time-replicate).

## Exact Boyer–Moore cost when the pattern repeats one letter and ends in another, which alone makes up the text

**Exact Boyer–Moore cost when the pattern repeats one letter and ends in another, which alone
makes up the text.** Let $a \ne b$ be letters of the alphabet $\{0, \dots, \sigma - 1\}$ and let
$m$ and $n$ be natural numbers with $2 \le m \le n$. Write $a^{m-1}b$ for the word of $m - 1$
copies of $a$ followed by one $b$, and $b^n$ for the word of $n$ copies of $b$. The cost of the
Boyer–Moore matcher with pattern $a^{m-1}b$ and text $b^n$ equals
$m + n + P + 4\lfloor n/m \rfloor$, where $P$ is the cost of the Boyer–Moore preprocessing of
the pattern $a^{m-1}b$.

On these inputs every alignment makes two character tests and is followed by a shift by $m$.

Formalized by `Cslib.Algorithms.Lean.TimeM.boyerMooreMatches_time_replicate_append`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Complexity.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/BoyerMoore/Complexity.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html#boyer-moore-matches-time-replicate-appen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Boyer–Moore string-search algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/string-algorithms/boyer-moore-string-search-algorithm)
