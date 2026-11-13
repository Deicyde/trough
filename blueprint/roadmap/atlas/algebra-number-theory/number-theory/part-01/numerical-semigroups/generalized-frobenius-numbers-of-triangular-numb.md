---
declaration: section
origin: cited
lean: MetaMathlibExt.triangularTriple, MetaMathlibExt.triangularTriple_one, MetaMathlibExt.triangularFrobeniusBound, MetaMathlibExt.triangularFrobeniusBound_zero, MetaMathlibExt.triangularFrobeniusX, MetaMathlibExt.triangularFrobeniusY, MetaMathlibExt.triangularFrobeniusXY_five, MetaMathlibExt.isGenFrobeniusNumber_cons_mul_of_gcd
statement: formalized
---

# Generalized Frobenius numbers of triangular numbers

17 results, 7 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html).

## Three consecutive triangular numbers

For a natural number $n$, the triangular triple of
$n$ is $(t_n, t_{n+1}, t_{n+2})$, where $t_m = m(m+1)/2$ is the $m$-th triangular number.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction.

Formalized by `MetaMathlibExt.triangularTriple`, a definition declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-triple).

## Triangular triple at $n = 1$

The three consecutive triangular numbers
$(t_1, t_2, t_3)$, where $t_m = m(m+1)/2$, are $(1, 3, 6)$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction.

Formalized by `MetaMathlibExt.triangularTriple_one`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-triple-one).

## Triangular Frobenius threshold

For natural numbers $n$ and $s$, the threshold $N_s$ is
the integer $N_s^{\mathrm{even}} = 6\lfloor\sqrt{s+1}\rfloor - 6$ when $n$ is even and
$N_s^{\mathrm{odd}} = 6\lfloor(\sqrt{4s+5} - 1)/2\rfloor - 3$ when $n$ is odd.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, equation (4).

Formalized by `MetaMathlibExt.triangularFrobeniusBound`, a definition declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-frobenius-bound).

## Triangular Frobenius threshold at $s = 0$

At $s = 0$ the triangular Frobenius threshold
$N_s$ equals $0$ for $n = 0$ (the even case, $N_0^{\mathrm{even}} = 6\lfloor\sqrt{1}\rfloor - 6$)
and $-3$ for $n = 1$ (the odd case, $N_0^{\mathrm{odd}} = 6\lfloor(\sqrt{5} - 1)/2\rfloor - 3$).

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, equation (4).

Formalized by `MetaMathlibExt.triangularFrobeniusBound_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-frobenius-bound-zero).

## The parameter $x_s$ of the triangular Frobenius formula

For natural numbers $n$, $k$
and $i$, let $x$ be $i$ if $i \le k$ and $i - k - 1$ if $i > k$ when $n$ is even, and $2i$ if
$i \le k$ and $2(i - k) - 1$ if $i > k$ when $n$ is odd. For $s = k(k+1) + i$ with
$0 \le i \le 2k+1$ this is the integer $x_s$ (written $x_s^{\mathrm{even}}$ or
$x_s^{\mathrm{odd}}$ by the parity of $n$).

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Definition 1.

Formalized by `MetaMathlibExt.triangularFrobeniusX`, a definition declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-frobenius-x).

## The parameter $y_s$ of the triangular Frobenius formula

For natural numbers $n$, $k$
and $i$, let $y$ be $2(k - i)$ if $i \le k$ and $4k + 3 - 2i$ if $i > k$ when $n$ is even, and
$k - i$ if $i \le k$ and $2k + 1 - i$ if $i > k$ when $n$ is odd, where a difference that would
be negative is replaced by $0$ (this happens only for $i > 2k + 1$). For $s = k(k+1) + i$ with
$0 \le i \le 2k+1$ this is the integer $y_s$ (written $y_s^{\mathrm{even}}$ or
$y_s^{\mathrm{odd}}$ by the parity of $n$).

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Definition 1.

Formalized by `MetaMathlibExt.triangularFrobeniusY`, a definition declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-frobenius-y).

## Triangular Frobenius parameters at $s = 5$

Take $k = 1$ and $i = 3$, so that
$s = k(k+1) + i = 5$. Then $(x_s, y_s) = (1, 1)$ for $n = 0$ (the even case) and
$(x_s, y_s) = (3, 0)$ for $n = 1$ (the odd case).

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Definition 1 and Table 2.

Formalized by `MetaMathlibExt.triangularFrobeniusXY_five`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#triangular-frobenius-xy-five).

## Beck–Kifer reduction by a common factor of all generators but the first

Let $K \ge 2$,
let $a_1$ and $\ell$ be positive integers, and let $a'_2, \dots, a'_K$ be positive integers with
$\gcd(a'_2, \dots, a'_K) = 1$ such that $\gcd(a_1, \ell a'_2, \dots, \ell a'_K) = 1$. Let $s$ be a
natural number. If $g'$ is the generalized Frobenius number $g(a_1, a'_2, \dots, a'_K; s)$, then
$\ell g' + a_1(\ell - 1)$ is the generalized Frobenius number
$g(a_1, \ell a'_2, \dots, \ell a'_K; s)$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Lemma 1, quoted from Beck and Kifer, Lemma 4.

Stated but not proved: `MetaMathlibExt.isGenFrobeniusNumber_cons_mul_of_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#is-gen-frobenius-number-cons-mul-of-gcd).

