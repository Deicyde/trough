---
declaration: section
origin: cited
lean: MetaMathlibExt.MallowsLetter, MetaMathlibExt.SternBrocotLetter, MetaMathlibExt.MallowsParityLetter, MetaMathlibExt.natPairToReal, MetaMathlibExt.natPairToReal_one_two, MetaMathlibExt.gapMediant, MetaMathlibExt.gapMediant_root, MetaMathlibExt.mallowsInsert
statement: formalized
---

# Mallows representation of irrational numbers

81 results, 47 proved and 34 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html).

## The Mallows alphabet

The letters of Mallows representations are the three distinct
letters $L$, $M$ and $R$, standing for "left", "middle" and "right".

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 4.

Formalized by `MetaMathlibExt.MallowsLetter`, an inductive type declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-letter).

## Stern–Brocot letters

The alphabet of Stern–Brocot representations: the two letters
$L$ ("left") and $R$ ("right").

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.SternBrocotLetter`, an inductive type declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-letter).

## The parity alphabet

The parity alphabet consists of the four letters $O_L$, $E_R$, $O_R$
and $E_L$. The intermediate set $I$ linking the Stern–Brocot and Mallows representations is a set
of infinite sequences over this alphabet.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.MallowsParityLetter`, an inductive type declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-parity-letter).

## Real value of a fraction encoded as a pair

The pair $(n, m)$ of natural numbers encodes
the fraction with numerator $n$ and denominator $m$, whose real value is $n / m$ (taken to be $0$
when $m = 0$).

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2 (fractions `n / m` labelling the trees).

Formalized by `MetaMathlibExt.natPairToReal`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#nat-pair-to-real).

## The pair $(1, 2)$ encodes $1/2$

The real value of the fraction encoded by the pair
$(1, 2)$ is $1/2$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.

Formalized by `MetaMathlibExt.natPairToReal_one_two`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#nat-pair-to-real-one-two).

## Mediant of a gap

For a gap bounded by two fractions $n_1/m_1$ and $n_2/m_2$, each encoded
as the pair (numerator, denominator) of natural numbers, the mediant is the fraction
$(n_1 + n_2)/(m_1 + m_2)$, encoded as the pair $(n_1 + n_2, m_1 + m_2)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 1 (mediant construction).

Formalized by `MetaMathlibExt.gapMediant`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#gap-mediant).

## The mediant of $0/1$ and $1/1$

With fractions encoded as pairs (numerator, denominator)
of natural numbers, the mediant of the gap bounded by $0/1$ and $1/1$ is $1/2$, that is, the
pair $(1, 2)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 1.

Formalized by `MetaMathlibExt.gapMediant_root`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#gap-mediant-root).

## Mallows' insertion rule

Let $n_1/m_1$ and $n_2/m_2$ be fractions, given as pairs of
natural numbers (numerator, denominator). Mallows' insertion rule inserts between them the
ordered pair of fractions
$\langle (n_1 + n_2)/(m_1 + m_2),\ (n_1 + 2n_2)/(m_1 + 2m_2) \rangle$ if $n_1$ is even, and
$\langle (2n_1 + n_2)/(2m_1 + m_2),\ (n_1 + n_2)/(m_1 + m_2) \rangle$ if $n_1$ is odd.
The rule is applied to adjacent fractions $n_1/m_1 < n_2/m_2$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3 (definition of `MT_{i+1}`).

Formalized by `MetaMathlibExt.mallowsInsert`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-insert).

## Mallows insertion between $0/1$ and $1/1$

Mallows' insertion rule inserts the pair
$\langle 1/2, 2/3 \rangle$ between the fractions $0/1$ and $1/1$, so the first level of the
Mallows tree is $MT_1 = \langle 1/2, 2/3 \rangle$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3.

Formalized by `MetaMathlibExt.mallowsInsert_zero_one`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-insert-zero-one).

## Mallows insertion between $1/2$ and $2/3$

Mallows' insertion rule inserts the pair
$\langle 4/7, 3/5 \rangle$ between the fractions $1/2$ and $2/3$ (here the left fraction $1/2$
has odd numerator).

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 1.

Formalized by `MetaMathlibExt.mallowsInsert_half_twoThirds`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-insert-half-two-thirds).

## One refinement step of the Mallows tree

Let $a_1, a_2, \ldots, a_k$ be a finite list of
fractions, each fraction $n/m$ recorded as the pair $(n, m)$ of natural numbers. Its refinement is
the list obtained by keeping every entry and inserting, between each two consecutive entries
$a_t$ and $a_{t+1}$, the two fractions that Mallows' insertion rule places between them, in the
order the rule gives them. A list with fewer than two entries is its own refinement.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3.

Formalized by `MetaMathlibExt.mallowsRefine`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-refine).

## Fractions inserted by one Mallows step

Fractions $n/m$ are written as pairs $(n, m)$ of
natural numbers. For a list of fractions $a_0, a_1, \dots, a_k$, this is the list obtained by
taking, for $j = 0, 1, \dots, k - 1$ in turn, the two fractions $p_j, q_j$ (in this order) that
Mallows' insertion rule inserts between $a_j$ and $a_{j+1}$, that is, the list
$p_0, q_0, p_1, q_1, \dots, p_{k-1}, q_{k-1}$. It is empty when the list has fewer than two
entries.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3.

Formalized by `MetaMathlibExt.mallowsInserted`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-inserted).

## Mallows levels

Fractions $n/m$ are written as pairs $(n, m)$ of natural numbers. Start
from the list $\langle 0/1, 1/1\rangle$ and refine it repeatedly, each refinement step inserting
between every two adjacent entries the pair of fractions given by Mallows' insertion rule. For
$i \ge 1$, $MT_i$ is the list of the fractions inserted at the $i$-th step: the fractions that
Mallows' rule inserts between adjacent entries of the list obtained after $i - 1$ steps, taken
from left to right, two for each adjacent pair.

After $k$ steps the list has $3^k + 1$ entries, so $MT_i$ has $2 \cdot 3^{i-1}$ entries.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3.

Formalized by `MetaMathlibExt.mallowsLevel`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-level).

## The second Mallows level

The ordered list of fractions inserted at the second step of
Mallows' construction is $MT_2 = \langle 1/3, 2/5, 4/7, 3/5, 3/4, 4/5\rangle$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 1 and Figure 2.

Formalized by `MetaMathlibExt.mallowsLevel_one`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-level-one).

## Children of a Mallows-tree vertex

Let a vertex of the Mallows tree have gap $(a, b)$,
where $a$ and $b$ are fractions, and let $\langle p, q \rangle$ be the pair of fractions that
Mallows' insertion rule inserts between $a$ and $b$. The left, middle and right children of the
vertex have gaps $(a, p)$, $(p, q)$ and $(q, b)$ respectively.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 3.

Formalized by `MetaMathlibExt.mallowsChild`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-child).

## Gaps of the Mallows tree

Fractions $n/m$ are written as pairs $(n, m)$ of natural
numbers. The root of the Mallows tree has gap $(0/1, 1/1)$. If a vertex has gap $(a, b)$ and
Mallows' insertion rule inserts $\langle p, q\rangle$ in $(a, b)$, then its children along the
letters $L$, $M$ and $R$ have gaps $(a, p)$, $(p, q)$ and $(q, b)$. The node of a word $w$ over
$L$, $M$, $R$ is the gap of the vertex reached from the root by following the letters of $w$
from left to right.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 3.

