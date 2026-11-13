---
declaration: section
origin: cited
lean: MetaMathlibExt.fixedDegreeMonic, MetaMathlibExt.mem_fixedDegreeMonic_iff, MetaMathlibExt.fixedDegreeMonic_zero, MetaMathlibExt.monicIrreducible, MetaMathlibExt.mem_monicIrreducible_iff, MetaMathlibExt.hFree, MetaMathlibExt.one_mem_hFree, MetaMathlibExt.hFull
statement: formalized
---

# Prime factors of given multiplicity in h-free polynomials

78 results, 55 proved and 23 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html).

## Monic polynomials of fixed degree

For a finite field $F$ and a natural number $n$, $M_n$ is
the finite set of monic polynomials of degree $n$ over $F$: the polynomials
$X^n + c_{n-1} X^{n-1} + \dots + c_1 X + c_0$ with $c_0, \dots, c_{n-1} \in F$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.fixedDegreeMonic`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#fixed-degree-monic).

## Membership in $M_n$

Let $F$ be a finite field and $n \in \mathbb{N}$. A polynomial $f$ over
$F$ lies in the set $M_n$ of monic polynomials of degree $n$ over $F$ if and only if there are
$c_0, \dots, c_{n-1} \in F$ with $f = X^n + \sum_{i=0}^{n-1} c_i X^i$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.mem_fixedDegreeMonic_iff`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#mem-fixed-degree-monic-iff).

## The only monic polynomial of degree zero

For every finite field $F$, the set $M_0$ of monic
polynomials of degree $0$ over $F$ is $\{1\}$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.fixedDegreeMonic_zero`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#fixed-degree-monic-zero).

## Monic irreducible polynomials

For a field $F$, $\mathcal{P}$ is the set of polynomials over
$F$ that are monic and irreducible; these are the prime polynomials of the paper.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.monicIrreducible`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#monic-irreducible).

## Membership in the set of monic irreducible polynomials

Let $F$ be a field. A polynomial $P$
over $F$ lies in the set $\mathcal{P}$ of monic irreducible polynomials over $F$ if and only if
$P$ is monic and irreducible.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.mem_monicIrreducible_iff`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#mem-monic-irreducible-iff).

## $h$-free polynomials

Let $F$ be a field and $h$ a natural number. The set $S_h$ of
$h$-free polynomials over $F$ consists of the monic polynomials $f$ over $F$ such that no monic
irreducible polynomial $P$ over $F$ satisfies $P^h \mid f$.

The condition makes sense for every natural number $h$; the paper's asymptotic theorems
separately assume $h \ge 2$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.hFree`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free).

## The polynomial $1$ is $h$-free

For every field $F$ and every natural number $h \ge 1$,
the constant polynomial $1 \in F[X]$ is $h$-free: it is monic and no $h$-th power of a monic
irreducible polynomial divides it.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.one_mem_hFree`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#one-mem-h-free).

## $h$-full polynomials

Let $F$ be a field and $h \in \mathbb{N}$. The set $N_h$ of $h$-full
polynomials over $F$ consists of the monic polynomials $f$ such that $P^h$ divides $f$ for
every monic irreducible polynomial $P$ that divides $f$.

As in the source, theorem statements impose $h \ge 2$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.hFull`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full).

## The polynomial $1$ is $h$-full

For every field $F$ and every natural number $h$, the
constant polynomial $1 \in F[X]$ is $h$-full: it is monic, and whenever a monic irreducible
polynomial $P$ divides it, so does $P^h$.

The divisibility condition holds vacuously, since no irreducible polynomial divides $1$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.one_mem_hFull`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#one-mem-h-full).

## Number of prime factors of given multiplicity

Let $F$ be a field and $k \in \mathbb{N}$. For a
nonzero polynomial $f$ over $F$, $\omega_k(f)$ is the number of distinct monic irreducible
polynomials $P$ dividing $f$ whose multiplicity in $f$ (the largest $m$ with $P^m \mid f$) is
exactly $k$. For the zero polynomial, $\omega_k(0) = 0$ by convention.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.omegaMult`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult).

## $\omega_k$ vanishes at the zero polynomial

For every field $F$ and every natural number $k$,
$\omega_k(0) = 0$. Here $\omega_k(f)$ is the number of distinct monic irreducible polynomials
dividing a nonzero polynomial $f$ over $F$ with multiplicity exactly $k$, and $\omega_k(0) = 0$
by convention, so this records that convention.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.omegaMult_zero`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-zero).

## $\omega_k$ vanishes at the polynomial $1$

For every field $F$ and every natural number $k$,
$\omega_k(1) = 0$, where $\omega_k(f)$ is the number of distinct monic irreducible polynomials
dividing a nonzero polynomial $f$ over $F$ with multiplicity exactly $k$.

The polynomial $1$ is a unit, so it has no monic irreducible factors.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Definitions.

Formalized by `MetaMathlibExt.omegaMult_one`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-one).

## Degree-nondecreasing functions

Let $F$ be a field, $U$ a set of polynomials over $F$ and
$G$ a real-valued function on polynomials over $F$. Then $G$ is degree-nondecreasing on $U$
when for all $f_1, f_2 \in U$ with $\deg f_2 \le \deg f_1$ we have $G(f_2) \le G(f_1)$. Here
$\deg$ is the natural degree, with $\deg 0 = 0$.

In particular $G$ takes the same value on members of $U$ of equal degree. The natural degree is
adequate because $U$ will consist of monic, hence nonzero, polynomials.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3 (definition preceding the requested normal-order results).

Formalized by `MetaMathlibExt.IsDegreeNondecreasing`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#is-degree-nondecreasing).

## Constant functions are degree-nondecreasing

Let $F$ be a field and $U$ a set of
polynomials over $F$. For every real number $c$, the constant function with value $c$ is
degree-nondecreasing on $U$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3 (definition preceding the requested normal-order results).

Formalized by `MetaMathlibExt.isDegreeNondecreasing_const`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#is-degree-nondecreasing-const).

## Normal order on a set of polynomials

Let $F$ be a finite field, let $U$ be a set of
polynomials over $F$, and let $g, G$ be real-valued functions on polynomials over $F$. For
$n \in \mathbb{N}$ let $M_n$ be the set of monic polynomials of degree $n$ over $F$. Then $g$
has normal order $G$ on $U$ when $g$ and $G$ are nonnegative on $U$, $G$ is
degree-nondecreasing on $U$ (for $f_1, f_2 \in U$, $\deg f_2 \le \deg f_1$ implies
$G(f_2) \le G(f_1)$, with $\deg$ the natural degree), and for every real $\varepsilon > 0$ the
number of $f \in U \cap M_n$ for which $(1 - \varepsilon)G(f) < g(f) < (1 + \varepsilon)G(f)$
fails is $o(|U \cap M_n|)$ as $n \to \infty$.

The paper takes $g, G : U \to \mathbb{R}_{\ge 0}$; here both are total real-valued functions,
with nonnegativity imposed on $U$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3 (definition preceding the requested normal-order results).

Formalized by `MetaMathlibExt.HasNormalOrder`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#has-normal-order).

## Normal orders are nonnegative

Let $F$ be a finite field, $U$ a set of polynomials over $F$,
and $g, G$ real-valued functions on polynomials over $F$. If $g$ has normal order $G$ on $U$, then
$G(f) \ge 0$ for every $f \in U$.

This is the second defining clause of a normal order.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3 (definition preceding the requested normal-order results).

Formalized by `MetaMathlibExt.HasNormalOrder.nonnegative`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#nonnegative).

## Erdős–Kac theorem for $\omega_1$ on $h$-free polynomials

Let $F$ be a finite field, let
$h \ge 2$ and let $\alpha \le \beta$ be real numbers. A monic polynomial $f$ over $F$ is $h$-free
if $P^h \nmid f$ for every monic irreducible $P$, and $\omega_1(f)$ is the number of distinct
monic irreducible $P$ that divide $f$ with multiplicity exactly $1$. For each $n$, let $p_n$ be
the number of $h$-free monic polynomials $f$ of degree $n$ over $F$ with

$$\alpha \le \frac{\omega_1(f) - \log n}{\sqrt{\log n}} \le \beta,$$

divided by the number of all $h$-free monic polynomials of degree $n$ over $F$. Then
$p_n \to \frac{1}{\sqrt{2\pi}} \int_\alpha^\beta e^{-t^2/2}\,dt$ as $n \to \infty$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 2.

Stated but not proved: `MetaMathlibExt.erdosKac_omegaOne_hFree` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#erdos-kac-omega-one-h-free).

## $\omega_k$ has no normal order on $h$-free polynomials for $1 < k < h$

Let $F$ be a finite
field, let $h \ge 2$ and $1 < k < h$, and let $S_h$ be the set of $h$-free monic polynomials over
$F$. Let $G$ be a real-valued function on polynomials over $F$ that is nonnegative on $S_h$ and
degree-nondecreasing on $S_h$, that is, $G(f_2) \le G(f_1)$ whenever $f_1, f_2 \in S_h$ and
$\deg f_2 \le \deg f_1$. Then $\omega_k$, the number of monic irreducible factors of multiplicity
exactly $k$, viewed as a real-valued function, does not have normal order $G$ on $S_h$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 4.

Stated but not proved: `MetaMathlibExt.omegaMult_no_normalOrder_hFree` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-no-normal-order-h-free).

## Erdős–Kac theorem for $\omega_h$ on $h$-full polynomials

Let $F$ be a finite field, let
$h \ge 2$ and let $\alpha \le \beta$ be real numbers. A monic polynomial $f$ over $F$ is $h$-full
if $P^h \mid f$ for every monic irreducible $P$ dividing $f$, and $\omega_h(f)$ is the number of
distinct monic irreducible $P$ that divide $f$ with multiplicity exactly $h$. For each $n$, let
$p_n$ be the number of $h$-full monic polynomials $f$ of degree $n$ over $F$ with

$$\alpha \le \frac{\omega_h(f) - \log(n/h)}{\sqrt{\log(n/h)}} \le \beta,$$

divided by the number of all $h$-full monic polynomials of degree $n$ over $F$, where $n/h$ is
real division. Then $p_n \to \frac{1}{\sqrt{2\pi}} \int_\alpha^\beta e^{-t^2/2}\,dt$ as
$n \to \infty$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 6.

Stated but not proved: `MetaMathlibExt.erdosKac_omegaH_hFull` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#erdos-kac-omega-h-h-full).

## $\omega_k$ has no normal order on $h$-full polynomials for $k > h$

Let $F$ be a finite
field, let $2 \le h < k$, and let $N_h$ be the set of $h$-full monic polynomials over $F$. Let
$G$ be a real-valued function on polynomials over $F$ that is nonnegative on $N_h$ and
degree-nondecreasing on $N_h$, that is, $G(f_2) \le G(f_1)$ whenever $f_1, f_2 \in N_h$ and
$\deg f_2 \le \deg f_1$. Then $\omega_k$, the number of monic irreducible factors of multiplicity
exactly $k$, viewed as a real-valued function, does not have normal order $G$ on $N_h$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 8.

Stated but not proved: `MetaMathlibExt.omegaMult_no_normalOrder_hFull` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-no-normal-order-h-full).

## Counting $\ell$-free polynomials coprime to an irreducible

Let $F$ be a finite field with
$q$ elements, let $\ell \ge 2$ and let $d$ be a natural number. Call a monic polynomial over $F$
$\ell$-free if it is divisible by the $\ell$-th power of no monic irreducible polynomial. There is a
constant $C \ge 0$ such that for every monic irreducible polynomial $P$ over $F$ of degree $d$,
with $|P| = q^{d}$, and every natural number $n$, the number $N$ of $\ell$-free monic polynomials
of degree $n$ over $F$ that are coprime to $P$ satisfies

$$\left| N - \frac{q^n (1 - q^{1-\ell})(1 - |P|^{-1})}{1 - |P|^{-\ell}} \right| \le C.$$

So $C$ depends on $F$, $\ell$ and $d$ but not on $P$ or $n$.

The source states the lemma for $\ell > 0$. The factor $1 - q^{1-\ell}$ equals $1/\zeta_q(\ell)$,
where $\zeta_q(s) = 1/(1 - q^{1-s})$ is the zeta function of the polynomial ring over $F$; it has
a pole at $s = 1$, so the statement here assumes $\ell \ge 2$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 3.

Stated but not proved: `MetaMathlibExt.card_hFree_coprime_irreducible_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#card-h-free-coprime-irreducible-asymptot).

