---
declaration: section
origin: cited
lean: MetaMathlibExt.basePhiValue, MetaMathlibExt.IsBergmanExpansion, MetaMathlibExt.IsGoldenMeanFlip, MetaMathlibExt.SatisfiesKnottCondition, MetaMathlibExt.knottExpansions, MetaMathlibExt.knottExpansionCount, MetaMathlibExt.naturalExpansions, MetaMathlibExt.naturalExpansionCount
statement: formalized
---

# Golden ratio base

84 results, 46 proved and 38 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html).

## Value of a base phi expansion

For a finite set $S$ of integers, the base phi value of
$S$ is the real number $\sum_{i \in S} \varphi^i$, where $\varphi = (1 + \sqrt 5)/2$ is the golden
ratio. It is the number represented by the base phi expansion with digit $1$ at each position in
$S$ and digit $0$ at every other position.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1 (definition of a base phi representation).

Formalized by `MetaMathlibExt.basePhiValue`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-value).

## Bergman expansions

Encode a finite base phi expansion with digits $0$ and $1$ by the
finite set $S \subseteq \mathbb{Z}$ of positions of its digits $1$. The expansion is a Bergman
expansion when no two digits $1$ are adjacent, that is, $i + 1 \notin S$ for every $i \in S$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1 (Bergman representation).

Formalized by `MetaMathlibExt.IsBergmanExpansion`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-bergman-expansion).

## Golden mean flips

Encode a finite base phi expansion with digits $0$ and $1$ by the
finite set of positions of its digits $1$. An expansion $T$ arises from an expansion $S$ by a
golden mean flip $100 \to 011$ when there is a position $i \in S$ with $i - 1 \notin S$ and
$i - 2 \notin S$ such that $T = (S \setminus \{i\}) \cup \{i - 1, i - 2\}$: the digit $1$ at
position $i$ is replaced by digits $1$ at positions $i - 1$ and $i - 2$, which were $0$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Sections 1 and 2 (the map `T_i`).

Formalized by `MetaMathlibExt.IsGoldenMeanFlip`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-golden-mean-flip).

## Knott's truncation rule

Let $\varphi$ be the golden ratio. Encode a finite base $\varphi$
expansion with digits $0$ and $1$ by the finite set $S \subseteq \mathbb{Z}$ of the positions of
its digits $1$, and write $a_i$ for its digit at position $i$. The expansion satisfies Knott's
condition when it does not end in the digits $0, 1, 1$: if $S$ is nonempty with least element $R$,
then $a_{R+2} a_{R+1} a_R \ne 011$, that is, it is not the case that both $R + 1 \in S$ and
$R + 2 \notin S$. The empty expansion satisfies the condition.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1, Equation (1.1).

Formalized by `MetaMathlibExt.SatisfiesKnottCondition`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#satisfies-knott-condition).

## Knott expansions

Let $\varphi$ be the golden ratio and $N$ a natural number. Encode a
finite base phi expansion with digits $0$ and $1$ by the finite set $S \subseteq \mathbb{Z}$ of the
positions of its digits $1$. The Knott expansions of $N$ are the expansions of value $N$ that
satisfy Knott's truncation rule: the set of all such $S$ with $\sum_{i \in S} \varphi^i = N$ that
satisfy Knott's condition.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1.

Formalized by `MetaMathlibExt.knottExpansions`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#knott-expansions).

## Number of Knott expansions

For a natural number $N$, $\mathrm{Tot}_\kappa(N)$ is the
number of Knott expansions of $N$ (OEIS A289749).

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1.

Formalized by `MetaMathlibExt.knottExpansionCount`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#knott-expansion-count).

## Natural base phi expansions

Let $\varphi$ be the golden ratio and $N$ a natural number.
Encode a finite base phi expansion with digits $0$ and $1$ by the finite set
$S \subseteq \mathbb{Z}$ of the positions of its digits $1$. The natural expansions of $N$ are the
Knott expansions $S$ of $N$ for which there is a Bergman expansion $T$ with
$\sum_{i \in T} \varphi^i = N$ whose lowest digit $1$ is at the same position as the lowest
digit $1$ of $S$, that is, $\min T = \min S$, where $S$ and $T$ both empty also counts as
equal.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 4.

Formalized by `MetaMathlibExt.naturalExpansions`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#natural-expansions).

## Number of natural expansions

For a natural number $N$, $\mathrm{Tot}_\nu(N)$ is the
number of natural base phi expansions of $N$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 4.

Formalized by `MetaMathlibExt.naturalExpansionCount`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#natural-expansion-count).

## Number of Fibonacci representations

For a natural number $m$,
$\mathrm{Tot}_{\mathrm{FIB}}(m)$ is the number of finite sets $T$ of indices $i \ge 2$ with
$\sum_{i \in T} F_i = m$, where $F_i$ are the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$); that is,
the number of ways to write $m$ as a sum of Fibonacci numbers with distinct indices at least $2$
(OEIS A000119). Indices above $m + 1$ never occur because $F_{m+2} > m$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1 (base Fibonacci representations).

Formalized by `MetaMathlibExt.fibonacciRepresentationCount`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#fibonacci-representation-count).

## The empty base phi expansion has value zero

The base phi value of the empty set of
positions is $0$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1.

Formalized by `MetaMathlibExt.basePhiValue_empty`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-value-empty).

## The single digit $1$ at position $0$ has value one

The base phi value of the set $\{0\}$
is $1$, that is, $\varphi^0 = 1$, where $\varphi$ is the golden ratio.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1.

Formalized by `MetaMathlibExt.basePhiValue_singleton_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-value-singleton-zero).

## The base phi expansion $10.01$ has value two

The base phi value of the set $\{1, -2\}$
is $2$, that is, $\varphi + \varphi^{-2} = 2$, where $\varphi$ is the golden ratio.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), proof of Proposition 3.1.

Formalized by `MetaMathlibExt.basePhiValue_one_neg_two`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-value-one-neg-two).

## The base phi expansion $1.11$ has value two

The base phi value of the set
$\{0, -1, -2\}$ is $2$, that is, $1 + \varphi^{-1} + \varphi^{-2} = 2$, where $\varphi$ is the
golden ratio.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 2.

Formalized by `MetaMathlibExt.basePhiValue_zero_neg_one_neg_two`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-value-zero-neg-one-neg-two).

## The expansion 10.01 is a Bergman expansion

The base phi expansion $10.01$, with digits $1$
at positions $1$ and $-2$ and digits $0$ elsewhere, has no two adjacent digits $1$, so it is a
Bergman expansion.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1.

Formalized by `MetaMathlibExt.isBergmanExpansion_one_neg_two`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-bergman-expansion-one-neg-two).

## A golden mean flip from 10.01 to 1.11

Applying the golden mean flip $100 \to 011$ at the
leading digit of $10.01$ (the digit $1$ at position $1$, followed by digits $0$ at positions $0$
and $-1$) gives $1.11$, the expansion with digits $1$ at positions $0$, $-1$ and $-2$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 2.

Formalized by `MetaMathlibExt.isGoldenMeanFlip_one_neg_two`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-golden-mean-flip-one-neg-two).

## A Knott expansion of two

Let $\varphi$ be the golden ratio. The base $\varphi$ expansion
$1.11$, whose digits $1$ sit at the positions $0$, $-1$ and $-2$, is a Knott expansion of $2$:
its value is $1 + \varphi^{-1} + \varphi^{-2} = 2$ and it satisfies Knott's truncation rule.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1.

Formalized by `MetaMathlibExt.zero_neg_one_neg_two_mem_knottExpansions`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#zero-neg-one-neg-two-mem-knott-expansion).

## The expansion 0.11 violates Knott's truncation rule

The finite base phi expansion
$0.11$, with digits $1$ at positions $-1$ and $-2$ and no others, ends in the digits $011$, so it
does not satisfy Knott's truncation rule.

It represents $1$, since $\varphi^{-1} + \varphi^{-2} = 1$ for the golden ratio $\varphi$, but
is not a Knott expansion of $1$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1, Equation (1.1).

Formalized by `MetaMathlibExt.not_satisfiesKnottCondition_neg_one_neg_two`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#not-satisfies-knott-condition-neg-one-ne).

## The expansion 10.01 is a natural expansion of 2

The finite base phi expansion $10.01$,
with digits $1$ exactly at positions $1$ and $-2$, is a natural base phi expansion of $2$.

It is the Bergman expansion of $2$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 4.

Formalized by `MetaMathlibExt.one_neg_two_mem_naturalExpansions`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#one-neg-two-mem-natural-expansions).

## Small values of the Fibonacci representation count

Let $F_i$ be the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$), and let $\mathrm{Tot}_{\mathrm{FIB}}(m)$ be the number of ways to write
$m$ as a sum of Fibonacci numbers $F_i$ with distinct indices $i \ge 2$. Then
$\mathrm{Tot}_{\mathrm{FIB}}(0), \dots, \mathrm{Tot}_{\mathrm{FIB}}(8)$ are
$1, 1, 1, 2, 1, 2, 2, 1, 3$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Section 1 (the listed values of `Tot_FIB`).

Formalized by `MetaMathlibExt.fibonacciRepresentationCount_small`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#fibonacci-representation-count-small).

## Golden mean flips connect all expansions to the Bergman expansion

Let $N$ be a natural
number, let $S$ be a Bergman expansion of $N$ and let $T$ be any finite base phi expansion of
$N$ with digits $0$ and $1$. Then $T$ is obtained from $S$ by finitely many (possibly zero)
golden mean flips $100 \to 011$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.reflTransGen_isGoldenMeanFlip_of_isBergmanExpansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#refl-trans-gen-is-golden-mean-flip-of-is).

## Recursion for the number of Knott expansions

Let $\varphi$ be the golden ratio, let
$N \ge 2$ and $n$ be natural numbers, and let $p_0, \dots, p_n$ be integers with
$p_{k+1} \ge p_k + 2$ for all $k < n$ and $\sum_{k=0}^{n} \varphi^{p_k} = N$. Thus $N$ has the
base phi expansion $10^{s_n} \cdots 10^{s_1} 1$ with digits $1$ at positions $p_0 < \dots < p_n$,
where $s_k = p_k - p_{k-1} - 1$ for $1 \le k \le n$. Let $r_0, r_1, \dots$ be integers with
$r_0 = 1$; if $n \ge 1$, let $r_1 = s_1/2 + 1$ when $s_1$ is even and $r_1 = (s_1 + 1)/2 + 1$
when $s_1$ is odd; and for $2 \le k \le n$, let $r_k = (s_k/2 + 1)\, r_{k-1}$ when $s_k$ is even
and $r_k = ((s_k + 1)/2 + 1)\, r_{k-1} - r_{k-2}$ when $s_k$ is odd. Then the number of Knott
expansions of $N$ is $r_n$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 2.3.

Stated but not proved: `MetaMathlibExt.knottExpansionCount_eq_of_recursion` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#knott-expansion-count-eq-of-recursion).

## Bergman expansions of the Fibonacci numbers

Let $n \ge 1$ and write $F_m$ for the $m$-th
Fibonacci number, with $F_1 = F_2 = 1$. Let $S$ be a finite set of integers with no two
consecutive elements (a Bergman expansion). If the base phi value of $S$ is $F_{2n}$, then
$S = \{t + 4j : 0 \le j < n\}$ for some integer $t$. If the base phi value of $S$ is
$F_{2n+1}$, then $S = \{t\} \cup \{t + 3 + 4j : 0 \le j < n\}$ for some integer $t$.

Read from the highest to the lowest position, these are the digit words $(1000)^{n-1}1$ and
$(1000)^{n-1}1001$; the position of the radix point is not determined.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Proposition 3.1.

Stated but not proved: `MetaMathlibExt.bergmanWord_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#bergman-word-fib).

