---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPermutiple, MetaMathlibExt.permutipleCarry, MetaMathlibExt.permutipleCarry_zero_one, MetaMathlibExt.isPermutiple_87912, MetaMathlibExt.permutipleCarry_relation, MetaMathlibExt.permutipleCarry_le, MetaMathlibExt.permutiple_basePerm_residue_le, MetaMathlibExt.permutipleGraphEdges
statement: formalized
---

# Permutiples

43 results, 28 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html).

## Permutiples with a given digit permutation

Let $n$, $b$ and $d_0, \dots, d_k$ be
natural numbers and let $\sigma$ be a permutation of $\{0, \dots, k\}$. The numeral
$(d_k, \dots, d_0)_b$ is an $(n, b, \sigma)$-permutiple when $d_j < b$ for every $j$ and

$$\sum_{j=0}^k d_j b^j = n \sum_{j=0}^k d_{\sigma(j)} b^j,$$

that is, $(d_k, \dots, d_0)_b = n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Definition 1 (from Holt, *Some general results and open questions on palintiple numbers*).

Formalized by `MetaMathlibExt.IsPermutiple`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-permutiple).

## Carries of a permutiple multiplication

Let $n$, $b$ and $d_0, \dots, d_k$ be
natural numbers and let $\sigma$ be a permutation of $\{0, \dots, k\}$. The carries of the
single-digit multiplication $n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$, where
$(e_k, \dots, e_0)_b$ denotes the base-$b$ numeral $\sum_{j=0}^{k} e_j b^j$, are the
natural numbers $c_0, c_1, c_2, \dots$ defined by $c_0 = 0$,
$c_{j+1} = \lfloor (n d_{\sigma(j)} + c_j) / b \rfloor$ for $0 \le j \le k$, and
$c_{j+1} = 0$ for $j > k$. Division by $b = 0$ is taken to give $0$.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Section 2.

Formalized by `MetaMathlibExt.permutipleCarry`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-carry).

## First two carries of a permutiple multiplication

Let $n$, $b$ and $d_0, \dots, d_k$
be natural numbers, let $\sigma$ be a permutation of $\{0, \dots, k\}$, and write
$(e_k, \dots, e_0)_b$ for the base-$b$ numeral $\sum_{j=0}^{k} e_j b^j$. The carries
$c_0, c_1, \dots$ of the single-digit multiplication
$n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$, defined by $c_0 = 0$ and
$c_{j+1} = \lfloor (n d_{\sigma(j)} + c_j) / b \rfloor$ for $0 \le j \le k$, satisfy
$c_0 = 0$ and $c_1 = \lfloor n d_{\sigma(0)} / b \rfloor$, where division by $b = 0$ is
taken to give $0$.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Section 2.

Formalized by `MetaMathlibExt.permutipleCarry_zero_one`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-carry-zero-one).

## $87912$ is a $(4, 10)$-permutiple by digit reversal

The numeral
$(d_4, d_3, d_2, d_1, d_0)_{10} = 87912$ is a $(4, 10, \sigma)$-permutiple, where $\sigma$ is the
reversal $j \mapsto 4 - j$ of $\{0, \dots, 4\}$; that is, $87912 = 4 \cdot 21978$, and $21978$ has
the digits of $87912$ in reverse order.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Introduction.

Formalized by `MetaMathlibExt.isPermutiple_87912`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-permutiple-87912).

## Carry relation for permutiples

Let $n$ and $b \ge 2$ be natural numbers, let
$\sigma$ be a permutation of $\{0, \dots, k\}$, and let $(d_k, \dots, d_0)_b$ be an
$(n, b, \sigma)$-permutiple, where $(e_k, \dots, e_0)_b$ denotes the base-$b$ numeral
$\sum_{j=0}^{k} e_j b^j$. Let $c_0, c_1, \dots$ be the carries of the multiplication
$n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$. Then for every $0 \le j \le k$,

$$b\, c_{j+1} - c_j = n\, d_{\sigma(j)} - d_j,$$

with both sides computed in the integers.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Theorem 1, quoting Holt's earlier paper; restated as Theorem 1 of Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13.

Stated but not proved: `MetaMathlibExt.permutipleCarry_relation` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-carry-relation).

## Carry bound for permutiples

