---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.cartesianRealPart, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.cartesianImagPart, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.bddAbove_numericalRadius, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_nonneg, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.le_numericalRadius, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_le, MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_le_norm
statement: formalized
---

# Numerical range and numerical radius

37 results, 36 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html).

## Numerical radius

The numerical radius of a bounded linear operator $T$ on a complex
Hilbert space $H$ is the real number
$w(T) = \sup \{ |\langle T x, x \rangle| : x \in H,\ \|x\| = 1 \}$, the supremum of the moduli of
the values $\langle T x, x \rangle$ over the unit vectors of $H$ (taken to be $0$ when $H = 0$).

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-radius).

## Real Cartesian part of an operator

For a bounded linear operator $T$ on a complex Hilbert
space with adjoint $T^*$, the real Cartesian part of $T$ is the bounded linear operator
$(T + T^*)/2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.cartesianRealPart`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#cartesian-real-part).

## Imaginary Cartesian part of an operator

For a bounded linear operator $T$ on a complex
Hilbert space with adjoint $T^*$, the imaginary Cartesian part of $T$ is the bounded linear
operator $(T - T^*)/(2i)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.cartesianImagPart`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#cartesian-imag-part).

## The numerical-radius family is bounded above

Let $T$ be a bounded linear operator on a
complex inner product space $H$. The set $\{|\langle Tx, x\rangle| : x \in H,\ \|x\| = 1\}$ is
bounded above.

The proof shows that $\|T\|$ is an upper bound, by the Cauchy–Schwarz inequality.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.bddAbove_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#bdd-above-numerical-radius).

## Nonnegativity of the numerical radius

For every bounded operator $T$ on a complex inner
product space, the numerical radius $w(T)$ of $T$ satisfies $w(T) \ge 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_nonneg`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-radius-nonneg).

## The numerical radius bounds the quadratic form on unit vectors

Let $T$ be a bounded
linear operator on a complex inner product space $H$, with numerical radius $w(T)$. For every
$x \in H$ with $\|x\| = 1$, $|\langle Tx, x\rangle| \le w(T)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.le_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#le-numerical-radius).

## Bounding the numerical radius from above

Let $T$ be a bounded operator on a complex
inner product space $H$ and let $c \ge 0$ be a real number. If $|\langle T x, x\rangle| \le c$
for every unit vector $x \in H$, then the numerical radius of $T$ satisfies $w(T) \le c$.

The hypothesis $c \ge 0$ matters only when $H = 0$: there are no unit vectors, and $w(T) = 0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-radius-le).

## Numerical radius at most the operator norm

For every bounded operator $T$ on a complex
inner product space, the numerical radius $w(T)$ is at most the operator norm: $w(T) \le \|T\|$.

The proof is the Cauchy–Schwarz inequality.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_le_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-radius-le-norm).

## Quadratic form at the normalized vector

Let $T$ be a bounded operator on a complex inner
product space $H$. For every $x \in H$,
$\langle T(\|x\|^{-1} x), \|x\|^{-1} x \rangle = \|x\|^{-2} \langle T x, x \rangle$,
where $0^{-1}$ is read as $0$, so that for $x = 0$ both sides vanish.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.quadForm_scale`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#quad-form-scale).

## Normalizing a nonzero vector gives a unit vector

Let $x$ be a nonzero vector in a
complex inner product space. Then the vector $\|x\|^{-1} x$ has norm $1$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.norm_normalize`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#norm-normalize).

## Numerical radius bounds the normalized real part of the quadratic form

Let $T$ be a
bounded linear operator on a complex inner product space $H$, with numerical radius $w(T)$. For
every $x \in H$, $|\operatorname{Re} \langle Tx, x\rangle| / \|x\|^2 \le w(T)$, where division by
zero is taken to be $0$, so the case $x = 0$ is trivial.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.abs_re_quadForm_div_le_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#abs-re-quad-form-div-le-numerical-radius).

## Numerical radius bounds the normalized imaginary part of the quadratic form

Let $T$ be
a bounded linear operator on a complex inner product space $H$, with numerical radius $w(T)$. For
every $x \in H$, $|\operatorname{Im} \langle Tx, x\rangle| / \|x\|^2 \le w(T)$, where division by
zero is taken to be $0$, so the case $x = 0$ is trivial.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.abs_im_quadForm_div_le_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#abs-im-quad-form-div-le-numerical-radius).

## Numerical radius bounds the Rayleigh quotient

Let $T$ be a bounded linear operator on a
complex inner product space $H$, with numerical radius $w(T)$. For every $x \in H$, the Rayleigh
quotient $R_T(x) = \operatorname{Re} \langle Tx, x\rangle / \|x\|^2$, taken to be $0$ at $x = 0$,
satisfies $|R_T(x)| \le w(T)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.abs_rayleighQuotient_le_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#abs-rayleigh-quotient-le-numerical-radiu).

## Complex conjugate of one half

The complex conjugate of $1/2 \in \mathbb{C}$ is $1/2$, that
is, $\overline{1/2} = 1/2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.starRingEnd_half`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#star-ring-end-half).

