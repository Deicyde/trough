---
declaration: section
origin: cited
lean: MetaMathlibExt.SelbergClassFunction, MetaMathlibExt.SelbergClassFunction.degree, MetaMathlibExt.SelbergClassFunction.degree_nonneg, MetaMathlibExt.SelbergClassFunction.differentiableAt_toFun, MetaMathlibExt.SelbergClassFunction.aPointCount, MetaMathlibExt.SelbergClassFunction.aPointCount_of_nonpos, MetaMathlibExt.SelbergClassFunction.exists_no_aPoint_right, MetaMathlibExt.SelbergClassFunction.iteratedDeriv_reflected_asymptotic
statement: formalized
---

# a-points of Selberg class functions

16 results, 6 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html).

## The Selberg class

## Functions in the Selberg class

A function in the Selberg class consists of Dirichlet
coefficients $a \colon \mathbb{N} \to \mathbb{C}$, a function $F \colon \mathbb{C} \to \mathbb{C}$,
a number $r \in \mathbb{N}$ of Gamma factors, a conductor $Q > 0$, real numbers
$\lambda_1, \dots, \lambda_r > 0$, complex numbers $\mu_1, \dots, \mu_r$ with
$\operatorname{Re} \mu_j \ge 0$ and a root number $\omega \in \mathbb{C}$ with $|\omega| = 1$,
such that:

- $a(1) = 1$;
- for every $s$ with $\operatorname{Re} s > 1$ the Dirichlet series $\sum_{n \ge 1} a(n) n^{-s}$
  converges absolutely and equals $F(s)$;
- (Ramanujan hypothesis) for every $\varepsilon > 0$ there is a constant $C$ with
  $|a(n)| \le C n^{\varepsilon}$ for all $n$;
- (Euler product) there are $b \colon \mathbb{N} \to \mathbb{C}$ with $b(n) = 0$ unless $n$ is a
  prime power, a real $\theta < 1/2$ and a constant $C$ with $|b(n)| \le C n^{\theta}$ for all $n$,
  and a real $\sigma_0$ such that for every $s$ with $\operatorname{Re} s > \sigma_0$ the series
  $\sum_{n \ge 1} b(n) n^{-s}$ converges absolutely and $F(s) = \exp \sum_{n \ge 1} b(n) n^{-s}$;
- (analytic continuation) there are $m \in \mathbb{N}$, an entire function $g$ and real numbers
  $\rho$, $A$ with $|g(s)| \le A e^{|s|^{\rho}}$ for all $s$ (so $g$ has finite order) and
  $g(s) = (s - 1)^m F(s)$ for all $s \ne 1$;
- (functional equation) with $\Phi(s) = F(s) Q^s \prod_{j=1}^r \Gamma(\lambda_j s + \mu_j)$, the
  identity $\Phi(s) = \omega \overline{\Phi(1 - \bar s)}$ holds for every $s \ne 0, 1$ such that
  for no $j$ is $\lambda_j s + \mu_j$ or $\lambda_j (1 - \bar s) + \mu_j$ an integer $\le 0$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Section 2.

Formalized by `MetaMathlibExt.SelbergClassFunction`, a structure declared in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#selberg-class-function).

## Degree of a function in the Selberg class

For a function $F$ in the Selberg class whose
functional equation has Gamma-factor scalings $\lambda_1, \dots, \lambda_r$, the degree of $F$ is
$d_F = 2 \sum_{j=1}^{r} \lambda_j$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Section 2.

Formalized by `MetaMathlibExt.SelbergClassFunction.degree`, a definition declared in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#degree).

## Nonnegativity of the degree

Let $F$ be a function in the Selberg class with Gamma-factor
scalings $\lambda_1, \dots, \lambda_r$. Then the degree $d_F = 2 \sum_{j=1}^{r} \lambda_j$
satisfies $d_F \ge 0$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Section 2.

