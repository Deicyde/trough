---
declaration: section
origin: cited
lean: MetaMathlibExt.cyclicProductNumber, MetaMathlibExt.cyclicProductNumber_of_odd, MetaMathlibExt.cyclicProductNumber_zero_right, MetaMathlibExt.cyclicProductNumber_small_values, MetaMathlibExt.genus_bounds_of_reduced_unicellular_hypermonopole, MetaMathlibExt.sum_cyclicProductNumber_mul_X_pow, MetaMathlibExt.card_unicellular_hypermonopoles_finRotate, MetaMathlibExt.reduced_iff_forall_face_ne_finRotate
statement: formalized
---

# Reduced unicellular hypermonopoles

12 results, 4 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html).

## Cyclic product numbers

For natural numbers $n$ and $k$, write $c(m, j)$ for the unsigned
Stirling numbers of the first kind. The cyclic product number $H(n, k)$ is the quotient
$c(n + 1, k) / \binom{n + 1}{2}$, rounded down to a natural number, when $n + k$ is even
(equivalently, $n - k$ is even), and $0$ when $n + k$ is odd. Division by zero gives $0$, so
$H(0, k) = 0$ for every $k$.

These are the numbers displayed in Theorem 5 of the source. The numbers $H(n + 1, k)$ are the
Hultman numbers (OEIS A164652).

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Theorem 5.

Formalized by `MetaMathlibExt.cyclicProductNumber`, a definition declared in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#cyclic-product-number).

## Vanishing of the cyclic product numbers for odd $n - k$

For natural numbers $n$ and $k$
such that $n + k$ is odd (equivalently, $n - k$ is odd), the cyclic product number $H(n, k)$ is
$0$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Theorem 5.

Formalized by `MetaMathlibExt.cyclicProductNumber_of_odd`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#cyclic-product-number-of-odd).

## Cyclic product numbers with second argument zero

For every natural number $n$, the
cyclic product number $H(n, 0)$ is $0$, since the unsigned Stirling number of the first kind
$c(n + 1, 0)$ is $0$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Theorem 5.

Formalized by `MetaMathlibExt.cyclicProductNumber_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#cyclic-product-number-zero-right).

## Small cyclic product numbers

The cyclic product numbers satisfy $H(3, 1) = 1$,
$H(4, 2) = 5$, $H(5, 1) = 8$ and $H(7, 1) = 180$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Table 1 (values of `H(n, k)`).

Formalized by `MetaMathlibExt.cyclicProductNumber_small_values`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#cyclic-product-number-small-values).

## Genus bounds for reduced unicellular hypermonopoles

Let $\sigma$ and $\alpha$ be
permutations of $\{0, 1, \dots, n - 1\}$, and write $z(\pi)$ for the number of cycles of a
permutation $\pi$, fixed points included. Suppose that $z(\sigma) = 1$, that
$z(\alpha^{-1} \circ \sigma) = 1$, that $\alpha$ has no fixed point, and that the natural
number $g$ satisfies $n + 2 = z(\sigma) + z(\alpha) + z(\alpha^{-1} \circ \sigma) + 2g$. Then
$2g + 1 \le n \le 4g$.

In the terms of the source, $(\sigma, \alpha)$ is a reduced unicellular hypermonopole on $n$
points and $g$ is its genus, given by Jacques' formula.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Lemma 2 (`jis-2025-25.3.3-lem-2`).

Stated but not proved: `MetaMathlibExt.genus_bounds_of_reduced_unicellular_hypermonopole` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#genus-bounds-of-reduced-unicellular-hype).

## Generating polynomial of the cyclic product numbers

For every natural number $n$, let
$H(n, k)$ be the cyclic product numbers, viewed as rational numbers. Then in the polynomial
ring $\mathbb{Q}[x]$

$$\sum_{k=0}^{n} H(n, k) x^k = c_n (x (x + 1) \cdots (x + n) - x (x - 1) \cdots (x - n)),$$

where $c_n = \frac{1}{(n + 1) n}$ for $n \ge 1$ and $c_0 = 0$; for $n = 0$ both sides are $0$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Lemma 6 (`jis-2025-25.3.3-lem-6`), quoting S. Grusea and A. Labarre.

Stated but not proved: `MetaMathlibExt.sum_cyclicProductNumber_mul_X_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#sum-cyclic-product-number-mul-x-pow).

