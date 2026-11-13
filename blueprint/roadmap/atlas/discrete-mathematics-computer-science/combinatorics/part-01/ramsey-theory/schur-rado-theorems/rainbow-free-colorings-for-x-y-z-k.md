---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_card_colorClass_eq_one_of_rainbowFree_powDiff, MetaMathlibExt.eq_zero_of_color_eq_color_zero_of_rainbowFree_powDiff, MetaMathlibExt.rainbowFree_powDiff_lift_of_zmod, MetaMathlibExt.exists_coprime_same_colors_of_coprime_dist, MetaMathlibExt.color_neg_eq_of_rainbowFree_powDiff, MetaMathlibExt.powMap_component_unique_cycle, MetaMathlibExt.card_powMap_components_eq_two_iff_of_even, MetaMathlibExt.card_powMap_components_eq_three_iff_of_odd
statement: formalized
---

# Rainbow-free colorings for x − y = z^k

23 results, 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html).

## Rainbow-free 3-colorings modulo a prime have a singleton color class

Let $p$ be a prime
and $k$ a natural number, and let $c$ be a coloring of $\mathbb{Z}/p\mathbb{Z}$ with three colors
that uses every color and is rainbow-free for $x - y = z^k$: no $x, y, z \in \mathbb{Z}/p\mathbb{Z}$
with $x - y = z^k$ have $c(x), c(y), c(z)$ pairwise distinct. Then some color is taken by exactly
one element of $\mathbb{Z}/p\mathbb{Z}$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Corollary 1.

Stated but not proved: `MetaMathlibExt.exists_card_colorClass_eq_one_of_rainbowFree_powDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-card-color-class-eq-one-of-rainbo).

## Zero has a color class of its own

Let $p$ be a prime and $k$ a natural number, and let $c$
be a coloring of $\mathbb{Z}/p\mathbb{Z}$ with three colors that uses every color and is
rainbow-free for $x - y = z^k$: no $x, y, z \in \mathbb{Z}/p\mathbb{Z}$ with $x - y = z^k$ have
$c(x), c(y), c(z)$ pairwise distinct. If $a \in \mathbb{Z}/p\mathbb{Z}$ satisfies $c(a) = c(0)$,
then $a = 0$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Corollary 2.

Stated but not proved: `MetaMathlibExt.eq_zero_of_color_eq_color_zero_of_rainbowFree_powDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#eq-zero-of-color-eq-color-zero-of-rainbo).

## Rainbow-free colorings of $\mathbb{Z}/n\mathbb{Z}$ lift to the positive integers

Let $n$
and $k$ be natural numbers and let $c$ be a coloring of $\mathbb{Z}/n\mathbb{Z}$ with three colors
that is rainbow-free for $x - y = z^k$: there are no $x, y, z \in \mathbb{Z}/n\mathbb{Z}$ with
$x - y = z^k$ whose colors $c(x)$, $c(y)$, $c(z)$ are pairwise distinct. Then the coloring
$i \mapsto c(i \bmod n)$ of the positive integers is rainbow-free for $x - y = z^k$: for all
positive integers $x, y, z$ with $x = y + z^k$, the colors $c(x \bmod n)$, $c(y \bmod n)$ and
$c(z \bmod n)$ are not pairwise distinct. (For $n = 0$, $\mathbb{Z}/0\mathbb{Z}$ is $\mathbb{Z}$
and $i \bmod 0 = i$.)

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 7.

Stated but not proved: `MetaMathlibExt.rainbowFree_powDiff_lift_of_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#rainbow-free-pow-diff-lift-of-zmod).

## Coprime representatives at a coprime distance

Let $n$ be a natural number and let $c$ be a
coloring of $\mathbb{Z}/n\mathbb{Z}$ with three colors, used to color every positive integer by its
residue modulo $n$. If $i_1, i_2$ are positive integers with $\gcd(|i_1 - i_2|, n) = 1$, then there
are coprime positive integers $j_1, j_2$ with $|j_1 - j_2| = |i_1 - i_2|$ such that $j_1$ has the
color of $i_1$ and $j_2$ has the color of $i_2$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 8.

Stated but not proved: `MetaMathlibExt.exists_coprime_same_colors_of_coprime_dist` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-coprime-same-colors-of-coprime-di).

## Rainbow-free colorings modulo a prime are symmetric under negation

Let $p$ be a prime and
$k$ a natural number, and let $c$ be a coloring of $\mathbb{Z}/p\mathbb{Z}$ with three colors that
uses every color and is rainbow-free for $x - y = z^k$: no $x, y, z \in \mathbb{Z}/p\mathbb{Z}$
with $x - y = z^k$ have $c(x), c(y), c(z)$ pairwise distinct. Then $c(-a) = c(a)$ for every
$a \in \mathbb{Z}/p\mathbb{Z}$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 10.

Stated but not proved: `MetaMathlibExt.color_neg_eq_of_rainbowFree_powDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#color-neg-eq-of-rainbow-free-pow-diff).

