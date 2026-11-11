---
declaration: section
origin: cited
lean: MetaMathlibExt.cloitreComplementFirst, MetaMathlibExt.cloitreMirror, MetaMathlibExt.cloitreApprox, MetaMathlibExt.cloitreSequence, MetaMathlibExt.IsRunBoundary, MetaMathlibExt.cloitreRunSum, MetaMathlibExt.IsCloitreSelfDescribing
statement: formalized
proof: formalized
---

# Cloitre's self-describing sequence

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html).

## First-letter complement of a word

For a finite list of natural numbers, a leading letter
$2$ is replaced by the two letters $1, 1$, and two leading letters $1, 1$ are replaced by the single
letter $2$; the empty list and every list beginning otherwise (with a letter other than $1$ or $2$,
or with a $1$ not followed by another $1$) are left unchanged.

Every word this is applied to in Cloitre's construction begins with $1, 1$ or with $2$, so the
last case does not arise there.

Formalized by `MetaMathlibExt.cloitreComplementFirst`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#cloitre-complement-first).

## Mirror image with first-letter complement

For a finite list $A$ of natural numbers, the
mirror image $A^r$ is obtained by reversing $A$ and then complementing the first letter: a leading
$2$ of the reversed list becomes $1, 1$, two leading letters $1, 1$ become $2$, and any other list
is left unchanged. For example $(1, 1, 2)^r = (1, 1, 1, 1)$ and
$(1, 1, 2, 1, 1, 1, 1)^r = (2, 1, 1, 2, 1, 1)$.

Formalized by `MetaMathlibExt.cloitreMirror`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#cloitre-mirror).

## Approximants of Cloitre's sequence

The finite words $A_k$ of natural numbers are defined
by $A_0 = (1, 1)$ and $A_{k+1} = A_k A_k^r$, the concatenation of $A_k$ with its mirror image
$A_k^r$: reverse $A_k$, then replace a leading $2$ by $1, 1$, or two leading letters $1, 1$ by
$2$, and otherwise leave it unchanged.

For example $A_1 = (1, 1, 2)$, $A_2 = (1, 1, 2, 1, 1, 1, 1)$ and
$A_3 = (1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1)$, and $A_4$ continues with $2, 2$.

Formalized by `MetaMathlibExt.cloitreApprox`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#cloitre-approx).

## Cloitre's sequence

Let $A_0 = (1, 1)$ and $A_{k+1} = A_k A_k^r$ be the approximants of
Cloitre's sequence, where $A_k^r$ is the mirror image of $A_k$: reverse $A_k$, then replace a
leading $2$ by $1, 1$, or two leading letters $1, 1$ by $2$, and otherwise leave it unchanged.
Cloitre's sequence $s : \mathbb{N} \to \mathbb{N}$ is defined by letting $s(n)$ be the letter at
position $n$ (counting from $0$) of $A_{n+2}$, or $0$ if $A_{n+2}$ has at most $n$ letters.

Each approximant is a prefix of the next and $A_{n+2}$ has more than $n$ letters, so $s$ is the
limit of the approximants. It begins $1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 2, \ldots$

Formalized by `MetaMathlibExt.cloitreSequence`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#cloitre-sequence).

## Run boundaries of a sequence

For sequences $s, b : \mathbb{N} \to \mathbb{N}$, $b$ marks
the maximal runs of $s$ when $b(0) = 0$, $b$ is strictly increasing, $s$ is constant on each
block $[b(n), b(n+1))$, and for every $n$ each value of $s$ on the block $[b(n), b(n+1))$ differs
from each value of $s$ on the next block $[b(n+1), b(n+2))$.

Because $b$ is strictly increasing with $b(0) = 0$, the blocks partition $\mathbb{N}$.

Formalized by `MetaMathlibExt.IsRunBoundary`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#is-run-boundary).

## Sum of a sequence over a run

For sequences $s, b : \mathbb{N} \to \mathbb{N}$ and
$n \in \mathbb{N}$, the $n$-th run sum is $\sum_{b(n) \le j < b(n+1)} s(j)$, the sum of $s$ over
the block $[b(n), b(n+1))$; it is $0$ when $b(n+1) \le b(n)$.

Formalized by `MetaMathlibExt.cloitreRunSum`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#cloitre-run-sum).

## Cloitre's self-describing property

A sequence $s : \mathbb{N} \to \mathbb{N}$ is
self-describing in Cloitre's sense when there is a sequence $b : \mathbb{N} \to \mathbb{N}$ with
$b(0) = 0$, $b$ strictly increasing, $s$ constant on each block $[b(n), b(n+1))$ and each value of
$s$ on a block different from each value on the next block (so the blocks are the maximal runs of
$s$), such that for every $n$, $2 s(n) = \sum_{b(n) \le j < b(n+1)} s(j)$.

In words, for every $n$ the $n$-th term $s(n)$ is half the sum of the $n$-th run; the condition is
stated with $2 s(n)$ to avoid truncated division in $\mathbb{N}$. For example, run sums
$2, 2, 4, 2, 2, 2, 2, 4, \ldots$ correspond to the terms $1, 1, 2, 1, 1, 1, 1, 2, \ldots$

Formalized by `MetaMathlibExt.IsCloitreSelfDescribing`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/CloitreSequence.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html#is-cloitre-self-describing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cloitre's self-describing sequence](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/cloitre-s-self-describing-sequence)
