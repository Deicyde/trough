---
declaration: section
origin: cited
lean: MetaMathlibExt.integerGroupDeterminants, MetaMathlibExt.one_mem_integerGroupDeterminants, MetaMathlibExt.circulantDetFour, MetaMathlibExt.circulantDetFour_single_one, MetaMathlibExt.c4SqB, MetaMathlibExt.c4SqC, MetaMathlibExt.c4SqD, MetaMathlibExt.c4SqAlpha
statement: formalized
---

# Integer group determinants

41 results, 15 proved and 26 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html).

## Integer group determinants

For a finite group $G$, written additively and not
necessarily commutative, $S(G)$ is the set of integers $\det(x_{g - h})_{g, h \in G}$, where $x$
ranges over all functions $G \to \mathbb{Z}$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 1 (definition of `S(G)`).

Formalized by `MetaMathlibExt.integerGroupDeterminants`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#integer-group-determinants).

## $1$ is an integer group determinant

For every finite group $G$, written additively,
$1 \in S(G)$, where $S(G)$ is the set of integer group determinants of $G$: the indicator
function of the identity element gives the identity matrix.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 1 (definition of `S(G)`).

Formalized by `MetaMathlibExt.one_mem_integerGroupDeterminants`, a theorem declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#one-mem-integer-group-determinants).

## The group determinant of $C_4$

For a commutative ring $R$ and
$x = (x_0, x_1, x_2, x_3) \in R^4$, $D_4(x_0, x_1, x_2, x_3)$ is the determinant of the
$4 \times 4$ circulant matrix whose $(i, j)$ entry is $x_{i - j}$, indices taken mod $4$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (definition of `D_n`).

Formalized by `MetaMathlibExt.circulantDetFour`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#circulant-det-four).

## The 4 × 4 circulant determinant of (1, 0, 0, 0)

Over every commutative ring $R$, the
$4 \times 4$ circulant determinant satisfies $D_4(1, 0, 0, 0) = 1$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (definition of `D_n`).

Formalized by `MetaMathlibExt.circulantDetFour_single_one`, a theorem declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#circulant-det-four-single-one).

## The sums $b_i$

For $a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ and
$i \in \mathbb{Z}/4$, $b_i = \bigl(a(i, 0) + a(i, 2)\bigr) + \bigl(a(i, 1) + a(i, 3)\bigr)$. In the
paper's indexing $a_{r + 4s} = a(r, s)$ this is $b_i = (a_i + a_{i+8}) + (a_{i+4} + a_{i+12})$
for $0 \le i \le 3$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (notation after Corollary 2).

Formalized by `MetaMathlibExt.c4SqB`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-b).

## The alternating sums $c_i$

For $a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$
and $i \in \mathbb{Z}/4$, $c_i = \bigl(a(i, 0) + a(i, 2)\bigr) - \bigl(a(i, 1) + a(i, 3)\bigr)$. In
the paper's indexing $a_{r + 4s} = a(r, s)$ this is $c_i = (a_i + a_{i+8}) - (a_{i+4} + a_{i+12})$
for $0 \le i \le 3$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (notation after Corollary 2).

Formalized by `MetaMathlibExt.c4SqC`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-c).

## The differences $d_i$ of a function on $C_4^2$

For
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$, the integers $d_0, \dots, d_7$ are
$d_i = a(i, 0) - a(i, 2)$ and $d_{i+4} = a(i, 1) - a(i, 3)$ for $0 \le i \le 3$. Writing
$a_{r + 4s}$ for $a(r, s)$, this is the paper's $d_i = a_i - a_{i+8}$ for $0 \le i \le 7$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (notation after Corollary 2).

Formalized by `MetaMathlibExt.c4SqD`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-d).

## The Gaussian integers $\alpha_i$

For
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ with differences $d_0, \dots, d_7$ (so
$d_i = a(i, 0) - a(i, 2)$ and $d_{i+4} = a(i, 1) - a(i, 3)$ for $0 \le i \le 3$), the Gaussian
integers $\alpha_0, \dots, \alpha_3 \in \mathbb{Z}[\sqrt{-1}]$ are
$\alpha_i = d_i + d_{i+4} \sqrt{-1}$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (notation after Corollary 2).

Formalized by `MetaMathlibExt.c4SqAlpha`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-alpha).

## The Gaussian integer $\beta$

For $a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$
with Gaussian integers $\alpha_0, \dots, \alpha_3$,
$\beta = (\alpha_0 + \alpha_2)^2 - (\alpha_1 + \alpha_3)^2 \in \mathbb{Z}[\sqrt{-1}]$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (definition before Lemma 1).