## Perron's formula for degree slices of monic polynomials

Let $F$ be a finite field,
let $M_m$ be the set of monic polynomials of degree $m$ over $F$, let
$a \colon F[X] \to \mathbb{C}$, and write $c_m = \sum_{f \in M_m} a(f)$. Let $r$ be a real
number with $0 < r < 1$ such that the series $\sum_{m \ge 0} |c_m| r^m$ converges, and let
$A \colon \mathbb{C} \to \mathbb{C}$ satisfy $A(u) = \sum_{m \ge 0} c_m u^m$ for every
complex $u$ with $|u| = r$. Then for every $n \ge 0$,

$$c_n = \frac{1}{2\pi i} \oint_{|u| = r} \frac{A(u)}{u^{n+1}}\, du,$$

where the circle $|u| = r$ is traversed once counterclockwise.

Convergence of $\sum |c_m| r^m$ at the single radius $r$ stands in for the paper's uniform
absolute convergence on the closed disk, and $A$ only has to agree with the series on the
circle, the only values the contour integral sees.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 9.

Stated but not proved: `MetaMathlibExt.perron_formula_polynomial_degree_slice` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#perron-formula-polynomial-degree-slice).

## The polynomial norm $q^{\deg f}$ over a finite field

Let $F$ be a finite field with
$q$ elements. The norm of a polynomial $f \in F[X]$ is the real number $|f| = q^{\deg f}$ if
$f \neq 0$, and $|0| = 0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Introduction.

Formalized by `MetaMathlibExt.polyNorm`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#poly-norm).

## The zero polynomial has norm $0$

For every finite field $F$, the norm of the zero
polynomial in $F[X]$ is $|0| = 0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Introduction.

Formalized by `MetaMathlibExt.polyNorm_zero`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#poly-norm-zero).

## A nonzero polynomial has norm $q^{\deg f}$

Let $F$ be a finite field with $q$
elements. Every nonzero polynomial $f \in F[X]$ has norm $|f| = q^{\deg f}$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Introduction.

Formalized by `MetaMathlibExt.polyNorm_of_ne_zero`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#poly-norm-of-ne-zero).

## Function field Mertens constant

For a finite field $F$ with $q$ elements, the analogue
of the first Mertens constant is

$$B_1 = \gamma + \sum_P \left(\log\left(1 - \frac{1}{|P|}\right) + \frac{1}{|P|}\right),$$

where $\gamma$ is the Euler–Mascheroni constant, the sum runs over the monic irreducible
polynomials $P$ over $F$, and $|P| = q^{\deg P}$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Introduction.

Formalized by `MetaMathlibExt.functionFieldMertensConstant`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#function-field-mertens-constant).

## Series for the function field Mertens constant

For a finite field $F$ with $q$ elements,
the function field Mertens constant $B_1$ of $F$ equals

$$\gamma + \sum_P \left(\log\left(1 - \frac{1}{|P|}\right) + \frac{1}{|P|}\right),$$

where $\gamma$ is the Euler–Mascheroni constant, the sum runs over the monic irreducible
polynomials $P$ over $F$, and $|P| = q^{\deg P}$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Introduction.

Formalized by `MetaMathlibExt.functionFieldMertensConstant_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#function-field-mertens-constant-eq).

## Moments of $\omega_k$ over $h$-free polynomials

Let $F$ be a finite field and let $h$,
$k$, $j$, $n$ be natural numbers. Let $S_h$ be the set of $h$-free monic polynomials over $F$
(those divisible by no $P^h$ with $P$ monic irreducible), $M_n$ the set of monic polynomials of
degree $n$ over $F$, and $\omega_k(f)$ the number of distinct monic irreducible factors of $f$
whose multiplicity is exactly $k$. The $j$-th moment of $\omega_k$ over the $h$-free monic
polynomials of degree $n$ is the real number

$$\frac{1}{|S_h \cap M_n|} \sum_{f \in S_h \cap M_n} \omega_k(f)^j,$$

which is $0$ when $S_h \cap M_n$ is empty.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorems 1 and 3.

Formalized by `MetaMathlibExt.hFreeMoment`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-moment).

## Explicit formula for the moments over h-free polynomials

Let $F$ be a finite field and
let $h, k, j, n$ be natural numbers. Write $M_n$ for the monic polynomials of degree $n$ over
$F$, $S_h$ for the $h$-free monic polynomials (those divisible by the $h$-th power of no monic
irreducible polynomial) and $\omega_k(f)$ for the number of distinct monic irreducible factors of
$f$ of multiplicity exactly $k$. Then the $j$-th moment of $\omega_k$ over $S_h \cap M_n$ equals

$$\frac{1}{|S_h \cap M_n|} \sum_{f \in S_h \cap M_n} \omega_k(f)^j,$$

which is $0$ when $S_h \cap M_n$ is empty.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorems 1 and 3.

Formalized by `MetaMathlibExt.hFreeMoment_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-moment-eq).

## The prime sum $T_h$

Let $F$ be a finite field with $q$ elements, let $h$ be a natural
number, and write $|P| = q^{\deg P}$ for a monic irreducible polynomial $P$ over $F$. The prime
sum $T_h$ is the real number

$$T_h = \sum_P \frac{|P|^{h-1} - 1}{|P|\,(|P|^h - 1)},$$

the sum running over all monic irreducible polynomials $P$ over $F$, where, when $h = 0$, the
exponent $h - 1$ is read as $0$ and each summand, whose denominator then vanishes, is read as $0$;
the sum is taken to be $0$ if it does not converge absolutely.
For $h \ge 2$ it is the prime sum in the constant term of the mean number of monic irreducible
factors of multiplicity exactly one of a monic $h$-free polynomial of degree $n$ (Theorem 1).

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1.

Formalized by `MetaMathlibExt.hFreeOmegaOneSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-sum).

## Unfolding the prime sum $T_h$

Let $F$ be a finite field with $q$ elements, let $h$ be a
natural number, and write $|P| = q^{\deg P}$ for a monic irreducible polynomial $P$ over $F$. Then
the prime sum $T_h$ equals the real sum over all monic irreducible polynomials $P$ over $F$

$$\sum_P \frac{|P|^{h-1} - 1}{|P|\,(|P|^h - 1)},$$

where, when $h = 0$, the exponent $h - 1$ is read as $0$ and each summand, whose denominator then
vanishes, is read as $0$; the sum is taken to be $0$ if it does not converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1.

Formalized by `MetaMathlibExt.hFreeOmegaOneSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-sum-eq).