Let $n$ and $b \ge 2$ be natural numbers, let $\sigma$
be a permutation of $\{0, \dots, k\}$, and let $(d_k, \dots, d_0)_b$ be an
$(n, b, \sigma)$-permutiple, where $(e_k, \dots, e_0)_b$ denotes the base-$b$ numeral
$\sum_{j=0}^{k} e_j b^j$. Let $c_0, c_1, \dots$ be the carries of the multiplication
$n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$. Then for every $0 \le j \le k$ we have
$c_j \le n - 1$ if $n \ge 1$, and $c_j = 0$ if $n = 0$.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Theorem 2, quoting Holt's earlier paper; restated as Theorem 2 of Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13.

Stated but not proved: `MetaMathlibExt.permutipleCarry_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-carry-le).

## Holt's residue condition for rearranged permutiples

Let $n \ge 1$ and $b \ge 2$ be
natural numbers, let $d_0, \dots, d_k$ be natural numbers, and write $(e_k, \dots, e_0)_b$
for the base-$b$ numeral $\sum_{j=0}^{k} e_j b^j$. Let $\sigma$, $\pi$ and $\tau$ be
permutations of $\{0, \dots, k\}$. If $(d_k, \dots, d_0)_b$ is an $(n, b, \sigma)$-permutiple
and $(d_{\pi(k)}, \dots, d_{\pi(0)})_b$ is an $(n, b, \tau)$-permutiple, then for every
$0 \le j \le k$

$$\lambda\bigl(d_j + (b - n)\, d_{\pi(\tau(\pi^{-1}(j)))}\bigr) \le n - 1,$$

where $\lambda(x)$ is the least non-negative residue of the integer $x$ modulo $b$ (the
difference $b - n$ is taken in the integers and may be negative).

The hypothesis $n \ge 1$ is needed: for $n = 0$ the only permutiples have all digits zero
and the bound would read $0 \le -1$.

## Sources

- B. V. Holt, *A Method for Finding All Permutiples with a Fixed Set of Digits from a Single Known Example*, INTEGERS 24 (2024), Article A88, Theorem 3.

Stated but not proved: `MetaMathlibExt.permutiple_basePerm_residue_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-base-perm-residue-le).

## Edge set of the graph of a numeral

Let $b$ be a base, let $d_0, \dots, d_k$ be
natural numbers, the digits of the base-$b$ numeral
$(d_k, \dots, d_0)_b = \sum_{j=0}^{k} d_j b^j$, and let $\sigma$ be a permutation of
$\{0, \dots, k\}$. The graph $G$ of these digits with digit permutation $\sigma$ has edge set

$$E = \{(d_j, d_{\sigma(j)}) : 0 \le j \le k\},$$

a finite set of ordered pairs of natural numbers; it does not depend on $b$.

The vertices of $G$ are all base-$b$ digits, so $G$ is determined by its edge set.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Definition 3 (the graph of a permutiple).

Formalized by `MetaMathlibExt.permutipleGraphEdges`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-graph-edges).

## Graph of the permutiple 87912

Let $(d_0, d_1, d_2, d_3, d_4) = (2, 1, 9, 7, 8)$ be
the decimal digits of $87912$, from the units digit up, and let $\sigma$ be the reversal
$\sigma(j) = 4 - j$ of $\{0, \dots, 4\}$. The edge set
$\{(d_j, d_{\sigma(j)}) : 0 \le j \le 4\}$ of the graph of these digits with digit
permutation $\sigma$ is exactly $\{(2, 8), (1, 7), (9, 9), (7, 1), (8, 2)\}$: the edges
$8 \rightleftarrows 2$ and $7 \rightleftarrows 1$ and a loop at $9$.

Here $87912 = 4 \cdot 21978$, and $21978$ is $87912$ with its digits reversed.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Figure 1.

Formalized by `MetaMathlibExt.permutipleGraphEdges_87912`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-graph-edges-87912).

## Edges of the mother graph

Let $n$ and $b$ be natural numbers. For natural numbers $x$
and $y$, the pair $(x, y)$ is an edge of the $(n, b)$-mother graph $M$ when $x < b$, $y < b$ and

$$\lambda(x + (b - n) y) \le n - 1,$$

where $\lambda(z)$ is the least non-negative residue of the integer $z$ modulo $b$, and $b - n$
and $n - 1$ are computed in the integers.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Definition 4 (the mother graph).

Formalized by `MetaMathlibExt.IsMotherGraphEdge`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-mother-graph-edge).

## An edge and a non-edge of the $(2, 4)$-mother graph