## Splitting off the first generator of the reduced triangular triple

For a natural number
$r$ write $t_r = r(r+1)/2$, and for an integer $m$ and natural numbers $a_1, \dots, a_k$ let
$d(m; a_1, \dots, a_k)$ be the number of representations of $m$ by $(a_1, \dots, a_k)$. Let
$n \ge 1$, $d_1 = \gcd(t_{n+1}, t_{n+2})$, $a = t_{n+1}/d_1$ and $b = t_{n+2}/d_1$. Then for every
natural number $m$,

$$d(m; t_n, a, b) = \sum_{j=0}^{\lfloor m/t_n \rfloor} d(m - j t_n; a, b).$$

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Lemma 2.

Stated but not proved: `MetaMathlibExt.frobeniusRepCount_triangular_reduced_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#frobenius-rep-count-triangular-reduced-e).

## Representation counts between consecutive two-generator Frobenius numbers

Let $a$ and $b$
be coprime positive integers. For a natural number $r$ let $g(a, b; r)$ be the generalized
Frobenius number of $(a, b)$ at $r$, and for an integer $m$ let $d(m; a, b)$ be the number of
representations of $m$ by $(a, b)$. Let $i$ and $s$ be natural numbers, let $c$ be a positive
integer divisible by $a$ or by $b$, and let $j$ be an integer. Then $d(g(a, b; s) + jc; a, b) = i$
if and only if $g(a, b; s) + jc \le g(a, b; i)$ and, in case $i \ge 1$, also
$g(a, b; i - 1) < g(a, b; s) + jc$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Lemma 3, quoted from Subwattanachai, *Generalized Frobenius number of three variables*.

Stated but not proved: `MetaMathlibExt.frobeniusRepCount_pair_eq_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#frobenius-rep-count-pair-eq-iff).

## Representation counts above a shifted two-generator Frobenius number

Let $a < b$ be
coprime positive integers, let $s$ and $k$ be natural numbers, let $g$ be the generalized Frobenius
number $g(a, b; s)$, and for an integer $m$ let $d(m; a, b)$ be the number of representations of
$m$ by $(a, b)$. If $m$ is an integer with $m > g + ka$, then for every natural number $j$,
$d(m - ja; a, b) \ge d(g + (k - j)a; a, b)$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Lemma 4, quoted from Subwattanachai, *Generalized Frobenius number of three variables*.

