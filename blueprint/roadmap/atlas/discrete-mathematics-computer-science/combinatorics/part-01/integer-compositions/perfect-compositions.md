---
declaration: section
origin: cited
lean: MetaMathlibExt.perfect_composition_iff_symbolic_parts_perm_perfect_partition_general, MetaMathlibExt.perfect_composition_iff_symbolic_parts_perm_perfect_partition
statement: formalized
proof: formalized
---

# Perfect compositions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/perfect-compositions/index.html).

## Perfect compositions are permuted perfect partitions

Call a list $L$ of positive integers
perfect for $n$ if for every integer $m$ with $0 < m < n$ there is exactly one list of integers
that is a sublist of $L$ (its entries taken in order, not necessarily contiguous) and has sum
$m$. A symbolic part $(a, u)$ with $a, u > 0$ stands for a run of $u$ copies of $a$, and the
expansion of a list of symbolic parts is the concatenation of their runs. Let $n$ be a natural
number and let $C$ be a list of symbolic parts, any two adjacent ones having different values
$a$, whose expansion has sum $n$. Then the expansion of $C$ is perfect for $n$ if and only if
$C$ is a permutation of a list $P$ of symbolic parts $(a, u)$ with $a, u > 0$ and strictly
increasing values $a$ whose expansion has sum $n$ and is perfect for $n$.

Formalized by `MetaMathlibExt.perfect_composition_iff_symbolic_parts_perm_perfect_partition_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PerfectCompositions.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PerfectCompositions.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/perfect-compositions/index.html#perfect-composition-iff-symbolic-parts-p).

## Munagi's theorem on perfect compositions

Call a list $L$ of positive integers perfect for
$n$ if for every integer $m$ with $0 < m < n$ there is exactly one list of integers that is a
sublist of $L$ (its entries taken in order, not necessarily contiguous) and has sum $m$. A
symbolic part $(a, u)$ with $a, u > 0$ stands for a run of $u$ copies of $a$, and the expansion
of a list of symbolic parts is the concatenation of their runs. Let $n > 0$ and let $C$ be a list
of symbolic parts, any two adjacent ones having different values $a$, whose expansion has sum
$n$. Then the expansion of $C$ is perfect for $n$ if and only if $C$ is a permutation of a list
$P$ of symbolic parts $(a, u)$ with $a, u > 0$ and strictly increasing values $a$ whose
expansion has sum $n$ and is perfect for $n$.

## Sources

- Augustine O. Munagi, "Perfect Compositions of Numbers," Journal of Integer Sequences 23 (2020), Article 20.5.1, Theorem 1, lines 138–140, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Munagi/munagi13.tex>.

Formalized by `MetaMathlibExt.perfect_composition_iff_symbolic_parts_perm_perfect_partition`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/PerfectCompositions.lean, line 696](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/PerfectCompositions.lean#L696). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/perfect-compositions/index.html#perfect-composition-iff-symbolic-parts-p-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Perfect compositions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-compositions/perfect-compositions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-compositions/perfect-compositions)
