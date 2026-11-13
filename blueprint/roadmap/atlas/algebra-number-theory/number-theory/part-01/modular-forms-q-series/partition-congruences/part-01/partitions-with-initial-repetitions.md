---
declaration: section
origin: cited
lean: MetaMathlibExt.isSquare_mod_two_pow_odd_not_even_iff, MetaMathlibExt.isSquare_mod_two_pow_even_not_odd_iff, MetaMathlibExt.card_not_isSquare_sixteen_mul_add_one_eight_mul_add_one, MetaMathlibExt.card_not_isSquare_twelve_mul_add_one_eight_mul_add_one, MetaMathlibExt.four_mul_card_legendreSym_pair_eq_neg_one, MetaMathlibExt.card_initialRepetitions_eq_card_not_dvd_eq_card_count_le, MetaMathlibExt.initialRepetitionsC2, MetaMathlibExt.initialRepetitionsC3
statement: formalized
---

# Partitions with initial repetitions

24 results, 5 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html).

## Residues that are squares modulo $2^{2k-1}$ but not modulo $2^{2k}$

Let $k \ge 0$ and let
$x$ be an integer with $0 \le x < 2^{2k}$, where the exponents $2k - 1$ and $2k - 2$ are truncated
at $0$. Then $x$ is a square modulo $2^{2k-1}$ but not a square modulo $2^{2k}$ if and only if
$x = 2^{2k-1}$ or $x = 2^{2k-1} + 2^{2k-2}$.

For $k \ge 1$ these are exactly two residues; for $k = 0$ both sides of the equivalence are false.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Lemma 2.

Stated but not proved: `MetaMathlibExt.isSquare_mod_two_pow_odd_not_even_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#is-square-mod-two-pow-odd-not-even-iff).

## Residues that are squares modulo $2^{2k}$ but not modulo $2^{2k+1}$

Let $k \ge 0$ and let
$x$ be an integer with $0 \le x < 2^{2k+1}$, where the exponent $2k - 2$ is truncated at $0$. Then
$x$ is a square modulo $2^{2k}$ but not a square modulo $2^{2k+1}$ if and only if
$x = 2^{2k} + 2^{2k-2}$.

For $k \ge 1$ this is the unique such residue; for $k = 0$ both sides of the equivalence are false.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Lemma 3.

Stated but not proved: `MetaMathlibExt.isSquare_mod_two_pow_even_not_odd_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#is-square-mod-two-pow-even-not-odd-iff).

## Residues $r$ with $16r + 1$ and $8r + 1$ both non-squares modulo $p$

For every prime $p$,
the number of integers $r$ with $1 \le r \le p - 1$ such that neither $16r + 1$ nor $8r + 1$ is a
square modulo $p$ equals $\lfloor p/4 \rfloor$.

Here $0$ counts as a square modulo $p$, so "not a square" means "quadratic nonresidue". The paper
assumes $p \ge 5$; for $p = 2$ and $p = 3$ both sides are $0$. If $0$ were counted as a non-square,
the count at $p = 5$ would be $2$ instead of $1$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 5.

Stated but not proved: `MetaMathlibExt.card_not_isSquare_sixteen_mul_add_one_eight_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#card-not-is-square-sixteen-mul-add-one-e).

## Residues $r$ with $12r + 1$ and $8r + 1$ both non-squares modulo $p$

For every prime $p$,
let $N$ be the number of integers $r$ with $1 \le r \le p - 1$ such that neither $12r + 1$ nor
$8r + 1$ is a square modulo $p$. Then $N = \lfloor p/4 \rfloor - 1$ if $p \equiv 5 \pmod{24}$,
$N = \lfloor p/4 \rfloor + 1$ if $p \equiv 11 \pmod{24}$, and $N = \lfloor p/4 \rfloor$ otherwise.

Here $0$ counts as a square modulo $p$, so "not a square" means "quadratic nonresidue". The paper
assumes $p \ge 5$; for $p = 2$ and $p = 3$ both sides are $0$. If $0$ were counted as a non-square,
the count at $p = 5$ would be $2$ instead of $0$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 8.

Stated but not proved: `MetaMathlibExt.card_not_isSquare_twelve_mul_add_one_eight_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#card-not-is-square-twelve-mul-add-one-ei).

## Counting $r$ with $mr + 1$ and $nr + 1$ both quadratic nonresidues

Let $p$ be an odd
prime, write $\left(\frac{a}{p}\right)$ for the Legendre symbol of an integer $a$, and let $m$ and
$n$ be integers with $p \nmid mn(n - m)$. If $N$ is the number of integers $r$ with
$0 \le r \le p - 1$ such that $\left(\frac{mr+1}{p}\right) = \left(\frac{nr+1}{p}\right) = -1$, then

