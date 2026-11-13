---
declaration: section
origin: cited
lean: MetaMathlibExt.toeplitzHessenberg_fussCatalan_examples, MetaMathlibExt.toeplitzHessenbergDet_genFun, MetaMathlibExt.toeplitzHessenbergDet_fussCatalan, MetaMathlibExt.toeplitzHessenbergDet_fussCatalan_special, MetaMathlibExt.toeplitzHessenbergDet_catalan, MetaMathlibExt.toeplitzHessenbergDet_ternary, MetaMathlibExt.trudiPartitionSum_fussCatalan, MetaMathlibExt.nonempty_equiv_evenNoncrossing_evenDescentDyck
statement: formalized
---

# Toeplitz–Hessenberg determinants of Fuss–Catalan numbers

8 results, 1 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html).

## Small generalized Fuss–Catalan numbers

For the generalized Fuss–Catalan numbers
$A_n(p, r) = \frac{r}{pn + r} \binom{pn + r}{n}$, one has $A_3(2, 1) = 5$, $A_2(2, 3) = 9$,
$A_3(3, 1) = 12$ and $A_2(3, 2) = 7$.

With $C_n$ the $n$-th Catalan number, $A_3(2, 1) = C_3$ and $A_2(2, 3) = C_4 - C_3$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Sections 1-2 (`C_n = A_n(2, 1)`, `K_n = A_n(2, 3)`, `H_n = A_n(3, 1)`, `J_n = A_n(3, 2)`).

Formalized by `MetaMathlibExt.toeplitzHessenberg_fussCatalan_examples`, a theorem declared in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#toeplitz-hessenberg-fuss-catalan-example).

## Generating function of Toeplitz–Hessenberg determinants

Let $R$ be a commutative ring and
$a_0, a_1, a_2, \dots$ a sequence in $R$. Write $\det(a_0; a_1, \dots, a_n)$ for the determinant
of the $n \times n$ Toeplitz–Hessenberg matrix whose entry in row $i$ and column $j$ is
$a_{i+1-j}$ for $j \le i + 1$ and $0$ above the superdiagonal. In the ring of formal power series
over $R$ let $f(x) = \sum_{n \ge 1} \det(a_0; a_1, \dots, a_n)\, x^n$ and
$H(x) = \sum_{i \ge 1} a_i (-a_0)^{i-1} x^i$. Then $f = H + H f$.

When $a_0$ is invertible, $H(x) = -g(-a_0 x)/a_0$ with $g(x) = \sum_{i \ge 1} a_i x^i$, and the
identity is the paper's $f(x) = (-g(-a_0 x)/a_0)/(1 + g(-a_0 x)/a_0)$. The form $f = H + H f$
needs no hypothesis on $a_0$; for $a_0 = 0$ it gives $\det(0; a_1, \dots, a_n) = a_1^n$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 2 (`jis-2026-26.1.2-lem-2`).

Stated but not proved: `MetaMathlibExt.toeplitzHessenbergDet_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#toeplitz-hessenberg-det-gen-fun).

## Toeplitz–Hessenberg determinants of Fuss–Catalan numbers

Write
$\det(a_0; a_1, \dots, a_n)$ for the determinant of the $n \times n$ Toeplitz–Hessenberg matrix
whose entry in row $i$ and column $j$ is $a_{i+1-j}$ for $j \le i + 1$ and $0$ above the
superdiagonal. For natural numbers $p, r, n$ let $A_n(p, r) = \frac{r}{pn + r} \binom{pn + r}{n}$
be the generalized Fuss–Catalan number, taken to be $0$ when $pn + r = 0$. Then for all natural
numbers $p, r$ and every $n \ge 1$,

$$\det(1; A_1(p, r), \dots, A_n(p, r)) = (-1)^{n-1} \frac{r}{n} \binom{pn - r - 1}{n - 1}$$

in $\mathbb{Q}$, where the binomial coefficient has an integer, possibly negative, upper index:
$\binom{x}{k} = x (x - 1) \cdots (x - k + 1)/k!$.

This includes $p = r = 0$, which the paper's standing assumption excludes; there every entry
$A_i(0, 0)$ is $0$ and both sides vanish.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Theorem 3 (`jis-2026-26.1.2-thm-3`).

Stated but not proved: `MetaMathlibExt.toeplitzHessenbergDet_fussCatalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#toeplitz-hessenberg-det-fuss-catalan).

