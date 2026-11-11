---
declaration: section
origin: cited
lean: MetaMathlibExt.baseWordValueLSD, MetaMathlibExt.IsKAutomaticSequence, MetaMathlibExt.IsCodingOfProlongableKUniformFixedPoint, MetaMathlibExt.cobham_automatic_iff_uniform_morphic, MetaMathlibExt.isCodingOfProlongableKUniformFixedPoint_iff, MetaMathlibExt.IsCodingOfProlongableKUniformFixedPoint.exists_isMorphic, MetaMathlibExt.IsKAutomaticSequence.exists_isMorphic, MetaMathlibExt.kKernel
statement: formalized
proof: formalized
---

# Automatic sequences

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html).

## Value of a base-$k$ digit word, least significant digit first

For a natural number $k$,
the value of a finite word $d_0 d_1 \cdots d_{m-1}$ of digits $d_i \in \{0, 1, \dots, k-1\}$ is
the natural number $\sum_{i < m} d_i k^i$, so the first digit is the least significant one; the
empty word has value $0$.

## Sources

- Sunic selects least-significant-digit reading with tolerance of trailing high-order zeros: lines 562-567 of `cubefree.tex`.

Formalized by `MetaMathlibExt.baseWordValueLSD`, a definition declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#base-word-value-lsd).

## Automatic sequences via finite automata

Let $k$ be a natural number and $B$ a finite
alphabet. A sequence $w : \mathbb{N} \to B$ is $k$-automatic when $k \ge 2$ and there is a
deterministic finite automaton with output, consisting of a nonempty finite set of states $Q$, an
initial state $s \in Q$, a transition map $\delta : Q \times \{0, 1, \dots, k-1\} \to Q$ and an
output map $\tau : Q \to B$, such that for every $n \in \mathbb{N}$ and every finite word
$d_0 d_1 \cdots d_{m-1}$ of digits in $\{0, 1, \dots, k-1\}$ with $\sum_{i < m} d_i k^i = n$, the
automaton started in $s$ and reading $d_0, d_1, \dots, d_{m-1}$ in this order (least significant
digit first) stops in a state $t$ with $\tau(t) = w(n)$.

## Sources

- Sunic Definition 3, lines 556-560 of `cubefree.tex`. The universal clause over all representing words enforces tolerance of trailing high-order zeros.

Formalized by `MetaMathlibExt.IsKAutomaticSequence`, a definition declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#is-kautomatic-sequence).

## Codings of prolongable uniform fixed points

Let $k$ be a natural number and $B$ a finite
alphabet. A sequence $w : \mathbb{N} \to B$ is a coding of a prolongable $k$-uniform fixed point
when $k \ge 2$ and there are a nonempty finite alphabet $A$, a map $f$ sending each letter of $A$
to a word of length exactly $k$ over $A$, a letter $a \in A$ with $f(a) = a\alpha$ for some
nonempty word $\alpha$ over $A$, a sequence $u : \mathbb{N} \to A$ and a map $g : A \to B$ such
that $u(0) = a$, the letter of $f(u(n))$ at position $j$ (counted from $0$) is $u(kn + j)$ for
all $n \in \mathbb{N}$ and $j < k$, and $w(n) = g(u(n))$ for all $n \in \mathbb{N}$.

The conditions on $u$ say that $u$ begins with $a$ and is fixed by $f$ applied letter by letter.

## Sources

- Sunic lines 569-584 state the equivalence and define prolongability and uniformity (`cubefree.tex`); Stipulanti lines 164-174 define morphism, coding, prolongability, and fixed point (`stip8.tex`).

Formalized by `MetaMathlibExt.IsCodingOfProlongableKUniformFixedPoint`, a definition declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#is-coding-of-prolongable-kuniform-fixed).

## Cobham's characterization of automatic sequences

Let $k \ge 2$ and let $B$ be a finite
alphabet. A sequence $w : \mathbb{N} \to B$ is $k$-automatic if and only if it is a coding of a
prolongable $k$-uniform fixed point.

## Sources

- Stipulanti lines 212-217 state the exact theorem (`stip8.tex`); its Cobham72 bibliography entry is line 1275.

Formalized by `MetaMathlibExt.cobham_automatic_iff_uniform_morphic`, a theorem declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#cobham-automatic-iff-uniform-morphic).

## Uniform fixed-point codings via iterates of a uniform map

Let $k \ge 2$ and let $B$
be a finite alphabet. A sequence $w : \mathbb{N} \to B$ is a coding of a prolongable $k$-uniform
fixed point if and only if there are a natural number $q$, a map $f$ sending each letter of the
alphabet $A = \{0, 1, \dots, q-1\}$ to a word of length exactly $k$ over $A$, a letter $a \in A$,
an infinite word $u$ over $A$ and a map $g : A \to B$ such that $f$ is prolongable at $a$, $u$ is
the limit of the iterates of $f$ at $a$, and $w(n) = g(u(n))$ for every $n \in \mathbb{N}$.

Formalized by `MetaMathlibExt.isCodingOfProlongableKUniformFixedPoint_iff`, a theorem declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#is-coding-of-prolongable-kuniform-fixed-2).

