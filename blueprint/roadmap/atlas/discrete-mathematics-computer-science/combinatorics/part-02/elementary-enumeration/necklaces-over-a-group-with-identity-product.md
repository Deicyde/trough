---
declaration: section
origin: cited
lean: MetaMathlibExt.identity_product_necklace_count, MetaMathlibExt.tupleRotationOrbit, MetaMathlibExt.self_mem_tupleRotationOrbit, MetaMathlibExt.comp_finRotate_mem_tupleRotationOrbit, MetaMathlibExt.identityProductNecklace_count_pi_cyclic, MetaMathlibExt.sum_div_mul_eq_sum_totient_mul, MetaMathlibExt.int_dvd_mul_iff_div_gcd_dvd, MetaMathlibExt.card_pow_eq_one_zmod
statement: formalized
---

# Necklaces over a group with identity product

24 results, 4 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html).

## Counting necklaces with identity product

Let $G$ be a finite group and $n \ge 1$. For an
$n$-tuple $x = (x_0, \dots, x_{n-1}) \in G^n$ let its necklace be the set of its $n$ cyclic
rotations $(x_m, x_{m+1}, \dots, x_{m+n-1})$, $0 \le m < n$, with indices taken mod $n$. Then the
number of necklaces of tuples $x$ with $x_0 x_1 \cdots x_{n-1} = 1$ is

$$\frac{1}{n} \sum_{d \mid n} \varphi(n/d) \, r_{n/d}(G) \, |G|^{d-1},$$

where $\varphi$ is Euler's totient function and $r_k(G)$ is the number of $g \in G$ with
$g^k = 1$.

## Sources

- Darij Grinberg and Peter Mao, "Necklaces over a Group with Identity Product," Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 1 (`thm.main`), lines 186–195, <https://cs.uwaterloo.ca/journals/JIS/VOL29/Grinberg/grinberg2.tex>. Identity-product tuples, divisor-count notation, and necklaces defined at lines 140–180.

Formalized by `MetaMathlibExt.identity_product_necklace_count`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/IdentityProductNecklace.lean, line 843](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/IdentityProductNecklace.lean#L843). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#identity-product-necklace-count).

## Rotation orbit of a tuple

Let $x = (x_0, \dots, x_{n-1})$ be a tuple of length $n$ with
entries in a type $\alpha$, and let $\sigma$ be the cyclic rotation of $\{0, \dots, n-1\}$ that
sends $i$ to $i + 1$ for $i < n - 1$ and sends $n - 1$ to $0$. The rotation orbit of $x$ is the
set of tuples $x \circ \sigma^m$ for $m \in \mathbb{N}$, that is, of the cyclic shifts
$(x_m, x_{m+1}, \dots, x_{m+n-1})$ of $x$, with indices taken modulo $n$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Definition 2.3 (the action of `C_n` by rotation; necklaces are its orbits), used by Theorem 16 (`jis-2026-26.4.6-thm-16`).

Formalized by `MetaMathlibExt.tupleRotationOrbit`, a definition declared in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#tuple-rotation-orbit).

## A tuple lies in its own rotation orbit

Every tuple $x$ of length $n$ with entries in a
type $\alpha$ belongs to the rotation orbit of $x$.

## Sources

- Grinberg and Mao, Journal of Integer Sequences 29 (2026), Article 26.4.6, Definition 2.3.

Formalized by `MetaMathlibExt.self_mem_tupleRotationOrbit`, a theorem declared in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#self-mem-tuple-rotation-orbit).

## One-step rotation stays in the rotation orbit

For every tuple
$x = (x_0, \dots, x_{n-1})$ with entries in a type $\alpha$, the tuple whose $i$-th entry is
$x_{i+1}$, indices taken modulo $n$ (that is, $(x_1, \dots, x_{n-1}, x_0)$ when $n \ge 1$), lies in
the rotation orbit of $x$.

## Sources

- Grinberg and Mao, Journal of Integer Sequences 29 (2026), Article 26.4.6, Definition 2.3.

Formalized by `MetaMathlibExt.comp_finRotate_mem_tupleRotationOrbit`, a theorem declared in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#comp-fin-rotate-mem-tuple-rotation-orbit).

## Identity-product necklaces over a product of cyclic groups

Let $k_1, \dots, k_m$ be
positive integers and let $G = C_{k_1} \times \dots \times C_{k_m}$, where $C_k$ is the cyclic
group $\mathbb{Z} / k\mathbb{Z}$ written multiplicatively. For $n \ge 1$, the number of rotation
orbits of $n$-tuples $(x_1, \dots, x_n) \in G^n$ with $x_1 x_2 \cdots x_n = 1$ (identity-product
$n$-necklaces) is

$$\frac{1}{n} \sum_{d \mid n} \varphi(n/d) \prod_{i=1}^{m} \gcd(k_i, n/d)\, k_i^{d-1},$$

where $\varphi$ is Euler's totient function.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Corollary 6 (`jis-2026-26.4.6-cor-6`).

Stated but not proved: `MetaMathlibExt.identityProductNecklace_count_pi_cyclic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#identity-product-necklace-count-pi-cycli).

## Totient-weighted divisor sum identity

Let $f$ and $g$ be functions from the natural
numbers to the rational numbers such that $g(k) = \sum_{d \mid k} f(d)$ for every positive
integer $k$, where sums over $d \mid k$ run over the positive divisors $d$ of $k$. Then for
every positive integer $k$,

$$\sum_{d \mid k} \frac{k}{d} \, f(d) = \sum_{d \mid k} \varphi\left(\frac{k}{d}\right) g(d),$$

where $\varphi$ is Euler's totient function.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 9 (`jis-2026-26.4.6-lem-9`).

Stated but not proved: `MetaMathlibExt.sum_div_mul_eq_sum_totient_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#sum-div-mul-eq-sum-totient-mul).

## Divisibility of a product through the gcd

Let $a, b, c$ be integers with $a$ and $b$ not
both zero. Then $a$ divides $bc$ if and only if $a / \gcd(a, b)$ divides $c$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 11 (`jis-2026-26.4.6-lem-11`).

Stated but not proved: `MetaMathlibExt.int_dvd_mul_iff_div_gcd_dvd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#int-dvd-mul-iff-div-gcd-dvd).

## Counting solutions of $x^b = 1$ in a cyclic group

For natural numbers $a \ge 1$ and
$b$, the cyclic group of order $a$ has exactly $\gcd(a, b)$ elements $x$ with $x^b = 1$.

The paper takes $b$ positive; for $b = 0$ both sides equal $a$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 12 (`jis-2026-26.4.6-lem-12`).

Stated but not proved: `MetaMathlibExt.card_pow_eq_one_zmod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-pow-eq-one-zmod).