## Knott expansions of Fibonacci numbers

Let $F_n$ be the Fibonacci numbers ($F_0 = 0$,
$F_1 = 1$). For every $n \ge 1$, the number of Knott expansions of $F_n$ is $F_n$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 3.2.

Stated but not proved: `MetaMathlibExt.knottExpansionCount_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#knott-expansion-count-fib).

## Knott expansions of Lucas numbers

For every $n \ge 1$, each of the Lucas numbers $L_{2n}$
and $L_{2n+1}$ (with $L_0 = 2$, $L_1 = 1$) has exactly $2n + 1$ Knott expansions.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 3.3.

Stated but not proved: `MetaMathlibExt.knottExpansionCount_lucasNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#knott-expansion-count-lucas-number).

## Recursion for the number of natural expansions

Let $N$ and $n$ be natural numbers and
let $p_0, \dots, p_n$ be integers with $p_k + 2 \le p_{k+1}$ for $k < n$ such that the base phi
expansion with digits $1$ at positions $p_0, \dots, p_n$ represents $N$. Put
$s_k = p_k - p_{k-1} - 1$ for $1 \le k \le n$. Let $r_0, r_1, \dots$ be integers with
$r_0 = 1$ such that, if $n \ge 1$, $2 r_1 = s_1 + 2$ when $s_1$ is even and $2 r_1 = s_1 + 1$
when $s_1$ is odd, and for $2 \le k \le n$, $2 r_k = (s_k + 2) r_{k-1}$ when $s_k$ is even and
$2 r_k = (s_k + 3) r_{k-1} - 2 r_{k-2}$ when $s_k$ is odd. Then the number
$\mathrm{Tot}_\nu(N)$ of natural base phi expansions of $N$ equals $r_n$.

Compared with the recursion for the number of Knott expansions, only the value of $r_1$ for odd
$s_1$ differs, and $N \ge 2$ is not assumed.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.naturalExpansionCount_eq_of_recursion` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#natural-expansion-count-eq-of-recursion).

## Fibonacci numbers in the Lucas intervals

Let $F_k$ be the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$) and $L_k$ the Lucas numbers ($L_0 = 2$, $L_1 = 1$). Call
$\Lambda_{2n} = [L_{2n}, L_{2n+1}]$ the even Lucas interval and
$\Lambda_{2n+1} = [L_{2n+1} + 1, L_{2n+2} - 1]$ the odd Lucas interval. For every $n \ge 1$,
$F_{2n+2} \in \Lambda_{2n}$ and $F_{2n+3} \in \Lambda_{2n+1}$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Lemma 4.2.

Stated but not proved: `MetaMathlibExt.fib_mem_lucasIntervals` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#fib-mem-lucas-intervals).

## Natural expansions of Fibonacci numbers

Write $\mathrm{Tot}_\nu(N)$ for the number of
natural base phi expansions of a natural number $N$ and $F_k$ for the $k$-th Fibonacci number.
Then for every $n \ge 0$, $\mathrm{Tot}_\nu(F_{2n+2}) = F_{2n+1}$ and
$\mathrm{Tot}_\nu(F_{2n+3}) = F_{2n+3}$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 4.3.

Stated but not proved: `MetaMathlibExt.naturalExpansionCount_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#natural-expansion-count-fib).

## Natural expansions are counted by Fibonacci representations

Write $F_k$ for the $k$-th
Fibonacci number. Let $N > 3$ be a natural number, let $S$ be a Bergman expansion of $N$ and let
$R$ be the lowest position of a digit $1$ in $S$. Then the number $\mathrm{Tot}_\nu(N)$ of natural
base phi expansions of $N$ equals the number $\mathrm{Tot}_{\mathrm{FIB}}(F_{2-R} N)$ of
representations of $F_{2-R} N$ as a sum of Fibonacci numbers with distinct indices at least $2$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 4.4.

Stated but not proved: `MetaMathlibExt.naturalExpansionCount_eq_fibonacciRepresentationCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#natural-expansion-count-eq-fibonacci-rep).

## Lucas interval of $N$ from the gap between its two lowest Bergman digits

Let $N \ge 2$
be a natural number, let $S$ be a finite set of integers with no two consecutive elements (a
Bergman expansion) whose base phi value is $N$, and let $a$ be an integer and $s$ a natural number
such that the elements of $S$ that are at most $a + s + 1$ are exactly $a$ and $a + s + 1$ (so the
expansion ends in the digits $10^s1$). Write $L_m$ for the $m$-th Lucas number. Then
$L_{2n} \le N \le L_{2n+1}$ for some natural number $n$ if and only if $s$ is odd, and
$L_{2n+1} + 1 \le N \le L_{2n+2} - 1$ for some natural number $n$ if and only if $s$ is even.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Proposition 5.1(a).

Stated but not proved: `MetaMathlibExt.bergman_tail_parity_iff_lucasInterval` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#bergman-tail-parity-iff-lucas-interval).

## Lowest Bergman digit of $N$ from its Lucas interval

Let $N$ and $n$ be natural numbers,
let $S$ be a finite set of integers with no two consecutive elements (a Bergman expansion) whose
base phi value is $N$, and let $R$ be the least element of $S$. Write $L_m$ for the $m$-th Lucas
number. If $L_{2n} \le N \le L_{2n+1}$, then $-R = 2n$. If $L_{2n+1} + 1 \le N \le L_{2n+2} - 1$,
then $-R = 2n + 2$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Proposition 5.1(b).

Stated but not proved: `MetaMathlibExt.bergman_lowest_position_lucasInterval` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#bergman-lowest-position-lucas-interval).

## Bergman expansion of $L_{2n} + k$

Let $n \ge 1$ and let $k$ be a natural number with
$k \le L_{2n-1}$, where $L_m$ is the $m$-th Lucas number. Let $S$ and $T$ be finite sets of
integers, each with no two consecutive elements (Bergman expansions), whose base phi values are
$k$ and $L_{2n} + k$ respectively. Then $2n \notin S$, $-2n \notin S$, and
$T = S \cup \{2n, -2n\}$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 5.2 I, quoting F. M. Dekking, *How to add two numbers in base phi*.

Stated but not proved: `MetaMathlibExt.bergman_lucas_even_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#bergman-lucas-even-add).