## Special Toeplitz–Hessenberg determinants of Fuss–Catalan numbers

Write
$\det(a_0; a_1, \dots, a_n)$ for the determinant of the $n \times n$ Toeplitz–Hessenberg matrix
whose entry in row $i$ and column $j$ is $a_{i+1-j}$ for $j \le i + 1$ and $0$ above the
superdiagonal. For natural numbers $p, r \ge 1$ let $A_n(p, r) = \frac{r}{pn + r} \binom{pn + r}{n}$
be the generalized Fuss–Catalan number, put
$D_n(p, r) = (-1)^{n-1} \det(1; A_1(p, r), \dots, A_n(p, r))$, and let $C_n$ be the $n$-th
Catalan number. Then, in $\mathbb{Q}$: $D_n(2, 3) = C_{n-1} - C_{n-2}$ for every $n \ge 2$;
$D_n(2, 4) = C_{n-1} - 2 C_{n-2}$ for every $n \ge 3$;
$D_n(3, 1) = \frac{1}{n} \binom{3n - 2}{n - 1}$ for every $n \ge 1$; and
$D_n(3, 2) = \frac{2}{n} \binom{3n - 3}{n - 1}$ for every $n \ge 1$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Corollary 4 (`jis-2026-26.1.2-cor-4`).

Stated but not proved: `MetaMathlibExt.toeplitzHessenbergDet_fussCatalan_special` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#toeplitz-hessenberg-det-fuss-catalan-spe).

## Toeplitz–Hessenberg determinants with Catalan entries

Write $\det(a_0; a_1, \dots, a_n)$
for the determinant of the $n \times n$ Toeplitz–Hessenberg matrix whose entry in row $i$ and
column $j$ is $a_{i+1-j}$ for $j \le i + 1$ and $0$ above the superdiagonal (so $a_0$ fills the
superdiagonal and $a_1, \dots, a_n$ the first column); for $n = 0$ it is $1$. Let $C_n$ be the
$n$-th Catalan number, $C(x) = \sum_{n \ge 0} C_n x^n \in \mathbb{Q}[[x]]$, and
$K_m = C_{m+2} - C_{m+1}$ for $m \ge -1$, so that $K_{-1} = 0$. Then the following hold.
(1) $\sum_{n \ge 1} \det(-1; C_1, C_3, \dots, C_{2n-1})\, x^{2n} = x^2 C(x)^2 C(-x)^2$.
(2) $\bigl(\sum_{n \ge 0} \det(-1; C_2, \dots, C_{n+1})\, x^n\bigr) \bigl(2 - C(x)^2\bigr) = 1$.
(3) For every $n \ge 1$,
$\det(1; K_{-1}, K_0, \dots, K_{n-2}) = (-1)^{n-1} \sum_{i=1}^{n-1} C_i$.
(4) For every $n \ge 1$, $\det(1; K_0, K_1, \dots, K_{n-1}) = (-1)^{n-1} \sum_{i=0}^{n-1} C_i$.
(5) $\bigl(\sum_{n \ge 1} \det(-1; K_0, K_1, \dots, K_{n-1})\, x^n\bigr) \bigl(1 - x C(x)^3\bigr) =
x C(x)^3$.

Thus the determinants in (2) have generating function $1/(2 - C(x)^2)$ and those in (5) have
generating function $x C(x)^3/(1 - x C(x)^3)$, the generating function of OEIS A026674; the
determinants in (1) form OEIS A066357.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Theorem 6 (`jis-2026-26.1.2-thm-6`).

