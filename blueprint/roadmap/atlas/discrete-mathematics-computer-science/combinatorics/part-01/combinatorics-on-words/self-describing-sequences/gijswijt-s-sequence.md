---
declaration: section
origin: cited
lean: MetaMathlibExt.curlingNumber, MetaMathlibExt.curlingNumber_example_one, MetaMathlibExt.curlingNumber_example_three, MetaMathlibExt.curlingNumber_nil, MetaMathlibExt.gijswijtPrefix, MetaMathlibExt.gijswijtTerm, MetaMathlibExt.gijswijtPrefix_one_nine, MetaMathlibExt.gijswijtPrefix_two_eight
statement: formalized
---

# Gijswijt's sequence

34 results, 19 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html).

## Curling number

The curling number $\mathcal{C}(S)$ of a finite string $S$ of natural
numbers is the largest integer $k$ such that $S = X Y^k$ for some strings $X$ and $Y$ with $Y$
nonempty; for the empty string $\varepsilon$ it is $\mathcal{C}(\varepsilon) = 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 1 (curling number) and Section 1.2 (`𝒞(ε) := 1`).

Formalized by `MetaMathlibExt.curlingNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number).

## Curling number of $112112223$

The string $112112223$ has curling number
$\mathcal{C}(112112223) = 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 1 (curling number examples).

Formalized by `MetaMathlibExt.curlingNumber_example_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number-example-one).

## Curling number of $222322232223$

The string $222322232223$ has curling number
$\mathcal{C}(222322232223) = 3$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 1 (curling number examples).

