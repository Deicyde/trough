---
declaration: section
origin: cited
lean: MetaMathlibExt.qBracket, MetaMathlibExt.IsCarlitzTypeWith, MetaMathlibExt.carlitzEtaPoly, MetaMathlibExt.carlitzBetaPoly, MetaMathlibExt.qBracket_zero, MetaMathlibExt.qBracket_one, MetaMathlibExt.IsCarlitzTypeWith.apply_zero, MetaMathlibExt.carlitzEtaPoly_zero
statement: formalized
---

# Carlitz q-Bernoulli polynomials

32 results, 13 proved and 19 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html).

## The $q$-analogue of a real number

For real numbers $q$ and $x$, the $q$-analogue of $x$
is

$$[x]_q = \frac{q^x - 1}{q - 1},$$

where $q^x$ is the real power; we write $[x]$ when $q$ is fixed. When $q = 1$ the denominator is
$0$ and the quotient is taken to be $0$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 1.

Formalized by `MetaMathlibExt.qBracket`, a definition declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#q-bracket).

## Carlitz-type sequences

For real $q$, a sequence of functions
$T_n : \mathbb{R} \to \mathbb{R}$, $n \ge 0$, is Carlitz-type with associated real sequence
$(a_k)_{k \ge 0}$ if for every natural number $n$ and every real $x$,
$T_n(x) = (q - 1)^{-n} \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} a_k q^{kx}$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Definition in Section 2.1.

Formalized by `MetaMathlibExt.IsCarlitzTypeWith`, a definition declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#is-carlitz-type-with).

## Carlitz $q$-polynomials $\eta_n$

For real $q$, write $[y] = (q^y - 1)/(q - 1)$ and let
$a_0 = 1$ and $a_k = k/[k]$ for $k \ge 1$. For natural $n$ and real $x$, Carlitz's $q$-polynomial
is $\eta_n(x) = (q - 1)^{-n} \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} a_k q^{kx}$; that is,
$(\eta_n)$ is the Carlitz-type sequence with associated sequence $(a_k)$. Its values at $0$ are
written $\eta_n = \eta_n(0)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.1 (examples after Theorem 2.1); after L. Carlitz (1948).

Formalized by `MetaMathlibExt.carlitzEtaPoly`, a definition declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-eta-poly).

## Carlitz $q$-Bernoulli polynomials

For real $q$, write $[y] = (q^y - 1)/(q - 1)$. For
natural $n$ and real $x$, Carlitz's $q$-Bernoulli polynomial is
$\beta_n(x) = (q - 1)^{-n} \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} \frac{k + 1}{[k + 1]} q^{kx}$;
that is, $(\beta_n)$ is the Carlitz-type sequence with associated sequence
$a_k = (k + 1)/[k + 1]$. The Carlitz $q$-Bernoulli numbers are $\beta_n = \beta_n(0)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.1 (examples after Theorem 2.1); after L. Carlitz (1948).

Formalized by `MetaMathlibExt.carlitzBetaPoly`, a definition declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-beta-poly).

## The $q$-analogue of $0$ is $0$

For every real number $q$, $[0]_q = 0$, where
$[x]_q = (q^x - 1)/(q - 1)$ is the $q$-analogue of a real number $x$, taken to be $0$ when
$q = 1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 1.

Formalized by `MetaMathlibExt.qBracket_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#q-bracket-zero).

## The $q$-number of $1$

For real $q \ne 1$, the $q$-analogue $[x] = (q^x - 1)/(q - 1)$
satisfies $[1] = 1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 1.

Formalized by `MetaMathlibExt.qBracket_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#q-bracket-one).

## The zeroth term of a Carlitz-type sequence

Let $q$ be a real number. If $(T_n)$ is a
Carlitz-type $q$-polynomial sequence with associated real sequence $(a_k)$, then $T_0(x) = a_0$
for every real $x$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Definition in Section 2.1.

Formalized by `MetaMathlibExt.IsCarlitzTypeWith.apply_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#apply-zero).

## The zeroth Carlitz $q$-polynomial

For all real $q$ and $x$, Carlitz's $q$-polynomial
$\eta_0(x)$ equals $1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.1.

Formalized by `MetaMathlibExt.carlitzEtaPoly_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-eta-poly-zero).

