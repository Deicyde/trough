---
declaration: section
origin: cited
lean: MetaMathlibExt.fermatUnitFunction, MetaMathlibExt.fermatUnitFunction_two_pow_sub_one, MetaMathlibExt.fermatUnitFunction_small_values, MetaMathlibExt.mobiusFermat_one_and_vanishing, MetaMathlibExt.mobiusFermat_eq_multinomial, MetaMathlibExt.vonMangoldtFermat_eq_multinomial, MetaMathlibExt.mobiusFermat_mul_factorial_eq_squarefree_part, MetaMathlibExt.mobiusFermat_three_pow_mul_seven_pow
statement: formalized
---

# Möbius–Fermat function

11 results, 3 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html).

## Fermat unit function

The Fermat unit function $u_M$ is the integer-valued arithmetic
function with $u_M(l) = 1$ when $l = 2^n - 1$ for some integer $n \ge 1$, and $u_M(l) = 0$
otherwise (in particular $u_M(0) = 0$). Equivalently, $u_M(l) = 1$ exactly when $l \ge 1$ and
$l + 1$ is a power of $2$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, equation (7).

Formalized by `MetaMathlibExt.fermatUnitFunction`, a definition declared in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#fermat-unit-function).

## The Fermat unit function at $2^n - 1$

For every integer $n \ge 1$, the Fermat unit
function $u_M$ satisfies $u_M(2^n - 1) = 1$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, equation (7).

Formalized by `MetaMathlibExt.fermatUnitFunction_two_pow_sub_one`, a theorem declared in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#fermat-unit-function-two-pow-sub-one).

## Small values of the Fermat unit function

The Fermat unit function $u_M$ satisfies
$u_M(1) = u_M(3) = u_M(7) = u_M(63) = 1$ and $u_M(2) = u_M(9) = 0$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, equation (7).

Formalized by `MetaMathlibExt.fermatUnitFunction_small_values`, a theorem declared in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#fermat-unit-function-small-values).

## The Möbius–Fermat and von Mangoldt–Fermat functions at $1$ and off the Fermat semigroup

**The Möbius–Fermat and von Mangoldt–Fermat functions at $1$ and off the Fermat
semigroup.** Let $u_M$ be the Fermat unit function
and let $\mu_M$ be an integer-valued arithmetic function with $\mu_M * u_M = \varepsilon$, where
$*$ is Dirichlet convolution and $\varepsilon$ is its identity, with $\varepsilon(1) = 1$ and
$\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the Dirichlet inverse of $u_M$, the
Möbius–Fermat function.
Let $\Lambda_M = \mu_M * u_M'$, computed with real values, where
$u_M'(l) = u_M(l) \log l$.
Then $\mu_M(1) = 1$ and $\Lambda_M(1) = 0$, and $\mu_M(l) = \Lambda_M(l) = 0$ for every natural
number $l$ outside the Fermat semigroup, the multiplicative submonoid of $\mathbb{N}$ generated
by the numbers $2^n - 1$ with $n \ge 2$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Proposition 2.

Stated but not proved: `MetaMathlibExt.mobiusFermat_one_and_vanishing` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#mobius-fermat-one-and-vanishing).

## Multinomial formula for the Möbius–Fermat function

Let $u_M$ be the Fermat unit function
and let $\mu_M$ be an integer-valued arithmetic function with $\mu_M * u_M = \varepsilon$, where
$*$ is Dirichlet convolution and $\varepsilon$ is its identity, with $\varepsilon(1) = 1$ and
$\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the Dirichlet inverse of $u_M$, the
Möbius–Fermat function.
Let $n_1, \dots, n_k$ be finitely many (possibly no) distinct integers with $n_i \ge 2$ and
$n_i \ne 6$, let $m_1, \dots, m_k \ge 1$ be integers, and put
$l = \prod_{i=1}^{k} (2^{n_i} - 1)^{m_i}$ and
$r = m_1 + \dots + m_k$. Suppose that $2$ is not among the $n_i$ or has exponent $1$, or that $3$
is not among the $n_i$; that is, the factor $3 = 2^2 - 1$ occurs at most to the first power or
the factor $7 = 2^3 - 1$ does not occur. Then, as rational numbers,
$\mu_M(l) = (-1)^r \, r! / (m_1! \cdots m_k!)$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Proposition 4.

