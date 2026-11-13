---
declaration: section
origin: cited
lean: MetaMathlibExt.smarandacheBlock, MetaMathlibExt.smarandachePrefix, MetaMathlibExt.smarandachePermutation, MetaMathlibExt.smarandacheBlock_one, MetaMathlibExt.smarandacheBlock_two, MetaMathlibExt.smarandacheBlock_three, MetaMathlibExt.smarandacheBlock_four, MetaMathlibExt.smarandachePrefix_three
statement: formalized
proof: formalized
---

# Smarandache permutation sequence

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html).

## Blocks of the Smarandache permutation sequence

For a natural number $n$, the $n$-th block
is the list of the odd numbers $1, 3, \ldots, 2n - 1$ in increasing order followed by the even
numbers $2n, 2n - 2, \ldots, 2$ in decreasing order; the $0$-th block is empty.

Formalized by `MetaMathlibExt.smarandacheBlock`, a definition declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-block).

## Prefix of the Smarandache permutation sequence

For a natural number $N$, this is the
list of natural numbers obtained by concatenating, in order, the Smarandache blocks numbered
$1, 2, \dots, N$, where block $n$ is the list $(1, 3, \dots, 2n - 1, 2n, 2n - 2, \dots, 2)$ of the
odd numbers below $2n$ in increasing order followed by the even numbers from $2n$ down to $2$.
For $N = 0$ it is the empty list.

Formalized by `MetaMathlibExt.smarandachePrefix`, a definition declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-prefix).

## Smarandache permutation sequence

The Smarandache permutation sequence (OEIS A004741) is
the sequence $(a_i)_{i \ge 0}$ of natural numbers, indexed from $0$, obtained by concatenating
the blocks $(1, 3, \ldots, 2n - 1, 2n, 2n - 2, \ldots, 2)$ for $n = 1, 2, 3, \ldots$ in order; it
begins $1, 2, 1, 3, 4, 2, 1, 3, 5, 6, 4, 2, \ldots$, so $a_0 = 1$.

Formalized by `MetaMathlibExt.smarandachePermutation`, a definition declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-permutation).

## First block of the Smarandache permutation sequence

The first block of the Smarandache
permutation sequence is $(1, 2)$.

Formalized by `MetaMathlibExt.smarandacheBlock_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-block-one).

## Second block of the Smarandache permutation sequence

The second block of the Smarandache
permutation sequence is $(1, 3, 4, 2)$.

Formalized by `MetaMathlibExt.smarandacheBlock_two`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-block-two).

## Third block of the Smarandache permutation sequence

The third block of the Smarandache
permutation sequence is $(1, 3, 5, 6, 4, 2)$.

Formalized by `MetaMathlibExt.smarandacheBlock_three`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-block-three).

## Fourth block of the Smarandache permutation sequence

The fourth block of the Smarandache
permutation sequence is $(1, 3, 5, 7, 8, 6, 4, 2)$.

Formalized by `MetaMathlibExt.smarandacheBlock_four`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-block-four).

## Concatenation of the first three Smarandache blocks

Concatenating the first three blocks
of the Smarandache permutation sequence gives $(1, 2, 1, 3, 4, 2, 1, 3, 5, 6, 4, 2)$.

Formalized by `MetaMathlibExt.smarandachePrefix_three`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-prefix-three).

## Initial term of the Smarandache permutation sequence

Indexing the Smarandache permutation
sequence $(a_i)_{i \ge 0}$ from $0$, its initial term is $a_0 = 1$.

Formalized by `MetaMathlibExt.smarandachePermutation_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-permutation-zero).

## Sixth term of the Smarandache permutation sequence

Indexing the Smarandache permutation
sequence $(a_i)_{i \ge 0}$ from $0$, its sixth term is $a_5 = 2$.

Formalized by `MetaMathlibExt.smarandachePermutation_five`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-permutation-five).

## Twelfth term of the Smarandache permutation sequence

Indexing the Smarandache permutation
sequence $(a_i)_{i \ge 0}$ from $0$, its twelfth term is $a_{11} = 2$.

Formalized by `MetaMathlibExt.smarandachePermutation_eleven`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/SmarandachePermutationSequence.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html#smarandache-permutation-eleven).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smarandache permutation sequence](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/smarandache-permutation-sequence)