$$4N = 4\left\lfloor \frac{p}{4} \right\rfloor -
\left(\left(\frac{m}{p}\right) - \left(\frac{n-m}{p}\right)\right)
\left(\left(\frac{n}{p}\right) - \left(\frac{m-n}{p}\right)\right).$$

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Lemma 1.

Stated but not proved: `MetaMathlibExt.four_mul_card_legendreSym_pair_eq_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#four-mul-card-legendre-sym-pair-eq-neg-o).

## Andrews' theorem on partitions with initial repetitions

Let $k \ge 1$ and $n \ge 0$ be
integers. Say that a partition has initial $k$-repetitions if, whenever a part $j$ appears at
least $k$ times, every integer $i$ with $1 \le i < j$ appears at least $k$ times. Then the number
of partitions of $n$ with initial $k$-repetitions equals the number of partitions of $n$ into parts
not divisible by $2k$, and this number equals the number of partitions of $n$ in which no part
appears more than $2k - 1$ times.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 1, quoting Andrews.

Stated but not proved: `MetaMathlibExt.card_initialRepetitions_eq_card_not_dvd_eq_card_count_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#card-initial-repetitions-eq-card-not-dvd).

## The partition function $c_2$ of Nyirenda and Mugwangwavari

For an integer $n \ge 0$,
$c_2(n)$ is the number of partitions of $n$ for which there is an integer $j$ with
$1 \le j \le n$ such that $j$ appears exactly $j$ times, every part other than $j$ is at least
$2j + 1$, and every even part that is at least $2j + 2$ appears only once.

Odd parts that are at least $2j + 1$ may appear any number of times.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Section 3 (definition of `c₂`, from Nyirenda and Mugwangwavari).

Formalized by `MetaMathlibExt.initialRepetitionsC2`, a definition declared in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c2).

## The initial-repetitions partition function $c_3$

For $n \ge 0$, $c_3(n)$ is the number
of partitions of $n$ for which there is an integer $j$ with $1 \le j \le n$ such that the part $1$
appears exactly $j^2$ or $j^2 + 1$ times, every odd part larger than $1$ appears exactly once,
every even part appears exactly once, and every even part greater than $2j$ is at least $4j + 4$
and divisible by $4$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Section 3 (definition of `c₃`, from Nyirenda and Mugwangwavari).

Formalized by `MetaMathlibExt.initialRepetitionsC3`, a definition declared in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c3).

## The partition function $c_8$

For $n \ge 0$, $c_8(n)$ is the number of partitions of $n$
such that either (a) all parts are even and distinct, or (b) for some positive integer $j$, the
largest odd part is $2j - 1$, every positive odd integer $i \le j$ appears once or twice, every
odd integer $i$ with $j < i \le 2j - 1$ appears exactly once, all even parts are distinct, and
every even part greater than $j$ is at least $2j + 2$.

For $j = 1$ the paper's clauses "the largest odd part $2j - 1$ appears once" and "odd integers
$\le j$ appear once or twice" conflict; the second governs, as in the generating function
$(q^2;q^2)_\infty \sum_n q^{n^2}/(q;q)_n$ the paper uses (the other reading gives $c_8(2) = 1$,
contradicting Theorem 11 of the paper since $31$ is not a square).

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Section 3 (definition of `c₈`, from Nyirenda and Mugwangwavari).

Formalized by `MetaMathlibExt.initialRepetitionsC8`, a definition declared in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8).

## The initial-repetitions partition function $c_8'$

For $n \ge 0$, $c_8'(n)$ is the number
of partitions of $n$ into distinct even parts plus the sum, over $m = 1, \dots, n$, of the number
of partitions of $n$ in which every even number $2i$ with $1 \le i \le m$ is a part, every even
part at most $m$ appears at most twice, every odd part at most $m$ appears exactly once, and every
part greater than $m$ is even and appears exactly once.

Equivalently, $c_8'(n)$ counts partitions of $n$ with a possibly distinguished part: either all
parts are even and distinct and no part is distinguished, or a part $2m$ is distinguished and the
conditions above hold for $m$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Section 4 (definition of `c₈'`).

Formalized by `MetaMathlibExt.initialRepetitionsC8Prime`, a definition declared in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-prime).

## Small values of the partition functions $c_2$, $c_3$, $c_8$ and $c_8'$

We have
$c_2(0) = 0$, $c_2(1) = 1$, $c_3(1) = 1$, $c_8(0) = c_8(1) = 1$, $c_8'(0) = 1$ and $c_8'(1) = 0$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Sections 3 and 4 (definitions of `c₂`, `c₃`, `c₈`, `c₈'`).

Formalized by `MetaMathlibExt.initialRepetitions_values_zero_one`, a theorem declared in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-values-zero-one).