## Recursive structure of Bergman expansions, odd Lucas case

Let $n \ge 2$, let $k$ be a
natural number, and write $L_m$ for the $m$-th Lucas number. Call a finite set of integers with no
two consecutive elements a Bergman expansion. Let $S$ and $T$ be Bergman expansions, let $a$ and
$t$ be the least and the greatest element of $S$, let $S' = S \setminus \{a, t\}$, and for an
integer $c$ write $S' + c = \{x + c : x \in S'\}$.

(i) If $1 \le k \le L_{2n-2} - 1$, the base phi value of $S$ is $L_{2n-1} + k$ and that of $T$
is $L_{2n+1} + k$, then there is an integer $b$ with
$T = \{b, b + 3, b + (t - a) + 4\} \cup (S' + (b - a + 2))$.

(ii) If $1 \le k \le L_{2n-2} - 1$, the base phi value of $S$ is $L_{2n-1} + k$ and that of $T$
is $L_{2n+1} + L_{2n-1} + k$, then there is an integer $b$ with
$T = \{b, b + (t - a) + 2, b + (t - a) + 4\} \cup (S' + (b - a + 2))$.

(iii) If $k \le L_{2n-3}$, the base phi value of $S$ is $L_{2n-2} + k$ and that of $T$ is
$L_{2n+1} + L_{2n-2} + k$, then there is an integer $b$ with
$T = \{b, b + 3, b + (t - a) + 4, b + (t - a) + 7\} \cup (S' + (b - a + 4))$.

## Sources

- Michel Dekking and Ad van Loon, *Counting Base Phi Representations*, Fibonacci Quarterly 62 (2024), Article 62-2/dekking11102023, Theorem 5.2 II, quoting F. M. Dekking, *How to add two numbers in base phi*.

Stated but not proved: `MetaMathlibExt.bergman_lucas_odd_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiRepresentationsWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#bergman-lucas-odd-add).

## Base phi expansion

Let $\varphi$ be the golden ratio. A finite set $S$ of integers, read as
the positions of the digits $1$ of a finite expansion with digits $0$ and $1$, is a base phi
expansion of the natural number $N$ when it is a Bergman expansion (no two digits $1$ are
adjacent: $i \in S$ implies $i + 1 \notin S$) and its value $\sum_{i \in S} \varphi^i$ equals $N$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 1 (definition of `β(N)`).

Formalized by `MetaMathlibExt.IsBasePhiExpansion`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-base-phi-expansion).

## Base phi expansion of zero

The empty set of positions, the expansion with no digit $1$, is
a base phi expansion of $0$: it has no two adjacent digits $1$, and its value, the empty sum, is
equal to $0$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 1.

Formalized by `MetaMathlibExt.isBasePhiExpansion_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-base-phi-expansion-zero).

## Base phi expansion of one

The set $\{0\}$, read as the positions of the digits $1$, is a
base phi expansion of $1$: the expansion with a single digit $1$ at position $0$ has no two
adjacent digits $1$, and its value $\varphi^0$ equals $1$, where $\varphi$ is the golden ratio.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Table 1.

Formalized by `MetaMathlibExt.isBasePhiExpansion_one`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-base-phi-expansion-one).

## Digit block of an expansion

Let $S$ be a finite set of integers, read as the positions of
the digits $1$ of an expansion with digits $d_i$, so $d_i = 1$ if $i \in S$ and $d_i = 0$
otherwise. For an integer $k$ and a finite word $w = w_0 w_1 \cdots w_{m-1}$ over the natural
numbers, $w$ occurs as a digit block of $S$ at position $k$ when the digits
$d_k d_{k-1} \cdots d_{k-m+1}$, read from the highest position down, are the letters of $w$: for
every $i < m$, $d_{k-i} = 1$ holds exactly when $w_i = 1$. A letter $1$ stands for the digit $1$
and any other letter for the digit $0$; the empty word occurs at every position.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Sections 6 and 7 (digit blocks `d_{m-1} ⋯ d_0` and `d_{-1} ⋯ d_{-m}`).

Formalized by `MetaMathlibExt.HasDigitBlock`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#has-digit-block).

## The empty digit block occurs everywhere

For every finite set $S$ of integers, read as the
positions of the digits $1$ of an expansion, and every integer $k$, the empty word occurs as a
digit block of $S$ at position $k$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 6.

Formalized by `MetaMathlibExt.hasDigitBlock_nil`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#has-digit-block-nil).

## Peeling off the leading letter of a digit block

Let $S$ be a finite set of integers, read
as the positions of the digits $1$ of an expansion. For every integer $k$, every natural number
$b$ and every finite word $w$ over the natural numbers, the word $bw$ (the letter $b$ followed by
$w$) occurs as a digit block of $S$ at position $k$ if and only if both $k \in S$ holds exactly
when $b = 1$, and $w$ occurs as a digit block of $S$ at position $k - 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 6.

Formalized by `MetaMathlibExt.hasDigitBlock_cons`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#has-digit-block-cons).

## Occurrence set of a digit block

For an integer $k$ and a word $w = w_1 w_2 \cdots w_\ell$
of natural numbers, the occurrence set of $w$ at position $k$ is the set of natural numbers $N$
that have a base phi expansion $S$ (the set of positions of its digits $1$) whose digits
$d_k d_{k-1} \cdots d_{k-\ell+1}$ spell $w$: for each $j = 1, \dots, \ell$, the position
$k - j + 1$ lies in $S$ if and only if $w_j = 1$.

The paper's $R_w$, the set of $N$ whose expansion has the end block $w$ at positions
$\ell - 1, \dots, 0$, is the case $k = \ell - 1$, and $R_{\cdot w}$, the set of $N$ whose digits at
positions $-1, \dots, -\ell$ spell $w$, is the case $k = -1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Sections 6 and 7 (occurrence sequences `R_w`).

Formalized by `MetaMathlibExt.basePhiOccurrences`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-occurrences).

## A base phi expansion of 1 ends in the digit 1