## Counting identity-product tuples with a given period

Let $G$ be a finite group,
$n \ge 1$ and $k$ a divisor of $n$. The number of tuples $x = (x_0, \dots, x_{n-1}) \in G^n$
with $x_0 x_1 \cdots x_{n-1} = 1$ and $x_{i+k} = x_i$ for all $i$ (indices taken mod $n$) is
$r_{n/k}(G) \, |G|^{k-1}$, where $r_m(G)$ is the number of $g \in G$ with $g^m = 1$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 13, with `A_k` as defined in Section 5 of the arXiv text (`jis-2026-26.4.6-lem-13`).

Stated but not proved: `MetaMathlibExt.card_identityProduct_period` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-identity-product-period).

## Splitting periodic identity-product tuples by smallest period

Let $G$ be a finite
group, $n$ a natural number and $k \ge 1$. Say that $x = (x_0, \dots, x_{n-1}) \in G^n$ has
period $l$ if $x_{i+l} = x_i$ for all $i$, with indices taken mod $n$. Let $A_k$ be the set of
tuples $x$ with $x_0 x_1 \cdots x_{n-1} = 1$ and period $k$, and for $d \ge 1$ let $P_d$ be the
set of tuples $x$ with $x_0 x_1 \cdots x_{n-1} = 1$ that have period $d$ but no period $l$ with
$0 < l < d$. Then $|A_k| = \sum_{d \mid k} |P_d|$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 14, with `A_k`, `P_k` as in equation (9) of the arXiv text (`jis-2026-26.4.6-lem-14`).

