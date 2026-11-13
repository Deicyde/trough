---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.rabinKarpMatches, Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_ret_eq_naiveMatches, Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_time_eq, Cslib.Algorithms.Lean.TimeM.mem_rabinKarpMatches_iff, Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_pairwise, Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_nil_pattern, Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_time_le, Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_of_length_lt
statement: formalized
proof: formalized
---

# Rabin–Karp algorithm

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html).

## Rabin–Karp string matching

Given a base $d$, a modulus $q > 0$, a pattern
$P = p_0 \dots p_{m-1}$ and a text $T = t_0 \dots t_{n-1}$, both lists of natural numbers, this
returns the list, in increasing order, of all shifts $s$ with $s + m \le n$ and $t_{s+k} = p_k$
for every $k < m$. For $m \ge 1$ it computes by Horner's rule the residues modulo $q$ of $P$ and
of the first length-$m$ window of $T$, read as base-$d$ numerals, and updates the window residue
by a rolling hash; symbols are compared at a shift only when the two residues agree, from left to
right. If $m > n$ it returns the empty list. The empty pattern returns every shift
$0, 1, \dots, n$ at cost $0$.

The cost counts each executed multiplication, addition, subtraction and modulus in computing
the residues and $d^{m-1} \bmod q$, and each borrow test, residue equality test and symbol
equality test; shift-offset arithmetic and all other operations are free.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches).

## Rabin–Karp and naive matching return the same offsets

For every base $d$, modulus
$q > 0$ and lists of natural numbers $P$ and $T$, the list of offsets returned by Rabin–Karp
matching of $P$ in $T$ with base $d$ and modulus $q$ equals the list returned by naive matching
of $P$ in $T$.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_ret_eq_naiveMatches`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-ret-eq-naive-matches).

## Exact cost of Rabin–Karp matching

Let $d$ be a base, $q > 0$ a modulus and $P$, $T$
lists of natural numbers with $0 < m \le |T|$, where $m = |P|$, and put $r = |T| - m$. Index
lists from $0$, write $T_{s..}$ for the suffix of $T$ starting at position $s$, and for a list
$S$ with at least $m$ entries put $h(S) = \bigl(\sum_{i\lt m} S_i\, d^{m-1-i}\bigr) \bmod q$. Let
$B$ be the number of offsets $s < r$ with $h(T_{s..}) < (T_s \cdot (d^{m-1} \bmod q)) \bmod q$.
For $s \le r$ let $c_s = m$ if $P$ is a prefix of $T_{s..}$, and otherwise $c_s = j + 1$ for the
least $j$ with $P_j \ne T_{s+j}$. Then Rabin–Karp matching of $P$ in $T$ with base $d$ and
modulus $q$ has counted cost exactly

$$(8m - 1) + (r + 1) + 7r + B + \sum_{s \le r,\ h(P) = h(T_{s..})} c_s.$$

The terms count the setup, one hash comparison per alignment, the rolling hash updates, one
extra addition per borrow, and the symbol comparisons that verify hash hits.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_time_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-time-eq).

## Correctness of Rabin–Karp matching

For every base $d$, every modulus $q > 0$, all
lists of natural numbers $P$ (the pattern) and $T$ (the text) and every natural number $s$,
Rabin–Karp matching of $P$ in $T$ with base $d$ and modulus $q$ reports the offset $s$ if and
only if $P$ matches $T$ at $s$, that is, $s \le |T|$ and $P$ is a prefix of the suffix of $T$
that starts at position $s$ (counting from $0$).

Formalized by `Cslib.Algorithms.Lean.TimeM.mem_rabinKarpMatches_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#mem-rabin-karp-matches-iff).

## Rabin–Karp reports offsets in increasing order