## Complex conjugate of minus half the imaginary unit

The complex conjugate of
$-i/2 \in \mathbb{C}$ is $i/2$, that is, $\overline{-i/2} = i/2$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.starRingEnd_neg_I_div_two`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#star-ring-end-neg-i-div-two).

## The real Cartesian part is symmetric

For every bounded linear operator $T$ on a complex
Hilbert space $H$ with adjoint $T^*$, the real Cartesian part $A = (T + T^*)/2$ is symmetric:
$\langle Ax, y\rangle = \langle x, Ay\rangle$ for all $x, y \in H$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.isSymmetric_cartesianRealPart`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#is-symmetric-cartesian-real-part).

## The imaginary Cartesian part is symmetric

For every bounded linear operator $T$ on a
complex Hilbert space $H$ with adjoint $T^*$, the imaginary Cartesian part $B = (T - T^*)/(2i)$ is
symmetric: $\langle Bx, y\rangle = \langle x, By\rangle$ for all $x, y \in H$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.isSymmetric_cartesianImagPart`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#is-symmetric-cartesian-imag-part).

## Quadratic form of the real Cartesian part

Let $T$ be a bounded operator on a complex
Hilbert space $H$ and let $A = (T + T^*)/2$ be the real Cartesian part of $T$. Then for every
$x \in H$ one has $\langle A x, x \rangle = \operatorname{Re} \langle T x, x \rangle$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.quadForm_cartesianRealPart`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#quad-form-cartesian-real-part).

## Quadratic form of the imaginary Cartesian part

Let $T$ be a bounded operator on a complex
Hilbert space $H$, whose inner product $\langle \cdot, \cdot \rangle$ is conjugate-linear in its
first argument, and let $B = (T - T^*)/(2i)$ be the imaginary Cartesian part of $T$. Then for
every $x \in H$ one has $\langle B x, x \rangle = -\operatorname{Im} \langle T x, x \rangle$.

The sign comes from the convention on the inner product: writing $T = A + iB$ with
$A = (T + T^*)/2$, one has
$\langle T x, x \rangle = \langle A x, x \rangle - i \langle B x, x \rangle$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.quadForm_cartesianImagPart`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#quad-form-cartesian-imag-part).

## Cartesian decomposition

Every bounded linear operator $T$ on a complex Hilbert space
satisfies $T = A + iB$, where $A = (T + T^*)/2$ and $B = (T - T^*)/(2i)$ are the real and
imaginary Cartesian parts of $T$ and $T^*$ is the adjoint of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.cartesian_decomposition`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#cartesian-decomposition).

## Norm of the real part is at most the numerical radius

Let $T$ be a bounded
operator on a complex Hilbert space, with adjoint $T^*$, and let $A = (T + T^*)/2$ be its real
Cartesian part. Then $\|A\| \le w(T)$, where $\|A\|$ is the operator norm of $A$ and $w(T)$ is
the numerical radius of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.norm_cartesianRealPart_le_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#norm-cartesian-real-part-le-numerical-ra).

## Norm of the imaginary part is at most the numerical radius

Let $T$ be a
bounded operator on a complex Hilbert space, with adjoint $T^*$, and let $B = (T - T^*)/(2i)$ be
its imaginary Cartesian part. Then $\|B\| \le w(T)$, where $\|B\|$ is the operator norm of $B$
and $w(T)$ is the numerical radius of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.norm_cartesianImagPart_le_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#norm-cartesian-imag-part-le-numerical-ra).

