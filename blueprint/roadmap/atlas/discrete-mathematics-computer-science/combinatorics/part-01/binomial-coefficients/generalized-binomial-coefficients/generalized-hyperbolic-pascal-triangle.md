---
declaration: section
origin: cited
lean: MetaMathlibExt.ghptInterior, MetaMathlibExt.ghptRow, MetaMathlibExt.ghptRow_figure_one, MetaMathlibExt.linearRecurrence_inhomogeneous_identity, MetaMathlibExt.linearRecurrence_inhomogeneous_explicit, MetaMathlibExt.ghptRow_weighted_alternating_sum
statement: formalized
---

# Generalized hyperbolic Pascal triangle

6 results, 3 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html).

## Interior step of the generalized hyperbolic Pascal triangle

Fix $q \in \mathbb{N}$ and a
type $R$ with an addition. A vertex is recorded as a pair $(c, x)$ of a type code $c \in \mathbb{N}$
(code $0$ for the wingers at the ends of a row, $1$ for type $A$ and $2$ for type $B$) and a
value $x \in R$. Given a list $v_0, v_1, \dots, v_m$ of such pairs with $m \ge 1$ and
$v_i = (c_i, x_i)$, the interior step lists, from left to right and for $i = 1, \dots, m$, the
type-$A$ vertex $(1, x_{i-1} + x_i)$, followed, when $i < m$, by $d_i$ copies of the type-$B$
vertex $(2, x_i)$, where $d_i = q - 4$ if $c_i = 1$ and $d_i = q - 3$ otherwise (both differences
truncated at $0$). A list with fewer than two entries gives the empty list.

## Sources

- Hacène Belbachir, Fella Rami, and László Szalay, *Alternating Sums in the Generalized Hyperbolic Pascal Triangle*, INTEGERS 24 (2024), Article A84, Section 1 (construction of the triangle linked to `{4, q}`).

