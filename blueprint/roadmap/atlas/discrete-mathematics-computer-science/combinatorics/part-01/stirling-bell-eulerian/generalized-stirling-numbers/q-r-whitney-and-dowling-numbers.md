---
declaration: section
origin: cited
lean: MetaMathlibExt.QRWhitney.qBrack, MetaMathlibExt.QRWhitney.whitneyFirst, MetaMathlibExt.QRWhitney.whitneySecond, MetaMathlibExt.QRWhitney.whitneyFirst_zero_zero, MetaMathlibExt.QRWhitney.whitneyFirst_zero_succ, MetaMathlibExt.QRWhitney.whitneyFirst_succ_zero, MetaMathlibExt.QRWhitney.whitneyFirst_succ_succ, MetaMathlibExt.QRWhitney.whitneySecond_zero_zero
statement: formalized
proof: formalized
---

# (q, r)-Whitney and Dowling numbers

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html).

## Complex q-integers

For a complex number $q$ and a natural number $n$, the q-integer
$[n]_q$ is the finite geometric sum $[n]_q = \sum_{i=0}^{n-1} q^i$.

Taking the sum rather than $(1 - q^n)/(1 - q)$ as the definition avoids any singularity at
$q = 1$.

Formalized by `MetaMathlibExt.QRWhitney.qBrack`, a definition declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#q-brack).

## (q, r)-Whitney numbers of the first kind

Let $m, r, q$ be complex numbers with
$q \ne 0$, and for a natural number $j$ let $[j]_q = \sum_{i=0}^{j-1} q^i$ be the q-integer.
The (q, r)-Whitney numbers of the first kind $w(n, k) = w_{m,r,q}(n, k)$, for natural numbers
$n$ and $k$, are defined by $w(0, 0) = 1$, $w(0, k + 1) = 0$ and, for all $n$ and $k$,

$$w(n + 1, 0) = -q^{-n} (m [n]_q + r) \, w(n, 0),$$



$$w(n + 1, k + 1) = q^{-n} \bigl( w(n, k) - (m [n]_q + r) \, w(n, k + 1) \bigr).$$

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst`, a definition declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first).

## (q, r)-Whitney numbers of the second kind

For complex numbers $m$, $r$, $q$, the
$(q, r)$-Whitney numbers of the second kind $W_{m,r,q}(n, k)$, indexed by natural numbers $n$
and $k$, are defined by $W_{m,r,q}(0, 0) = 1$, $W_{m,r,q}(0, k + 1) = 0$,
$W_{m,r,q}(n + 1, 0) = r \, W_{m,r,q}(n, 0)$ and

$$
W_{m,r,q}(n + 1, k + 1) = q^k \, W_{m,r,q}(n, k) + (m [k + 1]_q + r) \, W_{m,r,q}(n, k + 1),
$$

where $[j]_q = 1 + q + \dots + q^{j-1}$ is the $q$-integer.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond`, a definition declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second).

## Initial value of the first-kind (q, r)-Whitney numbers

For all complex numbers
$m, r, q$ with $q \ne 0$, the (q, r)-Whitney number of the first kind satisfies
$w_{m,r,q}(0, 0) = 1$.

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst_zero_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first-zero-zero).

## Row zero of the first-kind (q, r)-Whitney numbers

For all complex numbers $m, r, q$
with $q \ne 0$ and every natural number $k$, the (q, r)-Whitney number of the first kind
satisfies $w_{m,r,q}(0, k + 1) = 0$.

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst_zero_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first-zero-succ).

## Column-zero recurrence for first-kind (q, r)-Whitney numbers

Let $m, r, q$ be complex
numbers with $q \ne 0$, write $[j]_q$ for the q-integer of $j$, and write $w(n, k)$ for the
(q, r)-Whitney number of the first kind $w_{m,r,q}(n, k)$. Then for every natural number $n$,

$$w(n + 1, 0) = q^{-n} \bigl( 0 - (m [n]_q + r) \, w(n, 0) \bigr).$$

This is the general recurrence with $w(n, -1)$ read as $0$.

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst_succ_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first-succ-zero).

## Triangular recurrence for first-kind (q, r)-Whitney numbers

Let $m, r, q$ be complex
numbers with $q \ne 0$, write $[j]_q$ for the q-integer of $j$, and write $w(n, k)$ for the
(q, r)-Whitney number of the first kind $w_{m,r,q}(n, k)$. Then for all natural numbers $n$
and $k$,

$$w(n + 1, k + 1) = q^{-n} \bigl( w(n, k) - (m [n]_q + r) \, w(n, k + 1) \bigr).$$

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst_succ_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first-succ-succ).

## Initial value of the second-kind (q, r)-Whitney numbers

For complex numbers $m$, $r$,
$q$, let $W_{m,r,q}(i, j)$, for natural numbers $i$ and $j$, denote the $(q, r)$-Whitney numbers
of the second kind. Then $W_{m,r,q}(0, 0) = 1$.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_zero_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-zero-zero).

## Row zero of the second-kind (q, r)-Whitney numbers vanishes off the diagonal