The number $1$ lies in the occurrence
set of the one-letter digit block $1$ placed at position $0$ (the paper's $R_1$): some base phi
expansion of $1$ has the digit $1$ at position $0$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 6.

Formalized by `MetaMathlibExt.one_mem_basePhiOccurrences_one`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#one-mem-base-phi-occurrences-one).

## Generalized Beatty sequence

Let $\varphi$ be the golden ratio. For integers $p, q, r$, the
generalized Beatty sequence $V(p, q, r)$ is the integer sequence defined for every natural number
$n$, including $n = 0$, by $V(p, q, r)(n) = p\lfloor n\varphi \rfloor + qn + r$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 5.

Formalized by `MetaMathlibExt.generalizedBeatty`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#generalized-beatty).

## Generalized Beatty sequence at zero

Let $\varphi$ be the golden ratio. For all integers
$p, q, r$, the generalized Beatty sequence $V(p, q, r)(n) = p\lfloor n\varphi \rfloor + qn + r$
takes the value $V(p, q, r)(0) = r$ at $n = 0$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 6 (`V₀`).

Formalized by `MetaMathlibExt.generalizedBeatty_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#generalized-beatty-zero).

## Generalized Beatty sequence at one

Let $\varphi$ be the golden ratio. For all integers
$p, q, r$, the generalized Beatty sequence $V(p, q, r)(n) = p\lfloor n\varphi \rfloor + qn + r$
takes the value $V(p, q, r)(1) = p + q + r$ at $n = 1$, since $\lfloor \varphi \rfloor = 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 5.

Formalized by `MetaMathlibExt.generalizedBeatty_one`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#generalized-beatty-one).

## Terms of a generalized Beatty sequence

For integers $p$, $q$ and $r$, this is the set of
integers $p \lfloor n\varphi \rfloor + qn + r$ for natural numbers $n \ge 1$, where $\varphi$ is
the golden ratio: the set of terms $V(p, q, r)(n)$, $n \ge 1$, of the generalized Beatty
sequence $V(p, q, r)$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 5.

Formalized by `MetaMathlibExt.beattySet`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#beatty-set).

## Terms of a generalized Beatty sequence from index zero

For integers $p$, $q$ and $r$, this
is the set of integers $p \lfloor n\varphi \rfloor + qn + r$ for all natural numbers $n \ge 0$,
where $\varphi$ is the golden ratio: the set of values $V(p, q, r)(n)$, $n \ge 0$, of the
generalized Beatty sequence $V(p, q, r)$, which the paper denotes $V_0(p, q, r)$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 6 (definition of `V₀`).

Formalized by `MetaMathlibExt.beattySet₀`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#beatty-set-2).

## The value at one is a term of a generalized Beatty sequence

Let $\varphi$ be the golden
ratio. For all integers $p, q, r$, the number $p + q + r$ is a term
$p \lfloor n \varphi \rfloor + q n + r$, $n \ge 1$, of the generalized Beatty sequence
$V(p, q, r)$; it is the term at $n = 1$, since $\lfloor \varphi \rfloor = 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 5.

Formalized by `MetaMathlibExt.add_add_mem_beattySet`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#add-add-mem-beatty-set).

## The initial term of a generalized Beatty set

For all integers $p$, $q$ and $r$, the
integer $r$ belongs to the set $V_0(p, q, r)$ of terms $p \lfloor n\varphi \rfloor + qn + r$,
$n \ge 0$, of the generalized Beatty sequence, where $\varphi$ is the golden ratio; indeed $r$
is its term at $n = 0$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 6.

Formalized by `MetaMathlibExt.mem_beattySet₀_self`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#mem-beatty-set-self).

## The blocks $10^{2m} \cdot 1$ and $10^{2m+1} \cdot 0$ never occur

For every $m \ge 1$, no
base phi expansion of a natural number has digits
$d_{2m} \cdots d_0 \cdot d_{-1} = 10^{2m} \cdot 1$, and none has digits
$d_{2m+1} \cdots d_0 \cdot d_{-1} = 10^{2m+1} \cdot 0$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 1.

Stated but not proved: `MetaMathlibExt.basePhi_no_block_one_zeros_dot` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-no-block-one-zeros-dot).

## Propagation principle for base phi expansions

Let $w = w_1 \cdots w_8$ be a word of
length $8$ over the natural numbers. Say that a base phi expansion $S$ (the set of positions of its
digits $1$) contains $w$ centrally if for each $j = 1, \dots, 8$ the position $4 - j$ lies in $S$
exactly when $w_j = 1$, that is, if its digits $d_3 d_2 d_1 d_0 \cdot d_{-1} d_{-2} d_{-3} d_{-4}$
spell $w$. If no base phi expansion of any natural number $N \le 17$ contains $w$ centrally, then
no base phi expansion of any natural number contains $w$ centrally.

The hypothesis includes $N = 0$, as in the paper's proof.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 2 (a).

Stated but not proved: `MetaMathlibExt.basePhi_propagation_principle` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-propagation-principle).

## Generalized Beatty sequences composed with the Wythoff sequences

Let $\varphi$ be the
golden ratio and, for integers $a$, $b$, $c$ and natural numbers $n$, let
$V(a, b, c)(n) = a \lfloor n\varphi \rfloor + bn + c$. Let $A(n) = \lfloor n\varphi \rfloor$ and
$B(n) = \lfloor n\varphi \rfloor + n$ be the lower and upper Wythoff sequences. For all integers
$p$, $q$, $r$ and every natural number $n \ge 1$,
$V(p, q, r)(A(n)) = V(p + q, p, r - p)(n)$ and $V(p, q, r)(B(n)) = V(2p + q, p + q, r)(n)$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 3.

Stated but not proved: `MetaMathlibExt.generalizedBeatty_comp_wythoff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#generalized-beatty-comp-wythoff).

## Complement of the lower Wythoff part of a generalized Beatty sequence

Let $\varphi$ be the
golden ratio and, for integers $a$, $b$, $c$, let $V(a, b, c)$ be the set of integers
$a \lfloor n\varphi \rfloor + bn + c$ for natural numbers $n \ge 1$. Let $p$, $q$, $r$ be
integers with $p + q > 0$ and $2p + q > 0$. If $U$ and $W$ are disjoint sets of integers with
$U \cup W = V(p, q, r)$ and $U = V(p + q, p, r - p)$, then $W = V(2p + q, p + q, r)$.

This is the converse of the composition lemma. The hypotheses $p + q > 0$ and $2p + q > 0$ say
that the sequence $n \mapsto p \lfloor n\varphi \rfloor + qn + r$ is increasing, as the paper's
sequences are.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 4.

Stated but not proved: `MetaMathlibExt.beattySet_complement_of_lowerWythoff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#beatty-set-complement-of-lower-wythoff).

## First differences of a generalized Beatty sequence

Let $\varphi$ be the golden ratio, for
integers $p, q, r$ let $V(p, q, r)$ be the sequence $n \mapsto p\lfloor n\varphi \rfloor + qn + r$
on the natural numbers, and let $x_0 x_1 x_2 \cdots$ be the infinite Fibonacci word. For all
integers $p, q, r$ and every $n \ge 1$, the difference $V(p, q, r)(n+1) - V(p, q, r)(n)$ equals
$p + q$ if $x_{n-1} = 1$ and $2p + q$ if $x_{n-1} = 0$. Conversely, for all integers $a, b$ and
every sequence $v$ of integers indexed by the natural numbers such that, for every $n \ge 1$,
$v(n+1) - v(n)$ equals $b$ if $x_{n-1} = 1$ and $a$ if $x_{n-1} = 0$, there is an integer $r'$
with $v(n) = V(a - b, 2b - a, r')(n)$ for every $n \ge 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 5.

Stated but not proved: `MetaMathlibExt.generalizedBeatty_diff_eq_fibInf` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#generalized-beatty-diff-eq-fib-inf).

## For $m \ge 2$, no base phi expansion has end block $1\,0^{2m}\,1$

Let $m \ge 2$, let $N$
be a natural number and let $S$ be a base phi expansion of $N$, given as the set of positions of
its digits $1$. Then the digits $d_{2m+1} d_{2m} \cdots d_1 d_0$ at positions $2m+1, \dots, 0$ are
not $1\,0^{2m}\,1$: it is not the case that $2m+1 \in S$, $0 \in S$ and no $i$ with
$1 \le i \le 2m$ lies in $S$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 6.

Stated but not proved: `MetaMathlibExt.basePhi_no_end_block_one_zeros_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-no-end-block-one-zeros-one).

## End blocks $u1 \cdot 0$ and $u0 \cdot 0$ of consecutive numbers

Let $u$ be a nonempty
word of length $m - 1$, read as the digits $d_{m-1} \cdots d_1$ (a letter $1$ is a digit $1$,
any other letter a digit $0$), such that the word $u1$ has no two adjacent letters $1$. Then
for every $N \ge 1$, some base phi expansion of $N$ has digits
$d_{m-1} \cdots d_1 d_0 \cdot d_{-1} = u1 \cdot 0$ if and only if some base phi expansion of
$N - 1$ has digits $d_{m-1} \cdots d_1 d_0 \cdot d_{-1} = u0 \cdot 0$.

The hypothesis that $u1$ has no $11$ is the paper's implicit standing assumption on digit blocks:
for $u = 1$ the block $11 \cdot 0$ never occurs, while $10 \cdot 0$ occurs in the expansion
$10 \cdot 01$ of $2$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 7.

Stated but not proved: `MetaMathlibExt.basePhi_end_block_one_iff_pred` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-end-block-one-iff-pred).

## Lucas numbers from Fibonacci numbers

For every natural number $n$,
$F_n + 3F_{n+1} = L_{n+2}$, where $F_j$ is the $j$-th Fibonacci number ($F_0 = 0$, $F_1 = 1$) and
$L_j$ is the $j$-th Lucas number ($L_0 = 2$, $L_1 = 1$).

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 9.

Stated but not proved: `MetaMathlibExt.fib_add_three_mul_fib_succ_eq_lucasNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#fib-add-three-mul-fib-succ-eq-lucas-numb).

## Border words and codes of Lucas numbers

Let $n \ge 1$, and write $F_k$ for the Fibonacci
numbers and $L_k$ for the Lucas numbers. Let $S_1, S_2, S_3, S_4$ be base phi expansions (sets
of positions of the digits $1$) of $L_{2n}$, $L_{2n+1}$, $L_{2n+1} + 1$ and $L_{2n+2} - 1$
respectively, and let $S_k^-$ be the set of negative positions in $S_k$. Then
$S_1^- = \{-2n\}$, $S_2^- = \{-2j : 1 \le j \le n\}$,
$S_3^- = \{-2n-2\} \cup \{1 - 2j : 1 \le j \le n\}$ and $S_4^- = \{-2n-2\}$; that is, the
negative parts $\beta^-$ of these numbers are the words $0^{2n-2}01$, $(01)^n$, $(10)^n 01$ and
$0^{2n}01$. Moreover $\sum_{i \in S_1^-} F_{i+2n} = 0$,
$\sum_{i \in S_2^-} F_{i+2n} = F_{2n-1} - 1$, $\sum_{i \in S_3^-} F_{i+2n+2} = F_{2n+2} - 1$
and $\sum_{i \in S_4^-} F_{i+2n+2} = 0$.

In the paper's notation, with $\gamma^-(N)$ the word $\beta^-(N)$ with its final $01$ removed,
this says $\gamma^-(L_{2n}) = 0^{2n-2}$, $\gamma^-(L_{2n+1}) = (01)^{n-1}$,
$\gamma^-(L_{2n+1}+1) = (10)^n$ and $\gamma^-(L_{2n+2}-1) = 0^{2n}$, and that the codes $C(N)$
of the words $\gamma^-(N)$, which equal $\sum_{i \in \beta^-(N)} F_{i+2j}$ when $\beta^-(N)$
has length $2j$, are $C(L_{2n}) = 0$, $C(L_{2n+1}) = F_{2n-1} - 1$,
$C(L_{2n+1}+1) = F_{2n+2} - 1$ and $C(L_{2n+2}-1) = 0$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 10.

Stated but not proved: `MetaMathlibExt.basePhi_lucas_border_codes` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-lucas-border-codes).

## The digit blocks $10 \cdot 1$ and $00 \cdot 1$ around the radix point

Let $\varphi$ be the
golden ratio, let $N \ge 1$ and let $S$ be a base phi expansion of $N$, with digits $d_i$
($d_i = 1$ if $i \in S$, else $d_i = 0$). Then $d_1 d_0 \cdot d_{-1} \ne 10 \cdot 1$, and
$d_1 d_0 \cdot d_{-1} = 00 \cdot 1$ if and only if $N = 3 \lfloor n \varphi \rfloor + n + 1$ for
some integer $n \ge 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Proposition 1.

Stated but not proved: `MetaMathlibExt.basePhi_digits_dot_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-digits-dot-one).