Formalized by `MetaMathlibExt.c4SqBeta`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-beta).

## The Gaussian integer $\gamma$ of a function on $C_4^2$

For
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$, let
$\alpha_i = (a(i, 0) - a(i, 2)) + (a(i, 1) - a(i, 3))\sqrt{-1} \in \mathbb{Z}[\sqrt{-1}]$
for $0 \le i \le 3$. Then
$\gamma = (\alpha_0 - \alpha_2)^2 + (\alpha_1 - \alpha_3)^2 \in \mathbb{Z}[\sqrt{-1}]$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (definition before Lemma 1).

Formalized by `MetaMathlibExt.c4SqGamma`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-gamma).

## The C₄² notation at the indicator of the identity

Let $\delta$ be the integer-valued
function on $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$ that is $1$ at $(0, 0)$ and $0$ elsewhere.
For $a = \delta$ the associated integers are $b = c = (1, 0, 0, 0)$ and
$d = (1, 0, 0, 0, 0, 0, 0, 0)$, and the associated Gaussian integers are $\beta = \gamma = 1$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Section 2 (notation after Corollary 2).

Formalized by `MetaMathlibExt.c4Sq_notation_single`, a theorem declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-notation-single).

## Primes congruent to $-3$ modulo $8$

$P$ is the set of positive prime integers $p$
with $p \equiv -3 \pmod 8$, that is, $p \equiv 5 \pmod 8$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Theorem 1 (definition of `P`).

Formalized by `MetaMathlibExt.primesFiveModEight`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#primes-five-mod-eight).

## $5$ and $13$ lie in $P$

The integers $5$ and $13$ both belong to the set $P$ of
positive primes $p \equiv -3 \pmod 8$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Theorem 1 (definition of `P`).

Formalized by `MetaMathlibExt.five_thirteen_mem_primesFiveModEight`, a theorem declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#five-thirteen-mem-primes-five-mod-eight).

## The exceptional set $A$ for $C_4^2$

Let $P$ be the set of positive primes
$p \equiv 5 \pmod 8$. The set $A \subseteq \mathbb{Z}$ consists of all products
$(8k - 3)(8l - 3)(8m - 3)(8n - 3)$ with $k, l, m, n \in \mathbb{Z}$ such that $8l - 3$,
$8m - 3$ and $8n - 3$ lie in $P$ and $k + l \not\equiv m + n \pmod 2$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Theorem 1 (definition of `A`).

Formalized by `MetaMathlibExt.c4SqExceptionalSet`, a definition declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-exceptional-set).

## The exceptional set $A$ contains $1625$

Let $P$ be the set of positive primes
$p \equiv -3 \pmod 8$ and $A$ the set of products $(8k-3)(8l-3)(8m-3)(8n-3)$ with
$k, l, m, n \in \mathbb{Z}$, $8l-3, 8m-3, 8n-3 \in P$ and $k + l \not\equiv m + n \pmod 2$.
Then $1625 \in A$: take $k = l = m = 1$ and $n = 2$, so that $1625 = 5 \cdot 5 \cdot 5 \cdot 13$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Theorem 1 (definition of `A`).

Formalized by `MetaMathlibExt.mem_c4SqExceptionalSet_1625`, a theorem declared in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#mem-c4-sq-exceptional-set-1625).

## Factorization of the 4 × 4 circulant determinant

For every commutative ring $R$ and all
$x_0, x_1, x_2, x_3 \in R$, the $4 \times 4$ circulant determinant $D_4$ satisfies

$$D_4(x_0, x_1, x_2, x_3) =
\bigl((x_0 + x_2)^2 - (x_1 + x_3)^2\bigr)\bigl((x_0 - x_2)^2 + (x_1 - x_3)^2\bigr).$$

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Corollary 1.

Stated but not proved: `MetaMathlibExt.circulantDetFour_eq` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#circulant-det-four-eq).

## Factorization of the complex group determinant of $C_4^2$

For every
$y \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{C}$,

$$
\det\bigl(y(h - g)\bigr)_{g, h \in \mathbb{Z}/4 \times \mathbb{Z}/4} =
\prod_{k=0}^{3} D_4\bigl(z_k(0), z_k(1), z_k(2), z_k(3)\bigr), \qquad
z_k(r) = \sum_{s=0}^{3} i^{ks} y(r, s),
$$

where $i = \sqrt{-1}$ and $D_4(x_0, x_1, x_2, x_3)$ is the determinant of the $4 \times 4$
circulant matrix with first row $(x_0, x_1, x_2, x_3)$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Corollary 2.

