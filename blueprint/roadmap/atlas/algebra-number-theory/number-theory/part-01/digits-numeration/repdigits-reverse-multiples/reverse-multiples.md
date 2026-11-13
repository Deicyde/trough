---
declaration: section
origin: cited
lean: MetaMathlibExt.sloane_reverse_multiple_endpoint, MetaMathlibExt.sutcliffe_two_to_three_digit_reverse_multiple, MetaMathlibExt.isYoungRetained, MetaMathlibExt.isYoungRetained_iff, MetaMathlibExt.youngGraph, MetaMathlibExt.youngGraph_src, MetaMathlibExt.youngGraph_tgt, MetaMathlibExt.youngGraph_label
statement: formalized
---

# Reverse multiples

32 results, 16 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html).

## Sloane's endpoint formula for reverse multiples

Let $g$ and $k$ be integers with
$2 \le k < g$, and let $N = (a_n a_{n-1} \cdots a_0)_g$ have base-$g$ digits
$a_0, \dots, a_n \in \{0, \dots, g - 1\}$, with units digit $a_0$ and leading digit $a_n \ne 0$.
Suppose $N$ is a $(g, k)$ reverse multiple, that is, $k N = (a_0 a_1 \cdots a_n)_g$, and that
$a_0 + a_n = g$. Then $(k + 1) a_n = g$; in particular $k + 1$ divides $g$ and
$a_n = g / (k + 1)$.

## Sources