Stated but not proved: `MetaMathlibExt.card_identityProduct_period_eq_sum_smallestPeriod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-identity-product-period-eq-sum-smal).

## Counting aperiodic necklaces with identity product

Let $G$ be a finite group and
$n \ge 1$. For an $n$-tuple $x = (x_0, \dots, x_{n-1}) \in G^n$ let its rotation orbit be the set
of its cyclic rotations $(x_m, x_{m+1}, \dots, x_{m+n-1})$, $m \ge 0$, with indices taken mod
$n$. Then the number of rotation orbits with exactly $n$ elements of tuples $x$ with
$x_0 x_1 \cdots x_{n-1} = 1$ is

$$\frac{1}{n} \sum_{d \mid n} \mu(n/d) \, r_{n/d}(G) \, |G|^{d-1},$$

where $\mu$ is the Möbius function and $r_k(G)$ is the number of $g \in G$ with $g^k = 1$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 16 (`jis-2026-26.4.6-thm-16`).

Stated but not proved: `MetaMathlibExt.aperiodic_identityProductNecklace_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#aperiodic-identity-product-necklace-coun).

## Identity-product necklaces with a given smallest period

Let $G$ be a finite group, let
$n \ge 1$ and let $k$ be a divisor of $n$. The number of rotation orbits of size $k$ of $n$-tuples
$(x_1, \dots, x_n) \in G^n$ with $x_1 x_2 \cdots x_n = 1$ (identity-product $n$-necklaces of
smallest period $k$) is

$$\frac{1}{k} \sum_{d \mid k} \mu(k/d)\, N(n/d)\, |G|^{d-1},$$

where $\mu$ is the Möbius function and $N(e)$ is the number of $g \in G$ with $g^e = 1$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Corollary 18 (`jis-2026-26.4.6-cor-18`).

Stated but not proved: `MetaMathlibExt.identityProductNecklace_count_smallestPeriod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#identity-product-necklace-count-smallest).

## Counting tuples up to rotation and left multiplication

Let $G$ be a finite group and let
$n \ge 1$. Let $C_n \times G$ act on $G^n$, the cyclic group $C_n$ rotating tuples and $h \in G$
multiplying every entry on the left, so that the orbit of $x = (x_0, \dots, x_{n-1})$ is the set
of tuples $(h x_m, h x_{m+1}, \dots, h x_{m+n-1})$, indices taken modulo $n$, for $m \in \mathbb{N}$
and $h \in G$. The number of these orbits is

$$\frac{1}{n} \sum_{d \mid n} \varphi(n/d)\, N(n/d)\, |G|^{d-1},$$

where $\varphi$ is Euler's totient function and $N(e)$ is the number of $g \in G$ with $g^e = 1$.

The same formula counts the identity-product $n$-necklaces over $G$ (Theorem 5 of the paper), so
the two counts agree.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 19, with the action of Section 7 of the arXiv text (`jis-2026-26.4.6-thm-19`).

Stated but not proved: `MetaMathlibExt.homogeneousNecklace_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#homogeneous-necklace-count).

## Counting necklaces with product in a conjugation-closed set

Let $G$ be a finite group,
let $K \subseteq G$ be closed under conjugation ($g k g^{-1} \in K$ for all $g \in G$ and
$k \in K$), and let $n \ge 1$. The number of rotation orbits of $n$-tuples
$(x_1, \dots, x_n) \in G^n$ with $x_1 x_2 \cdots x_n \in K$ ($K$-product $n$-necklaces) is

$$\frac{1}{n} \sum_{d \mid n} \varphi(n/d)\, N_K(n/d)\, |G|^{d-1},$$

where $\varphi$ is Euler's totient function and $N_K(e)$ is the number of $a \in G$ with
$a^e \in K$.

The printed Theorem 22 has $N_K(n)$ in place of $N_K(n/d)$; the arXiv text (Theorem 8.3) has
$n/d$, and the printed formula fails for $G = S_3$, $K = \{1\}$, $n = 2$ ($5$ necklaces against
$14$).

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 22 (`jis-2026-26.4.6-thm-22`).