Formalized by `MetaMathlibExt.mallowsNode`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-node).

## Labels of the Mallows tree

For a word $w$ over the letters $L$, $M$, $R$, the label of
the Mallows-tree vertex reached from the root by the path $w$ is the pair
$\langle p, q\rangle$ of fractions that Mallows' insertion rule inserts in the gap $(a, b)$ of
that vertex.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 3 and Figure 3.

Formalized by `MetaMathlibExt.mallowsLabel`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-label).

## Labels of the first Mallows-tree vertices

In the Mallows tree, the root is labelled
$\langle 1/2, 2/3\rangle$, its middle child is labelled $\langle 4/7, 3/5\rangle$ and its right
child is labelled $\langle 3/4, 4/5\rangle$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Figure 3.

Formalized by `MetaMathlibExt.mallowsLabel_small`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-label-small).

## Letter chosen at a Mallows-tree vertex

Let a vertex of the Mallows tree have gap
$(a, b)$ and label $\langle p, q \rangle$, the pair of fractions that Mallows' insertion rule
inserts between $a$ and $b$. For a real number $\alpha$, the letter chosen at this vertex is $L$
if $\alpha < p$; otherwise it is $M$ if $\alpha < q$, and $R$ if $\alpha \ge q$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 4.

Formalized by `MetaMathlibExt.mallowsChoose`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-choose).

## Gaps along the Mallows path of a real number

Fractions $n/m$ are written as pairs
$(n, m)$ of natural numbers. For a gap $(a, b)$ let $\langle p, q\rangle$ be the pair that
Mallows' insertion rule inserts in $(a, b)$. For a real number $\alpha$, the gaps
$I_0, I_1, \dots$ are defined by $I_0 = (0/1, 1/1)$ and, if $I_i = (a, b)$, by
$I_{i+1} = (a, p)$ when $\alpha < p$, $I_{i+1} = (p, q)$ when $p \le \alpha < q$, and
$I_{i+1} = (q, b)$ when $\alpha \ge q$. In the paper's notation, $I_i$ is the gap of the vertex
$\mathrm{pf}_{i+1}(\alpha)$ of the Mallows tree visited at step $i + 1$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 4.

Formalized by `MetaMathlibExt.mallowsInterval`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-interval).

## Mallows representation

For a real number $\alpha$, the Mallows representation
$M(\alpha) = M_1(\alpha) M_2(\alpha) \cdots$ is the infinite word over $\{L, M, R\}$ that records
the path of $\alpha$ down the Mallows tree. Fractions are written as numerator–denominator pairs.
Start with the gap between $0/1$ and $1/1$. At step $i \ge 1$, if the current gap lies between
$a = n_1/m_1$ and $b = n_2/m_2$, let $(p, q)$ be the pair that Mallows' rule inserts into it:
$p = (n_1 + n_2)/(m_1 + m_2)$ and $q = (n_1 + 2n_2)/(m_1 + 2m_2)$ if $n_1$ is even, and
$p = (2n_1 + n_2)/(2m_1 + m_2)$ and $q = (n_1 + n_2)/(m_1 + m_2)$ if $n_1$ is odd. Then
$M_i(\alpha) = L$ and the next gap is $(a, p)$ if $\alpha < p$; $M_i(\alpha) = M$ and the next
gap is $(p, q)$ if $p \le \alpha < q$; and $M_i(\alpha) = R$ and the next gap is $(q, b)$
otherwise.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 4.

Formalized by `MetaMathlibExt.mallowsRep`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep).

## The first Mallows letter below one half

For every real number $\alpha < 1/2$, the first
letter $M_1(\alpha)$ of the Mallows representation of $\alpha$ is $L$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 4 and Figure 4.

Formalized by `MetaMathlibExt.mallowsRep_zero_of_lt`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-zero-of-lt).

## Children in the Stern–Brocot tree

Fractions are pairs $(n, m)$ of natural numbers
(numerator, denominator), and the mediant of $a = n_1/m_1$ and $b = n_2/m_2$ is
$a \oplus b = (n_1 + n_2)/(m_1 + m_2)$. The child of a gap $(a, b)$ in direction $L$ is the
gap $(a, a \oplus b)$, and its child in direction $R$ is the gap $(a \oplus b, b)$. For the gap
of a Stern–Brocot vertex, whose label is $a \oplus b$, these are the gaps of its left and right
children.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 1.

Formalized by `MetaMathlibExt.sternBrocotChild`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-child).

## Labels of the Stern–Brocot tree

Fractions are pairs (numerator, denominator) of
natural numbers, and the mediant of $n_1/m_1$ and $n_2/m_2$ is $(n_1 + n_2)/(m_1 + m_2)$. For a
word $w$ over $\{L, R\}$, start from the gap $(0/1, 1/1)$ and read $w$ from left to right,
replacing the current gap $(a, b)$, with mediant $c$, by $(a, c)$ for each $L$ and by $(c, b)$
for each $R$. The label of $w$ is the mediant of the final gap: the label of the vertex reached
from the root by the path $w$ in the left subtree of the Stern–Brocot tree, whose root is $1/2$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 1 and Figure 1.

Formalized by `MetaMathlibExt.sternBrocotLabel`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-label).

## Small labels of the Stern–Brocot tree

In the left subtree of the Stern–Brocot tree,
the root (reached by the empty path) is labelled $1/2$, and the vertex reached from the root by
the path $LR$ is labelled $2/5$, as numerator–denominator pairs.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Figure 1.

Formalized by `MetaMathlibExt.sternBrocotLabel_small`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-label-small).

## The Stern–Brocot choice at a vertex

Let $\alpha$ be a real number and let $(a, b)$ be
a gap with fractions $a = n_1/m_1$ and $b = n_2/m_2$ (pairs of natural numbers). The letter
chosen at $(a, b)$ is $L$ if $\alpha$ is less than the real number $(n_1 + n_2)/(m_1 + m_2)$,
the value of the mediant of $a$ and $b$ (the label of the Stern–Brocot vertex with this gap),
and $R$ otherwise.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.sternBrocotChoose`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-choose).

## Gaps along the Stern–Brocot path

Fractions are pairs (numerator, denominator) of
natural numbers, and the mediant $a \oplus b$ of $a = n_1/m_1$ and $b = n_2/m_2$ is
$(n_1 + n_2)/(m_1 + m_2)$. For a real number $\alpha$, the gaps $I_0(\alpha), I_1(\alpha), \dots$
are defined by $I_0(\alpha) = (0/1, 1/1)$ and, if $I_j(\alpha) = (a, b)$, by
$I_{j+1}(\alpha) = (a, a \oplus b)$ when $\alpha < a \oplus b$ (as real numbers) and
$I_{j+1}(\alpha) = (a \oplus b, b)$ otherwise. The gap $I_j(\alpha)$ is that of the Stern–Brocot
vertex visited at step $j + 1$, whose label is the fraction $f_{j+1}(\alpha)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.sternBrocotInterval`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-interval).

## Fractions on the Stern–Brocot path