## End blocks of length at most three ending in $0$

Let $\varphi$ be the golden ratio.
For integers $p, q, r$ let $V(p, q, r) = \{p \lfloor n\varphi \rfloor + qn + r : n \ge 1\}$ and
$V_0(p, q, r) = \{p \lfloor n\varphi \rfloor + qn + r : n \ge 0\}$. For a word $w$ of length $\ell$
let $R_w$ be the set of natural numbers having a base phi expansion whose digits
$d_{\ell-1} \cdots d_0$ at positions $\ell - 1, \dots, 0$ spell $w$. Then for every natural number
$N \ge 1$: $N \in R_0$ if and only if $N \in V(-1, 3, 0)$; $N \in R_{00}$ if and only if
$N \in V_0(1, 2, 0) \cup V(3, 1, 1)$; $N \in R_{10}$ if and only if $N \in V(1, 2, -1)$;
$N \in R_{010}$ if and only if $N \in V(1, 2, -1)$; $N \in R_{000}$ if and only if
$N \in V_0(4, 3, 0) \cup V(3, 1, 1)$; and $N \in R_{100}$ if and only if $N \in V(3, 1, -1)$.
Moreover $V_0(1, 2, 0)$ and $V_0(4, 3, 0)$ are each disjoint from $V(3, 1, 1)$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Proposition 2.

