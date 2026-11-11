---
declaration: section
origin: cited
lean: MetaMathlibExt.twoUnramifiedDegreeOnePrimes, MetaMathlibExt.mem_twoUnramifiedDegreeOnePrimes, MetaMathlibExt.ringOfIntegers_quotient_pow_ringEquiv_zmod_two_pow, MetaMathlibExt.generalizedFruit_no_solution_two_dvd, MetaMathlibExt.twoUnramifiedDegreeOnePrimes_nonempty_iff_quadratic, MetaMathlibExt.squarefree_one_mod_eight_relativeDensity, MetaMathlibExt.squarefree_count_arithmeticProgression_isEquivalent, MetaMathlibExt.weierstrass_torsion_not_primePow_integral
statement: formalized
---

# Generalized fruit equation

13 results, 4 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html).

## Unramified primes of degree one above $2$

For a number field $K$ with ring of integers
$\mathcal{O}_K$, $T_K$ is the set of prime ideals $P$ of $\mathcal{O}_K$ that contain $2$ and have
ramification index $e(P \mid 2) = 1$ and inertia degree $f(P \mid 2) = 1$ over $\mathbb{Z}$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Section 2 (definition of `T_K`).

Formalized by `MetaMathlibExt.twoUnramifiedDegreeOnePrimes`, a definition declared in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#two-unramified-degree-one-primes).

## Membership in $T_K$

Let $K$ be a number field with ring of integers $\mathcal{O}_K$, and
let $T_K$ be the set of prime ideals of $\mathcal{O}_K$ that contain $2$ and have ramification
index $1$ and inertia degree $1$ over $\mathbb{Z}$. Then an ideal $P$ of $\mathcal{O}_K$ lies in
$T_K$ if and only if $P$ is a prime ideal, $2 \in P$, and $P$ has ramification index $1$ and
inertia degree $1$ over $\mathbb{Z}$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Section 2.

Formalized by `MetaMathlibExt.mem_twoUnramifiedDegreeOnePrimes`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#mem-two-unramified-degree-one-primes).

## Quotients by powers of a prime in $T_K$

Let $K$ be a number field with ring of integers
$\mathcal{O}_K$, and let $P \in T_K$, that is, $P$ is a prime ideal of $\mathcal{O}_K$ lying over
$2$ with ramification index $1$ and inertia degree $1$ over $\mathbb{Z}$. Then for every $n \ge 1$
the ring $\mathcal{O}_K / P^n$ is isomorphic to $\mathbb{Z} / 2^n \mathbb{Z}$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Lemma 1.

Stated but not proved: `MetaMathlibExt.ringOfIntegers_quotient_pow_ringEquiv_zmod_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#ring-of-integers-quotient-pow-ring-equiv).

## No solutions of the generalized fruit equation with even $x$

Let $K$ be a number field
with ring of integers $\mathcal{O}_K$ such that some prime ideal of $\mathcal{O}_K$ lying over $2$
has ramification index $1$ and inertia degree $1$ over $\mathbb{Z}$. Let $a, b \in \mathcal{O}_K$
be nonzero, let $r \ge 2$ and $d \ge 3$ be odd natural numbers, and let $c = 2^d b - 3^r$. Then
the equation $a x^d - y^2 - z^2 + x y z - c = 0$ has no solution $(x, y, z) \in \mathcal{O}_K^3$
with $2 \mid x$ in $\mathcal{O}_K$.

The hypothesis that $r$ is odd cannot be dropped: over $K = \mathbb{Q}$ with $a = b = 1$, $d = 3$
and $r = 2$ (so $c = -1$), $(x, y, z) = (2, 3, 0)$ is a solution. The source states "integers
$r \ge 2$ and $d \ge 3$ odd"; its proof (arXiv:2408.12278, proof of Theorem 1) uses that $r$ is
odd, so oddness is read as applying to both $r$ and $d$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Theorem 1.

Stated but not proved: `MetaMathlibExt.generalizedFruit_no_solution_two_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#generalized-fruit-no-solution-two-dvd).

## Unramified degree-one primes above $2$ in quadratic fields

Let $t \ne 1$ be a squarefree
integer, and let $K$ be a number field of degree $2$ over $\mathbb{Q}$ that contains an element
$\alpha$ with $\alpha^2 = t$, so that $K = \mathbb{Q}(\sqrt{t})$. Then the set $T_K$ of prime
ideals of the ring of integers $\mathcal{O}_K$ above $2$ with ramification index $1$ and inertia
degree $1$ is nonempty if and only if $t \equiv 1 \pmod{8}$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Corollary 1.