Fractions are pairs (numerator, denominator) of
natural numbers, and the mediant $a \oplus b$ of $a = n_1/m_1$ and $b = n_2/m_2$ is
$(n_1 + n_2)/(m_1 + m_2)$. For a real number $\alpha$, start with the gap $(0/1, 1/1)$; at each
step pass from the gap $(a, b)$ to $(a, a \oplus b)$ if $\alpha < a \oplus b$ (as real numbers)
and to $(a \oplus b, b)$ otherwise. For $j \ge 0$, the fraction $f_{j+1}(\alpha)$ is the mediant
of the gap reached after $j$ steps; in particular $f_1(\alpha) = 1/2$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.sternBrocotFrac`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-frac).

## The Stern–Brocot path starts at $1/2$

For every real number $\alpha$, the first
fraction $f_1(\alpha)$ on the Stern–Brocot path of $\alpha$ is $1/2$, as the pair with numerator
$1$ and denominator $2$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.sternBrocotFrac_zero`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-frac-zero).

## Stern–Brocot representation

For a real number $\alpha$, the Stern–Brocot representation
$SB(\alpha) = SB_1(\alpha) SB_2(\alpha) \cdots$ is the infinite sequence over $\{L, R\}$ obtained
by walking down the Stern–Brocot tree from its vertex $1/2$, the vertex with gap $(0/1, 1/1)$.
The vertex with gap $(a, b)$ has label the mediant $a \oplus b$ and children with gaps
$(a, a \oplus b)$ (left) and $(a \oplus b, b)$ (right). If $f_j(\alpha)$ is the label of the
$j$-th vertex of the walk, then $SB_j(\alpha) = L$ and the walk moves to the left child when
$\alpha < f_j(\alpha)$; otherwise $SB_j(\alpha) = R$ and the walk moves to the right child.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.sternBrocotRep`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-rep).

## First Stern–Brocot letter below one half

For every real number $\alpha < 1/2$, the
first letter $SB_1(\alpha)$ of the Stern–Brocot representation of $\alpha$ is $L$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Definition 2.

Formalized by `MetaMathlibExt.sternBrocotRep_zero_of_lt`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-rep-zero-of-lt).

## The map $\varphi_{SBT}$

Let $a = n_1/m_1$ and $b = n_2/m_2$ be fractions, given by
numerator and denominator, and consider the Stern–Brocot vertex with gap $(a, b)$: its label is
the mediant $f = a \oplus b = (n_1 + n_2)/(m_1 + m_2)$, and its left and right children have
labels $l = a \oplus f$ and $r = f \oplus b$. Then $\varphi_{SBT}$ of this vertex is the pair
$\langle l, f \rangle$ if the numerator of $l$ is even, and $\langle f, r \rangle$ otherwise.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3 (definition of `φ_SBT`).

Formalized by `MetaMathlibExt.sternBrocotPhi`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-phi).

## The map $\psi_{SBT}$

Encode a Stern–Brocot vertex by its gap $(a, b)$ of fractions: its
label is the mediant $a \oplus b$ (numerators added, denominators added), and its left and right
children are the vertices with gaps $(a, a \oplus b)$ and $(a \oplus b, b)$. Let $v_L$ and $v_R$
be the left and right children of a vertex $v$. If the label of $v_L$ has odd numerator, then
$\psi_{SBT}(v)$ is the list consisting of $v_L$ followed by the left and right children of
$v_R$; otherwise it is the list consisting of the left and right children of $v_L$ followed by
$v_R$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3 (definition of `ψ_SBT`).

Formalized by `MetaMathlibExt.sternBrocotPsi`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-psi).

## The maps $\varphi_{SBT}$ and $\psi_{SBT}$ at the root

At the root $1/2$ of the
Stern–Brocot tree (the vertex with gap $(0/1, 1/1)$), $\varphi_{SBT}(1/2) = \langle 1/2, 2/3
\rangle$ and $\psi_{SBT}(1/2) = \langle 1/3, 3/5, 3/4 \rangle$, where the vertices $1/3$, $3/5$
and $3/4$ are the ones with gaps $(0/1, 1/2)$, $(1/2, 2/3)$ and $(2/3, 1/1)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 2.3.

Formalized by `MetaMathlibExt.sternBrocotPhi_psi_root`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-phi-psi-root).

## Transition rule of the parity sequence

The map $\mathrm{step}$ sends a letter of the
parity alphabet $\{O_L, E_R, O_R, E_L\}$ and a letter of $\{L, R\}$ to a letter of the parity
alphabet, by $\mathrm{step}(O_L, L) = O_L$, $\mathrm{step}(O_L, R) = E_R$,
$\mathrm{step}(E_R, L) = O_R$, $\mathrm{step}(E_R, R) = O_L$, $\mathrm{step}(O_R, L) = E_L$,
$\mathrm{step}(O_R, R) = O_R$, $\mathrm{step}(E_L, L) = O_R$ and $\mathrm{step}(E_L, R) = O_L$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3 (definition of `Q`, Figure 5).

Formalized by `MetaMathlibExt.mallowsQStep`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-qstep).

## The parity sequence of a Stern–Brocot word

Let $x = x_0 x_1 x_2 \cdots$ be an infinite
word over $\{L, R\}$. Its parity sequence $Q(x) = Q_0 Q_1 Q_2 \cdots$ over the parity alphabet
$\{O_L, E_R, O_R, E_L\}$ is defined by $Q_0 = O_L$ and $Q_{j+1} = \mathrm{step}(Q_j, x_j)$ for
every $j \ge 0$, where $\mathrm{step}$ is the transition rule of the parity sequence.

Indices start at $0$ here; the source numbers from $1$, so $Q_0$ is the source's $Q_1(x)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.mallowsQ`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-q).

## First values of the parity sequence

Let $x = x_0 x_1 x_2 \cdots$ be an infinite word over
$\{L, R\}$ with $x_0 = R$ and $x_1 = L$. Then the parity sequence $Q(x) = Q_0 Q_1 Q_2 \cdots$ of
$x$ satisfies $Q_0 = O_L$, $Q_1 = E_R$ and $Q_2 = O_R$.

Indices start at $0$ here; in the source these values are $Q_1$, $Q_2$ and $Q_3$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.mallowsQ_small`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-q-small).

## The admissible parity sequences $I$

The set $I$ consists of the infinite sequences
$x = (x_0, x_1, \dots)$ over the alphabet $\{O_L, E_R, O_R, E_L\}$ such that $x_0 = O_L$; no two
consecutive terms $(x_j, x_{j+1})$ form one of the pairs $(O_L, O_R)$, $(O_L, E_L)$,
$(E_R, E_L)$, $(E_R, E_R)$, $(O_R, O_L)$, $(O_R, E_R)$, $(E_L, E_L)$, $(E_L, E_R)$; $x$ is not
eventually constant equal to $O_L$, nor eventually constant equal to $O_R$; and no tail of $x$
is the periodic sequence $(O_L, E_R, O_L, E_R, \dots)$ or $(O_R, E_L, O_R, E_L, \dots)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.mallowsAdmissible`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-admissible).

## The constant sequence $O_L O_L O_L \cdots$ is not admissible