## Each component of the power digraph has exactly one cycle

Let $p$ be a prime and $k$ a
natural number, and let $G^k_p$ be the digraph on $\mathbb{Z}/p\mathbb{Z}$ with edges
$a \to a^k$, so that $m$ steps lead from $a$ to $a^{k^m}$. Call $a$ a cycle vertex if
$a^{k^r} = a$ for some $r > 0$, and say that $a$ and $b$ lie in the same component if
$a^{k^m} = b^{k^n}$ for some $m, n \ge 0$. Then every $a$ has a cycle vertex $a^{k^m}$ among its
iterates, and if two cycle vertices $a$ and $b$ lie in the same component, then $b = a^{k^m}$
for some $m \ge 0$. Thus every component of $G^k_p$ contains exactly one cycle.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 12.

Stated but not proved: `MetaMathlibExt.powMap_component_unique_cycle` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#pow-map-component-unique-cycle).

## Power digraphs modulo a prime with two components

Let $p$ be a prime and $k > 0$ an even
natural number, and let $G^k_p$ be the directed graph on $\mathbb{Z}/p\mathbb{Z}$ with an edge
$a \to a^k$ from every vertex $a$. Its (weak) components are the classes of the equivalence
relation "$a^{k^m} = b^{k^n}$ for some natural numbers $m, n$". Then $G^k_p$ has exactly two
components if and only if every prime factor of $p - 1$ divides $k$.

In the source, writing the prime factorization of $k$ as
$k = 2^{\alpha_0} q_1^{\alpha_1} \cdots q_\ell^{\alpha_\ell}$ with distinct odd primes
$q_1, \dots, q_\ell$, the condition reads
$p - 1 = 2^{\beta_0} q_1^{\beta_1} \cdots q_\ell^{\beta_\ell}$ with all $\beta_i \ge 0$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Proposition 1.

Stated but not proved: `MetaMathlibExt.card_powMap_components_eq_two_iff_of_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#card-pow-map-components-eq-two-iff-of-ev).

## Power digraphs modulo a prime with three components

Let $p$ be a prime and $k \ge 3$ an
odd natural number, and let $G^k_p$ be the directed graph on $\mathbb{Z}/p\mathbb{Z}$ with an edge
$a \to a^k$ from every vertex $a$. Its (weak) components are the classes of the equivalence
relation "$a^{k^m} = b^{k^n}$ for some natural numbers $m, n$". Then $G^k_p$ has exactly three
components if and only if $p - 1 = 2m$ for some natural number $m$ every prime factor of which
divides $k$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Proposition 2.

Stated but not proved: `MetaMathlibExt.card_powMap_components_eq_three_iff_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#card-pow-map-components-eq-three-iff-of).

## Large multiples of the gcd are nonnegative combinations

Let $i$ and $j$ be positive
integers. There is an $n_0$ such that every integer $m > n_0$ divisible by $\gcd(i, j)$ can be
written as $m = ui + vj$ with nonnegative integers $u$ and $v$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_forall_gcd_dvd_eq_add_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-forall-gcd-dvd-eq-add-mul).

## Upper density threshold for rainbow solutions of $x - y = z^k$

Let $k \ge 2$ be an
integer, let $s = \lfloor k / 2 \rfloor$ and $\delta = (4^s - 1) / (3 \cdot 4^s)$, and let $c$ be
a coloring of the positive integers by three colors. Suppose that for each color $e$ there is
an $\varepsilon > 0$ such that, for arbitrarily large $N$, more than $(\delta + \varepsilon) N$
of the integers $x \in \{1, \dots, N\}$ have $c(x) = e$; that is, every color class has upper
density greater than $\delta$. Then there are positive integers $x, y, z$ with $x = y + z^k$
such that $c(x)$, $c(y)$, $c(z)$ are pairwise distinct.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 3.

