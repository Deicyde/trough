---
declaration: section
origin: cited
lean: MetaMathlibExt.subRepCount, MetaMathlibExt.diffBasisNumber, MetaMathlibExt.groupDiffBasisNumber, MetaMathlibExt.boundedDiffSetNumber, MetaMathlibExt.subRepCount_zero, MetaMathlibExt.diffBasisNumber_one_one, MetaMathlibExt.groupDiffBasisNumber_one_zmod_three, MetaMathlibExt.boundedDiffSetNumber_le
statement: formalized
---

# Difference bases

26 results, 9 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html).

## Difference representation function

For a finite subset $A$ of an abelian group $G$ and
an element $x \in G$, the difference representation function $r_{A-A}(x)$ is the number of
ordered pairs $(a, a') \in A \times A$ with $a - a' = x$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 1.

Formalized by `MetaMathlibExt.subRepCount`, a definition declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#sub-rep-count).

## The $g$-difference basis number

For a finite set $A \subseteq \mathbb{Z}$ and
$x \in \mathbb{Z}$, write $r_{A-A}(x)$ for the number of ordered pairs $(a, a') \in A \times A$
with $a - a' = x$. For natural numbers $g$ and $n$, a finite set $A \subseteq \mathbb{Z}$ is a
$g$-difference basis for $[n] = \{1, \dots, n\}$ if $r_{A-A}(x) \ge g$ for every $x \in [n]$, and
$\eta_g(n)$ is the least size of such a set.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 1.

Formalized by `MetaMathlibExt.diffBasisNumber`, a definition declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#diff-basis-number).

## Difference basis number of an abelian group

For an abelian group $G$ and
$g \in \mathbb{N}$, a $g$-difference basis of $G$ is a finite set $A \subseteq G$ such that every
$x \in G$ equals $a - a'$ for at least $g$ ordered pairs $(a, a') \in A \times A$. The difference
basis number $\eta_g(G)$ is the least size of a $g$-difference basis of $G$, and $0$ if $G$ has
none.

There is no $g$-difference basis when $G$ is infinite and $g \ge 1$, or when $G$ is finite and
$g > |G|$, since each element is $a - a'$ for at most $|A| \le |G|$ pairs; in these cases the
value $0$ is a convention. When $G$ is finite and $g \le |G|$, the set $A = G$ is a
$g$-difference basis, so $\eta_g(G)$ is a true minimum. This is the paper's $\eta_g(S)$ with
$S = G$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Sections 1 and 3.

Formalized by `MetaMathlibExt.groupDiffBasisNumber`, a definition declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#group-diff-basis-number).

## Maximal sets with bounded difference multiplicities

For a finite set
$A \subseteq \mathbb{Z}$ and $x \in \mathbb{Z}$, write $r_{A-A}(x)$ for the number of ordered
pairs $(a, a') \in A \times A$ with $a - a' = x$. For natural numbers $g$ and $n$, $\alpha_g(n)$
is the largest size of a set $A \subseteq [n] = \{1, \dots, n\}$ with $r_{A-A}(x) \le g$ for
every nonzero integer $x$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Sections 1 and 4.

Formalized by `MetaMathlibExt.boundedDiffSetNumber`, a definition declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#bounded-diff-set-number).

## Representations of zero as a difference

For every finite subset $A$ of an abelian
group, $r_{A-A}(0) = |A|$: the number of ordered pairs $(a, a') \in A \times A$ with
$a - a' = 0$ equals the number of elements of $A$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 1.

Formalized by `MetaMathlibExt.subRepCount_zero`, a theorem declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#sub-rep-count-zero).

## The value $\eta_1(1) = 2$

Let $\eta_1(1)$ be the least size of a finite set
$A \subseteq \mathbb{Z}$ containing elements $a, a'$ with $a - a' = 1$. Then $\eta_1(1) = 2$: such a
set needs two elements, and $\{0, 1\}$ is one.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 1.

Formalized by `MetaMathlibExt.diffBasisNumber_one_one`, a theorem declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#diff-basis-number-one-one).

## Difference basis number of $\mathbb{Z}/3\mathbb{Z}$

The least size
$\eta_1(\mathbb{Z}/3\mathbb{Z})$ of a set $A \subseteq \mathbb{Z}/3\mathbb{Z}$ such that every
element of $\mathbb{Z}/3\mathbb{Z}$ is a difference $a - a'$ of two elements of $A$ equals $2$:
the set $\{0, 1\}$ has differences $0, 1, 2$, and one element is not enough.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 3.

Formalized by `MetaMathlibExt.groupDiffBasisNumber_one_zmod_three`, a theorem declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#group-diff-basis-number-one-zmod-three).

## Trivial upper bound for sets with bounded difference multiplicities

For natural numbers
$g$ and $n$, let $\alpha_g(n)$ be the largest size of a set $A \subseteq [n] = \{1, \dots, n\}$
such that every nonzero integer $x$ is the difference $a - a'$ of at most $g$ ordered pairs
$(a, a') \in A \times A$. Then $\alpha_g(n) \le n$, since these sets are subsets of $[n]$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 4.

Formalized by `MetaMathlibExt.boundedDiffSetNumber_le`, a theorem declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#bounded-diff-set-number-le).

## The value $\alpha_g(1) = 1$

For natural numbers $g$ and $n$, let $\alpha_g(n)$ be the
largest size of a set $A \subseteq \{1, \dots, n\}$ such that every nonzero integer $x$ is the
difference $a - a'$ of at most $g$ ordered pairs $(a, a') \in A \times A$. Then for every natural
number $g$ we have $\alpha_g(1) = 1$: the singleton $\{1\}$ has no nonzero differences.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Section 4.

Formalized by `MetaMathlibExt.boundedDiffSetNumber_one`, a theorem declared in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#bounded-diff-set-number-one).

## Trivial lower bound for difference bases of an interval

Let $g, n \in \mathbb{N}$ with
$n > 1$, and let $\eta_g(n)$ be the least size of a finite set $A \subseteq \mathbb{Z}$ such that
every $x \in \{1, \dots, n\}$ equals $a - a'$ for at least $g$ ordered pairs
$(a, a') \in A \times A$. Then $\eta_g(n) / \sqrt{n} \ge \sqrt{2g}$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 1.

Stated but not proved: `MetaMathlibExt.sqrt_two_mul_le_diffBasisNumber_div_sqrt` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#sqrt-two-mul-le-diff-basis-number-div-sq).

## Rédei–Rényi difference basis

Let $n \ge 1$ and $k = \lceil \sqrt{n} \rceil$. The set
of integers $B_n = \{1, \dots, k - 1\} \cup \{k, 2k, \dots, k^2, (k + 1)k\}$ has $2k$ elements,
and every $x \in \{1, \dots, n\}$ is a difference $b - b'$ of two elements of $B_n$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 2.

Stated but not proved: `MetaMathlibExt.redeiRenyi_diffBasis` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#redei-renyi-diff-basis).

## Upper bound for the $g$-difference basis number

For natural numbers $g$ and $n$, let
$\eta_g(n)$ be the least size of a finite set $A \subseteq \mathbb{Z}$ such that every
$x \in \{1, \dots, n\}$ is the difference $a - a'$ of at least $g$ ordered pairs
$(a, a') \in A \times A$. Then for all natural numbers $g$ and $n$,

$$\frac{\eta_g(n)}{\sqrt{n}} \le 2\left(1 + \frac{1}{\sqrt{n}}\right) g,$$

where for $n = 0$ both quotients are read with the convention that division by $0$ gives $0$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Corollary 1.

Stated but not proved: `MetaMathlibExt.diffBasisNumber_div_sqrt_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#diff-basis-number-div-sqrt-le).

## Comparing $g$-difference bases with difference bases

For natural numbers $g$ and $n$,
let $\eta_g(n)$ be the least size of a finite set $A \subseteq \mathbb{Z}$ such that every
$x \in \{1, \dots, n\}$ is the difference $a - a'$ of at least $g$ ordered pairs
$(a, a') \in A \times A$. If $n > 1$ and $g \ge 1$, then
$\eta_1(n) \le \eta_g(n) \le g\,\eta_1(n)$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Corollary 2.

Stated but not proved: `MetaMathlibExt.diffBasisNumber_one_le_and_le_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#diff-basis-number-one-le-and-le-mul).

## Kravitz's question: the normalized difference basis numbers converge

For a finite set
$A$ of integers and an integer $x$, write $r_{A-A}(x)$ for the number of ordered pairs
$(a, a') \in A \times A$ with $a - a' = x$. For every integer $g \ge 1$, let $\eta_g(n)$ be the
least size of a finite set $A$ of integers with $r_{A-A}(x) \ge g$ for every integer
$x \in [1, n]$. Then there is a real number $c > 0$ with $\eta_g(n) / \sqrt{n} \to c$ as
$n \to \infty$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Theorem 1.

Stated but not proved: `MetaMathlibExt.tendsto_diffBasisNumber_div_sqrt` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#tendsto-diff-basis-number-div-sqrt).

## Singer product construction of difference bases

Let $g, q, v \in \mathbb{N}$ and
$m = q^2 + q + 1$. Let $a_0, \dots, a_q$ be integers in $\{1, \dots, m\}$ such that every
$r \in \{1, \dots, m - 1\}$ is congruent modulo $m$ to $a_i - a_j$ for exactly one ordered pair
$(i, j)$ with $i \ne j$ (a Singer difference set modulo $m$). Let $B$ be a finite set of
integers such that every $x \in \{1, \dots, v\}$ equals $b - b'$ for at least $g$ ordered pairs
$(b, b') \in B \times B$. Then, with $F = \{a_i + mb : 0 \le i \le q,\ b \in B\}$, every
$s \in \{1, \dots, mv\}$ equals $f - f'$ for at least $g$ ordered pairs $(f, f') \in F \times F$.

All $q + 1$ Singer elements are used; the paper prints $1 \le i \le q$, for which the statement
fails.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 4.

Stated but not proved: `MetaMathlibExt.singer_product_diffBasis` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#singer-product-diff-basis).

## Scaling bound for the $g$-difference basis number

For natural numbers $g$ and $m$, let
$\eta_g(m)$ be the least size of a finite set $A \subseteq \mathbb{Z}$ such that every
$x \in \{1, \dots, m\}$ is the difference $a - a'$ of at least $g$ ordered pairs
$(a, a') \in A \times A$. If $q$ is a prime and $n$ and $v$ are natural numbers with
$n \le q^2 v$, then $\eta_g(n) \le (q + 1)\,\eta_g(v)$.

For $v \ge 1$ the hypothesis $n \le q^2 v$ says $\sqrt{n/v} \le q$. Corrected reading: the paper
prints the factor $q$, obtained from the misprinted Lemma 4; its proof gives $q + 1$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Corollary 3.

Stated but not proved: `MetaMathlibExt.diffBasisNumber_le_succ_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#diff-basis-number-le-succ-mul).

## Products of difference bases

Let $G_1, G_2$ be abelian groups, $g_1, g_2 \in \mathbb{N}$,
and $A_1 \subseteq G_1$, $A_2 \subseteq G_2$ finite sets. If every element of $G_1$ equals $a - a'$
for at least $g_1$ ordered pairs $(a, a') \in A_1 \times A_1$, and every element of $G_2$ equals
$a - a'$ for at least $g_2$ ordered pairs $(a, a') \in A_2 \times A_2$, then every element of
$G_1 \times G_2$ equals $z - z'$ for at least $g_1 g_2$ ordered pairs
$(z, z') \in (A_1 \times A_2) \times (A_1 \times A_2)$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 5.

Stated but not proved: `MetaMathlibExt.subRepCount_prod_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#sub-rep-count-prod-ge).

## Difference bases of the integers modulo a prime

For every prime $p$, the least size
$\eta_1(\mathbb{Z}/p\mathbb{Z})$ of a set $A \subseteq \mathbb{Z}/p\mathbb{Z}$ such that every
residue modulo $p$ is a difference $a - a'$ of two elements of $A$ satisfies
$\eta_1(\mathbb{Z}/p\mathbb{Z}) \le 2 \lceil \sqrt{p} \rceil$.

The bound comes from reducing the Rédei–Rényi set modulo $p$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, equation (5) after Lemma 5.

Stated but not proved: `MetaMathlibExt.groupDiffBasisNumber_zmod_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#group-diff-basis-number-zmod-le).

## Difference bases of the square of a finite field

For an abelian group $G$ let
$\eta_1(G)$ be the least size of a set $A \subseteq G$ such that every element of $G$ is a
difference $a - a'$ of two elements of $A$. If $K$ is a finite field with $q$ elements whose
characteristic is not $2$, then $\eta_1(K \times K) \le q + \eta_1(K)$, where $K$ and
$K \times K$ are taken as additive groups.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 6.

Stated but not proved: `MetaMathlibExt.groupDiffBasisNumber_prod_self_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#group-diff-basis-number-prod-self-le).

## Square-root bound for difference bases of finite fields

For every finite field $K$ with
$q$ elements, the least size $\eta_1(K)$ of a set $A \subseteq K$ such that every element of $K$
is a difference $a - a'$ of two elements of $A$ satisfies $\eta_1(K) \le 100 \sqrt{q}$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 7.

Stated but not proved: `MetaMathlibExt.groupDiffBasisNumber_le_hundred_sqrt` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#group-diff-basis-number-le-hundred-sqrt).

## Difference bases of $\mathbb{F}_{p^t} \times \mathbb{F}_{p^t}$

Let $p$ be an odd prime.
For a finite abelian group $G$, a set $A \subseteq G$ and $x \in G$, write $r_{A-A}(x)$ for the
number of ordered pairs $(a, a') \in A \times A$ with $a - a' = x$, and let $\eta_1(G)$ be the
least size of a set $A \subseteq G$ with $r_{A-A}(x) \ge 1$ for every $x \in G$. Then
$\eta_1(\mathbb{F}_{p^t} \times \mathbb{F}_{p^t}) / p^t \to 1$ as $t \to \infty$, that is,
$\eta_1(\mathbb{F}_{p^t} \times \mathbb{F}_{p^t}) = (1 + o(1))\, p^t$, where $\mathbb{F}_{p^t}$
is the field with $p^t$ elements.

The restriction to odd $p$ is deliberate: for $p = 2$ the claim fails.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 8.

Stated but not proved: `MetaMathlibExt.tendsto_groupDiffBasisNumber_galoisField_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#tendsto-group-diff-basis-number-galois-f).

## Even and odd limits for difference bases of $\mathbb{F}_p^n$

Let $p$ be an odd prime and
$g \ge 1$ an integer. For a finite abelian group $G$, a set $A \subseteq G$ and $x \in G$, write
$r_{A-A}(x)$ for the number of ordered pairs $(a, a') \in A \times A$ with $a - a' = x$, and let
$\eta_g(G)$ be the least size of a set $A \subseteq G$ with $r_{A-A}(x) \ge g$ for every $x \in G$.
Then there are real numbers $L_e > 0$ and $L_o > 0$ such that, as $k \to \infty$,
$\eta_g(\mathbb{F}_p^{2k}) / \sqrt{p^{2k}} \to L_e$ and
$\eta_g(\mathbb{F}_p^{2k+1}) / \sqrt{p^{2k+1}} \to L_o$, where $\mathbb{F}_p^n$ is the additive
group of $n$-tuples over the field $\mathbb{F}_p$ with $p$ elements.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Theorem 2.

Stated but not proved: `MetaMathlibExt.tendsto_groupDiffBasisNumber_even_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#tendsto-group-diff-basis-number-even-odd).

## Nonzero differences of the Bose–Chowla set avoid the subgroup of order $g$

Let $q$
and $g$ be natural numbers with $g \mid q - 1$, let $K$ be a finite field with $q^2$ elements, and
let $\theta \in K$ be a primitive $(q^2 - 1)$-th root of unity, that is, a generator of $K^\times$.
If $a$ and $b$ are natural numbers less than $q^2 - 1$ with
$(\theta^a - \theta)^q = \theta^a - \theta$ and $(\theta^b - \theta)^q = \theta^b - \theta$, and
$(q^2 - 1)/g$ divides $a - b$, then $a = b$.

Equivalently, let $\mathbb{F}_q = \{x \in K : x^q = x\}$, let
$B_q = \{a \in \mathbb{Z}/(q^2 - 1) : \theta^a - \theta \in \mathbb{F}_q\}$ be the Bose–Chowla set
and let $H$ be the subgroup of $\mathbb{Z}/(q^2 - 1)$ generated by $(q^2 - 1)/g$; then
$(B_q - B_q) \cap H = \{0\}$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Lemma 9, quoting Bose–Chowla and Brandão–Debarre–Tait / Gómez–Trujillo–Tait.

Stated but not proved: `MetaMathlibExt.boseChowla_sub_mem_subgroup_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#bose-chowla-sub-mem-subgroup-eq).

## Upper bound for sets with bounded difference multiplicities

For natural numbers $g$ and
$n$, let $\alpha_g(n)$ be the largest size of a set $A \subseteq \{1, \dots, n\}$ such that every
nonzero integer $x$ is the difference $a - a'$ of at most $g$ ordered pairs
$(a, a') \in A \times A$. If $g \ge 1$, then for every real $\varepsilon > 0$ we have
$\alpha_g(n) \le (1 + \varepsilon)\sqrt{gn}$ for all sufficiently large $n$; that is,
$\alpha_g(n) \le (1 + o(1))\sqrt{gn}$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Proposition 1.

Stated but not proved: `MetaMathlibExt.boundedDiffSetNumber_le_one_add_mul_sqrt` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#bounded-diff-set-number-le-one-add-mul-s).

## Lower-bound construction for sets with bounded difference multiplicities

For every
integer $g \ge 1$ there are finite sets $A_n \subseteq \{1, \dots, n\}$ of integers, one for each
$n \in \mathbb{N}$, such that for every $n$ each nonzero integer $x$ equals $a - a'$ for at most
$g$ ordered pairs $(a, a') \in A_n \times A_n$, and $|A_n| / \sqrt{gn} \to 1$ as $n \to \infty$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Proposition 2.

Stated but not proved: `MetaMathlibExt.exists_boundedDiffSet_card_div_sqrt_tendsto` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#exists-bounded-diff-set-card-div-sqrt-te).

## Asymptotics of the largest sets with bounded difference counts

For a finite set $A$ of
integers and an integer $x$, write $r_{A-A}(x)$ for the number of ordered pairs
$(a, a') \in A \times A$ with $a - a' = x$. For every integer $g \ge 1$, let $\alpha_g(n)$ be the
largest size of a set $A$ of integers in the interval $[1, n]$ with $r_{A-A}(x) \le g$ for every
nonzero integer $x$. Then $\alpha_g(n) / \sqrt{gn} \to 1$ as $n \to \infty$, that is,
$\alpha_g(n) = (1 + o_g(1)) \sqrt{gn}$.

## Sources

- Eric Schmutz and Michael Tait, *Cardinalities of g-Difference Sets*, INTEGERS 25 (2025), Article A77, Theorem 3.

Stated but not proved: `MetaMathlibExt.tendsto_boundedDiffSetNumber_div_sqrt` is written with `theorem_wanted` in [WantedExt/Combinatorics/GDifferenceBasesWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GDifferenceBasesWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html#tendsto-bounded-diff-set-number-div-sqrt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Difference bases](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/difference-bases)