## The squared prime sum $U_h$ for multiplicity $1$ on $h$-free polynomials

Let $F$ be a
finite field with $q$ elements, let $h$ be a natural number, and for a monic irreducible
polynomial $P$ over $F$ write $|P| = q^{\deg P}$. Then $U_h$ is the real number

$$U_h = \sum_P \left(\frac{|P|^{\max(h-2,\,0)} (|P| - 1)}{|P|^h - 1}\right)^2,$$

the sum over all monic irreducible $P$, where a quotient with zero denominator (only when
$h = 0$) is read as $0$ and the sum is $0$ when the series does not converge absolutely.

$U_h$ enters the constants in the second moment and the variance of the number of distinct monic
irreducible factors of multiplicity exactly $1$ over $h$-free polynomials.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1.

Formalized by `MetaMathlibExt.hFreeOmegaOneSqSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 475](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L475). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-sq-sum).

## Series formula for the squared prime sum $U_h$

Let $F$ be a finite field with $q$
elements, let $h$ be a natural number, and for a monic irreducible polynomial $P$ over $F$ write
$|P| = q^{\deg P}$. Then the squared prime sum $U_h$ for multiplicity $1$ on $h$-free polynomials
equals

$$\sum_P \left(\frac{|P|^{\max(h-2,\,0)} (|P| - 1)}{|P|^h - 1}\right)^2,$$

the sum over all monic irreducible $P$, where a quotient with zero denominator (only when
$h = 0$) is read as $0$ and the sum is $0$ when the series does not converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1.

Formalized by `MetaMathlibExt.hFreeOmegaOneSqSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-sq-sum-eq).

## The prime sum $S_{h,k}$ for multiplicity $k$ on $h$-free polynomials

Let $F$ be a finite
field with $q$ elements and let $h$, $k$ be natural numbers. For a monic irreducible polynomial
$P$ over $F$ write $|P| = q^{\deg P}$ and $a_P = |P|^{\max(h-k-1,\,0)} (|P| - 1)/(|P|^h - 1)$,
read as $0$ when the denominator vanishes (only when $h = 0$). Then $S_{h,k}$ is the real number
$\sum_P a_P$, the sum over all monic irreducible $P$, taken to be $0$ when the series does not
converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3.

Formalized by `MetaMathlibExt.hFreeOmegaMultSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-mult-sum).

## Series formula for the prime sum $S_{h,k}$

Let $F$ be a finite field with $q$ elements
and let $h$, $k$ be natural numbers. For a monic irreducible polynomial $P$ over $F$ write
$|P| = q^{\deg P}$ and $a_P = |P|^{\max(h-k-1,\,0)} (|P| - 1)/(|P|^h - 1)$, read as $0$ when the
denominator vanishes (only when $h = 0$). Then the prime sum $S_{h,k}$ for multiplicity $k$ on
$h$-free polynomials equals $\sum_P a_P$, the sum over all monic irreducible $P$, taken to be $0$
when the series does not converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3.

Formalized by `MetaMathlibExt.hFreeOmegaMultSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-mult-sum-eq).

## Squared prime sum for multiplicity $k$ on $h$-free polynomials

Let $F$ be a finite field
with $q$ elements and let $h$, $k$ be natural numbers. For a monic irreducible polynomial $P$
over $F$ write $|P| = q^{\deg P}$ and $a_P = |P|^{\max(h-k-1,\,0)} (|P| - 1)/(|P|^h - 1)$, read
as $0$ when the denominator vanishes (only when $h = 0$). The squared prime sum is the real
number $\sum_P a_P^2$, the sum over all monic irreducible $P$, taken to be $0$ when the series
does not converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3.

Formalized by `MetaMathlibExt.hFreeOmegaMultSqSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-mult-sq-sum).

## Series formula for the squared prime sum for multiplicity $k$ on $h$-free polynomials

Let $F$ be a finite field with $q$ elements and let $h$, $k$ be natural numbers. For a monic
irreducible polynomial $P$ over $F$ write $|P| = q^{\deg P}$ and
$a_P = |P|^{\max(h-k-1,\,0)} (|P| - 1)/(|P|^h - 1)$, read as $0$ when the denominator vanishes
(only when $h = 0$). Then the squared prime sum for multiplicity $k$ on $h$-free polynomials
equals $\sum_P a_P^2$, the sum over all monic irreducible $P$, taken to be $0$ when the series
does not converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3.

Formalized by `MetaMathlibExt.hFreeOmegaMultSqSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-mult-sq-sum-eq).

## Mean of $\omega_1$ over $h$-free polynomials

Let $F$ be a finite field with $q$ elements
and let $h \ge 2$. Let $\omega_1(f)$ be the number of monic irreducible $P$ dividing $f$ exactly
once, write $|P| = q^{\deg P}$, and let $B_1 = \gamma + \sum_P (\log(1 - 1/|P|) + 1/|P|)$ be the
function field Mertens constant, with $\gamma$ the Euler–Mascheroni constant, and let
$T_h = \sum_P (|P|^{h-1} - 1)/(|P|(|P|^h - 1))$, both sums over monic irreducible $P$. Then the
mean of $\omega_1$ over the $h$-free monic polynomials of degree $n$ over $F$ is
$\log n + B_1 - T_h + O(1/n)$ as $n \to \infty$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1, Equation (4).

Stated but not proved: `MetaMathlibExt.omegaOne_hFree_mean_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 530](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L530). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-one-h-free-mean-asymptotic).

## Second moment of $\omega_1$ over $h$-free polynomials

Let $F$ be a finite field with $q$
elements, let $h \ge 2$ and let $\varepsilon > 0$. Let $\omega_1(f)$ be the number of monic
irreducible $P$ dividing $f$ exactly once, write $S_h \cap M_n$ for the set of $h$-free monic
polynomials of degree $n$ over $F$ and $|P| = q^{\deg P}$, and let
$B_1 = \gamma + \sum_P (\log(1 - 1/|P|) + 1/|P|)$ be the function field Mertens constant, with
$\gamma$ the Euler–Mascheroni constant, $T_h = \sum_P (|P|^{h-1} - 1)/(|P|(|P|^h - 1))$ and
$U_h = \sum_P (|P|^{h-2}(|P| - 1)/(|P|^h - 1))^2$, all sums over monic irreducible $P$. Then the
mean of $\omega_1^2$ over $S_h \cap M_n$ is $\log^2 n + C_2 \log n + C_3 + O(n^{\varepsilon - 1})$
as $n \to \infty$, where $C_2 = 2(B_1 - T_h) + 1$ and
$C_3 = B_1^2 + B_1 - \pi^2/6 - U_h + T_h^2 - (2B_1 + 1) T_h$.

The printed error $O_\varepsilon(q^n/n^{1-\varepsilon})$ is the error of the unnormalized sum in
the paper's proof; divided by $|S_h \cap M_n| = q^n/\zeta_q(h)$ for $n \ge h$, where
$\zeta_q(h) = (1 - q^{1-h})^{-1}$, it is $O_\varepsilon(n^{\varepsilon-1})$, the order that the
paper's remark (an extra factor $n^\varepsilon$ over the first moment's $O(1/n)$) and its
variance formula state.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1, Equation (5).

Stated but not proved: `MetaMathlibExt.omegaOne_hFree_secondMoment_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-one-h-free-second-moment-asymptoti).

## Variance of $\omega_1$ over $h$-free polynomials

Let $F$ be a finite field with $q$
elements, let $h \ge 2$ and let $\varepsilon > 0$. Let $\omega_1(f)$ be the number of monic
irreducible $P$ dividing $f$ exactly once, write $|P| = q^{\deg P}$, and let
$B_1 = \gamma + \sum_P (\log(1 - 1/|P|) + 1/|P|)$ be the function field Mertens constant, with
$\gamma$ the Euler–Mascheroni constant, $T_h = \sum_P (|P|^{h-1} - 1)/(|P|(|P|^h - 1))$ and
$U_h = \sum_P (|P|^{h-2}(|P| - 1)/(|P|^h - 1))^2$, all sums over monic irreducible $P$. Then the
variance of $\omega_1$ over the $h$-free monic polynomials of degree $n$ over $F$, that is, the
mean of $\omega_1^2$ minus the square of the mean of $\omega_1$, is
$\log n + B_1 - \pi^2/6 - U_h - T_h + O(n^{\varepsilon - 1})$ as $n \to \infty$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 1.

Stated but not proved: `MetaMathlibExt.omegaOne_hFree_variance_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 564](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L564). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-one-h-free-variance-asymptotic).

## Mean of $\omega_k$ over $h$-free polynomials

Let $F$ be a finite field with $q$ elements,
let $h, k$ be natural numbers with $1 < k < h$, and let $\varepsilon > 0$. Write $S_h \cap M_n$ for
the set of monic polynomials $f$ of degree $n$ over $F$ that are $h$-free (no $P^h$ with $P$ monic
irreducible divides $f$), and $\omega_k(f)$ for the number of monic irreducible $P$ that divide $f$
exactly $k$ times. For monic irreducible $P$ put $|P| = q^{\deg P}$ and
$a_P = |P|^{h-k-1}(|P| - 1)/(|P|^h - 1)$, and let $S_{h,k} = \sum_P a_P$, the sum over monic
irreducible $P$. Then, as $n \to \infty$, the mean of $\omega_k$ over
$S_h \cap M_n$ is $S_{h,k} + O(q^{n/k - n + \varepsilon n})$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3, Equation (6).

Stated but not proved: `MetaMathlibExt.omegaMult_hFree_mean_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-h-free-mean-asymptotic).