Stated but not proved: `MetaMathlibExt.frobeniusRepCount_pair_sub_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#frobenius-rep-count-pair-sub-ge).

## Representation count of the reduced triangular triple at a shifted Frobenius number

For a
natural number $r$ write $t_r = r(r+1)/2$. Let $n$, $k$, $i$ be natural numbers with $i \le 2k + 1$
and put $s = k(k+1) + i$. Let $N_s = 6\lfloor\sqrt{s+1}\rfloor - 6$ if $n$ is even and
$N_s = 6\lfloor(\sqrt{4s+5} - 1)/2\rfloor - 3$ if $n$ is odd, and suppose $n > N_s$. For even $n$
let $(x_s, y_s) = (i, 2(k - i))$ if $i \le k$ and $(x_s, y_s) = (i - k - 1, 4k - 2i + 3)$ if
$i > k$; for odd $n$ let $(x_s, y_s) = (2i, k - i)$ if $i \le k$ and
$(x_s, y_s) = (2(i - k) - 1, 2k - i + 1)$ if $i > k$. Put $d_1 = \gcd(t_{n+1}, t_{n+2})$,
$a = t_{n+1}/d_1$ and $b = t_{n+2}/d_1$. If $g$ is the generalized Frobenius number
$g(a, b; x_s)$, then the number of representations of $g + y_s t_n$ by $(t_n, a, b)$ is $s$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Lemma 5.

Stated but not proved: `MetaMathlibExt.frobeniusRepCount_triangular_reduced_at_pair_frobenius` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#frobenius-rep-count-triangular-reduced-a).

## Generalized Frobenius numbers of three consecutive triangular numbers

For a natural number
$j$ write $t_j = j(j+1)/2$. Let $n$ and $s$ be natural numbers, let $r = \lfloor\sqrt{s}\rfloor$,
let $\delta_s = 1$ if $s \ge r^2 + r$ and $\delta_s = 0$ otherwise, and put
$q_s = 2r + 2 + \delta_s$ and $c_s = s - r^2 - \delta_s r$. Suppose that
$n > 6\lfloor\sqrt{s+1}\rfloor - 6$ if $n$ is even and $n > 6\lfloor(\sqrt{4s+5} - 1)/2\rfloor - 3$
if $n$ is odd. Then the generalized Frobenius number $g$ of $(t_n, t_{n+1}, t_{n+2})$ at $s$ exists
and satisfies $4(g + 1) = (n+1)(n+2)(q_s n + 6c_s)$ if $n$ is even and
$4(g + 1) = (n+1)(n+2)(q_s n + 6c_s - 3\delta_s)$ if $n$ is odd.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Theorem 1.

Stated but not proved: `MetaMathlibExt.isGenFrobeniusNumber_triangularTriple` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#is-gen-frobenius-number-triangular-tripl).

## Komatsu's conjecture on generalized Frobenius numbers of triangular triples

For a natural
number $r$ write $t_r = r(r+1)/2$. Let $n$ and $s$ be natural numbers, let
$N_{s+1} = 6\lfloor\sqrt{s+2}\rfloor - 6$ if $n$ is even and
$N_{s+1} = 6\lfloor(\sqrt{4s+9} - 1)/2\rfloor - 3$ if $n$ is odd, and suppose $n > N_{s+1}$. Let
$g_s$ and $g_{s+1}$ be the generalized Frobenius numbers of $(t_n, t_{n+1}, t_{n+2})$ at $s$ and at
$s + 1$, and put $P = (n+1)(n+2)$. Then: (i) if $s + 1$ is neither $k^2$ nor $k(k+1)$ for any
integer $k \ge 1$, then $4(g_{s+1} - g_s) = 6P$; (ii) if $n$ is even and $s + 1 = k^2$ or
$s + 1 = k(k+1)$ for an integer $k \ge 1$, then $4(g_{s+1} - g_s) = (n - 6k + 6)P$; (iii) if $n$ is
odd and $k \ge 1$ is an integer, then $4(g_{s+1} - g_s) = (n - 6k + 9)P$ when $s + 1 = k^2$, and
$4(g_{s+1} - g_s) = (n - 6k + 3)P$ when $s + 1 = k(k+1)$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Theorem 2.

Stated but not proved: `MetaMathlibExt.isGenFrobeniusNumber_triangularTriple_succ_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#is-gen-frobenius-number-triangular-tripl-2).

## Generalized Frobenius numbers of triangular triples in parametrized form