## Carlitz's initial value $\eta_1 = 0$

For real $q \ne 1$, the value $\eta_1 = \eta_1(0)$ of
Carlitz's $q$-polynomial $\eta_1$ at $0$ equals $0$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Sections 1 and 2.1.

Formalized by `MetaMathlibExt.carlitzEtaPoly_one_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-eta-poly-one-zero).

## The zeroth Carlitz $q$-Bernoulli polynomial

For real $q \ne 1$ and every real $x$, the
Carlitz $q$-Bernoulli polynomial $\beta_0(x)$ equals $1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.1.

Formalized by `MetaMathlibExt.carlitzBetaPoly_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-beta-poly-zero).

## Characterization of Carlitz-type sequences

Let $q > 0$ with $q \ne 1$ be real and write
$[x] = (q^x - 1)/(q - 1)$. A sequence of functions $T_n : \mathbb{R} \to \mathbb{R}$ is
Carlitz-type with some associated real sequence $(a_k)$ if and only if for every natural $n$ and
every real $x$, $T_n(x) = \sum_{k=0}^{n} \binom{n}{k} T_k(0) q^{kx} [x]^{n-k}$.

This is a $q$-analogue of the characterization of Appell sequences.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.isCarlitzType_iff_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#is-carlitz-type-iff-sum-choose).

## Binomial inversion

For real sequences $(u_n)$ and $(v_n)$, the identities
$u_n = \sum_{k=0}^{n} \binom{n}{k} v_k$ hold for all natural numbers $n$ if and only if the
identities $v_n = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} u_k$ hold for all natural numbers $n$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.binomial_inversion_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#binomial-inversion-iff).

## Sums of $q^{rk} (k)^n$ via Carlitz-type sequences

Let $q > 0$ with $q \ne 1$, let
$[x] = (q^x - 1)/(q - 1)$, and let $r \ge 1$ be a natural number. Let $S_m(x)$
($m \in \mathbb{N}$, $x \in \mathbb{R}$) be the Carlitz-type sequence with associated sequence
$a_k = 1/((q - 1)[k + r])$, that is,

$$S_m(x) = (q - 1)^{-m} \sum_{k=0}^{m} (-1)^{m-k} \binom{m}{k} a_k q^{kx}$$

for all $m$ and all real $x$. Then for all natural numbers $n$ and $N$,

$$\sum_{k=0}^{N-1} q^{rk} [k]^n = q^{rN} S_n(N) - S_n(0),$$

where $0^0 = 1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.3.

Stated but not proved: `MetaMathlibExt.sum_qpow_mul_qBracket_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#sum-qpow-mul-q-bracket-pow).

## Sums of $q^{rk} (k)^{n-d}$ via Carlitz-type sequences

Let $q > 0$ with $q \ne 1$, let
$[x] = (q^x - 1)/(q - 1)$, and let $r$, $d$ and $n$ be natural numbers with $r \ge 1$, $d \le r$
and $d \le n$. Write $(k)_d = k(k-1)\cdots(k-d+1)$ for the falling factorial (with $(k)_0 = 1$).
Let $T_m(x)$ ($m \in \mathbb{N}$, $x \in \mathbb{R}$) be the Carlitz-type sequence with associated
sequence $a_k = (q - 1)^{d-1} (k)_d / [k + r - d]$, that is,

$$T_m(x) = (q - 1)^{-m} \sum_{k=0}^{m} (-1)^{m-k} \binom{m}{k} a_k q^{kx}$$

for all $m$ and all real $x$. Then for every natural number $N$,

$$\sum_{k=0}^{N-1} q^{rk} [k]^{n-d} = \frac{q^{(r-d)N} T_n(N) - T_n(0)}{(n)_d},$$

where $0^0 = 1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.4.

Stated but not proved: `MetaMathlibExt.sum_qpow_mul_qBracket_pow_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#sum-qpow-mul-q-bracket-pow-sub).

## Symbolic recurrence for Carlitz-type sequences

Let $q > 0$ with $q \ne 1$, write
$[x] = (q^x - 1)/(q - 1)$, let $r$ be a natural number, let $P$ be a real polynomial and let
$(a_k)$ be a real sequence with $[k + r]\, a_k = P(k)$ for every natural number $k$. If $(T_n)$ is
a Carlitz-type sequence with associated sequence $(a_k)$ and $t_n = T_n(0)$, then for every natural
number $n$ greater than the degree of $P$ (taken to be $0$ when $P = 0$),
$q^r \sum_{j=0}^{n} \binom{n}{j} q^j t_j = t_n$, which in umbral notation reads
$q^r (q t + 1)^n = t^n$.