## Second moment of $\omega_k$ over $h$-free polynomials

Let $F$ be a finite field with $q$
elements, let $h, k$ be natural numbers with $1 < k < h$, and let $\varepsilon > 0$. Write
$S_h \cap M_n$ for the set of monic polynomials $f$ of degree $n$ over $F$ that are $h$-free (no
$P^h$ with $P$ monic irreducible divides $f$), and $\omega_k(f)$ for the number of monic
irreducible $P$ that divide $f$ exactly $k$ times. For monic irreducible $P$ put
$|P| = q^{\deg P}$ and $a_P = |P|^{h-k-1}(|P| - 1)/(|P|^h - 1)$, and let $S_{h,k} = \sum_P a_P$,
the sum over monic irreducible $P$. Then, as $n \to \infty$, the mean of $\omega_k^2$ over
$S_h \cap M_n$ is $S_{h,k}^2 - \sum_P a_P^2 + S_{h,k} + O(q^{n/k - n + \varepsilon n})$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 3, Equation (7).

Stated but not proved: `MetaMathlibExt.omegaMult_hFree_secondMoment_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-h-free-second-moment-asymptot).

## Derivatives at $z = 1$ of uniform approximations

Let $r > 0$, let $D$ be the open disk of
radius $r$ centred at $1$ in $\mathbb{C}$, and let $f$ and $G_n$ ($n \in \mathbb{N}$) be complex
functions analytic on $D$. Suppose there is a real constant $C$ such that
$|G_n(z) - f(z)\, n^{z-1}| \le C\, n^{\operatorname{Re} z - 2}$ for all $n \ge 1$ and all
$z \in D$. Then for every $k \in \mathbb{N}$ and every $\varepsilon > 0$, as $n \to \infty$,

$$G_n^{(k)}(1) - \frac{d^k}{dz^k}\big(f(z)\, n^{z-1}\big)\Big|_{z=1} = O(n^{\varepsilon - 1}).$$

This is the paper's Lemma 1, a corrected version of Lalín and Zhang's Lemma 3.2; Equation (11) is
the case $k = 1$. The paper's "analytic at $z = 1$" with an error term "in a neighborhood of
$z = 1$" is read as analyticity on a fixed disk on which the bound holds with one constant for all
$n \ge 1$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 1.

Stated but not proved: `MetaMathlibExt.iteratedDeriv_sub_isBigO_of_uniform_approx` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 607](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L607). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#iterated-deriv-sub-is-big-o-of-uniform-a).

## Selberg–Delange theorem for function fields

Let $q > 1$ and $A > 0$ be real numbers,
and let $B_z(n)$ and $C_z(n)$ be complex numbers, for $z \in \mathbb{C}$ and integers $n \ge 0$,
such that for all $z$ and $n$

$$C_z(n) = \sum_{a=0}^{n} B_z(a)\, q^{n-a} \frac{(z)_{n-a}}{(n-a)!},$$

where $(z)_m = z(z+1)\cdots(z+m-1)$ is the rising factorial. Suppose there is a constant $M$
such that for every complex $z$ with $|z| \le A$ the series
$\sum_{n \ge 0} |B_z(n)| (n+1)^{2A+2} q^{-n}$ converges and its sum is at most $M$. Then there
is a constant $K$ such that for every complex $z$ with $|z| \le A$ and every integer $n \ge 1$,

$$\left| C_z(n) - \frac{q^n n^{z-1}}{\Gamma(z)} \sum_{a \ge 0} \frac{B_z(a)}{q^a} \right|
\le K q^n n^{\operatorname{Re} z - 2}.$$

In terms of the generating functions $B(u, z) = \sum_{n \ge 0} B_z(n) u^n$ and
$C(u, z) = \sum_{n \ge 0} C_z(n) u^n$, and with $Z_q(u) = (1 - qu)^{-1}$, the hypothesis on
$C_z(n)$ says $C(u, z) = B(u, z) Z_q(u)^z$, and the main term is
$q^n n^{z-1} B(1/q, z)/\Gamma(z)$. The paper's $q$ is the size of the field. The weight
$(n+1)^{2A+2}$ replaces the paper's $n^{2A+2}$: equivalent for $n \ge 1$, it also bounds
$B_z(0)$ uniformly, without which the conclusion fails (unbounded $B_z(0)$ along $z \to 2$
with $A = 2$).

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 10.

Stated but not proved: `MetaMathlibExt.selbergDelange_functionField` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 630](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L630). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#selberg-delange-function-field).

## Selberg–Delange theorem, $h$-th power version

Let $q > 1$ and $A > 0$ be real numbers,
let $h \ge 1$ be an integer, let $\xi$ be a primitive $h$-th root of unity in $\mathbb{C}$, and
let $B_z(n)$ and $C_z(n)$ be complex numbers, for $z \in \mathbb{C}$ and integers $n \ge 0$,
such that for all $z$ and $n$

$$C_z(n) = \sum_{\substack{0 \le a \le n \\ h \mid n - a}} B_z(a)\, q^{(n-a)/h}
\frac{(z)_{(n-a)/h}}{((n-a)/h)!},$$

where $(z)_m = z(z+1)\cdots(z+m-1)$ is the rising factorial. Suppose there is a constant $M$
such that for every complex $z$ with $|z| \le A$ the series
$\sum_{n \ge 0} |B_z(n)| (n+1)^{2A+2} q^{-n/h}$ converges and its sum is at most $M$. Then there
is a constant $K$ such that for every complex $z$ with $|z| \le A$ and every integer $n \ge 1$,

$$\left| C_z(n) - \frac{q^{n/h} n^{z-1}}{h^z \Gamma(z)} \sum_{j=0}^{h-1} \xi^{jn}
\sum_{a \ge 0} B_z(a) \left(q^{1/h} \xi^j\right)^{-a} \right|
\le K q^{n/h} n^{\operatorname{Re} z - 2}.$$

In terms of the generating functions $B(u, z) = \sum_{n \ge 0} B_z(n) u^n$ and
$C(u, z) = \sum_{n \ge 0} C_z(n) u^n$, and with $Z_q(u) = (1 - qu)^{-1}$, the hypothesis on
$C_z(n)$ says $C(u, z) = B(u, z) Z_q(u^h)^z$, and the inner sums are
$B((q^{1/h} \xi^j)^{-1}, z)$. The paper's $q$ is the size of the field. As in the case $h = 1$,
the weight is $(n+1)^{2A+2}$ rather than $n^{2A+2}$, so that $B_z(0)$ is bounded uniformly.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 11.

Stated but not proved: `MetaMathlibExt.selbergDelange_functionField_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#selberg-delange-function-field-pow).

## Coefficients of $B_{1,S_h}(u, z)$

Let $F$ be a finite field with $q$ elements, let $h$
be a natural number and let $z$ be a complex number. Let $S_h$ be the set of $h$-free monic
polynomials over $F$ (those divisible by no $P^h$ with $P$ monic irreducible), and $\omega_1(f)$
the number of distinct monic irreducible factors of $f$ of multiplicity exactly $1$. Write
$C_{1,S_h}(u, z) = \sum_{f \in S_h} z^{\omega_1(f)} u^{\deg f}$ and
$B_{1,S_h}(u, z) = Z_q(u)^{-z} C_{1,S_h}(u, z)$, where $Z_q(u)^{-z} = (1 - qu)^z$ is the power
series with coefficient $q^m (-z)_m / m!$ at $u^m$ and $(x)_m = x(x+1) \cdots (x+m-1)$ is the
rising factorial. For a natural number $n$, $B_z(n)$ is the coefficient of $u^n$ in
$B_{1,S_h}(u, z)$, that is,

$$B_z(n) = \sum_{a=0}^{n} \Bigl(\sum_{f \in S_h,\ \deg f = a} z^{\omega_1(f)}\Bigr)
\frac{q^{n-a} (-z)_{n-a}}{(n-a)!}.$$

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 3.1 (definition preceding Lemma 2).

Formalized by `MetaMathlibExt.hFreeOmegaOneB`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-b).

## Constant coefficient of $B_{1,S_h}$

Let $F$ be a finite field with $q$ elements and let
$h \ge 1$ be a natural number. Let $S_h$ be the set of $h$-free monic polynomials over $F$ (those
divisible by no $P^h$ with $P$ monic irreducible) and $\omega_1(f)$ the number of distinct monic
irreducible factors of $f$ of multiplicity exactly $1$. For every complex number $z$, the
coefficient $B_z(0)$ of $u^0$ in the formal power series

$$B_{1,S_h}(u, z) = (1 - qu)^z \sum_{f \in S_h} z^{\omega_1(f)} u^{\deg f},$$

where $(1 - qu)^z = \sum_{m \ge 0} \binom{z}{m} (-qu)^m$, equals $1$.

The only monic polynomial of degree $0$ is $1$, which is $h$-free and has $\omega_1(1) = 0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 3.1 (definition preceding Lemma 2).

Formalized by `MetaMathlibExt.hFreeOmegaOneB_zero`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 688](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L688). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-b-zero).

## The coefficients $B_z(n)$ of the $h$-full series

