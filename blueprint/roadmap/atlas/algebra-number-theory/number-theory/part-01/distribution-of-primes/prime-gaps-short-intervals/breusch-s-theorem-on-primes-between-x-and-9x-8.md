---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.BreuschWanted.Internal.Q9, MathlibExt.NumberTheory.BreuschWanted.Internal.w9, MathlibExt.NumberTheory.BreuschWanted.Internal.w9_length, MathlibExt.NumberTheory.BreuschWanted.Internal.w9_complete, MathlibExt.NumberTheory.BreuschWanted.Internal.w9_pos, MathlibExt.NumberTheory.BreuschWanted.Internal.w9_dvd, MathlibExt.NumberTheory.BreuschWanted.Internal.G9term, MathlibExt.NumberTheory.BreuschWanted.Internal.G9
statement: formalized
proof: formalized
---

# Breusch's theorem on primes between x and 9x/8

182 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/index.html).

## The modulus $Q_9 = 210$

For the $k = 9$ case of Breusch's argument, the truncation
modulus is the natural number $Q_9 = 2 \cdot 3 \cdot 5 \cdot 7 = 210$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Q9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#q9).

## The Möbius divisor table for $210$

$W_9$ is the list of pairs of a natural number and an
integer
$(1, 1), (2, -1), (3, -1), (5, -1), (6, 1), (7, -1), (10, 1), (14, 1), (15, 1), (21, 1),$
$(30, -1), (35, 1), (42, -1), (70, -1), (105, -1), (210, 1)$,
in this order. It pairs each divisor $d$ of $210$ with its Möbius value $\mu(d)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#w9).

## The divisor table for $210$ has 16 entries

The Möbius divisor table $W_9$ for $210$ is a
list of length $16$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_length`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#w9-length).

## The divisor table for $210$ lists every divisor

The set of first components $d$ of the
pairs $(d, \varepsilon)$ in the Möbius divisor table $W_9$ is exactly the set of divisors of
$Q_9 = 210$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_complete`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#w9-complete).

## Divisors in the table for $210$ are positive

For every pair $(d, \varepsilon)$ in the
Möbius divisor table $W_9$ for $210$, $d \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#w9-pos).

## Entries of the divisor table for $210$ divide $210$

For every pair $(d, \varepsilon)$ in
the Möbius divisor table $W_9$, $d$ divides $Q_9 = 210$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_dvd`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#w9-dvd).

## Summand of the Breusch grid function

For a natural number $d$, an integer $m$ and a
natural number $j$, the summand of the pair $(d, m)$ at $j$ is the integer

$$
m \Bigl( \Bigl\lfloor \frac{10 \cdot 210 \cdot j}{18900\, d} \Bigr\rfloor -
\Bigl\lfloor \frac{9 \cdot 210 \cdot j}{18900\, d} \Bigr\rfloor -
\Bigl\lfloor \frac{210 \cdot j}{18900\, d} \Bigr\rfloor \Bigr),
$$

where each floor is a quotient in natural-number division (equal to $0$ when $d = 0$) and the
differences are taken in the integers.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9term`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#g9term).

## Breusch grid function for $k = 9$

For a natural number $j$, $G_9(j)$ is the integer

$$
G_9(j) = \sum_{d \mid 210} \mu(d) \Bigl(
\Bigl\lfloor \frac{10 \cdot 210 \cdot j}{18900\, d} \Bigr\rfloor -
\Bigl\lfloor \frac{9 \cdot 210 \cdot j}{18900\, d} \Bigr\rfloor -
\Bigl\lfloor \frac{210 \cdot j}{18900\, d} \Bigr\rfloor \Bigr),
$$

where $\mu$ is the Möbius function, the sum runs over the $16$ positive divisors $d$ of
$210 = 2 \cdot 3 \cdot 5 \cdot 7$, each floor is a quotient of natural numbers, and the
differences are taken in the integers.

The sum runs over an explicit table of the divisors of $210$ with their Möbius values.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#g9).

## Grid bound $G_9 \le 3$ for $0 \le j < 2700$

For every natural number $k < 2700$,
the grid function satisfies $G_9(0 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j < 2700$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block0`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block0).

## Grid bound $G_9 \le 3$ for $2700 \le j < 5400$

For every natural number $k < 2700$,
the grid function satisfies $G_9(2700 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j$ with $2700 \le j < 5400$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block1`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block1).

## Grid bound $G_9 \le 3$ for $5400 \le j < 8100$

For every natural number $k < 2700$,
the grid function satisfies $G_9(5400 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j$ with $5400 \le j < 8100$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block2`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block2).

## Grid bound $G_9 \le 3$ for $8100 \le j < 10800$

For every natural number $k < 2700$,
the grid function satisfies $G_9(8100 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j$ with $8100 \le j < 10800$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block3`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block3).

## Grid bound $G_9 \le 3$ for $10800 \le j < 13500$

For every natural number $k < 2700$,
the grid function satisfies $G_9(10800 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j$ with $10800 \le j < 13500$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block4`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block4).

## Grid bound $G_9 \le 3$ for $13500 \le j < 16200$

For every natural number $k < 2700$,
the grid function satisfies $G_9(13500 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j$ with $13500 \le j < 16200$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block5`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block5).

## Grid bound $G_9 \le 3$ for $16200 \le j < 18900$

For every natural number $k < 2700$,
the grid function satisfies $G_9(16200 + k) \le 3$; that is, $G_9(j) \le 3$ for all natural
numbers $j$ with $16200 \le j < 18900$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_block6`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-block6).

## Grid bound $G_9 \le 3$

For every natural number $j < 18900$, the grid function satisfies
$G_9(j) \le 3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M9_le`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#m9-le).

## The grid function reaches $1$ at $279$

The Breusch grid function $G_9$ for $k = 9$
satisfies $G_9(279) \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin1_attained`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#jmin1-attained).

## The grid function stays below $1$ on $(10, 279)$

For every natural number $j$ with
$10 \le j < 279$, the Breusch grid function $G_9$ for $k = 9$ satisfies $G_9(j) < 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin1_core`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#jmin1-core).

## First index from $10$ where the grid function reaches $1$

The Breusch grid function
$G_9$ for $k = 9$ satisfies $G_9(279) \ge 1$, and $G_9(j) < 1$ for every natural number $j$ with
$10 \le j < 279$. So $279$ is the least $j \ge 10$ with $G_9(j) \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin1`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#jmin1).

## The grid function reaches $2$ at $657$

The Breusch grid function $G_9$ for $k = 9$
satisfies $G_9(657) \ge 2$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin2_attained`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-01/index.html#jmin2-attained).

## The grid function stays below $2$ on $(10, 657)$

For every natural number $j$ with
$10 \le j < 657$, the Breusch grid function $G_9$ for $k = 9$ satisfies $G_9(j) < 2$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin2_core`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#jmin2-core).

## First index from $10$ where the grid function reaches $2$

The Breusch grid function
$G_9$ for $k = 9$ satisfies $G_9(657) \ge 2$, and $G_9(j) < 2$ for every natural number $j$ with
$10 \le j < 657$. So $657$ is the least $j \ge 10$ with $G_9(j) \ge 2$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin2`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#jmin2).

## The grid function reaches $3$ at $963$

The Breusch grid function $G_9$ for $k = 9$
satisfies $G_9(963) \ge 3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin3_attained`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#jmin3-attained).

## The grid function stays below $3$ on $(10, 963)$

For every natural number $j$ with
$10 \le j < 963$, the Breusch grid function $G_9$ for $k = 9$ satisfies $G_9(j) < 3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin3_core`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#jmin3-core).

## First index from 10 on with grid value at least 3

The grid function $G_9$ satisfies
$G_9(963) \ge 3$, and $G_9(j) < 3$ for every natural number $j$ with $10 \le j < 963$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.jmin3`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#jmin3).

## Signs in the divisor table for $210$

For every pair $(d, \varepsilon)$ in the Möbius
divisor table $W_9$ for $210$, $\varepsilon = 1$ or $\varepsilon = -1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_mu_sign`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#w9-mu-sign).

