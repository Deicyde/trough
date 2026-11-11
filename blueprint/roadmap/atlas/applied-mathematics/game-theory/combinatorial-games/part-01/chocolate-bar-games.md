---
declaration: section
origin: cited
lean: MetaMathlibExt.HasNSProperty, MetaMathlibExt.hasNSProperty_const, MetaMathlibExt.not_hasNSProperty_id, MetaMathlibExt.hasNSProperty_extend_const, MetaMathlibExt.min_div_two_pow_eq_of_div_two_pow_eq, MetaMathlibExt.HasNSProperty.min_div_two_pow_eq, MetaMathlibExt.HasNSProperty.exists_of_lt_xor, MetaMathlibExt.HasNSProperty.exists_of_lt_xor_xor
statement: formalized
---

# Chocolate bar games

33 results, 12 proved and 21 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html).

## NS property

A function $h : \mathbb{N} \to \mathbb{N}$ has the *NS property* if it is
monotone (weakly increasing) and, for all $z, z' \in \mathbb{N}$ and every natural number
$i \ge 1$, $\lfloor z / 2^i \rfloor = \lfloor z' / 2^i \rfloor$ implies
$\lfloor h(z) / 2^{i-1} \rfloor = \lfloor h(z') / 2^{i-1} \rfloor$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definition 11 (text of arXiv:2207.09134v1, NS property in Section 2).

Formalized by `MetaMathlibExt.HasNSProperty`, a definition declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#has-nsproperty).

## Constant functions have the NS property

For every natural number $c$, the constant
function $\mathbb{N} \to \mathbb{N}$ with value $c$ has the NS property.

## Sources

- characteristic lemma for the NS property of Miyadera, Manabe and Singh, INTEGERS 25 (2025), Article G3, Definition 11.

Formalized by `MetaMathlibExt.hasNSProperty_const`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#has-nsproperty-const).

## The identity function lacks the NS property

The identity function on the natural
numbers does not have the NS property: $\lfloor 0/2 \rfloor = \lfloor 1/2 \rfloor$, but
$0 \ne 1$.

## Sources

- characteristic lemma for the NS property of Miyadera, Manabe and Singh, INTEGERS 25 (2025), Article G3, Definition 11.

Formalized by `MetaMathlibExt.not_hasNSProperty_id`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#not-has-nsproperty-id).

## Constant extension preserves the NS property

Let $z \in \mathbb{N}$ and let
$h : \mathbb{N} \to \mathbb{N}$ satisfy $h(a) \le h(b)$ whenever $a \le b \le z$, and
$\lfloor h(a) / 2^{i-1} \rfloor = \lfloor h(b) / 2^{i-1} \rfloor$ whenever $a, b \le z$,
$i \ge 1$ and $\lfloor a / 2^i \rfloor = \lfloor b / 2^i \rfloor$. Then the function sending
$x$ to $h(x)$ for $x \le z$ and to $h(z)$ for $x > z$ has the NS property.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 1.

Stated but not proved: `MetaMathlibExt.hasNSProperty_extend_const` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#has-nsproperty-extend-const).

## Taking a minimum preserves quotients by powers of two

Let $a, b, c, k \in \mathbb{N}$. If
$\lfloor a / 2^k \rfloor = \lfloor b / 2^k \rfloor$, then
$\lfloor \min(a, c) / 2^k \rfloor = \lfloor \min(b, c) / 2^k \rfloor$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 2 (i).

Stated but not proved: `MetaMathlibExt.min_div_two_pow_eq_of_div_two_pow_eq` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#min-div-two-pow-eq-of-div-two-pow-eq).

## Quotients of a truncated NS function by powers of two

Let $h : \mathbb{N} \to \mathbb{N}$
have the NS property and let $z, z', k \in \mathbb{N}$ with $k \ge 1$ and
$\lfloor z' / 2^k \rfloor = \lfloor z / 2^k \rfloor$. Then for every $y \in \mathbb{N}$,
$\lfloor \min(h(z'), y) / 2^{k-1} \rfloor = \lfloor \min(h(z), y) / 2^{k-1} \rfloor$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 2 (ii).

Stated but not proved: `MetaMathlibExt.HasNSProperty.min_div_two_pow_eq` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#min-div-two-pow-eq).

## Mex step for chocolate bars with one function

Let $g : \mathbb{N} \to \mathbb{N}$ have
the NS property, and let $x, z, c$ be natural numbers with $x \le g(z)$ and $c < x \oplus z$,
where $\oplus$ is nim-sum (bitwise exclusive or). Then $c = u \oplus z$ for some $u < x$, or
$c = \min(g(w), x) \oplus w$ for some $w < z$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 3 (a).

Stated but not proved: `MetaMathlibExt.HasNSProperty.exists_of_lt_xor` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#exists-of-lt-xor).

## Mex step for chocolate bars with two functions

Let $g, h : \mathbb{N} \to \mathbb{N}$
have the NS property, and let $x, y, z, c$ be natural numbers with $x \le g(z)$, $y \le h(z)$
and $c < x \oplus y \oplus z$, where $\oplus$ is nim-sum (bitwise exclusive or). Then
$c = u \oplus y \oplus z$ for some $u < x$, or $c = x \oplus v \oplus z$ for some $v < y$, or
$c = \min(g(w), x) \oplus \min(h(w), y) \oplus w$ for some $w < z$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 3 (b).

Stated but not proved: `MetaMathlibExt.HasNSProperty.exists_of_lt_xor_xor` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#exists-of-lt-xor-xor).

## Mex step for chocolate bars with many functions

Let $m$ be a natural number, let
$f_1, \dots, f_m : \mathbb{N} \to \mathbb{N}$ have the NS property, and let
$x_1, \dots, x_m, z, c$ be natural numbers with $x_t \le f_t(z)$ for all $t$ and
$c < x_1 \oplus \cdots \oplus x_m \oplus z$, where $\oplus$ is nim-sum (bitwise exclusive or).
Then either there are an index $i$ and some $u < x_i$ such that $c$ is the nim-sum
$x_1 \oplus \cdots \oplus x_m \oplus z$ with $x_i$ replaced by $u$, or there is some $w < z$
with $c = \min(x_1, f_1(w)) \oplus \cdots \oplus \min(x_m, f_m(w)) \oplus w$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 4.

Stated but not proved: `MetaMathlibExt.exists_of_lt_foldl_xor` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#exists-of-lt-foldl-xor).

## Nim-sum image identity for two NS functions

Let $g, h : \mathbb{N} \to \mathbb{N}$ have
the NS property and let $x, y, z \in \mathbb{N}$ with $x \le g(z)$ and $y \le h(z)$. Writing
$\oplus$ for the nim-sum (bitwise exclusive or) of natural numbers, the sets
$\{x \oplus y \oplus w : w < z\}$ and $\{\min(g(w), x) \oplus \min(h(w), y) \oplus w : w < z\}$
are equal, where $w$ ranges over the natural numbers.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 5, equation (19).

Stated but not proved: `MetaMathlibExt.HasNSProperty.image_xor_xor_eq` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#image-xor-xor-eq).

## Nim-sum image identity for one NS function

Let $g : \mathbb{N} \to \mathbb{N}$ have the
NS property and let $x, z \in \mathbb{N}$ with $x \le g(z)$. Writing $\oplus$ for the nim-sum
(bitwise exclusive or) of natural numbers, the sets $\{x \oplus w : w < z\}$ and
$\{\min(g(w), x) \oplus w : w < z\}$ are equal, where $w$ ranges over the natural numbers.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 5, equation (20).

Stated but not proved: `MetaMathlibExt.HasNSProperty.image_xor_eq` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#image-xor-eq).

## Halving functions have the NS property

For every natural number $m \ge 1$, the function
$x \mapsto \lfloor x / 2^m \rfloor$ on $\mathbb{N}$ has the NS property.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 7.

Stated but not proved: `MetaMathlibExt.hasNSProperty_div_two_pow` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#has-nsproperty-div-two-pow).

## Equal quotients by a power of two lie in one dyadic block

Let $i$ be a natural number
and let $z < z'$ be natural numbers. Then $\lfloor z / 2^i \rfloor = \lfloor z' / 2^i \rfloor$ if
and only if there is a natural number $d$ with $d \cdot 2^i \le z$ and $z' < (d + 1) \cdot 2^i$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 8 (a).

Stated but not proved: `MetaMathlibExt.div_two_pow_eq_iff_exists_block` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#div-two-pow-eq-iff-exists-block).

## Dyadic splitting of two numbers with different quotients

Let $z, z', i$ be natural
numbers with $\lfloor z / 2^i \rfloor < \lfloor z' / 2^i \rfloor$. Then there are natural numbers
$c$, $s$ and $t$ with $s \ge i$, $t < 2^s$, $z = c \cdot 2^{s+1} + t$ and
$c \cdot 2^{s+1} + 2^s \le z'$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 8 (b).

Stated but not proved: `MetaMathlibExt.exists_split_of_div_two_pow_lt` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#exists-split-of-div-two-pow-lt).

## Indicator functions with the NS property

Let $f : \mathbb{N} \to \mathbb{N}$ be monotone,
with $f(x) \le 1$ for all $x$ and $f(x) = 1$ for some $x$. Then $f$ has the NS property if and
only if there is an even $m \in \mathbb{N}$ such that $f$ is the indicator function of
$\{n \in \mathbb{N} : n \ge m\}$, that is, $f(n) = 1$ for $n \ge m$ and $f(n) = 0$ for $n < m$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 9.

Stated but not proved: `MetaMathlibExt.indicator_Ici_even_iff_hasNSProperty` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#indicator-ici-even-iff-has-nsproperty).

## Grundy number of a chocolate bar

Let $f_1, \dots, f_s : \mathbb{N} \to \mathbb{N}$. For
coordinates $x = (x_1, \dots, x_s) \in \mathbb{N}^s$ and a width $z \in \mathbb{N}$, the position
$(x, z)$ stands for the chocolate bar $\mathrm{CB}(f_1, \dots, f_s, x_1, \dots, x_s, z)$, whose
column at width $w \le z$ extends $\min(f_t(w), x_t) + 1$ cells along axis $t$. A move either
lowers one coordinate $x_i$ to some $u < x_i$, keeping the width $z$, or cuts the width to some
$w < z$, which replaces every $x_t$ by $\min(x_t, f_t(w))$. The Grundy number of $(x, z)$ is the
mex (least natural number not attained) of the Grundy numbers of the positions reachable from
$(x, z)$ in one move. It is defined for all $(x, z)$; the bars themselves are the positions with
$x_t \le f_t(z)$ for all $t$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definitions 2, 8, 9 and 10 (two functions) and Section 4, before Theorem 5 (four functions).

Formalized by `MetaMathlibExt.chocolateBarGrundy`, a definition declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#chocolate-bar-grundy).

## Mex recursion for the Grundy number of a chocolate bar

Let $f_1, \dots, f_s$ be
functions $\mathbb{N} \to \mathbb{N}$ and write $G(x, z)$ for the Grundy number of the chocolate
bar with coordinates $x = (x_1, \dots, x_s) \in \mathbb{N}^s$ and width $z \in \mathbb{N}$. For
all $x$ and $z$, $G(x, z)$ is the least natural number $m$ such that $m \ne G(x', z)$ for every
$x'$ obtained from $x$ by replacing one coordinate $x_i$ with some $u < x_i$, and
$m \ne G(x^{(w)}, w)$ for every $w < z$, where $x^{(w)}_t = \min(x_t, f_t(w))$ for all $t$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definitions 9 and 10.

Formalized by `MetaMathlibExt.chocolateBarGrundy_eq`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#chocolate-bar-grundy-eq).

## The single bitter square has Grundy number zero

For all functions
$f_1, \dots, f_s : \mathbb{N} \to \mathbb{N}$, the chocolate bar
$\mathrm{CB}(f_1, \dots, f_s, 0, \dots, 0, 0)$, whose coordinates and width are all $0$, has
Grundy number $0$: it is a single bitter square and has no move.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definitions 9 and 10.

Formalized by `MetaMathlibExt.chocolateBarGrundy_zero`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#chocolate-bar-grundy-zero).

## Grundy number of a chocolate bar with a height function

Let $s \in \mathbb{N}$ and
$F : \mathbb{N}^s \to \mathbb{N}$. The $(s + 1)$-dimensional chocolate bar
$\mathrm{CB}(F, x_1, \dots, x_s, y)$ has, at each $u = (u_1, \dots, u_s)$ with $u_t \le x_t$ for
all $t$, a column of height $\min(F(u), y) + 1$. A move either lowers one coordinate $x_i$ to some
$a < x_i$, which clamps the height to $\min(F(x'), y)$ for the new position $x'$, or lowers the
height $y$ to some $v < y$. The Grundy number of $\mathrm{CB}(F, x_1, \dots, x_s, y)$ is the mex
(least natural number not attained) of the Grundy numbers of the positions reachable in one
move. It is defined for all $x \in \mathbb{N}^s$ and $y \in \mathbb{N}$; the bars themselves are
the positions with $y \le F(x)$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definitions 15, 16 and 17 (and Definition 13 with second function `0`).

Formalized by `MetaMathlibExt.heightChocolateBarGrundy`, a definition declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#height-chocolate-bar-grundy).

## Mex recursion for chocolate bars with a height function

Let $s \in \mathbb{N}$ and
$F : \mathbb{N}^s \to \mathbb{N}$, and write $G(x, y)$ for the Grundy number of the chocolate bar
$\mathrm{CB}(F, x_1, \dots, x_s, y)$. For all $x \in \mathbb{N}^s$ and $y \in \mathbb{N}$,
$G(x, y)$ is the least natural number $m$ such that $m \ne G(x', \min(F(x'), y))$ for every $x'$
obtained from $x$ by lowering one coordinate $x_i$ to some $u < x_i$, and $m \ne G(x, v)$ for
every $v < y$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definition 17.

Formalized by `MetaMathlibExt.heightChocolateBarGrundy_eq`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#height-chocolate-bar-grundy-eq).

## The single bitter cube has Grundy number zero

For every $s \in \mathbb{N}$ and every
$F : \mathbb{N}^s \to \mathbb{N}$, the chocolate bar $\mathrm{CB}(F, 0, \dots, 0, 0)$ has no move,
so its Grundy number is $0$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Definition 17.

Formalized by `MetaMathlibExt.heightChocolateBarGrundy_zero`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#height-chocolate-bar-grundy-zero).

## Pass indicator of Nim with a restricted pass

For $s$ piles with thresholds
$m_0, \dots, m_{s-1}$ and pile sizes $x_0, \dots, x_{s-1}$ (natural numbers), the pass
indicator is $1$ if $m_j \le x_j$ for some pile $j$ (the pass may be used), and $0$ if
$x_j < m_j$ for every pile $j$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 10 and Corollary 2 (the function `F`).

Formalized by `MetaMathlibExt.nimPassIndicator`, a definition declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#nim-pass-indicator).

## The Nim pass indicator is at most one

For every $s \in \mathbb{N}$ and all
$m, x \in \mathbb{N}^s$, the pass indicator of $m$ at $x$ is at most $1$; that is, it takes values
in $\{0, 1\}$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 10 (the function `F`).

Formalized by `MetaMathlibExt.nimPassIndicator_le_one`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#nim-pass-indicator-le-one).

## The pass is unavailable from the empty position

Let $s \in \mathbb{N}$ and
$m \in \mathbb{N}^s$ with $m_i > 0$ for every $i < s$. Then the pass indicator of $m$ takes the
value $0$ at the zero tuple $(0, \dots, 0)$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 10 (the function `F`).

Formalized by `MetaMathlibExt.nimPassIndicator_zero`, a theorem declared in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#nim-pass-indicator-zero).

## Nim-sum sets under clamping by functions with the NS property

Let $m \in \mathbb{N}$,
let $f_0, \dots, f_{m-1} : \mathbb{N} \to \mathbb{N}$ have the NS property, and let
$x_0, \dots, x_{m-1}, z \in \mathbb{N}$ satisfy $x_t \le f_t(z)$ for every $t < m$. Then

$$
\{x_0 \oplus \cdots \oplus x_{m-1} \oplus w : w < z\} =
\{\min(x_0, f_0(w)) \oplus \cdots \oplus \min(x_{m-1}, f_{m-1}(w)) \oplus w : w < z\},
$$

where $\oplus$ denotes nim-sum (bitwise exclusive or).

The printed left-hand nim-sum carries a stray index $j \ne i$ with $i$ unbound; it is read as the
full nim-sum, as in Lemma 5 (the case of two functions), which the proof generalises.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 6.

Stated but not proved: `MetaMathlibExt.image_foldl_xor_eq_image_min` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#image-foldl-xor-eq-image-min).

## The NS property characterises nim-sum Grundy numbers of two-dimensional chocolate bars

Let $f : \mathbb{N} \to \mathbb{N}$ be monotone. Then $f$ has the NS property if and only if, for
all $x, z \in \mathbb{N}$ with $x \le f(z)$, the chocolate bar $\mathrm{CB}(f, 0, x, 0, z)$ of
width $z$ (first function $f$, first coordinate $x$, second function constantly $0$, second
coordinate $0$) has Grundy number $x \oplus z$, where $\oplus$ denotes nim-sum (bitwise exclusive
or).

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Theorem 2.

Stated but not proved: `MetaMathlibExt.hasNSProperty_iff_chocolateBarGrundy_depth_zero` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#has-nsproperty-iff-chocolate-bar-grundy).

## NS property of sections and the three-dimensional chocolate bar

Let
$F : \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ be monotone for the componentwise order. Then
the sections $x \mapsto F(n, x)$ and $w \mapsto F(w, n)$ have the NS property for every
$n \in \mathbb{N}$ if and only if, for all natural numbers $w$, $x$, $y$ with $y \le F(w, x)$,
the Grundy number of the chocolate bar $\mathrm{CB}(F, w, x, y)$, whose column at $(u, v)$
(with $u \le w$, $v \le x$) has height $\min(F(u, v), y) + 1$, equals the nim-sum
$w \oplus x \oplus y$ (bitwise exclusive or).

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Theorem 3.

Stated but not proved: `MetaMathlibExt.sections_hasNSProperty_iff_heightChocolateBarGrundy_eq_xor` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#sections-has-nsproperty-iff-height-choco).

## Nim-sum Grundy numbers of chocolate bars with two functions

Let
$g, h : \mathbb{N} \to \mathbb{N}$ be monotone. Then $g$ and $h$ both have the NS property if and
only if, for all natural numbers $x, y, z$ with $x \le g(z)$ and $y \le h(z)$, the Grundy number
of the chocolate bar $\mathrm{CB}(g, h, x, y, z)$ equals $x \oplus y \oplus z$, where $\oplus$ is
nim-sum (bitwise exclusive or).

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Theorem 4.

Stated but not proved: `MetaMathlibExt.hasNSProperty_and_iff_chocolateBarGrundy_eq_xor` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#has-nsproperty-and-iff-chocolate-bar-gru).

## Nim-sum Grundy numbers of chocolate bars with four functions

Let
$f_1, f_2, f_3, f_4 : \mathbb{N} \to \mathbb{N}$ be monotone. Then all four have the NS property if
and only if, for all natural numbers $x_1, x_2, x_3, x_4, z$ with $x_t \le f_t(z)$ for every $t$,
the Grundy number of the chocolate bar $\mathrm{CB}(f_1, f_2, f_3, f_4, x_1, x_2, x_3, x_4, z)$
equals $x_1 \oplus x_2 \oplus x_3 \oplus x_4 \oplus z$, where $\oplus$ is nim-sum (bitwise
exclusive or).

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Theorem 5.

Stated but not proved: `MetaMathlibExt.forall_hasNSProperty_iff_chocolateBarGrundy_eq_xor_four` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#forall-has-nsproperty-iff-chocolate-bar).

## P-positions of a three-dimensional chocolate bar with floor-quotient height

Let $k$ be a
natural number with $k \equiv 3 \pmod 4$, and let $F(w, x) = \lfloor (w + x) / k \rfloor$. For
all $w, x, y \in \mathbb{N}$ with $y \le F(w, x)$, the three-dimensional chocolate bar
$\mathrm{CB}(F, w, x, y)$ has Grundy number $0$ (is a P-position) if and only if
$w \oplus x \oplus y = 0$, where $\oplus$ denotes nim-sum (bitwise exclusive or).

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Theorem 8.

Stated but not proved: `MetaMathlibExt.heightChocolateBarGrundy_add_div_eq_zero_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#height-chocolate-bar-grundy-add-div-eq-z).

## Height-one chocolate bars with nim-sum Grundy numbers

Let $s \in \mathbb{N}$ and let
$F : \mathbb{N}^s \to \mathbb{N}$ be monotone for the coordinatewise order, with $F(x) \le 1$ for
all $x$. For $x \in \mathbb{N}^s$, $i < s$ and $t \in \mathbb{N}$ write $x[i \mapsto t]$ for $x$
with its $i$-th coordinate replaced by $t$, and suppose that for all $x$ and $i$ there is a $t$
with $F(x[i \mapsto t]) = 1$. Write $\oplus$ for nim-sum. Then the following are equivalent:
(a) for all $x \in \mathbb{N}^s$ and $i < s$ there is an even $m \in \mathbb{N}$ (depending on $x$
and $i$) such that $F(x[i \mapsto t]) = 1$ for $t \ge m$ and $F(x[i \mapsto t]) = 0$ for $t < m$;
(b) for all $x \in \mathbb{N}^s$ and $y \in \mathbb{N}$ with $y \le F(x)$, the Grundy number of the
chocolate bar $\mathrm{CB}(F, x_0, \dots, x_{s-1}, y)$ is
$x_0 \oplus \cdots \oplus x_{s-1} \oplus y$.

The hypothesis that every section takes the value $1$ is that of Lemma 9, from which the
corollary is derived.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Corollary 1.

Stated but not proved: `MetaMathlibExt.indicator_sections_iff_heightChocolateBarGrundy_eq_xor` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#indicator-sections-iff-height-chocolate).

## Sections of the Nim pass indicator with the NS property

Let $s \in \mathbb{N}$ and
$m \in \mathbb{N}^s$ with $m_i > 0$ for every $i < s$, and let $F : \mathbb{N}^s \to \mathbb{N}$ be
the pass indicator of $m$: $F(x) = 1$ if $m_j \le x_j$ for some $j$, and $F(x) = 0$ otherwise.
For $x \in \mathbb{N}^s$, $i < s$ and $t \in \mathbb{N}$ write $x[i \mapsto t]$ for $x$ with its
$i$-th coordinate replaced by $t$. Then the following are equivalent: (a) for all
$x \in \mathbb{N}^s$ and $i < s$, the function $t \mapsto F(x[i \mapsto t])$ has the NS property;
(b) $m_i$ is even for every $i < s$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Lemma 10.

Stated but not proved: `MetaMathlibExt.nimPassIndicator_sections_hasNSProperty_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 412](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L412). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#nim-pass-indicator-sections-has-nsproper).

## Nim with a restricted pass

Let $s \in \mathbb{N}$ and $m \in \mathbb{N}^s$ with $m_i > 0$
for every $i < s$, and let $F : \mathbb{N}^s \to \mathbb{N}$ be the pass indicator of $m$:
$F(x) = 1$ if $m_j \le x_j$ for some $j$, and $F(x) = 0$ otherwise. Write $\oplus$ for nim-sum.
Then the following are equivalent: (a) for all $x \in \mathbb{N}^s$ and $p \in \mathbb{N}$ with
$p \le F(x)$, the Grundy number of the chocolate bar $\mathrm{CB}(F, x_0, \dots, x_{s-1}, p)$ is
$x_0 \oplus \cdots \oplus x_{s-1} \oplus p$; (b) $m_i$ is even for every $i < s$.

The bar is Nim on $s$ piles with a one-time pass usable only while $F(x) = 1$: removing stones
from a pile, reaching $x'$, replaces $p$ by $\min(F(x'), p)$, and the pass lowers $p$ from $1$
to $0$.

## Sources

- Ryohei Miyadera, Hikaru Manabe and Aditi Singh, *Generalizations of Two-Dimensional and Three-Dimensional Chocolate Bar Games*, INTEGERS 25 (2025), Article G3, Corollary 2.

Stated but not proved: `MetaMathlibExt.nimPassGrundy_eq_xor_iff` is written with `theorem_wanted` in [WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GameTheory/ChocolateBarNSPropertyWanted.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html#nim-pass-grundy-eq-xor-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chocolate bar games](https://deicyde.github.io/atlas-lean/roadmap/GameTheory/combinatorial-games/chocolate-bar-games/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GameTheory/combinatorial-games/chocolate-bar-games)