Let $F$ be a finite field with $q$
elements, let $h$ and $n$ be natural numbers and let $z$ be a complex number. Write $N_h$ for the
set of $h$-full monic polynomials over $F$ (monic $f$ such that $P^h$ divides $f$ for every monic
irreducible $P$ dividing $f$), $\omega_h(f)$ for the number of monic irreducible polynomials that
divide $f$ with multiplicity exactly $h$, and $(x)_m = x(x + 1) \cdots (x + m - 1)$ for the
rising factorial. For $0 \le a \le n$ let $c_a = \sum_f z^{\omega_h(f)}$, the sum over the
$f \in N_h$ of degree $a$. Then $B_z(n)$ is the sum of $c_a \, q^m (-z)_m / m!$ over the $a$ with
$0 \le a \le n$ and $h \mid n - a$, where $m = (n - a)/h$; when $h = 0$ only $a = n$ occurs, with
$m = 0$.

For $h \ge 1$, $B_z(n)$ is the coefficient of $u^n$ in
$B_{h,N_h}(u, z) = (1 - qu^h)^z \sum_{f \in N_h} z^{\omega_h(f)} u^{\deg f}$, since $(1 - qu^h)^z$
has coefficient $q^m (-z)_m / m!$ at $u^{hm}$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 4.1 (definition preceding Lemma 4).

Formalized by `MetaMathlibExt.hFullOmegaHB`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 701](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L701). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-hb).

## Constant coefficient of $B_{h,N_h}$

Let $F$ be a finite field with $q$ elements, let $h$
be a natural number and let $z$ be a complex number. Then the coefficient $B_z(0)$ of the
$h$-full series for $F$, $h$ and $z$ equals $1$. For $h \ge 1$, $B_z(0)$ is the constant
coefficient of $B_{h,N_h}(u, z) = (1 - qu^h)^z \sum_{f \in N_h} z^{\omega_h(f)} u^{\deg f}$,
where $N_h$ is the set of $h$-full monic polynomials over $F$ and $\omega_h(f)$ is the number of
monic irreducible polynomials dividing $f$ with multiplicity exactly $h$.

The only monic polynomial of degree $0$ is $1$, which is $h$-full and has $\omega_h(1) = 0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 4.1 (definition preceding Lemma 4).

Formalized by `MetaMathlibExt.hFullOmegaHB_zero`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-hb-zero).

## Weighted coefficient bound for $B_{1,S_h}$

Let $F$ be a finite field with $q$ elements,
let $h \ge 2$ be a natural number, and let $A$ and $\sigma > 1/2$ be real numbers. Let $S_h$ be
the set of $h$-free monic polynomials over $F$ (those divisible by no $P^h$ with $P$ monic
irreducible) and $\omega_1(f)$ the number of distinct monic irreducible factors of $f$ of
multiplicity exactly $1$. For a complex number $z$ and a natural number $a$ let $B_z(a)$ be the
coefficient of $u^a$ in the formal power series

$$B_{1,S_h}(u, z) = (1 - qu)^z \sum_{f \in S_h} z^{\omega_1(f)} u^{\deg f},$$

where $(1 - qu)^z = \sum_{m \ge 0} \binom{z}{m} (-qu)^m$. Then there is a real constant $c$ such
that for every complex number $z$ with $|z| \le A$ and every natural number $n \ge 2$,

$$\sum_{a=0}^{n} |B_z(a)|\, q^{-\sigma a} \le c.$$

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 2.

Stated but not proved: `MetaMathlibExt.hFreeOmegaOneB_weighted_sum_bounded` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-free-omega-one-b-weighted-sum-bounded).

## Uniform bound for the weighted coefficients of $B_{h,N_h}(u, z)$

Let $F$ be a finite
field with $q$ elements, let $h \ge 2$ be a natural number, and let $A$ and $\sigma$ be real
numbers with $\sigma > 1/(h + 1)$. Then there is a real constant $c$ such that for every complex
number $z$ with $|z| \le A$ and every natural number $n \ge 2$,

$$\sum_{a=0}^{n} |B_z(a)| \, q^{-\sigma a} \le c,$$

where $B_z(a)$ is the coefficient of $u^a$ in the series $B_{h,N_h}(u, z)$ attached to the
$h$-full polynomials over $F$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 4.

Stated but not proved: `MetaMathlibExt.hFullOmegaHB_weighted_sum_bounded` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 740](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L740). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-hb-weighted-sum-bounded).

## The pole parameter $q^{1/h}\xi^j$

Let $F$ be a finite set with $q$ elements, and let
$h, j \in \mathbb{N}$ and $\xi \in \mathbb{C}$. The pole parameter is the complex number
$q^{1/h}\xi^j$, where $q^{1/h}$ is the nonnegative real $h$-th root of $q$ (for $h = 0$ the
exponent $1/h$ is read as $0$, so that $q^{1/h} = 1$).

When $F$ is a field, $h \ge 1$ and $\xi$ is a primitive $h$-th root of unity, the inverses
$(q^{1/h}\xi^j)^{-1}$ are the poles $u$ of $Z_q(u^h)$, where $Z_q(u) = 1/(1 - qu)$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 4.

Formalized by `MetaMathlibExt.hFullRoot`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 753](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L753). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-root).

## Formula for the pole parameter

Let $F$ be a finite set with $q$ elements, and let
$h, j \in \mathbb{N}$ and $\xi \in \mathbb{C}$. The pole parameter $q^{1/h}\xi^j$ equals the
real power $q^{1/h}$, whose exponent is the real number $1/h$ (read as $0$ when $h = 0$), viewed
as a complex number and multiplied by $\xi^j$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 4.

Formalized by `MetaMathlibExt.hFullRoot_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-root-eq).

## The Euler product $H_{N_h, S_\ell}$ for $h$-full, $\ell$-free polynomials

Let $F$ be a
finite field, let $h$ and $\ell$ be natural numbers and let $u$ be a complex number. Then
$H_{N_h, S_\ell}(u)$ is the complex number

$$H_{N_h, S_\ell}(u) = \prod_P (1 + \frac{x^{h+1} - x^{\ell} - x^{2h} + x^{h+\ell}}{1 - x}),$$

the product running over all monic irreducible polynomials $P$ over $F$, where $x = u^{\deg P}$
in the factor for $P$ (Equation (53)), the quotient is read as $0$ when $x = 1$, and the product
is taken to be $1$ if it does not converge unconditionally.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 5, Equation (53).

Formalized by `MetaMathlibExt.hFullFreeEulerH`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 770](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L770). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-free-euler-h).

## Unfolding the Euler product $H_{N_h, S_\ell}$

Let $F$ be a finite field, let $h$ and
$\ell$ be natural numbers and let $u$ be a complex number. Then $H_{N_h, S_\ell}(u)$ equals the
complex product over all monic irreducible polynomials $P$ over $F$

$$\prod_P \Bigl(1 + \frac{x^{h+1} - x^{\ell} - x^{2h} + x^{h+\ell}}{1 - x}\Bigr),$$

where $x = u^{\deg P}$ in the factor for $P$, the quotient is read as $0$ when $x = 1$, and the
product is taken to be $1$ if it does not converge unconditionally.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 5, Equation (53).

Formalized by `MetaMathlibExt.hFullFreeEulerH_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-free-euler-h-eq).

## Counting $h$-full, $\ell$-free polynomials

Let $F$ be a finite field with $q$ elements,
let $h$ and $\ell$ be natural numbers with $0 < h < \ell$, let $\xi \in \mathbb{C}$ be a primitive
$h$-th root of unity and let $\varepsilon > 0$. A monic polynomial $f$ over $F$ is $h$-full if
$P^h \mid f$ for every monic irreducible $P$ dividing $f$, and $\ell$-free if $P^\ell \nmid f$ for
every monic irreducible $P$. Write $r_j = q^{1/h} \xi^j$ with $q^{1/h}$ the positive real root,
and let $H(u)$ be the product over all monic irreducible $P$ over $F$ of
$1 + (x^{h+1} - x^\ell - x^{2h} + x^{h+\ell})/(1 - x)$, where $x = u^{\deg P}$. Then there is a
constant $C$ such that for every $n \ge \ell$ the number $N$ of monic polynomials of degree $n$
over $F$ that are $h$-full and $\ell$-free satisfies

$$\Bigl| N - \frac{q^{n/h}}{h} \sum_{j=0}^{h-1} \xi^{jn} H(r_j^{-1}) \Bigr|
\le C q^{n/(h+1) + \varepsilon n}.$$

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 5, Equation (51).