Stated but not proved: `MetaMathlibExt.c4Sq_groupDet_eq_prod_circulantDetFour` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-group-det-eq-prod-circulant-det-fo).

## Sums of two squares congruent to −3 modulo 8

Let $a$ and $b$ be integers with
$a^2 + b^2 \equiv -3 \pmod 8$. Then there are integers $k$ and $l$ such that $8l - 3$ lies in
the set $P$ of positive primes congruent to $5$ modulo $8$, and $a^2 + b^2 = (8k + 1)(8l - 3)$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Corollary 3.

Stated but not proved: `MetaMathlibExt.sq_add_sq_eq_mul_of_mod_eight` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#sq-add-sq-eq-mul-of-mod-eight).

## Norms of β and γ as products of sums of two squares (C₄²)

Let $a$ be an integer-valued
function on $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$, with associated integers $d_0, \dots, d_7$
and Gaussian integers $\beta$, $\gamma$, and write $\beta\bar\beta$, $\gamma\bar\gamma$ for the
norms of $\beta$ and $\gamma$. Then

$$\beta\bar\beta = \bigl((d_0 + d_2 + d_1 + d_3)^2 + (d_4 + d_6 + d_5 + d_7)^2\bigr)
\bigl((d_0 + d_2 - d_1 - d_3)^2 + (d_4 + d_6 - d_5 - d_7)^2\bigr)$$

and

$$\gamma\bar\gamma = \bigl((d_0 - d_2 - d_5 + d_7)^2 + (d_4 - d_6 + d_1 - d_3)^2\bigr)
\bigl((d_0 - d_2 + d_5 - d_7)^2 + (d_4 - d_6 - d_1 + d_3)^2\bigr).$$

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 1.

Stated but not proved: `MetaMathlibExt.c4Sq_norm_beta_gamma_eq` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-norm-beta-gamma-eq).

## The group determinant of $C_4^2$ modulo $2$

Let $a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$. For $0 \le i \le 3$ let
$b_i = a(i, 0) + a(i, 2) + a(i, 1) + a(i, 3)$, $c_i = a(i, 0) + a(i, 2) - a(i, 1) - a(i, 3)$
and $\alpha_i = (a(i, 0) - a(i, 2)) + (a(i, 1) - a(i, 3))\sqrt{-1} \in \mathbb{Z}[\sqrt{-1}]$,
and let $\beta = (\alpha_0 + \alpha_2)^2 - (\alpha_1 + \alpha_3)^2$ and
$\gamma = (\alpha_0 - \alpha_2)^2 + (\alpha_1 - \alpha_3)^2$, with complex conjugates $\bar\beta$
and $\bar\gamma$. Let $D_4(x_0, x_1, x_2, x_3)$ be the determinant of the $4 \times 4$
circulant matrix with first row $(x_0, x_1, x_2, x_3)$.
Then the group determinant $D_{4 \times 4}(a) = \det\bigl(a(h - g)\bigr)_{g, h}$, with $g, h$
ranging over $\mathbb{Z}/4 \times \mathbb{Z}/4$, satisfies
$D_{4 \times 4}(a) \equiv D_4(b) \equiv D_4(c) \equiv \beta\bar\beta \equiv \gamma\bar\gamma
\pmod 2$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 2.

Stated but not proved: `MetaMathlibExt.c4Sq_groupDet_congr_mod_two` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-group-det-congr-mod-two).

## Norms of β and γ as differences of squares (C₄²)

Let $a$ be an integer-valued function
on $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$, with associated integers $d_0, \dots, d_7$ and
Gaussian integers $\beta$, $\gamma$, and write $\beta\bar\beta$, $\gamma\bar\gamma$ for the norms of
$\beta$ and $\gamma$. Then

$$\beta\bar\beta = \bigl((d_0 + d_2)^2 + (d_4 + d_6)^2 + (d_1 + d_3)^2 + (d_5 + d_7)^2\bigr)^2 -
4\bigl((d_0 + d_2)(d_1 + d_3) + (d_4 + d_6)(d_5 + d_7)\bigr)^2$$

and

$$\gamma\bar\gamma = \bigl((d_0 - d_2)^2 + (d_4 - d_6)^2 + (d_1 - d_3)^2 + (d_5 - d_7)^2\bigr)^2 -
4\bigl((d_0 - d_2)(d_5 - d_7) - (d_4 - d_6)(d_1 - d_3)\bigr)^2.$$

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 3.

Stated but not proved: `MetaMathlibExt.c4Sq_norm_beta_gamma_eq_sq_sub` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-norm-beta-gamma-eq-sq-sub).

