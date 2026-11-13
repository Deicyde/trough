---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMVanishingFamily, MetaMathlibExt.IsVanishingFamily, MetaMathlibExt.sumAddMulProdFamily, MetaMathlibExt.IsMVanishingFamily.mono, MetaMathlibExt.isMVanishingFamily_zero, MetaMathlibExt.sumAddMulProdFamily_two, MetaMathlibExt.isVanishingFamily_sum, MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_of_ne
statement: formalized
---

# Zero-sum van der Waerden theorems for symmetric functions

20 results, 6 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html).

## $m$-vanishing family

Let $n$ be a natural number and let $F = (f^{(l)})_{l \ge 0}$ be a
family of functions $f^{(l)} : (\mathbb{Z}/n\mathbb{Z})^l \to M$ into a type $M$ with a zero
element. For a natural number $m$, $F$ is $m$-vanishing if for every sequence
$a_0, a_1, a_2, \dots$ of elements of $\mathbb{Z}/n\mathbb{Z}$ there are a length $l > 1$ and a
start $s \ge 0$ such that $f^{(l)}(a_{s+jl}, a_{s+jl+1}, \dots, a_{s+jl+l-1}) = 0$ for every
$j < m$; that is, the sequence contains $m$ consecutive blocks of a common length $l > 1$ on each
of which $f^{(l)}$ vanishes.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Section 2 (definition of `m`-vanishing).

Formalized by `MetaMathlibExt.IsMVanishingFamily`, a definition declared in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-mvanishing-family).

## Vanishing family

Let $n$ be a natural number. A family $F$ of functions on blocks over
$\mathbb{Z}/n\mathbb{Z}$ with values in a type with a zero is vanishing if it is $m$-vanishing for
every positive integer $m$.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Section 2 (definition of vanishing).

Formalized by `MetaMathlibExt.IsVanishingFamily`, a definition declared in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-vanishing-family).

## The sum-plus-product family $F_c$

For $c \in \mathbb{Z}/n$, the family $F_c$ over
$\mathbb{Z}/n$ sends a block $(b_1, \dots, b_l)$ of elements of $\mathbb{Z}/n$, of any length
$l \ge 0$, to $b_1 + \dots + b_l + c\, b_1 b_2 \cdots b_l$, where an empty sum is $0$ and an
empty product is $1$.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Section 2 (the family `F_c`).

Formalized by `MetaMathlibExt.sumAddMulProdFamily`, a definition declared in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#sum-add-mul-prod-family).

## Monotonicity of $m$-vanishing

Let $F$ be a family of functions on blocks over
$\mathbb{Z}/n$ with values in a type $M$ with a zero. If $F$ is $m$-vanishing and $m' \le m$,
then $F$ is $m'$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Section 2 (definition of `m`-vanishing).

Formalized by `MetaMathlibExt.IsMVanishingFamily.mono`, a theorem declared in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#mono).

## Every family is $0$-vanishing

For every natural number $n$ and every family $F$ of
functions $f^{(l)} : (\mathbb{Z}/n\mathbb{Z})^l \to M$, $l \ge 0$, into a type $M$ with a zero
element, $F$ is $0$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Section 2 (definition of `m`-vanishing).

Formalized by `MetaMathlibExt.isMVanishingFamily_zero`, a theorem declared in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-mvanishing-family-zero).

## The sum-plus-product family on blocks of length two

For $c \in \mathbb{Z}/n$ and
$b_0, b_1 \in \mathbb{Z}/n$, the sum-plus-product family $F_c$ over $\mathbb{Z}/n$ satisfies
$F_c(b_0, b_1) = b_0 + b_1 + c\, b_0 b_1$.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Section 2 (the family `F_c`).

Formalized by `MetaMathlibExt.sumAddMulProdFamily_two`, a theorem declared in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#sum-add-mul-prod-family-two).

## Zero-sum van der Waerden theorem

For every positive integer $n$, the family over
$\mathbb{Z}/n\mathbb{Z}$ sending a block $(b_1, \dots, b_l)$ to $\sum_i b_i$ is vanishing: for
every $m > 0$, every sequence over $\mathbb{Z}/n\mathbb{Z}$ contains $m$ consecutive blocks of a
common length $l > 1$, each with sum zero.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Theorem 1.

