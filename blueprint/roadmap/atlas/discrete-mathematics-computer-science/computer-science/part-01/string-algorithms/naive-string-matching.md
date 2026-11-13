---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.naiveMatches, Cslib.Algorithms.Lean.TimeM.naiveMatches_ret, Cslib.Algorithms.Lean.TimeM.mem_naiveMatches_iff, Cslib.Algorithms.Lean.TimeM.naiveMatches_pairwise, Cslib.Algorithms.Lean.TimeM.naiveMatches_time_eq, Cslib.Algorithms.Lean.TimeM.naiveMatches_time_le, Cslib.Algorithms.Lean.TimeM.naiveMatches_ret_replicate, Cslib.Algorithms.Lean.TimeM.naiveMatches_time_replicate
statement: formalized
proof: formalized
---

# Naive string matching

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html).

## Naive string matcher

Let $p = p_0 \cdots p_{m-1}$ be a pattern and
$t = t_0 \cdots t_{n-1}$ a text over an alphabet with a Boolean equality test. If $m \le n$, the
naive matcher handles the shifts $s = 0, 1, \dots, n - m$ in turn: it compares $p_i$ with
$t_{s+i}$ for $i = 0, 1, \dots$ until a comparison fails or all $m$ symbols are compared, and it
reports $s$ if no comparison failed. It returns the reported shifts in the order found, with cost
the total number of symbol comparisons executed, failed comparisons included. If $m > n$, it
reports no shift at cost $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches).

## Output of naive matching

Let $p$ be a pattern of length $m$ and $t$ a text of length
$n$. If $m \le n$, the list of shifts reported by the naive matcher on $p$ and $t$ is the
increasing list of all $s \in \{0, \dots, n - m\}$ such that $p$ is a prefix of the suffix of
$t$ starting at the zero-based position $s$, with symbols compared by the Boolean equality of the
alphabet. If $m > n$, the list is empty.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-ret).

## Correctness of naive string matching

Let $\alpha$ be a type whose Boolean equality
agrees with equality, and write $|t|$ for the length of a list $t$. For every pattern $p$ and
text $t$ over $\alpha$ and every natural number $s$, the naive matcher run on $p$ and $t$
reports the shift $s$ if and only if $p$ matches $t$ at $s$, that is, $s \le |t|$ and $p$ is a
prefix of the suffix of $t$ obtained by dropping its first $s$ symbols.

In particular, the empty pattern is reported at every shift $s \le |t|$.

Formalized by `Cslib.Algorithms.Lean.TimeM.mem_naiveMatches_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#mem-naive-matches-iff).

## Naive matching reports shifts in increasing order

For every pattern $p$ and text $t$,
the list of shifts reported by the naive matcher on $p$ and $t$ is strictly increasing; in
particular, no shift is reported twice.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-pairwise).

## Exact comparison count of naive matching

Let $p = p_0 \cdots p_{m-1}$ be a pattern and
$t = t_0 \cdots t_{n-1}$ a text. If $m \le n$, the number of symbol comparisons performed by the
naive matcher on $p$ and $t$ is

$$\sum_{s=0}^{n-m} \min(m, k_s + 1),$$

where $k_s$ is the least $i < m$ such that $p_i$ and $t_{s+i}$ are unequal under the Boolean
equality of the alphabet, and $k_s = m$ if there is no such $i$. If $m > n$, the naive matcher
performs no comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_time_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-time-eq).

## Upper bound on the comparisons of naive matching

For a pattern of length $m$ and a text
of length $n$, the naive matcher performs at most $(n - m + 1) \cdot m$ symbol comparisons if
$m \le n$, and no comparisons if $m > n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-time-le).

## Naive matching on a repeated symbol reports every shift

Let $\alpha$ be a type whose
Boolean equality is reflexive, let $x \in \alpha$, and let $m \le n$ be natural numbers. On the
pattern consisting of $m$ copies of $x$ and the text consisting of $n$ copies of $x$, the naive
matcher reports exactly the shifts $0, 1, \dots, n - m$ in increasing order, so all overlapping
occurrences are reported.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_ret_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-ret-replicate).

## Comparison count of naive matching on a repeated symbol

Let $\alpha$ be a type whose
Boolean equality is reflexive, let $x \in \alpha$, and let $m \le n$ be natural numbers. On the
pattern consisting of $m$ copies of $x$ and the text consisting of $n$ copies of $x$, the naive
matcher performs exactly $(n - m + 1) \cdot m$ symbol comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_time_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-time-replicate).

## Naive matching with the empty pattern

For every text $t$ of length $n$, the naive
matcher run on the empty pattern and $t$ reports exactly the shifts $0, 1, \dots, n$ in
increasing order and performs no symbol comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_nil_pattern`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-nil-pattern).

## Naive matching with a pattern longer than the text

If the pattern $p$ is longer than
the text $t$, then the naive matcher run on $p$ and $t$ reports no shifts and performs no symbol
comparisons.

Formalized by `Cslib.Algorithms.Lean.TimeM.naiveMatches_of_length_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Naive.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/Naive.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html#naive-matches-of-length-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Naive string matching](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/naive-string-matching/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/string-algorithms/naive-string-matching)