Stated but not proved: `MetaMathlibExt.twoUnramifiedDegreeOnePrimes_nonempty_iff_quadratic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#two-unramified-degree-one-primes-nonempt).

## Relative density of square-free integers congruent to $1$ modulo $8$

As $X \to \infty$
through the natural numbers, the number of square-free integers $t$ with $1 \le t \le X$ and
$t \equiv 1 \pmod 8$, divided by the number of square-free integers $t$ with $1 \le t \le X$,
tends to $1/6$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Theorem 2.

Stated but not proved: `MetaMathlibExt.squarefree_one_mod_eight_relativeDensity` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#squarefree-one-mod-eight-relative-densit).

## Square-free integers in an arithmetic progression

Let $r \in \mathbb{Z}$ and let $N \ge 1$
be an integer such that $s = \gcd(r, N)$ is square-free. Then, as the real number $X \to \infty$,
the number of square-free integers $t$ with $1 \le t \le X$ and $t \equiv r \pmod N$ is
asymptotically equivalent to

$$
\frac{\varphi(N)}{s \, \varphi(N/s) \, N} \prod_{q \mid N} \left(1 - \frac{1}{q^2}\right)^{-1}
\frac{6}{\pi^2} X,
$$

where $\varphi$ is Euler's totient function and the product runs over the primes $q$ dividing $N$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Theorem 3, quoted from their reference [2].

Stated but not proved: `MetaMathlibExt.squarefree_count_arithmeticProgression_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#squarefree-count-arithmetic-progression).

## Torsion points of non-prime-power order are integral

Let $K$ be a number field with ring
of integers $\mathcal{O}_K$, and let $E$ be a Weierstrass curve with coefficients in
$\mathcal{O}_K$ whose base change to $K$ is an elliptic curve. If $P = (x, y) \in E(K)$ is a
point of finite order $m \ge 2$ and $m$ is not a prime power, then $x$ and $y$ lie in
$\mathcal{O}_K$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Theorem 5, quoted from Silverman, *The Arithmetic of Elliptic Curves*.

Stated but not proved: `MetaMathlibExt.weierstrass_torsion_not_primePow_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#weierstrass-torsion-not-prime-pow-integr).

## Nagell–Lutz integrality

Let $E : y^2 = x^3 + A x + B$ be an elliptic curve over
$\mathbb{Q}$ with $A, B \in \mathbb{Z}$. Every point $P = (x, y) \in E(\mathbb{Q})$ of finite order
$m \ge 2$ has $x, y \in \mathbb{Z}$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Theorem 6, quoted from Silverman, *The Arithmetic of Elliptic Curves*.

Stated but not proved: `MetaMathlibExt.short_weierstrass_torsion_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#short-weierstrass-torsion-integral).

## The Weierstrass curve $E_\alpha$ of the generalized fruit equation

For a commutative ring
$R$ and $\alpha \in R$, $E_\alpha$ is the Weierstrass curve over $R$ with coefficients
$a_1 = -\alpha$, $a_2 = a_3 = a_4 = 0$ and $a_6 = -(\alpha^2 + 5)$, that is, the curve
$y^2 - \alpha x y = x^3 - (\alpha^2 + 5)$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Theorem 4, Equation (4.1).

Formalized by `MetaMathlibExt.fruitWeierstrassCurve`, a definition declared in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#fruit-weierstrass-curve).

## Discriminant of the curve $E_\alpha$

For every commutative ring $R$ and every
$\alpha \in R$, the Weierstrass curve $E_\alpha : y^2 - \alpha x y = x^3 - (\alpha^2 + 5)$ over $R$
has discriminant $\alpha^8 + 5\alpha^6 - 432\alpha^4 - 4320\alpha^2 - 10800$.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, proof of Theorem 4.

Formalized by `MetaMathlibExt.fruitWeierstrassCurve_Δ`, a theorem declared in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#fruit-weierstrass-curve-2).

## Torsion points of $E_\alpha$ with even integral $x$-coordinate have prime-power order

Let
$K$ be a number field with ring of integers $\mathcal{O}_K$ such that some prime ideal of
$\mathcal{O}_K$ lying over $2$ has ramification index $1$ and inertia degree $1$ over $\mathbb{Z}$.
Let $\alpha \in \mathcal{O}_K$ satisfy
$\alpha^8 + 5\alpha^6 - 432\alpha^4 - 4320\alpha^2 - 10800 \neq 0$, and let $E_\alpha$ be the curve
$y^2 - \alpha x y = x^3 - (\alpha^2 + 5)$ over $K$. If $P = (x_0, y_0) \in E_\alpha(K)$ is a point
of finite order with $x_0 \in \mathcal{O}_K$ and $2 \mid x_0$ in $\mathcal{O}_K$, then the order of
$P$ is a prime power.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Corollary 2.

Stated but not proved: `MetaMathlibExt.fruitWeierstrassCurve_not_isOfFinOrder_of_two_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#fruit-weierstrass-curve-not-is-of-fin-or).

## Points of $E_\alpha(\mathbb{Q})$ with even numerator have infinite order

Let $\alpha$ be an
integer with $\alpha^8 + 5\alpha^6 - 432\alpha^4 - 4320\alpha^2 - 10800 \neq 0$, and let $E_\alpha$
be the curve $y^2 - \alpha x y = x^3 - (\alpha^2 + 5)$ over $\mathbb{Q}$. If
$P = (x_0, y_0) \in E_\alpha(\mathbb{Q})$ is a point such that $x_0$, written in lowest terms, has
even numerator, then $P$ has infinite order.

## Sources

- Satyabrat Sahoo and Shanta Laishram, *Generalized Fruit Diophantine Equation over Number Fields*, INTEGERS 26 (2026), Article A21, Corollary 3.

Stated but not proved: `MetaMathlibExt.fruitWeierstrassCurve_rat_not_isOfFinOrder_of_two_dvd_num` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GeneralizedFruitDiophantineWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html#fruit-weierstrass-curve-rat-not-is-of-fi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized fruit equation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/generalized-fruit-equation)