Stated but not proved: `MetaMathlibExt.mobiusFermat_eq_multinomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#mobius-fermat-eq-multinomial).

## Multinomial formula for the von Mangoldt–Fermat function

Let $u_M$ be the Fermat unit
function, and let $\mu$ be an integer-valued arithmetic function with $\mu * u_M = \varepsilon$,
where $*$ is Dirichlet convolution and $\varepsilon$ is its identity (so $\mu$ is the
Möbius–Fermat function $\mu_M$). Let $\Lambda_M = \mu * u'_M$, computed with real values, where
$u'_M(l) = u_M(l) \log l$. Let $f : \mathbb{N} \to \mathbb{N}$ be finitely supported, with
$n \ge 2$ and $n \ne 6$ for every $n$ such that $f(n) \ne 0$, and with $f(2) \le 1$ or $f(3) = 0$.
Put $l = \prod_n (2^n - 1)^{f(n)}$ and $r = \sum_n f(n)$. Then

$$\Lambda_M(l) = (-1)^{r - 1} \frac{(r - 1)!}{\prod_n f(n)!} \log l,$$

where $r - 1$ is read as $0$ when $r = 0$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Proposition 5.

Stated but not proved: `MetaMathlibExt.vonMangoldtFermat_eq_multinomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#von-mangoldt-fermat-eq-multinomial).

## Reduction of the Möbius–Fermat function to distinct factors

Let $u_M$ be the Fermat
unit function and let $\mu_M$ be an integer-valued arithmetic function with
$\mu_M * u_M = \varepsilon$, where $*$ is Dirichlet convolution and $\varepsilon$ is its
identity, with $\varepsilon(1) = 1$ and $\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the
Dirichlet inverse of $u_M$, the Möbius–Fermat function.
Let $m_1, m_2 \ge 0$ be integers, let $n_3, \dots, n_k$ be finitely many (possibly no) distinct
integers with $n_j \ge 4$ and $n_j \ne 6$, let $m_3, \dots, m_k \ge 1$ be integers, and put
$l = 3^{m_1} 7^{m_2} \prod_{j=3}^{k} (2^{n_j} - 1)^{m_j}$.
Then for every finite set $T$ of integers $n \ge 4$ with $n \ne 6$ and
$|T| = m_3 + \dots + m_k$,

$$\mu_M(l) \, m_3! \cdots m_k! = \mu_M\Big(3^{m_1} 7^{m_2} \prod_{n \in T} (2^n - 1)\Big).$$

In particular the right-hand side does not depend on the choice of $T$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Proposition 6.

Stated but not proved: `MetaMathlibExt.mobiusFermat_mul_factorial_eq_squarefree_part` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#mobius-fermat-mul-factorial-eq-squarefre).

## The Möbius–Fermat function at $3^m 7^n$

Let $u_M$ be the Fermat unit function
and let $\mu_M$ be an integer-valued arithmetic function with $\mu_M * u_M = \varepsilon$, where
$*$ is Dirichlet convolution and $\varepsilon$ is its identity, with $\varepsilon(1) = 1$ and
$\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the Dirichlet inverse of $u_M$, the
Möbius–Fermat function.
Then for all integers $m, n \ge 0$,

$$\mu_M(3^m 7^n) = (-1)^{m+n} \sum_{j=0}^{\min(\lfloor m/2 \rfloor, n)}
\binom{n}{j} \binom{m + n - 2j}{m - 2j},$$

and, as rational numbers,

$$\mu_M(3^m 7^n) = (-1)^{m+n} \sum_{j=0}^{\min(\lfloor m/2 \rfloor, n)}
\frac{(m + n - 2j)!}{(m - 2j)! \, (n - j)! \, j!}.$$

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Proposition 7.

