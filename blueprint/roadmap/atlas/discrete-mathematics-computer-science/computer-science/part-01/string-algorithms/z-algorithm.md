---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.StringMatching.computeZ, Cslib.Algorithms.Lean.StringMatching.computeZ_zero, Cslib.Algorithms.Lean.StringMatching.computeZ_prefix_iff, Cslib.Algorithms.Lean.StringMatching.computeZ_getElem_le, Cslib.Algorithms.Lean.StringMatching.computeZ_time_le, Cslib.Algorithms.Lean.StringMatching.computeZ_time_ge, Cslib.Algorithms.Lean.StringMatching.computeZ_replicate, Cslib.Algorithms.Lean.StringMatching.computeZ_replicate_time
statement: formalized
proof: formalized
---

# Z algorithm

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html).

## Z-algorithm

Given a word $s = s_0 \dots s_{n-1}$ over a type $\alpha$ with a Boolean
equality test, Gusfield's Z-box algorithm returns an array $Z$ of $n$ natural numbers with
$Z_0 = n$. It visits $i = 1, \dots, n - 1$ in turn, keeping a box $[\ell, r)$, initially empty,
that is the rightmost match of a prefix of $s$ found so far. If $\ell \le i < r$ and
$Z_{i - \ell} < r - i$, it sets $Z_i = Z_{i - \ell}$. Otherwise it finds $Z_i$ by comparing
symbols directly, starting at offset $r - i$ if $i < r$ and at offset $0$ if not, and if
$Z_i > 0$ the box becomes $[i, i + Z_i)$. When the equality test is lawful, $Z_i$ is the length
of the longest common prefix of $s$ and its suffix $s_i \dots s_{n-1}$. The cost counts one unit
for each visited position $i \ge 1$ and one unit for each symbol comparison; on the empty word the
result is empty with cost $0$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z).

## The first Z-value is the word length

Let $\alpha$ be a type with a Boolean equality
test. For every nonempty word of length $n$ over $\alpha$, the Z-array $Z$ computed by the
Z-algorithm has $Z_0 = n$.

Gusfield leaves this entry undefined; this convention completes it.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-zero).

## Z-values are longest common prefix lengths

Let $\alpha$ be a type with a lawful Boolean
equality test, let $s = s_0 \dots s_{n-1}$ be a word over $\alpha$, and let $Z$ be the Z-array
computed by the Z-algorithm on $s$. For every position $i < n$ and every natural number $q$,
$q \le Z_i$ holds if and only if $q \le n - i$ and $s_k = s_{i+k}$ for all $k < q$. Hence $Z_i$ is
the length of the longest common prefix of $s$ and its suffix $s_i \dots s_{n-1}$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_prefix_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 440](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L440). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-prefix-iff).

## Z-values are at most the suffix length

Let $\alpha$ be a type with a Boolean equality
test, not necessarily lawful, and let $s$ be a word of length $n$ over $\alpha$. For every position
$i < n$, the entry at $i$ of the Z-array computed by the Z-algorithm on $s$ is at most $n - i$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_getElem_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-get-elem-le).

## Linear upper bound for the Z-algorithm

Let $\alpha$ be a type with a Boolean equality
test, not necessarily lawful. On every word of length $n$ over $\alpha$, the Z-algorithm has cost
at most $3(n - 1)$, read as $0$ when $n = 0$, where the cost counts one unit for each visited
position $i \ge 1$ and one unit for each symbol comparison.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-time-le).

## Linear lower bound for the Z-algorithm

Let $\alpha$ be a type with a Boolean equality
test, not necessarily lawful. On every word of length $n$ over $\alpha$, the Z-algorithm has cost
at least $n - 1$, where the cost counts one unit for each visited position $i \ge 1$ and one unit
for each symbol comparison.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_time_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 661](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L661). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-time-ge).

## Z-array of a repeated symbol

Let $\alpha$ be a type with a lawful Boolean equality
test, let $a \in \alpha$ and $n \in \mathbb{N}$. The Z-array computed by the Z-algorithm on the word
$a^n$ has entry $n - i$ at every position $i < n$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_replicate`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 680](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L680). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-replicate).

## Z-algorithm cost on a repeated symbol

Let $\alpha$ be a type with a lawful Boolean
equality test, let $a \in \alpha$ and $n \in \mathbb{N}$. The Z-algorithm run on the word $a^n$ has
cost exactly $2(n - 1)$, read as $0$ when $n = 0$, where the cost counts one unit for each visited
position $i \ge 1$ and one unit for each symbol comparison. Thus it makes $n - 1$ visits and
$n - 1$ comparisons.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_replicate_time`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 763](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L763). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-replicate-time).

## Z-algorithm cost on a repeated symbol followed by a distinct one

Let $\alpha$ be a type
with a lawful Boolean equality test and let $a \ne b$ be elements of $\alpha$. For every $n \ge 1$,
the Z-algorithm run on the word $a^n b$ has cost exactly $3n - 1$, where the cost counts one unit
for each visited position $i \ge 1$ and one unit for each symbol comparison. In terms of the
input length $N = n + 1$, this is $3N - 4$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.computeZ_replicate_push_time`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean, line 927](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/StringMatching/ZAlgorithm.lean#L927). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html#compute-z-replicate-push-time).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Z algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/z-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/string-algorithms/z-algorithm)