Stated but not proved: `MetaMathlibExt.card_hFull_hFree_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 796](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L796). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#card-h-full-h-free-asymptotic).

## Counting $h$-full, $\ell$-free polynomials coprime to an irreducible

Let $F$ be a finite
field with $q$ elements, let $h$ and $\ell$ be natural numbers with $0 < h < \ell$, let
$\xi \in \mathbb{C}$ be a primitive $h$-th root of unity, let $P_0$ be a monic irreducible
polynomial over $F$ and let $\varepsilon > 0$. A monic polynomial $f$ over $F$ is $h$-full if
$P^h \mid f$ for every monic irreducible $P$ dividing $f$, and $\ell$-free if $P^\ell \nmid f$ for
every monic irreducible $P$. Write $r_j = q^{1/h} \xi^j$ with $q^{1/h}$ the positive real root,
$y_j = r_j^{-\deg P_0}$, and let $H(u)$ be the product over all monic irreducible $P$ over $F$ of
$1 + (x^{h+1} - x^\ell - x^{2h} + x^{h+\ell})/(1 - x)$, where $x = u^{\deg P}$. Then there is a
constant $C$ (which may depend on $P_0$) such that for every $n \ge \ell$ the number $N$ of monic
polynomials of degree $n$ over $F$ that are $h$-full, $\ell$-free and coprime to $P_0$ satisfies

$$\Bigl| N - \frac{q^{n/h}}{h} \sum_{j=0}^{h-1} \xi^{jn} H(r_j^{-1})
\frac{1 - y_j}{1 - y_j + y_j^h - y_j^\ell} \Bigr| \le C q^{n/(h+1) + \varepsilon n}.$$

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Lemma 5, Equation (52).

Stated but not proved: `MetaMathlibExt.card_hFull_hFree_coprime_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 813](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L813). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#card-h-full-h-free-coprime-asymptotic).

## The $j$-th moment of $\omega_k$ over $h$-full polynomials of degree $n$

Let $F$ be a
finite field and let $h$, $k$, $j$ and $n$ be natural numbers. Let $N_h \cap M_n$ be the finite
set of $h$-full monic polynomials of degree $n$ over $F$ (monic $f$ such that $P^h$ divides $f$
for every monic irreducible $P$ dividing $f$), and let $\omega_k(f)$ be the number of monic
irreducible polynomials that divide $f$ with multiplicity exactly $k$. The moment is the real
number

$$|N_h \cap M_n|^{-1} \sum_{f \in N_h \cap M_n} \omega_k(f)^j,$$

taken to be $0$ when $N_h \cap M_n$ is empty.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorems 5 and 7.

Formalized by `MetaMathlibExt.hFullMoment`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 834](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L834). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-moment).

## The $h$-full moment is an average of $\omega_k^j$

Let $F$ be a finite field and let $h$,
$k$, $j$ and $n$ be natural numbers. Let $N_h \cap M_n$ be the finite set of $h$-full monic
polynomials of degree $n$ over $F$ (monic $f$ such that $P^h$ divides $f$ for every monic
irreducible $P$ dividing $f$), and let $\omega_k(f)$ be the number of monic irreducible
polynomials that divide $f$ with multiplicity exactly $k$. Then the $j$-th moment of $\omega_k$
over $N_h \cap M_n$ equals

$$|N_h \cap M_n|^{-1} \sum_{f \in N_h \cap M_n} \omega_k(f)^j,$$

where the quotient is $0$ when $N_h \cap M_n$ is empty. This holds by definition.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorems 5 and 7.

Formalized by `MetaMathlibExt.hFullMoment_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 844](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-moment-eq).

## The local factor $K(P, h, j)$

Let $F$ be a finite field with $q$ elements, let $h$ and
$j$ be natural numbers, let $\xi$ be a complex number and let $P$ be a polynomial over $F$. Write
$\rho_j = q^{1/h} \xi^j$, where $q^{1/h}$ is the positive real $h$-th root of $q$ (read as $1$
when $h = 0$), and read $\rho_j^{-1}$ as $0$ when $\rho_j = 0$; let $|P| = q^{\deg P}$ if
$P \ne 0$ and $|0| = 0$; and put $y = (\rho_j^{-1})^{\deg P}$, with $\deg 0$ read as $0$. Then

$$K(P, h, j) = \frac{1 - y}{|P|\,(1 - y) + 1},$$

read as $0$ when the denominator vanishes.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 1 (notation preceding Theorem 5).

Formalized by `MetaMathlibExt.hFullK`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-k).

## Unfolding the local factor $K(P, h, j)$

Let $F$ be a finite field with $q$ elements, let
$h$ and $j$ be natural numbers, let $\xi$ be a complex number and let $P$ be a polynomial over $F$.
Write $\rho_j = q^{1/h} \xi^j$, where $q^{1/h}$ is the positive real $h$-th root of $q$ (read as
$1$ when $h = 0$), and read $\rho_j^{-1}$ as $0$ when $\rho_j = 0$; let $|P| = q^{\deg P}$ if
$P \ne 0$ and $|0| = 0$; and put $y = (\rho_j^{-1})^{\deg P}$, with $\deg 0$ read as $0$. Then
$K(P, h, j)$ equals

$$\frac{1 - y}{|P|\,(1 - y) + 1},$$

read as $0$ when the denominator vanishes.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 1 (notation preceding Theorem 5).

Formalized by `MetaMathlibExt.hFullK_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 864](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L864). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-k-eq).

## The Euler product $\Pi_j$ for $h$-full polynomials

Let $F$ be a finite field with $q$
elements, let $h$ and $j$ be natural numbers and let $\xi$ be a complex number. Write
$\rho_j = q^{1/h} \xi^j$, where $q^{1/h}$ is the positive real $h$-th root of $q$ (read as $1$
when $h = 0$), read $\rho_j^{-1}$ as $0$ when $\rho_j = 0$, and write $|P| = q^{\deg P}$ for a
monic irreducible polynomial $P$ over $F$. Then $\Pi_j$ is the complex number

$$\Pi_j = \prod_P (1 - |P|^{-1})\Bigl(1 + \frac{1}{|P|\,(1 - (\rho_j^{-1})^{\deg P})}\Bigr),$$

the product running over all monic irreducible polynomials $P$ over $F$ (Equation (46)), where
$1/0$ is read as $0$, and the product is taken to be $1$ if it does not converge unconditionally.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 1 (asymptotic for `|N_h ∩ M_n|` preceding Theorem 5).

Formalized by `MetaMathlibExt.hFullEulerProduct`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 874](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L874). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-euler-product).

## Unfolding the Euler product $\Pi_j$

Let $F$ be a finite field with $q$ elements, let $h$
and $j$ be natural numbers and let $\xi$ be a complex number. Write $\rho_j = q^{1/h} \xi^j$, where
$q^{1/h}$ is the positive real $h$-th root of $q$ (read as $1$ when $h = 0$), read $\rho_j^{-1}$
as $0$ when $\rho_j = 0$, and write $|P| = q^{\deg P}$ for a monic irreducible polynomial $P$
over $F$. Then $\Pi_j$ equals the complex product over all monic irreducible polynomials $P$
over $F$

$$\prod_P (1 - |P|^{-1})\Bigl(1 + \frac{1}{|P|\,(1 - (\rho_j^{-1})^{\deg P})}\Bigr),$$

where $1/0$ is read as $0$, and the product is taken to be $1$ if it does not converge
unconditionally.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Section 1 (asymptotic for `|N_h ∩ M_n|` preceding Theorem 5).

Formalized by `MetaMathlibExt.hFullEulerProduct_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 884](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L884). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-euler-product-eq).

## The $h$-full weighted mean

Let $F$ be a finite field with $q$ elements, let
$h, n \in \mathbb{N}$, $\xi \in \mathbb{C}$ and $X : \mathbb{N} \to \mathbb{C}$. Let
$N_h \cap M_n$ be the set of $h$-full monic polynomials of degree $n$ over $F$. For each $j$ let
$\rho_j = q^{1/h}\xi^j$ be the pole parameter and let
$\Pi_j = \prod_P (1 - 1/|P|)(1 + 1/(|P|(1 - \rho_j^{-\deg P})))$, the product over monic
irreducible $P$ with $|P| = q^{\deg P}$, taken to be $1$ when the family is not multipliable.
The $h$-full weighted mean of $X$ is the complex number

$$\frac{q^{n/h}/h}{|N_h \cap M_n|} \sum_{j=0}^{h-1} \xi^{jn} \, \Pi_j \, X_j.$$

Here $q^{n/h}$ is a real power with real exponent $n/h$, and division by zero (including
$0^{-1}$) gives $0$.

It carries every $n$-dependent constant in Theorems 5 and 7.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorems 5 and 7.

Formalized by `MetaMathlibExt.hFullWeightedMean`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 897](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L897). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-weighted-mean).

## Formula for the $h$-full weighted mean

Let $F$ be a finite field with $q$ elements, let
$h, n \in \mathbb{N}$, $\xi \in \mathbb{C}$ and $X : \mathbb{N} \to \mathbb{C}$. Let
$N_h \cap M_n$ be the set of $h$-full monic polynomials of degree $n$ over $F$. For each $j$ let
$\rho_j = q^{1/h}\xi^j$ be the pole parameter and let
$\Pi_j = \prod_P (1 - 1/|P|)(1 + 1/(|P|(1 - \rho_j^{-\deg P})))$, the product over monic
irreducible $P$ with $|P| = q^{\deg P}$, taken to be $1$ when the family is not multipliable.
Then the $h$-full weighted mean of $X$ equals

$$\frac{q^{n/h}/h}{|N_h \cap M_n|} \sum_{j=0}^{h-1} \xi^{jn} \, \Pi_j \, X_j.$$

Here $q^{n/h}$ is a real power with real exponent $n/h$, and division by zero (including
$0^{-1}$) gives $0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorems 5 and 7.

Formalized by `MetaMathlibExt.hFullWeightedMean_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 908](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L908). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-weighted-mean-eq).

## The constant $\kappa_j$ for $h$-full polynomials