## Uniform fixed-point codings are morphic

Let $k$ be a natural number and $B$ a finite
alphabet. If a sequence $w : \mathbb{N} \to B$ is a coding of a prolongable $k$-uniform fixed
point, then there are a natural number $q$, an infinite word $u$ over the alphabet
$A = \{0, 1, \dots, q-1\}$ and a map $g : A \to B$ such that $w$ is morphic with generator $u$
and coding $g$.

Formalized by `MetaMathlibExt.IsCodingOfProlongableKUniformFixedPoint.exists_isMorphic`, a theorem declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#exists-is-morphic).

## Automatic sequences are morphic

Let $k$ be a natural number and $B$ a finite alphabet.
If a sequence $w : \mathbb{N} \to B$ is $k$-automatic, then there are a natural number $q$, an
infinite word $u$ over the alphabet $A = \{0, 1, \dots, q-1\}$ and a map $g : A \to B$ such that
$w$ is morphic with generator $u$ and coding $g$.

Formalized by `MetaMathlibExt.IsKAutomaticSequence.exists_isMorphic`, a theorem declared in [MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/CobhamUniformMorphism.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#exists-is-morphic-2).

## The $k$-kernel of a sequence

For a natural number $k$ and a sequence $a$ indexed by
$\mathbb{N}$, the $k$-kernel of $a$ is the set of all sequences $n \mapsto a(k^e n + r)$ with
$e, r \in \mathbb{N}$ and $r < k^e$.

## Sources

- Adamczewski--Bell, arXiv:1205.4091v1, lines 1105--1129. The finite-kernel representation: the kernel is the set of all subsequence maps `n ↦ a (k ^ e * n + r)` as `e : ℕ` varies over exponents and `r : ℕ` varies over residues with `r < k ^ e`. Each member is hence recorded as an explicit pair `(e, r)` together with the equality to the corresponding decimated subsequence.

Formalized by `MetaMathlibExt.kKernel`, a definition declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#k-kernel).

## $k$-automatic sequence (finite-kernel definition)

For a natural number $k$, a sequence
$a$ indexed by $\mathbb{N}$ is $k$-automatic when $k \ge 2$ and the $k$-kernel of $a$ is finite.

## Sources

- Adamczewski--Bell, arXiv:1205.4091v1, lines 160--195 for the finite-automaton (DFAO) definition, and lines 1105--1129 for Eilenberg's equivalence between `k`-automaticity and finiteness of the `k`-kernel. A sequence is `k`-automatic when `2 ≤ k` and its `k`-kernel `kKernel k a` is finite.

Formalized by `MetaMathlibExt.IsKAutomatic`, a definition declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#is-kautomatic).

## The $p^r$-kernel lies in the $p$-kernel

For all natural numbers $p$ and $r$ and every
sequence $a$ indexed by $\mathbb{N}$, the $p^r$-kernel of $a$ is contained in the $p$-kernel of
$a$.

Formalized by `MetaMathlibExt.chr_qkernel_subset`, a theorem declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#chr-qkernel-subset).

## Finiteness of the $p$-kernel from the $p^r$-kernel

Let $p$ and $r$ be positive natural
numbers and let $a$ be a sequence indexed by $\mathbb{N}$. If the $p^r$-kernel of $a$ is finite,
then the $p$-kernel of $a$ is finite.

Formalized by `MetaMathlibExt.chr_pkernel_finite`, a theorem declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#chr-pkernel-finite).

## The $q$-kernel is closed under decimation

Let $q$ be a natural number and let $a$ be a
sequence indexed by $\mathbb{N}$. If $b$ belongs to the $q$-kernel of $a$ and $j < q$, then the
sequence $n \mapsto b(qn + j)$ also belongs to the $q$-kernel of $a$.

Formalized by `MetaMathlibExt.chr_kernel_lam_mem`, a theorem declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#chr-kernel-lam-mem).

## A sequence lies in its own kernel

For every natural number $q$, every sequence $a$
indexed by $\mathbb{N}$ belongs to its own $q$-kernel.

Formalized by `MetaMathlibExt.chr_self_mem_kernel`, a theorem declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#chr-self-mem-kernel).

## Eilenberg's theorem: finite kernel iff automatic

Let $k$ be a natural number and let
$a$ be a sequence indexed by $\mathbb{N}$ with values in a finite type $B$. Then $k \ge 2$ and the
$k$-kernel of $a$ is finite (that is, $a$ is $k$-automatic in the finite-kernel sense) if and only
if $k \ge 2$ and some deterministic finite automaton with output, reading base-$k$ digits least
significant first, outputs $a(n)$ on every word of base-$k$ digits whose value is $n$, for every
$n \in \mathbb{N}$ (that is, $a$ is a $k$-automatic sequence in the automaton sense).

Formalized by `MetaMathlibExt.isKAutomatic_iff_isKAutomaticSequence`, a theorem declared in [MathlibExt/Combinatorics/Words/Automatic.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/Automatic.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html#is-kautomatic-iff-is-kautomatic-sequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Automatic sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/automatic-sequences)