The constant sequence whose
every term is $O_L$ does not belong to the set $I$ of admissible sequences over
$\{O_L, E_R, O_R, E_L\}$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.const_OL_not_mem_mallowsAdmissible`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#const-ol-not-mem-mallows-admissible).

## Odd positions of a parity sequence

Let $x = x_0 x_1 x_2 \cdots$ be an infinite sequence
over the parity alphabet $\{O_L, E_R, O_R, E_L\}$, and call a position $j \ge 0$ odd when
$x_j \in \{O_L, O_R\}$. For $i \ge 0$, the $i$-th odd position of $x$ is the $(i+1)$-st smallest
odd position of $x$, and it is $0$ by convention when $x$ has at most $i$ odd positions.

In the source, positions are numbered from $1$ and the odd positions are enumerated as
$o(1) < o(2) < \cdots$; the $i$-th odd position here is $o(i+1) - 1$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.mallowsOddIndex`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-odd-index).

## The first odd position of a sequence starting with $O_L$

Let $x = x_0 x_1 x_2 \cdots$
be an infinite sequence over the parity alphabet $\{O_L, E_R, O_R, E_L\}$ with $x_0 = O_L$, and
call a position $j \ge 0$ odd when $x_j \in \{O_L, O_R\}$. Then the $0$-th odd position of $x$,
the smallest odd position, is $0$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3 (`o(1) = 1`).

Formalized by `MetaMathlibExt.mallowsOddIndex_zero`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-odd-index-zero).

## The letter rule of $T$

For a truth value $b$ and letters $a, a'$ of
$\{O_L, E_R, O_R, E_L\}$, the letter $\tau(b, a, a') \in \{L, M, R\}$ is defined as follows. If
$b$ is true, it is $L$ when $a = O_L$ and $R$ otherwise. If $b$ is false, it is $M$ when
$a \ne a'$, $L$ when $a = a' = O_R$, and $R$ when $a = a' \ne O_R$.

If $o(1) < o(2) < \cdots$ are the positions of the letters $O_L$ and $O_R$ in a sequence $x$,
then $T_i(x) = \tau(b, x_{o(i)}, x_{o(i+1)})$, where $b$ is true exactly when
$o(i + 1) = o(i) + 1$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3 (definition of `T_i`).

Formalized by `MetaMathlibExt.mallowsTLetter`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-tletter).

## The map $T$

Let $x = \langle x_1, x_2, \dots \rangle$ be a sequence over
$\{O_L, E_R, O_R, E_L\}$ and let $o(1) < o(2) < \cdots$ be the positions $j$ with
$x_j \in \{O_L, O_R\}$. The sequence $T(x) = \langle T_1(x), T_2(x), \dots \rangle$ over
$\{L, M, R\}$ is defined as follows. If $o(i + 1) = o(i) + 1$, then $T_i(x)$ is $L$ when
$x_{o(i)} = O_L$ and $R$ otherwise. If $o(i + 1) \ne o(i) + 1$, then $T_i(x)$ is $M$ when
$x_{o(i)} \ne x_{o(i + 1)}$, $L$ when $x_{o(i)} = x_{o(i + 1)} = O_R$, and $R$ when
$x_{o(i)} = x_{o(i + 1)} \ne O_R$.

If there are only finitely many such positions, $o(i)$ is taken to be $1$ for every $i$ larger
than their number.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 3.

Formalized by `MetaMathlibExt.mallowsT`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-t).

## The finite version $\dot T$ of $T$

Let $y = \langle y_1, \dots, y_n \rangle$ be a finite
word over $\{O_L, E_R, O_R, E_L\}$ and let $p_1 < p_2 < \cdots < p_k$ be the positions $j$ with
$y_j \in \{O_L, O_R\}$. Then $\dot T(y) = \langle t_1, \dots, t_{k-1} \rangle$ is the word over
$\{L, M, R\}$ (empty if $k \le 1$) given as follows. If $p_{i+1} = p_i + 1$, then $t_i$ is $L$
when $y_{p_i} = O_L$ and $R$ otherwise. If $p_{i+1} \ne p_i + 1$, then $t_i$ is $M$ when
$y_{p_i} \ne y_{p_{i+1}}$, $L$ when $y_{p_i} = y_{p_{i+1}} = O_R$, and $R$ when
$y_{p_i} = y_{p_{i+1}} = O_L$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 4.3 (definition of `Ṫ`).

Formalized by `MetaMathlibExt.mallowsTFin`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-tfin).

## Two values of $\dot T$

The finite version $\dot T$ of $T$ satisfies
$\dot T(\langle O_L, E_R, O_R \rangle) = \langle M \rangle$ and
$\dot T(\langle O_L, O_L \rangle) = \langle L \rangle$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 4.3.

Formalized by `MetaMathlibExt.mallowsTFin_small`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-tfin-small).

## Positively Poisson stable sequence

A sequence $x = (x_0, x_1, x_2, \dots)$ with values in
a set $A$ is positively Poisson stable if there is an index $n_0$ such that for every length
$\ell$ there is a shift $p \ge 1$ with $x_{n_0 + p + t} = x_{n_0 + t}$ for all $t < \ell$; that
is, every initial block of the tail $(x_{n_0}, x_{n_0 + 1}, \dots)$ occurs again at a later
position.

This is the shift-space form of the condition that the positive orbit of $x$ under the shift
$\sigma$ meets the $\omega$-limit set of $x$. The point that recurs is $\sigma^{n_0} x$, not
necessarily $x$ itself: for example, $(0, 1, 1, 1, \dots)$ is positively Poisson stable.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 4.2.

Formalized by `MetaMathlibExt.IsPositivelyPoissonStable`, a definition declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#is-positively-poisson-stable).

## Constant sequences are positively Poisson stable

For every set $A$ and every $c \in A$,
the constant sequence $(c, c, c, \dots)$ is positively Poisson stable.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Section 4.2.

Formalized by `MetaMathlibExt.isPositivelyPoissonStable_const`, a theorem declared in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 453](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L453). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#is-positively-poisson-stable-const).

## Stern–Brocot tree: labels, order and paths

Consider the subtree of the Stern–Brocot
tree with root $1/2$, and identify each vertex with its path $w$ from the root, a finite word over
$\{L, R\}$. Then:
(i) every rational $q$ with $0 < q < 1$ is the label of exactly one vertex;
(ii) for all words $u, v_1, v_2$ over $\{L, R\}$ with $v_1$ and $v_2$ of the same length, the
label of $u L v_1$ is less than the label of $u R v_2$;
(iii) if the label of the vertex $w$ has continued fraction expansion $[0; a_1, \ldots, a_\ell]$
with last partial quotient $a_\ell \ge 2$, then $w = L^{a_1 - 1} R^{a_2} L^{a_3} \cdots$, made of
$\ell$ blocks alternating between $L$ and $R$ starting with $L$, where the $k$-th block has
length $a_k$, except that the first block has length $a_1 - 1$ and the last has length
$a_\ell - 1$; if $\ell = 1$, then $w = L^{a_1 - 2}$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 1.

Stated but not proved: `MetaMathlibExt.sternBrocotTree_label_unique_order_path` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-tree-label-unique-order-pat).

## Stern–Brocot representation and continued fractions