Let $F$ be a finite field with $q$
elements, let $h$ and $j$ be natural numbers and let $\xi$ be a complex number. Write
$\rho = q^{1/h}\xi^j$, where $q^{1/h}$ is the positive real $h$-th root of $q$ for $h \ge 1$ and
$q^{1/h} = 1$ for $h = 0$, and let $\rho^{-1}$ be read as $0$ when $\rho = 0$. For a monic
irreducible polynomial $P$ over $F$ write $|P| = q^{\deg P}$, $y = (\rho^{-1})^{\deg P}$ and
$K(P, h, j) = (1 - y)/(|P|(1 - y) + 1)$, read as $0$ when the denominator vanishes. Then
$\kappa_j = \sum_P (K(P, h, j) - 1/|P|)$, the sum over all monic irreducible polynomials $P$ over
$F$, taken as an unconditional sum that is $0$ when the family is not summable.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5.

Formalized by `MetaMathlibExt.hFullKSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 919](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L919). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-ksum).

## The series defining $\kappa_j$

Let $F$ be a finite field with $q$ elements, let $h$ and
$j$ be natural numbers and let $\xi$ be a complex number. Write $\rho = q^{1/h}\xi^j$, where
$q^{1/h}$ is the positive real $h$-th root of $q$ for $h \ge 1$ and $q^{1/h} = 1$ for $h = 0$, and
let $\rho^{-1}$ be read as $0$ when $\rho = 0$. For a monic irreducible polynomial $P$ over $F$
write $|P| = q^{\deg P}$, $y = (\rho^{-1})^{\deg P}$ and $K(P, h, j) = (1 - y)/(|P|(1 - y) + 1)$,
read as $0$ when the denominator vanishes. Then the constant $\kappa_j$ attached to $F$, $h$, $\xi$
and $j$ equals $\sum_P (K(P, h, j) - 1/|P|)$, the sum over all monic irreducible polynomials $P$
over $F$, taken as an unconditional sum that is $0$ when the family is not summable. This holds
by definition.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5.

Formalized by `MetaMathlibExt.hFullKSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 928](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L928). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-ksum-eq).

## The sum $\sum_P K(P, h, j)^2$ over monic irreducible polynomials

Let $F$ be a finite
field with $q$ elements, let $h$ and $j$ be natural numbers and let $\xi$ be a complex number.
Write $\rho = q^{1/h}\xi^j$, where $q^{1/h}$ is the positive real $h$-th root of $q$ for $h \ge 1$
and $q^{1/h} = 1$ for $h = 0$, and let $\rho^{-1}$ be read as $0$ when $\rho = 0$. For a monic
irreducible polynomial $P$ over $F$ write $|P| = q^{\deg P}$, $y = (\rho^{-1})^{\deg P}$ and
$K(P, h, j) = (1 - y)/(|P|(1 - y) + 1)$, read as $0$ when the denominator vanishes. This defines
the complex number $\sum_P K(P, h, j)^2$, the sum over all monic irreducible polynomials $P$ over
$F$, taken as an unconditional sum that is $0$ when the family is not summable.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5.

Formalized by `MetaMathlibExt.hFullKSqSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 937](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L937). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-ksq-sum).

## Unfolding the sum of the squares $K(P, h, j)^2$

Let $F$ be a finite field, let $h$ and
$j$ be natural numbers and let $\xi$ be a complex number. The quantity $\sum_P K(P, h, j)^2$ of
Theorem 5 is the complex sum, over all monic irreducible polynomials $P$ over $F$, of the squares
of the local factors $K(P, h, j)$ attached to $h$, $j$ and $\xi$, taken to be $0$ if it does not
converge absolutely.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5.

Formalized by `MetaMathlibExt.hFullKSqSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 946](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L946). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-ksq-sum-eq).

## The $h$-full prime sum $\sum_P b_P$

Let $F$ be a finite field with $q$ elements, let
$h, k, j \in \mathbb{N}$ and $\xi \in \mathbb{C}$, and let $\rho = q^{1/h}\xi^j$ be the pole
parameter, where $q^{1/h}$ is a real power whose exponent $1/h$ is read as $0$ when $h = 0$.
For a monic irreducible polynomial $P$ over $F$ put $|P| = q^{\deg P}$,
$y_P = \rho^{-\deg P}$, $K(P, h, j) = (1 - y_P)/(|P|(1 - y_P) + 1)$ and
$b_P = |P| \, y_P^{k} \, K(P, h, j)$. The $h$-full prime sum is the complex number
$\sum_P b_P$ over all monic irreducible $P$, taken to be $0$ when the family $(b_P)$ is not
summable. Inverses use the convention $0^{-1} = 0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 7.

Formalized by `MetaMathlibExt.hFullOmegaMultSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 954](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L954). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-mult-sum).

## Formula for the $h$-full prime sum $\sum_P b_P$

Let $F$ be a finite field with $q$
elements, let $h, k, j \in \mathbb{N}$ and $\xi \in \mathbb{C}$, and let $\rho = q^{1/h}\xi^j$
be the pole parameter, where $q^{1/h}$ is a real power whose exponent $1/h$ is read as $0$
when $h = 0$. For a monic irreducible polynomial $P$ over $F$ put $|P| = q^{\deg P}$,
$K(P, h, j) = (1 - \rho^{-\deg P})/(|P|(1 - \rho^{-\deg P}) + 1)$ and
$b_P = |P| \, (\rho^{-1})^{k \deg P} \, K(P, h, j)$. Then the $h$-full prime sum $\sum_P b_P$
equals the sum of $b_P$ over all monic irreducible polynomials $P$ over $F$, taken to be $0$
when the family is not summable. Inverses use the convention $0^{-1} = 0$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 7.

Formalized by `MetaMathlibExt.hFullOmegaMultSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 964](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L964). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-mult-sum-eq).

## The sum $\sum_P b_P^2$ over monic irreducible polynomials

Let $F$ be a finite field
with $q$ elements, let $h$, $k$ and $j$ be natural numbers and let $\xi$ be a complex number.
Write $\rho = q^{1/h}\xi^j$, where $q^{1/h}$ is the positive real $h$-th root of $q$ for $h \ge 1$
and $q^{1/h} = 1$ for $h = 0$, and let $\rho^{-1}$ be read as $0$ when $\rho = 0$. For a monic
irreducible polynomial $P$ over $F$ write $|P| = q^{\deg P}$, $y = (\rho^{-1})^{\deg P}$,
$K(P, h, j) = (1 - y)/(|P|(1 - y) + 1)$, read as $0$ when the denominator vanishes, and
$b_P = |P| (\rho^{-1})^{k \deg P} K(P, h, j)$. This defines the complex number $\sum_P b_P^2$, the
sum over all monic irreducible polynomials $P$ over $F$, taken as an unconditional sum that is $0$
when the family is not summable.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 7.

Formalized by `MetaMathlibExt.hFullOmegaMultSqSum`, a definition declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 973](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L973). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-mult-sq-sum).

## The series defining $\sum_P b_P^2$

Let $F$ be a finite field with $q$ elements, let $h$,
$k$ and $j$ be natural numbers and let $\xi$ be a complex number. Write $\rho = q^{1/h}\xi^j$,
where $q^{1/h}$ is the positive real $h$-th root of $q$ for $h \ge 1$ and $q^{1/h} = 1$ for
$h = 0$, and let $\rho^{-1}$ be read as $0$ when $\rho = 0$. For a monic irreducible polynomial
$P$ over $F$ write $|P| = q^{\deg P}$, $y = (\rho^{-1})^{\deg P}$ and
$K(P, h, j) = (1 - y)/(|P|(1 - y) + 1)$, read as $0$ when the denominator vanishes. Then the
constant $\sum_P b_P^2$ attached to $F$, $h$, $k$, $\xi$ and $j$ equals
$\sum_P (|P| (\rho^{-1})^{k \deg P} K(P, h, j))^2$, the sum over all monic irreducible
polynomials $P$ over $F$, taken as an unconditional sum that is $0$ when the family is not
summable. This holds by definition.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 7.

Formalized by `MetaMathlibExt.hFullOmegaMultSqSum_eq`, a theorem declared in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 983](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L983). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#h-full-omega-mult-sq-sum-eq).

## Mean of $\omega_h$ over $h$-full polynomials

Let $F$ be a finite field with $q$ elements,
let $h \ge 2$, let $\xi \in \mathbb{C}$ be a primitive $h$-th root of unity, and let
$\varepsilon > 0$. Write $N_h \cap M_n$ for the set of monic polynomials $f$ of degree $n$ over $F$
that are $h$-full (if a monic irreducible $P$ divides $f$, then so does $P^h$), and $\omega_h(f)$
for the number of monic irreducible $P$ that divide $f$ exactly $h$ times. For monic irreducible
$P$ and $j < h$ put $|P| = q^{\deg P}$, $y_{P,j} = (q^{1/h}\xi^j)^{-\deg P}$ with $q^{1/h} > 0$,
and $K(P, h, j) = (1 - y_{P,j})/(|P|(1 - y_{P,j}) + 1)$. Let
$\kappa_j = \sum_P (K(P, h, j) - |P|^{-1})$ and
$\Pi_j = \prod_P (1 - |P|^{-1})(1 + |P|^{-1}(1 - y_{P,j})^{-1})$, with sum and product over monic
irreducible $P$, and for $X = (X_j)_j$ put
$W_n(X) = |N_h \cap M_n|^{-1} (q^{n/h}/h) \sum_{j=0}^{h-1} \xi^{jn} \Pi_j X_j$. Let $B_1$ be the
function field Mertens constant and $L_n = \log(n/h)$. Then, as $n \to \infty$, the mean
of $\omega_h$ over $N_h \cap M_n$ is $L_n + B_1 + W_n(\kappa) + O(n^{\varepsilon - 1})$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5, Equation (8).