Formalized by `MetaMathlibExt.curlingNumber_example_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number-example-three).

## Curling number of the empty string

The empty string $\varepsilon$ has curling number
$\mathcal{C}(\varepsilon) = 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 1.2 (`𝒞(ε) := 1`).

Formalized by `MetaMathlibExt.curlingNumber_nil`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number-nil).

## Prefixes of the $m$th order Gijswijt sequence

Let $m$ and $n$ be natural numbers. The
list of the first $n$ terms of the $m$th order sequence $A^{(m)}$ is defined by recursion on $n$:
for $n = 0$ it is the empty list, and the list for $n + 1$ is the list $P$ for $n$ followed by
the term $\max(m, \mathcal{C}(P))$, where $\mathcal{C}(P)$ is the curling number of $P$ (the
largest $k$ with $P = XY^k$ for strings $X$, $Y$ with $Y$ nonempty, and $1$ for the empty string).
For $m \ge 1$ the first term is therefore $A^{(m)}(1) = m$; the case $m = 1$ is Gijswijt's
sequence.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (definition of `A^{(m)}`).

Formalized by `MetaMathlibExt.gijswijtPrefix`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-prefix).

## Terms of the $m$th order Gijswijt sequence

For $k \ge 1$, $A^{(m)}(k)$ is the $k$th
term of the $m$th order sequence $A^{(m)}$, that is, the last entry of the list of its first $k$
terms. For $k = 0$ the value is $0$ by convention.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (definition of `A^{(m)}`).

Formalized by `MetaMathlibExt.gijswijtTerm`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-term).

## First terms of Gijswijt's sequence

The first nine terms of Gijswijt's sequence $A^{(1)}$
are $1, 1, 2, 1, 1, 2, 2, 2, 3$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 1 (initial terms of `A`).

Formalized by `MetaMathlibExt.gijswijtPrefix_one_nine`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-prefix-one-nine).

## Initial terms of the second-order Gijswijt sequence

The first eight terms of the
second-order sequence $A^{(2)}$ are $2, 2, 2, 3, 2, 2, 2, 3$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (initial terms of `A^{(2)}`).

Formalized by `MetaMathlibExt.gijswijtPrefix_two_eight`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-prefix-two-eight).

## First occurrence of a value in a Gijswijt sequence

For natural numbers $m$ and $n$, the
first occurrence of $n$ in the $m$th order Gijswijt sequence $A^{(m)}$ is the least position
$k \ge 1$ with $A^{(m)}(k) = n$, and it is $0$ if $n$ does not occur in $A^{(m)}$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 1 (first occurrence) and Section 3 (definition of `t(m, n)`).

Formalized by `MetaMathlibExt.gijswijtFirstOccurrence`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-first-occurrence).

## Block lengths of the higher-order Gijswijt sequences

For a natural number $m$, write
$A^{(m)}(k)$ for the $k$th term of the $m$th order sequence. The block lengths $\beta^{(m)}(t)$
are defined by $\beta^{(m)}(0) = 0$, $\beta^{(m)}(1) = 1$ and, for $t \ge 1$, $\beta^{(m)}(t+1)$
is the least $k > (m+1)\,\beta^{(m)}(t)$ with $A^{(m)}(k+1) = m$, or $0$ if there is no such $k$.

This matches the paper's recursion $B_{t+1} = (B_t)^{m+1} S_t$ for the blocks $B_t$: the glue
string $S_t$ is the run of terms after position $(m+1)\,\beta^{(m)}(t)$ up to the next $m$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (blocks `B_t^{(m)}`, glue strings `S_t^{(m)}`, and their lengths `β^{(m)}(t)`).

Formalized by `MetaMathlibExt.gijswijtBlockLength`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-length).

## Gijswijt blocks

For natural numbers $m$ and $t$, the block $B_t^{(m)}$ is the prefix of
length $\beta^{(m)}(t)$ of the $m$th order Gijswijt sequence $A^{(m)}$, where $\beta^{(m)}(t)$ is
the $t$th block length.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (blocks `B_t^{(m)}`).

Formalized by `MetaMathlibExt.gijswijtBlock`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block).

## Glue strings of a Gijswijt sequence

For natural numbers $m$ and $t$, the glue string
$S^{(m)}_t$ is the block $B^{(m)}_{t+1}$ of the $m$th order Gijswijt sequence with its first
$(m+1)\,\beta^{(m)}(t)$ elements removed, where $\beta^{(m)}(t)$ is the length of the block
$B^{(m)}_t$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (glue strings `S_t^{(m)}`).

Formalized by `MetaMathlibExt.gijswijtGlue`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue).

## Concatenated glue strings of a Gijswijt sequence

For natural numbers $m$ and $t$, the
string $T^{(m)}_t$ is the concatenation $S^{(m)}_1 S^{(m)}_2 \cdots S^{(m)}_{t-1}$ of the glue
strings of the $m$th order Gijswijt sequence; it is empty when $t \le 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (strings `T_t^{(m)}`).

Formalized by `MetaMathlibExt.gijswijtGlueConcat`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat).

## Block index of the first occurrence

For natural numbers $m$ and $n$, let $p$ be the
position of the first occurrence of $n$ in the $m$th order Gijswijt sequence $A^{(m)}$, with
$p = 0$ if $n$ does not occur. Then $t(m, n)$ is the least $t \ge 1$ such that the block length
$\beta^{(m)}(t)$ equals $p$, so that when $n$ occurs, this first $n$ is the last element of the
block $B_t^{(m)}$; if there is no such $t$, then $t(m, n) = 0$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 3 (definition of `t(m, n)`).

Formalized by `MetaMathlibExt.gijswijtBlockIndex`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-index).

## Block words

For natural numbers $m$ and $u$ and exponents $a_1, a_2, \ldots$, the block
word of order $m$ is the concatenation $B_{u-1}^{a_{u-1}} \cdots B_2^{a_2} B_1^{a_1}$, where
$B_i = B_i^{(m)}$ is the $i$th block of the $m$th order Gijswijt sequence and $B_i^{a_i}$ is
$a_i$ copies of $B_i$ in a row. Only $a_1, \ldots, a_{u-1}$ are used, and the word is empty when
$u \le 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 4, Expression (1) in Lemma 11.

Formalized by `MetaMathlibExt.gijswijtBlockWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-word).

## The first block has length one

For every natural number $m$, the first block length
$\beta^{(m)}(1)$ of the $m$th order Gijswijt sequence equals $1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (`B_1^{(m)} = m`).

