---
declaration: section
origin: cited
lean: MetaMathlibExt.morphExtend, MetaMathlibExt.morphIterate, MetaMathlibExt.morphExtend_append, MetaMathlibExt.morphIterate_length_of_uniform, MetaMathlibExt.IsNonErasing, MetaMathlibExt.IsPrefixPreserving, MetaMathlibExt.IsOmegaLimit, MetaMathlibExt.IsPureMorphic
statement: formalized
proof: formalized
---

# Morphic words

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html).

## Extension of a letter map to finite words

Given a map $f$ sending each letter of an
alphabet $A$ to a finite word over $A$, its extension to finite words sends a word
$a_1 a_2 \cdots a_m$ over $A$ to the concatenation $f(a_1) f(a_2) \cdots f(a_m)$ of the images
of its letters in order; the empty word is sent to the empty word.

Formalized by `MetaMathlibExt.morphExtend`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#morph-extend).

## Iterates of a letter map

Let $f$ send each letter of an alphabet $A$ to a finite word
over $A$, extended to finite words by concatenation. The iterates of $f$ on finite words over
$A$ are defined by $f^0(w) = w$ and $f^{n+1}(w) = f(f^n(w))$ for every finite word $w$ over $A$
and every natural number $n$.

Formalized by `MetaMathlibExt.morphIterate`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#morph-iterate).

## Extended letter maps preserve concatenation

Let $f$ send each letter of an alphabet $A$
to a finite word over $A$, extended to finite words by concatenation. Then $f(uv) = f(u)f(v)$
for all finite words $u$ and $v$ over $A$.

Formalized by `MetaMathlibExt.morphExtend_append`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#morph-extend-append).

## Length of iterates of a uniform letter map

Let $k$ be a natural number and let $f$ send
each letter of an alphabet $A$ to a word of length exactly $k$ over $A$, extended to finite
words by concatenation, with iterates $f^n$ (where $f^0$ is the identity). Then for every
natural number $n$ and every finite word $w$ over $A$, the word $f^n(w)$ has length $k^n$ times
the length of $w$.

Formalized by `MetaMathlibExt.morphIterate_length_of_uniform`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#morph-iterate-length-of-uniform).

## Non-erasing letter maps

A map $f$ sending each letter of an alphabet $A$ to a finite
word over $A$ is non-erasing when the word $f(a)$ is nonempty for every letter $a \in A$.

Formalized by `MetaMathlibExt.IsNonErasing`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#is-non-erasing).

## Prolongable letter maps

Let $f$ send each letter of an alphabet $A$ to a finite word
over $A$, extended to finite words by concatenation, with iterates $f^n$ (where $f^0$ is the
identity). Then $f$ is prefix-preserving (prolongable) at a letter $a \in A$ when
$f(a) = a\alpha$ for some finite word $\alpha$ over $A$ such that the word $f^n(\alpha)$ is
nonempty for every natural number $n$, including $n = 0$.

Formalized by `MetaMathlibExt.IsPrefixPreserving`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#is-prefix-preserving).

## Infinite word as the limit of iterates

Let $f$ send each letter of an alphabet $A$ to a
finite word over $A$, extended to finite words by concatenation, with iterates $f^n$ (where $f^0$
is the identity), let $a \in A$, and let $w = w_0 w_1 w_2 \cdots$ be an infinite word over $A$.
Then $w$ is the limit of the iterates of $f$ at $a$ when the lengths of the words $f^n(a)$
(iterates applied to the one-letter word $a$) are unbounded as $n$ ranges over the natural
numbers, and for every $n$ and every position $i$ of $f^n(a)$, counted from $0$, the letter of
$f^n(a)$ at position $i$ is $w_i$.

Formalized by `MetaMathlibExt.IsOmegaLimit`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#is-omega-limit).

## Pure morphic words

An infinite word $w$ over a finite alphabet $A$ is pure morphic when
there are a map $f$ sending each letter of $A$ to a finite word over $A$ and a letter $a \in A$
such that $f$ is prolongable at $a$ and $w$ is the limit of the iterates of $f$ at $a$.

No coding is applied to the limit, and $f$ is not required to be non-erasing on every letter.

Formalized by `MetaMathlibExt.IsPureMorphic`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/PureMorphicWord.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#is-pure-morphic).

## Morphic words via a coding

Let $A$ be a finite alphabet, $B$ any alphabet, $u$ an
infinite word over $A$, $\tau : A \to B$ a map (a coding) and $w$ an infinite word over $B$.
Then $w$ is morphic with generator $u$ and coding $\tau$ if $u$ is a pure morphic word and
$w(n) = \tau(u(n))$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsMorphic`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#is-morphic).

## Building a morphic word from its generator

Let $A$ be a finite alphabet, $u$ a pure
morphic infinite word over $A$, $\tau : A \to B$ a map and $w$ an infinite word over $B$. If
$w(n) = \tau(u(n))$ for every $n \in \mathbb{N}$, then $w$ is morphic with generator $u$ and
coding $\tau$.

Formalized by `MetaMathlibExt.IsMorphic.intro`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#intro).

## The generator of a morphic word is pure morphic

Let $A$ be a finite alphabet, $u$ an
infinite word over $A$, $\tau : A \to B$ a map and $w$ an infinite word over $B$. If $w$ is
morphic with generator $u$ and coding $\tau$, then $u$ is a pure morphic word.

Formalized by `MetaMathlibExt.IsMorphic.pure`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#pure).

## A morphic word is the coding of its generator

Let $A$ be a finite alphabet, $u$ an
infinite word over $A$, $\tau : A \to B$ a map and $w$ an infinite word over $B$. If $w$ is
morphic with generator $u$ and coding $\tau$, then $w(n) = \tau(u(n))$ for every
$n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.IsMorphic.coding_eq`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#coding-eq).

## Pure morphic words are morphic

Let $A$ be a finite alphabet and $u$ a pure morphic
infinite word over $A$. Then $u$ is morphic with generator $u$ and the identity coding of $A$.

Formalized by `MetaMathlibExt.IsMorphic.ofPureMorphic`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/InfiniteWord/MorphicWord.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html#of-pure-morphic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Morphic words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/morphic-words)
