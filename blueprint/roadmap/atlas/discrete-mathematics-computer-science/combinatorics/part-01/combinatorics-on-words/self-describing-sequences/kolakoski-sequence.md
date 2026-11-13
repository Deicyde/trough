---
declaration: section
origin: cited
lean: MetaMathlibExt.kolakoskiBlockStart, MetaMathlibExt.IsKolakoski
statement: formalized
proof: formalized
---

# Kolakoski sequence

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/kolakoski-sequence/index.html).

## Starting positions of Kolakoski blocks

For a sequence $K_1, K_2, K_3, \ldots$ of natural
numbers, the starting positions $s_n$ of its blocks are defined by $s_1 = 1$ and
$s_{n+1} = s_n + K_n$ for every $n \ge 1$, together with the convention $s_0 = 0$.

Block $n$ of a candidate Kolakoski sequence $K$ consists of the positions $i$ with
$s_n \le i < s_n + K_n$; index $0$ lies outside the one-indexed sequence.

Formalized by `MetaMathlibExt.kolakoskiBlockStart`, a definition declared in [MathlibExt/Combinatorics/Words/KolakoskiSequence.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/KolakoskiSequence.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/kolakoski-sequence/index.html#kolakoski-block-start).

## Kolakoski sequences

A sequence $K_1, K_2, K_3, \ldots$ of natural numbers is a Kolakoski
sequence when $K_1 = 1$, every $K_n$ with $n \ge 1$ is $1$ or $2$, and $K$ describes its own runs
in the following sense. Let $s_1 = 1$ and $s_{n+1} = s_n + K_n$ for $n \ge 1$, and call block $n$
the set of positions $i$ with $s_n \le i < s_n + K_n$. For every $n \ge 1$, every term $K_i$ with
$i$ in block $n$ equals $1$ if $n$ is odd and $2$ if $n$ is even.

The sequence is indexed from $1$; its value at index $0$ is unconstrained.

Formalized by `MetaMathlibExt.IsKolakoski`, a definition declared in [MathlibExt/Combinatorics/Words/KolakoskiSequence.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/KolakoskiSequence.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/kolakoski-sequence/index.html#is-kolakoski).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolakoski sequence](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/kolakoski-sequence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/kolakoski-sequence)