## The divisor table for $210$ has no repeated entries

No pair $(d, \varepsilon)$ occurs more
than once in the list $W_9$, the Möbius divisor table for $210$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_nodup`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#w9-nodup).

## Sum over a duplicate-free list

Let $M$ be an additive commutative monoid, let $l$ be
a list of elements of $\mathbb{N} \times \mathbb{Z}$ with no repeated entries, and let
$f : \mathbb{N} \times \mathbb{Z} \to M$. Then the sum of the values of $f$ along $l$ equals
the sum of $f$ over the finite set of entries of $l$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.map_sum_toFinset`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Grid.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#map-sum-to-finset).

## Exponential bound by the geometric series

For every real number $u$ with $0 \le u < 1$,
$e^u \le \frac{1}{1 - u}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.exp_le_inv_one_sub`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#exp-le-inv-one-sub).

## Logarithm is at least 1 − 1/t

For every real number $t \ge 1$, $1 - 1/t \le \log t$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.one_sub_inv_le_log`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#one-sub-inv-le-log).

## Weak Stirling lower bound for factorials

For every natural number $n \ge 1$,
$n^n e^{1-n} \le n!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.stirling_lower`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#stirling-lower).

## Weak Stirling upper bound for factorials

For every natural number $n \ge 1$,
$n! \le n^{n+1} e^{1-n}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.stirling_upper`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#stirling-upper).

## Scaled factorial argument $N_{10}$

Let $Q_9 = 2 \cdot 3 \cdot 5 \cdot 7 = 210$. For
natural numbers $m$ and $n$, $N_{10}(m, n)$ is the natural number $10 n \lfloor Q_9 / m \rfloor$,
where $\lfloor Q_9 / 0 \rfloor$ is taken to be $0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N10m`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#n10m).

## Scaled factorial argument N₉

For natural numbers $m$ and $n$,
$N_9(m, n) = 9n \lfloor Q_9 / m \rfloor$, where $Q_9 = 210$ and $\lfloor Q_9 / m \rfloor$ is the
quotient of natural-number division, taken to be $0$ when $m = 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N9m`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#n9m).

## Scaled factorial argument $N_1$

Let $Q_9 = 2 \cdot 3 \cdot 5 \cdot 7 = 210$. For natural
numbers $m$ and $n$, $N_1(m, n)$ is the natural number $n \lfloor Q_9 / m \rfloor$, where
$\lfloor Q_9 / 0 \rfloor$ is taken to be $0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N1m`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#n1m).

## Binomial factor ratio₉

For natural numbers $m$ and $n$,
$\mathrm{ratio}_9(m, n) = N_{10}(m, n)! / (N_9(m, n)! \cdot N_1(m, n)!)$, with natural-number
division, where $N_k(m, n) = kn \lfloor Q_9 / m \rfloor$ for $k = 1, 9, 10$ and $Q_9 = 210$
(the quotient $\lfloor Q_9 / m \rfloor$ is taken to be $0$ when $m = 0$).

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.ratio9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#ratio9).

## Logarithm of Breusch's product $F_9(n)$

Let $w_9$ be the table of divisors $d$ of
$Q_9 = 210$ paired with their Möbius values $\varepsilon$. For a natural number $n$, writing
$k_d = 210/d$,

$$\log F_9(n) = \sum_{(d, \varepsilon) \in w_9}
\varepsilon \log \frac{(10 n k_d)!}{(9 n k_d)!\,(n k_d)!}.$$

This is the logarithm of the Möbius-weighted product $F_9(n)$ in Breusch's argument.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.logF9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#log-f9).

## Q₉ is positive

The truncation modulus $Q_9$ of the $k = 9$ case satisfies $0 < Q_9$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Q9_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#q9-pos).

## Value of Q₉

The truncation modulus $Q_9 = 2 \cdot 3 \cdot 5 \cdot 7$ of the $k = 9$ case
equals $210$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Q9_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#q9-eq).

## Quotients of Q₉ by its divisors are positive

For every natural number $m \ge 1$ dividing
$Q_9 = 210$, the quotient $Q_9 / m$ is at least $1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Q9div_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-02/index.html#q9div-pos).

## Positivity of the scaled factorial argument $N_{10}$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_{10}(m, n) = 10 n \lfloor Q_9 / m \rfloor$. If $n \ge 1$, $m \ge 1$
and $m$ divides $Q_9$, then $N_{10}(m, n) \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N10_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n10-pos).

## Positivity of the scaled argument N₉

For natural numbers $m$ and $n$ with $n \ge 1$,
$m \ge 1$ and $m$ dividing $Q_9 = 210$, the scaled factorial argument
$N_9(m, n) = 9n \lfloor Q_9 / m \rfloor$ satisfies $N_9(m, n) \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N9_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n9-pos).

## Positivity of the scaled factorial argument $N_1$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_1(m, n) = n \lfloor Q_9 / m \rfloor$. If $n \ge 1$, $m \ge 1$ and $m$
divides $Q_9$, then $N_1(m, n) \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N1_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n1-pos).

## Upper bound for the scaled factorial argument $N_{10}$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_{10}(m, n) = 10 n \lfloor Q_9 / m \rfloor$, where
$\lfloor Q_9 / 0 \rfloor$ is taken to be $0$. Then $N_{10}(m, n) \le 10 Q_9 n$ for all natural
numbers $m$ and $n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N10_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n10-le).

## Upper bound for the scaled factorial argument $N_9$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_9(m, n) = 9 n \lfloor Q_9 / m \rfloor$, where $\lfloor Q_9 / 0 \rfloor$
is taken to be $0$. Then $N_9(m, n) \le 10 Q_9 n$ for all natural numbers $m$ and $n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N9_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n9-le).

## Upper bound for the scaled factorial argument $N_1$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_1(m, n) = n \lfloor Q_9 / m \rfloor$, where $\lfloor Q_9 / 0 \rfloor$
is taken to be $0$. Then $N_1(m, n) \le 10 Q_9 n$ for all natural numbers $m$ and $n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N1_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n1-le).

## N₁₀ splits as N₉ + N₁

For natural numbers $m$ and $n$ with $m \ge 1$ and $m$ dividing
$Q_9 = 210$, write $N_k(m, n) = kn \lfloor Q_9 / m \rfloor$ for $k = 1, 9, 10$. Then
$N_{10}(m, n) = N_9(m, n) + N_1(m, n)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Nadd9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#nadd9).

## Factorial divisibility behind ratio₉

For natural numbers $m$ and $n$ with $m \ge 1$ and
$m$ dividing $Q_9 = 210$, write $N_k(m, n) = kn \lfloor Q_9 / m \rfloor$ for $k = 1, 9, 10$.
Then $N_9(m, n)! \cdot N_1(m, n)!$ divides $N_{10}(m, n)!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.ratio9_dvd`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#ratio9-dvd).

## Positivity of ratio₉

For natural numbers $m$ and $n$ with $n \ge 1$, $m \ge 1$ and $m$
dividing $Q_9 = 210$, the binomial factor
$\mathrm{ratio}_9(m, n) = N_{10}(m, n)! / (N_9(m, n)! \cdot N_1(m, n)!)$ is positive, where
$N_k(m, n) = kn \lfloor Q_9 / m \rfloor$ for $k = 1, 9, 10$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.ratio9_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#ratio9-pos).

## Logarithm of the binomial factor

Let $m$ and $n$ be natural numbers with $n \ge 1$,
$m \ge 1$ and $m \mid 210$, and put $k = 210/m$. Then

$$\log \frac{(10nk)!}{(9nk)!\,(nk)!} = \log (10nk)! - \log (9nk)! - \log (nk)!.$$

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_ratio9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#log-ratio9).

## Möbius reciprocal sum over the divisors of 210, in the rationals