Formalized by `MetaMathlibExt.gijswijtBlockLength_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-length-one).

## The first block

For every $m \ge 1$, the first block $B_1^{(m)}$ of the $m$th order
Gijswijt sequence is the one-term string $m$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (`B_1^{(m)} = m`, Table 1).

Formalized by `MetaMathlibExt.gijswijtBlock_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-one).

## The first concatenated glue string is empty

For every natural number $m$, the
concatenated glue string $T^{(m)}_1$ is the empty string.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Section 2 (Table 1).

Formalized by `MetaMathlibExt.gijswijtGlueConcat_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat-one).

## The empty block word

For every natural number $m$ and every sequence of exponents
$a_1, a_2, \ldots$, the block word $B_{u-1}^{a_{u-1}} \cdots B_1^{a_1}$ of order $m$ with $u = 1$,
where $B_i$ is the $i$th block of the $m$th order Gijswijt sequence, is a product of no blocks
and hence the empty string.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, proof of Lemma 11 (case `u = 1`).

Formalized by `MetaMathlibExt.gijswijtBlockWord_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-word-one).

## Van de Pol's tower formula for first occurrences

For every $n \ge 4$ there is a real
number $\alpha$ with $n - 2 < \alpha < n - 1$ such that the first occurrence of $n$ in Gijswijt's
sequence is at position $2^{2^{3^{\cdot^{\cdot^{(n-2)^{\alpha}}}}}}$, a power tower whose bases
are $2, 2, 3, \ldots, n-2$ from the bottom up and whose top exponent is $\alpha$; for $n = 4$ it
is $2^{2^{\alpha}}$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Theorem 1 (`jis-2025-25.4.6-thm-1`).

Stated but not proved: `MetaMathlibExt.gijswijtFirstOccurrence_tower` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-first-occurrence-tower).

## The curling number is monotone under suffixes

For strings $S$ and $T$ of natural numbers,
if $T$ is a suffix of $S$, then $\mathcal{C}(T) \le \mathcal{C}(S)$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 3 (`jis-2025-25.4.6-lem-3`).

Stated but not proved: `MetaMathlibExt.curlingNumber_le_of_suffix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number-le-of-suffix).

## Concatenated glue strings occur in a block only at its end

Let $m \ge 1$ and $t \ge 2$.
The element $m$ followed by the concatenated glue string $T^{(m)}_t$ is a suffix of the block
$B^{(m)}_t$, and whenever $B^{(m)}_t = X\,T^{(m)}_t\,Y$ for strings $X$ and $Y$, the string $Y$ is
empty; that is, $T^{(m)}_t$ occurs in $B^{(m)}_t$ only as a suffix.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 4 (`jis-2025-25.4.6-lem-4`).

Stated but not proved: `MetaMathlibExt.gijswijtGlueConcat_suffix_block` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat-suffix-block).

## Concatenated glue strings are the next-order prefixes with small curling number

Let
$m \ge 1$. A finite string $P$ of natural numbers is a prefix of the $(m+1)$th order Gijswijt
sequence $A^{(m+1)}$ with curling number $\mathcal{C}(P) \le m$ if and only if $P = T^{(m)}_t$ for
some $t \ge 1$, where $T^{(m)}_t$ is the concatenated glue string.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 5 (`jis-2025-25.4.6-lem-5`).

Stated but not proved: `MetaMathlibExt.gijswijtGlueConcat_iff_prefix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat-iff-prefix).

## Runs of the smallest term in a block

Let $m \ge 1$ and $t \ge 2$, and consider the block
$B_t^{(m)}$ of the $m$th order Gijswijt sequence. Every maximal run of consecutive terms equal to
$m$ in $B_t^{(m)}$ has length exactly $m + 1$, and the term right after the run exists and equals
$m + 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 6 (`jis-2025-25.4.6-lem-6`).

Stated but not proved: `MetaMathlibExt.gijswijtBlock_runs` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-runs).

## First occurrences end blocks