Formalized by `MetaMathlibExt.SelbergClassFunction.degree_nonneg`, a theorem declared in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#degree-nonneg).

## Holomorphy of Selberg class functions away from $s = 1$

For a function $F$ in the
Selberg class, $F$ is complex differentiable at every $s \in \mathbb{C}$ with $s \ne 1$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Section 2.

Formalized by `MetaMathlibExt.SelbergClassFunction.differentiableAt_toFun`, a theorem declared in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#differentiable-at-to-fun).

## Counting function of a-points of derivatives

Let $F$ be a function in the Selberg class,
$k \in \mathbb{N}$, $a \in \mathbb{C}$ and $E_2, E_1, T \in \mathbb{R}$. Then $N_k(a; T, F)$ is the
number of points $\rho$ with $F^{(k)}(\rho) = a$, where $F^{(k)}$ is the $k$-th derivative of $F$,
in the rectangle $E_2 < \operatorname{Re} \rho < E_1$, $0 < \operatorname{Im} \rho < T$, each
counted with its multiplicity as a zero of $F^{(k)} - a$.

A point near which $F^{(k)} - a$ vanishes identically is given multiplicity $0$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Theorem 1 and Section 2.

Formalized by `MetaMathlibExt.SelbergClassFunction.aPointCount`, a definition declared in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#a-point-count).

## The a-point count vanishes at nonpositive height

Let $F$ be a function in the Selberg
class, $k \in \mathbb{N}$, $a \in \mathbb{C}$ and $E_2, E_1 \in \mathbb{R}$. If $T \le 0$, then
$N_k(a; T, F) = 0$, where $N_k(a; T, F)$ is the number of a-points of the $k$-th derivative
$F^{(k)}$, counted with multiplicity, in $E_2 < \operatorname{Re} s < E_1$,
$0 < \operatorname{Im} s < T$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Theorem 1.

Formalized by `MetaMathlibExt.SelbergClassFunction.aPointCount_of_nonpos`, a theorem declared in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#a-point-count-of-nonpos).

## Lemma 1 (no a-points of derivatives far to the right)

Let $F$ be a function in the
Selberg class with Dirichlet coefficients $a(n)$, let $k \ge 1$, and let $a \in \mathbb{C}$ be such
that $a \ne 0$ or $a(n) \ne 0$ for some $n \ge 2$. Then there is a real number $E_1 \ge 1$ such
that the $k$-th derivative $F^{(k)}$ satisfies $F^{(k)}(s) \ne a$ for every $s \in \mathbb{C}$
with $\operatorname{Re} s \ge E_1$.

For $F = 1$ and $a = 0$ every point is a $0$-point, so the hypothesis on $a$ cannot be dropped.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 1.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.exists_no_aPoint_right` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#exists-no-a-point-right).

## Asymptotics of the derivatives of the reflected function (Lemma 2)

Let $F$ be a function
in the Selberg class with Gamma-factor data $\lambda_j$, $\mu_j$ for $1 \le j \le r$, conductor
$Q$, root number $\omega$ and degree $d_F = 2 \sum_j \lambda_j$, let $k \ge 1$ and let $c > 1$.
Write $\log$ for the principal branch of the logarithm and put

$$M(s) = \frac{d_F^k}{\pi^r \omega} Q^{2s - 1}
\prod_{j=1}^r \Gamma(\lambda_j s + \mu_j) \Gamma(\lambda_j s + 1 - \lambda_j - \bar\mu_j)
\prod_{j=1}^r \sin\bigl(\pi (\lambda_j + \bar\mu_j - \lambda_j s)\bigr) (\log s)^k F(s).$$

Let $G(w) = \overline{F(1 - \bar w)}$ and let $G^{(k)}$ be its $k$-th derivative. Then there are
real numbers $\tau$ and $C$ such that $|G^{(k)}(s) - M(s)| \le C |M(s)| / |\log s|$ for every
$s \in \mathbb{C}$ with $\operatorname{Re} s > c$ and $|\operatorname{Im} s| \ge \tau$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 2.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.iteratedDeriv_reflected_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#iterated-deriv-reflected-asymptotic).

## No $a$-points of derivatives far to the left (Lemma 3)

Let $F$ be a function in the
Selberg class with Dirichlet coefficients $a(n)$, let $k \ge 1$, and let $a \in \mathbb{C}$ be such
that $a \ne 0$ or $a(n) \ne 0$ for some $n \ge 2$. Then there are real numbers $E_2 \le 0$ and
$\tau$ such that the $k$-th derivative $F^{(k)}$ satisfies $F^{(k)}(s) \ne a$ for every
$s \in \mathbb{C}$ with $\operatorname{Re} s \le E_2$ and $|\operatorname{Im} s| \ge \tau$.

For $F = 1$ and $a = 0$ every point is a $0$-point, so the hypothesis on $a$ cannot be dropped.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 3.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.exists_no_aPoint_left` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#exists-no-a-point-left).