Let $w_9$ be the
table of pairs $(d, \mu(d))$, where $d$ runs over the divisors of $210$ and $\mu$ is the Möbius
function. Then the sum of $\mu(d)/d$ over the pairs of $w_9$, computed in $\mathbb{Q}$, is
$8/35$; that is, $\sum_{d \mid 210} \mu(d)/d = 8/35$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_mu_sum_Q`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#w9-mu-sum-q).

## Möbius reciprocal sum over the divisors of 210, in the reals

Let $w_9$ be the
table of pairs $(d, \mu(d))$, where $d$ runs over the divisors of $210$ and $\mu$ is the Möbius
function. Then the sum of $\mu(d)/d$ over the pairs of $w_9$, computed in $\mathbb{R}$, is
$8/35$; that is, $\sum_{d \mid 210} \mu(d)/d = 8/35$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.w9_mu_sum_R`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#w9-mu-sum-r).

## Lower bound for $\log N!$

For every natural number $N \ge 1$,
$N \log N - N + 1 \le \log N!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_fact_lower`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#log-fact-lower).

## Upper bound for $\log N!$

For every natural number $N \ge 1$,
$\log N! \le (N + 1) \log N - N + 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_fact_upper`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#log-fact-upper).

## Main Stirling term

For a real number $x$, $f_{\mathrm{main}}(x) = x \log x - x$.

This is the main term of Stirling's approximation to $\log x!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.fmain`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#fmain).

## Termwise Stirling lower bound in Breusch's argument

Let $(d, \varepsilon)$ be a pair in
the Möbius divisor table $W_9$ for $Q_9 = 210$ and let $n \ge 1$ be a natural number. Write
$q = \lfloor Q_9 / d \rfloor$ for the natural-number quotient, and let $A = N_{10}(d, n) = 10nq$,
$B = N_9(d, n) = 9nq$ and $C = N_1(d, n) = nq$ be the scaled factorial arguments and
$f_{\mathrm{main}}(x) = x \log x - x$ the main Stirling term. Then
$\varepsilon (\log A! - \log B! - \log C!) \ge \varepsilon (f_{\mathrm{main}}(A) -
f_{\mathrm{main}}(B) - f_{\mathrm{main}}(C)) - (1 + \log A + \log B + \log C)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.logF9_term_lower`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#log-f9-term-lower).

## Divisors of 210 divide multiples of 210

Let $w_9$ be the table of divisors $d$ of
$Q_9 = 210$ paired with their Möbius values. If $C$ is a natural number with $Q_9 \mid C$, then
for every pair $(d, \varepsilon)$ in $w_9$ and every natural number $n$, $d \mid C n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.CNdvd9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#cndvd9).

## The constant $K_9$

Let $w_9$ be the table of divisors $d$ of $Q_9 = 210$ paired with
their Möbius values $\varepsilon$. Then

$$K_9 = \sum_{(d, \varepsilon) \in w_9} \frac{\varepsilon \log d}{d}.$$

It comes from the $\log d$ terms in the closed form of
$\sum_{(d, \varepsilon) \in w_9} \varepsilon f(N/d)$ with $f(x) = x \log x - x$, for $N$ a
multiple of $210$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.K9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#k9).

## Closed form of the Möbius-weighted main-term sum

Let $w_9$ be the table of pairs
$(d, \mu(d))$ for the divisors $d$ of $210$, let $f(x) = x \log x - x$, and let
$K_9 = \sum_{(d, \mu(d)) \in w_9} \mu(d) \log d / d$. For natural numbers $C > 0$ and $n \ge 1$
with $210 \mid C$, writing $N = Cn$ (so that $N/d$ is an integer for each $d$ in $w_9$), we have
$\sum_{(d, \mu(d)) \in w_9} \mu(d) f(N/d) = \frac{8}{35} N (\log N - 1) - K_9 N$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Z9_value`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#z9-value).

## Exact formula for the scaled factorial argument $N_{10}$

Let $Q_9 = 210$ and, for
natural numbers $m$ and $n$, let $N_{10}(m, n) = 10 n \lfloor Q_9 / m \rfloor$. If $m \ge 1$ and
$m$ divides $Q_9$, then $N_{10}(m, n) = \lfloor 10 Q_9 n / m \rfloor$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N10_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-03/index.html#n10-eq).

## Exact formula for the scaled factorial argument $N_9$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_9(m, n) = 9 n \lfloor Q_9 / m \rfloor$. If $m \ge 1$ and $m$ divides
$Q_9$, then $N_9(m, n) = \lfloor 9 Q_9 n / m \rfloor$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N9_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#n9-eq).

## Exact formula for the scaled factorial argument $N_1$

Let $Q_9 = 210$ and, for natural
numbers $m$ and $n$, let $N_1(m, n) = n \lfloor Q_9 / m \rfloor$. If $m \ge 1$ and $m$ divides
$Q_9$, then $N_1(m, n) = \lfloor Q_9 n / m \rfloor$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.N1_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#n1-eq).

## Combined main term of the Möbius-weighted Stirling sums

Let $w_9$ be the table of
pairs $(d, \mu(d))$ for the divisors $d$ of $210$, and let $f(x) = x \log x - x$. For every
natural number $n \ge 1$, writing $N = 210n$ (so that $N/d$ is an integer for each $d$ in
$w_9$), we have
$\sum_{(d, \mu(d)) \in w_9} \mu(d) \bigl(f(10N/d) - f(9N/d) - f(N/d)\bigr) =
48 n (10 \log 10 - 9 \log 9)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.Z9_combined`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 478](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L478). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#z9-combined).

## Lower bound for $\log F_9(n)$

Let $w_9$ be the table of divisors $d$ of $Q_9 = 210$
paired with their Möbius values $\varepsilon$, and for a natural number $n$ let

$$\log F_9(n) = \sum_{(d, \varepsilon) \in w_9}
\varepsilon \log \frac{(10 n k_d)!}{(9 n k_d)!\,(n k_d)!}, \qquad k_d = 210/d.$$

Then for every natural number $n \ge 1$,

$$48 n (10 \log 10 - 9 \log 9) - 16 - 48 \log(2100 n) \le \log F_9(n).$$

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.logF9_lower`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Lower.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#log-f9-lower).

## Extending the primorial bound leftward across an interval

Let $a \le m \le b$ be
natural numbers, and write $n\#$ for the primorial of $n$ (the product of all primes
$p \le n$). If $10^a \cdot b\# \le 34^a$, then $10^m \cdot m\# \le 34^m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.theta34_of_interval`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/ThetaBaseCases.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/ThetaBaseCases.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#theta34-of-interval).

## The multinomial coefficient $M(t)$ for the 3.4 primorial bound

For a natural number
$t$, $M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$, defined as the quotient of $(6t)!$ by
$(3t)!\,(2t)!\,t!$ in natural-number division.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34).

## Factorial divisibility behind the multinomial coefficient

For every natural number $t$,
the product $(3t)!\,(2t)!\,t!$ divides $(6t)!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_dvd`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-dvd).

## Positivity of the multinomial coefficient $M(t)$

Let $M(t)$ be the natural-number
quotient of $(6t)!$ by $(3t)!\,(2t)!\,t!$. For every natural number $t$, $M(t) > 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-pos).

## Cleared-denominator identity for the multinomial coefficient $M(t)$

Let $M(t)$ be the
natural-number quotient of $(6t)!$ by $(3t)!\,(2t)!\,t!$. For every natural number $t$,
$M(t) \cdot \big((3t)!\,(2t)!\,t!\big) = (6t)!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_eq_mul`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-eq-mul).

## The multinomial coefficient $M(t)$ as a product of binomial coefficients

Let
$M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$. For every natural number $t$,
$M(t) = \binom{6t}{3t} \binom{3t}{t}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_eq_choose_mul`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-eq-choose-mul).

## Half-power bound for the central binomial coefficient

For every natural number
$m \ge 1$, $\binom{2m}{m} \le 2^{2m-1}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.choose_middle_half`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#choose-middle-half).

## Multinomial bound for $(3t)!$

For every natural number $t$,
$(3t)! \le 3^{3t} (t!)^3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.multinomial3_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#multinomial3-le).

## Binomial factorization of the factorial of a multiple of three