Stated but not proved: `MetaMathlibExt.productInNecklace_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#product-in-necklace-count).

## Counting periodic tuples with product in a conjugation-closed set

Let $G$ be a finite
group, let $K \subseteq G$ satisfy $g c g^{-1} \in K$ for all $g \in G$ and $c \in K$, let
$n \ge 1$ and let $k$ be a divisor of $n$. The number of tuples
$x = (x_0, \dots, x_{n-1}) \in G^n$ with $x_0 x_1 \cdots x_{n-1} \in K$ and $x_{i+k} = x_i$ for
all $i$ (indices taken mod $n$) is $\#\{a \in G : a^{n/k} \in K\} \cdot |G|^{k-1}$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 23 (`jis-2026-26.4.6-lem-23`).

Stated but not proved: `MetaMathlibExt.card_productIn_period` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-product-in-period).

## Counting aperiodic necklaces with product in a conjugation-closed set

Let $G$ be a
finite group, let $K \subseteq G$ satisfy $g c g^{-1} \in K$ for all $g \in G$ and $c \in K$, and
let $n \ge 1$. For an $n$-tuple $x = (x_0, \dots, x_{n-1}) \in G^n$ let its rotation orbit be the
set of its cyclic rotations $(x_m, x_{m+1}, \dots, x_{m+n-1})$, $m \ge 0$, with indices taken mod
$n$. Then the number of rotation orbits with exactly $n$ elements of tuples $x$ with
$x_0 x_1 \cdots x_{n-1} \in K$ is

$$\frac{1}{n} \sum_{d \mid n} \mu(n/d) \, \#\{a \in G : a^{n/d} \in K\} \, |G|^{d-1},$$

where $\mu$ is the Möbius function.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 24 (`jis-2026-26.4.6-thm-24`).

Stated but not proved: `MetaMathlibExt.aperiodic_productInNecklace_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#aperiodic-product-in-necklace-count).

## Normal basis theorem for finite fields

Let $K$ be a finite field that is an algebra over
a finite field $F$. Then there is an element $\beta \in K$ whose images $\sigma(\beta)$, as $\sigma$
ranges over the $F$-algebra automorphisms of $K$, are linearly independent over $F$ (as a family
indexed by $\sigma$).

Since $K / F$ is Galois, there are $[K : F]$ such automorphisms, so these images form a basis of
$K$ over $F$, a normal basis.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 27 (`jis-2026-26.4.6-thm-27`).

Stated but not proved: `MetaMathlibExt.exists_normalBasis_finiteField` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#exists-normal-basis-finite-field).

## Normal basis coordinates turn Frobenius into rotation

Let $K$ be a finite field that is an
algebra over a finite field $F$, let $q = |F|$ and $n = [K : F]$, and let $\beta \in K$ be such
that $\beta, \beta^q, \dots, \beta^{q^{n-1}}$ are linearly independent over $F$. Define
$\Phi : F^n \to K$ by $\Phi(a_0, \dots, a_{n-1}) = \sum_{i=0}^{n-1} a_i \beta^{q^i}$. Then $\Phi$ is
a bijection, and for every $a \in F^n$,

$$\Phi(a_0, \dots, a_{n-1})^q = \Phi(a_{n-1}, a_0, a_1, \dots, a_{n-2}),$$

that is, raising to the $q$-th power rotates the coordinates one step.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Lemma 28, with `Φ` as defined in Section 9 of the arXiv text (`jis-2026-26.4.6-lem-28`).

Stated but not proved: `MetaMathlibExt.normalBasisMap_bijective_frobenius` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#normal-basis-map-bijective-frobenius).

## Rotation orbits correspond to conjugate elements

Let $K$ be a finite field that is an
algebra over a finite field $F$, let $q = |F|$ and $n = [K : F]$, and let $\beta \in K$ be such
that $\beta, \beta^q, \dots, \beta^{q^{n-1}}$ are linearly independent over $F$. Define
$\Phi : F^n \to K$ by $\Phi(a_0, \dots, a_{n-1}) = \sum_{i=0}^{n-1} a_i \beta^{q^i}$. Then for all
$a, b \in F^n$, the tuple $b$ lies in the rotation orbit of $a$ if and only if $\Phi(a)$ and
$\Phi(b)$ have the same minimal polynomial over $F$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Corollary 29 (`jis-2026-26.4.6-cor-29`).

Stated but not proved: `MetaMathlibExt.normalBasisMap_rotation_iff_conj` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#normal-basis-map-rotation-iff-conj).

## Zero-sum tuples correspond to trace-zero elements

Let $K$ be a finite field that is an
algebra over a finite field $F$, let $q = |F|$ and $n = [K : F]$, and let $\beta \in K$ be such
that $\beta, \beta^q, \dots, \beta^{q^{n-1}}$ are linearly independent over $F$. Define
$\Phi : F^n \to K$ by $\Phi(a_0, \dots, a_{n-1}) = \sum_{i=0}^{n-1} a_i \beta^{q^i}$. Then for
every $a = (a_0, \dots, a_{n-1}) \in F^n$, we have $a_0 + a_1 + \dots + a_{n-1} = 0$ if and only if
the trace of $\Phi(a)$ from $K$ to $F$ is $0$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Theorem 30 (`jis-2026-26.4.6-thm-30`).