## Difference of the squared sums of squares of the $d_i$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$, and let $d_i = a(i, 0) - a(i, 2)$ and
$d_{i+4} = a(i, 1) - a(i, 3)$ for $0 \le i \le 3$. Then

$$
\bigl((d_0 + d_2)^2 + (d_4 + d_6)^2 + (d_1 + d_3)^2 + (d_5 + d_7)^2\bigr)^2 -
\bigl((d_0 - d_2)^2 + (d_4 - d_6)^2 + (d_1 - d_3)^2 + (d_5 - d_7)^2\bigr)^2 =
8 \Bigl(\sum_{i=0}^{7} d_i^2\Bigr)(d_0 d_2 + d_4 d_6 + d_1 d_3 + d_5 d_7).
$$

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 4.

Stated but not proved: `MetaMathlibExt.c4SqD_sum_sq_sq_sub_sq` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-d-sum-sq-sq-sub-sq).

## Cross terms of the $d_i$ modulo $4$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$, alternating sums
$c_i$ and differences $d_0, \dots, d_7$. Then the following five congruences hold modulo $4$:
$2(d_0 d_2 + d_4 d_6 + d_1 d_3 + d_5 d_7) \equiv b_0 b_2 + b_1 b_3 + c_0 c_2 + c_1 c_3$;
$2(d_0 d_7 + d_2 d_5 + d_4 d_3 + d_6 d_1) \equiv b_0 b_3 + b_2 b_1 - c_0 c_3 - c_2 c_1$;
$2(d_0 d_3 + d_2 d_1 + d_4 d_7 + d_6 d_5) \equiv b_0 b_3 + b_2 b_1 + c_0 c_3 + c_2 c_1$;
$2(d_0 d_5 + d_2 d_7 + d_4 d_1 + d_6 d_3) \equiv b_0 b_1 + b_2 b_3 - c_0 c_1 - c_2 c_3$;
$2(d_0 d_1 + d_2 d_3 + d_4 d_5 + d_6 d_7) \equiv b_0 b_1 + b_2 b_3 + c_0 c_1 + c_2 c_3$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 5.

Stated but not proved: `MetaMathlibExt.c4SqD_cross_terms_mod_four` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-d-cross-terms-mod-four).

## The 4 × 4 circulant determinant modulo 16 at two parity patterns

For all integers
$k$, $l$, $m$, $n$, the $4 \times 4$ circulant determinant $D_4$ satisfies
$D_4(2k + 1, 2l, 2m, 2n) \equiv 8m + 1 \pmod{16}$ and
$D_4(2k, 2l + 1, 2m + 1, 2n + 1) \equiv 8(k + l + n) - 3 \pmod{16}$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 6.

Stated but not proved: `MetaMathlibExt.circulantDetFour_mod_sixteen` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#circulant-det-four-mod-sixteen).

## Powers of $2$ dividing the $C_4$ group determinant at four parity patterns

Let
$D(x_0, x_1, x_2, x_3)$ be the group determinant of $C_4$, that is the determinant of the
$4 \times 4$ circulant matrix with $(i, j)$ entry $x_{i - j}$ (indices mod $4$). For integers
$k, l, m, n$ put $D_1 = D(2k, 2l, 2m, 2n)$, $D_2 = D(2k+1, 2l+1, 2m+1, 2n+1)$,
$D_3 = D(2k, 2l+1, 2m, 2n+1)$, $D_4 = D(2k, 2l, 2m+1, 2n+1)$,
$w_3 = (2k+2l+1)(2m+2n+1)$ and $w_4 = (2k+2m+1)(2l+2n+1)$, and write $2^e \mathbb{Z}_{odd}$
for the set of integers $2^e(2t+1)$ with $t \in \mathbb{Z}$. Then:

* if $k + m \not\equiv l + n \pmod 2$ then $D_1 \in 2^4 \mathbb{Z}_{odd}$, and if
  $k + m \equiv l + n \pmod 2$ then $2^8 \mid D_1$;
* if $k + m \not\equiv l + n \pmod 2$ then $D_2 \in 2^4 \mathbb{Z}_{odd}$; if
  $(k + m)(l + n) \equiv -1 \pmod 4$ then $D_2 \in 2^7 \mathbb{Z}_{odd}$; and if
  $k + m \equiv l + n \pmod 2$ and $(k + m)(l + n) \not\equiv -1 \pmod 4$ then $2^9 \mid D_2$;
* if $k - m$ and $l - n$ are both odd then $D_3 \in 2^5 \mathbb{Z}_{odd}$; if
  $k \equiv m \pmod 2$ and $w_3 \equiv \pm 3 \pmod 8$ then $D_3 \in 2^6 \mathbb{Z}_{odd}$; and if
  neither of these two conditions holds then $2^7 \mid D_3$;