Stated but not proved: `MetaMathlibExt.isVanishingFamily_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-vanishing-family-sum).

## $F_c$ with $c \notin \{0, \pm 1\}$ is not $m$-vanishing for $m > 0$

Let $n > 1$ and let
$c \in \mathbb{Z}/n$ with $c \ne 0$, $c \ne 1$ and $c \ne -1$. Then for every $m > 0$ the
sum-plus-product family $F_c$ over $\mathbb{Z}/n$,
$F_c(b_1, \dots, b_l) = b_1 + \dots + b_l + c\, b_1 \cdots b_l$, is not $m$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Theorem 2.

Stated but not proved: `MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_of_ne` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#not-is-mvanishing-family-sum-add-mul-pro).

## Classification of vanishing for the sum-plus-product family $F_1$

Let $n > 1$ and let
$F_1$ be the family over $\mathbb{Z}/n$ given by
$F_1(b_1, \dots, b_l) = b_1 + \dots + b_l + b_1 \cdots b_l$. If $n \notin \{2, 3, 4, 6, 8\}$,
then $F_1$ is not $m$-vanishing for any $m > 0$. If $n \in \{2, 3, 4, 8\}$, then $F_1$ is
vanishing. If $n = 6$, then $F_1$ is $1$-vanishing but not $m$-vanishing for any $m > 1$.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Theorem 3.

Stated but not proved: `MetaMathlibExt.sumAddMulProd_one_classification` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#sum-add-mul-prod-one-classification).

## The sum-plus-product family is vanishing over $\mathbb{Z}/3\mathbb{Z}$

Let $F_1$ be the
family over $\mathbb{Z}/3\mathbb{Z}$ sending a block $(b_1, \dots, b_l)$ to
$\sum_i b_i + \prod_i b_i$. Then $F_1$ is vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 1.

Stated but not proved: `MetaMathlibExt.isVanishingFamily_sumAddMulProd_one_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-vanishing-family-sum-add-mul-prod-one).

## The sum-plus-product family is vanishing over $\mathbb{Z}/4\mathbb{Z}$ and $\mathbb{Z}/8\mathbb{Z}$

**The sum-plus-product family is vanishing over $\mathbb{Z}/4\mathbb{Z}$ and
$\mathbb{Z}/8\mathbb{Z}$.** Let $n \in \{4, 8\}$ and let $F_1$ be the family over
$\mathbb{Z}/n\mathbb{Z}$ sending a block $(b_1, \dots, b_l)$ to $\sum_i b_i + \prod_i b_i$. Then
$F_1$ is vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 2.

Stated but not proved: `MetaMathlibExt.isVanishingFamily_sumAddMulProd_one_four_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-vanishing-family-sum-add-mul-prod-one-2).

## The sum-plus-product family is $1$-vanishing over $\mathbb{Z}/6\mathbb{Z}$

Let $F_1$ be
the family over $\mathbb{Z}/6\mathbb{Z}$ sending a block $(b_1, \dots, b_l)$ to
$\sum_i b_i + \prod_i b_i$. Then $F_1$ is $1$-vanishing: every sequence over
$\mathbb{Z}/6\mathbb{Z}$ contains a block of consecutive terms, of some length $l > 1$, on which
$F_1$ vanishes.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 3.

Stated but not proved: `MetaMathlibExt.isMVanishingFamily_one_sumAddMulProd_one_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-mvanishing-family-one-sum-add-mul-pro).

## $F_{\pm 1}$ over $\mathbb{Z}/6$ is not $m$-vanishing for $m > 1$

For every $m > 1$,
neither of the sum-plus-product families $F_{-1}$ and $F_1$ over $\mathbb{Z}/6$, where
$F_c(b_1, \dots, b_l) = b_1 + \dots + b_l + c\, b_1 \cdots b_l$, is $m$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 4.

Stated but not proved: `MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#not-is-mvanishing-family-sum-add-mul-pro-2).

## $F_1$ modulo a prime $n \equiv 1 \pmod 4$ is not $m$-vanishing for $m > 0$

Let $n$ be
a prime with $n \equiv 1 \pmod 4$. Then for every $m > 0$ the sum-plus-product family $F_1$
over $\mathbb{Z}/n$, $F_1(b_1, \dots, b_l) = b_1 + \dots + b_l + b_1 \cdots b_l$, is not
$m$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 5, quoting Theorem 3.6 of Bialostocki and Dierker.

Stated but not proved: `MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_one_prime_one_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#not-is-mvanishing-family-sum-add-mul-pro-3).