Stated but not proved: `MetaMathlibExt.normalBasisMap_sum_eq_zero_iff_trace` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#normal-basis-map-sum-eq-zero-iff-trace).

## Trace-zero Galois orbits and zero-sum necklaces

Let $K$ be a finite field extension
of a finite field $F$ and $n = [K : F]$. For $z \in K$ let its Galois orbit be the set of all
$\sigma(z)$ with $\sigma$ an automorphism of $K$ fixing $F$, and for
$a = (a_0, \dots, a_{n-1}) \in F^n$ let its rotation orbit be the set of its cyclic rotations
$(a_m, a_{m+1}, \dots, a_{m+n-1})$, $m \ge 0$, with indices taken mod $n$. The number of Galois
orbits of elements $z \in K$ with $\operatorname{Tr}_{K/F}(z) = 0$ equals the number of rotation
orbits of tuples $a \in F^n$ with $a_0 + a_1 + \dots + a_{n-1} = 0$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Corollary 31 (`jis-2026-26.4.6-cor-31`).

Stated but not proved: `MetaMathlibExt.card_traceZero_conjClasses` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-trace-zero-conj-classes).

## Trace-zero Galois orbits of full size and aperiodic zero-sum necklaces

Let $K$ be a
finite field extension of a finite field $F$ and $n = [K : F]$. For $z \in K$ let its Galois
orbit be the set of all $\sigma(z)$ with $\sigma$ an automorphism of $K$ fixing $F$, and for
$a = (a_0, \dots, a_{n-1}) \in F^n$ let its rotation orbit be the set of its cyclic rotations
$(a_m, a_{m+1}, \dots, a_{m+n-1})$, $m \ge 0$, with indices taken mod $n$. The number of Galois
orbits with exactly $n$ elements of elements $z \in K$ with $\operatorname{Tr}_{K/F}(z) = 0$
equals the number of rotation orbits with exactly $n$ elements of tuples $a \in F^n$ with
$a_0 + a_1 + \dots + a_{n-1} = 0$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Proposition 32 (`jis-2026-26.4.6-prop-32`).

Stated but not proved: `MetaMathlibExt.card_traceZero_conjClasses_size_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-trace-zero-conj-classes-size-eq).

## Trace-zero elements with Galois orbits of full size

Let $K$ be a finite field
extension of a finite field $F$ and $n = [K : F]$. The number of $z \in K$ with
$\operatorname{Tr}_{K/F}(z) = 0$ whose Galois orbit, the set of all $\sigma(z)$ with $\sigma$ an
automorphism of $K$ fixing $F$, has exactly $n$ elements equals the number of tuples
$a = (a_0, \dots, a_{n-1}) \in F^n$ with $a_0 + a_1 + \dots + a_{n-1} = 0$ for which there is no
$l$ with $0 < l < n$ such that $a_{i+l} = a_i$ for all $i$ (indices taken mod $n$).

The trace condition, present in Corollary 9.9 of the arXiv text, cannot be dropped: for
$F = \mathbb{F}_2$ and $n = 3$ there are $6$ elements with Galois orbits of size $3$ but only $3$
such tuples.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Corollary 33 (`jis-2026-26.4.6-cor-33`).

Stated but not proved: `MetaMathlibExt.card_traceZero_size_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-trace-zero-size-eq).

## Monic irreducible polynomials with vanishing second coefficient

Let $F$ be a finite
field and $n \ge 1$. For $a = (a_0, \dots, a_{n-1}) \in F^n$ let its rotation orbit be the set
of its cyclic rotations $(a_m, a_{m+1}, \dots, a_{m+n-1})$, $m \ge 0$, with indices taken mod
$n$. The number of monic irreducible polynomials of degree $n$ over $F$ whose coefficient of
$X^{n-1}$ is $0$ equals the number of rotation orbits with exactly $n$ elements of tuples
$a \in F^n$ with $a_0 + a_1 + \dots + a_{n-1} = 0$.

## Sources

- Darij Grinberg and Peter Mao, *Necklaces over a Group with Identity Product*, Journal of Integer Sequences 29 (2026), Article 26.4.6, Corollary 35 (`jis-2026-26.4.6-cor-35`).

Stated but not proved: `MetaMathlibExt.card_monic_irreducible_nextCoeff_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/IdentityProductNecklaceWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html#card-monic-irreducible-next-coeff-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Necklaces over a group with identity product](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/elementary-enumeration/necklaces-over-a-group-with-identity-product)