In the $(2, 4)$-mother graph, the
pair $(0, 2)$ is an edge, since $\lambda(0 + (4 - 2) \cdot 2) = \lambda(4) = 0 \le 1$, and the
pair $(0, 1)$ is not an edge, since $\lambda(0 + (4 - 2) \cdot 1) = \lambda(2) = 2 > 1$, where
$\lambda$ is the least non-negative residue modulo $4$.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Definition 4 and Example 1.

Formalized by `MetaMathlibExt.isMotherGraphEdge_two_four`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-mother-graph-edge-two-four).

## Carries of the Hoey–Sloane machine

Let $n$ and $b$ be natural numbers and let
$(d_0, \hat d_0)(d_1, \hat d_1) \cdots (d_k, \hat d_k)$ be an input string of pairs of natural
numbers. The carries $c_0, c_1, c_2, \dots$ of the $(n, b)$-Hoey–Sloane machine on this string
are the integers given by $c_0 = 0$,

$$c_{j+1} = \left\lfloor \frac{n \hat d_j - d_j + c_j}{b} \right\rfloor \quad (0 \le j \le k)$$

and $c_{j+1} = 0$ for $j > k$, where division by $b = 0$ gives $0$.

The machine has a transition from the state $c_j$ on the input $(d_j, \hat d_j)$ when this
division is exact.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Section 4, Equation (2) (the Hoey-Sloane machine).

Formalized by `MetaMathlibExt.hoeySloaneCarry`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#hoey-sloane-carry).

## Carries of the $(2, 4)$-Hoey–Sloane machine on $(0,0)(2,3)(1,2)(3,1)$

On the input
string $(d_0, \hat d_0)(d_1, \hat d_1)(d_2, \hat d_2)(d_3, \hat d_3) = (0,0)(2,3)(1,2)(3,1)$,
the carries $c_0, c_1, c_2, c_3, c_4$ of the $(2, 4)$-Hoey–Sloane machine are $0, 0, 1, 1, 0$.

This is the $(2, 4)$-permutiple string of $(3, 1, 2, 0)_4 = 216 = 2 \cdot 108 =
2 \cdot (1, 2, 3, 0)_4$.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Example 1.

Formalized by `MetaMathlibExt.hoeySloaneCarry_two_four_example`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#hoey-sloane-carry-two-four-example).

## Hoey–Sloane words

Let $n$ and $b$ be natural numbers. An input string
$(d_0, \hat d_0) \cdots (d_k, \hat d_k)$ of pairs of natural numbers belongs to the language $L$
of the $(n, b)$-Hoey–Sloane machine when, with $c_0, \dots, c_{k+1}$ the carries of the machine
on this string, every input $(d_j, \hat d_j)$ is an edge of the $(n, b)$-mother graph, $b$
divides $n \hat d_j - d_j + c_j$ for every $0 \le j \le k$, and $c_{k+1} = 0$.

So the walk starts in the state $c_0 = 0$, every transition is an exact division, and the walk
ends in the state $0$.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Section 4 (the language `L` and `L`-walks).

Formalized by `MetaMathlibExt.IsHoeySloaneWord`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-hoey-sloane-word).

## The string $(0,0)(2,3)(1,2)(3,1)$ lies in the $(2, 4)$-Hoey–Sloane language

The input
string $(d_0, \hat d_0) \cdots (d_3, \hat d_3) = (0,0)(2,3)(1,2)(3,1)$ belongs to the language
$L$ of the $(2, 4)$-Hoey–Sloane machine.

This is the $(2, 4)$-permutiple string of $(3, 1, 2, 0)_4 = 216 = 2 \cdot 108 =
2 \cdot (1, 2, 3, 0)_4$.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Example 1.

Formalized by `MetaMathlibExt.isHoeySloaneWord_two_four_example`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-hoey-sloane-word-two-four-example).

## Conjugate rearrangements have the same graph

Let $d_0, \dots, d_k$ be natural numbers
and let $\pi_1, \pi_2, \tau_1, \tau_2$ be permutations of $\{0, \dots, k\}$ with
$\pi_1 \tau_1 \pi_1^{-1} = \pi_2 \tau_2 \pi_2^{-1}$. Then the graph of the digits
$d_{\pi_1(0)}, \dots, d_{\pi_1(k)}$ with digit permutation $\tau_1$ and the graph of the digits
$d_{\pi_2(0)}, \dots, d_{\pi_2(k)}$ with digit permutation $\tau_2$ have the same edge set:

$$\{(d_{\pi_1(j)}, d_{\pi_1(\tau_1(j))}) : 0 \le j \le k\} =
\{(d_{\pi_2(j)}, d_{\pi_2(\tau_2(j))}) : 0 \le j \le k\}.$$

The source assumes, for a base $b$ and a multiplier $n$ with $1 < n < b$, that
$(d_{\pi_1(k)}, \dots, d_{\pi_1(0)})_b$ is an $(n, b, \tau_1)$-permutiple and that
$(d_{\pi_2(k)}, \dots, d_{\pi_2(0)})_b$ is an $(n, b, \tau_2)$-permutiple, together with a base
permutiple $(d_k, \dots, d_0)_b$; these hypotheses are not needed.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Theorem 4.

Stated but not proved: `MetaMathlibExt.permutipleGraphEdges_eq_of_conj` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-graph-edges-eq-of-conj).

## Every permutiple has a cycle-preserving digit permutation

Let $n$, $b$ and
$d_0, \dots, d_k$ be natural numbers and let $\sigma$ be a permutation of $\{0, \dots, k\}$ such
that $(d_k, \dots, d_0)_b$ is an $(n, b, \sigma)$-permutiple. Then there is a permutation
$\hat\sigma$ of $\{0, \dots, k\}$ such that $(d_k, \dots, d_0)_b$ is also an
$(n, b, \hat\sigma)$-permutiple and the digits along each cycle of $\hat\sigma$ are distinct:
for all $j \in \{0, \dots, k\}$ and all $i \ge 0$, if $d_{\hat\sigma^i(j)} = d_j$ then
$\hat\sigma^i(j) = j$.

Unlike the paper, no assumption $1 < n < b$ is made.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Theorem 5, with Definition 5 (cycle-preserving permutations).

Stated but not proved: `MetaMathlibExt.exists_cyclePreserving_permutiple` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#exists-cycle-preserving-permutiple).

## Permutiple graphs are unions of simple cycles of the mother graph

Let $n \ge 1$
and $b \ge 2$ be natural numbers, let $\sigma$ be a permutation of $\{0, \dots, k\}$, and
let $(d_k, \dots, d_0)_b$ be an $(n, b, \sigma)$-permutiple, where $(e_k, \dots, e_0)_b$
denotes the base-$b$ numeral $\sum_{j=0}^{k} e_j b^j$. Let
$E = \{(d_j, d_{\sigma(j)}) : 0 \le j \le k\}$ be the edge set of its graph. Then every
pair in $E$ is an edge of the $(n, b)$-mother graph, and every $e \in E$ lies on a directed
cycle with distinct vertices all of whose edges are in $E$: there are $m \ge 0$ and pairwise
distinct natural numbers $v_0, \dots, v_m$ such that, with indices taken modulo $m + 1$,
$(v_i, v_{i+1}) \in E$ for every $0 \le i \le m$ and $e = (v_i, v_{i+1})$ for some $i$.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Theorem 6, with Definition 6 (permutiple classes and their graphs).

Stated but not proved: `MetaMathlibExt.permutipleGraphEdges_union_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-graph-edges-union-cycles).

## Hoey–Sloane words with permuted digits are unions of cycles

Let $n \ge 1$ and $b \ge 2$
be natural numbers, and let $s = (d_0, \hat d_0) \cdots (d_k, \hat d_k)$ be an input string in
the language $L$ of the $(n, b)$-Hoey–Sloane machine such that $\hat d_j = d_{\sigma(j)}$ for all
$j$, for some permutation $\sigma$ of $\{0, \dots, k\}$. Let
$E = \{(d_j, \hat d_j) : 0 \le j \le k\}$ be the set of inputs of $s$. Then every $e \in E$ lies
on a directed cycle with edges in $E$: there are $m \ge 0$ and pairwise distinct natural numbers
$v_0, \dots, v_m$ such that $(v_i, v_{i+1}) \in E$ for all $0 \le i \le m$, with indices taken
modulo $m + 1$, and $e = (v_i, v_{i+1})$ for some $i$.

## Sources

- B. V. Holt, *Finding Permutiples of a Known Base and Multiplier*, INTEGERS 25 (2025), Article A13, Corollary 1.

Stated but not proved: `MetaMathlibExt.hoeySloaneWord_inputs_union_cycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#hoey-sloane-word-inputs-union-cycles).

## Sample edges of the $(4, 10)$-mother graph