Stated but not proved: `MetaMathlibExt.basePhi_short_end_blocks_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-short-end-blocks-zero).

## Short prefixes of the negative parts of base phi expansions

Let $\varphi$ be the golden
ratio. For integers $p, q, r$ let $V(p, q, r) = \{p \lfloor n\varphi \rfloor + qn + r : n \ge 1\}$
and $V_0(p, q, r) = \{p \lfloor n\varphi \rfloor + qn + r : n \ge 0\}$. For a word $w$ of length
$\ell$ let $R_{\cdot w}$ be the set of natural numbers having a base phi expansion whose digits
$d_{-1} d_{-2} \cdots d_{-\ell}$ spell $w$, where $d_i = 1$ if position $i$ carries a digit $1$
and $d_i = 0$ otherwise. Then for every natural number $N \ge 2$:
$N \in R_{\cdot 0}$ if and only if $N \in V(1, 2, -1) \cup V(1, 2, 0) \cup V(1, 2, 1)$;
$N \in R_{\cdot 1}$ if and only if $N \in V(3, 1, 1)$;
$N \in R_{\cdot 10}$ if and only if $N \in V(3, 1, 1)$;
$N \in R_{\cdot 00}$ if and only if $N \in V(3, 1, 2) \cup V(3, 1, 3) \cup V(3, 1, 4)$;
$N \in R_{\cdot 01}$ if and only if $N \in V_0(4, 3, 2) \cup V_0(4, 3, 3) \cup V_0(4, 3, 4)$;
$N \in R_{\cdot 010}$ if and only if $N \in V_0(4, 3, 2) \cup V_0(4, 3, 3) \cup V_0(4, 3, 4)$;
$N \in R_{\cdot 000}$ if and only if $N \in V(4, 3, -1) \cup V(4, 3, 0) \cup V(4, 3, 1)$;
$N \in R_{\cdot 001}$ if and only if $N \in V(7, 4, 2) \cup V(7, 4, 3) \cup V(7, 4, 4)$;
$N \in R_{\cdot 100}$ if and only if $N \in V(4, 3, -2)$; and
$N \in R_{\cdot 101}$ if and only if $N \in V(7, 4, 1)$.

The bound $N \ge 2$ makes the negative part nonempty: the expansion of $1$ is $1$ itself. The first
equivalence follows the reading $R_{\cdot 0} = V(1, 2, [-1, 0, 1])$ of the paper's Figure 3: as
printed, $V(2, 1, -1) \cup V(2, 1, 0) \cup V(2, 1, 1)$ misses $6$, whose expansion is
$1010 \cdot 0001$, and contains $12$, whose expansion is $100000 \cdot 101001$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Proposition 3.

Stated but not proved: `MetaMathlibExt.basePhi_short_negative_prefixes` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-short-negative-prefixes).

## Embedding of base phi expansions into Zeckendorf expansions

Let $\varphi$ be the golden
ratio and let $F_j$ be the Fibonacci numbers, $F_0 = 0$, $F_1 = F_2 = 1$. For a natural number $M$
let $Z(M)$ be the set of indices $i \ge 0$ such that $F_{i+2}$ occurs in the Zeckendorf
representation of $M$, so that $M = \sum_{i \in Z(M)} F_{i+2}$. Let $N$ be a natural number, let
$S$ be a base phi expansion of $N$ (the set of positions of its digits $1$), and let $s(N)$ be the
number of integers $n$ with $1 \le n \le N$ and $3 \lfloor n \varphi \rfloor + n + 1 < N$. Then
$\{i \in S : i \ge 0\} = Z(N + s(N))$.

Since $3 \lfloor n \varphi \rfloor + n + 1 > N$ for $n \ge N$, $s(N)$ is the number of all $n \ge 1$
with $3 \lfloor n \varphi \rfloor + n + 1 < N$, that is, the number of $M < N$ whose digit at
position $-1$ is $1$, as in the paper's proof. Both formulas for $s(N)$ printed in the paper are off
by one: $\max\{k : 3 \lfloor k \varphi \rfloor + k \le N\}$ gives $s(4) = 1$, but $Z(5) = \{3\}$
while $4 = \varphi^2 + 1 + \varphi^{-2}$ has nonnegative positions $\{0, 2\}$; and
$\max\{k : 3 \lfloor k \varphi \rfloor + k + 1 \le N\} - 1$ gives $s(6) = 0$, but
$Z(6) = \{0, 3\}$ while $6 = \varphi^3 + \varphi + \varphi^{-4}$ has nonnegative positions
$\{1, 3\}$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 1.

Stated but not proved: `MetaMathlibExt.basePhi_positive_part_eq_zeckendorf` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-positive-part-eq-zeckendorf).

## Recursive structure theorem for base phi expansions, part (A)

Let $n \ge 2$ and let $L_j$
be the Lucas numbers; $k$ denotes a natural number, and base phi expansions are given as sets of
positions of digits $1$.
(I) If $1 \le k \le L_{2n-2} - 1$, $T$ is a base phi expansion of $L_{2n-1} + k$ and $S$ is a base
phi expansion of $L_{2n+1} + k$, then $2n-1 \in T$, $2n-2 \notin T$, $1-2n \notin T$, $-2n \in T$
and $S = (T \setminus \{2n-1, -2n\}) \cup \{2n+1, 1-2n, -2n-2\}$.
(K) If $1 \le k \le L_{2n-2} - 1$, $T$ is a base phi expansion of $L_{2n-1} + k$ and $S$ is a base
phi expansion of $L_{2n+1} + L_{2n-1} + k$, then $2n-1 \in T$, $2n-2 \notin T$, $1-2n \notin T$,
$-2n \in T$ and $S = (T \setminus \{-2n\}) \cup \{2n+1, -2n-2\}$.
(J) If $0 \le k \le L_{2n-3}$, $T$ is a base phi expansion of $L_{2n-2} + k$ and $S$ is a base phi
expansion of $L_{2n+1} + L_{2n-2} + k$, then $2n-2 \in T$, $2n-3 \notin T$, $3-2n \notin T$,
$2-2n \in T$ and $S = (T \setminus \{2-2n\}) \cup \{2n+1, 1-2n, -2n-2\}$.

In the paper's word notation, where $\beta(M)$ is the expansion of $M$ written as a word of digits
(with $\cdot$ between positions $0$ and $-1$) and $(10)^{-1}$, $(01)^{-1}$ cancel a leading $10$
and a trailing $01$, these are
$\beta(L_{2n+1}+k) = 1000\,(10)^{-1}\,\beta(L_{2n-1}+k)\,(01)^{-1}\,1001$,
$\beta(L_{2n+1}+L_{2n-1}+k) = 1010\,(10)^{-1}\,\beta(L_{2n-1}+k)\,(01)^{-1}\,0001$ and
$\beta(L_{2n+1}+L_{2n-2}+k) = 10010\,(10)^{-1}\,\beta(L_{2n-2}+k)\,(01)^{-1}\,001001$. The
source's ranges $k \le L_{2n} - 1$ for (I) and (K) and $k \le L_{2n-1}$ for (J) are too wide: for
$n = 2$ and $k = 3$, $\beta(L_3 + 3) = \beta(7) = 10000 \cdot 0001$ has no digit $1$ at
position $3$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 2.

Stated but not proved: `MetaMathlibExt.basePhi_recursive_structure` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-recursive-structure).

## Recursive structure of base phi expansions on Lucas intervals

Let $n \ge 1$, let $L_k$ be
the Lucas numbers, and for $j \ge 0$ let $\Lambda_{2j}$ be the set of natural numbers in
$[L_{2j}, L_{2j+1}]$ and $\Lambda_{2j+1}$ the set of natural numbers in
$[L_{2j+1} + 1, L_{2j+2} - 1]$. Let $T$ be a base phi expansion of a natural number $M$ and $S$ a
base phi expansion of a natural number $N$, both given as sets of positions of digits $1$. Then:
(A)(a) if $M \in \Lambda_{2n-1}$ and $N = M + L_{2n}$, then $2n-1 \in T$, $2n-2 \notin T$,
$1-2n \notin T$, $-2n \in T$ and $S = (T \setminus \{2n-1, -2n\}) \cup \{2n+1, 1-2n, -2n-2\}$;
(A)(b) if $M \in \Lambda_{2n-2}$ and $N = M + L_{2n+1}$, then $3-2n \notin T$, $2-2n \in T$ and
$S = (T \setminus \{2-2n\}) \cup \{2n+1, 1-2n, -2n-2\}$;
(A)(c) if $M \in \Lambda_{2n-1}$ and $N = M + L_{2n+1}$, then $2n-1 \in T$, $1-2n \notin T$,
$-2n \in T$ and $S = (T \setminus \{-2n\}) \cup \{2n+1, -2n-2\}$;
(B)(a) if $M \in \Lambda_{2n}$ and $N = M + L_{2n+1}$, then $2n \in T$, $2n-1 \notin T$,
$1-2n \notin T$, $-2n \in T$ and $S = (T \setminus \{2n, -2n\}) \cup \{2n+2, -2n-2\}$;
(B)(b) if $M \in \Lambda_{2n-1}$ and $N = M + L_{2n+2}$, then $S = T \cup \{2n+2, -2n-2\}$;
(B)(c) if $M \in \Lambda_{2n}$ and $N = M + L_{2n+2}$, then $S = T \cup \{2n+2, -2n-2\}$.

In the paper's word notation, where $\beta(M)$ is the expansion of $M$ written as a word of digits
(with $\cdot$ between positions $0$ and $-1$) and $(10)^{-1}$, $(01)^{-1}$ cancel a leading $10$
and a trailing $01$, (A)(a) is
$\beta(M + L_{2n}) = 1000\,(10)^{-1}\,\beta(M)\,(01)^{-1}\,1001$ and (B)(b) is
$\beta(M + L_{2n+2}) = 100\,\beta(M)\,01$; the digit conditions on $T$ make the cancellations
$(10)^{-1}$ and $(01)^{-1}$ valid. In (B)(c) the source writes $\beta(N - L_{2n+1})$ for
$N \in \Lambda_{2n} + L_{2n+2}$; the shift $L_{2n+2}$ is used here, since as printed $n = 1$ and
$N = 10$ give $10\,\beta(6)\,01 = 101010 \cdot 000101$, which is not $\beta(10) = 10100 \cdot 0101$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 3.

Stated but not proved: `MetaMathlibExt.basePhi_recursive_structure_lucas_intervals` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-recursive-structure-lucas-inter).

## Short end blocks

Let $\varphi$ be the golden ratio. For integers $p, q, r$ let
$V(p, q, r)$ be the set of the integers $p \lfloor n\varphi \rfloor + qn + r$ with $n \ge 1$, and
$V_0(p, q, r)$ the same set with $n \ge 0$. Then for every natural number $N \ge 1$:
some base phi expansion of $N$ has digit $1$ at position $0$ if and only if
$N \in V_0(1, 2, 1)$; some base phi expansion of $N$ has digits $1, 0$ at positions $1, 0$ if
and only if $N \in V(1, 2, -1)$; some base phi expansion of $N$ has digits $0, 0, 0$ at
positions $1, 0, -1$ if and only if $N \in V_0(1, 2, 0)$; and some base phi expansion of $N$
has digits $0, 0, 1$ at positions $1, 0, -1$ if and only if $N \in V(3, 1, 1)$.

In the paper's notation: $R_1 = V_0(1, 2, 1)$, $R_{10} = V(1, 2, -1)$,
$R_{00 \cdot 0} = V_0(1, 2, 0)$ and $R_{00 \cdot 1} = V(3, 1, 1)$, on the numbers $N \ge 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 6.

Stated but not proved: `MetaMathlibExt.basePhi_short_end_blocks` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-short-end-blocks).

## End blocks ending in $0$ are Lucas–Wythoff sequences

Let $\varphi$ be the golden ratio
and $L_n$ the Lucas numbers. For integers $p, q, r$ let $V(p, q, r)$ be the set of the integers
$p \lfloor n\varphi \rfloor + qn + r$ with $n \ge 1$, and $V_0(p, q, r)$ the same set with
$n \ge 0$. For a word $w = w_{m-1} \cdots w_0$ of length $m$ over the natural numbers, let $R_w$ be
the set of natural numbers $N$ with a base phi expansion whose digit at position $i$ is $1$
exactly when $w_i = 1$, for $i = m - 1, \dots, 0$. Then:
(1) for every word $w = w_{m-1} \cdots w_0$ of length $m \ge 2$ with letters in $\{0, 1\}$, no two
consecutive letters $1$, $w_0 = 0$ and $w \ne 0^m$, there is an integer $\gamma \le 0$ such that
every natural number $N \ge 1$ lies in $R_w$ if and only if it lies in
$V(L_{m-2}, L_{m-3}, \gamma)$ when $w_{m-1} = 0$, respectively in $V(L_{m-1}, L_{m-2}, \gamma)$
when $w_{m-1} = 1$;
(2) for every $m \ge 1$ and every natural number $N \ge 1$, $N \in R_{0^{2m}}$ if and only if
$N \in V(L_{2m}, L_{2m-1}, 1) \cup V_0(L_{2m-1}, L_{2m-2}, 0)$, and $N \in R_{0^{2m+1}}$ if and
only if $N \in V_0(L_{2m+1}, L_{2m}, 0) \cup V(L_{2m}, L_{2m-1}, 1)$; moreover
$V(L_{2m}, L_{2m-1}, 1)$ and $V_0(L_{2m-1}, L_{2m-2}, 0)$ are disjoint, and
$V_0(L_{2m+1}, L_{2m}, 0)$ and $V(L_{2m}, L_{2m-1}, 1)$ are disjoint.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 7.

Stated but not proved: `MetaMathlibExt.basePhi_end_blocks_lucasWythoff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-end-blocks-lucas-wythoff).

## End blocks ending in $1$ are Lucas–Wythoff sequences

Let $\varphi$ be the golden ratio
and $L_n$ the Lucas numbers. For integers $p, q, r$ let $V(p, q, r)$ be the set of the integers
$p \lfloor n\varphi \rfloor + qn + r$ with $n \ge 1$, and $V_0(p, q, r)$ the same set with
$n \ge 0$. For a word $w = w_{m-1} \cdots w_0$ of length $m$ over the natural numbers, let $R_w$ be
the set of natural numbers $N$ with a base phi expansion whose digit at position $i$ is $1$
exactly when $w_i = 1$, for $i = m - 1, \dots, 0$. Then:
(1) for every word $w = w_{m-1} \cdots w_0$ of length $m \ge 3$ with letters in $\{0, 1\}$, no two
consecutive letters $1$ and $w_0 = 1$, which is not of the form $0^k 1$ or $1 0^k 1$ with
$k \ge 2$, and for which $R_w$ is nonempty, there is an integer $\gamma \le 0$ such that every
natural number $N \ge 1$ lies in $R_w$ if and only if it lies in $V(L_{m-2}, L_{m-3}, \gamma)$
when $w_{m-1} = 0$, respectively in $V(L_{m-1}, L_{m-2}, \gamma)$ when $w_{m-1} = 1$;
(2) for every $m \ge 1$ and every natural number $N \ge 1$: $N \in R_{0^{2m} 1}$ if and only if
$N \in V_0(L_{2m+1}, L_{2m}, 1)$; $N \in R_{0^{2m+1} 1}$ if and only if
$N \in V_0(L_{2m+1}, L_{2m}, 1)$; $N \notin R_{1 0^{2m} 1}$; and $N \in R_{1 0^{2m+1} 1}$ if and
only if $N \in V(L_{2m+2}, L_{2m+1}, 1 - L_{2m+1})$.