## Unicellular hypermonopoles with a cyclic vertex permutation

Let $n$ and $k$ be natural
numbers, let $\sigma$ be the cyclic permutation $i \mapsto i + 1$ (modulo $n$) of
$\{0, 1, \dots, n - 1\}$, and write $z(\pi)$ for the number of cycles of a permutation $\pi$,
fixed points included. Then the number of permutations $\alpha$ of $\{0, 1, \dots, n - 1\}$ with
$z(\alpha^{-1} \circ \sigma) = 1$ and $z(\alpha) = k$ is the cyclic product number $H(n, k)$.

In the terms of the source, these $\alpha$ are the unicellular hypermonopoles $(\sigma, \alpha)$
with $\sigma = (1, \dots, n)$ and $z(\alpha) = k$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Corollary 8 (`jis-2025-25.3.3-cor-8`).

Stated but not proved: `MetaMathlibExt.card_unicellular_hypermonopoles_finRotate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#card-unicellular-hypermonopoles-fin-rota).

## Criterion for a hypermap with a cyclic vertex permutation to have no bud

Let $\sigma$ be
the cyclic permutation $i \mapsto i + 1$ (modulo $n$) of $\{0, 1, \dots, n - 1\}$. A permutation
$\alpha$ of $\{0, 1, \dots, n - 1\}$ has no fixed point if and only if
$\pi = \alpha^{-1} \circ \sigma$ satisfies $\pi(i) \ne i + 1$ (modulo $n$) for every $i$.

In the terms of the source, a bud of the hypermap $(\sigma, \alpha)$ is a fixed point of $\alpha$.
The source assumes the hypermap is a unicellular hypermonopole; the equivalence does not use that
assumption, so it is stated for every $\alpha$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Lemma 10 (`jis-2025-25.3.3-lem-10`).

Stated but not proved: `MetaMathlibExt.reduced_iff_forall_face_ne_finRotate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#reduced-iff-forall-face-ne-fin-rotate).

## Cycle count of a fixed-point-free permutation

Let $n \ge 1$ and let $\alpha$ be a
permutation of $\{0, 1, \dots, n - 1\}$ with no fixed point. Then the number $z(\alpha)$ of
cycles of $\alpha$ satisfies $1 \le z(\alpha)$ and $2 z(\alpha) \le n$.

This is the source's bound $1 \le z(\alpha) \le n / 2$ for a reduced unicellular
hypermonopole $(\sigma, \alpha)$ on $n$ points: only $n \ge 1$ (forced by $z(\sigma) = 1$) and
the absence of buds (fixed points of $\alpha$) are used.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Corollary 11 (`jis-2025-25.3.3-cor-11`).

Stated but not proved: `MetaMathlibExt.cycleCount_bounds_of_reduced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#cycle-count-bounds-of-reduced).

## Counting reduced unicellular hypermonopoles with a cyclic vertex permutation

Let
$n \ge 2$ and $k \ge 1$ be natural numbers with $2k \le n$, let $\sigma$ be the cyclic
permutation $i \mapsto i + 1$ (modulo $n$) of $\{0, 1, \dots, n - 1\}$, and write $z(\pi)$ for
the number of cycles of a permutation $\pi$, fixed points included. Let $r(n, k)$ be the number
of permutations $\alpha$ of $\{0, 1, \dots, n - 1\}$ with no fixed point such that
$z(\alpha^{-1} \circ \sigma) = 1$ and $z(\alpha) = k$. Then, in terms of the cyclic product
numbers $H$,

$$r(n, k) = \sum_{i=0}^{k-1} (-1)^i \binom{n}{i} H(n - i, k - i).$$

In the terms of the source, $r(n, k)$ counts the reduced unicellular hypermonopoles
$(\sigma, \alpha)$ with $\sigma = (1, \dots, n)$ and $z(\alpha) = k$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Proposition 12 (`jis-2025-25.3.3-prop-12`).

Stated but not proved: `MetaMathlibExt.card_reduced_unicellular_hypermonopoles_finRotate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#card-reduced-unicellular-hypermonopoles).