## Parity of $c_2(5n + 2)$

Let $c_2(m)$ be the number of partitions of $m$ for which there
is an integer $j$ with $1 \le j \le m$ such that $j$ appears exactly $j$ times, every part other
than $j$ is at least $2j + 1$, and every even part that is at least $2j + 2$ appears only once.
Nyirenda and Mugwangwavari: for every integer $n \ge 0$, the number $c_2(5n + 2)$ is even.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 3.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC2_five_mul_add_two_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c2-five-mul-add-two).

## Parity of $c_2(pn + r)$ for primes $p \ge 5$

Let $c_2(m)$ be the number of partitions of
$m$ for which there is an integer $j$ with $1 \le j \le m$ such that $j$ appears exactly $j$
times, every part other than $j$ is at least $2j + 1$, and every even part that is at least
$2j + 2$ appears only once. Let $p \ge 5$ be a prime and let $r$ be an integer with
$1 \le r \le p - 1$ such that neither $16r + 1$ nor $8r + 1$ is a square modulo $p$. Then
$c_2(pn + r)$ is even for every integer $n \ge 0$.

Here $0$ counts as a square modulo $p$, so the hypothesis says that $16r + 1$ and $8r + 1$ are
quadratic nonresidues modulo $p$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 4.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC2_prime_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c2-prime-mul-add-eve).

## Parity of $c_3(11n + 5)$, $c_3(11n + 7)$ and $c_3(11n + 9)$

Let $c_3(m)$ be the number
of partitions of $m$ for which there is an integer $j$ with $1 \le j \le m$ such that the part $1$
appears exactly $j^2$ or $j^2 + 1$ times, the odd parts greater than $1$ are distinct, the even
parts are distinct, and every even part greater than $2j$ is divisible by $4$ and at least
$4j + 4$. Nyirenda and Mugwangwavari: for every integer $n \ge 0$, the numbers $c_3(11n + 5)$,
$c_3(11n + 7)$ and $c_3(11n + 9)$ are all even.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 6.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC3_eleven_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c3-eleven-mul-add-ev).

## Parity of $c_3$ on residue classes modulo a prime

Let $c_3$ be the initial-repetitions
partition function of Nyirenda and Mugwangwavari. Let $p \ge 5$ be a prime and let $r$ be an
integer with $1 \le r \le p - 1$ such that neither $12r + 1$ nor $8r + 1$ is a square modulo $p$.
Then $c_3(pn + r)$ is even for every integer $n \ge 0$.

Here $x$ is a square modulo $p$ when $x \equiv y^2 \pmod{p}$ for some integer $y$, so multiples
of $p$ count as squares.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 7.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC3_prime_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c3-prime-mul-add-eve).

## $c_8$ is even on six residue classes modulo $49$

Let $c_8$ be the initial-repetitions
partition function of Nyirenda and Mugwangwavari. For every integer $n \ge 0$ and every
$r \in \{6, 20, 27, 34, 41, 48\}$, the number $c_8(49n + r)$ is even.

This result is due to Nyirenda and Mugwangwavari.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 9.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8_fortyNine_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-forty-nine-mul-ad).

## Andrews' identity for the first Rogers–Ramanujan series

Let $q$ be a complex number with
$|q| < 1$, write $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$ for $j \ge 0$, and let
$(q^2;q^2)_\infty = \prod_{n=0}^{\infty} (1 - q^{2n+2})$ be the infinite q-Pochhammer symbol. Then

$$(q^2;q^2)_\infty \sum_{j=0}^{\infty} \frac{q^{j^2}}{(q;q)_j} = \sum_{\lambda \in \mathbb{Z}}
\left(q^{60\lambda^2+4\lambda} - q^{60\lambda^2+44\lambda+8} + q^{60\lambda^2+16\lambda+1} -
q^{60\lambda^2+64\lambda+17}\right).$$

All exponents on the right are nonnegative for integer $\lambda$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 10, quoting Andrews.

Stated but not proved: `MetaMathlibExt.andrews_rogersRamanujan_first_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#andrews-rogers-ramanujan-first-dissectio).

## $c_8(N)$ is even when $15N + 1$ is not a square

Let $c_8$ be the initial-repetitions
partition function of Nyirenda and Mugwangwavari. For every integer $N \ge 0$ such that $15N + 1$
is not a perfect square, $c_8(N)$ is even.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 11.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8_even_of_not_isSquare` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-even-of-not-is-sq).

## Andrews' identity for the second Rogers–Ramanujan series

Let $q$ be a complex number
with $|q| < 1$, write $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$ for $j \ge 0$, and let
$(q^2;q^2)_\infty = \prod_{n=0}^{\infty} (1 - q^{2n+2})$ be the infinite q-Pochhammer symbol. Then