For a natural
number $r$ write $t_r = r(r+1)/2$. Let $n$, $k$, $i$ be natural numbers with $i \le 2k + 1$ and
put $s = k(k+1) + i$. Suppose that $s \le 2$ or that $s$ is neither $m^2$ nor $m(m+1)$ for any
integer $m \ge 1$. Let $N_s = 6\lfloor\sqrt{s+1}\rfloor - 6$ if $n$ is even and
$N_s = 6\lfloor(\sqrt{4s+5} - 1)/2\rfloor - 3$ if $n$ is odd, and suppose $n \ge 2$ and $n > N_s$.
For even $n$ let $(x_s, y_s) = (i, 2(k - i))$ if $i \le k$ and
$(x_s, y_s) = (i - k - 1, 4k - 2i + 3)$ if $i > k$; for odd $n$ let $(x_s, y_s) = (2i, k - i)$ if
$i \le k$ and $(x_s, y_s) = (2(i - k) - 1, 2k - i + 1)$ if $i > k$. Then the generalized Frobenius
number $g$ of $(t_n, t_{n+1}, t_{n+2})$ at $s$ exists and satisfies
$4(g + 1) = (n+1)(n+2)\bigl((2x_s + y_s + 3)n + 6x_s\bigr)$ if $n$ is even and
$4(g + 1) = (n+1)(n+2)\bigl((x_s + 2y_s + 3)n + 3(x_s - 1)\bigr)$ if $n$ is odd.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Theorem 3.

Stated but not proved: `MetaMathlibExt.isGenFrobeniusNumber_triangularTriple_of_xy` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#is-gen-frobenius-number-triangular-tripl-3).

## Generalized Frobenius numbers of the reduced triangular triple

For a natural number $r$
write $t_r = r(r+1)/2$. Let $n$, $k$, $i$ be natural numbers with $i \le 2k + 1$ and put
$s = k(k+1) + i$. Let $N_s = 6\lfloor\sqrt{s+1}\rfloor - 6$ if $n$ is even and
$N_s = 6\lfloor(\sqrt{4s+5} - 1)/2\rfloor - 3$ if $n$ is odd, and suppose $n > N_s$. For even $n$
let $(x_s, y_s) = (i, 2(k - i))$ if $i \le k$ and $(x_s, y_s) = (i - k - 1, 4k - 2i + 3)$ if
$i > k$; for odd $n$ let $(x_s, y_s) = (2i, k - i)$ if $i \le k$ and
$(x_s, y_s) = (2(i - k) - 1, 2k - i + 1)$ if $i > k$. Put $d_1 = \gcd(t_{n+1}, t_{n+2})$,
$a = t_{n+1}/d_1$ and $b = t_{n+2}/d_1$. Then $(x_s + 1)ab - a - b$ is the generalized Frobenius
number $g(a, b; x_s)$, and $(x_s + 1)ab - b - a + y_s t_n$ is the generalized Frobenius number
$g(t_n, a, b; s)$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Theorem 4.

Stated but not proved: `MetaMathlibExt.isGenFrobeniusNumber_triangular_reduced` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#is-gen-frobenius-number-triangular-reduc).

## Explicit generalized Frobenius numbers of triangular triples at levels 11 to 20

For a
natural number $r$ write $t_r = r(r+1)/2$. For a natural number $n$, a natural number $s$ and an
integer $L$, say that $s$ has value $L$ when the generalized Frobenius number $g$ of
$(t_n, t_{n+1}, t_{n+2})$ at $s$ exists and satisfies $4(g + 1) = (n+1)(n+2)L$. Then for every
natural number $n$: $11$ has value $8n + 12$ if $n = 12$ or $n \ge 14$; $12$ has value $9n$ for
even $n \ge 14$ and $9n - 3$ for odd $n \ge 17$; $13$ has value $9n + 6$ for even $n \ge 12$ and
$9n + 3$ for odd $n \ge 15$; $14$ has value $9n + 12$ for even $n \ge 12$ and $9n + 9$ for odd
$n \ge 15$; $15$ has value $9n + 18$ for even $n \ge 18$ and $9n + 15$ for odd $n \ge 15$; $16$
has value $10n$ if $n = 17$ or $n \ge 19$; $17$ has value $10n + 6$ if $n = 15$ or $n \ge 17$; $18$
has value $10n + 12$ if $n = 17$ or $n \ge 19$; $19$ has value $10n + 18$ if $n = 20$ or
$n \ge 22$; $20$ has value $11n$ for even $n \ge 18$ and $11n - 3$ for odd $n \ge 21$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Corollary 1.

Stated but not proved: `MetaMathlibExt.isGenFrobeniusNumber_triangularTriple_eleven_to_twenty` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedFrobeniusTriangularWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html#is-gen-frobenius-number-triangular-tripl-4).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Frobenius numbers of triangular numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers-of-triangular-numb)