* if $w_4 \equiv \pm 3 \pmod 8$ then $D_4 \in 2^4 \mathbb{Z}_{odd}$, and if
  $w_4 \equiv \pm 1 \pmod 8$ then $2^5 \mid D_4$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 7.

Stated but not proved: `MetaMathlibExt.circulantDetFour_two_power_cases` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#circulant-det-four-two-power-cases).

## Odd integer group determinants of $C_4 \times C_4$

Let $C_4$ be the cyclic group of
order $4$, $S(C_4^2)$ the set of integer group determinants of $C_4 \times C_4$ and $P$ the set
of positive primes $p \equiv -3 \pmod 8$, and let $A$ be the set of products
$(8k-3)(8l-3)(8m-3)(8n-3)$ with $k, l, m, n \in \mathbb{Z}$, $8l-3, 8m-3, 8n-3 \in P$ and
$k + l \not\equiv m + n \pmod 2$. Every odd $z \in S(C_4^2)$ is of the form $16m + 1$ for some
integer $m$ or lies in $A$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 8.

Stated but not proved: `MetaMathlibExt.odd_mem_integerGroupDeterminants_c4Sq` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#odd-mem-integer-group-determinants-c4-sq).

## Factorization shapes of $D_4(b) D_4(c)$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$ and alternating sums
$c_i$, let $D_4$ be the $4 \times 4$ circulant determinant, and suppose
$b_0 + b_2 \not\equiv b_1 + b_3 \pmod 2$. Put $x = b_0 b_2 + b_1 b_3$, $y = c_0 c_2 + c_1 c_3$
and $D = D_4(b) D_4(c)$. If $(x, y) \equiv (0, 0)$ or $(2, 2) \pmod 4$, then
$D = (8k + 1)(8l + 1)$ for some integers $k \equiv l \pmod 2$. If
$(x, y) \equiv (0, 2)$ or $(2, 0) \pmod 4$, then $D = (8k + 1)(8l + 1)$ for some integers
$k \not\equiv l \pmod 2$. If $(x, y) \equiv (1, 1)$ or $(-1, -1) \pmod 4$, then
$D = (8k - 3)(8l - 3)$ for some integers $k \equiv l \pmod 2$. If
$(x, y) \equiv (1, -1)$ or $(-1, 1) \pmod 4$, then $D = (8k - 3)(8l - 3)$ for some integers
$k \not\equiv l \pmod 2$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 9.

Stated but not proved: `MetaMathlibExt.c4Sq_circulantDetFour_product_classes` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-circulant-det-four-product-classes).

## $D_4(b) D_4(c)$ modulo $16$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$ and alternating sums
$c_i$, and let $D_4$ be the $4 \times 4$ circulant determinant. If
$b_0 + b_2 \not\equiv b_1 + b_3 \pmod 2$, then
$D_4(b) D_4(c) \equiv 1 - 4(b_0 b_2 + b_1 b_3 + c_0 c_2 + c_1 c_3) \pmod{16}$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 10.

Stated but not proved: `MetaMathlibExt.c4Sq_circulantDetFour_product_mod_sixteen` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-circulant-det-four-product-mod-six).

## A prime factor $8l - 3$ of $D_4(b) D_4(c)$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$, alternating sums
$c_i$ and Gaussian integer $\beta$, let $D_4$ be the $4 \times 4$ circulant determinant, and let
$P$ be the set of positive primes $p \equiv 5 \pmod 8$. Suppose
$b_0 + b_2 \not\equiv b_1 + b_3 \pmod 2$ and that the norm $\beta \bar\beta \equiv -3 \pmod 8$,
and put $Q = b_0 b_2 + b_1 b_3 + c_0 c_2 + c_1 c_3$. If $Q \equiv 0 \pmod 4$, then
$D_4(b) D_4(c) = (8k - 3)(8l - 3)$ for some integers $k \not\equiv l \pmod 2$ with
$8l - 3 \in P$. If $Q \equiv 2 \pmod 4$, then $D_4(b) D_4(c) = (8k - 3)(8l - 3)$ for some
integers $k \equiv l \pmod 2$ with $8l - 3 \in P$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 11.

Stated but not proved: `MetaMathlibExt.c4Sq_circulantDetFour_product_prime_factor` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-circulant-det-four-product-prime-f).

## The difference of the norms of β and γ modulo 16 (C₄²)