For every natural
number $t$, $\binom{3t}{t} \binom{2t}{t} (t!)^3 = (3t)!$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.choose3_mul_choose2`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#choose3-mul-choose2).

## Four-power lower bound for the central binomial coefficient

For every natural number
$t$, $4^t \le (2t+1)\binom{2t}{t}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.four_pow_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#four-pow-le).

## Key estimate for the multinomial coefficient $M(t)$

Let
$M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$. For every natural number $t \ge 1$,
$2\,M(t) \le 432^t \, (2t + 1)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_key`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-key).

## Base case of the threshold inequality

The inequality
$10^{1145} \cdot 432^{230} \cdot 461 \le 2 \cdot 34^{1145}$ holds; this is the inequality
$10^{5t-5} \cdot 432^{t} \cdot (2t+1) \le 2 \cdot 34^{5t-5}$ at $t = 230$.

Checked by direct computation.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.P34_base`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#p34-base).

## Induction step of the threshold inequality

Let $t \ge 230$ be a natural number. If
$10^{5t-5} \cdot 432^{t} \cdot (2t+1) \le 2 \cdot 34^{5t-5}$, then
$10^{5t} \cdot 432^{t+1} \cdot (2t+3) \le 2 \cdot 34^{5t}$, which is the same inequality with
$t+1$ in place of $t$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.P34_step`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#p34-step).

## Threshold inequality for the multinomial bound

For every natural number $t \ge 230$,
$10^{5t-5} \cdot 432^{t} \cdot (2t+1) \le 2 \cdot 34^{5t-5}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.P34`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#p34).

## Power bound for the multinomial coefficient $M(t)$, large $t$

Let
$M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$. For every natural number $t \ge 230$,
$10^{5t-5} \cdot M(t) \le 34^{5t-5}$, that is, $M(t) \le 3.4^{5t-5}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_bound_large`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-bound-large).

## Power bound for the multinomial coefficient $M(t)$, small $t$

Let
$M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$. For every natural number $k < 207$, writing
$t = 23 + k$ (so $23 \le t < 230$), we have $10^{5t-5} \cdot M(t) \le 34^{5t-5}$.

The finitely many cases are checked by direct computation.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_bound_small`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-04/index.html#m34-bound-small).

## Power bound for the multinomial coefficient $M(t)$

Let
$M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$. For every natural number $t \ge 23$,
$10^{5t-5} \cdot M(t) \le 34^{5t-5}$, that is, $M(t) \le 3.4^{5t-5}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.M34_bound`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#m34-bound).

## Superadditivity of floor division for three terms

For natural numbers $a, b, c$ and
$q > 0$, $\lfloor a/q \rfloor + \lfloor b/q \rfloor + \lfloor c/q \rfloor \le
\lfloor (a+b+c)/q \rfloor$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.div_add_div_add_div_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#div-add-div-add-div-le).

## Floor-difference bound on the range 3t < p ≤ 6t

Let $t \ge 1$ and $p$ be natural
numbers with $3t < p \le 6t$. Then
$\lfloor 6t/p \rfloor - \lfloor 3t/p \rfloor - \lfloor 2t/p \rfloor \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_term_case1`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-term-case1).

## Floor-difference bound on the range 2t < p ≤ 3t

Let $t \ge 1$ and $p$ be natural
numbers with $2t < p \le 3t$. Then
$\lfloor 6t/p \rfloor - \lfloor 3t/p \rfloor - \lfloor 2t/p \rfloor \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_term_case2`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-term-case2).

## Floor-difference bound on the range 3t/2 < p ≤ 2t

Let $t \ge 1$ and $p$ be natural
numbers with $3t < 2p$ and $p \le 2t$. Then
$\lfloor 6t/p \rfloor - \lfloor 3t/p \rfloor - \lfloor 2t/p \rfloor \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_term_case3`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-term-case3).

## Floor-difference bound on the range 6t/5 < p ≤ 3t/2

Let $t \ge 1$ and $p$ be natural
numbers with $6t < 5p$ and $2p \le 3t$. Then
$\lfloor 6t/p \rfloor - \lfloor 3t/p \rfloor - \lfloor 2t/p \rfloor \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_term_case4`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-term-case4).

## Floor-difference bound on the range t < p ≤ 6t/5

Let $t \ge 1$ and $p$ be natural
numbers with $t < p$ and $5p \le 6t$. Then
$\lfloor 6t/p \rfloor - \lfloor 3t/p \rfloor - \lfloor 2t/p \rfloor \ge 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_term_case5`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-term-case5).

## Floor-difference bound on the range t < p ≤ 6t

Let $t \ge 1$ and $p$ be natural
numbers with $t < p \le 6t$. Then
$\lfloor 6t/p \rfloor - \lfloor 3t/p \rfloor - \lfloor 2t/p \rfloor \ge 1$.

This is the $j = 1$ term of Legendre's formula for the exponent of $p$ in
$(6t)!/((3t)!\,(2t)!\,t!)$; on this range $\lfloor t/p \rfloor = 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_term1`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-term1).

## Primes in $(t, 6t)$ occur in $M(t)$

For every natural number $t \ge 1$ and every prime $p$
with $t < p \le 6t$, the exponent of $p$ in the prime factorization of the multinomial coefficient
$M(t) = (6t)!/((3t)!\,(2t)!\,t!)$ is at least $1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_M34`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#vp-m34).

## Splitting the primorial with a multinomial coefficient

For a natural number $n$ let
$n\#$ be the primorial, the product of the primes $p \le n$, and let
$M(t) = \frac{(6t)!}{(3t)!\,(2t)!\,t!}$. For every natural number $m \ge 1$, with
$t = \lfloor (m+5)/6 \rfloor$, we have $m\# \le t\# \cdot M(t)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.theta_le_M34`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 439](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L439). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#theta-le-m34).

## Primorial bound $3.4^m$ below $133$

For a natural number $n$ let $n\#$ be the
primorial, the product of the primes $p \le n$. For every natural number $m < 133$,
$10^m \cdot m\# \le 34^m$.

Proved by covering $0 \le m \le 132$ with finitely many intervals $[a, b]$ and checking
$10^a \cdot b\# \le 34^a$ for each; this gives the bound on $[a, b]$ because $n\#$ is
nondecreasing in $n$ and $10 \le 34$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.theta34_base`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#theta34-base).

## Primorial bound by powers of 3.4, integer form

For every natural number $m$, the
primorial $m\#$ (the product of all primes $p \le m$) satisfies $10^m \cdot m\# \le 34^m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.theta34_nat`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#theta34-nat).

## Primorial bound by powers of 3.4, real form

For every real number $x \ge 0$, the
primorial of $\lfloor x \rfloor$ (the product of all primes $p \le \lfloor x \rfloor$) is at
most $3.4^x$, where $3.4^x$ is the real power.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.theta34_real`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 531](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L531). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#theta34-real).

## Bounding a logarithm above by the exponential

Let $a$ and $r$ be real numbers with
$a > 0$. If $a < e^r$, then $\log a < r$, where $\log$ is the natural logarithm.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_lt_of_exp_gt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 549](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L549). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#log-lt-of-exp-gt).

## Logarithm lower bound from an exponential bound

For real numbers $a > 0$ and $r$, if
$e^r < a$ then $r < \log a$, where $\log$ is the natural logarithm.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_gt_of_exp_lt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#log-gt-of-exp-lt).

## Exponential lower bound from a power comparison

Let $a$ and $c$ be nonnegative real
numbers and let $n$ and $m$ be positive integers. If $c < e$ and $a^n < c^m$, then
$a < e^{m/n}$, where $m/n$ is real division.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.lt_exp_of_pow_lt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 562](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L562). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#lt-exp-of-pow-lt).

## Power comparison above e bounds an exponential

Let $e$ be Euler's number, let $a$
and $c$ be real numbers and let $m, n$ be nonzero natural numbers, with $a \ge 0$,
$e^{m/n} \ge 0$ and $c > e$. If $c^m < a^n$, then $e^{m/n} < a$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.exp_lt_of_pow_lt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 583](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L583). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#exp-lt-of-pow-lt).

## Lower bound for log 2

The natural logarithm of $2$ satisfies $0.6931 < \log 2$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log2_gt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#log2-gt).

## Lower bound for log 5

The natural logarithm of $5$ satisfies $1.6094 < \log 5$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log5_gt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#log5-gt).

## Upper bound for log 3

The natural logarithm of $3$ satisfies $\log 3 < 1.0987$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log3_lt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-05/index.html#log3-lt).

## Upper bound for log 17

The natural logarithm of $17$ satisfies $\log 17 < 2.8333$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log17_lt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 660](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L660). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log17-lt).

## Logarithm of 10

The natural logarithm satisfies $\log 10 = \log 2 + \log 5$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log10_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log10-eq).

## Logarithm of 9

The natural logarithm satisfies $\log 9 = 2 \log 3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log9_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 684](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L684). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log9-eq).

## Logarithm of 3.4

The natural logarithm satisfies $\log(34/10) = \log 17 - \log 5$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log34div10_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log34div10-eq).

## Evaluation of a three-term rational sum

In the real numbers,
$\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963} = \frac{28121100}{242141}$.

The right-hand side is the sum written in lowest terms.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.c9_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#c9-eq).

## Numerical margin of the main term

With $\log$ the natural logarithm,
$48\,(10 \log 10 - 9 \log 9) -
\left(\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963}\right) \log \frac{34}{10} > 13$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.T03c_eqmain_margin`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 700](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L700). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#t03c-eqmain-margin).

