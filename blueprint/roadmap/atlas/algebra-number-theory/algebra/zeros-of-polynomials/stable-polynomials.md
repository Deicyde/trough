---
declaration: section
origin: cited
lean: MvPolynomial.IsStable, MvPolynomial.IsRealStable, MvPolynomial.univariateSpecialization, MvPolynomial.derivative_univariateSpecialization, MvPolynomial.eval_univariateSpecialization, MvPolynomial.map_star_univariateSpecialization, MvPolynomial.IsStable.roots_im_nonpos_univariateSpecialization, MvPolynomial.isRealRooted_univariateSpecialization_of_isRealStable
statement: formalized
proof: formalized
---

# Stable polynomials

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html).

## Mv Polynomial

## Stable polynomials

A complex multivariate polynomial is stable if it has no zero when
every variable lies in the open upper half-plane.

Formalized by `MvPolynomial.IsStable`, a definition declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#is-stable).

## Real stable polynomials

A complex multivariate polynomial is real stable if it is stable
and has real coefficients.

Formalized by `MvPolynomial.IsRealStable`, a definition declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#is-real-stable).

## Univariate specialization

Let $R$ be a commutative ring, let $p$ be a multivariate
polynomial over $R$ in variables $X_j$ indexed by $j \in \sigma$, and let $i \in \sigma$ and
$x : \sigma \to R$. The univariate specialization of $p$ at $i$ and $x$ is the polynomial in
$R[X]$ obtained from $p$ by substituting $X$ for $X_i$ and the constant $x_j$ for every $X_j$ with
$j \ne i$; the value $x_i$ is not used.

Formalized by `MvPolynomial.univariateSpecialization`, a definition declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#univariate-specialization).

## Partial derivatives under univariate specialization

Let $R$ be a commutative ring, let
$p$ be a multivariate polynomial over $R$ in variables $X_j$ indexed by $j \in \sigma$, let
$i \in \sigma$ and $x : \sigma \to R$, and for a polynomial $q$ write $q_{i,x} \in R[X]$ for its
univariate specialization that keeps $X_i$ as the variable $X$ and sets every other $X_j$ to
$x_j$. Then $(\partial p / \partial X_i)_{i,x} = (p_{i,x})'$, the derivative of $p_{i,x}$.

Formalized by `MvPolynomial.derivative_univariateSpecialization`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#derivative-univariate-specialization).

## Evaluating a univariate specialization

Let $R$ be a commutative ring, let $p$ be a
multivariate polynomial over $R$ in variables $X_j$ indexed by $j \in \sigma$, and let
$i \in \sigma$, $x : \sigma \to R$ and $t \in R$. Evaluating at $t$ the univariate specialization
of $p$ that keeps $X_i$ as the variable and sets every other $X_j$ to $x_j$ gives $p(y)$, where
$y_i = t$ and $y_j = x_j$ for $j \ne i$.

Formalized by `MvPolynomial.eval_univariateSpecialization`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#eval-univariate-specialization).

## Univariate specialization at real values preserves real coefficients

Let $p$ be a
complex multivariate polynomial with real coefficients in variables $X_j$ indexed by
$j \in \sigma$, let $i \in \sigma$, and let $a : \sigma \to \mathbb{C}$ with $a_j$ real for every
$j \ne i$. Then the univariate specialization of $p$ that keeps $X_i$ as the variable and sets
every other $X_j$ to $a_j$ has real coefficients.

Formalized by `MvPolynomial.map_star_univariateSpecialization`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#map-star-univariate-specialization).

## Roots of specializations of stable polynomials lie in the closed lower half-plane

Let
$p$ be a stable complex multivariate polynomial in variables $X_j$ indexed by $j \in \sigma$, let
$i \in \sigma$, and let $a : \sigma \to \mathbb{C}$ with $\operatorname{Im} a_j \ge 0$ for every
$j \ne i$. If the univariate specialization of $p$ that keeps $X_i$ as the variable and sets every
other $X_j$ to $a_j$ is nonzero, then every root $w$ of it satisfies $\operatorname{Im} w \le 0$.

Formalized by `MvPolynomial.IsStable.roots_im_nonpos_univariateSpecialization`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 464](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L464). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#roots-im-nonpos-univariate-specializatio).

## Real-rootedness of univariate specializations of real stable polynomials

Let $p$ be a
real stable complex multivariate polynomial in variables $X_j$ indexed by $j \in \sigma$, let
$i \in \sigma$, and for $x : \sigma \to \mathbb{C}$ write $p_{i,x} \in \mathbb{C}[X]$ for the
univariate specialization of $p$ that keeps $X_i$ as the variable $X$ and sets every other $X_j$
to $x_j$. Suppose there is a natural number $d$ such that for every $x : \sigma \to \mathbb{C}$
the polynomial $p_{i,x}$ is monic of degree $d$. Then for every $a : \sigma \to \mathbb{C}$ with
$a_j$ real for all $j \ne i$, the polynomial $p_{i,a}$ is real-rooted.

Formalized by `MvPolynomial.isRealRooted_univariateSpecialization_of_isRealStable`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 576](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#is-real-rooted-univariate-specialization).

## Subtracting a partial derivative preserves stability

Let $p$ be a stable complex
multivariate polynomial in variables $X_j$ indexed by $j \in \sigma$, let $i \in \sigma$, and
write $\partial_i p$ for the partial derivative of $p$ with respect to $X_i$. Then
$p - \partial_i p$ is stable.

Formalized by `MvPolynomial.IsStable.sub_pderiv`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 645](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L645). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#sub-pderiv).

## Subtracting a partial derivative preserves real stability

Let $p$ be a real stable
complex multivariate polynomial in variables $X_j$ indexed by $j \in \sigma$, let $i \in \sigma$,
and write $\partial_i p$ for the partial derivative of $p$ with respect to $X_i$. Then
$p - \partial_i p$ is real stable.

Formalized by `MvPolynomial.IsRealStable.sub_pderiv`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#sub-pderiv-2).

## The mixed differential preserves stability

Let $p$ be a stable complex multivariate
polynomial in variables $X_s$ indexed by $s \in \sigma$, and write $\partial_s$ for the partial
derivative with respect to $X_s$. For every finite list $(i_1, \dots, i_k)$ of indices in
$\sigma$ (repetitions allowed, possibly empty), the mixed differential of $p$ along the list,
$(1 - \partial_{i_k}) \cdots (1 - \partial_{i_1})\, p$, is stable.

Formalized by `MvPolynomial.IsStable.mixedDifferential`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#mixed-differential).

## The mixed differential preserves real stability

Let $p$ be a real stable complex
multivariate polynomial in variables $X_s$ indexed by $s \in \sigma$, and write $\partial_s$ for
the partial derivative with respect to $X_s$. For every finite list $(i_1, \dots, i_k)$ of indices
in $\sigma$ (repetitions allowed, possibly empty), the mixed differential of $p$ along the list,
$(1 - \partial_{i_k}) \cdots (1 - \partial_{i_1})\, p$, is real stable.

Formalized by `MvPolynomial.IsRealStable.mixedDifferential`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/Stable.lean, line 704](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/Stable.lean#L704). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html#mixed-differential-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stable polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/stable-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/zeros-of-polynomials/stable-polynomials)