- L. H. Kendrick, *Young Graphs: 1089 et al.*, Journal of Integer Sequences 18 (2015), Article 15.9.7, Corollary `cor:lastdig1089` (Sloane's Conjecture 3.5) and proof, lines 418–424, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Kendrick/ken1.tex>.

Formalized by `MetaMathlibExt.sloane_reverse_multiple_endpoint`, a theorem declared in [MathlibExt/NumberTheory/Digits/SloaneReverseMultiple.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/SloaneReverseMultiple.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#sloane-reverse-multiple-endpoint).

## Sutcliffe's theorem on two- and three-digit reverse multiples

Let $g$ and $k$ be
integers with $2 \le k < g$, and let $a$ and $b$ be base-$g$ digits, $0 \le a, b < g$, with
$a \ne 0$, such that $(a\,b)_g$ is a $(g, k)$ reverse multiple, that is,
$k (a g + b) = b g + a$. Then $a + b < g$, so $a + b$ is a base-$g$ digit, and
$(a\,(a + b)\,b)_g$ is again a $(g, k)$ reverse multiple, that is,
$k (a g^2 + (a + b) g + b) = b g^2 + (a + b) g + a$.

This is the forward implication of Sutcliffe's theorem; the converse is not included.

## Sources

- L. H. Kendrick, *Young Graphs: 1089 et al.*, Journal of Integer Sequences 18 (2015), Article 15.9.7, Remark `rem:truncate` (quoting Sutcliffe's Theorem 3), lines 203–205, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Kendrick/ken1.tex>.

Formalized by `MetaMathlibExt.sutcliffe_two_to_three_digit_reverse_multiple`, a theorem declared in [MathlibExt/NumberTheory/Digits/SutcliffeReverseMultiple.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/SutcliffeReverseMultiple.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#sutcliffe-two-to-three-digit-reverse-mul).

## Retained node

Let $V$ be a set, let $P$ be a predicate on $V$ (the pivot nodes) and let
$\prec$ be a binary relation on $V$. A node $v \in V$ is retained with respect to $P$ and $\prec$
if $P(v)$ holds or there is a node $w \in V$ with $P(w)$ and $v \prec w$.

Formalized by `MetaMathlibExt.isYoungRetained`, a definition declared in [MathlibExt/NumberTheory/Digits/YoungGraph.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungGraph.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#is-young-retained).

## Characterization of retained nodes

Let $V$ be a set, let $P$ be a predicate on $V$ and
let $\prec$ be a binary relation on $V$. A node $v \in V$ is retained with respect to $P$ and
$\prec$ if and only if $P(v)$ holds or there is a node $w \in V$ with $P(w)$ and $v \prec w$.

Formalized by `MetaMathlibExt.isYoungRetained_iff`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungGraph.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungGraph.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#is-young-retained-iff).

## Young graph of a labeled directed graph

Let $G$ be a labeled directed graph with vertex
set $V$, edge set $E$ and label set $L$, let $P$ be a predicate on $V$ and let $\prec$ be a binary
relation on $V$. The Young graph of $G$ with respect to $P$ and $\prec$ is the labeled directed
graph with label set $L$ whose vertices are the vertices of $G$ that are retained with respect to
$P$ and $\prec$, whose edges are the edges of $G$ whose source and target are both retained, and
in which each edge has the same source, target and label as in $G$.

Formalized by `MetaMathlibExt.youngGraph`, a definition declared in [MathlibExt/NumberTheory/Digits/YoungGraph.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungGraph.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-graph).

## Source of an edge in the Young graph

Let $G$ be a labeled directed graph, let $P$ be a
predicate on its vertices, let $\prec$ be a binary relation on its vertices, and let $e$ be an
edge of $G$ whose source and target are both retained with respect to $P$ and $\prec$, viewed as
an edge of the Young graph of $G$ with respect to $P$ and $\prec$. The source of $e$ in the Young
graph, viewed as a vertex of $G$, is the source of $e$ in $G$.

Formalized by `MetaMathlibExt.youngGraph_src`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungGraph.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungGraph.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-graph-src).

## Target of an edge in the Young graph

Let $G$ be a labeled directed graph, let $P$ be a
predicate on its vertices, let $\prec$ be a binary relation on its vertices, and let $e$ be an
edge of $G$ whose source and target are both retained with respect to $P$ and $\prec$, viewed as
an edge of the Young graph of $G$ with respect to $P$ and $\prec$. The target of $e$ in the Young
graph, viewed as a vertex of $G$, is the target of $e$ in $G$.

Formalized by `MetaMathlibExt.youngGraph_tgt`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungGraph.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungGraph.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-graph-tgt).

## Label of an edge in the Young graph

Let $G$ be a labeled directed graph, let $P$ be a
predicate on its vertices, let $\prec$ be a binary relation on its vertices, and let $e$ be an
edge of $G$ whose source and target are both retained with respect to $P$ and $\prec$, viewed as
an edge of the Young graph of $G$ with respect to $P$ and $\prec$. The label of $e$ in the Young
graph is its label in $G$.

Formalized by `MetaMathlibExt.youngGraph_label`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungGraph.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungGraph.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-graph-label).

## Carry equations for reverse multiples, general form

Let $g, k, n$ be natural numbers
with $2 \le k < g$, and let $a_0, \dots, a_{n-1}$ be natural numbers with $a_i < g$ for every $i$.
Then $k \sum_{i\lt n} a_i g^i = \sum_{i\lt n} a_{n-1-i} g^i$ if and only if there is a unique sequence
of natural numbers $r_0, \dots, r_n$ with $r_0 = 0$, $r_n = 0$ and, for every $i < n$,
$r_{i+1} < k$ and $k a_i + r_i = a_{n-1-i} + r_{i+1} g$.

No hypothesis is placed on $n$ or on the end digits $a_0$ and $a_{n-1}$; in particular $n$ may be
$0$.

Formalized by `MetaMathlibExt.young_reverse_multiple_carry_path_iff_general`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungReverseMultipleCarryPath.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungReverseMultipleCarryPath.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-reverse-multiple-carry-path-iff-ge).

## Carry equations for reverse multiples

Let $g, k, n$ be natural numbers with
$2 \le k < g$ and $n \ge 1$, and let $a_0, \dots, a_{n-1}$ be natural numbers with $a_i < g$ for
every $i$, $a_{n-1} \ne 0$ and $a_0 \ne 0$. Then $k \sum_{i\lt n} a_i g^i = \sum_{i\lt n} a_{n-1-i} g^i$,
that is, $k$ times the number with base-$g$ digits $a_{n-1}, \dots, a_0$ (most significant first)
equals the number with these digits reversed, if and only if there is a unique sequence of natural
numbers $r_0, \dots, r_n$ with $r_0 = 0$, $r_n = 0$ and, for every $i < n$, $r_{i+1} < k$ and
$k a_i + r_i = a_{n-1-i} + r_{i+1} g$.

The carry $r_{i+1}$ here is the source's $r_i$.

## Sources

- L. H. Kendrick, *Young Graphs: 1089 et al.*, Journal of Integer Sequences 18 (2015), Article 15.9.7, subsection `subsec:eqtns`, lines 128–154 (the column equations for `kN = Reverse_g(N)`, Young's bound `r_i ≤ k - 1`, and equation `eq:rmdig`), <https://cs.uwaterloo.ca/journals/JIS/VOL18/Kendrick/ken1.tex>. It follows from `young_reverse_multiple_carry_path_iff_general`; the hypotheses `hfirst` and `hlast` (and `hn`, which only serves to state them) are unused and keep the source's shape.

Formalized by `MetaMathlibExt.young_reverse_multiple_carry_path_iff`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungReverseMultipleCarryPath.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungReverseMultipleCarryPath.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-reverse-multiple-carry-path-iff).

## Young's theorem on reverse multiples

Let $g$ and $k$ be natural numbers with $2 \le k < g$.
A $(g, k)$ reverse multiple is a list of base-$g$ digits $d_1, d_2, \dots, d_n$, most significant
first, with $n \ge 2$, $d_1 \ne 0$, $d_n \ne 0$ and $d_i < g$ for every $i$, such that $k$ times
the number $\sum_{i=1}^{n} d_i g^{n-i}$ equals the number $\sum_{i=1}^{n} d_{n+1-i} g^{n-i}$
whose digits are those of the first in reverse order. Consider the graph whose nodes are pairs
$(r, s)$ of natural numbers, with an edge labeled $(a, b)$ from $(r, s)$ to $(r', s')$ whenever
$k b + s = a + s' g$ and $k a + r' = b + r g$. A path is a sequence of nodes $v_0, \dots, v_m$
together with a sequence of labels $\ell_1, \dots, \ell_m$ such that $m \ge 1$, $v_0 = (0, 0)$,
both coordinates of every node are less than $k$, both coordinates of every label are less
than $g$, both coordinates of $\ell_1$ are nonzero, and for each $j$ the label $\ell_j$ labels an
edge from $v_{j-1}$ to $v_j$. A node $(r, s)$ is an even pivot if $r = s$, and an odd pivot if
for some $c < g$ there is an edge labeled $(c, c)$ from $(r, s)$ to $(s, r)$.

Then there is a bijection from the $(g, k)$ reverse multiples with an even number of digits to
the paths whose last node is an even pivot, and a bijection from the $(g, k)$ reverse multiples
with an odd number of digits to the paths whose last node is an odd pivot. Under both
bijections, a reverse multiple $d_1, \dots, d_n$ is sent to a path with labels
$(d_1, d_n), (d_2, d_{n-1}), \dots, (d_h, d_{n+1-h})$, where $h = \lfloor n/2 \rfloor$; in the
odd case, if $(r, s)$ is the last node of that path, there is an edge labeled
$(d_{h+1}, d_{h+1})$ from $(r, s)$ to $(s, r)$.

## Sources

- L. H. Kendrick, *Young Graphs: 1089 et al.*, Journal of Integer Sequences 18 (2015), Article 15.9.7, Theorem [Young's Theorem], lines 192-197, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Kendrick/ken1.tex>, after Theorems 1 and 2 of Young's first paper on reverse multiples.

Formalized by `MetaMathlibExt.young_reverse_multiples_equiv_pivot_paths`, a theorem declared in [MathlibExt/NumberTheory/Digits/YoungReverseMultiples.lean, line 1785](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/YoungReverseMultiples.lean#L1785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#young-reverse-multiples-equiv-pivot-path).

## Reverse divisor

A natural number $n$ is a reverse divisor if $n > 0$ and there is a
natural number $k \ge 2$ such that the decimal reversal of $n$ equals $kn$. Since $n > 0$, such a
$k$ is unique; it is called the quotient of $n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Section 1 (terminology).

Formalized by `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.IsReverseDivisor`, a definition declared in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#is-reverse-divisor).

## Characterization of reverse divisors

A natural number $n$ is a reverse divisor if and
only if $n > 0$ and there is a natural number $k \ge 2$ such that the decimal reversal of $n$
equals $kn$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Section 1 (terminology).

Formalized by `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.isReverseDivisor_iff`, a theorem declared in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#is-reverse-divisor-iff).

## Property $P^*$

**Property $P^*$.** A natural number $n$ has property $P^*$ if $n$ divides the decimal
reversal of every multiple of $n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Section 2 (terminology).

Formalized by `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.HasPropertyPStar`, a definition declared in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#has-property-pstar).

## Unfolding property $P^*$

**Unfolding property $P^*$.** A natural number $n$ has property $P^*$ if and only if $n$
divides the decimal reversal of every multiple of $n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Section 2 (terminology).

Formalized by `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.hasPropertyPStar_iff`, a theorem declared in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#has-property-pstar-iff).

## The positive integers with property $P^*$ are the divisors of $99$

**The positive integers with property $P^*$ are the divisors of $99$.** A natural number
$n \ge 1$ has property $P^*$ if and only if $n$ divides $99$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.hasPropertyPStar_iff_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#has-property-pstar-iff-dvd).

## Divisors of $99$ have property $P^*$

**Divisors of $99$ have property $P^*$.** Every divisor of $99$ has property $P^*$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.hasPropertyPStar_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#has-property-pstar-of-dvd).

## Positive integers sharing a factor with $10$ lack property $P^*$

**Positive integers sharing a factor with $10$ lack property $P^*$.** If $n \ge 1$ is a
natural number with $\gcd(n, 10) \ne 1$, then $n$ does not have the property $P^*$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.not_hasPropertyPStar_of_not_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#not-has-property-pstar-of-not-coprime).

## Palindromes with property $P^*$

**Palindromes with property $P^*$.** Let $n \ge 1$ be a natural number that is a decimal
palindrome, that is, whose decimal reversal equals $n$. If $n$ has the property $P^*$, then $n$
is one of $1$, $3$, $9$, $11$, $33$ and $99$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 3.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.palindrome_hasPropertyPStar` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#palindrome-has-property-pstar).

## Reverse divisors have quotient $4$ or $9$

If $n$ is a reverse divisor, then the decimal
reversal of $n$ equals $4n$ or $9n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Theorem 1 (quoted from the literature).

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.reverseDigits_eq_four_or_nine_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#reverse-digits-eq-four-or-nine-mul).

## Basic reverse divisors

For every natural number $k \ge 2$, the numbers
$11(10^k - 1)$ and $22(10^k - 1)$ both have exactly $k + 2$ decimal digits, the decimal
reversal of $11(10^k - 1)$ equals $9 \cdot 11(10^k - 1)$, and the decimal reversal of
$22(10^k - 1)$ equals $4 \cdot 22(10^k - 1)$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Theorem 1 (quoted from the literature).

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.basic_reverseDivisors` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#basic-reverse-divisors).

## Reverse divisors have at least four digits

Every reverse divisor has at least four
decimal digits.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Theorem 1 (quoted from the literature).

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.four_le_length_digits` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#four-le-length-digits).

## Reverse divisors with at most seven digits

Let $n$ be a reverse divisor with $L$
decimal digits, where $L \le 7$. Then $n = 11(10^{L-2} - 1)$ or $n = 22(10^{L-2} - 1)$, where
$L - 2$ is read as $0$ when $L < 2$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Theorem 1 (quoted from the literature).

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.eq_basic_of_length_le_seven` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#eq-basic-of-length-le-seven).

## Reverse divisors with quotient $4$ lack property $P^*$

**Reverse divisors with quotient $4$ lack property $P^*$.** If $n > 0$ is a natural number
whose decimal reversal equals $4n$, then $n$ does not have the property $P^*$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.not_hasPropertyPStar_of_quotient_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#not-has-property-pstar-of-quotient-four).

## For $k \ge 2$, the number $11 \cdot (10^k - 1)$ lacks property $P^*$

**For $k \ge 2$, the number $11 \cdot (10^k - 1)$ lacks property $P^*$.** For every natural
number $k \ge 2$, the number $11 \cdot (10^k - 1)$ does not have the property $P^*$.

In the source these numbers $1089, 10989, 109989, \dots$ are the basic reverse divisors with
quotient $9$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.not_hasPropertyPStar_basic_nine` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#not-has-property-pstar-basic-nine).

## No reverse divisor has property $P^*$

**No reverse divisor has property $P^*$.** If $n$ is a reverse divisor, then $n$ does not have
the property $P^*$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 4.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.not_hasPropertyPStar_of_isReverseDivisor` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#not-has-property-pstar-of-is-reverse-div).

## A product congruent to $11$ modulo a power of ten

For every natural number $r$, let
$a = (10^r - 1) \cdot 100 + 89$, the integer whose decimal digits are $r$ nines followed by $89$,
and let $b = 10^{r+2} - 1$, the integer whose decimal digits are $r + 2$ nines. Then the
remainder of $ab$ modulo $10^{r+2}$ is $11$; that is, the last $r + 2$ decimal digits of $ab$ are
$r$ zeros followed by $11$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Lemma 4.

Formalized by `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.mul_nines_modEq_eleven`, a theorem declared in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#mul-nines-mod-eq-eleven).

## In base $B$, divisors of $B^2 - 1$ divide reversals of their multiples

Let $B \ge 2$ be
a natural number and let $n$ be a natural number dividing $B^2 - 1$. Then $n$ divides the
base-$B$ reversal of every multiple of $n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 5.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.dvd_reverseDigits_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#dvd-reverse-digits-of-dvd).

## Infinitely many multiples with divisible reversal

Let $n$ be a natural number not
divisible by $10$, and suppose that $n$ divides the decimal reversal of $k_0 n$ for some natural
number $k_0 \ge 1$. Then there are infinitely many natural numbers $k \ge 1$ such that $n$
divides the decimal reversal of $k n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 6.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.infinite_dvd_reverseDigits_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#infinite-dvd-reverse-digits-mul).

## Sufficient conditions for a multiple with divisible reversal

Let $n$ be a natural
number such that $\gcd(n, 10) = 1$, or $n$ equals its decimal reversal, or $n$ is a reverse
divisor. Then there is a natural number $k_0 \ge 1$ such that $n$ divides the decimal reversal
of $k_0 n$.

## Sources

- Mohamed Ayad and Rachid Bouchenna, "Which Integer Divides the Reverse of Any of Its Multiples?", Proposition 6.

Stated but not proved: `MathlibExt.NumberTheory.Digits.ReverseDivisorWanted.exists_dvd_reverseDigits_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/ReverseDivisorWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#exists-dvd-reverse-digits-mul).

## Complete Young graphs

For natural numbers $g$, $k$ and $m$, the Young graph $Y(g, k)$ of
the $k$-reverse multiples in base $g$ is complete on $m$ nodes: the nodes other than its
distinguished starting node form the complete directed graph on $m$ nodes, so $Y(g, k)$ has
$m + 1$ nodes in all; the node $[0, 0]$ is one of these $m$ nodes, and the starting node has an
edge to every node except $[0, 0]$.

## Sources

- L. H. Kendrick, "Young Graphs: 1089 et al.", Journal of Integer Sequences 18 (2015), <https://cs.uwaterloo.ca/journals/JIS/VOL18/Kendrick/ken1.tex>. Definition at lines 458-460: in the source's `K_m` convention, the nodes other than the distinguished starting node form the complete directed graph on `m` nodes, so the Young graph has `m + 1` total nodes including that distinguished start; `[0, 0]` is one of the `m` non-start nodes, and the starting node connects to every node except `[0, 0]`.

Stated but not proved: `MetaMathlibExt.IsCompleteYoungGraph` is written with `def_wanted` in [WantedExt/NumberTheory/Digits/SloaneCompleteYoungGraphCharacterization.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SloaneCompleteYoungGraphCharacterization.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#is-complete-young-graph).

## Characterization of complete Young graphs

Let $g$, $k$ and $m$ be natural numbers with
$2 \le k < g$ and $m \ge 2$. Then the Young graph $Y(g, k)$ is complete on $m$ nodes if and only
if

$$\left\lfloor \frac{\gcd(g - k,\, k^2 - 1)}{k + 1} \right\rfloor = m - 1.$$

## Sources

- Corollary at lines 574-576 of L. H. Kendrick, "Young Graphs: 1089 et al.", Journal of Integer Sequences 18 (2015), <https://cs.uwaterloo.ca/journals/JIS/VOL18/Kendrick/ken1.tex>. In the source's `K_m` convention, the nodes other than the distinguished starting node form the complete directed graph on `m` nodes, so the Young graph has `m + 1` total nodes including that distinguished start; `[0, 0]` is one of the `m` non-start nodes. Natural-number division represents the source floor because all quantities are nonnegative and the denominator is positive. The hypothesis is `2 ≤ m`, not `1 ≤ m`. The corollary rests on a theorem whose proof starts "Since $s_1$ exists", so it needs `m - 1 ≥ 1`. For `m = 1` the class `K_1` contains no Young graph: every Young graph is connected and contains `[0, 0]`, so the starting node has an edge to some node other than `[0, 0]`, while a graph in `K_1` has none. With `1 ≤ m`, `(g, k) = (10, 9)` and `m = 1` give `gcd(1, 80) / 10 = 0 = m - 1`, but `Y(10, 9)` is the 1089 graph, not in `K_1`.

Stated but not proved: `MetaMathlibExt.sloane_complete_young_graph_characterization` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/SloaneCompleteYoungGraphCharacterization.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Digits/SloaneCompleteYoungGraphCharacterization.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html#sloane-complete-young-graph-characteriza).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reverse multiples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/reverse-multiples)