## Prime-counting bound $\pi(m) \le m/3$ for $36 \le m < 156$

Let $\pi(m)$ denote the
number of primes $p \le m$. For every natural number $m$ with $36 \le m < 156$, $3\pi(m) \le m$.

Checked by computation.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.pi_third_small`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 711](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L711). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#pi-third-small).

## Prime-counting bound $\pi(m) \le m/3$ from $156$ on

Let $\pi(m)$ denote the number of
primes $p \le m$. For every natural number $m \ge 156$, $3\pi(m) \le m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.pi_third_large`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 715](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L715). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#pi-third-large).

## Prime-counting bound $\pi(m) \le m/3$ for natural $m \ge 36$

Let $\pi(m)$ denote the
number of primes $p \le m$. For every natural number $m \ge 36$, $3\pi(m) \le m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.pi_third_nat`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 729](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L729). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#pi-third-nat).

## Prime-counting bound $\pi(x) \le x/3$ for real $x \ge 36$

Let $\pi(n)$ denote the
number of primes $p \le n$. For every real number $x \ge 36$, $\pi(\lfloor x \rfloor) \le x/3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.pi_third`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#pi-third).

## Upper bound for log 10

The natural logarithm of $10$ satisfies $\log 10 < 2.4$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log10_lt`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log10-lt).

## Strict decay of log over square root beyond e squared

Let $a$ and $t$ be real numbers
with $a > 0$, $t > 1$ and $\log a > 2$, where $\log$ is the natural logarithm. Then
$\frac{\log(at)}{\sqrt{at}} < \frac{\log a}{\sqrt{a}}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_div_sqrt_decay`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log-div-sqrt-decay).

## Logarithm bounded by a multiple of the square root

For every real number $x \ge 10^7$,
$\log x \le 0.006\sqrt{x}$, where $\log$ is the natural logarithm.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.log_le_sqrt06`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#log-le-sqrt06).

## Positivity of the gap in Breusch's prime interval argument

For every natural number
$n \ge 4762$, $13n - 16 - 48\log(2100n) - \sqrt{2100n}\,\log(2100n) > 0$, where $\log$ is the
natural logarithm.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.gap_pos`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean, line 853](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Theta.lean#L853). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#gap-pos).

## Continuous Breusch function

For real $x$, the continuous Breusch function is the
integer

$$G(x) = \sum_{d \mid 210} \mu(d) \left( \lfloor 2100x/d \rfloor - \lfloor 1890x/d \rfloor -
\lfloor 210x/d \rfloor \right),$$

where $d$ ranges over the positive divisors of $210$, $\mu$ is the Möbius function, and each
floor is the natural-number floor, which is $0$ for negative arguments.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#g9r).

## Floor of a quotient of natural numbers

For all natural numbers $a$ and $b$, the floor of
the real number $a / b$ equals the quotient of $a$ by $b$ in integer division. When $b = 0$ both
sides are $0$, since division by zero gives $0$ in both the reals and the natural numbers.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.nat_floor_nat_div`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#nat-floor-nat-div).

## Remainder bound for common multiples

Let $a$, $b$, $d$ be natural numbers with $b > 0$,
$d > 0$, $d \mid b$ and $d \mid a$. Then the remainder of $a$ modulo $b$ is at most $b - d$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.nat_mod_le_of_dvd`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#nat-mod-le-of-dvd).

## Real floors at divisors of 210 agree with grid floors

Let $C$ and $L$ be positive natural
numbers, let $m$ be a divisor of $210$ with $C \mid mL$, and let $x \ge 0$ be a real number. Then
$\lfloor Cx/m \rfloor = \lfloor C \lfloor Lx \rfloor / (mL) \rfloor$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.floor_grid_match`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#floor-grid-match).

## Shifting a floor quotient by one period

Let $C$ and $m$ be natural numbers with $m > 0$
and $m \mid C$. Then for every natural number $j$,
$\lfloor C(j + 18900)/(18900m) \rfloor = \lfloor Cj/(18900m) \rfloor + C/m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.div_shift189`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#div-shift189).

## One-period shift of $G_9$

For every natural number $j$, the grid $G$-function for $k = 9$
satisfies $G_9(j + 18900) = G_9(j)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9_shift`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-06/index.html#g9-shift).

## Periodicity of $G_9$ in multiples of $18900$

For all natural numbers $o$ and $r$, the
grid $G$-function for $k = 9$ satisfies $G_9(18900\,o + r) = G_9(r)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9_period_iter`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9-period-iter).

## $G_9$ depends only on the residue modulo $18900$

For every natural number $j$, the grid
$G$-function for $k = 9$ satisfies $G_9(j) = G_9(j \bmod 18900)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9_eq_mod`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9-eq-mod).

## The continuous Breusch function agrees with the grid function

For every real
$x \ge 0$, the continuous Breusch function $G$ and the Breusch grid function $G_9$ satisfy
$G(x) = G_9(\lfloor 18900x \rfloor)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_eq_grid`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-eq-grid).

## The Breusch grid function vanishes below 9

For every natural number $j < 9$, the
Breusch grid function $G_9$ satisfies $G_9(j) = 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9_zero9`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9-zero9).

## Value of $G_9$ at $9$

The grid $G$-function for $k = 9$ satisfies $G_9(9) = 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9_at9`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9-at9).

## Bound $G_9 \le 1$ below $10$

For every natural number $j < 10$, the grid $G$-function for
$k = 9$ satisfies $G_9(j) \le 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9_small_le1`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9-small-le1).

## The continuous Breusch function is at most 3

For every real $x \ge 0$, the continuous
Breusch function $G$ satisfies $G(x) \le 3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_le3`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-le3).

## The continuous Breusch function vanishes near zero

For every real $x$ with
$0 \le x < 1/2100$, the continuous Breusch function $G$ satisfies $G(x) = 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_vanish`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-vanish).

## Level-$1$ threshold for the continuous Breusch function

Let $Q_9 = 210$. For every real
$x \ge 1/(9 Q_9) = 1/1890$, if the continuous Breusch function $G$ satisfies $G(x) \ge 1$, then
$x \ge 279/18900$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_level1`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-level1).

## Level-$2$ threshold for the continuous Breusch function

Let $Q_9 = 210$. For every real
$x \ge 1/(9 Q_9) = 1/1890$, if the continuous Breusch function $G$ satisfies $G(x) \ge 2$, then
$x \ge 657/18900$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_level2`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-level2).

## Level-$3$ threshold for the continuous Breusch function

Let $Q_9 = 210$. For every real
$x \ge 1/(9 Q_9) = 1/1890$, if the continuous Breusch function $G$ satisfies $G(x) \ge 3$, then
$x \ge 963/18900$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_level3`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-level3).