## Vanishing of the reduced unicellular hypermonopole counts

Let $\sigma_n$ be the cyclic
permutation $i \mapsto i + 1$ (modulo $n$) of $\{0, 1, \dots, n - 1\}$, write $z(\pi)$ for the
number of cycles of a permutation $\pi$, fixed points included, and let $r(n, k)$ be the number
of permutations $\alpha$ of $\{0, 1, \dots, n - 1\}$ with no fixed point such that
$z(\alpha^{-1} \circ \sigma_n) = 1$ and $z(\alpha) = k$. Then $r(n, k) = 0$ for all natural
numbers $n$ and $k$ with $n - k$ odd; $r(3, k) > 0$ for some natural number $k$ with $2k \le 3$;
and $r(n, k) = 0$ whenever $n < 3$ and $2k \le n$.

So the least $n$ with $r(n, k) > 0$ for some $k \le n / 2$ is $n = 3$. In the terms of the
source, $r(n, k)$ counts the reduced unicellular hypermonopoles $(\sigma_n, \alpha)$ with
$\sigma_n = (1, \dots, n)$ and $z(\alpha) = k$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Corollary 13 (`jis-2025-25.3.3-cor-13`).

Stated but not proved: `MetaMathlibExt.reduced_unicellular_hypermonopoles_finRotate_vanishing` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#reduced-unicellular-hypermonopoles-fin-r).

## Counting reduced unicellular hypermonopoles by genus

Fix $g \in \mathbb{N}$. For
each $n \in \mathbb{N}$ let $\zeta_n$ be the cyclic permutation of $\{0, \ldots, n - 1\}$
sending $i$ to $i + 1$ modulo $n$, and let $z(\pi)$ be the number of cycles of a permutation
$\pi$, fixed points included. Let $U_g$ be the set of pairs $(n, \alpha)$, with
$n \in \mathbb{N}$ and $\alpha$ a permutation of $\{0, \ldots, n - 1\}$, such that
$z(\zeta_n) = 1$, $z(\alpha^{-1} \zeta_n) = 1$ (the product applies $\zeta_n$ first), $\alpha$
has no fixed point, and $n + 2 = z(\zeta_n) + z(\alpha) + z(\alpha^{-1} \zeta_n) + 2g$. Then
$U_g$ is finite and its number of elements is $\sum_{n = 2g + 1}^{4g} r(n, n - 2g)$, where
$r(n, k)$ is the number of permutations $\alpha$ of $\{0, \ldots, n - 1\}$ without fixed
points such that $z(\alpha^{-1} \zeta_n) = 1$ and $z(\alpha) = k$.

The pairs in $U_g$ are the reduced unicellular hypermonopoles $(\zeta_n, \alpha)$ of genus
$g$, with the genus given by Jacques' formula and the vertex permutation normalized to
$\zeta_n$. The paper writes $u(g)$ for the number of elements of $U_g$; its first value is
$u(1) = 2$.

## Sources

- Robert Cori and Gábor Hetyei, *On Reduced Unicellular Hypermonopoles*, Journal of Integer Sequences 28 (2025), Article 25.3.3, Proposition 15 (`jis-2025-25.3.3-prop-15`).

Stated but not proved: `MetaMathlibExt.reduced_unicellular_hypermonopoles_of_genus_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ReducedUnicellularHypermonopolesWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html#reduced-unicellular-hypermonopoles-of-ge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reduced unicellular hypermonopoles](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/set-partitions/reduced-unicellular-hypermonopoles)