For
complex numbers $m$, $r$, $q$, let $W_{m,r,q}(i, j)$, for natural numbers $i$ and $j$, denote
the $(q, r)$-Whitney numbers of the second kind. Then $W_{m,r,q}(0, k + 1) = 0$ for every
natural number $k$.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_zero_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-zero-succ).

## Column-zero recurrence for second-kind (q, r)-Whitney numbers

For complex numbers $m$,
$r$, $q$, let $W_{m,r,q}(i, j)$, for natural numbers $i$ and $j$, denote the $(q, r)$-Whitney
numbers of the second kind. Then for every natural number $n$,
$W_{m,r,q}(n + 1, 0) = r \, W_{m,r,q}(n, 0)$.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_succ_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-succ-zero).

## Triangular recurrence for second-kind (q, r)-Whitney numbers

For all complex numbers
$m$, $r$, $q$ and all natural numbers $n$ and $k$, the $(q, r)$-Whitney numbers of the second kind
$W_{m,r,q}(n, k)$ satisfy

$$
W_{m,r,q}(n + 1, k + 1) = q^k \, W_{m,r,q}(n, k) + (m [k + 1]_q + r) \, W_{m,r,q}(n, k + 1),
$$

where $[j]_q = 1 + q + \dots + q^{j-1}$ is the $q$-integer.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_succ_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-succ-succ).

## First-kind (q, r)-Whitney numbers vanish above the diagonal

For all complex numbers
$m, r, q$ with $q \ne 0$ and all natural numbers $n$ and $k$ with $n < k$, the (q, r)-Whitney
number of the first kind satisfies $w_{m,r,q}(n, k) = 0$.

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst_eq_zero_of_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first-eq-zero-of-lt).

## Second-kind (q, r)-Whitney numbers vanish above the diagonal

For all complex numbers
$m, r, q$ and all natural numbers $n$ and $k$ with $n < k$, the (q, r)-Whitney number of the
second kind satisfies $W_{m,r,q}(n, k) = 0$.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_eq_zero_of_lt`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-eq-zero-of-lt).

## Triangular recurrence for first-kind (q, r)-Whitney numbers, positive column form

Let
$m, r, q$ be complex numbers with $q \ne 0$, write $[j]_q$ for the q-integer of $j$, and write
$w(n, k)$ for the (q, r)-Whitney number of the first kind $w_{m,r,q}(n, k)$. Then for all
natural numbers $n$ and $k$ with $k \ge 1$,

$$w(n + 1, k) = q^{-n} \bigl( w(n, k - 1) - (m [n]_q + r) \, w(n, k) \bigr).$$

Formalized by `MetaMathlibExt.QRWhitney.whitneyFirst_succ_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-first-succ-eq).

## Triangular recurrence for second-kind (q, r)-Whitney numbers, positive column form

Let $m, r, q$ be complex numbers, write $[j]_q$ for the q-integer of $j$, and write $W(n, k)$
for the (q, r)-Whitney number of the second kind $W_{m,r,q}(n, k)$. Then for all natural numbers
$n$ and $k$ with $k \ge 1$,

$$W(n + 1, k) = q^{k - 1} \, W(n, k - 1) + (m [k]_q + r) \, W(n, k).$$

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_succ_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRWhitneyNumbers.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-succ-eq).

## $(q, r)$-Dowling polynomial

Let $R$ be a semiring and let $W(n, k) \in R$ for all
natural numbers $n$ and $k$ (intended to be the $(q, r)$-Whitney numbers of the second kind, but
any family is allowed). For a natural number $n$, the $(q, r)$-Dowling polynomial of $W$ at $n$ is
the polynomial $\sum_{k=0}^{n} W(n, k)\, x^k$ in $R[x]$.