## Integer cast of the floor of a quotient of natural numbers

For natural numbers $t$ and
$d$, the floor of the real number $t/d$, as an integer, equals the natural-number quotient of $t$
by $d$ (rounded down), as an integer. Both sides are $0$ when $d = 0$, since division by zero is
$0$ for both real numbers and natural numbers.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.intFloor_cast`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#int-floor-cast).

## Legendre terms of $N_{10}$ as real floors

Let $m \ge 1$ divide $Q_9 = 210$, and let
$p \ge 2$, $n$ and $j$ be natural numbers. Write $N_{10}(m, n) = 10n \cdot (Q_9/m)$.
Then $\lfloor N_{10}(m, n)/p^j \rfloor$ equals the floor of the real number $10 Q_9 (n/p^j)/m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.floor_N10`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#floor-n10).

## Legendre terms of $N_9$ as real floors

Let $m \ge 1$ divide $Q_9 = 210$, and let
$p \ge 2$, $n$ and $j$ be natural numbers. Write $N_9(m, n) = 9n \cdot (Q_9/m)$.
Then $\lfloor N_9(m, n)/p^j \rfloor$ equals the floor of the real number $9 Q_9 (n/p^j)/m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.floor_N9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#floor-n9).

## Legendre terms of $N_1$ as real floors

Let $m \ge 1$ divide $Q_9 = 210$, and let
$p \ge 2$, $n$ and $j$ be natural numbers. Write $N_1(m, n) = n \cdot (Q_9/m)$.
Then $\lfloor N_1(m, n)/p^j \rfloor$ equals the floor of the real number $Q_9 (n/p^j)/m$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.floor_N1`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#floor-n1).

## Legendre's formula with integer summands

Let $p$ be a prime and let $N$ and $b$ be
natural numbers with $\lfloor \log_p N \rfloor < b$, where $\lfloor \log_p N \rfloor$ is taken to
be $0$ when $N = 0$. Then the exponent of $p$ in $N!$, as an integer, equals
$\sum_{j=1}^{b-1} \lfloor N / p^j \rfloor$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.legendre_sum9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#legendre-sum9).

## Valuation of a factorial ratio as a difference of valuations

Let $Q = 210$, let
$m \ge 1$ be a divisor of $Q$, and let $n$, $p$ be natural numbers. Write $N = n \cdot (Q/m)$
and $R_m(n) = (10N)! / ((9N)! \, N!)$. Then, as integers,
$v_p(R_m(n)) = v_p((10N)!) - v_p((9N)!) - v_p(N!)$, where $v_p(k)$ is the exponent of $p$
in the prime factorization of $k$ (zero when $p$ is not prime).

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.vp_ratio9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#vp-ratio9).

## One divisor's contribution to the valuation

For a pair $(m, \varepsilon)$ of a natural
number $m$ and an integer $\varepsilon$, and natural numbers $p$ and $n$, let
$a = \lfloor 210/m \rfloor$ (so $a = 0$ when $m = 0$). The term is the integer
$\varepsilon\bigl(v_p((10na)!) - v_p((9na)!) - v_p((na)!)\bigr)$, where $v_p(k)$ is the exponent
of $p$ in the prime factorization of $k$ (zero when $p$ is not prime).

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.nu9term`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#nu9term).

## The $p$-adic valuation of the weighted product

For natural numbers $p$ and $n$,
$\nu_p(n)$ is the integer
$\sum_{d \mid 210} \mu(d)\bigl(v_p((2100n/d)!) - v_p((1890n/d)!) -
v_p((210n/d)!)\bigr)$, where $\mu$ is the Möbius function and $v_p(m)$ is the exponent of $p$
in the prime factorization of $m$ (zero when $p$ is not prime).

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.nu9`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#nu9).

## The continuous Breusch function vanishes at small ratios

Let $p$ be a prime and let
$n \ge 1$ and $j$ be natural numbers. If $p^j > 2100n$, then the continuous Breusch function
$G$ satisfies $G(n/p^j) = 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.G9r_vanish_of`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-07/index.html#g9r-vanish-of).

## Valuation identity for the weighted product

Write $v_p(m)$ for the exponent of $p$ in $m$
and $\mu$ for the Möbius function, and set
$\nu_p(n) = \sum_{d \mid 210} \mu(d)\bigl(v_p((2100n/d)!) - v_p((1890n/d)!) -
v_p((210n/d)!)\bigr)$ and, for real $x \ge 0$,
$G(x) = \sum_{d \mid 210} \mu(d)\bigl(\lfloor 2100x/d \rfloor - \lfloor 1890x/d \rfloor -
\lfloor 210x/d \rfloor\bigr)$. If $p$ is a prime and $n$, $b$ are natural numbers with
$\lfloor \log_p (2100n) \rfloor < b$, where the floor of the logarithm is taken to be $0$ when
$n = 0$, then $\nu_p(n) = \sum_{j=1}^{b-1} G(n/p^j)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.nu9_eq_sum_G`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 466](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L466). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#nu9-eq-sum-g).

## Single-term valuation identity for large primes

Write $v_p(m)$ for the exponent of $p$
in $m$ and $\mu$ for the Möbius function, and set
$\nu_p(n) = \sum_{d \mid 210} \mu(d)\bigl(v_p((2100n/d)!) - v_p((1890n/d)!) -
v_p((210n/d)!)\bigr)$ and, for real $x \ge 0$,
$G(x) = \sum_{d \mid 210} \mu(d)\bigl(\lfloor 2100x/d \rfloor - \lfloor 1890x/d \rfloor -
\lfloor 210x/d \rfloor\bigr)$. If $p$ is a prime and $n \ge 1$ is a natural number with
$2100n < p^2$, then $\nu_p(n) = G(n/p)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.nu9_eq_single`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#nu9-eq-single).

## Value of $10Qn$

Let $Q = 210$ be the truncation modulus. For every natural number $n$,
$10 \cdot Q \cdot n = 2100n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_10Q9`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 523](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L523). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-10-q9).

## Logarithm of a natural number from its factorization

For every nonzero natural number
$K$, $\log K = \sum_{p} v_p(K) \log p$, where $p$ runs over the prime divisors of $K$ and
$v_p(K)$ is the exponent of $p$ in the prime factorization of $K$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_log_fact`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-log-fact).

## Bound on the prime factors of the ratio factors

Let $(m, \mu)$ be an entry of the
divisor table $w_9$ (so $m$ divides $210$ and $\mu$ is the Möbius value of $m$), let $n$ be a
natural number and put $d = 210/m$. Then every prime factor of $(10nd)!/((9nd)!\,(nd)!)$ is at
most $2100n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_supp_sub`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-supp-sub).

## Valuation term of one binomial factor

Let $Q = 210$, let $m \ge 1$ be a divisor of $Q$,
let $w$ be an integer, and let $p$ and $n$ be natural numbers. Put $N = n \cdot (Q/m)$ and
$R = (10N)!/((9N)!\,N!)$. For a natural number $a$, write $v_p(a)$ for the exponent of $p$ in
the prime factorization of $a$ (zero when $p$ is not prime). Then
$w \, (v_p((10N)!) - v_p((9N)!) - v_p(N!)) = w \, v_p(R)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_nu9term_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 570](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-nu9term-eq).

## Valuation terms vanish off the prime support

Let $m \ge 1$ be a divisor of $Q_9 = 210$,
let $\mu$ be an integer, let $p$ and $n$ be natural numbers, and put $d = 210/m$. For a natural
number $k$ write $v_p(k)$ for the exponent of $p$ in the prime factorization of $k$ (zero when
$p$ is not prime). If $v_p\bigl((10nd)!/((9nd)!\,(nd)!)\bigr) = 0$, then the valuation term
$\mu\,\bigl(v_p((10nd)!) - v_p((9nd)!) - v_p((nd)!)\bigr)$ of the pair $(m, \mu)$ at $p$ and $n$
is $0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_nu9term_zero`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-nu9term-zero).