Stated but not proved: `MetaMathlibExt.toeplitzHessenbergDet_catalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#toeplitz-hessenberg-det-catalan).

## Toeplitz–Hessenberg determinants of ternary Fuss–Catalan numbers

Write
$\det(a_0; a_1, \dots, a_n)$ for the determinant of the $n \times n$ Toeplitz–Hessenberg matrix
whose entry in row $i$ and column $j$ is $a_{i+1-j}$ for $j \le i + 1$ and $0$ above the
superdiagonal, and let $H_n = \frac{1}{3n + 1} \binom{3n + 1}{n}$ and
$J_n = \frac{2}{3n + 2} \binom{3n + 2}{n}$. Then, in $\mathbb{Q}$,
$\det(1; H_2, H_3, \dots, H_{n+1}) = \frac{2 (-1)^{n-1}}{n} \binom{3n - 3}{n - 1}$ for every
$n \ge 2$, and $\det(-1; J_0, J_1, \dots, J_{n-1}) = H_n$ for every $n \ge 1$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Theorem 8, formulas (4) and (6) (`jis-2026-26.1.2-thm-8`).

Stated but not proved: `MetaMathlibExt.toeplitzHessenbergDet_ternary` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#toeplitz-hessenberg-det-ternary).

## Trudi multi-sums of Fuss–Catalan numbers

For $s \in \mathbb{Q}$ and rational numbers
$a_1, \dots, a_n$ let $T_s(a_1, \dots, a_n)$ be the sum of
$s^{|\alpha|} \binom{|\alpha|}{\alpha_1, \dots, \alpha_n} a_1^{\alpha_1} \cdots a_n^{\alpha_n}$
over all $(\alpha_1, \dots, \alpha_n) \in \mathbb{N}^n$ with
$\alpha_1 + 2 \alpha_2 + \dots + n \alpha_n = n$, where $|\alpha| = \alpha_1 + \dots + \alpha_n$.
Let $A_n(p, r) = \frac{r}{pn + r} \binom{pn + r}{n}$ be the generalized Fuss–Catalan number,
taken to be $0$ when $pn + r = 0$; let $C_n$ be the $n$-th Catalan number,
$K_m = C_{m+2} - C_{m+1}$ for $m \ge -1$ (so $K_{-1} = 0$), $H_n = A_n(3, 1)$ and
$J_n = A_n(3, 2)$. Then the following hold.
(1) For all natural numbers $p, r$ and every $n \ge 1$,
$-T_{-1}(A_1(p, r), \dots, A_n(p, r)) = \frac{r}{n} \binom{pn - r - 1}{n - 1}$, where the
binomial coefficient has an integer, possibly negative, upper index:
$\binom{x}{k} = x (x - 1) \cdots (x - k + 1)/k!$.
(2) For every $n \ge 1$, $-T_{-1}(K_{-1}, K_0, \dots, K_{n-2}) = \sum_{i=1}^{n-1} C_i$.
(3) For every $n \ge 1$, $-T_{-1}(K_0, K_1, \dots, K_{n-1}) = \sum_{i=0}^{n-1} C_i$.
(4) For every $n \ge 2$, $-T_{-1}(H_2, H_3, \dots, H_{n+1}) = \frac{2}{n} \binom{3n - 3}{n - 1}$.
(5) For every $n \ge 1$, $T_1(J_0, J_1, \dots, J_{n-1}) = H_n$.

Identity (1) includes $p = r = 0$, which the paper's standing assumption excludes; there both
sides are $0$.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Corollary 9 (`jis-2026-26.1.2-cor-9`).

Stated but not proved: `MetaMathlibExt.trudiPartitionSum_fussCatalan` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#trudi-partition-sum-fuss-catalan).

## Even noncrossing partitions and Dyck paths with even descents

For every natural number
$n$, there is a bijection between the noncrossing partitions of $\{0, \dots, 2n - 1\}$ all of
whose blocks have even size and the Dyck paths of semilength $2n$ all of whose descents have even
length. Here the descents of a Dyck path are the lengths of its maximal runs of down steps, one
for each peak $UD$: the run of down steps starting at the $D$ of that peak.

## Sources

- Taras Goy and Mark Shattuck, *Determinants of Toeplitz-Hessenberg Matrices with Fuss-Catalan Entries*, Journal of Integer Sequences 29 (2026), Article 26.1.2, Lemma 10 (`jis-2026-26.1.2-lem-10`).

Stated but not proved: `MetaMathlibExt.nonempty_equiv_evenNoncrossing_evenDescentDyck` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/ToeplitzHessenbergFussCatalanWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html#nonempty-equiv-even-noncrossing-even-des).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Toeplitz–Hessenberg determinants of Fuss–Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/hankel-continued-fractions/toeplitz-hessenberg-determinants-of-fuss-catalan)