The hypothesis $[k + r]\, a_k = P(k)$ encodes $a_k = P(k)/[k + r]$; for $r = 0$ it forces
$P(0) = 0$ and leaves $a_0$ free.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.5.

Stated but not proved: `MetaMathlibExt.carlitzType_symbolic_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-type-symbolic-recurrence).

## Closure properties of Carlitz-type sequences

Let $q > 0$ with $q \ne 1$ be real, and let
$(T_n)$ be a Carlitz-type sequence of functions $\mathbb{R} \to \mathbb{R}$ with associated real
sequence $(a_k)$. Then:
(i) $n q^x T_{n-1}(x)$ is Carlitz-type with associated sequence $(q - 1) k a_{k-1}$;
(ii) if $a_0 = 0$, then $q^{-x} T_{n+1}(x)/(n + 1)$ is Carlitz-type with associated sequence
$a_{k+1}/((q - 1)(k + 1))$;
(iii) $q^{-x} (T_n(x) + (q - 1) T_{n+1}(x))$ is Carlitz-type with associated sequence $a_{k+1}$;
(iv) $n (T_{n-1}(x) + (q - 1) T_n(x))$ is Carlitz-type with associated sequence $(q - 1) k a_k$.
At $n = 0$ the functions in (i) and (iv) are $0$, and at $k = 0$ the associated sequence in (i)
is $0$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Proposition 2.6.

Stated but not proved: `MetaMathlibExt.isCarlitzTypeWith_closure` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#is-carlitz-type-with-closure).

## Sums of $q^k (k)^{n-1}$ via Carlitz's $q$-polynomials $\eta_n$

Let $q > 0$ with $q \ne 1$,
let $[x] = (q^x - 1)/(q - 1)$, and let $\eta_n(x)$ be Carlitz's $q$-polynomials, with
$\eta_n = \eta_n(0)$. Then for every natural number $n \ge 1$ and every natural number $N$,

$$\sum_{k=0}^{N-1} q^k [k]^{n-1} = \frac{\eta_n(N) - \eta_n}{n},$$

where $0^0 = 1$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Corollary 2.7.

Stated but not proved: `MetaMathlibExt.sum_qpow_mul_qBracket_pow_eq_carlitzEta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#sum-qpow-mul-q-bracket-pow-eq-carlitz-et).

## Weighted $q$-power sums via Carlitz's $q$-Bernoulli polynomials

Let $q > 0$ with
$q \ne 1$, let $[x] = (q^x - 1)/(q - 1)$, and let $\beta_n(x)$ be Carlitz's $q$-Bernoulli
polynomials, with $\beta_n = \beta_n(0)$. Then for all natural numbers $n$ and $N$,

$$n \sum_{k=0}^{N-1} q^{2k} [k]^{n-1} + (q - 1) \sum_{k=0}^{N-1} q^k [k]^n =
q^N \beta_n(N) - \beta_n,$$

where $0^0 = 1$, and the first term is $0$ when $n = 0$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Corollary 2.8.

Stated but not proved: `MetaMathlibExt.sum_qpow_mul_qBracket_pow_eq_carlitzBeta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#sum-qpow-mul-q-bracket-pow-eq-carlitz-be).

## Extended Carlitz $q$-Bernoulli polynomials

For real $q$, the extended Carlitz
$q$-Bernoulli polynomials $\beta_n^{(r)}(x)$, indexed by natural numbers $r$ and $n$ and evaluated
at real $x$, are defined by recursion on $r$: $\beta_n^{(0)}(x) = \eta_n(x)$ is Carlitz's
$q$-polynomial, and
$\beta_n^{(r+1)}(x) = q^{-x} \bigl(\beta_n^{(r)}(x) + (q - 1) \beta_{n+1}^{(r)}(x)\bigr)$.
The extended Carlitz $q$-Bernoulli numbers are $\beta_n^{(r)} = \beta_n^{(r)}(0)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.2 (definition of the extended family).

Formalized by `MetaMathlibExt.extendedCarlitzBetaPoly`, a definition declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#extended-carlitz-beta-poly).

## Extended Carlitz $q$-Bernoulli polynomials of order zero

For every real $q$, natural number
$n$ and real $x$, the extended Carlitz $q$-Bernoulli polynomial $\beta_n^{(0)}(x)$ equals Carlitz's
$q$-polynomial $\eta_n(x)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.2.

Formalized by `MetaMathlibExt.extendedCarlitzBetaPoly_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#extended-carlitz-beta-poly-zero).