## A weighted log-factor as a sum over primes

Let $(m, \mu)$ be an entry of the divisor
table $w_9$ (so $m$ divides $210$ and $\mu$ is the Möbius value of $m$), let $n \ge 1$ be a
natural number, put $d = 210/m$ and $R = (10nd)!/((9nd)!\,(nd)!)$, and for a prime $p$ write
$\nu_p = \mu\,\bigl(v_p((10nd)!) - v_p((9nd)!) - v_p((nd)!)\bigr)$, where $v_p(k)$ is the
exponent of $p$ in the prime factorization of $k$. Then $\mu \log R$ equals the sum of
$\nu_p \log p$ over all primes $p \le 2100n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_q_expand`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 587](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L587). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-q-expand).

## Prime factorization of $\log F_9(n)$

Let $n \ge 1$ be a natural number. For each divisor
$m$ of $210$ put $N_m = 210n/m$, let $\mu$ be the Möbius function, and let
$F_9(n) = \prod_{m \mid 210} \binom{10N_m}{N_m}^{\mu(m)}$. For a prime $p$ let $v_p$ denote the
$p$-adic valuation and put
$\nu_9(p, n) = \sum_{m \mid 210} \mu(m) (v_p((10N_m)!) - v_p((9N_m)!) - v_p(N_m!))$, the
$p$-adic valuation of $F_9(n)$. Then $\log F_9(n) = \sum_{p \le 2100n} \nu_9(p, n) \log p$, where
$p$ runs over the primes at most $2100n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_bridge`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-bridge).

## Logarithms of primes are nonnegative

For every prime $p$, $\log p \ge 0$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_logp_nonneg`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 634](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L634). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-logp-nonneg).

## $G$ is at most its positive part

For real $y$ let
$G(y) = \sum_{m \mid 210} \mu(m) (\lfloor 2100y/m \rfloor_+ - \lfloor 1890y/m \rfloor_+ -
\lfloor 210y/m \rfloor_+)$, where $\mu$ is the Möbius function and
$\lfloor t \rfloor_+ = \max(\lfloor t \rfloor, 0)$. For every real number $x$,
$G(x) \le \max(G(x), 0)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_G_toNat`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 641](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L641). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-g-to-nat).

## The truncated continuous Breusch function is at most 3

For every real $x \ge 0$, the
continuous Breusch function $G$ satisfies $\max(G(x), 0) \le 3$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_toNat_le3`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-to-nat-le3).

## Positive lower bounds on a truncation lift to the integer

Let $z$ be an integer and let
$i \ge 1$ be a natural number. If $i \le \max(z, 0)$, then $i \le z$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_of_toNat`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-of-to-nat).

## Layer-cake decomposition with three levels

Let $B$ be a finite set of natural numbers,
let $M : \mathbb{N} \to \mathbb{N}$ and $c : \mathbb{N} \to \mathbb{R}$, and suppose $M(p) \le 3$
for every $p \in B$. Then
$\sum_{p \in B} M(p) c(p) = \sum_{i=1}^{3} \sum_{p \in B,\, M(p) \ge i} c(p)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_layercake`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 669](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L669). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-layercake).

## A level bound turns into a bound on the prime

Let $n \ge 1$ be a natural number, $p$ a
prime and $j \ge 1$ a real number. If $j / 18900 \le n / p$, then $p \le 18900\,n / j$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_ple_of_G`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 710](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L710). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-ple-of-g).

## Primes up to $1890n$ have $n/p \ge 1/1890$

Let $Q = 210$ be the truncation modulus, let
$n \ge 1$ be a natural number and let $p$ be a prime with $p \le 1890 n$. Then
$1/(9Q) \le n/p$, where $9Q = 1890$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_xlo`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-xlo).

## Upper bound for primes where a Möbius-weighted floor sum is at least 1

For real
$x \ge 0$ let $G(x) = \sum_{m \mid 210} \mu(m)\bigl(\lfloor 2100x/m \rfloor -
\lfloor 1890x/m \rfloor - \lfloor 210x/m \rfloor\bigr)$, where $\mu$ is the Möbius function.
Let $n \ge 1$ be a natural number and $p \le 1890n$ a prime. If $G(n/p) \ge 1$, then
$p \le 18900n/279$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_ple1`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-ple1).

## Upper bound for primes where a Möbius-weighted floor sum is at least 2

For real
$x \ge 0$ let $G(x) = \sum_{m \mid 210} \mu(m)\bigl(\lfloor 2100x/m \rfloor -
\lfloor 1890x/m \rfloor - \lfloor 210x/m \rfloor\bigr)$, where $\mu$ is the Möbius function.
Let $n \ge 1$ be a natural number and $p \le 1890n$ a prime. If $G(n/p) \ge 2$, then
$p \le 18900n/657$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_ple2`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 748](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L748). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-ple2).

## Upper bound for primes where a Möbius-weighted floor sum is at least 3

For real
$x \ge 0$ let $G(x) = \sum_{m \mid 210} \mu(m)\bigl(\lfloor 2100x/m \rfloor -
\lfloor 1890x/m \rfloor - \lfloor 210x/m \rfloor\bigr)$, where $\mu$ is the Möbius function.
Let $n \ge 1$ be a natural number and $p \le 1890n$ a prime. If $G(n/p) \ge 3$, then
$p \le 18900n/963$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_ple3`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-ple3).

## The primorial as a product of primes