Stated but not proved: `MetaMathlibExt.exists_rainbow_powDiff_of_upperDensity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-rainbow-pow-diff-of-upper-density).

## Small color classes in rainbow-free 3-colorings modulo an odd integer

Let $n$ be an odd
natural number, let $r_1$ be its smallest prime factor (with $r_1 = 1$ when $n = 1$), let $k$ be a
natural number, and let $c$ be a coloring of $\mathbb{Z}/n\mathbb{Z}$ with three colors that uses
every color and is rainbow-free for $x - y = z^k$: no $x, y, z \in \mathbb{Z}/n\mathbb{Z}$ with
$x - y = z^k$ have $c(x), c(y), c(z)$ pairwise distinct. Then some color class has at most
$n / r_1$ elements.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 4.

Stated but not proved: `MetaMathlibExt.exists_card_colorClass_le_div_minFac_of_rainbowFree_powDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-card-color-class-le-div-min-fac-o).

## Rainbow-free colorings of $\mathbb{Z}/p\mathbb{Z}$ for $x - y = z^k$

Let $p$ be a prime,
$k$ a natural number, and $c$ a coloring of $\mathbb{Z}/p\mathbb{Z}$ by three colors that uses
all three. Then $c$ has no solution of $x - y = z^k$ in $\mathbb{Z}/p\mathbb{Z}$ with $c(x)$,
$c(y)$, $c(z)$ pairwise distinct if and only if the following three conditions hold: $0$ is the
only element of its color class; $c(a) = c(b)$ whenever $a^{k^m} = b^{k^n}$ for some
$m, n \ge 0$, that is, every component of the digraph $a \mapsto a^k$ is monochromatic; and
$c(-a) = c(a)$ for every $a$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 5.

Stated but not proved: `MetaMathlibExt.rainbowFree_powDiff_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#rainbow-free-pow-diff-iff).

## Rainbow number of the power-difference equation modulo a prime, even exponent

Let $p$ be
a prime and $k$ an even natural number. A coloring of $\mathbb{Z}/p\mathbb{Z}$ with $r$ colors is
exact if it uses every color, and a solution of $x - y = z^k$ in $\mathbb{Z}/p\mathbb{Z}$ is
rainbow if $x$, $y$ and $z$ receive pairwise distinct colors. Then the least $r \ge 3$ such that
every exact coloring of $\mathbb{Z}/p\mathbb{Z}$ with $r$ colors has a rainbow solution of
$x - y = z^k$ is $3$ if every prime factor of $p - 1$ divides $k$, and $4$ otherwise.

The bound $r \ge 3$ is part of the definition: a rainbow solution needs three colors, and for
$r = 0$ the condition would hold vacuously, as $\mathbb{Z}/p\mathbb{Z}$ has no coloring with no
colors.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 7.

Stated but not proved: `MetaMathlibExt.rainbowNumber_powDiff_of_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#rainbow-number-pow-diff-of-even).

## Rainbow number of the power-difference equation modulo a prime, odd exponent

Let $p$ be
an odd prime and $k \ge 3$ an odd natural number. A coloring of $\mathbb{Z}/p\mathbb{Z}$ with $r$
colors is exact if it uses every color, and a solution of $x - y = z^k$ in $\mathbb{Z}/p\mathbb{Z}$
is rainbow if $x$, $y$ and $z$ receive pairwise distinct colors. Then the least $r \ge 3$ such
that every exact coloring of $\mathbb{Z}/p\mathbb{Z}$ with $r$ colors has a rainbow solution of
$x - y = z^k$ is $3$ if $p - 1 = 2m$ for a natural number $m$ all of whose prime factors divide
$k$, and $4$ otherwise.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 8.

Stated but not proved: `MetaMathlibExt.rainbowNumber_powDiff_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#rainbow-number-pow-diff-of-odd).

## The color of one dominates bichromatic strings

Let $r$ and $k$ be natural numbers and let
$c$ be a coloring of the positive integers with $r$ colors that uses every color on some positive
integer and is rainbow-free for $x - y = z^k$: no positive integers $x, y, z$ with $x = y + z^k$
have $c(x), c(y), c(z)$ pairwise distinct. Then for every positive integer $i$ and every natural
number $\ell$, if $c$ takes exactly two colors on $i, i + 1, \dots, i + \ell - 1$, one of these
integers has the color $c(1)$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 1.

Stated but not proved: `MetaMathlibExt.color_one_dominant_of_rainbowFree_powDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#color-one-dominant-of-rainbow-free-pow-d).

## Shifting monochromatic strings by $k$-th powers