In the $(4, 10)$-mother graph, $(2, 8)$ and
$(9, 9)$ are edges and $(2, 1)$ is not. With $\lambda$ the least non-negative residue modulo
ten, $\lambda(2 + 6 \cdot 8) = 0 \le 3$ and $\lambda(9 + 6 \cdot 9) = 3 \le 3$, while
$\lambda(2 + 6 \cdot 1) = 8 > 3$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 4 and Example 1.

Formalized by `MetaMathlibExt.isMotherGraphEdge_four_ten`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-mother-graph-edge-four-ten).

## Transitions of the Hoey-Sloane machine

Let $n$, $b$, $c_1$, $c_2$, $d_1$ and $d_2$ be
natural numbers. The input $e = (d_1, d_2)$ moves state $c_1$ to state $c_2$ in one transition of
the $(n, b)$-Hoey-Sloane machine $\Gamma$ when $c_1 < n$, $c_2 < n$, $(d_1, d_2)$ is an edge of
the $(n, b)$-mother graph, and $b c_2 - c_1 = n d_2 - d_1$ in the integers (Equation (1)).

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3, Equation (1).

Formalized by `MetaMathlibExt.IsHoeySloaneStep`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-hoey-sloane-step).

## Runs of the Hoey-Sloane machine

Let $n$, $b$, $c$ and $c'$ be natural numbers and let
$s = e_1 e_2 \cdots e_m$ be a finite string of inputs, each a pair of natural numbers. The
$(n, b)$-Hoey-Sloane machine can go from state $c$ to state $c'$ reading $s$ from left to right
when there are natural numbers $c_0, c_1, \dots, c_m$ with $c_0 = c$ and $c_m = c'$ such that,
for each $1 \le i \le m$, the input $e_i$ moves state $c_{i-1}$ to state $c_i$ in one transition
of the $(n, b)$-Hoey-Sloane machine. For the empty string ($m = 0$) this says $c = c'$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3.

Formalized by `MetaMathlibExt.IsHoeySloaneRun`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-hoey-sloane-run).

## Language of the Hoey–Sloane machine

For natural numbers $n$ and $b$, the language
$L$ of the $(n, b)$-Hoey–Sloane machine is the set of strings $s$ of pairs of natural
numbers such that the machine, reading $s$ from left to right, can go from state $0$ to
state $0$. In particular the empty string belongs to $L$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3.

Formalized by `MetaMathlibExt.hoeySloaneLanguage`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#hoey-sloane-language).

## A word in the $(4, 10)$-Hoey-Sloane language

The input string
$(2, 8)(1, 7)(9, 9)(7, 1)(8, 2)$ belongs to the language of the $(4, 10)$-Hoey-Sloane machine:
reading it from left to right, the machine can go from state $0$ to state $0$.

Writing $87912 = (d_4, \dots, d_0)_{10}$ and letting $\sigma$ be the digit reversal
$\sigma(j) = 4 - j$, so that $87912 = 4 \cdot (d_{\sigma(4)}, \dots, d_{\sigma(0)})_{10}$ is
$4 \cdot 21978$, the inputs are the pairs $(d_j, d_{\sigma(j)})$ for $j = 0, \dots, 4$; an
accepting run passes through the states $0, 3, 3, 3, 0, 0$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3 and Example 2.

Formalized by `MetaMathlibExt.mem_hoeySloaneLanguage_87912`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#mem-hoey-sloane-language-87912).

## Permutiple strings

Let $n$ and $b$ be natural numbers, and for natural numbers
$a_0, \dots, a_k$ write $(a_k, \dots, a_0)_b = \sum_{j=0}^{k} a_j b^j$. A string $s$ of inputs
(pairs of natural numbers) is an $(n, b)$-permutiple string when it belongs to the language $L$ of
the $(n, b)$-Hoey-Sloane machine and there are a natural number $k$, natural numbers
$d_0, \dots, d_k$ and a permutation $\sigma$ of $\{0, \dots, k\}$ such that $(d_k, \dots, d_0)_b$
is an $(n, b, \sigma)$-permutiple, that is, every $d_j$ is less than $b$ and
$(d_k, \dots, d_0)_b = n (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$, and
$s = (d_0, d_{\sigma(0)})(d_1, d_{\sigma(1)}) \cdots (d_k, d_{\sigma(k)})$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3.

Formalized by `MetaMathlibExt.IsPermutipleString`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-permutiple-string).

## The permutiple string of $87912 = 4 \cdot 21978$