$$(q^2;q^2)_\infty \sum_{j=0}^{\infty} \frac{q^{j^2+j}}{(q;q)_j} = \sum_{\lambda \in \mathbb{Z}}
\left(q^{60\lambda^2+8\lambda} - q^{60\lambda^2+32\lambda+4} + q^{60\lambda^2+28\lambda+3} -
q^{60\lambda^2+52\lambda+11}\right).$$

All exponents on the right are nonnegative for integer $\lambda$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 12, quoting Andrews.

Stated but not proved: `MetaMathlibExt.andrews_rogersRamanujan_second_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#andrews-rogers-ramanujan-second-dissecti).

## $c_8'(N)$ is even when $15N + 4$ is not a square

Let $c_8'$ be the partition function
that counts partitions with a possibly distinguished part. For every integer $N \ge 0$ such that
$15N + 4$ is not a perfect square, $c_8'(N)$ is even.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Theorem 13.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8Prime_even_of_not_isSquare` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-prime-even-of-not).

## Parity of $c_8$ on residue classes modulo powers of $2$

Let $c_8$ be the
initial-repetitions partition function of Nyirenda and Mugwangwavari, and let $k \ge 1$,
$n \ge 0$ and $r \ge 0$ be integers. If $r < 2^{2k}$ and $15r \equiv 2^{2k-1} - 1 \pmod{2^{2k}}$,
then $c_8(2^{2k} n + r)$ is even. If $r < 2^{2k}$ and
$15r \equiv 2^{2k-1} + 2^{2k-2} - 1 \pmod{2^{2k}}$, then $c_8(2^{2k} n + r)$ is even. If
$r < 2^{2k+1}$ and $15r \equiv 2^{2k} + 2^{2k-2} - 1 \pmod{2^{2k+1}}$, then
$c_8(2^{2k+1} n + r)$ is even.

These $r$ are the paper's least nonnegative residues $r_{k,1}$, $r_{k,2}$, $r_{k,3}$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Corollary 1.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8_two_pow_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-two-pow-mul-add-e).

## Parity of $c_8$ on residue classes modulo a prime

Let $c_8$ be the initial-repetitions
partition function of Nyirenda and Mugwangwavari. Let $p \ge 7$ be a prime and let $r$ be an
integer with $1 \le r \le p - 1$ such that $15r + 1$ is not a square modulo $p$. Then
$c_8(pn + r)$ is even for every integer $n \ge 0$.

Here $x$ is a square modulo $p$ when $x \equiv y^2 \pmod{p}$ for some integer $y$, so multiples
of $p$ count as squares.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Corollary 2.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8_prime_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-prime-mul-add-eve).

## Parity of $c_8'$ on residue classes modulo powers of $2$

Let $c_8'$ be the partition
function that counts partitions with a possibly distinguished part, and let $k \ge 1$, $n \ge 0$
and $r \ge 0$ be integers. If $r < 2^{2k}$ and $15r \equiv 2^{2k-1} - 4 \pmod{2^{2k}}$, then
$c_8'(2^{2k} n + r)$ is even. If $r < 2^{2k}$ and
$15r \equiv 2^{2k-1} + 2^{2k-2} - 4 \pmod{2^{2k}}$, then $c_8'(2^{2k} n + r)$ is even. If
$r < 2^{2k+1}$ and $15r \equiv 2^{2k} + 2^{2k-2} - 4 \pmod{2^{2k+1}}$, then
$c_8'(2^{2k+1} n + r)$ is even.

These $r$ are the paper's least nonnegative residues $r'_{k,1}$, $r'_{k,2}$, $r'_{k,3}$.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Corollary 3.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8Prime_two_pow_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-prime-two-pow-mul).

## Parity of $c_8'$ on residue classes modulo a prime

Let $c_8'$ be the partition function
that counts partitions with a possibly distinguished part. Let $p \ge 7$ be a prime and let $r$ be
an integer with $1 \le r \le p - 1$ such that $15r + 4$ is not a square modulo $p$. Then
$c_8'(pn + r)$ is even for every integer $n \ge 0$.

Here $x$ is a square modulo $p$ when $x \equiv y^2 \pmod{p}$ for some integer $y$, so multiples
of $p$ count as squares.

## Sources

- John Greene and James A. Sellers, *Extending Recent Parity Results of Nyirenda and Mugwangwavari for Partitions with Initial Repetitions*, INTEGERS 25 (2025), Article A32, Corollary 4.

Stated but not proved: `MetaMathlibExt.initialRepetitionsC8Prime_prime_mul_add_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GreeneSellersInitialRepetitionsWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html#initial-repetitions-c8-prime-prime-mul-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partitions with initial repetitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/partitions-with-initial-repetitions)