## Operator norm at most twice the numerical radius

For every bounded operator $T$ on a
complex Hilbert space, $\|T\| \le 2\,w(T)$, where $\|T\|$ is the operator norm and $w(T)$ is the
numerical radius of $T$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.norm_le_two_mul_numericalRadius`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#norm-le-two-mul-numerical-radius).

## Numerical radius of a self-adjoint operator

If $T$ is a self-adjoint bounded operator
on a complex Hilbert space, then its numerical radius equals its operator norm:
$w(T) = \|T\|$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_eq_norm_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-radius-eq-norm-of-is-self-adjo).

## The quadratic form of the adjoint has the same modulus

Let $T$ be a bounded operator
on a complex Hilbert space $H$, with adjoint $T^*$. For every $x \in H$,
$|\langle T^* x, x\rangle| = |\langle T x, x\rangle|$, since $\langle T^* x, x\rangle$ is the
complex conjugate of $\langle T x, x\rangle$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.norm_quadForm_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#norm-quad-form-adjoint).

## Numerical radius of the adjoint

For every bounded operator $T$ on a complex Hilbert
space, the numerical radius of its adjoint $T^*$ equals the numerical radius of $T$:
$w(T^*) = w(T)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRadius.numericalRadius_adjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRadius.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-radius-adjoint).

## Numerical range

For a bounded linear operator $A$ on a complex inner product space $E$,
the numerical range of $A$ is the set
$W(A) = \{\langle A x, x \rangle : x \in E,\ \|x\| = 1\} \subseteq \mathbb{C}$, where the inner
product $\langle \cdot, \cdot \rangle$ of $E$ is conjugate-linear in its first argument and linear
in its second.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzHausdorffWanted.numericalRange`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-range).

## Membership in the numerical range

Let $A$ be a bounded linear operator on a complex inner
product space $E$. A complex number $c$ lies in the numerical range $W(A)$ if and only if there is
a vector $x \in E$ with $\|x\| = 1$ and $\langle A x, x \rangle = c$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzHausdorffWanted.mem_numericalRange_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#mem-numerical-range-iff).

## Unit vectors give points of the numerical range

Let $A$ be a bounded linear operator on a
complex inner product space $E$. For every $x \in E$ with $\|x\| = 1$, the number
$\langle A x, x \rangle$ lies in the numerical range $W(A)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzHausdorffWanted.inner_mem_numericalRange`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#inner-mem-numerical-range).

## Toeplitz–Hausdorff theorem without completeness

The numerical range of a bounded linear
operator on a complex inner product space is convex. Completeness of the space is not needed.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzHausdorffWanted.toeplitz_hausdorff_general`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#toeplitz-hausdorff-general).

## Toeplitz–Hausdorff theorem

The numerical range of a bounded linear operator on a complex
Hilbert space is convex.

## Sources

- O. Toeplitz, Das algebraische Analogon zu einem Satze von Fejer, Math. Z. 2 (1918), 187-197, DOI 10.1007/BF01212904; F. Hausdorff, Der Wertvorrat einer Bilinearform, Math. Z. 3 (1919), 314-316, DOI 10.1007/BF01292610. It follows from `toeplitz_hausdorff_general`; the hypothesis `CompleteSpace E` is unused and keeps the source's shape.

Formalized by `MathlibExt.Analysis.InnerProductSpace.ToeplitzHausdorffWanted.toeplitz_hausdorff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/ToeplitzHausdorff.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#toeplitz-hausdorff).

## Conjugate shifts off the closed numerical range are invertible

Let $A$ be a bounded
linear operator on a complex Hilbert space $E$, whose inner product $\langle \cdot, \cdot \rangle$
is conjugate-linear in its first argument and linear in its second, let
$W(A) = \{\langle A x, x \rangle : x \in E,\ \|x\| = 1\}$ be the numerical range of $A$ and let
$\mu \in \mathbb{C}$. If $\mu$ is not in the closure of $W(A)$, then $A - \overline{\mu}\, I$,
where $\overline{\mu}$ is the complex conjugate of $\mu$ and $I$ is the identity operator, is
invertible in the algebra of bounded linear operators on $E$.

Both this operator and its adjoint are bounded below, so it is injective with closed range, and
its range has trivial orthogonal complement, hence it is surjective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRangeSpectrum.isUnit_of_notMem_closure_numericalRange`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#is-unit-of-not-mem-closure-numerical-ran).