## Lemma 4 (a-points of derivatives in windows of unit height)

Let $F$ be a function in the
Selberg class with Dirichlet coefficients $a(n)$, let $k \ge 1$, and let $a \in \mathbb{C}$ be such
that $a \ne 0$ or $a(n) \ne 0$ for some $n \ge 2$. Let $E_2, E_1$ be real numbers and let
$N_k(a; T, F)$ be the number of a-points of the $k$-th derivative $F^{(k)}$, counted with
multiplicity, in $E_2 < \operatorname{Re} s < E_1$, $0 < \operatorname{Im} s < T$. Then
$N_k(a; T + 1, F) - N_k(a; T, F) = O(\log T)$ as $T \to \infty$.

The paper takes $E_1$ and $E_2$ from Lemmas 1 and 3; the bound is stated here for every strip.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 4.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.aPointCount_unit_window` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#a-point-count-unit-window).

## Local partial-fraction formula at the a-points of the k-th derivative (Lemma 5)

Let $F$
be a function in the Selberg class, let $k \ge 1$, write $F^{(k)}$ for the $k$-th derivative of
$F$, and let $a \in \mathbb{C}$ and let $\sigma_1$, $\sigma_2$ be real numbers. Then there are real
numbers $t_0$ and $C$ such that for every $s \in \mathbb{C}$ with
$\sigma_1 < \operatorname{Re} s < \sigma_2$, $\operatorname{Im} s \ge t_0$ and $F^{(k)}(s) \ne a$,

$$\left| \frac{F^{(k+1)}(s)}{F^{(k)}(s) - a} - \sum_{\rho} \frac{m(\rho)}{s - \rho} \right|
\le C \log \operatorname{Im} s,$$

where $\rho$ runs over the points with $F^{(k)}(\rho) = a$ and
$|\operatorname{Im} \rho - \operatorname{Im} s| \le 1$, and $m(\rho)$ is the order of the zero of
$F^{(k)} - a$ at $\rho$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 5.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.logDeriv_aPoint_partialFraction` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#log-deriv-a-point-partial-fraction).

## Lemma 6, case a ≠ 0 (expansion of the logarithmic derivative)

Let $F$ be a function in
the Selberg class with Dirichlet coefficients $a(n)$, let $k \ge 1$ and let $a \in \mathbb{C}$ with
$a \ne 0$. Then there is a real number $E$ such that for every $s \in \mathbb{C}$ with
$\operatorname{Re} s \ge E$,

$$
\frac{F^{(k+1)}(s)}{F^{(k)}(s) - a} = \sum_{l \ge 0} \sum_{n_0, \dots, n_l \ge 1}
\frac{(-1)^{k(l+1)}}{a^{l+1}} (\log n_0)^{k+1} (\log n_1 \cdots \log n_l)^k
\frac{a(n_0) \cdots a(n_l)}{n_0^s \cdots n_l^s},
$$

