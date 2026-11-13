---
declaration: section
origin: cited
lean: MetaMathlibExt.IsVanDerLaanWindow, MetaMathlibExt.IsVanDerLaan, MetaMathlibExt.isVanDerLaanWindow_ordered_iff, MetaMathlibExt.isVanDerLaanWindow_const_iff, MetaMathlibExt.isVanDerLaan_const_iff
statement: formalized
proof: formalized
---

# Van der Laan sequences

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html).

## Van der Laan windows

Four natural numbers $a, b, c, d$ form a Van der Laan window when
the largest of them equals the sum of the two smallest, that is, when
$\max(a, b, c, d) = \min(a + b, a + c, a + d, b + c, b + d, c + d)$.

The minimum of the six pair sums is the sum of the two smallest of the four values counted with
multiplicity, so repeated values are handled correctly.

Formalized by `MetaMathlibExt.IsVanDerLaanWindow`, a definition declared in [MathlibExt/Combinatorics/VanDerLaanSequence.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VanDerLaanSequence.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html#is-van-der-laan-window).

## Van der Laan sequences

A sequence $s \colon \mathbb{N} \to \mathbb{N}$ is a Van der Laan
sequence when, for every $n \in \mathbb{N}$, the four consecutive terms
$s(n), s(n + 1), s(n + 2), s(n + 3)$ form a Van der Laan window, that is, the largest of them
equals the sum of the two smallest.

Formalized by `MetaMathlibExt.IsVanDerLaan`, a definition declared in [MathlibExt/Combinatorics/VanDerLaanSequence.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VanDerLaanSequence.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html#is-van-der-laan).

## Van der Laan windows in increasing order

Let $a \le b \le c \le d$ be natural numbers.
Then $a, b, c, d$ form a Van der Laan window if and only if $d = a + b$.

Formalized by `MetaMathlibExt.isVanDerLaanWindow_ordered_iff`, a theorem declared in [MathlibExt/Combinatorics/VanDerLaanSequence.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VanDerLaanSequence.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html#is-van-der-laan-window-ordered-iff).

## Constant Van der Laan windows

For a natural number $k$, the window $k, k, k, k$ is a
Van der Laan window if and only if $k = 0$.

Its largest value is $k$ and the sum of its two smallest values is $k + k$.

Formalized by `MetaMathlibExt.isVanDerLaanWindow_const_iff`, a theorem declared in [MathlibExt/Combinatorics/VanDerLaanSequence.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VanDerLaanSequence.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html#is-van-der-laan-window-const-iff).

## Constant Van der Laan sequences

For a natural number $k$, the constant sequence
$s \colon \mathbb{N} \to \mathbb{N}$ with $s(n) = k$ for all $n$ is a Van der Laan sequence if and
only if $k = 0$.

In particular the identically zero sequence, one of the alternatives in the source conjecture,
is a Van der Laan sequence.

Formalized by `MetaMathlibExt.isVanDerLaan_const_iff`, a theorem declared in [MathlibExt/Combinatorics/VanDerLaanSequence.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VanDerLaanSequence.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html#is-van-der-laan-const-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Van der Laan sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/van-der-laan-sequences)