For every base $d$, modulus $q > 0$ and
lists of natural numbers $P$ and $T$, the offsets returned by Rabin–Karp matching of $P$ in $T$
form a strictly increasing list; in particular no offset is reported twice.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_pairwise`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-pairwise).

## Rabin–Karp matching with the empty pattern

For every base $d$, modulus $q > 0$ and
list of natural numbers $T$, Rabin–Karp matching of the empty pattern in $T$ returns the list
$[0, 1, \dots, |T|]$ of all offsets from $0$ to $|T|$ in increasing order, at counted cost $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_nil_pattern`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-nil-pattern).

## Cost bound for Rabin–Karp matching

Let $d$ be a base, $q > 0$ a modulus and $P$, $T$
lists of natural numbers with $0 < m \le |T|$, where $m = |P|$, and put $r = |T| - m$. Index
lists from $0$, write $T_{s..}$ for the suffix of $T$ starting at position $s$, and for a list
$S$ with at least $m$ entries put $h(S) = \bigl(\sum_{i\lt m} S_i\, d^{m-1-i}\bigr) \bmod q$. Let
$H$ be the number of hash hits, the offsets $s \le r$ with $h(P) = h(T_{s..})$. Then
Rabin–Karp matching of $P$ in $T$ with base $d$ and modulus $q$ has counted cost at most
$(8m - 1) + (9(r + 1) - 8) + mH$.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-time-le).

## Rabin–Karp matching with a pattern longer than the text

For every base $d$, modulus
$q > 0$ and lists of natural numbers $P$ and $T$ with $|T| < |P|$, Rabin–Karp matching of $P$ in
$T$ returns no offsets, at counted cost exactly $1 + 2(|P| - 1) + 6|T|$.

This cost is the work of computing the high-place power and the Horner setup steps attempted
before the text runs out.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_of_length_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-of-length-lt).

## Exact cost of Rabin–Karp matching on repeated-symbol words

Let $d$ be a base, $q > 0$ a
modulus, $a$ a natural number and $m$, $n$ natural numbers with $0 < m \le n$. Put
$t = \bigl(a \sum_{i\lt m} d^i\bigr) \bmod q$, and let $\beta = 1$ if
$t < (a \cdot (d^{m-1} \bmod q)) \bmod q$ and $\beta = 0$ otherwise. Then Rabin–Karp matching
with base $d$ and modulus $q$ of the pattern $a^m$ in the text $a^n$ (the lists of $m$ and of
$n$ copies of $a$) has counted cost exactly

$$(8m - 1) + (n - m + 1) + 7(n - m) + (n - m)\beta + m(n - m + 1).$$

The last term is $m$ symbol comparisons at each of the $n - m + 1$ alignments.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_time_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-time-replicate).

## Rabin–Karp offsets on repeated-symbol words

For every base $d$, modulus $q > 0$, symbol
$a \in \mathbb{N}$ and natural numbers $m \le n$, Rabin–Karp matching of the pattern $a^m$ in the
text $a^n$ (the lists of $m$ and of $n$ copies of $a$) returns $[0, 1, \dots, n - m]$, that is,
every shift in increasing order, including overlapping ones.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_ret_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-ret-replicate).

## Matching cost of Rabin–Karp on repeated-symbol words

Let $d$ be a base, $q > 0$ a
modulus, $a$ a natural number and $m$, $n$ natural numbers with $0 < m \le n$. Let $C$ be the
counted cost of Rabin–Karp matching with base $d$ and modulus $q$ of the pattern $a^m$ in the
text $a^n$ (the lists of $m$ and of $n$ copies of $a$), minus $8m - 1$, with subtraction
truncated at $0$. Then $m(n - m + 1) \le C \le 10\,m(n - m + 1)$.

The subtracted $8m - 1$ is the preprocessing cost, so the bounds do not depend on it.

Formalized by `Cslib.Algorithms.Lean.TimeM.rabinKarpMatches_matching_time_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/RabinKarp.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html#rabin-karp-matches-matching-time-replica).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rabin–Karp algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/string-algorithms/rabin-karp-algorithm)