Stated but not proved: `MetaMathlibExt.omegaH_hFull_mean_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 994](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L994). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-h-h-full-mean-asymptotic).

## Second moment of $\omega_h$ over $h$-full polynomials

Let $F$ be a finite field with $q$
elements, let $h \ge 2$, let $\xi \in \mathbb{C}$ be a primitive $h$-th root of unity, and let
$\varepsilon > 0$. Write $N_h \cap M_n$ for the set of monic polynomials $f$ of degree $n$ over $F$
that are $h$-full (if a monic irreducible $P$ divides $f$, then so does $P^h$), and $\omega_h(f)$
for the number of monic irreducible $P$ that divide $f$ exactly $h$ times. For monic irreducible
$P$ and $j < h$ put $|P| = q^{\deg P}$, $y_{P,j} = (q^{1/h}\xi^j)^{-\deg P}$ with $q^{1/h} > 0$,
and $K(P, h, j) = (1 - y_{P,j})/(|P|(1 - y_{P,j}) + 1)$. Let
$\kappa_j = \sum_P (K(P, h, j) - |P|^{-1})$ and
$\Pi_j = \prod_P (1 - |P|^{-1})(1 + |P|^{-1}(1 - y_{P,j})^{-1})$, with sum and product over monic
irreducible $P$, and for $X = (X_j)_j$ put
$W_n(X) = |N_h \cap M_n|^{-1} (q^{n/h}/h) \sum_{j=0}^{h-1} \xi^{jn} \Pi_j X_j$. Let $B_1$ be the
function field Mertens constant and $L_n = \log(n/h)$. Then, as $n \to \infty$,
the mean of $\omega_h^2$ over $N_h \cap M_n$ is
$L_n^2 + (2B_1 + 1 + 2W_n(\kappa)) L_n + B_1^2 + B_1 - \pi^2/6 + W_n(X) + O(n^{\varepsilon - 1})$,
where $X_j = -\sum_P K(P, h, j)^2 + \kappa_j^2 + (2B_1 + 1)\kappa_j$.

This follows the paper's proof: the printed constant term $C_3$ has $-W_n(Z)$ in place of
$W_n(X)$, where $Z_j = \sum_P K(P, h, j)^2 + \kappa_j^2 + (2B_1 + 1)\kappa_j$; this contradicts
the final display of the proof (page 29) and the printed variance.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5, Equation (9).

Stated but not proved: `MetaMathlibExt.omegaH_hFull_secondMoment_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 1012](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L1012). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-h-h-full-second-moment-asymptotic).

## Variance of $\omega_h$ over $h$-full polynomials

Let $F$ be a finite field with $q$
elements, let $h \ge 2$, let $\xi \in \mathbb{C}$ be a primitive $h$-th root of unity, and let
$\varepsilon > 0$. Write $N_h \cap M_n$ for the set of monic polynomials $f$ of degree $n$ over $F$
that are $h$-full (if a monic irreducible $P$ divides $f$, then so does $P^h$), and $\omega_h(f)$
for the number of monic irreducible $P$ that divide $f$ exactly $h$ times. For monic irreducible
$P$ and $j < h$ put $|P| = q^{\deg P}$, $y_{P,j} = (q^{1/h}\xi^j)^{-\deg P}$ with $q^{1/h} > 0$,
and $K(P, h, j) = (1 - y_{P,j})/(|P|(1 - y_{P,j}) + 1)$. Let
$\kappa_j = \sum_P (K(P, h, j) - |P|^{-1})$ and
$\Pi_j = \prod_P (1 - |P|^{-1})(1 + |P|^{-1}(1 - y_{P,j})^{-1})$, with sum and product over monic
irreducible $P$, and for $X = (X_j)_j$ put
$W_n(X) = |N_h \cap M_n|^{-1} (q^{n/h}/h) \sum_{j=0}^{h-1} \xi^{jn} \Pi_j X_j$. Let $B_1$ be the
function field Mertens constant and $L_n = \log(n/h)$. Then, as $n \to \infty$,
the variance of $\omega_h$ over $N_h \cap M_n$ (the mean of $\omega_h^2$ minus the square of the
mean of $\omega_h$) is
$L_n + B_1 - \pi^2/6 + W_n(Y) - W_n(\kappa)^2 + O(n^{\varepsilon - 1})$, where
$Y_j = -\sum_P K(P, h, j)^2 + \kappa_j^2 + \kappa_j$.

The printed display writes $\omega_1$ for $\omega_h$ in the definition of the variance and omits
the factor $q^{n/h}/h$ in both weighted sums; both are restored as in Equations (8) and (9), from
which the paper derives the variance.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 5.

Stated but not proved: `MetaMathlibExt.omegaH_hFull_variance_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 1034](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L1034). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-h-h-full-variance-asymptotic).

## Mean of $\omega_k$ over $h$-full polynomials for $k > h$

Let $F$ be a finite field with
$q$ elements, let $2 \le h < k$, let $\xi \in \mathbb{C}$ be a primitive $h$-th root of unity and
let $\varepsilon > 0$. Write $M_n$ for the set of monic polynomials of degree $n$ over $F$, $N_h$
for the set of $h$-full monic polynomials, $|P| = q^{\deg P}$, and $\omega_k(f)$ for the number of
monic irreducible $P$ dividing $f$ whose multiplicity in $f$ is exactly $k$. For $j < h$ and a
monic irreducible $P$ put $y_{P,j} = (q^{1/h}\xi^j)^{-\deg P}$, where $q^{1/h}$ is the positive
real root, $K(P, h, j) = (1 - y_{P,j})/(|P|(1 - y_{P,j}) + 1)$ and
$b_P(j) = |P| (q^{1/h}\xi^j)^{-k \deg P} K(P, h, j)$, and let
$\Pi_j = \prod_P (1 - 1/|P|)(1 + 1/(|P|(1 - y_{P,j})))$, where sums and products over $P$ run
over the monic irreducible polynomials. For $X = (X_0, \dots, X_{h-1}) \in \mathbb{C}^h$ let
$W_n(X) = |N_h \cap M_n|^{-1} (q^{n/h}/h) \sum_{j\lt h} \xi^{jn} \Pi_j X_j$. Then the mean of
$\omega_k$ over $N_h \cap M_n$ equals
$W_n\bigl(\sum_P b_P(0), \dots, \sum_P b_P(h-1)\bigr) + O(q^{-n/(h(h+1)) + \varepsilon n})$ as
$n \to \infty$.

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 7.

Stated but not proved: `MetaMathlibExt.omegaMult_hFull_mean_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 1053](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L1053). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-h-full-mean-asymptotic).

## Second moment of $\omega_k$ over $h$-full polynomials for $k > h$

Let $F$ be a finite
field with $q$ elements, let $2 \le h < k$, let $\xi \in \mathbb{C}$ be a primitive $h$-th root of
unity and let $\varepsilon > 0$. Write $M_n$ for the set of monic polynomials of degree $n$ over
$F$, $N_h$ for the set of $h$-full monic polynomials, $|P| = q^{\deg P}$, and $\omega_k(f)$ for the
number of monic irreducible $P$ dividing $f$ whose multiplicity in $f$ is exactly $k$. For $j < h$
and a monic irreducible $P$ put $y_{P,j} = (q^{1/h}\xi^j)^{-\deg P}$, where $q^{1/h}$ is the
positive real root, $K(P, h, j) = (1 - y_{P,j})/(|P|(1 - y_{P,j}) + 1)$ and
$b_P(j) = |P| (q^{1/h}\xi^j)^{-k \deg P} K(P, h, j)$, and let
$\Pi_j = \prod_P (1 - 1/|P|)(1 + 1/(|P|(1 - y_{P,j})))$, where sums and products over $P$ run
over the monic irreducible polynomials. For $X = (X_0, \dots, X_{h-1}) \in \mathbb{C}^h$ let
$W_n(X) = |N_h \cap M_n|^{-1} (q^{n/h}/h) \sum_{j\lt h} \xi^{jn} \Pi_j X_j$. Then the mean of
$\omega_k^2$ over $N_h \cap M_n$ equals $W_n(X) + O(q^{-n/(h(h+1)) + \varepsilon n})$ as
$n \to \infty$, where $X_j = (\sum_P b_P(j))^2 - \sum_P b_P(j)^2 + \sum_P b_P(j)$.

This is the reading of the paper's proof. The printed statement has
$\sum_P b_P^2 - (\sum_P b_P)^2$ (with $b_P = b_P(j)$) with the signs swapped, contradicting the
computation of the second derivative in $z$ of the paper's generating function $B_{k,N_h}(u, z)$
at the end of the proof (page 31).

## Sources

- Juan Arévalo Gómez and Matilde Lalín, *Prime Factors with Given Multiplicity in h-Free and h-Full Polynomials over Function Fields*, INTEGERS 25 (2025), Article A9, Theorem 7.

Stated but not proved: `MetaMathlibExt.omegaMult_hFull_secondMoment_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean, line 1069](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FunctionFieldMultiplicityWanted.lean#L1069). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html#omega-mult-h-full-second-moment-asymptot).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime factors of given multiplicity in h-free polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/function-fields/prime-factors-of-given-multiplicity-in-h-free-po)