The hypothesis that $R_w$ is nonempty is added to the printed statement: as printed, the
statement fails for $w = 01001$, which never occurs (its end block $1001$ is excluded), while
every $V(p, q, \gamma)$ is nonempty; the source's proof derives its description of $R_w$ only
under the assumption $R_w \ne \emptyset$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 8.

Stated but not proved: `MetaMathlibExt.basePhi_end_blocks_one_lucasWythoff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-end-blocks-one-lucas-wythoff).

## Every even-length Zeckendorf word ending in $1$ is a negative part

Let $n \ge 1$ and let
$T$ be a finite set of integers with $T \subseteq [-2n, -1]$ and $-2n \in T$ that contains no
two consecutive integers. Then there are a natural number $N$ and a base phi expansion $S$ of $N$
(the set of positions of its digits $1$) with $\{i \in S : i < 0\} = T$. In words, every
Zeckendorf word of even length $2n \ge 2$ ending in $1$ is the negative part $\beta^-(N)$ of
some $N$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 9.

Stated but not proved: `MetaMathlibExt.basePhi_negative_parts_surject` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-negative-parts-surject).

## Recursive structure of the negative parts of base phi expansions

Let $n \ge 1$, let $L_k$
be the Lucas numbers, and for $j \ge 0$ let $\Lambda_{2j}$ be the set of natural numbers in
$[L_{2j}, L_{2j+1}]$ and $\Lambda_{2j+1}$ the set of natural numbers in
$[L_{2j+1} + 1, L_{2j+2} - 1]$. Let $T$ be a base phi expansion of a natural number $M$ and $S$ a
base phi expansion of a natural number $N$, both given as sets of positions of digits $1$. Write
$S^- = \{i \in S : i < 0\}$ and, for an integer $a$, $T_a = \{i \in T : a \le i < 0\}$. Then:
(A)(a) if $M \in \Lambda_{2n-1}$ and $N = M + L_{2n}$, then $S^- = T_{2-2n} \cup \{1-2n, -2n-2\}$;
(A)(b) if $M \in \Lambda_{2n-2}$ and $N = M + L_{2n+1}$, then $S^- = T_{4-2n} \cup \{1-2n, -2n-2\}$;
(A)(c) if $M \in \Lambda_{2n-1}$ and $N = M + L_{2n+1}$, then $S^- = T_{2-2n} \cup \{-2n-2\}$;
(B)(a) if $M \in \Lambda_{2n}$ and $N = M + L_{2n+1}$, then $S^- = T_{2-2n} \cup \{-2n-2\}$;
(B)(b) if $M \in \Lambda_{2n-1}$ and $N = M + L_{2n+2}$, then $S^- = T_{2-2n} \cup \{-2n, -2n-2\}$;
(B)(c) if $M \in \Lambda_{2n}$ and $N = M + L_{2n+2}$, then $S^- = T_{2-2n} \cup \{-2n, -2n-2\}$.

These are the paper's identities for the words $\gamma^-(N)$, the negative part of the expansion of
$N$ with its final digits $01$ removed; for example (A)(a) is
$\gamma^-(M + L_{2n}) = \gamma^-(M)\,10$. In (B)(c) the source writes $\gamma^-(N - L_{2n+1})$ for
$N \in \Lambda_{2n} + L_{2n+2}$; the shift $L_{2n+2}$ is used here, since as printed $n = 1$ and
$N = 10$ give $\gamma^-(6)\,01 = 0001$ while $\gamma^-(10) = 01$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 10.

Stated but not proved: `MetaMathlibExt.basePhi_recursive_structure_gamma` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 534](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-recursive-structure-gamma).

## The codes of the negative parts follow an orbit of addition modulo a Fibonacci number

Let $n \ge 1$, write $F_k$ for the Fibonacci numbers and $L_k$ for the Lucas numbers, and let
$c$ be a function from the natural numbers to the natural numbers such that
$c(N) = \sum_{i \in S,\, i < 0} F_{i+2n}$ (with $F_k$ read as $0$ for $k < 0$) whenever $S$ is a
base phi expansion of $N$. List the values $c(N)$ for $N = L_{2n-1} + 1, \dots, L_{2n+1}$ (the
interval $\Xi_n$) in increasing order of $N$, and merge every run of equal consecutive values
into a single entry. The resulting list is $(F_{2n} - 1 + j F_{2n-2}) \bmod F_{2n}$ for
$j = 0, 1, \dots, F_{2n} - 1$: the orbit of $F_{2n} - 1$ under addition of $F_{2n-2}$ in
$\mathbb{Z}/F_{2n}\mathbb{Z}$.

Here $c(N)$ is the paper's code $C(N)$ of the negative part $\beta^-(N)$ (the digits of $N$ at
negative positions), and the merged runs are its tridents.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 11.

Stated but not proved: `MetaMathlibExt.basePhi_negative_part_order_orbit` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 568](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-negative-part-order-orbit).

## Left end of a Lucas interval

Let $L_0 = 2$, $L_1 = 1$, $L_{j+2} = L_{j+1} + L_j$ be the
Lucas numbers, and let the Lucas intervals be $\Lambda_{2n} = [L_{2n}, L_{2n+1}]$ and
$\Lambda_{2n+1} = [L_{2n+1} + 1, L_{2n+2} - 1]$. The left end of $\Lambda_m$ is $L_m$ when $m$
is even and $L_m + 1$ when $m$ is odd.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 3 (Lucas intervals).

Formalized by `MetaMathlibExt.lucasIntervalLo`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#lucas-interval-lo).

## Right end of a Lucas interval

Let $L_0 = 2$, $L_1 = 1$, $L_{j+2} = L_{j+1} + L_j$ be the
Lucas numbers, and let the Lucas intervals be $\Lambda_{2n} = [L_{2n}, L_{2n+1}]$ and
$\Lambda_{2n+1} = [L_{2n+1} + 1, L_{2n+2} - 1]$. The right end of $\Lambda_m$ is $L_{m+1}$ when
$m$ is even and $L_{m+1} - 1$ when $m$ is odd.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 3 (Lucas intervals).

Formalized by `MetaMathlibExt.lucasIntervalHi`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#lucas-interval-hi).

## Endpoints of the Lucas interval $\Lambda_3$

The Lucas interval $\Lambda_3$ has left end
$5$ and right end $6$, that is, $\Lambda_3 = [5, 6]$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 3.

Formalized by `MetaMathlibExt.lucasInterval_three`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#lucas-interval-three).

## Endpoints of the Lucas interval $\Lambda_4$

The Lucas interval $\Lambda_4$ has left end
$7$ and right end $11$, that is, $\Lambda_4 = [7, 11]$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 3.

Formalized by `MetaMathlibExt.lucasInterval_four`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 601](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L601). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#lucas-interval-four).

## Endpoints of the Lucas interval $\Lambda_5$

The Lucas interval $\Lambda_5$ has left end
$12$ and right end $17$, that is, $\Lambda_5 = [12, 17]$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 3.

Formalized by `MetaMathlibExt.lucasInterval_five`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#lucas-interval-five).

## Lucas tilings

Write $\Lambda_k = [\ell_k, h_k]$ for the Lucas interval with left end
$\ell_k$ and right end $h_k$. For natural numbers $a$, $b$ and a list $P$ of pairs $(k, t)$ of
natural numbers, $P$ is a Lucas tiling of $[a, b]$ when the translated Lucas intervals
$\Lambda_k + t$, $(k, t) \in P$, taken in the order of $P$, are adjacent and their union is
$[a, b]$. Precisely, it is defined by recursion on $P$: the empty list is a Lucas tiling of
$[a, b]$ exactly when $a = b + 1$, and the list consisting of $(k, t)$ followed by $P$ is a Lucas
tiling of $[a, b]$ exactly when $\ell_k + t = a$ and $P$ is a Lucas tiling of $[h_k + t + 1, b]$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4 ("a union of adjacent translations" of Lucas intervals).

Formalized by `MetaMathlibExt.IsLucasTiling`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 616](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L616). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-lucas-tiling).

## Lucas tilings by the empty list

For all natural numbers $a$ and $b$, the empty list is a
Lucas tiling of $[a, b]$ if and only if $a = b + 1$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4.

Formalized by `MetaMathlibExt.isLucasTiling_nil`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 624](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-lucas-tiling-nil).

## Lucas tilings of a list with a first interval

Write $\Lambda_k = [\ell_k, h_k]$ for the
Lucas interval with left end $\ell_k$ and right end $h_k$. For all natural numbers $a$, $b$, $k$,
$t$ and every list $P$ of pairs of natural numbers, the list consisting of $(k, t)$ followed by
$P$ is a Lucas tiling of $[a, b]$ if and only if $\ell_k + t = a$ and $P$ is a Lucas tiling of
$[h_k + t + 1, b]$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4.

Formalized by `MetaMathlibExt.isLucasTiling_cons`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#is-lucas-tiling-cons).

## Canonical splitting of a Lucas interval

Let $L_j$ be the $j$-th Lucas number
($L_0 = 2$, $L_1 = 1$, $L_{j+2} = L_{j+1} + L_j$). For a natural number $m$, the canonical
splitting of the Lucas interval $\Lambda_m$ is the list of pairs $(k, t)$ of natural numbers
defined by recursion on $m$: for $m \le 5$ it is the one-pair list $[(m, 0)]$, and for $m \ge 6$
it is the concatenation, in this order, of the canonical splitting of $\Lambda_{m-2}$ with
$L_{m-1}$ added to the second coordinate of each pair, the canonical splitting of
$\Lambda_{m-3}$ with $L_m$ added to the second coordinate of each pair, and the canonical
splitting of $\Lambda_{m-2}$ with $L_m$ added to the second coordinate of each pair.

Here $\Lambda_{2n} = [L_{2n}, L_{2n+1}]$ and $\Lambda_{2n+1} = [L_{2n+1} + 1, L_{2n+2} - 1]$, and a
pair $(k, t)$ stands for the translate $\Lambda_k + t$. The recursion follows the second
Recursive Structure Theorem
$\Lambda_m = (\Lambda_{m-2} + L_{m-1}) \cup (\Lambda_{m-3} + L_m) \cup (\Lambda_{m-2} + L_m)$
(the paper's splittings of $\Lambda_6, \Lambda_7, \Lambda_8$, "continuing in this fashion").
That for $m \ge 3$ the result splits $\Lambda_m$ into adjacent translates of $\Lambda_3$,
$\Lambda_4$ and $\Lambda_5$ is the paper's Theorem 4. Only $m \ge 3$ is used.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4 (canonical splitting).

Formalized by `MetaMathlibExt.canonicalLucasSplitting`, a definition declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#canonical-lucas-splitting).

## Canonical splitting of a short Lucas interval

For every natural number $m < 6$, the
canonical splitting of the Lucas interval $\Lambda_m$ is the one-pair list $[(m, 0)]$, that is,
$\Lambda_m$ itself.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4.

Formalized by `MetaMathlibExt.canonicalLucasSplitting_of_lt_six`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 655](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L655). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#canonical-lucas-splitting-of-lt-six).

## Recursion for the canonical splitting

For every natural number $m$, the canonical
splitting of the Lucas interval $\Lambda_{m+6}$ is the concatenation, in this order, of the
canonical splitting of $\Lambda_{m+4}$ with $L_{m+5}$ added to the second coordinate of each
pair, the canonical splitting of $\Lambda_{m+3}$ with $L_{m+6}$ added to the second coordinate of
each pair, and the canonical splitting of $\Lambda_{m+4}$ with $L_{m+6}$ added to the second
coordinate of each pair, where $L_j$ is the $j$-th Lucas number.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4.

Formalized by `MetaMathlibExt.canonicalLucasSplitting_add_six`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#canonical-lucas-splitting-add-six).

## Canonical splitting of the sixth Lucas interval

The canonical splitting of the Lucas
interval $\Lambda_6$ is the list $[(4, 11), (3, 18), (4, 18)]$.

The pairs stand for the translates $\Lambda_4 + L_5$, $\Lambda_3 + L_6$ and $\Lambda_4 + L_6$,
where $L_5 = 11$ and $L_6 = 18$ are Lucas numbers.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Section 4.

Formalized by `MetaMathlibExt.canonicalLucasSplitting_six`, a theorem declared in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 674](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L674). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#canonical-lucas-splitting-six).

## Dekking's Theorem 4: the coding of the canonical splittings of Lucas intervals

Write
$\Lambda_m = [\ell_m, h_m]$ for the Lucas interval with left end $\ell_m$ and right end $h_m$. For
every $n \ge 3$, every pair $(k, t)$ in the canonical splitting of $\Lambda_n$ has
$k \in \{3, 4, 5\}$, and the canonical splitting of $\Lambda_n$ is a Lucas tiling of
$[\ell_n, h_n]$. Let $\kappa$ be the map on finite words of natural numbers that replaces each
letter $3$ by the word $5$, each letter $4$ by $434$ and every other letter by $545$, and let
$C(\Lambda_m)$ be the word formed by the first components $k$ of the pairs $(k, t)$ of the
canonical splitting of $\Lambda_m$, in order. Then for every $n \ge 0$,
$C(\Lambda_{2n+4}) = \kappa^n(4)$ and $C(\Lambda_{2n+5}) = \kappa^n(5)$, where $\kappa^n$ is the
$n$-fold iterate of $\kappa$ applied to the one-letter word.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 4.

Stated but not proved: `MetaMathlibExt.lucasInterval_canonical_splitting_coding` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#lucas-interval-canonical-splitting-codin).

## Canonical splitting and coding of unions of two Lucas intervals

Let $L_m$ denote the
$m$-th Lucas number and $\Lambda_m$ the Lucas interval, so $\Lambda_{2k} = [L_{2k}, L_{2k+1}]$
and $\Lambda_{2k+1} = [L_{2k+1} + 1, L_{2k+2} - 1]$. For $n \ge 2$, let $P_n$ be the canonical
splitting of $\Lambda_{2n-1}$ followed by the canonical splitting of $\Lambda_{2n}$, a list of
translations $\Lambda_k + t$. Then every index $k$ occurring in $P_n$ is $3$, $4$ or $5$, and
the intervals of $P_n$, taken in order, are adjacent with union $[L_{2n-1} + 1, L_{2n+1}]$.
Moreover, for every $n \ge 0$ the list of indices $k$ of $P_{n+2}$ (the coding $C(\Xi_{n+2})$,
where $\Xi_n = \Lambda_{2n-1} \cup \Lambda_{2n}$) equals $\delta(h^n(b))$, where $h$ is the
morphism $a \mapsto aab$, $b \mapsto ab$ on words over $\{a, b\}$ and $\delta$ is the morphism
$a \mapsto 54$, $b \mapsto 34$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 5.

Stated but not proved: `MetaMathlibExt.xi_canonical_splitting_coding` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 708](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#xi-canonical-splitting-coding).

## Trident splitting at an even Lucas number

Let $n \ge 1$ and let $L_{2n}$ be the $2n$-th
Lucas number. If $S_1$, $S_2$ and $S_3$ are base phi expansions of $L_{2n} - 1$, $L_{2n}$ and
$L_{2n} + 1$ respectively, each given as the set of positions of its digits $1$, then the
negative positions $i < 0$ of $S_1$, of $S_2$ and of $S_3$ are the same.

In the paper's terms, the last number $L_{2n} - 1$ of the Lucas interval $\Lambda_{2n-1}$ and the
first two numbers $L_{2n}$, $L_{2n} + 1$ of $\Lambda_{2n}$ form a trident: three consecutive
numbers $N$, $N + 1$, $N + 2$ with $\beta^-(N) = \beta^-(N+1) = \beta^-(N+2)$, where $\beta^-$ is
the negative part of the base phi expansion.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Lemma 8.

Stated but not proved: `MetaMathlibExt.basePhi_trident_splitting` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-trident-splitting).

## The codes of the negative parts follow the golden rotation

Let $n \ge 1$, write $\varphi$
for the golden ratio, $F_k$ for the Fibonacci numbers and $L_k$ for the Lucas numbers, and let
$c$ be a function from the natural numbers to the natural numbers such that
$c(N) = \sum_{i \in S,\, i < 0} F_{i+2n}$ (with $F_k$ read as $0$ for $k < 0$) whenever $S$ is a
base phi expansion of $N$. List the values $c(N)$ for $N = L_{2n-1} + 1, \dots, L_{2n+1}$ (the
interval $\Xi_n$) in increasing order of $N$, and merge every run of equal consecutive values
into a single entry. The resulting list is a permutation of $0, 1, \dots, F_{2n} - 1$, and the
fractional parts $\{(k+1)\varphi\}$ of its entries $k$ strictly decrease along it: if $k$ comes
before $k'$, then $\{(k'+1)\varphi\} < \{(k+1)\varphi\}$.

This list is the paper's permutation $\Pi^\beta_{2n}$ (the codes $C(N)$ of the negative parts
$\beta^-(N)$, tridents merged, as in Theorem 11), and the statement says it is the order in
which the first $F_{2n}$ iterates of the rotation $z \mapsto \exp(2\pi i(z - \varphi))$ occur on
the circle, the entry $k$ standing for the iterate number $k + 1$. This is the reading fixed by
the paper's worked case $n = 3$, where $\Pi^\beta_6 = 7\,2\,5\,0\,3\,6\,1\,4$.

## Sources

- F. Michel Dekking, *The Structure of Base Phi Expansions*, INTEGERS 24 (2024), Article A24, Theorem 12.

Stated but not proved: `MetaMathlibExt.basePhi_negative_part_order_rotation` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean, line 742](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/BasePhiStructureWanted.lean#L742). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html#base-phi-negative-part-order-rotation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Golden ratio base](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/golden-ratio-base)