Formalized by `MetaMathlibExt.qrDowlingPolynomial`, a definition declared in [MathlibExt/NumberTheory/QRDowlingPolynomial.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QRDowlingPolynomial.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#qr-dowling-polynomial).

## $(q, r)$-Dowling number

Let $R$ be a semiring and let $W(n, k) \in R$ for all natural
numbers $n$ and $k$. For a natural number $n$, the $(q, r)$-Dowling number of $W$ at $n$ is the
value at $x = 1$ of the $(q, r)$-Dowling polynomial $\sum_{k=0}^{n} W(n, k)\, x^k$ of $W$.

Formalized by `MetaMathlibExt.qrDowlingNumber`, a definition declared in [MathlibExt/NumberTheory/QRDowlingPolynomial.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QRDowlingPolynomial.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#qr-dowling-number).

## $(q, r)$-Dowling numbers as sums of coefficients

Let $R$ be a semiring and let
$W(n, k) \in R$ for all natural numbers $n$ and $k$. For every natural number $n$, the
$(q, r)$-Dowling number of $W$ at $n$ equals $\sum_{k=0}^{n} W(n, k)$.

Formalized by `MetaMathlibExt.qrDowlingNumber_eq_sum`, a theorem declared in [MathlibExt/NumberTheory/QRDowlingPolynomial.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QRDowlingPolynomial.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#qr-dowling-number-eq-sum).

## (q, r)-Whitney numbers of the second kind through q-Stirling numbers

Let
$m, r, q \in \mathbb{C}$ and write $[k + 1]_q = 1 + q + \dots + q^k$. Let $S$ be a complex-valued
function on pairs of natural numbers satisfying the recurrence of the $q$-Stirling numbers of the
second kind: for all $a, k \in \mathbb{N}$, $S(0, 0) = 1$, $S(0, k + 1) = 0$, $S(a + 1, 0) = 0$
and $S(a + 1, k + 1) = q^k S(a, k) + [k + 1]_q \, S(a, k + 1)$. Then for all $a, k \in \mathbb{N}$
the $(q, r)$-Whitney numbers of the second kind satisfy

$$W_{m,r,q}(a, k) = \sum_{j=0}^{a} \binom{a}{j} r^{a-j} m^{j-k} S(j, k),$$

where the exponent $j - k$ is read as $0$ when $j < k$.

Formalized by `MetaMathlibExt.QRWhitney.whitneySecond_eq_sum_qStirlingSecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRDowlingQStirlingExpansion.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRDowlingQStirlingExpansion.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#whitney-second-eq-sum-q-stirling-second).

## Expansion of the (q, r)-Dowling polynomial in q-Stirling numbers

Let
$m, r, q, x \in \mathbb{C}$ and $n \in \mathbb{N}$, and write $[k + 1]_q = 1 + q + \dots + q^k$.
Let $S$ be a complex-valued function on pairs of natural numbers satisfying the recurrence of the
$q$-Stirling numbers of the second kind: for all $a, k \in \mathbb{N}$, $S(0, 0) = 1$,
$S(0, k + 1) = 0$, $S(a + 1, 0) = 0$ and $S(a + 1, k + 1) = q^k S(a, k) + [k + 1]_q \, S(a, k + 1)$.
Let $W_{m,r,q}$ be the $(q, r)$-Whitney numbers of the second kind, and let $D_n(x)$ be the
value at $x$ of the $(q, r)$-Dowling polynomial $\sum_{k=0}^{n} W_{m,r,q}(n, k) \, X^k$. Then

$$D_n(x) = \sum_{k=0}^{n} \binom{n}{k} r^{n-k} \sum_{j=0}^{k} m^{k-j} S(k, j) \, x^j.$$

## Sources

- M. M. Mangontarum, *Some Theorems and Applications of the (q,r)-Whitney Numbers*, Journal of Integer Sequences 20 (2017), Article 17.2.5, theorem equation `genpriv`, lines 782-789, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Mangontarum/mango4.tex>.

Formalized by `MetaMathlibExt.eval_qrDowlingPolynomial_whitneySecond`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRDowlingQStirlingExpansion.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRDowlingQStirlingExpansion.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#eval-qr-dowling-polynomial-whitney-secon).

## (q, r)-Dowling polynomial expansion from the defining recurrences

Let
$q, m, r, x \in \mathbb{C}$ and $n \in \mathbb{N}$, and write $[k + 1]_q = \sum_{i=0}^{k} q^i$.
Let $S$ and $W$ be complex-valued functions on pairs of natural numbers, and let $D(a, y)$ be a
complex-valued function of $a \in \mathbb{N}$ and $y \in \mathbb{C}$, such that for all
$a, k \in \mathbb{N}$ and $y \in \mathbb{C}$: $S(0, 0) = 1$, $S(0, k + 1) = 0$, $S(a + 1, 0) = 0$
and $S(a + 1, k + 1) = q^k S(a, k) + [k + 1]_q \, S(a, k + 1)$ (the recurrence of the
$q$-Stirling numbers of the second kind); $W(0, 0) = 1$, $W(0, k + 1) = 0$,
$W(a + 1, 0) = r^{a + 1}$ and $W(a + 1, k + 1) = q^k W(a, k) + (m [k + 1]_q + r) \, W(a, k + 1)$
(the recurrence of the $(q, r)$-Whitney numbers of the second kind); and
$D(a, y) = \sum_{k=0}^{a} W(a, k) \, y^k$ (the $(q, r)$-Dowling polynomial). Then

$$D(n, x) = \sum_{k=0}^{n} \binom{n}{k} r^{n-k} \sum_{j=0}^{k} m^{k-j} S(k, j) \, x^j.$$

## Sources

- M. M. Mangontarum, *Some Theorems and Applications of the (q,r)-Whitney Numbers*, Journal of Integer Sequences 20 (2017), Article 17.2.5, theorem equation `genpriv`, lines 782-789, <https://cs.uwaterloo.ca/journals/JIS/VOL20/Mangontarum/mango4.tex>.

Formalized by `MetaMathlibExt.q_r_dowling_polynomial_q_stirling_expansion`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/QRDowlingQStirlingExpansion.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/QRDowlingQStirlingExpansion.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html#q-r-dowling-polynomial-q-stirling-expans).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: (q, r)-Whitney and Dowling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/generalized-stirling-numbers/q-r-whitney-and-dowling-numbers)