Let $a$ be an integer-valued
function on $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$, with associated integers $b_i$, $c_i$
$(0 \le i \le 3)$ and Gaussian integers $\beta$, $\gamma$, and write $\beta\bar\beta$,
$\gamma\bar\gamma$ for the norms of $\beta$ and $\gamma$. If
$b_0 + b_2 \not\equiv b_1 + b_3 \pmod 2$, then
$\beta\bar\beta - \gamma\bar\gamma \equiv 4(b_0b_2 + b_1b_3 + c_0c_2 + c_1c_3) \pmod{16}$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 12.

Stated but not proved: `MetaMathlibExt.c4Sq_norm_beta_sub_norm_gamma_mod_sixteen` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-norm-beta-sub-norm-gamma-mod-sixte).

## Two prime factors ≡ −3 mod 8 of ββ̄γγ̄ (C₄²)

Let $a$ be an integer-valued function on
$C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$, with associated integers $b_i$, $c_i$ $(0 \le i \le 3)$
and Gaussian integers $\beta$, $\gamma$, write $\beta\bar\beta$, $\gamma\bar\gamma$ for the norms of
$\beta$ and $\gamma$, let $P$ be the set of primes $p \equiv -3 \pmod 8$, and put
$Q = b_0b_2 + b_1b_3 + c_0c_2 + c_1c_3$. Suppose that $b_0 + b_2 \not\equiv b_1 + b_3 \pmod 2$ and
$\beta\bar\beta \equiv -3 \pmod 8$. If $Q \equiv 0 \pmod 4$, there are integers $j$, $m$, $n$ with
$8m - 3 \in P$, $8n - 3 \in P$, $j \equiv m + n \pmod 2$ and
$\beta\bar\beta\gamma\bar\gamma = (8j + 1)(8m - 3)(8n - 3)$. If $Q \equiv 2 \pmod 4$, the same holds
with $j \not\equiv m + n \pmod 2$ in place of $j \equiv m + n \pmod 2$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 13.

Stated but not proved: `MetaMathlibExt.c4Sq_norm_beta_gamma_prime_factors` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-norm-beta-gamma-prime-factors).

## Even integer group determinants of $C_4 \times C_4$

Let $C_4$ be the cyclic group of
order $4$, $S(C_4^2)$ the set of integer group determinants of $C_4 \times C_4$ and $P$ the set
of positive primes $p \equiv -3 \pmod 8$, and let $z \in S(C_4^2)$. If $z$ is even, then
$2^{15} \mid z$. If $z = 2^{15}(2t + 1)$ for some integer $t$, then $z = 2^{15} p (2m + 1)$ for
some $p \in P$ and some integer $m$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 14.

Stated but not proved: `MetaMathlibExt.even_mem_integerGroupDeterminants_c4Sq` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#even-mem-integer-group-determinants-c4-s).

## The power of $2$ in $D_4(b) D_4(c)$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$ and alternating sums
$c_i$, let $D_4$ be the $4 \times 4$ circulant determinant, put $D = D_4(b) D_4(c)$, and say
that $D \in 2^e \mathbb{Z}_{\mathrm{odd}}$ when $D = 2^e (2t + 1)$ for some integer $t$.
If every $b_i$ is even, then $D \in 2^8 \mathbb{Z}_{\mathrm{odd}}$ when
$b_0 + b_1 + b_2 + b_3 \equiv c_0 + c_1 + c_2 + c_3 \equiv 2 \pmod 4$, and $2^{12} \mid D$
otherwise. If every $b_i$ is odd, then $D \in 2^8 \mathbb{Z}_{\mathrm{odd}}$ under the same
condition, and $2^{11} \mid D$ otherwise. If $b_0 \equiv b_2$, $b_1 \equiv b_3$ and
$b_0 \not\equiv b_1 \pmod 2$, then $D \in 2^{10} \mathbb{Z}_{\mathrm{odd}}$ when
$b_0 - b_2 \equiv b_1 - b_3 \equiv c_0 - c_2 \equiv c_1 - c_3 \equiv 2 \pmod 4$, and
$2^{11} \mid D$ otherwise. If $b_0 + b_2$ and $b_1 + b_3$ are both odd, put
$u = (b_0 + b_2)(b_1 + b_3)$ and $v = (c_0 + c_2)(c_1 + c_3)$; then
$D \in 2^8 \mathbb{Z}_{\mathrm{odd}}$ when $u \equiv \pm 3$ and $v \equiv \pm 3 \pmod 8$, and
$2^9 \mid D$ otherwise.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 15.

Stated but not proved: `MetaMathlibExt.c4Sq_circulantDetFour_product_two_power` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-circulant-det-four-product-two-pow).