Let $\alpha \in (0, 1)$ be
irrational with continued fraction expansion $\alpha = [0; a_1, a_2, \ldots]$, let
$f_1(\alpha), f_2(\alpha), \ldots$ be the fractions labelling the vertices visited by its
Stern–Brocot path, and let $SB(\alpha) = SB_1(\alpha) SB_2(\alpha) \cdots$ be its Stern–Brocot
representation. Then (i) $f_j(\alpha) \to \alpha$ as $j \to \infty$; and (ii)
$SB(\alpha) = L^{a_1 - 1} R^{a_2} L^{a_3} R^{a_4} \cdots$, that is, for all $j \ge 1$ and
$k \ge 0$ with $a_1 + \cdots + a_k \le j < a_1 + \cdots + a_{k+1}$, the letter $SB_j(\alpha)$ is
$L$ if $k$ is even and $R$ if $k$ is odd.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 2.

Stated but not proved: `MetaMathlibExt.sternBrocotRep_tendsto_and_contFract` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-rep-tendsto-and-cont-fract).

## Characterization of Stern–Brocot representations

A sequence over $\{L, R\}$ is the
Stern–Brocot representation $\mathrm{SB}(\alpha)$ of some irrational $\alpha \in (0, 1)$ if and
only if it is neither eventually constantly $L$ nor eventually constantly $R$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Corollary 1.

Stated but not proved: `MetaMathlibExt.image_sternBrocotRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#image-stern-brocot-rep).

## Each rational in $(0, 1)$ occurs once in the Mallows tree, in increasing order on each level

**Each rational in $(0, 1)$ occurs once in the Mallows tree, in increasing order on each
level.** For a finite word $w$ over $\{L, M, R\}$ let $\langle p_w, q_w \rangle$ be the label, a
pair of fractions, of the vertex of the Mallows tree reached from the root by the path $w$;
fractions are compared by their real values. Then: (i) for every rational number $r$ with
$0 < r < 1$ there is exactly one pair $(w, s)$ of a path $w$ and a side
$s \in \{\text{left}, \text{right}\}$ such that the fraction on side $s$ of the label of $w$
($p_w$ for left, $q_w$ for right) has value $r$; (ii) $p_w < q_w$ for every path $w$; (iii) for
all words $u$, $v_1$, $v_2$ over $\{L, M, R\}$ with $v_1$ and $v_2$ of the same length and every
pair $(b, c)$ among $(L, M)$, $(L, R)$, $(M, R)$, we have $q_{u b v_1} < p_{u c v_2}$.

Together, (ii) and (iii) say that on each level $\mathrm{MT}_i$ of the tree the left-to-right
order of the fractions agrees with their increasing order.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 3.

Stated but not proved: `MetaMathlibExt.mallowsTree_label_unique_order` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-tree-label-unique-order).

## Mallows levels from the Stern–Brocot maps

Encode each vertex of the Stern–Brocot tree
(left subtree, root $1/2$) by its gap, so that the root is the gap $(0/1, 1/1)$, and extend
$\psi_{\mathrm{SBT}}$ and $\varphi_{\mathrm{SBT}}$ to lists of vertices by applying them to each
entry and concatenating the results in order. Then for every $i \ge 1$ the ordered list $MT_i$
of fractions inserted at step $i$ of Mallows' construction is
$MT_i = \varphi_{\mathrm{SBT}}(\psi_{\mathrm{SBT}}^{\,i-1}(\langle 1/2\rangle))$, where
$\psi_{\mathrm{SBT}}^{\,i-1}$ is the $(i-1)$-fold iterate and $\langle 1/2\rangle$ is the list
whose only entry is the root.

The paper quotes this identity from Hida, J. Comb. 14 (2023).

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 1.

Stated but not proved: `MetaMathlibExt.mallowsLevel_eq_phi_psi_iterate` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-level-eq-phi-psi-iterate).

## Characterization of Mallows representations

A sequence over $\{L, M, R\}$ is the Mallows
representation $M(\alpha)$ of some irrational $\alpha \in (0, 1)$ if and only if it is neither
eventually constantly $L$ nor eventually constantly $R$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 4.

Stated but not proved: `MetaMathlibExt.image_mallowsRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 536](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L536). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#image-mallows-rep).

## Hida's map $Q$ is a bijection onto $I$

Let $\mathrm{SB}(\alpha)$ be the Stern–Brocot
representation of a real number $\alpha$, let $Q$ be Hida's map from sequences over $\{L, R\}$ to
sequences over $\{O_L, E_R, O_R, E_L\}$, and let $I$ be the set of admissible sequences over
$\{O_L, E_R, O_R, E_L\}$. Then $Q$ maps the set of Stern–Brocot representations
$\{\mathrm{SB}(\alpha) : \alpha \in (0, 1) \text{ irrational}\}$ bijectively onto $I$: for every
irrational $\alpha \in (0, 1)$ the sequence $Q(\mathrm{SB}(\alpha))$ lies in $I$, $Q$ is injective
on this set of representations, and every element of $I$ equals $Q(\mathrm{SB}(\alpha))$ for some
irrational $\alpha \in (0, 1)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 5.

Stated but not proved: `MetaMathlibExt.bijOn_mallowsQ` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 545](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L545). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#bij-on-mallows-q).

## Parity and side of the Stern–Brocot fractions

Let $\alpha \in (0, 1)$ be irrational,
let $f_1(\alpha), f_2(\alpha), \dots$ be the fractions on its Stern–Brocot path, and let
$SB(\alpha) = \langle SB_1, SB_2, \dots \rangle$ be its Stern–Brocot representation. Let
$Q(SB(\alpha)) = \langle Q_1, Q_2, \dots \rangle$ be the sequence over
$\{O_L, E_R, O_R, E_L\}$ with $Q_1 = O_L$ in which $Q_{j+1}$ is determined by $Q_j$ and $SB_j$
as follows: from $O_L$, $L \mapsto O_L$ and $R \mapsto E_R$; from $E_R$, $L \mapsto O_R$ and
$R \mapsto O_L$; from $O_R$, $L \mapsto E_L$ and $R \mapsto O_R$; from $E_L$, $L \mapsto O_R$
and $R \mapsto O_L$. Then for every $j \ge 1$: (i) the numerator of $f_j(\alpha)$ is odd if
and only if $Q_j \in \{O_L, O_R\}$; (ii) $f_j(\alpha)$ is the left or the right element of the
label of some vertex of the Mallows tree; (iii) for every vertex of the Mallows tree, if
$f_j(\alpha)$ is the left element of its label then $Q_j \in \{O_L, E_L\}$, and if it is the
right element then $Q_j \in \{O_R, E_R\}$.

Since every fraction is an element of at most one Mallows label (Proposition 3), (ii) and
(iii) give the paper's equivalence: $f_j(\alpha)$ is the left (resp. right) element of its
Mallows label if and only if $Q_j \in \{O_L, E_L\}$ (resp. $\{O_R, E_R\}$).

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 6.

Stated but not proved: `MetaMathlibExt.sternBrocotFrac_parity_side` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-frac-parity-side).

## Gaps between odd letters of admissible sequences

Let $x = x_0 x_1 x_2 \cdots$ be a
sequence in the admissible set $I$ over the letters $O_L$, $E_R$, $O_R$, $E_L$, and for
$i \ge 0$ let $p_i$ be the $i$-th position (counting from $0$) at which $x$ has one of the
letters $O_L$, $O_R$. Then for every $i \ge 0$, $p_{i+1} > p_i + 1$ holds if and only if
$p_{i+1} = p_i + 2$.

Since the positions increase, this says that consecutive positions of $O_L$ or $O_R$ are at
distance one or two.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 7.