Formalized by `MetaMathlibExt.ghptInterior`, a definition declared in [WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html#ghpt-interior).

## Rows of the generalized hyperbolic Pascal triangle

Fix $q \in \mathbb{N}$, a type $R$ with
an addition, and leg sequences $\alpha, \beta \colon \mathbb{N} \to R$ (left and right). Row $n$ of
the generalized hyperbolic Pascal triangle linked to the mosaic $\{4, q\}$ is the list of its
vertices from left to right, each recorded as a pair (type code, value) as in the interior step,
with code $0$ for the wingers. Row $1$ is $(0, \alpha_1), (0, \beta_1)$, and for $n \ge 1$ row
$n + 1$ is $(0, \alpha_{n+1})$, followed by the interior step applied to row $n$, followed by
$(0, \beta_{n+1})$. Row $0$ (the indeterminate root $\Omega$) is represented by the empty list.

## Sources

- Hacène Belbachir, Fella Rami, and László Szalay, *Alternating Sums in the Generalized Hyperbolic Pascal Triangle*, INTEGERS 24 (2024), Article A84, Section 1 (construction of the triangle linked to `{4, q}`, Figure 1).

Formalized by `MetaMathlibExt.ghptRow`, a definition declared in [WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html#ghpt-row).

## Rows 3 and 4 of an example generalized hyperbolic Pascal triangle

In the generalized
hyperbolic Pascal triangle linked to $\{4, 5\}$ (so $q = 5$) with legs $\alpha_n = 3n$ and
$\beta_n = 3^n$ in $\mathbb{N}$, the values of the entries of row $3$, from left to right, are
$9, 12, 6, 15, 27$, and those of row $4$ are $12, 21, 12, 18, 6, 6, 21, 15, 42, 81$.

## Sources

- Hacène Belbachir, Fella Rami, and László Szalay, *Alternating Sums in the Generalized Hyperbolic Pascal Triangle*, INTEGERS 24 (2024), Article A84, Figure 1.

Formalized by `MetaMathlibExt.ghptRow_figure_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html#ghpt-row-figure-one).

## Convolution identity for an inhomogeneous linear recurrence

Let $k \in \mathbb{N}$ and let
$A, f, G, w \colon \mathbb{N} \to \mathbb{C}$ be sequences such that, for every $m \ge k$,
$f_m = \sum_{i=1}^{k} A_i f_{m-i}$ and $G_m = \sum_{i=1}^{k} A_i G_{m-i} + w_{m-k}$. Then for
every $n \ge k$,

$$\sum_{j=0}^{k-1} f_j G_{n+k-j} =
\sum_{j=0}^{k-1} \sum_{i=0}^{k-1-j} f_{n-j} A_{j+1+i} G_{k-1-i} +
\sum_{j=0}^{k-2} \sum_{i=1}^{k-1-j} f_j A_i G_{n+k-j-i} + \sum_{j=0}^{n} f_{n-j} w_j.$$

The identity is quoted from Belbachir–Rami–Szalay 2022; its hypotheses $A_k \neq 0$ and
$k \ge 1$ are not needed.

## Sources

- Hacène Belbachir, Fella Rami, and László Szalay, *Alternating Sums in the Generalized Hyperbolic Pascal Triangle*, INTEGERS 24 (2024), Article A84, Theorem 1.

Stated but not proved: `MetaMathlibExt.linearRecurrence_inhomogeneous_identity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html#linear-recurrence-inhomogeneous-identity).

## Explicit formula for an inhomogeneous linear recurrence

Let $k \in \mathbb{N}$ and let
$A, f, G, w \colon \mathbb{N} \to \mathbb{C}$ be sequences such that, for every $m \ge k$,
$f_m = \sum_{i=1}^{k} A_i f_{m-i}$ and $G_m = \sum_{i=1}^{k} A_i G_{m-i} + w_{m-k}$. Suppose
moreover that $f_j = 0$ for every $j < k - 1$ and $f_{k-1} = 1$. Then for every $n \ge k - 1$,

$$G_{n+1} = \sum_{j=0}^{k-1} \sum_{i=0}^{k-1-j} f_{n-j} A_{j+1+i} G_{k-1-i} +
\sum_{j=0}^{n} f_{n-j} w_j.$$

For $k = 0$ the index $k - 1$ is read as $0$, so the hypotheses cannot all hold. The source
states the formula for $n \ge k$, as a consequence of its Theorem 1.

## Sources

- Hacène Belbachir, Fella Rami, and László Szalay, *Alternating Sums in the Generalized Hyperbolic Pascal Triangle*, INTEGERS 24 (2024), Article A84, Corollary 1.

Stated but not proved: `MetaMathlibExt.linearRecurrence_inhomogeneous_explicit` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html#linear-recurrence-inhomogeneous-explicit).

## Weighted alternating row sums of the generalized hyperbolic Pascal triangle

Let
$q, n \in \mathbb{N}$, let $\alpha, \beta \colon \mathbb{N} \to \mathbb{C}$ and let
$v, w \in \mathbb{C}$. Let $x_0, x_1, \dots, x_{\ell - 1}$ be the values of the entries of row $n$
of the generalized hyperbolic Pascal triangle linked to $\{4, q\}$ with legs $\alpha$ and $\beta$,
from left to right, and put $\hat s_n = \sum_i x_i$, $\tilde s_n = \sum_i (-1)^i x_i$ and
$\tilde s_{(v,w),n} = \sum_{i \text{ even}} v x_i + \sum_{i \text{ odd}} w x_i$. Then
$\tilde s_{(v,w),n} = \frac{\hat s_n + \tilde s_n}{2} v + \frac{\hat s_n - \tilde s_n}{2} w$ and
$\tilde s_{(v,w),n} = \frac{v + w}{2} \hat s_n + \frac{v - w}{2} \tilde s_n$.

The identities do not use the structure of the rows; they hold for every $q$ and $n$.

## Sources

- Hacène Belbachir, Fella Rami, and László Szalay, *Alternating Sums in the Generalized Hyperbolic Pascal Triangle*, INTEGERS 24 (2024), Article A84, Corollary 2.

Stated but not proved: `MetaMathlibExt.ghptRow_weighted_alternating_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/HyperbolicPascalAlternatingSumsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html#ghpt-row-weighted-alternating-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized hyperbolic Pascal triangle](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/generalized-hyperbolic-pascal-triangle)