## The power of $2$ in $\beta\bar\beta\gamma\bar\gamma$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$, alternating sums
$c_i$, differences $d_0, \dots, d_7$ and Gaussian integers $\beta$, $\gamma$, and put
$N = \beta \bar\beta \gamma \bar\gamma$, the product of the norms of $\beta$ and $\gamma$. If
$b_0 + b_2$ and $b_1 + b_3$ are both even, then $N = 2^4 (2t + 1)$ for some integer $t$ when
$b_0 + b_1 + b_2 + b_3 \not\equiv c_0 + c_1 + c_2 + c_3 \pmod 4$, and $2^8 \mid N$ when
$b_0 + b_1 + b_2 + b_3 \equiv c_0 + c_1 + c_2 + c_3 \pmod 4$. If $b_0 + b_2$ and $b_1 + b_3$
are both odd, put
$d = \bigl((d_0 + d_2)(d_5 + d_7) + (d_4 + d_6)(d_1 + d_3)\bigr)
\bigl((d_0 - d_2)(d_1 - d_3) + (d_4 - d_6)(d_5 - d_7)\bigr)$; then $N = 2^7 (2t + 1)$ for
some integer $t$ when $d \equiv 2 \pmod 4$, and $2^8 \mid N$ when $d \equiv 0 \pmod 4$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 16.

Stated but not proved: `MetaMathlibExt.c4Sq_norm_beta_gamma_two_power` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-norm-beta-gamma-two-power).

## Two conditions forcing $b_0 b_2 + b_1 b_3 + c_0 c_2 + c_1 c_3 \equiv 2 \pmod 4$

Let
$a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$ have sums $b_i$, alternating sums
$c_i$ and Gaussian integers $\beta$, $\gamma$; let $D_4$ be the $4 \times 4$ circulant
determinant, and put $D = D_4(b) D_4(c)$, $N = \beta \bar\beta \gamma \bar\gamma$ and
$Q = b_0 b_2 + b_1 b_3 + c_0 c_2 + c_1 c_3$. If every $b_i$ is odd and $D = 2^{11} (2t + 1)$
for some integer $t$, then $Q \equiv 2 \pmod 4$. If $b_0 \equiv b_2$, $b_1 \equiv b_3$ and
$b_0 \not\equiv b_1 \pmod 2$, and $D = 2^{11} (2t + 1)$ and $N = 2^4 (2s + 1)$ for some
integers $t$ and $s$, then $Q \equiv 2 \pmod 4$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 17.

Stated but not proved: `MetaMathlibExt.c4Sq_cross_sum_mod_four_of_two_power` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 454](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L454). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-cross-sum-mod-four-of-two-power).

## A prime factor p ≡ −3 mod 8 of ββ̄γγ̄ in the even case (C₄²)

Let $a$ be an integer-valued
function on $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$, with associated integers $b_i$, $c_i$
$(0 \le i \le 3)$ and Gaussian integers $\beta$, $\gamma$, write $\beta\bar\beta$ and
$\gamma\bar\gamma$ for the norms of $\beta$ and $\gamma$, and let $P$ be the set of primes
$p \equiv -3 \pmod 8$. Suppose that $b_0 + b_2 \equiv b_1 + b_3 \equiv 0 \pmod 2$, that
$\beta\bar\beta\gamma\bar\gamma = 2^4(2t + 1)$ for some integer $t$, and that
$b_0b_2 + b_1b_3 + c_0c_2 + c_1c_3 \equiv 2 \pmod 4$. Then
$\beta\bar\beta\gamma\bar\gamma = 2^4 p(2m + 1)$ for some $p \in P$ and some integer $m$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 18.

Stated but not proved: `MetaMathlibExt.c4Sq_norm_beta_gamma_prime_factor` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 469](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-norm-beta-gamma-prime-factor).

## A prime factor $p \equiv 5 \pmod 8$ of $D_4(b) D_4(c) \beta\bar\beta \gamma\bar\gamma$