where $F^{(k)}$ is the $k$-th derivative of $F$ and the sum over all pairs of $l \ge 0$ and
positive integers $(n_0, \dots, n_l)$ converges unconditionally (equivalently, absolutely).

The paper sums over $n_i \ge \ell$, where $\ell \ge 2$ is least with $a(\ell) \ne 0$; the added
terms vanish because $\log 1 = 0$ and $a(n) = 0$ for $2 \le n < \ell$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 6.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.hasSum_logDeriv_aPoint_of_ne_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#has-sum-log-deriv-a-point-of-ne-zero).

## Expansion of the logarithmic derivative of the k-th derivative (Lemma 6, zeros case)

Let $F$ be a function in the Selberg class with Dirichlet coefficients $a(n)$, write $F^{(k)}$ for
the $k$-th derivative of $F$, let $k \ge 1$, and let $\ell \ge 2$ be such that $a(\ell) \ne 0$
and $a(n) = 0$ for $2 \le n < \ell$. Then there is a real number $E$ such that for every
$s \in \mathbb{C}$ with $\operatorname{Re} s \ge E$,

$$\frac{F^{(k+1)}(s)}{F^{(k)}(s)} = \sum_{l \ge 0} \sum_{n_0, \dots, n_l}
\left(\frac{-1}{a(\ell) (\log \ell)^k}\right)^{l+1} (\log n_0)^{k+1} (\log n_1 \cdots \log n_l)^k
\frac{\ell^{(l+1)s} a(n_0) \cdots a(n_l)}{(n_0 \cdots n_l)^s},$$

where the inner sum runs over the natural numbers $n_0 \ge \ell$ and $n_1, \dots, n_l \ge \ell + 1$,
and the sum over all pairs of $l$ and $(n_0, \dots, n_l)$ converges absolutely.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Lemma 6.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.hasSum_logDeriv_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#has-sum-log-deriv-zero).

## Asymptotic count of a-points of derivatives in the Selberg class

Let $F$ be a function in
the Selberg class with conductor $Q$, Gamma-factor scalings $\lambda_1, \dots, \lambda_r$ and
degree $d_F$, let $k \ge 1$ and $a \in \mathbb{C}$ with $a \ne 0$, and put
$\lambda = \prod_{j=1}^{r} \lambda_j^{2\lambda_j}$. Let $E_1, E_2, \tau$ be real numbers such that
the $k$-th derivative $F^{(k)}$ satisfies $F^{(k)}(s) \ne a$ whenever $\operatorname{Re} s \ge E_1$,
and $F^{(k)}(s) \ne a$ whenever $\operatorname{Re} s \le E_2$ and $|\operatorname{Im} s| \ge \tau$.
Let $N_k(a; T, F)$ be the number of a-points of $F^{(k)}$, counted with multiplicity, in the
rectangle $E_2 < \operatorname{Re} s < E_1$, $0 < \operatorname{Im} s < T$. Then, as $T \to \infty$,

$$
N_k(a; T, F) = \frac{d_F T}{2\pi} \log T + \frac{T}{2\pi} \log (\lambda Q^2) -
\frac{d_F T}{2\pi} + O(\log T).
$$

The bounds $E_1 \ge 1$ and $E_2 \le 0$ of Lemmas 1 and 3 are not needed and are dropped.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Theorem 1.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.aPointCount_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#a-point-count-asymptotic).

## Landau-type formula for the a-points of the k-th derivative (Theorem 2, a ≠ 0)

Let $F$ be
a function in the Selberg class with Dirichlet coefficients $a_F(n)$, write $F^{(k)}$ for the
$k$-th derivative of $F$, let $k \ge 1$, let $a \ne 0$ be a complex number and let $x > 1$ be
real. Let $E_1$, $E_2$ and $\tau$ be real numbers such that $F^{(k)}(s) \ne a$ whenever
$\operatorname{Re} s \ge E_1$, and whenever $\operatorname{Re} s \le E_2$ and
$|\operatorname{Im} s| \ge \tau$. Put