Stated but not proved: `MetaMathlibExt.mallowsOddIndex_gap` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 575](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L575). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-odd-index-gap).

## Hida's map $T$ is a bijection from $I$ onto the Mallows representations

Let $I$ be the
set of admissible sequences over $\{O_L, E_R, O_R, E_L\}$, let $T$ be Hida's map from sequences
over $\{O_L, E_R, O_R, E_L\}$ to sequences over $\{L, M, R\}$, and let $M(\alpha)$ be the Mallows
representation of a real number $\alpha$. Then $T$ maps $I$ bijectively onto the set
$\{M(\alpha) : \alpha \in (0, 1) \text{ irrational}\}$: for every $x \in I$ the sequence $T(x)$
lies in this set, $T$ is injective on $I$, and for every irrational $\alpha \in (0, 1)$ there is
$x \in I$ with $T(x) = M(\alpha)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 8.

Stated but not proved: `MetaMathlibExt.bijOn_mallowsT` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#bij-on-mallows-t).

## Stern–Brocot labels of the Mallows representation vertices

For irrational `α ∈ (0, 1)` and `i ≥ 1`, `φ_SBT(f_{o(i)}(α)) = pf_i(α)`. The vertex
`f_{o(i)}(α)` is encoded by its gap, `pf_i(α)` is the label `⟨p, q⟩` inserted in the gap
`mallowsInterval α (i - 1)`, written as the list `[p, q]`, and `o` is computed on `Q(SB(α))`.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Lemma 1.

Stated but not proved: `MetaMathlibExt.sternBrocotPhi_oddIndex` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 595](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L595). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-phi-odd-index).

## The Mallows representation from the Stern–Brocot representation

For every irrational
number $\alpha$ with $0 < \alpha < 1$, the Mallows representation $M(\alpha)$ is obtained from the
Stern–Brocot representation $\mathrm{SB}(\alpha)$ by applying the map $Q$, which gives a sequence
over $\{O_L, E_R, O_R, E_L\}$, and then the map $T$, which gives a sequence over $\{L, M, R\}$:
$T(Q(\mathrm{SB}(\alpha))) = M(\alpha)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 2.

Stated but not proved: `MetaMathlibExt.mallowsT_mallowsQ_sternBrocotRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-t-mallows-q-stern-brocot-rep).

## Block-matching lemma

Let $\alpha \in (0, 1)$ be irrational, let $x = \mathrm{SB}(\alpha)$
be its Stern–Brocot representation, let $q = Q(x)$ be the image of $x$ under Hida's map $Q$ to
sequences over $\{O_L, E_R, O_R, E_L\}$, and let $T(q)$ be the image of $q$ under Hida's map $T$
to sequences over $\{L, M, R\}$; all sequences are indexed from $0$. Let $o(i)$ be the $i$-th
position, counting from $0$, at which $q$ takes the value $O_L$ or $O_R$. Then for all natural
numbers $\ell$, $j_1$, $j_2$, $i_1$, $i_2$, with $-$ denoting truncated subtraction of natural
numbers:
(i) $x_{j_1 + t} = x_{j_2 + t}$ for all $t < \ell$ together with $q_{j_1} = q_{j_2}$ holds if and
only if $q_{j_1 + t} = q_{j_2 + t}$ for all $t \le \ell$;
(ii) $T(q)_{i_1 + t} = T(q)_{i_2 + t}$ for all $t < \ell$ together with $q_{o(i_1)} = q_{o(i_2)}$
holds if and only if $q_{o(i_1) + t} = q_{o(i_2) + t}$ for all $t \le o(i_1 + \ell) - o(i_1)$;
(iii) if $T(q)_{i_1 + t} = T(q)_{i_2 + t}$ for all $t < \ell$ and $q_{o(i_1)} = q_{o(i_2)}$, then
$o(i_2 + k) - o(i_2) = o(i_1 + k) - o(i_1)$ for all $k \le \ell$.

The paper assumes $\ell \ge 1$, $j_1 < j_2$ and $i_1 < i_2$; the statement is trivial for
$\ell = 0$, symmetric in the two positions, and trivial for equal positions.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Lemma 2.

Stated but not proved: `MetaMathlibExt.block_match_sternBrocot_mallowsQ` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#block-match-stern-brocot-mallows-q).

## Blocks of $T(Q(\mathrm{SB}(\alpha)))$ and of $Q(\mathrm{SB}(\alpha))$

Let $X$ be one of
the letters $O_L, E_R, O_R, E_L$, let $u = u_1 \cdots u_\ell$ be a finite word over $\{L, R\}$,
and let $\dot Q^X(u) = \langle X_0, X_1, \dots, X_\ell \rangle$ be the word with $X_0 = X$ and
$X_k = \delta(X_{k-1}, u_k)$ for $1 \le k \le \ell$, where $\delta$ is the transition rule that
defines the map $Q$ from sequences over $\{L, R\}$ to sequences over $\{O_L, E_R, O_R, E_L\}$.
Assume that $X_\ell$ is $O_L$ or $O_R$, and let $n$ be the length of the word
$\dot T(\dot Q^X(u))$, where $\dot T$ is the finite version of the map $T$ from sequences over
$\{O_L, E_R, O_R, E_L\}$ to sequences $T(x) = \langle T_1(x), T_2(x), \dots \rangle$ over
$\{L, M, R\}$. Let $\alpha$ be an irrational number with $0 < \alpha < 1$, let
$\mathrm{SB}(\alpha)$ be its Stern–Brocot representation, write
$x = Q(\mathrm{SB}(\alpha)) = \langle x_1, x_2, \dots \rangle$, let $o(1) < o(2) < \cdots$ be the
positions $j$ with $x_j \in \{O_L, O_R\}$, and let $i_0 \ge 1$. Then the $n$ letters
$T_{i_0}(x), \dots, T_{i_0 + n - 1}(x)$ form the word $\dot T(\dot Q^X(u))$ and $x_{o(i_0)} = X$
if and only if the $\ell + 1$ letters $x_{o(i_0)}, x_{o(i_0) + 1}, \dots, x_{o(i_0) + \ell}$ form
the word $\dot Q^X(u)$.

The source assumes $X \in \{O_L, O_R\}$ and $\ell \ge 1$. For $X \in \{E_R, E_L\}$ both sides are
false, since $x_{o(i_0)}$ is $O_L$ or $O_R$; for $\ell = 0$ both sides say $x_{o(i_0)} = X$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Lemma 3.

Stated but not proved: `MetaMathlibExt.mallowsT_startsWith_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-t-starts-with-iff).

## The letter $M$ in $T(Q(\mathrm{SB}(\alpha)))$ marks the ends of runs

Let
$\alpha \in (0, 1)$ be irrational, let $x = Q(\mathrm{SB}(\alpha))$ be the sequence over
$\{O_L, E_R, O_R, E_L\}$ obtained from the Stern–Brocot representation $\mathrm{SB}(\alpha)$, and
let $o(1) < o(2) < \cdots$ be the positions $j$ with $x_j \in \{O_L, O_R\}$. Let
$e_1, e_2, \ldots$ be positive integers such that
$(x_{o(1)}, x_{o(2)}, \ldots) = O_L^{e_1} O_R^{e_2} O_L^{e_3} \cdots$, that is, for every
$k \ge 0$ and every $i$ with $e_1 + \cdots + e_k < i \le e_1 + \cdots + e_{k+1}$ (the empty sum
being $0$), $x_{o(i)}$ is $O_L$ if $k$ is even and $O_R$ if $k$ is odd. Then for every $i \ge 1$,
the $i$-th letter $T_i(x)$ of $T(x)$ is $M$ if and only if $i = e_1 + \cdots + e_k$ for some
$k \ge 1$.

