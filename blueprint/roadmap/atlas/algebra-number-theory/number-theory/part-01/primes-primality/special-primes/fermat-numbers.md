---
declaration: section
origin: cited
lean: MetaMathlibExt.IsFermatPrime, Nat.fermatNumber_mod_prime_exact_preperiod_period, MetaMathlibExt.fermatNumber_modEq_exists_repeat, MetaMathlibExt.fermatNumber_modEq_add, MetaMathlibExt.fermatNumber_not_modEq_add_of_le, MetaMathlibExt.fermatNumber_modEq_iff_preperiod_period, MetaMathlibExt.gcd_card_sub_one_exponent_eq_div_orderOf, MetaMathlibExt.exists_coprime_modEq_of_coprime
statement: formalized
---

# Fermat numbers

16 results, 2 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html).

## Fermat prime

A natural number $p$ is a Fermat prime if $p$ is prime and
$p = 2^{2^k} + 1$ for some natural number $k$, that is, $p$ is a prime Fermat number.

Formalized by `MetaMathlibExt.IsFermatPrime`, a definition declared in [MathlibExt/NumberTheory/FermatPrime.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/FermatPrime.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#is-fermat-prime).

## Preperiod and period of Fermat numbers modulo an odd prime

Let $p$ be an odd prime
and write the multiplicative order of $2$ modulo $p$ as $2^v w$ with $v, w$ natural numbers and
$w$ odd. Let $k$ be the multiplicative order of $2$ modulo $w$ (so $k = 1$ when $w = 1$), and
let $F_m = 2^{2^m} + 1$ be the $m$-th Fermat number. Then the sequence $n \mapsto F_{v+n} \bmod p$
is periodic with period $k$; for every $h < v$, the sequence $n \mapsto F_{h+n} \bmod p$ has no
positive period; and every positive period of the sequence $n \mapsto F_{v+n} \bmod p$ is
divisible by $k$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL28/Klaska/klaska22.tex>, Theorem, lines 593--606. This is the complete selected theorem statement, not a prerequisite stage.

Formalized by `Nat.fermatNumber_mod_prime_exact_preperiod_period`, a theorem declared in [MathlibExt/NumberTheory/FermatResiduePeriod.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/FermatResiduePeriod.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#fermat-number-mod-prime-exact-preperiod).

## Two of $F_0, \dots, F_p$ are congruent modulo $p$

Write $F_n = 2^{2^n} + 1$. For every
positive integer $p$ there are natural numbers $i < j \le p$ with $F_i \equiv F_j \pmod p$.

This is the pigeonhole principle; $p$ need not be prime.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 2 (`jis-2025-25.8.7-lem-2`).

Stated but not proved: `MetaMathlibExt.fermatNumber_modEq_exists_repeat` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#fermat-number-mod-eq-exists-repeat).

## Congruences between Fermat numbers propagate

Write $F_n = 2^{2^n} + 1$. Let $m$, $i$ and
$j$ be natural numbers with $F_i \equiv F_j \pmod m$. Then $F_{i+t} \equiv F_{j+t} \pmod m$ for
every natural number $t$.

No condition on $m$, $i$ or $j$ is needed.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 4 (i) (`jis-2025-25.8.7-lem-4`).

Stated but not proved: `MetaMathlibExt.fermatNumber_modEq_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#fermat-number-mod-eq-add).

## Non-congruence of Fermat numbers passes to smaller indices

Write $F_n = 2^{2^n} + 1$ for
the $n$-th Fermat number. Let $m$ be a natural number and let $i \le j$. If
$F_j \not\equiv F_{j+t} \pmod{m}$ for every $t \ge 1$, then $F_i \not\equiv F_{i+t} \pmod{m}$
for every $t \ge 1$.

The statement holds for every modulus $m$ and allows $i = j$; the paper takes $m = p$ prime and
$i < j$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 4 (ii) (`jis-2025-25.8.7-lem-4`).

Stated but not proved: `MetaMathlibExt.fermatNumber_not_modEq_add_of_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#fermat-number-not-mod-eq-add-of-le).

## Coincidences among Fermat residues

Write $F_n = 2^{2^n} + 1$. Let $p$ be a prime, and let
$h$ and $k$ be the preperiod and the period of $n \mapsto F_n \bmod p$ in the following sense:
$k > 0$, the sequence $n \mapsto F_{h+n} \bmod p$ is periodic with period $k$, every positive
period of it is a multiple of $k$, and for no $h' < h$ is the sequence $n \mapsto F_{h'+n} \bmod p$
periodic with a positive period. Then for all natural numbers $i < j$, $F_i \equiv F_j \pmod p$
if and only if $i \ge h$ and $i \equiv j \pmod k$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 6 (`jis-2025-25.8.7-lem-6`).

Stated but not proved: `MetaMathlibExt.fermatNumber_modEq_iff_preperiod_period` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#fermat-number-mod-eq-iff-preperiod-perio).

## The index of a residue and its multiplicative order

Let $p$ be a prime, let $g$ be a
primitive root modulo $p$ (an element of $\mathbb{Z}/p\mathbb{Z}$ of multiplicative order
$p - 1$), and let $a \in \mathbb{Z}/p\mathbb{Z}$. If $g^i = a$ for a natural number $i$, then
$\gcd(p - 1, i) = (p - 1)/\operatorname{ord}_p(a)$, where $\operatorname{ord}_p(a)$ is the
multiplicative order of $a$ modulo $p$.

This holds for every natural number $i$ with $g^i = a$; the paper's index
$\operatorname{ind}_g(a)$, which lies between $1$ and $p - 1$, is one of them.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 8 (iv) (`jis-2025-25.8.7-lem-8`).

Stated but not proved: `MetaMathlibExt.gcd_card_sub_one_exponent_eq_div_orderOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#gcd-card-sub-one-exponent-eq-div-order-o).

## Coprime representatives of a residue class

Let $\alpha$, $\beta$ and $\gamma$ be natural
numbers with $\gamma > 0$ and $\gcd(\alpha, \beta) = 1$. Then there is a natural number $c > 0$
with $\gcd(c, \gamma) = 1$ and $c \equiv \beta \pmod{\alpha}$.

The numbers $\alpha$ and $\beta$ need not be positive.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 10 (`jis-2025-25.8.7-lem-10`).

Stated but not proved: `MetaMathlibExt.exists_coprime_modEq_of_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#exists-coprime-mod-eq-of-coprime).

## A primitive root in which a residue has index $(p-1)/\operatorname{ord}_p(a)$

Let $p$ be
a prime and let $a$ be a nonzero residue modulo $p$, of multiplicative order
$\operatorname{ord}_p(a)$. Then there is a primitive root $g$ modulo $p$ (an element of order
$p - 1$ in $\mathbb{Z}/p\mathbb{Z}$) with $g^{(p-1)/\operatorname{ord}_p(a)} = a$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Proposition 11 (`jis-2025-25.8.7-prop-11`).

Stated but not proved: `MetaMathlibExt.exists_primitiveRoot_pow_card_sub_one_div_orderOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#exists-primitive-root-pow-card-sub-one-d).

## Indices dividing $p - 1$

Let $p$ be a prime, let $g$ be a primitive root modulo $p$ (an
element of order $p - 1$ in $\mathbb{Z}/p\mathbb{Z}$), let $a \in \mathbb{Z}/p\mathbb{Z}$ and let
$i$ be a natural number with $g^i = a$. Then $i$ divides $p - 1$ if and only if
$i = (p - 1)/\operatorname{ord}_p(a)$, where $\operatorname{ord}_p(a)$ is the multiplicative order
of $a$.

For $i$ outside $\{1, \dots, p - 1\}$ both sides are false, so the statement concerns the index
$\operatorname{ind}_g(a)$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Proposition 13 (`jis-2025-25.8.7-prop-13`).

Stated but not proved: `MetaMathlibExt.exponent_dvd_card_sub_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#exponent-dvd-card-sub-one-iff).

## Uniqueness of the $2$-adic decomposition of the index of $2$

Let $p$ be an odd prime and
write $p - 1 = 2^r u$ with $u$ odd. Then there is exactly one pair $(s, t)$ of natural numbers
with $s \le r$ and $t \mid u$ such that $g^{2^s t} = 2$ for some primitive root $g$ modulo $p$
(an element of order $p - 1$ in $\mathbb{Z}/p\mathbb{Z}$).

Since $2^s t$ divides $p - 1$, it lies in $\{1, \dots, p - 1\}$, so it is the index
$\operatorname{ind}_g(2)$ of $2$ with respect to $g$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Corollary 14 (`jis-2025-25.8.7-cor-14`); also Theorem 15 (i).

Stated but not proved: `MetaMathlibExt.existsUnique_twoAdic_index_of_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#exists-unique-two-adic-index-of-two).

## Preperiod and period of Fermat residues from the index of $2$

Write $F_n = 2^{2^n} + 1$.
Let $p$ be an odd prime, write $p - 1 = 2^r u$ with $u$ odd, and let $s \le r$ and $t \mid u$ be
natural numbers such that $g^{2^s t} = 2$ for some primitive root $g$ modulo $p$ (an element of
order $p - 1$ in $\mathbb{Z}/p\mathbb{Z}$). Let $k$ be the multiplicative order of $2$ modulo
$u/t$, with $k = 1$ when $t = u$. Then the sequence $n \mapsto F_{r-s+n} \bmod p$ is periodic
with period $k$, every positive period of it is a multiple of $k$, and for no $h < r - s$ is the
sequence $n \mapsto F_{h+n} \bmod p$ periodic with a positive period. Thus $n \mapsto F_n \bmod p$
has preperiod $r - s$ and primitive period $k$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Theorem 15 (ii) and (iii) (`jis-2025-25.8.7-thm-15`).

Stated but not proved: `MetaMathlibExt.fermatNumber_mod_prime_preperiod_period_of_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#fermat-number-mod-prime-preperiod-period).

## Prime divisors of Fermat numbers and the order of $2$

Write $F_n = 2^{2^n} + 1$ for the
$n$-th Fermat number. An odd prime $p$ divides $F_n$ if and only if the multiplicative order of
$2$ modulo $p$ equals $2^{n+1}$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Lemma 17 (`jis-2025-25.8.7-lem-17`).

Stated but not proved: `MetaMathlibExt.prime_dvd_fermatNumber_iff_orderOf_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#prime-dvd-fermat-number-iff-order-of-two).

## Prime divisors of Fermat numbers and the period of Fermat residues

Write
$F_n = 2^{2^n} + 1$ for the $n$-th Fermat number. Let $p$ be an odd prime, let $h$ be a natural
number and let $k$ be a positive integer such that the sequence $n \mapsto F_{h+n} \bmod p$ is
periodic with period $k$ and every positive period of it is a multiple of $k$. Then $p$ divides
$F_n$ for some natural number $n$ if and only if $k = 1$.

Any such $h$ is at least the preperiod of $n \mapsto F_n \bmod p$, and $k$ is then the primitive
period of $n \mapsto F_n \bmod p$, which does not depend on $h$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Proposition 18 (`jis-2025-25.8.7-prop-18`).

Stated but not proved: `MetaMathlibExt.exists_prime_dvd_fermatNumber_iff_period_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#exists-prime-dvd-fermat-number-iff-perio).

## The power of $2$ dividing the order of $2$ modulo a prime

Let $p$ be a prime and let
$\operatorname{ord}_p(2)$ be the multiplicative order of $2$ modulo $p$. If $p \equiv 7 \pmod 8$,
then $\operatorname{ord}_p(2)$ is odd. If $p \equiv 3 \pmod 8$, then $\operatorname{ord}_p(2)$ is
divisible by $2$ but not by $4$. If $p \equiv 5 \pmod 8$, then $\operatorname{ord}_p(2)$ is
divisible by $4$ but not by $8$.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Theorem 22, order statements (`jis-2025-25.8.7-thm-22`).

Stated but not proved: `MetaMathlibExt.orderOf_two_twoAdic_of_mod_eight` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#order-of-two-two-adic-of-mod-eight).

## Every preperiod of Fermat residues occurs for a prime $p \equiv 1 \pmod 8$

Write
$F_n = 2^{2^n} + 1$. For every natural number $v$ there is a prime $p \equiv 1 \pmod 8$ such that
the sequence $n \mapsto F_n \bmod p$ has preperiod exactly $v$: the sequence
$n \mapsto F_{v+n} \bmod p$ is periodic with some positive period, and for no $h < v$ is the
sequence $n \mapsto F_{h+n} \bmod p$ periodic with a positive period.

## Sources

- Jiří Klaška, *Fermat Numbers Modulo a Prime*, Journal of Integer Sequences 28 (2025), Article 25.8.7, Theorem 23 (`jis-2025-25.8.7-thm-23`).

Stated but not proved: `MetaMathlibExt.exists_prime_one_mod_eight_fermat_preperiod` is written with `theorem_wanted` in [WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FermatNumbersModPrimeWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html#exists-prime-one-mod-eight-fermat-preper).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fermat numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/special-primes/fermat-numbers)