## Recurrence for the extended Carlitz $q$-Bernoulli polynomials

For every real $q$, natural
numbers $r$ and $n$, and real $x$, the extended Carlitz $q$-Bernoulli polynomials satisfy
$\beta_n^{(r+1)}(x) = q^{-x} \bigl(\beta_n^{(r)}(x) + (q - 1) \beta_{n+1}^{(r)}(x)\bigr)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Section 2.2.

Formalized by `MetaMathlibExt.extendedCarlitzBetaPoly_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#extended-carlitz-beta-poly-succ).

## Closed forms for the extended Carlitz $q$-Bernoulli polynomials

Let $q > 0$ with
$q \ne 1$ be real, write $[x] = (q^x - 1)/(q - 1)$, let $r$ be a natural number, and let
$\beta_n^{(r)}(x)$ be the extended Carlitz $q$-Bernoulli polynomials. Put $a_k = (k + r)/[k + r]$
for natural $k$ with $k + r \ne 0$, and $a_0 = 1$ if $r = 0$. Then:
(i) for every natural $n$ and real $x$,
$\beta_n^{(r)}(x) = (q - 1)^{-n} \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} a_k q^{kx}$;
(ii) for every natural $n$ and real $x$,
$\beta_n^{(r)}(x) = \sum_{k=0}^{n} \binom{n}{k} \beta_k^{(r)}(0) q^{kx} [x]^{n-k}$;
(iii) for every natural $n \ge 2$,
$q^r \sum_{j=0}^{n} \binom{n}{j} q^j \beta_j^{(r)}(0) = \beta_n^{(r)}(0)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Proposition 2.9.

Stated but not proved: `MetaMathlibExt.extendedCarlitzBetaPoly_closed_forms` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#extended-carlitz-beta-poly-closed-forms).

## Weighted $q$-power sums via the extended Carlitz $q$-Bernoulli polynomials

Let $q > 0$
with $q \ne 1$, let $[x] = (q^x - 1)/(q - 1)$, and let $\beta_n^{(r)}(x)$ be the extended Carlitz
$q$-Bernoulli polynomials, with $\beta_n^{(r)} = \beta_n^{(r)}(0)$. Then for all natural numbers
$r$, $n$ and $N$,

$$n \sum_{k=0}^{N-1} q^{(r+1)k} [k]^{n-1} + (q - 1) r \sum_{k=0}^{N-1} q^{rk} [k]^n =
q^{rN} \beta_n^{(r)}(N) - \beta_n^{(r)},$$

where $0^0 = 1$, and the first term is $0$ when $n = 0$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.10.

Stated but not proved: `MetaMathlibExt.sum_qpow_mul_qBracket_pow_eq_extendedCarlitzBeta` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#sum-qpow-mul-q-bracket-pow-eq-extended-c).

## Series for the extended Carlitz $q$-Bernoulli numbers

Let $0 < q < 1$, write
$[x] = (q^x - 1)/(q - 1)$, and let $\beta_n^{(r)} = \beta_n^{(r)}(0)$ be the extended Carlitz
$q$-Bernoulli numbers. For every natural number $n \ge 1$,
$\beta_n^{(0)} = -n \sum_{k=0}^{\infty} q^k [k]^{n-1} + (1 - q)^{-n}$, and for every natural number
$r \ge 1$,

$$
\beta_n^{(r)} = -n \sum_{k=0}^{\infty} q^{(r+1)k} [k]^{n-1} +
r (1 - q) \sum_{k=0}^{\infty} q^{rk} [k]^n.
$$

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.11.

Stated but not proved: `MetaMathlibExt.extendedCarlitzBeta_eq_tsum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#extended-carlitz-beta-eq-tsum).

## Bernoulli numbers as a limit as $q \to 1^-$