For every natural number $k$, the primorial $k\#$
equals the product of all primes $p$ with $p < k + 1$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_primorial_eq`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 762](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L762). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-08/index.html#u9-primorial-eq).

## Chebyshev-type bound for the sum of prime logarithms

For every real number $Y \ge 0$,
the sum of $\log p$ over all primes $p \le \lfloor Y \rfloor$ is at most $Y \log 3.4$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_theta_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#u9-theta-le).

## Prime-logarithm bound for one level of $G$

For real $x \ge 0$ let
$G(x) = \sum_{m \mid 210} \mu(m) (\lfloor 2100x/m \rfloor - \lfloor 1890x/m \rfloor -
\lfloor 210x/m \rfloor)$, where $\mu$ is the Möbius function. Let $n \ge 1$ be a natural number,
let $B$ be a finite set of primes $p$ with $p \le 1890n$, let $i \ge 1$ be a natural number, and
let $j \ge 1$ be a real number with $18900n/j \ge 0$. Suppose that every prime $p \le 1890n$ with
$G(n/p) \ge i$ satisfies $p \le 18900n/j$. Then the sum of $\log p$ over the $p \in B$ with
$\max(G(n/p), 0) \ge i$ is at most $(18900n/j) \log 3.4$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_Bi_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 799](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L799). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#u9-bi-le).

## Contribution of primes with $p^2 > 2100n$

Write $v_p(m)$ for the exponent of $p$ in $m$
and $\mu$ for the Möbius function, and set
$\nu_p(n) = \sum_{d \mid 210} \mu(d)\bigl(v_p((2100n/d)!) - v_p((1890n/d)!) -
v_p((210n/d)!)\bigr)$. For every natural number $n \ge 1$, the sum of $\nu_p(n) \log p$ over the
primes $p \le 1890n$ with $p^2 > 2100n$ satisfies

$$
\sum_{\substack{p \le 1890n \text{ prime} \\ p^2 > 2100n}} \nu_p(n) \log p \le
\left(\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963}\right) n \log 3.4.
$$

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_B_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 830](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L830). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#u9-b-le).

## Bound for one small-square prime term

Let $n \ge 1$ be a natural number and let $p$ be a
prime with $p^2 \le 2100n$. For each divisor $m$ of $210$ put $N_m = 210n/m$, let $\mu$ be the
Möbius function and $v_p$ the $p$-adic valuation, and put
$\nu_9(p, n) = \sum_{m \mid 210} \mu(m) (v_p((10N_m)!) - v_p((9N_m)!) - v_p(N_m!))$. Then
$\nu_9(p, n) \log p \le 3 \log(2100n)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_Cterm_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 923](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L923). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#u9-cterm-le).

## Counting small-square primes

Let $n \ge 1$ be a natural number and let $C$ be a finite
set of primes $p$ with $p^2 \le 2100n$. Then $C$ has at most $\sqrt{2100n}/3$ elements.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_Ccard_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 1001](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L1001). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#u9-ccard-le).

## Contribution of the small-square primes

Let $n \ge 1$ be a natural number. For each
divisor $m$ of $210$ put $N_m = 210n/m$, let $\mu$ be the Möbius function, and for a prime $p$
with $p$-adic valuation $v_p$ put
$\nu_9(p, n) = \sum_{m \mid 210} \mu(m) (v_p((10N_m)!) - v_p((9N_m)!) - v_p(N_m!))$. Then the
sum of $\nu_9(p, n) \log p$ over the primes $p \le 1890n$ with $p^2 \le 2100n$ is at most
$\sqrt{2100n} \log(2100n)$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.U9_C_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 1037](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L1037). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#u9-c-le).

## Upper bound for $\log F_9(n)$ when $(1890n, 2100n)$ has no prime

Let $n \ge 1$ be a
natural number such that no prime $p$ satisfies $1890n < p \le 2100n$, and let
$\log F_9(n) = \sum_{d \mid 210} \mu(d) \log \frac{(2100n/d)!}{(1890n/d)!\,(210n/d)!}$, where $\mu$
is the Möbius function. Then

$$
\log F_9(n) \le \left(\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963}\right) n \log 3.4
\;+\; \sqrt{2100n}\,\log(2100n).
$$

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.logF9_upper`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean, line 1075](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch/Upper.lean#L1075). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#log-f9-upper).

## Breusch's endgame upper-bound inequality

For a natural number $n$ write
$L(n) = \sum_{d \mid 210} \mu(d) \log \binom{2100n/d}{210n/d}$, where $\mu$ is the Möbius function;
this is the logarithm of Breusch's product $F_9(n)$. The endgame upper-bound inequality at $n$ is
the statement

$$L(n) \le \left(\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963}\right)
n \log 3.4 + \sqrt{2100n}\,\log(2100n).$$

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.UpperIneq`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#upper-ineq).

## Breusch's prime chain

The chain is the list of the following 111 natural numbers, in
order:

53, 59, 61, 67, 73, 79, 83, 89, 97, 109, 113, 127, 139, 151, 167, 181, 199, 223, 241, 271, 293,
317, 353, 397, 443, 491, 547, 613, 683, 761, 853, 953, 1069, 1201, 1327, 1489, 1669, 1877, 2111,
2371, 2663, 2971, 3331, 3739, 4201, 4723, 5309, 5953, 6691, 7523, 8461, 9511, 10691, 12011, 13499,
15173, 17053, 19183, 21577, 24251, 27281, 30689, 34519, 38833, 43669, 49123, 55259, 62143, 69899,
78623, 88427, 99469, 111893, 125863, 141587, 159233, 179119, 201499, 226669, 254993, 286859,
322709, 363047, 408427, 459479, 516911, 581521, 654209, 735983, 827969, 931421, 1047841, 1178809,
1326151, 1491913, 1678399, 1888193, 2124197, 2389721, 2688421, 3024457, 3402473, 3827767, 4306231,
4844501, 5450041, 6131239, 6897643, 7759831, 8729801, 9820997.

Every entry is prime, and each entry after the first is less than $\frac{9}{8}$ times the entry
before it.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.chain`, a definition declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#chain).

## Entries of Breusch's prime chain are prime

Every entry of the chain is a prime number.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.chain_prime`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#chain-prime).

## Breusch's prime chain is strictly increasing

Each entry of the chain is less than every
later entry.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.chain_sorted`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#chain-sorted).

## Consecutive entries of Breusch's prime chain are within a factor $9/8$

If $b$ immediately
follows $a$ in the chain, then $8b < 9a$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.chain_ratio`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#chain-ratio).

## Last entry of Breusch's prime chain

The last entry of the chain is $9820997$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.chain_getLast`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#chain-get-last).

## Bracketing a real number in an increasing list

Let $X$ be a real number and let
$c_0 < c_1 < \dots < c_k$ be natural numbers with $c_0 \le X < c_k$. Then there is an index
$i < k$ with $c_i \le X < c_{i+1}$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.bracket`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#bracket).

## Consecutive pairs survive prepending

Let $R$ be a list of natural numbers and let
$a, b, d$ be natural numbers. If $(a, b)$ is a pair of consecutive entries of $R$ (an element
of the list obtained by zipping $R$ with its tail), then $(a, b)$ is also a pair of consecutive
entries of the list obtained by prepending $d$ to $R$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.zip_cons_mem`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#zip-cons-mem).

## Adjacent entries form a consecutive pair

Let $l$, $l_1$, $l_2$ be lists of natural
numbers and let $a, b$ be natural numbers. If $l$ is the concatenation of $l_1$, the two-entry
list $a, b$, and $l_2$, then $(a, b)$ is a pair of consecutive entries of $l$ (an element of the
list obtained by zipping $l$ with its tail).

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.zip_mem_of_consec`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#zip-mem-of-consec).

## Primes in $(X, 9X/8)$ for $53 \le X < 9820997$

For every real number $X$ with
$53 \le X < 9820997$ there is a prime $p$ with $X < p < \frac{9}{8}X$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.chain_cover`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#chain-cover).

## Every large real lies in a window $(5600n/3, 1890n)$

For every real number
$X \ge 5600 \cdot 4762 / 3$ there is a natural number $n \ge 4762$ with
$5600n/3 \le X \le 1890n$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.overlap`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#overlap).

## Endgame contradiction in Breusch's theorem

Let $n \ge 4762$ be a natural number. If
there is no prime $p$ with $1890n < p \le 2100n$ and $n$ satisfies the endgame upper-bound
inequality, then we have a contradiction.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.main_contra`, a lemma declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#main-contra).

## Primes in $(X, 9X/8)$ for large $X$, assuming the upper bound

For a natural number $n$
write $L(n) = \sum_{m \mid 210} \mu(m) \log \binom{2100n/m}{210n/m}$, where $\mu$ is the Möbius
function. Let $X \ge 5600 \cdot 4762 / 3$ be a real number, and suppose that every natural number
$n \ge 1$ such that no prime $p$ satisfies $1890n < p \le 2100n$ also satisfies
$L(n) \le \left(\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963}\right) n \log 3.4 +
\sqrt{2100n}\,\log(2100n)$. Then there is a prime $p$ with $X < p < \frac{9}{8}X$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.analytic_at_X`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-09/index.html#analytic-at-x).

## Breusch's theorem from the upper bound

For a natural number $n$ write
$L(n) = \sum_{m \mid 210} \mu(m) \log \binom{2100n/m}{210n/m}$, where $\mu$ is the Möbius function.
Let $x \ge 48$ be a real number, and suppose that every natural number $n \ge 1$ such that no
prime $p$ satisfies $1890n < p \le 2100n$ also satisfies
$L(n) \le \left(\frac{18900}{279} + \frac{18900}{657} + \frac{18900}{963}\right) n \log 3.4 +
\sqrt{2100n}\,\log(2100n)$. Then there is a prime $p$ with $x < p < \frac{9}{8}x$.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.Internal.breusch_prime_interval_of_upper`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-10/index.html#breusch-prime-interval-of-upper).

## Breusch's theorem on primes between $x$ and $9x/8$

For every real number $x \ge 48$
there is a prime $p$ with $x < p < \frac{9}{8}x$.

## Sources

- R. Breusch, *Zur Verallgemeinerung des Bertrandschen Postulates*, Math. Z. 34 (1932), 505–526, conclusion on p. 515.

Formalized by `MathlibExt.NumberTheory.BreuschWanted.breusch_prime_interval`, a theorem declared in [MathlibExt/NumberTheory/PrimeInterval/Breusch.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeInterval/Breusch.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/part-10/index.html#breusch-prime-interval).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Breusch's theorem on primes between x and 9x/8](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/breusch-s-theorem-on-primes-between-x-and-9x-8)