Let $a \colon \mathbb{Z}/4 \times \mathbb{Z}/4 \to \mathbb{Z}$. For $0 \le i \le 3$ let
$b_i = a(i, 0) + a(i, 2) + a(i, 1) + a(i, 3)$, $c_i = a(i, 0) + a(i, 2) - a(i, 1) - a(i, 3)$
and $\alpha_i = (a(i, 0) - a(i, 2)) + (a(i, 1) - a(i, 3))\sqrt{-1} \in \mathbb{Z}[\sqrt{-1}]$,
and let $\beta = (\alpha_0 + \alpha_2)^2 - (\alpha_1 + \alpha_3)^2$ and
$\gamma = (\alpha_0 - \alpha_2)^2 + (\alpha_1 - \alpha_3)^2$, with complex conjugates $\bar\beta$
and $\bar\gamma$. Let $D_4(x_0, x_1, x_2, x_3)$ be the determinant of the $4 \times 4$
circulant matrix with first row $(x_0, x_1, x_2, x_3)$.
Let $P$ be the set of positive primes $p \equiv 5 \pmod 8$. Suppose that $b_0 + b_2$ and
$b_1 + b_3$ are odd, that $D_4(b) D_4(c) = 2^8 (2t + 1)$ for some integer $t$, and that
$\beta\bar\beta \gamma\bar\gamma = 2^7 (2t' + 1)$ for some integer $t'$. Then there are $p \in P$
and $m \in \mathbb{Z}$ with $D_4(b) D_4(c) \beta\bar\beta \gamma\bar\gamma = 2^{15} p (2m + 1)$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 19.

Stated but not proved: `MetaMathlibExt.c4Sq_groupDet_factors_prime_factor` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 482](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L482). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-group-det-factors-prime-factor).

## Basic integer group determinants of $C_4^2$

For every integer $m$, the integers
$16m + 1$, $2^{16} (4m + 1)$, $2^{16} (4m - 1)$ and $2^{16} \cdot 2m$ all lie in the set
$S(C_4^2)$ of integer group determinants of $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 20.

Stated but not proved: `MetaMathlibExt.c4Sq_integerGroupDeterminants_basic_members` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-integer-group-determinants-basic-m).

## Four-factor integer group determinants of $C_4^2$

Let
$P$ be the set of positive primes $p \equiv 5 \pmod 8$, and let $k, l, m, n$ be integers such
that $16l - 3$, $16l + 5$, $16m - 3$, $16m + 5$, $16n - 3$ and $16n + 5$ all lie in $P$. Then
the four integers $(16k - 3)(16l + 5)(16m - 3)(16n - 3)$,
$(16k - 3)(16l + 5)(16m + 5)(16n + 5)$, $(16k + 5)(16l - 3)(16m - 3)(16n - 3)$ and
$(16k + 5)(16l - 3)(16m + 5)(16n + 5)$ all lie in the set $S(C_4^2)$ of integer group
determinants of $C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$.

All six membership hypotheses are assumed for each of the four conclusions, as in the paper's
shared hypothesis list.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 21.

Stated but not proved: `MetaMathlibExt.c4Sq_integerGroupDeterminants_four_factor_members` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-integer-group-determinants-four-fa).

## Integer group determinants of $C_4^2$ of the form $2^{15} p (2m + 1)$

Let $P$ be
the set of positive primes $p \equiv 5 \pmod 8$. For every integer $m$ and every $p \in P$, the
integer $2^{15} p (2m + 1)$ lies in the set $S(C_4^2)$ of integer group determinants of
$C_4^2 = \mathbb{Z}/4 \times \mathbb{Z}/4$.

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Lemma 22.

Stated but not proved: `MetaMathlibExt.c4Sq_integerGroupDeterminants_two_pow_fifteen` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#c4-sq-integer-group-determinants-two-pow).

## Integer group determinants of $C_4 \times C_4$

Let $C_4$ be the cyclic group of order
$4$, let $S(C_4^2)$ be the set of integer group determinants of $C_4 \times C_4$, let $P$ be the
set of positive primes $p \equiv -3 \pmod 8$, and let $A$ be the set of products
$(8k-3)(8l-3)(8m-3)(8n-3)$ with $k, l, m, n \in \mathbb{Z}$, $8l-3, 8m-3, 8n-3 \in P$ and
$k + l \not\equiv m + n \pmod 2$. Then $A$ is a proper subset of
$\{16m - 7 \mid m \in \mathbb{Z}\}$, and

$$S(C_4^2) = \{16m + 1 \mid m \in \mathbb{Z}\} \cup
\{2^{15} p (2m + 1) \mid p \in P, m \in \mathbb{Z}\} \cup
\{2^{16} m \mid m \in \mathbb{Z}\} \cup A.$$

## Sources

- Yuka Yamaguchi and Naoya Yamaguchi, *Integer Group Determinants for C_4^2*, INTEGERS 24 (2024), Article A30, Theorem 1.

Stated but not proved: `MetaMathlibExt.integerGroupDeterminants_c4Sq` is written with `theorem_wanted` in [WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean, line 533](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Algebra/IntegerGroupDeterminantsC4SqWanted.lean#L533). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html#integer-group-determinants-c4-sq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer group determinants](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/characters-of-finite-groups/integer-group-determinants)