Let $r \ge 1$ and $n \ge 1$ be integers and,
for real $q$ and $x$, write $[x] = (q^x - 1)/(q - 1)$. Then, as $q$ tends to $1$ from below,

$$\sum_{k=0}^{\infty} \left(r q^{rk} - (n + r) q^{(r+1)k}\right) [k]^{n-1} \to B_n,$$

where $B_n$ is the $n$-th Bernoulli number, with the convention $B_1 = -1/2$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Corollary 2.12.

Stated but not proved: `MetaMathlibExt.tendsto_tsum_qBracket_bernoulli` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#tendsto-tsum-q-bracket-bernoulli).

## Sums of $q^{ir}$ times $q$-falling factorials

Let $q > 0$ with $q \ne 1$, let
$[x] = (q^x - 1)/(q - 1)$, and write $[x]_m = [x][x-1]\cdots[x-m+1]$ for the $q$-falling factorial
(with $[x]_0 = 1$). Then for all natural numbers $r \ge 1$, $k$ and $N$,

$$\sum_{i=0}^{N-1} q^{ir} [i]_k = \left(\sum_{\ell=0}^{r-1}
\frac{q^{(r-\ell-1)N + (\ell+1)k} \, [r-1]_\ell}{[k+r]_{\ell+1}}\right) [N]_{k+1}.$$

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Proposition 2.14.

Stated but not proved: `MetaMathlibExt.sum_qpow_mul_qFalling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#sum-qpow-mul-q-falling).

## Limit of the $q$-power-sum interpolant at $0$: first closed form

Let $q > 0$ with
$q \ne 1$, let $r \ge 1$ and $k \ge 0$ be integers, and for real $x$ write
$[x] = (q^x - 1)/(q - 1)$, $[x]_m = [x][x-1]\cdots[x-m+1]$ (with $[x]_0 = 1$) and
$[k]! = [1][2]\cdots[k]$. Let $P$ be a real polynomial such that
$P(q^N) = q^{k(k-1)/2} \sum_{i=0}^{N-1} q^{ir} [i]_k$ for every positive integer $N$. Then
$P(q^x)/[x]$ tends, as $x \to 0$ with $x \ne 0$, to

$$(-1)^k [k]! \sum_{i=0}^{r-1} \frac{q^{ik} [r-1]_i}{[k+r]_{i+1}}.$$

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Corollary 2.15.

Stated but not proved: `MetaMathlibExt.tendsto_qInterpolant_div_qBracket` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#tendsto-q-interpolant-div-q-bracket).

## Partial fraction decomposition of $q^{kx}$ over a $q$-falling factorial

Let $q > 0$ with
$q \ne 1$, let $[x] = (q^x - 1)/(q - 1)$, write $[m]! = [1][2]\cdots[m]$ (with $[0]! = 1$) and
$\binom{k}{i}_q = [k]!/([i]!\,[k-i]!)$. Then for every natural number $k$ and every real number
$x \notin \{0, 1, \dots, k\}$,

$$\frac{q^{kx}}{[x][x-1]\cdots[x-k]} = \frac{1}{[k]!} \sum_{i=0}^{k} (-1)^{k-i} \binom{k}{i}_q
\frac{q^{(k^2+k)/2 + (i^2-i)/2}}{[x-i]}.$$

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Proposition 2.16.

Stated but not proved: `MetaMathlibExt.qpow_div_qFalling_partial_fractions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#qpow-div-q-falling-partial-fractions).

## Second closed form of a limit of $q$-interpolated falling-factorial sums

Let $q > 0$
with $q \ne 1$, let $[x] = (q^x - 1)/(q - 1)$, write $[x]_m = [x][x-1]\cdots[x-m+1]$ and
$[m]! = [1][2]\cdots[m]$ (both equal to $1$ when $m = 0$), and let $r \ge 1$ and $k$ be natural
numbers. Let $P$ be a real polynomial such that

$$P(q^N) = q^{k(k-1)/2} \sum_{i=0}^{N-1} q^{ir} [i]_k$$

for every integer $N \ge 1$. Then, as $x \to 0$ through real numbers $x \ne 0$, $P(q^x)/[x]$
tends to