The source assumes that $O_L$ and $O_R$ both occur infinitely often among the $x_{o(i)}$; this
is exactly what makes such $e_k$ exist, so the run decomposition is taken as a hypothesis.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Lemma 4.

Stated but not proved: `MetaMathlibExt.mallowsT_eq_M_iff_runEnd` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-t-eq-m-iff-run-end).

## Mallows and Stern–Brocot representations are eventually periodic together

For every
irrational $\alpha \in (0, 1)$, the Mallows representation $M(\alpha)$ is eventually periodic if
and only if the Stern–Brocot representation $\mathrm{SB}(\alpha)$ is eventually periodic.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 3.

Stated but not proved: `MetaMathlibExt.isEventuallyPeriodic_mallowsRep_iff_sternBrocotRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#is-eventually-periodic-mallows-rep-iff-s).

## Lagrange's theorem for Mallows representations

For every irrational $\alpha \in (0, 1)$,
the Mallows representation $M(\alpha)$ is eventually periodic if and only if $\alpha$ is a real
quadratic irrational, that is, algebraic of degree $2$ over $\mathbb{Q}$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Corollary 2.

Stated but not proved: `MetaMathlibExt.isEventuallyPeriodic_mallowsRep_iff_quadratic` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#is-eventually-periodic-mallows-rep-iff-q).

## Poisson stability of the Mallows and Stern–Brocot representations

For every irrational
$\alpha \in (0, 1)$, the Mallows representation of $\alpha$ is positively Poisson stable if and
only if the Stern–Brocot representation of $\alpha$ is positively Poisson stable.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 4.

Stated but not proved: `MetaMathlibExt.isPositivelyPoissonStable_mallowsRep_iff_sternBrocotRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#is-positively-poisson-stable-mallows-rep).

## Poisson stability of the Mallows representation and the continued fraction

Let
$\alpha \in (0, 1)$ be irrational, with continued fraction expansion
$\alpha = [0; a_1, a_2, \dots]$. Then the Mallows representation of $\alpha$ is positively
Poisson stable if and only if the sequence $(a_1, a_2, \dots)$ of its partial quotients is
positively Poisson stable.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Corollary 3.

Stated but not proved: `MetaMathlibExt.isPositivelyPoissonStable_mallowsRep_iff_contFract` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#is-positively-poisson-stable-mallows-rep-2).

## Transitivity of the Mallows and Stern–Brocot representations

Let $\alpha \in (0, 1)$ be
irrational. Every finite word over the alphabet $\{L, M, R\}$ occurs as a factor of the Mallows
representation of $\alpha$ if and only if every finite word over the alphabet $\{L, R\}$ occurs
as a factor of the Stern–Brocot representation of $\alpha$; that is, the Mallows representation
of $\alpha$ is transitive if and only if its Stern–Brocot representation is. The empty word
occurs trivially.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 5.

Stated but not proved: `MetaMathlibExt.transitive_mallowsRep_iff_sternBrocotRep` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 727](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L727). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#transitive-mallows-rep-iff-stern-brocot).

## Transitive Mallows representations and continued fractions

Let $\alpha \in (0, 1)$ be
irrational with continued fraction expansion $\alpha = [0; a_1, a_2, \ldots]$. The Mallows
representation of $\alpha$ is transitive, that is, every finite word over $\{L, M, R\}$ occurs
in it as a factor, if and only if every finite word over the positive integers occurs as a
factor of the sequence $a_1 a_2 a_3 \cdots$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Corollary 4.

Stated but not proved: `MetaMathlibExt.transitive_mallowsRep_iff_contFract` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 737](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L737). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#transitive-mallows-rep-iff-cont-fract).

## Mallows representations without the letter $M$

Let $\alpha \in (0, 1)$ be irrational,
with continued fraction expansion $\alpha = [0; a_1, a_2, \ldots]$. The letter $M$ does not occur
in the Mallows representation $M(\alpha)$ if and only if $a_{2k}$ is even for every $k \ge 1$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 9.

Stated but not proved: `MetaMathlibExt.mallowsRep_ne_M_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ne-m-iff).

## Mallows representations without the letter $R$

Let $\alpha \in (0, 1)$ be irrational,
with continued fraction expansion $\alpha = [0; a_1, a_2, \ldots]$. The letter $R$ does not occur
in the Mallows representation $M(\alpha)$ if and only if $a_2 = 1$, $a_3$ is even, and the
sequence $a_4, a_5, \ldots$ is a concatenation of blocks, each of the form $(2, b)$ or
$(1, c, 1, b)$ with $b$ even. Equivalently,
$(a_1, a_2, \ldots) = (e'_1, 1, 2e'_2)\, w_1\, (2e'_3)\, w_2\, (2e'_4) \cdots$ with positive
integers $e'_k$ and each $w_k$ equal to $(2)$ or $(1, e''_k, 1)$ for a positive integer $e''_k$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 10.

Stated but not proved: `MetaMathlibExt.mallowsRep_ne_R_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ne-r-iff).

## Mallows representations without the letter $L$

Let $\alpha \in (0, 1)$ be irrational,
with continued fraction expansion $\alpha = [0; a_1, a_2, \ldots]$. The letter $L$ does not occur
in the Mallows representation $M(\alpha)$ if and only if $a_1 = 1$, $a_2$ is odd, and the
sequence $a_3, a_4, \ldots$ is a concatenation of blocks, each of the form $(2, b)$ or
$(1, c, 1, b)$ with $b$ even. Equivalently,
$(a_1, a_2, \ldots) = (1, 2e'_1 - 1)\, w_1\, (2e'_2)\, w_2\, (2e'_3) \cdots$ with positive integers
$e'_k$ and each $w_k$ equal to $(2)$ or $(1, e''_k, 1)$ for a positive integer $e''_k$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 11.

Stated but not proved: `MetaMathlibExt.mallowsRep_ne_L_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 777](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L777). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ne-l-iff).

## The numerator parities are not eventually constant

Let $\alpha \in (0, 1)$ be
irrational and let $f_1(\alpha), f_2(\alpha), \dots$ be the fractions on its Stern–Brocot path.
Then there are no natural numbers $c$ and $j_0$ such that the numerator of $f_j(\alpha)$ has
remainder $c$ modulo $2$ for all $j \ge j_0$: the parities of these numerators are not
eventually constant.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 12.

Stated but not proved: `MetaMathlibExt.sternBrocotFrac_parity_not_eventually_const` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 789](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L789). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#stern-brocot-frac-parity-not-eventually).

## Eventually alternating parities of Stern–Brocot numerators

Let $\alpha$ be an irrational
number with $0 < \alpha < 1$, let $f_1(\alpha), f_2(\alpha), \dots$ be the fractions on its
Stern–Brocot path, and let $M(\alpha) = \langle M_1(\alpha), M_2(\alpha), \dots \rangle$ be its
Mallows representation. The following are equivalent: (a) there is $j_0$ such that for every
$j \ge j_0$ the numerators of $f_j(\alpha)$ and $f_{j+1}(\alpha)$ have different parities;
(b) the letter $M$ occurs infinitely often in $M(\alpha)$, and, writing $m_1 < m_2 < \cdots$ for
the positions $i$ with $M_i(\alpha) = M$, there is an integer $k \ge 1$ such that for every
$t \ge 2k$ and every $i$ with $m_t < i < m_{t+1}$ we have $M_i(\alpha) = R$ if $t$ is even and
$M_i(\alpha) = L$ if $t$ is odd.

In other words, from the $2k$-th occurrence of $M$ on,
$M(\alpha) = M R^{e'_1} M L^{e'_2} M R^{e'_3} M \cdots$ with all $e'_i \ge 0$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 13.

Stated but not proved: `MetaMathlibExt.parity_eventually_alternating_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 801](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L801). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#parity-eventually-alternating-iff).