Let $k$ be a natural number and let $c$
be a coloring of the positive integers by three distinct colors $R$, $B$, $G$ with no rainbow
solution of $x - y = z^k$: there are no positive integers $x, y, z$ with $x = y + z^k$ and
$c(x)$, $c(y)$, $c(z)$ pairwise distinct. Assume that $R$ is dominant: for all positive integers
$i$ and all $\ell \ge 0$, if $c$ takes exactly two colors on $\{i, i + 1, \dots, i + \ell - 1\}$,
then one of them is $R$. Let $j$ be a positive integer with $c(j) = B$, and let $i \ge 1$ and
$\ell \ge 0$ be such that $c(i + t) = G$ for all $0 \le t < \ell$. Then there is a color
$e \in \{B, G\}$ with $c(i + j^k + t) = e$ for all $0 \le t < \ell$, and, if $j^k < i$, there
is a color $e' \in \{B, G\}$ with $c(i - j^k + t) = e'$ for all $0 \le t < \ell$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 2.

Stated but not proved: `MetaMathlibExt.monochromatic_shift_of_rainbowFree_powDiff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#monochromatic-shift-of-rainbow-free-pow).

## Zhan's small-gap lemma

Let $S$ be a set of natural numbers, let $n_0 \ge 2$ be an
integer, and write $S(n)$ for the number of elements of $S \cap \{1, \dots, n\}$. If
$\limsup_{n \to \infty} (S(n) - n / n_0) = \infty$, that is, for every real $M$ there are
arbitrarily large $n$ with $S(n) - n / n_0 > M$, then there is an integer $d$ with
$1 \le d \le n_0 - 1$ such that $j$ and $j + d$ both lie in $S$ for arbitrarily large $j$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 3.

Stated but not proved: `MetaMathlibExt.exists_small_gap_of_limsup_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-small-gap-of-limsup-count).

## Non-dominant monochromatic strings have bounded length

Let $k$ be a natural number, let
$n_0 \ge 2$ be an integer, and let $c$ be a coloring of the positive integers by three colors
with no rainbow solution of $x - y = z^k$: there are no positive integers $x, y, z$ with
$x = y + z^k$ and $c(x)$, $c(y)$, $c(z)$ pairwise distinct. For a color $e$ write $N_e(n)$ for
the number of $x \in \{1, \dots, n\}$ with $c(x) = e$, and assume that for every real $M$ there
are arbitrarily large $n$ with $N_e(n) - n / n_0 > M$ for all three colors $e$, that is,
$\limsup_{n \to \infty} \bigl(\min_e N_e(n) - n / n_0\bigr) = \infty$. Let $d$ be a dominant
color: for all positive integers $i$ and all $\ell \ge 0$, if $c$ takes exactly two colors on
$\{i, i + 1, \dots, i + \ell - 1\}$, then one of them is $d$. Then there is an $L$ such that for
all positive integers $i$ and all $\ell \ge 0$, if $c(i) \ne d$ and $c(i + t) = c(i)$ for all
$0 \le t < \ell$, then $\ell \le L$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 4.

Stated but not proved: `MetaMathlibExt.nondominant_string_length_bounded` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#nondominant-string-length-bounded).

## Coprime numbers of a non-dominant color cannot both have the $A$-property

Let $k$ be a
natural number, let $n_0 \ge 2$ be an integer, and let $c$ be a coloring of the positive
integers by three distinct colors $R$, $B$, $G$ with no rainbow solution of $x - y = z^k$: there
are no positive integers $x, y, z$ with $x = y + z^k$ and $c(x)$, $c(y)$, $c(z)$ pairwise
distinct. For a color $e$ write $N_e(n)$ for the number of $x \in \{1, \dots, n\}$ with
$c(x) = e$, and assume that for every real $M$ there are arbitrarily large $n$ with
$N_e(n) - n / n_0 > M$ for all three colors $e$. Assume that $R$ is dominant: for all positive
integers $i$ and all $\ell \ge 0$, if $c$ takes exactly two colors on
$\{i, i + 1, \dots, i + \ell - 1\}$, then one of them is $R$. Say that a positive integer $j$
has the $A$-property if there is a positive integer $i$ with $c(i + t j^k) = B$ for all
$t \ge 0$. If $j_1$ and $j_2$ are coprime positive integers with $c(j_1) = c(j_2) = G$, then
$j_1$ and $j_2$ do not both have the $A$-property.

The density hypothesis comes from Lemma 4 of the source; it is added because the source's proof
of this lemma ends by contradicting Lemma 4.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 5; `A`-property as defined before Lemma 5 in arXiv:2305.15133.

Stated but not proved: `MetaMathlibExt.not_both_aProperty_of_coprime` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#not-both-a-property-of-coprime).

## Coprime pairs in both non-dominant colors force a rainbow solution of $x - y = z^k$