## Conjugates of spectral values lie in the closed numerical range

Let $A$ be a bounded
linear operator on a complex Hilbert space $E$, whose inner product $\langle \cdot, \cdot \rangle$
is conjugate-linear in its first argument and linear in its second, and let
$W(A) = \{\langle A x, x \rangle : x \in E,\ \|x\| = 1\}$ be the numerical range of $A$. If $z$
is in the spectrum of $A$, then the complex conjugate $\overline{z}$ lies in the closure of
$W(A)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRangeSpectrum.conj_mem_closure_numericalRange_of_mem_spectrum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#conj-mem-closure-numerical-range-of-mem).

## The spectrum lies in the conjugate of the closed numerical range

Let $A$ be a bounded
linear operator on a complex Hilbert space $E$, whose inner product $\langle \cdot, \cdot \rangle$
is conjugate-linear in its first argument and linear in its second, and let
$W(A) = \{\langle A x, x \rangle : x \in E,\ \|x\| = 1\}$ be the numerical range of $A$. Then
every point of the spectrum of $A$ is the complex conjugate $\overline{w}$ of some point $w$ of
the closure of $W(A)$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRangeSpectrum.spectrum_subset_star_image_closure_numericalRange`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#spectrum-subset-star-image-closure-numer).

## Conjugates of eigenvalues lie in the numerical range

Let $A$ be a bounded linear operator
on a complex inner product space $E$, whose inner product $\langle \cdot, \cdot \rangle$ is
conjugate-linear in its first argument and linear in its second, let
$W(A) = \{\langle A x, x \rangle : x \in E,\ \|x\| = 1\}$ be the numerical range of $A$ and let
$z \in \mathbb{C}$. If there is a vector $x \in E$ with $\|x\| = 1$ and $A x = z x$, then the
complex conjugate $\overline{z}$ lies in $W(A)$ itself, not just in its closure.

Indeed $\langle A x, x \rangle = \overline{z}$ for such a unit eigenvector $x$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRangeSpectrum.conj_mem_numericalRange_of_exists_unit_eigenvector`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#conj-mem-numerical-range-of-exists-unit).

## The numerical range is bounded by the operator norm

Let $A$ be a bounded linear operator
on a complex inner product space $E$. Then every point of the numerical range $W(A)$ has absolute
value at most the operator norm $\|A\|$: $W(A)$ lies in the closed disc of radius $\|A\|$ centred
at $0$.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NumericalRangeSpectrum.numericalRange_subset_closedBall_norm`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NumericalRangeSpectrum.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#numerical-range-subset-closed-ball-norm).

## Lower bound from the numerical range

Let $H$ be a complex Hilbert space with inner
product $\langle \cdot, \cdot \rangle$, conjugate-linear in the first argument and linear in the
second, and let $T : H \to H$ be a bounded linear operator. Let
$N(T) = \{\langle \psi, T\psi \rangle : \psi \in H,\ \|\psi\| = 1\} \subseteq \mathbb{C}$ be the
numerical range of $T$, and for $z \in \mathbb{C}$ let $d(z, N(T))$ be the infimum of the
distances from $z$ to the points of $N(T)$, taken to be $0$ when $N(T)$ is empty. Then for every
$\psi \in H$ and every $z \in \mathbb{C}$, $\|(T - zI)\psi\| \ge d(z, N(T))\,\|\psi\|$, where $I$
is the identity operator on $H$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Operator theory; General theory of linear operators), problem `ma_proofbench_l2_55`.

Stated but not proved: `MathlibExt.Analysis.OperatorTheory.NumericalRangeDistanceLowerBoundWanted.infDist_numericalRange_mul_norm_le_norm_sub_smul_apply` is written with `theorem_wanted` in [WantedExt/Analysis/OperatorTheory/NumericalRangeDistanceLowerBoundWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/OperatorTheory/NumericalRangeDistanceLowerBoundWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html#inf-dist-numerical-range-mul-norm-le-nor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Numerical range and numerical radius](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/spectral-theory/numerical-range-and-numerical-radius)