$$c = \sum_{l \ge 0} \sum_{n_0 \cdots n_l = x} \frac{(-1)^{k(l+1)}}{a^{l+1}} (\log n_0)^{k+1}
(\log n_1 \cdots \log n_l)^k a_F(n_0) \cdots a_F(n_l),$$

the inner sum over the natural numbers $n_0, \dots, n_l \ge 1$ with product $x$ (only finitely
many terms are nonzero, since a term vanishes when some $n_i = 1$). Then, as $T \to \infty$,

$$\sum_{\rho} m(\rho) x^{\rho} = \frac{T}{2\pi} c + O(\log T),$$

where $\rho$ runs over the points with $F^{(k)}(\rho) = a$, $E_2 < \operatorname{Re} \rho < E_1$
and $0 < \operatorname{Im} \rho < T$, and $m(\rho)$ is the order of the zero of $F^{(k)} - a$ at
$\rho$.

The paper takes $E_1$, $E_2$, $\tau$ from Lemmas 1 and 3 and restricts to $n_i \ge \ell$, where
$\ell \ge 2$ is least with $a_F(\ell) \ne 0$; the added terms vanish. Its closing remark that the
sum is empty for $x \notin \mathbb{Z}$ is immediate from the condition on the $n_i$.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Theorem 2.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.sum_aPoint_pow_of_ne_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#sum-a-point-pow-of-ne-zero).

## Landau-type formula for the zeros of the k-th derivative (Theorem 2, zeros case)

Let $F$
be a function in the Selberg class with Dirichlet coefficients $a(n)$, write $F^{(k)}$ for the
$k$-th derivative of $F$, let $k \ge 1$, let $\ell \ge 2$ be such that $a(\ell) \ne 0$ and
$a(n) = 0$ for $2 \le n < \ell$, and let $x > 1$ be real. Let $E_1$, $E_2$ and $\tau$ be real
numbers such that $F^{(k)}(s) \ne 0$ whenever $\operatorname{Re} s \ge E_1$, and whenever
$\operatorname{Re} s \le E_2$ and $|\operatorname{Im} s| \ge \tau$. Put

$$c = \sum_{l \ge 0} \sum_{n_0, \dots, n_l} \left(\frac{-1}{a(\ell) (\log \ell)^k}\right)^{l+1}
(\log n_0)^{k+1} (\log n_1 \cdots \log n_l)^k a(n_0) \cdots a(n_l),$$

the inner sum over the natural numbers $n_0 \ge \ell$ and $n_1, \dots, n_l \ge \ell + 1$ with
$n_0 \cdots n_l = x \ell^{l+1}$ (a finite sum, since $n_0 \cdots n_l \ge \ell (\ell + 1)^l$).
Then, as $T \to \infty$,

$$\sum_{\rho} m(\rho) x^{\rho} = \frac{T}{2\pi} c + O(\log T),$$

where $\rho$ runs over the zeros of $F^{(k)}$ with $E_2 < \operatorname{Re} \rho < E_1$ and
$0 < \operatorname{Im} \rho < T$, and $m(\rho)$ is the order of the zero of $F^{(k)}$ at $\rho$.

The paper takes $E_1$, $E_2$, $\tau$ from Lemmas 1 and 3. Its closing remark that the sum is
empty when $\ell^n x \notin \mathbb{Z}$ for all $n$ is not stated separately.

## Sources

- M. P. Chaudhary, Salem Guiben, Kamel Mazhouda and Mohammed Mekkaoui, *On the a-Points of the kth Derivative of an L-Function in the Selberg Class*, INTEGERS 24 (2024), Article A11, Theorem 2.

Stated but not proved: `MetaMathlibExt.SelbergClassFunction.sum_zero_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SelbergClassDerivativeAPointsWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html#sum-zero-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: a-points of Selberg class functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/a-points-of-selberg-class-functions)