$$g_r(q, k) = (-1)^k [k]! \, [r-1]! \, q^{1-r} \sum_{i=0}^{r-1}
\frac{(q-1)^i \, q^{i(i+1)/2 - i(r-1)}}{[r-1-i]! \, [k+i+1]}.$$

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Proposition 2.17.

Stated but not proved: `MetaMathlibExt.tendsto_qInterpolant_div_qBracket'` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#tendsto-q-interpolant-div-q-bracket-2).

## Extended Carlitz $q$-Bernoulli numbers via $q$-Stirling numbers

Let $q > 0$ with
$q \ne 1$ be real, write $[x] = (q^x - 1)/(q - 1)$ for real $x$, $[x]_m = [x][x-1] \cdots [x-m+1]$
(with $[x]_0 = 1$) and $[m]! = [1][2] \cdots [m]$ (with $[0]! = 1$), and let $\beta_n^{(r)}(x)$
be the extended Carlitz $q$-Bernoulli polynomials, with numbers $\beta_n^{(r)} = \beta_n^{(r)}(0)$.
Let $r \ge 1$ and $n$ be natural numbers, and let $S(m, k)$ be real numbers such that
$[x]^m = \sum_{k=0}^{m} q^{k(k-1)/2} S(m, k) [x]_k$ for every natural number $m$ and every real
$x$ (the defining identity of Carlitz's $q$-Stirling numbers of the second kind). For natural $k$
put $\varphi_r(q, k) = (-1)^k [k]! \sum_{i=0}^{r-1} q^{ik} [r-1]_i / [k+r]_{i+1}$. Then

$$\beta_n^{(r)} = \sum_{k=0}^{n} \varphi_r(q, k) S(n, k),$$

and for every natural number $k$,

$$
\varphi_r(q, k) = (-1)^k [k]! \, [r-1]! \, q^{1-r} \sum_{i=0}^{r-1}
\frac{(q-1)^i q^{i(i+1)/2 - i(r-1)}}{[r-1-i]! \, [k+i+1]}.
$$

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Theorem 2.13.

Stated but not proved: `MetaMathlibExt.extendedCarlitzBeta_eq_sum_qStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#extended-carlitz-beta-eq-sum-q-stirling).

## Carlitz $q$-Bernoulli numbers via $q$-Stirling numbers

Let $q > 0$ with $q \ne 1$, write
$[x] = (q^x - 1)/(q - 1)$, $[x]_k = [x][x - 1] \cdots [x - k + 1]$ and $[k]! = [1][2] \cdots [k]$
(empty products are $1$), and let $\beta_n = \beta_n(0)$ be Carlitz's $q$-Bernoulli numbers. If
real numbers $S_q(m,k)$ satisfy $[x]^m = \sum_{k=0}^{m} q^{k(k-1)/2} S_q(m,k) [x]_k$ for every
natural number $m$ and every real $x$ (this is the defining identity of Carlitz's $q$-Stirling
numbers of the second kind), then for every natural number $n$,
$\beta_n + q \beta_{n+1} = \sum_{k=0}^{n} (-1)^k \frac{[k]!}{[k+2]} S_q(n,k)$.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Corollary 2.18.

Stated but not proved: `MetaMathlibExt.carlitzBeta_add_mul_succ_eq_sum_qStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 398](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L398). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#carlitz-beta-add-mul-succ-eq-sum-q-stirl).

## Sum of consecutive Bernoulli numbers via Stirling numbers

For every natural number $n$,
$B_n + B_{n+1} = \sum_{k=0}^{n} (-1)^k \frac{k!}{k+2} S(n,k)$, where $B_n$ are the Bernoulli numbers
with $B_1 = -1/2$ (generating function $t/(e^t - 1)$, the paper's convention) and $S(n,k)$ are the
Stirling numbers of the second kind.

## Sources

- Bakir Farhi, *q-Analogues of Sums of Consecutive Powers of Natural Numbers and Extended Carlitz q-Bernoulli Numbers and Polynomials*, INTEGERS 26 (2026), Article A85, Corollary 2.19.

Stated but not proved: `MetaMathlibExt.bernoulli_add_bernoulli_succ_eq_sum_stirlingSecond` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/CarlitzTypeQPolynomialsWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html#bernoulli-add-bernoulli-succ-eq-sum-stir).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Carlitz q-Bernoulli polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/carlitz-q-bernoulli-polynomials)