The string of inputs
$(2, 8)(1, 7)(9, 9)(7, 1)(8, 2)$ is a $(4, 10)$-permutiple string. It is produced by the
$(4, 10)$-permutiple $87912 = 4 \cdot 21978$, whose multiplication reverses the digits.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3 and Table 1.

Formalized by `MetaMathlibExt.isPermutipleString_87912`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-permutiple-string-87912).

## Edge list of a closed walk

For a list $[v_0, \dots, v_{r-1}]$ of natural numbers,
read as the vertex list of a closed walk, the edge list is
$[(v_0, v_1), \dots, (v_{r-2}, v_{r-1}), (v_{r-1}, v_0)]$: each vertex is paired with the
next one, and the last vertex with the first. A single vertex $[v_0]$ gives the loop
$[(v_0, v_0)]$, and the empty list gives the empty edge list.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 5 (cycles of `M`).

Formalized by `MetaMathlibExt.cycleEdges`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#cycle-edges).

## Edges of the closed walks $2 \to 8 \to 2$ and $9 \to 9$

The closed walk with vertex
list $[2, 8]$ has edge list $[(2, 8), (8, 2)]$, and the closed walk with vertex list $[9]$
(a loop at $9$) has edge list $[(9, 9)]$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Example 2.

Formalized by `MetaMathlibExt.cycleEdges_examples`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#cycle-edges-examples).

## Cycles of the mother graph

Let $n$ and $b$ be natural numbers. A list
$[v_0, \dots, v_{r-1}]$ of natural numbers is a (directed) cycle of the $(n, b)$-mother graph when
it is nonempty, has no repeated entry, and each of its edges
$(v_0, v_1), \dots, (v_{r-2}, v_{r-1}), (v_{r-1}, v_0)$ is an edge of the $(n, b)$-mother graph.
In particular a one-element list $[v]$ is a cycle when $(v, v)$ is an edge of the mother graph.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 5 (cycles of `M`).

Formalized by `MetaMathlibExt.IsMotherGraphCycle`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-mother-graph-cycle).

## Multiset union of cycle edges

For a multiset $I$ of lists of natural numbers, each
read as the vertex list of a closed walk, write $C_j$ for the edge list of $j \in I$. The
multiset union $C_I = \biguplus_{j \in I} C_j$ is the multiset of all these edges, counted
with multiplicity: each list $j$ contributes its edges as often as $j$ occurs in $I$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 2.3 (multiset cycle union `C_I`).

Formalized by `MetaMathlibExt.cycleUnion`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#cycle-union).

## Hoey–Sloane transition of a digit pair

For natural numbers $n$ and $b$ and a pair
$e = (d_1, d_2)$ of natural numbers, the multi-edge of the $(n, b)$-Hoey–Sloane multigraph
carrying the label $e$ is $(c_1, c_2)$, where $c_1 = \lambda(d_1 + (b - n) d_2)$ with
$\lambda$ the least non-negative residue modulo $b$ (computed in the integers), and
$c_2 = \lfloor (n d_2 - d_1 + c_1) / b \rfloor$, replaced by $0$ when negative. For $b = 0$
the conventions are $x \bmod 0 = x$ and $x / 0 = 0$, and $c_1$ is likewise replaced by $0$
when negative.

For an edge $e$ of the $(n, b)$-mother graph with $1 < n < b$, the source shows that
$(c_1, c_2)$ is the unique solution of $b c_2 - c_1 = n d_2 - d_1$ with
$0 \le c_1, c_2 \le n - 1$, that is, the transition of the Hoey–Sloane machine with input $e$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 6 and the proof of Theorem 6.

Formalized by `MetaMathlibExt.hoeySloaneTransition`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#hoey-sloane-transition).

## Two multi-edges of the $(4, 10)$-Hoey–Sloane multigraph

In the
$(4, 10)$-Hoey–Sloane multigraph the label $(2, 8)$ sits on the multi-edge from state $0$
to state $3$, and the label $(1, 7)$ sits on the loop at state $3$: the Hoey–Sloane
transition sends $(2, 8)$ to $(0, 3)$ and $(1, 7)$ to $(3, 3)$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 6 and Figure 4.

Formalized by `MetaMathlibExt.hoeySloaneTransition_four_ten`, a theorem declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#hoey-sloane-transition-four-ten).

## Multi-image union of a multiset of cycles