Let $1 \le m \le n$, and write $\beta^{(m)}(t)$ for the
length of the block $B_t^{(m)}$ of the $m$th order Gijswijt sequence $A^{(m)}$. Then there is a
$t \ge 1$ such that $A^{(m)}(\beta^{(m)}(t)) = n$ and $\beta^{(m)}(t)$ is the position of the
first occurrence of $n$ in $A^{(m)}$; that is, the first $n$ in $A^{(m)}$ is the last term of the
block $B_t^{(m)}$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 7 (`jis-2025-25.4.6-lem-7`).

Stated but not proved: `MetaMathlibExt.gijswijtFirstOccurrence_eq_blockLength` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-first-occurrence-eq-block-lengt).

## Concatenated glue strings at first occurrences are blocks of the next order

Let $m \ge 1$
and $n \ge m + 1$. For $j \ge 1$ let $t(j, n)$ be the least $t \ge 1$ such that the block
$B^{(j)}_t$ of the $j$th order Gijswijt sequence has length equal to the position of the first
occurrence of $n$ in that sequence (this position is taken to be $0$ if $n$ does not occur), and
$t(j, n) = 0$ if there is no such $t$. Then the concatenated glue string $T^{(m)}_{t(m,n)}$
equals the block $B^{(m+1)}_{t(m+1,n)}$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 9 (`jis-2025-25.4.6-lem-9`).

Stated but not proved: `MetaMathlibExt.gijswijtGlueConcat_blockIndex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat-block-index).

## Proper prefixes of a block with curling number at most $m + 1$

Let $m \ge 1$ and
$u \ge 1$, and write $B_t$ for the block $B_t^{(m+1)}$ of the $(m+1)$th order Gijswijt sequence.
A string $P$ is a proper prefix of $B_u$ (a prefix strictly shorter than $B_u$) with curling
number $\mathcal{C}(P) \le m + 1$ if and only if $P = B_{u-1}^{a_{u-1}} \cdots B_2^{a_2} B_1^{a_1}$
for some natural numbers $a_1, \dots, a_{u-1} \le m + 1$, where $B_t^{a}$ denotes $a$ copies of
$B_t$ concatenated.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 11 (`jis-2025-25.4.6-lem-11`).

Stated but not proved: `MetaMathlibExt.gijswijtProperPrefix_curling_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-proper-prefix-curling-iff).

## Curling number of block words with a maximal exponent

Let $m \ge 1$ and $u \ge 1$, and
let $a_1, \dots, a_{u-1} \in \{0, \dots, m+1\}$ with $a_i = m + 1$ for some $1 \le i \le u - 1$.
Writing $B_t = B_t^{(m+1)}$ for the blocks of the $(m+1)$th order Gijswijt sequence $A^{(m+1)}$,
the string $P = B_{u-1}^{a_{u-1}} \cdots B_2^{a_2} B_1^{a_1}$ has curling number
$\mathcal{C}(P) = m + 1$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 12 (`jis-2025-25.4.6-lem-12`).

Stated but not proved: `MetaMathlibExt.curlingNumber_blockWord_of_max` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number-block-word-of-max).

## Curling number of block words with small exponents

Let $m \ge 1$ and $u \ge 2$, and let
$a_1, \dots, a_{u-1} \in \{0, \dots, m\}$ with $a_1 \ne 0$. Writing $B_t = B_t^{(m+1)}$ for the
blocks of the $(m+1)$th order Gijswijt sequence $A^{(m+1)}$, the string
$P = B_{u-1}^{a_{u-1}} \cdots B_2^{a_2} B_1^{a_1}$ has curling number $\mathcal{C}(P) \le m$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 13 (`jis-2025-25.4.6-lem-13`).