## Nonzero solutions of a two-equation system modulo primes greater than 3 congruent to 3 mod 4

**Nonzero solutions of a two-equation system modulo primes greater than 3 congruent to 3
mod 4.** Let $n > 3$ be a prime with $n \equiv 3 \pmod 4$. Then there are nonzero
$x, y \in \mathbb{Z}/n\mathbb{Z}$ and an integer $r \in \{2, 3\}$ such that $x + ry = 0$ and
$xy^r = 1$ in $\mathbb{Z}/n\mathbb{Z}$.

The source prints the second equation as $xy r = 1$; it is read as $xy^r = 1$, as in the proof,
whose first case computes $xy^2 = x^3/4 = 1$.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 6.

Stated but not proved: `MetaMathlibExt.exists_add_mul_eq_zero_mul_pow_eq_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#exists-add-mul-eq-zero-mul-pow-eq-one).

## $F_1$ modulo a prime $n > 3$ with $n \equiv 3 \pmod 4$ is not $m$-vanishing for $m > 0$

Let $n > 3$ be a prime with $n \equiv 3 \pmod 4$. Then for every $m > 0$ the sum-plus-product
family $F_1$ over $\mathbb{Z}/n$, $F_1(b_1, \dots, b_l) = b_1 + \dots + b_l + b_1 \cdots b_l$, is
not $m$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 7.

Stated but not proved: `MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_one_prime_three_mod_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#not-is-mvanishing-family-sum-add-mul-pro-4).

## $F_1$ modulo $8u$ with $u > 1$ is not $m$-vanishing for $m > 0$

Let $u > 1$ be a natural
number and $n = 8u$. Then for every $m > 0$ the sum-plus-product family $F_1$ over $\mathbb{Z}/n$,
$F_1(b_1, \dots, b_l) = b_1 + \dots + b_l + b_1 \cdots b_l$, is not $m$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 8.

Stated but not proved: `MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_one_eight_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#not-is-mvanishing-family-sum-add-mul-pro-5).

## $F_1$ modulo $9u$ with $u > 0$ is not $m$-vanishing for $m > 0$

Let $u > 0$ be a natural
number and $n = 9u$. Then for every $m > 0$ the sum-plus-product family $F_1$ over $\mathbb{Z}/n$,
$F_1(b_1, \dots, b_l) = b_1 + \dots + b_l + b_1 \cdots b_l$, is not $m$-vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Lemma 9.

Stated but not proved: `MetaMathlibExt.not_isMVanishingFamily_sumAddMulProd_one_nine_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#not-is-mvanishing-family-sum-add-mul-pro-6).

## The sum-minus-product family is vanishing modulo prime powers

Let $p$ be a prime,
$k > 0$ and $n = p^k$, and let $F_{-1}$ be the family over $\mathbb{Z}/n\mathbb{Z}$ sending a
block $(b_1, \dots, b_l)$ to $\sum_i b_i - \prod_i b_i$. Then $F_{-1}$ is vanishing.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Theorem 4.

Stated but not proved: `MetaMathlibExt.isVanishingFamily_sumAddMulProd_neg_one_prime_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-vanishing-family-sum-add-mul-prod-neg).

## Vanishing of families of sums of transformed entries

Let $n$ be a positive integer, $d$ a
natural number and $g_1, \dots, g_d : \mathbb{Z}/n\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ maps.
Then the family over $\mathbb{Z}/n\mathbb{Z}$ sending a block $(b_1, \dots, b_l)$ to the vector
$\left(\sum_i g_1(b_i), \dots, \sum_i g_d(b_i)\right) \in (\mathbb{Z}/n\mathbb{Z})^d$ is
vanishing, where a block counts as vanishing when all $d$ coordinates of this vector are zero.

The source assumes $d > 0$; for $d = 0$ the statement is trivial.

## Sources

- Arie Bialostocki and Vladyslav Oles, *On Generalizing the Van Der Waerden Theorem to Some Symmetric Functions*, INTEGERS 26 (2026), Article A25, Theorem 6.

Stated but not proved: `MetaMathlibExt.isVanishingFamily_transformation_sums` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Additive/VanDerWaerdenSymmetricFunctionsWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html#is-vanishing-family-transformation-sums).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zero-sum van der Waerden theorems for symmetric functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/zero-sum-van-der-waerden-theorems-for-symmetric)