Let $n$ and $b$ be natural numbers and let $I$
be a multiset of vertex lists. Let $C_I$ be the multiset cycle union of $I$: the multiset sum,
over the lists in $I$, of their edges, where a nonempty list $[v_0, \dots, v_{r-1}]$ has the
edges $(v_0, v_1), \dots, (v_{r-2}, v_{r-1}), (v_{r-1}, v_0)$ and the empty list has none. The
multi-image union $\Delta_I$ is the multiset obtained by replacing each edge $e = (d_1, d_2)$ of
$C_I$, with its multiplicity, by the multi-edge $(c_1, c_2)$ of the $(n, b)$-Hoey-Sloane
multigraph that carries the label $e$: $c_1 = \lambda(d_1 + (b - n) d_2)$, where $\lambda$ is
the least non-negative residue modulo $b$ computed in the integers (the identity when $b = 0$),
and $c_2 = \lfloor (n d_2 - d_1 + c_1) / b \rfloor$ (taken to be $0$ when $b = 0$), with a
negative value of $c_1$ or $c_2$ replaced by $0$.

The labels are dropped, since they do not affect in- and out-degrees, connectivity or Eulerian
circuits.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 7.

Formalized by `MetaMathlibExt.multiImageUnion`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#multi-image-union).

## Eulerian circuit through the zero state

Read a multiset $D$ of pairs of natural
numbers as the multi-edges $(c_1, c_2)$ of a directed multigraph. Then $D$ has an Eulerian
circuit beginning and ending with the zero state when there is a nonempty list of pairs
whose multiset of entries is $D$ (so it uses every multi-edge exactly once), in which each
multi-edge ends where the next one begins, the first one starts at $0$ and the last one
ends at $0$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Theorem 7 (hypothesis).

Formalized by `MetaMathlibExt.HasEulerianCircuitFromZero`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#has-eulerian-circuit-from-zero).

## $L$-Eulerian multigraphs

Let $D$ be a finite multiset of multi-edges $(x, y)$ between
natural numbers, and call a number a vertex of $D$ when it is an endpoint of some multi-edge in
$D$. The multigraph $D$ is $L$-Eulerian when $0$ is a vertex of $D$, every vertex $u$ of $D$
reaches every vertex $v$ of $D$ along a (possibly empty) directed path of multi-edges in $D$, and
for every natural number $c$ the number of multi-edges in $D$ ending at $c$ equals the number of
multi-edges in $D$ starting at $c$, counted with multiplicity.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Section 4 (definition of `L`-Eulerian, before Corollary 2).

Formalized by `MetaMathlibExt.IsLEulerian`, a definition declared in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-leulerian).

## Edge condition for permutiples

Let $n \ge 1$, $b$ and $k$ be natural numbers, let $\sigma$
be a permutation of $\{0, \dots, k\}$ and let $(d_k, \dots, d_0)_b$ be an
$(n, b, \sigma)$-permutiple, that is, $d_i < b$ for all $i$ and
$(d_k, \dots, d_0)_b = n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$. Then for every
$0 \le j \le k$, $\lambda(d_j + (b - n) d_{\sigma(j)}) \le n - 1$, where $\lambda$ is the least
non-negative residue modulo $b$ and $b - n$ is computed in the integers, so it may be negative.

The hypothesis $n \ge 1$ is needed: for $n = 0$ the only permutiples have all digits zero and the
bound would read $0 \le -1$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Theorem 3, quoting Holt, *Finding Permutiples of a Known Base and Multiplier*.

Stated but not proved: `MetaMathlibExt.permutiple_edge_residue_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-edge-residue-le).

## Edges of a permutiple's graph lie on cycles of the mother graph

Let $n \ge 1$, $b$ and $k$
be natural numbers, let $\sigma$ be a permutation of $\{0, \dots, k\}$ and let
$(d_k, \dots, d_0)_b$ be an $(n, b, \sigma)$-permutiple, that is, $d_i < b$ for all $i$ and
$(d_k, \dots, d_0)_b = n \cdot (d_{\sigma(k)}, \dots, d_{\sigma(0)})_b$. Its graph has the edges
$(d_i, d_{\sigma(i)})$ for $0 \le i \le k$. Then for every $0 \le j \le k$, the pair
$(d_j, d_{\sigma(j)})$ is an edge of the $(n, b)$-mother graph, and $d_j$ is reachable from
$d_{\sigma(j)}$ along edges of the graph of the permutiple (in zero steps when they are equal),
so the edge $(d_j, d_{\sigma(j)})$ lies on a directed cycle of that graph.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Theorem 4, quoting Holt, *Finding Permutiples of a Known Base and Multiplier*.

Stated but not proved: `MetaMathlibExt.permutiple_graph_isUnion_motherGraphCycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#permutiple-graph-is-union-mother-graph-c).