Let $k \ge 2$ and $n_0 \ge 2$ be integers, and let $c$ be a coloring of the positive integers
by three distinct colors $R$, $B$, $G$. For a color $e$ write $N_e(n)$ for the number of
$x \in \{1, \dots, n\}$ with $c(x) = e$. Assume that for every real $M$ there are arbitrarily
large $n$ with $N_e(n) - n / n_0 > M$ for all three colors $e$, that is,
$\limsup_{n \to \infty} \bigl(\min_e N_e(n) - n / n_0\bigr) = \infty$. Assume also that $R$ is
dominant: for all positive integers $i$ and all $\ell \ge 0$, if $c$ takes exactly two colors on
$\{i, i + 1, \dots, i + \ell - 1\}$, then one of them is $R$. If there are coprime positive
integers $i_1, i_2$ with $c(i_1) = c(i_2) = B$ and coprime positive integers $j_1, j_2$ with
$c(j_1) = c(j_2) = G$, then there are positive integers $x, y, z$ with $x = y + z^k$ such that
$c(x)$, $c(y)$, $c(z)$ are pairwise distinct.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_rainbow_powDiff_of_coprime_pairs` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#exists-rainbow-pow-diff-of-coprime-pairs).

## Dominant colors on power-step strings modulo a prime

Let $p$ be a prime and $k$ a natural
number, and let $c$ be a coloring of $\mathbb{Z}/p\mathbb{Z}$ with three colors that uses every
color and is rainbow-free for $x - y = z^k$: no $x, y, z \in \mathbb{Z}/p\mathbb{Z}$ with
$x - y = z^k$ have $c(x), c(y), c(z)$ pairwise distinct. Let $a \ne 0$ and $i$ be elements of
$\mathbb{Z}/p\mathbb{Z}$ and let $\ell$ be a natural number. If the elements $(i + t)a^k$ for
$0 \le t < \ell$ take exactly two colors, then one of these elements has the color $c(a)$.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 9.

Stated but not proved: `MetaMathlibExt.color_dominant_powStrings_of_rainbowFree_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#color-dominant-pow-strings-of-rainbow-fr).

## Components avoiding the color of zero are monochromatic

Let $n$ and $t$ be natural
numbers, let $f$ be a map from $\mathbb{Z}/n\mathbb{Z}$ to itself, and let $c$ be a coloring of
$\mathbb{Z}/n\mathbb{Z}$ with $t$ colors that uses every color and is rainbow-free for
$x - y = f(z)$: no $x, y, z \in \mathbb{Z}/n\mathbb{Z}$ with $x - y = f(z)$ have $c(x), c(y), c(z)$
pairwise distinct. For $v \in \mathbb{Z}/n\mathbb{Z}$, call the set of $a$ with
$f^m(a) = f^{m'}(v)$ for some natural numbers $m, m'$ the component of $v$, where $f^m$ is the
$m$-th iterate of $f$. If no element of the component of $v$ has the color $c(0)$, then all its
elements have the same color.

The source record prints the equation as $x - y = f(x)$; the paper's proof uses the solution
$(f(a), 0, a)$ of $x - y = f(z)$, and the reading $x - y = f(x)$ fails on small examples.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Lemma 11.

Stated but not proved: `MetaMathlibExt.component_monochromatic_of_rainbowFree` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#component-monochromatic-of-rainbow-free).

## Cycle vertices of the $k$-th power map modulo $p$

Let $p$ be an odd prime, $k$ a natural
number, and $t$ the largest divisor of $p - 1$ that is coprime to $k$. A nonzero
$a \in \mathbb{Z}/p\mathbb{Z}$ lies on a cycle of the map $x \mapsto x^k$, that is,
$a^{k^m} = a$ for some $m \ge 1$, if and only if the multiplicative order of $a$ divides $t$.

Only this characterization is stated; the source's further claims (there are $t + 1$ cycle
vertices, and two components exactly when $t = 1$) are not.

## Sources

- Katie Ansaldi, Gabriel Cowley, Eric Green, Kihyun Kim and JT Rapp, *Rainbow-Free Colorings and Rainbow Numbers for x-y=z^k*, INTEGERS 24 (2024), Article A105, Theorem 6 (after Lucheta, Miller and Reiter).

Stated but not proved: `MetaMathlibExt.isCycleVertex_powMap_iff_orderOf_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/RainbowPowerDifferenceWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html#is-cycle-vertex-pow-map-iff-order-of-dvd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rainbow-free colorings for x − y = z^k](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/rainbow-free-colorings-for-x-y-z-k)