Stated but not proved: `MetaMathlibExt.curlingNumber_blockWord_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#curling-number-block-word-le).

## Concatenated glue strings inside a block of the next order

Let $m \ge 1$ and $u \ge 2$,
and for exponents $a_1, \ldots, a_{u-1}$ let
$W(a) = (B^{(m+1)}_{u-1})^{a_{u-1}} \cdots (B^{(m+1)}_1)^{a_1}$ be the word in the blocks of the
$(m+1)$th order Gijswijt sequence. (a) If $t \ge 1$ and the concatenated glue string $T^{(m)}_t$
is a proper prefix of $B^{(m+1)}_u$, then $T^{(m)}_t = W(a)$ for some
$a_1, \ldots, a_{u-1} \in \{0, \ldots, m\}$. (b) For all $a_1, \ldots, a_{u-1} \in \{0, \ldots, m\}$
with $a_1 \ne 0$, there is $t \ge 1$ such that $T^{(m)}_t$ is a proper prefix of $B^{(m+1)}_u$ and
$W(a) = T^{(m)}_t$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 16 (`jis-2025-25.4.6-lem-16`).

Stated but not proved: `MetaMathlibExt.gijswijtGlueConcat_blockWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat-block-word).

## Bounds on the block lengths of order $m+1$

Let $m \ge 1$ and $u \ge 2$. Write
$\beta^{(m+1)}(u)$ for the length of the block $B_u^{(m+1)}$ of the $(m+1)$th order Gijswijt
sequence, and $\tau^{(m)}(t)$ for the length of $T_t^{(m)} = S_1^{(m)} \cdots S_{t-1}^{(m)}$, the
concatenation of the first $t - 1$ glue strings of order $m$. Then
$\tau^{(m)}(m (m+1)^{u-2}) \le \beta^{(m+1)}(u) \le \tau^{(m)}((m+1)^{u-1} + 1)$, and the second
inequality is strict when $u = m + 3$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 17 (`jis-2025-25.4.6-lem-17`).

Stated but not proved: `MetaMathlibExt.gijswijtBlockLength_estimates` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-length-estimates).

## Length estimates for concatenated glue strings

Let $m \ge 1$ and $t \ge 2$, write
$\tau^{(m)}(t)$ for the length of the concatenated glue string $T^{(m)}_t$ and $\beta^{(m+1)}$ for
the block lengths of the $(m+1)$th order Gijswijt sequence, and let $c$ be the least natural
number with $t \le (m+1)^c$, that is, $c = \lceil \log_{m+1} t \rceil$. Then
$\beta^{(m+1)}(c) \le \tau^{(m)}(t) \le \beta^{(m+1)}(c + 2)$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Proposition 18 (`jis-2025-25.4.6-prop-18`).

Stated but not proved: `MetaMathlibExt.gijswijtGlueConcat_length_estimates` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-glue-concat-length-estimates).

## Recursive estimate for the block index

Let $m \ge 1$ and $n \ge m + 3$, and for $k \ge 1$
let $t(k, n)$ be the index $t$ such that the first occurrence of $n$ in the $k$th order Gijswijt
sequence $A^{(k)}$ is the last element of the block $B_t^{(k)}$ of $A^{(k)}$. Then
$m (m+1)^{t(m+1,n) - 2} \le t(m, n) \le (m+1)^{t(m+1,n) - 1} + 1$, and the second inequality is
strict when $n = m + 3$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Proposition 19 (`jis-2025-25.4.6-prop-19`).

Stated but not proved: `MetaMathlibExt.gijswijtBlockIndex_estimates` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-index-estimates).

## Upper bound on block lengths

Let $M_7 = 4$ and $M_{k+1} = M_k (1 + 9 (k+1)^{1.59} / 2^k)$
for $k \ge 7$. Then for all $m \ge 1$ and $u \ge 7$, the block lengths $\beta^{(m)}(u)$ of the
$m$th order Gijswijt sequence $A^{(m)}$ satisfy $\beta^{(m)}(u) / (m+1)^{u-1} < M_u$.

## Sources

- Levi van de Pol, *The Growth Rate of Gijswijt's Sequence*, Journal of Integer Sequences 28 (2025), Article 25.4.6, Lemma 20 (`jis-2025-25.4.6-lem-20`).

Stated but not proved: `MetaMathlibExt.gijswijtBlockLength_div_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/GijswijtSequenceWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html#gijswijt-block-length-div-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gijswijt's sequence](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/gijswijt-s-sequence)