Stated but not proved: `MetaMathlibExt.mobiusFermat_three_pow_mul_seven_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#mobius-fermat-three-pow-mul-seven-pow).

## The Möbius–Fermat function at $3^m 7^n q^k$

Let $u_M$ be the Fermat unit function
and let $\mu_M$ be an integer-valued arithmetic function with $\mu_M * u_M = \varepsilon$, where
$*$ is Dirichlet convolution and $\varepsilon$ is its identity, with $\varepsilon(1) = 1$ and
$\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the Dirichlet inverse of $u_M$, the
Möbius–Fermat function.
Let $t \ge 4$ be an integer with $t \ne 6$ and put $q = 2^t - 1$. Then for all integers
$m, n, k \ge 0$, as rational numbers,

$$\mu_M(3^m 7^n q^k) = (-1)^{m+n+k} \sum_{j=0}^{\min(\lfloor m/2 \rfloor, n)}
\frac{(m + n - 2j + k)!}{(m - 2j)! \, (n - j)! \, j! \, k!}.$$

The conditions on $t$ exclude $q = 1, 3, 7, 63$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Proposition 8.

Stated but not proved: `MetaMathlibExt.mobiusFermat_three_pow_mul_seven_pow_mul_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#mobius-fermat-three-pow-mul-seven-pow-mu).

## Closed form of the Möbius–Fermat function

Let $u_M$ be the Fermat unit function
and let $\mu_M$ be an integer-valued arithmetic function with $\mu_M * u_M = \varepsilon$, where
$*$ is Dirichlet convolution and $\varepsilon$ is its identity, with $\varepsilon(1) = 1$ and
$\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the Dirichlet inverse of $u_M$, the
Möbius–Fermat function.
Let $m_1, m_2 \ge 0$ be integers, let $n_3, \dots, n_k$ be finitely many (possibly no) distinct
integers with $n_j \ge 4$ and $n_j \ne 6$, let $m_3, \dots, m_k \ge 1$ be integers, and put
$l = 3^{m_1} 7^{m_2} \prod_{j=3}^{k} (2^{n_j} - 1)^{m_j}$ and
$r = m_1 + m_2 + m_3 + \dots + m_k$. Then, as rational numbers,

$$\mu_M(l) = (-1)^r \sum_{j=0}^{\min(\lfloor m_1/2 \rfloor, m_2)}
\frac{(r - 2j)!}{(m_1 - 2j)! \, (m_2 - j)! \, j! \, m_3! \cdots m_k!}.$$

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Theorem 9.

Stated but not proved: `MetaMathlibExt.mobiusFermat_closed_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#mobius-fermat-closed-form).

## Closed form of the von Mangoldt–Fermat function

Let $u_M$ be the Fermat unit function
and let $\mu_M$ be an integer-valued arithmetic function with $\mu_M * u_M = \varepsilon$, where
$*$ is Dirichlet convolution and $\varepsilon$ is its identity, with $\varepsilon(1) = 1$ and
$\varepsilon(l) = 0$ for $l \ne 1$; thus $\mu_M$ is the Dirichlet inverse of $u_M$, the
Möbius–Fermat function.
Let $\Lambda_M = \mu_M * u_M'$, computed with real values, where
$u_M'(l) = u_M(l) \log l$.
Let $m_1, m_2 \ge 0$ be integers, let $n_3, \dots, n_k$ be finitely many (possibly no) distinct
integers with $n_j \ge 4$ and $n_j \ne 6$, let $m_3, \dots, m_k \ge 1$ be integers, and put
$l = 3^{m_1} 7^{m_2} \prod_{j=3}^{k} (2^{n_j} - 1)^{m_j}$ and
$r = m_1 + m_2 + m_3 + \dots + m_k$. Then

$$\Lambda_M(l) = (-1)^{r-1} \Big(\sum_{j=0}^{\min(\lfloor m_1/2 \rfloor, m_2)}
\frac{(r - 2j - 1)!}{(m_1 - 2j)! \, (m_2 - j)! \, j! \, m_3! \cdots m_k!}\Big) \log l.$$

When $r = 0$, that is $l = 1$, both sides are $0$: on the right, $r - 1$ and $r - 2j - 1$ are
read as $0$ and $\log 1 = 0$.

## Sources

- J. L. Varona, *The Möbius and the von Mangoldt-type Functions of the Fermat Zeta Function*, INTEGERS 26 (2026), Article A106, Theorem 10.

Stated but not proved: `MetaMathlibExt.vonMangoldtFermat_closed_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/MobiusFermatWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MobiusFermatWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html#von-mangoldt-fermat-closed-form).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Möbius–Fermat function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/m-bius-fermat-function)