## Uniqueness of Hoey-Sloane transitions

Let $n \le b$. If an input $e$ moves state $c_1$
to state $c_2$ and also moves state $\hat c_1$ to state $\hat c_2$, each in one transition of the
$(n, b)$-Hoey-Sloane machine, then $c_1 = \hat c_1$ and $c_2 = \hat c_2$.

The paper assumes $1 < n < b$; here it is weakened to $n \le b$. For $n > b$ the claim can fail:
for $n = 3$ and $b = 1$ the input $(0, 0)$ moves $0$ to $0$ and also $1$ to $1$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Theorem 5.

Stated but not proved: `MetaMathlibExt.isHoeySloaneStep_unique` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-hoey-sloane-step-unique).

## Every mother-graph edge induces a carry transition

Let $n$ and $b$ be natural
numbers. If $(d_1, d_2)$ is an edge of the $(n, b)$-mother graph, then there are natural
numbers $c_1$ and $c_2$ with $c_1 \le n - 1$ and $c_2 \le n - 1$ such that
$b c_2 - c_1 = n d_2 - d_1$ as integers.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Theorem 6.

Stated but not proved: `MetaMathlibExt.exists_carries_of_isMotherGraphEdge` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#exists-carries-of-is-mother-graph-edge).

## Hoey-Sloane transitions are transitions of the machine

Let $1 < n < b$, let
$e = (d_1, d_2)$ be an edge of the $(n, b)$-mother graph, and let $(c_1, c_2)$ be the Hoey-Sloane
transition of $e$, that is, $c_1 = \lambda(d_1 + (b - n) d_2)$ and $c_2 = (n d_2 - d_1 + c_1) / b$,
where $\lambda$ is the least non-negative residue modulo $b$. Then the input $e$ moves state $c_1$
to state $c_2$ in one transition of the $(n, b)$-Hoey-Sloane machine.

By the uniqueness of Hoey-Sloane transitions (Theorem 5), it is the only transition labelled
by $e$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Definition 6, from Theorems 5 and 6.

Stated but not proved: `MetaMathlibExt.isHoeySloaneStep_hoeySloaneTransition` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-hoey-sloane-step-hoey-sloane-transiti).

## Inputs of a permutiple string lie on mother-graph cycles

Let $1 < n < b$ and let $s$ be
an $(n, b)$-permutiple string. Then every input $(d, \hat d)$ of $s$ is an edge of the
$(n, b)$-mother graph, and $\hat d$ reaches $d$ along a (possibly empty) directed path in the
graph whose edges are the inputs of $s$, so $(d, \hat d)$ lies on a directed cycle of that graph.
In this sense the inputs of $s$ form a union of cycles of the mother graph.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Corollary 1, quoting Holt, *Finding Permutiples of a Known Base and Multiplier*.

Stated but not proved: `MetaMathlibExt.isPermutipleString_inputs_isUnion_motherGraphCycles` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#is-permutiple-string-inputs-is-union-mot).

## Eulerian circuits through zero yield permutiple strings

Let $1 < n < b$ and let $I$
be a multiset of cycles of the $(n, b)$-mother graph, with multiset union of cycle edges
$C_I$ and multi-image union $\Delta_I$. If $\Delta_I$ has an Eulerian circuit beginning
and ending at the zero state, then there is an $(n, b)$-permutiple string $s$ whose
multiset of entries is $C_I$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Theorem 7.

Stated but not proved: `MetaMathlibExt.exists_isPermutipleString_of_hasEulerianCircuitFromZero` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#exists-is-permutiple-string-of-has-euler).

## $L$-Eulerian criterion for permutiple strings

Let $1 < n < b$ and let $I$ be a
multiset of cycles of the $(n, b)$-mother graph, with multiset union of cycle edges $C_I$
and multi-image union $\Delta_I$. Then $\Delta_I$ is $L$-Eulerian if and only if there is
an $(n, b)$-permutiple string $s$ whose multiset of entries is $C_I$.

## Sources

- Benjamin V. Holt, *A Multigraph Characterization of Permutiple Strings*, INTEGERS 25 (2025), Article A111, Corollary 2.

Stated but not proved: `MetaMathlibExt.exists_isPermutipleString_iff_isLEulerian` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/PermutipleStringsWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html#exists-is-permutiple-string-iff-is-leule).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutiples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/permutiples)