## Eventual period three of the numerator parities

Let $\alpha \in (0, 1)$ be
irrational, let $f_1(\alpha), f_2(\alpha), \dots$ be the fractions on its Stern–Brocot path,
with numerators $p_1, p_2, \dots$, and let $M(\alpha) = \langle M_1, M_2, \dots \rangle$ be its
Mallows representation. Then there is $j_0 \ge 1$ with $p_{j+3} \equiv p_j \pmod 2$ for all
$j \ge j_0$ if and only if one of the following holds:
(a) there is $i_0 \ge 1$ such that $M_{i_0 + 2t} = L$ and $M_{i_0 + 2t + 1} = R$ for all
$t \ge 0$;
(b) the letter $M$ occurs infinitely often in $M(\alpha)$, and so do the letters other than
$M$; writing $u_1, u_2, \dots$ for the sequence obtained from $M(\alpha)$ by deleting every
$M$, there is $s \ge 1$ with $u_{s + 2t} = L$ and $u_{s + 2t + 1} = R$ for all $t \ge 0$; and,
writing $m(1) < m(2) < \cdots$ for the positions of $M$ in $M(\alpha)$, there is $k \ge 1$
such that for all $k' \ge k$ we have $M_{m(2k') - 1} = R$, $M_{m(2k') + 1} = L$,
$M_{m(2k'+1) - 1} = L$ and $M_{m(2k'+1) + 1} = R$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 14.

Stated but not proved: `MetaMathlibExt.parity_eventually_period_three_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 818](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L818). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#parity-eventually-period-three-iff).

## Typical properties of Mallows representations

Each of the following holds for
Lebesgue-almost every $\alpha \in (0, 1)$, provided $\alpha$ is irrational: (i) the Mallows
representation $M(\alpha)$ is not eventually periodic; (ii) $M(\alpha)$ is positively Poisson
stable; (iii) $M(\alpha)$ is transitive, that is, every finite word over $\{L, M, R\}$ occurs in
$M(\alpha)$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Proposition 15.

Stated but not proved: `MetaMathlibExt.mallowsRep_ae_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 838](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L838). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ae-properties).

## Factor complexity of almost every Mallows representation

For almost every irrational
$\alpha \in (0, 1)$, with respect to Lebesgue measure, the factor complexity of the Mallows
representation $M(\alpha)$ satisfies $p_{M(\alpha)}(n) = 3^n$ for every $n \ge 0$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Corollary 5.

Stated but not proved: `MetaMathlibExt.mallowsRep_ae_factorComplexity` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 851](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L851). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ae-factor-complexity).

## Words without bounded gaps in almost every Mallows representation

For Lebesgue-almost
every $\alpha \in (0, 1)$, if $\alpha$ is irrational, then there is a finite word $w$ over
$\{L, M, R\}$ that does not occur relatively densely in the Mallows representation
$M(\alpha) = M_1(\alpha) M_2(\alpha) \cdots$: there is no $\ell > 0$ such that, for every
$i \ge 0$, the window $M_{i+1}(\alpha) \cdots M_{i+\ell}(\alpha)$ contains an occurrence of $w$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Corollary 6.

Stated but not proved: `MetaMathlibExt.mallowsRep_ae_not_relativelyDense` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 861](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L861). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ae-not-relatively-dense).

## Words of frequency zero in almost every Mallows representation

Let $w$ be a finite word
over $\{L, M, R\}$ that contains the letter $M$ or contains both $L$ and $R$. Then for almost
every irrational $\alpha \in (0, 1)$, with respect to Lebesgue measure, $w$ has frequency $0$ in
the Mallows representation $M(\alpha) = M_0(\alpha) M_1(\alpha) M_2(\alpha) \cdots$: if $N_n$ is
the number of positions $i < n$ with $M_i(\alpha) M_{i+1}(\alpha) \cdots M_{i+|w|-1}(\alpha) = w$,
then $N_n / n \to 0$ as $n \to \infty$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 6.

Stated but not proved: `MetaMathlibExt.mallowsRep_ae_frequency_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 871](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L871). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ae-frequency-zero).

## Matching fractions of almost every Mallows representation

For almost every irrational
$\alpha \in (0, 1)$, with respect to Lebesgue measure, the Mallows representation
$M(\alpha) = M_0(\alpha) M_1(\alpha) M_2(\alpha) \cdots$ satisfies, for every $\ell \ge 0$,

$$\lim_{n \to \infty} \frac{|\{i < n : M_i(\alpha) = M_{i+\ell}(\alpha)\}|}{n} = 1,$$

that is, its $\ell$-th matching fraction is $1$.

For $\ell = 0$ the statement is trivial; the source states it for $\ell \ge 1$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 7.

Stated but not proved: `MetaMathlibExt.mallowsRep_ae_matchingFraction_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 884](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L884). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-ae-matching-fraction-one).

## Extremal measures of Mallows cylinder sets

Let $\ell \ge 0$. For a word
$w = w_1 \cdots w_\ell$ over $\{L, M, R\}$, let $C_w$ be the set of irrational $\alpha \in (0, 1)$
whose Mallows representation begins with $w$, that is, $M_t(\alpha) = w_t$ for $1 \le t \le \ell$.
Over the $3^\ell$ words $w$ of length $\ell$, the Lebesgue measure of $C_w$ attains the maximum
value $1/(\ell + 1)$ and the minimum value

$$\frac{4\sqrt{2}}{(1 + \sqrt{2})^{2\ell + 2} - (1 - \sqrt{2})^{2\ell + 2}}.$$

For $\ell = 0$ both values equal $1$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 8.

Stated but not proved: `MetaMathlibExt.mallowsRep_cylinder_measure_extrema` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 895](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L895). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-cylinder-measure-extrema).

## Measure bound for the letter $M$ at a fixed position

For every $i \ge 1$, the set of
irrational $\alpha \in (0, 1)$ whose Mallows representation has $i$-th letter
$M_i(\alpha) = M$ has Lebesgue measure less than $3 - 2\sqrt{2}$.

## Sources

- Takanori Hida, *The Mallows Representation of the Irrational Numbers*, INTEGERS 25 (2025), Article A78, Theorem 9.

Stated but not proved: `MetaMathlibExt.mallowsRep_eq_M_measure_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/MallowsRepresentationWanted.lean, line 910](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MallowsRepresentationWanted.lean#L910). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html#mallows-rep-eq-m-measure-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mallows representation of irrational numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/mallows-representation-of-irrational-numbers)
