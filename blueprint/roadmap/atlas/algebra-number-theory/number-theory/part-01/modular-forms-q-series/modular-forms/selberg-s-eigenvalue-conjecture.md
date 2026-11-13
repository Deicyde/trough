---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.SelbergSpectralGap.IsCongruenceSubgroup, MathlibExt.NumberTheory.SelbergSpectralGap.isCongruenceSubgroup_top, MathlibExt.NumberTheory.SelbergSpectralGap.ext, MathlibExt.NumberTheory.SelbergSpectralGap.partialRe, MathlibExt.NumberTheory.SelbergSpectralGap.partialIm, MathlibExt.NumberTheory.SelbergSpectralGap.hyperbolicLaplacian, MathlibExt.NumberTheory.SelbergSpectralGap.hyperbolicLaplacian_const, MathlibExt.NumberTheory.SelbergSpectralGap.hyperbolicLaplacian_im_sq
statement: formalized
---

# Selberg's eigenvalue conjecture

26 results, 22 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html).

## Congruence subgroup of the modular group

A subgroup $\Gamma$ of
$\mathrm{SL}(2, \mathbb{Z})$ is a congruence subgroup if there is a positive integer $N$
such that every $\gamma \in \mathrm{SL}(2, \mathbb{Z})$ whose entries are congruent modulo
$N$ to those of the identity matrix lies in $\Gamma$; that is, $\Gamma$ contains the
principal congruence subgroup of level $N$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.IsCongruenceSubgroup`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#is-congruence-subgroup).

## The modular group is a congruence subgroup

The full group
$\mathrm{SL}(2, \mathbb{Z})$, as a subgroup of itself, is a congruence subgroup.

It contains the principal congruence subgroup of level $1$, which is the whole group.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.isCongruenceSubgroup_top`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#is-congruence-subgroup-top).

## Zero extension from the upper half plane

For a function $f$ from the upper half plane
to $\mathbb{C}$, its zero extension is the function from $\mathbb{C}$ to $\mathbb{C}$ that takes
the value $f(z)$ at every $z$ with $\operatorname{Im} z > 0$ and the value $0$ at every other
point.

It is used to read coordinate derivatives of $f$ in the interior.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.ext`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#ext).

## Partial derivative in the real direction

For a function
$f \colon \mathbb{H} \to \mathbb{C}$ and a point $z \in \mathbb{H}$, $\partial_x f(z)$ is the real
Fréchet derivative at $z$ of the zero extension of $f$ to $\mathbb{C}$, applied to the vector $1$.
When the zero extension is real-differentiable at $z$ this is the partial derivative of $f$ with
respect to $x = \operatorname{Re} z$; otherwise the value is $0$.

Real, not complex, differentiability is essential: with complex derivatives the two second
derivatives in the hyperbolic Laplacian would cancel by the Cauchy–Riemann equations, and the
Laplacian would vanish identically.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.partialRe`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#partial-re).

## Partial derivative in the imaginary direction

For a function
$f \colon \mathbb{H} \to \mathbb{C}$ and a point $z \in \mathbb{H}$, $\partial_y f(z)$ is the real
Fréchet derivative at $z$ of the zero extension of $f$ to $\mathbb{C}$, applied to the vector $i$.
When the zero extension is real-differentiable at $z$ this is the partial derivative of $f$ with
respect to $y = \operatorname{Im} z$; otherwise the value is $0$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.partialIm`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#partial-im).

## Hyperbolic Laplacian

For a function $f$ from the upper half plane to $\mathbb{C}$ and a
point $z = x + iy$ of the upper half plane, the hyperbolic Laplacian of $f$ at $z$ is

$$\Delta f(z) = -y^2 \left(\partial_x \partial_x f(z) + \partial_y \partial_y f(z)\right),$$

where, for a function $g$ from the upper half plane to $\mathbb{C}$, $\partial_x g(z)$ and
$\partial_y g(z)$ are the real Fréchet derivatives at $z$ of the zero extension of $g$ to
$\mathbb{C}$, applied to the vectors $1$ and $i$ respectively (taken to be $0$ where that
extension is not real differentiable).

On smooth functions this agrees with the coordinate formula
$-y^2 (\partial^2 f / \partial x^2 + \partial^2 f / \partial y^2)$ at every interior point.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.hyperbolicLaplacian`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#hyperbolic-laplacian).

## The hyperbolic Laplacian kills constants

For every complex number $c$ and every
point $z$ of the upper half plane, the hyperbolic Laplacian of the constant function with
value $c$ at $z$ is $0$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.hyperbolicLaplacian_const`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#hyperbolic-laplacian-const).

## Hyperbolic Laplacian of the squared imaginary part

Let $f$ be the function on the upper
half plane given by $f(u) = (\operatorname{Im} u)^2$, viewed as a complex number. Then for
every point $z$ of the upper half plane the hyperbolic Laplacian of $f$ at $z$ equals
$-2 (\operatorname{Im} z)^2$.

This is a non-holomorphic check: the value is not zero, whereas with complex derivatives the
computation would collapse by Cauchy--Riemann.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.hyperbolicLaplacian_im_sq`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#hyperbolic-laplacian-im-sq).

## Twice continuously differentiable functions on the upper half-plane

A function
$f \colon \mathbb{H} \to \mathbb{C}$ is smooth (of order two) when it is the restriction of a
function $F \colon \mathbb{C} \to \mathbb{C}$ that is twice continuously differentiable, in the real
sense, on the open set $\{z \in \mathbb{C} : \operatorname{Im} z > 0\}$.

Differentiability is real, not complex: eigenfunctions of the Laplacian need not be holomorphic.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.IsSmooth`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#is-smooth).

## Standard fundamental domain of the modular group

The standard fundamental domain for
$\mathrm{SL}(2, \mathbb{Z})$ is the set of points $z$ of the upper half plane with
$|\operatorname{Re} z| \le 1/2$ and $|z| \ge 1$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.fundamentalDomain`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#fundamental-domain).

## Finite coset covers of the modular group

A finite set
$s \subseteq \mathrm{SL}(2, \mathbb{Z})$ covers $\mathrm{SL}(2, \mathbb{Z})$ by cosets of a subgroup
$\Gamma$ when every $g \in \mathrm{SL}(2, \mathbb{Z})$ can be written as $g = \gamma a$ with
$\gamma \in \Gamma$ and $a \in s$, that is, when the cosets $\Gamma a$ with $a \in s$ cover
$\mathrm{SL}(2, \mathbb{Z})$. The elements of $s$ need not lie in distinct cosets.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.IsCosetCover`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#is-coset-cover).

## Square-integrable functions on a modular quotient

For a subgroup $\Gamma$ of
$\mathrm{SL}(2, \mathbb{Z})$, a function $f \colon \mathbb{H} \to \mathbb{C}$ is
square-integrable on $\Gamma \backslash \mathbb{H}$ when there is a finite set
$s \subseteq \mathrm{SL}(2, \mathbb{Z})$ whose cosets $\Gamma a$, $a \in s$, cover
$\mathrm{SL}(2, \mathbb{Z})$, such that

$$\int_{U} |f(z)|^2 \, d\mu(z) < \infty, \qquad U = \bigcup_{a \in s} a \cdot \mathcal{F},$$

where $\mathcal{F} = \{z \in \mathbb{H} : |\operatorname{Re} z| \le 1/2,\ |z| \ge 1\}$ is the
standard fundamental domain of $\mathrm{SL}(2, \mathbb{Z})$, $a \cdot \mathcal{F}$ is its image
under the Möbius action of $a$, and $\mu$ is the hyperbolic area measure $dx \, dy / y^2$ on
$\mathbb{H}$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.IsL2Quotient`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#is-l2-quotient).

## Eigenvalues of the hyperbolic Laplacian on a modular quotient

Let $\Gamma$ be a subgroup
of $\mathrm{SL}(2, \mathbb{Z})$. A real number $\lambda$ is an eigenvalue of the hyperbolic
Laplacian $\Delta$ for $\Gamma$ when there is a function $f \colon \mathbb{H} \to \mathbb{C}$ on
the upper half plane $\mathbb{H}$ such that $f$ is not identically zero, $f$ is the restriction of
a function on $\mathbb{C}$ that is twice continuously differentiable in the real sense on the
upper half plane, $f(\gamma z) = f(z)$ for every $\gamma \in \Gamma$ and every $z \in \mathbb{H}$
(Möbius action), $f$ is square-integrable on $\Gamma \backslash \mathbb{H}$, and
$\Delta f(z) = \lambda f(z)$ for every $z \in \mathbb{H}$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.IsEigenvalue`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#is-eigenvalue).

## Gap contributions of a subgroup of the modular group

For a subgroup $\Gamma$ of
$\mathrm{SL}(2, \mathbb{Z})$, the set of gap contributions of $\Gamma$ is the set of real
numbers consisting of $0$ together with $\sqrt{1/4 - \lambda}$ for every real eigenvalue
$\lambda$ of the hyperbolic Laplacian for $\Gamma$ with $0 < \lambda < 1/4$ (an exceptional
eigenvalue).

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.exceptionalGaps`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#exceptional-gaps).

## Gap parameter of a subgroup of the modular group

For a subgroup $\Gamma$ of
$\mathrm{SL}(2, \mathbb{Z})$, the gap parameter $\theta(\Gamma)$ is the supremum of the set of
gap contributions of $\Gamma$: the number $0$ together with $\sqrt{1/4 - \lambda}$ for every
real eigenvalue $\lambda$ of the hyperbolic Laplacian for $\Gamma$ with $0 < \lambda < 1/4$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.exceptionalGap`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#exceptional-gap).

## Selberg's congruence spectral-gap constant

Selberg's constant $C_{61}$ is the supremum of
the gap parameters $\theta(\Gamma)$ over all congruence subgroups $\Gamma$ of
$\mathrm{SL}(2, \mathbb{Z})$, where $\theta(\Gamma)$ is the supremum of $0$ and of the numbers
$\sqrt{1/4 - \lambda}$ for the eigenvalues $\lambda$ of $\Gamma$ with $0 < \lambda < 1/4$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.selbergConstant`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#selberg-constant).

## Selberg's eigenvalue conjecture

No congruence subgroup $\Gamma$ of
$\mathrm{SL}(2, \mathbb{Z})$ has an eigenvalue $\lambda$ with $0 < \lambda < 1/4$: for every
congruence subgroup $\Gamma$ and every eigenvalue $\lambda$ of $\Gamma$, either $\lambda \le 0$ or
$\lambda \ge 1/4$.

Here eigenvalues are realized by smooth square-integrable eigenfunctions, which captures the
discrete spectrum of the hyperbolic Laplacian.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.SelbergEigenvalueConjecture`, a definition declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#selberg-eigenvalue-conjecture).

## Exceptional eigenvalues bound the gap parameter

Let $\Gamma$ be a subgroup of
$\mathrm{SL}(2, \mathbb{Z})$ and let $\lambda$ be a real eigenvalue of the hyperbolic
Laplacian on $L^2(\Gamma \backslash \mathbb{H})$ with $0 < \lambda < 1/4$. Then
$\sqrt{1/4 - \lambda}$ is at most the gap parameter $\theta(\Gamma)$ of $\Gamma$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.sqrt_le_exceptionalGap`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#sqrt-le-exceptional-gap).

## Congruence gaps are bounded by Selberg's constant

For every congruence subgroup
$\Gamma$ of $\mathrm{SL}(2, \mathbb{Z})$, the gap parameter $\theta(\Gamma)$ is at most the
Selberg constant $C_{61}$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.exceptionalGap_le_selbergConstant`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#exceptional-gap-le-selberg-constant).

## Selberg's constant is at most one half

Selberg's constant $C_{61}$ satisfies
$C_{61} \le 1/2$.

This elementary bound follows directly from the definition.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.selbergConstant_le_half`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#selberg-constant-le-half).

## Exceptional eigenvalues bound Selberg's constant

Let $\Gamma$ be a congruence
subgroup of $\mathrm{SL}(2, \mathbb{Z})$ and let $\lambda$ be a real eigenvalue of the
hyperbolic Laplacian on $L^2(\Gamma \backslash \mathbb{H})$ with $0 < \lambda < 1/4$.
Then $\sqrt{1/4 - \lambda}$ is at most Selberg's constant $C_{61}$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.sqrt_le_selbergConstant`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#sqrt-le-selberg-constant).

## Selberg's constant vanishes exactly under Selberg's eigenvalue conjecture

Selberg's
constant $C_{61}$ equals $0$ if and only if Selberg's eigenvalue conjecture holds, that is, if and
only if no congruence subgroup of $\mathrm{SL}(2, \mathbb{Z})$ has an eigenvalue $\lambda$ with
$0 < \lambda < 1/4$.

Formalized by `MathlibExt.NumberTheory.SelbergSpectralGap.selbergConstant_eq_zero_iff`, a theorem declared in [MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ModularForms/SelbergSpectralGap.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#selberg-constant-eq-zero-iff).

## Selberg's 3/16 theorem

Let $\Gamma$ be a congruence subgroup of
$\mathrm{SL}(2, \mathbb{Z})$ and let $\lambda$ be a real eigenvalue of the hyperbolic Laplacian
$\Delta$ for $\Gamma$, that is, $\Delta f = \lambda f$ for some nonzero, twice continuously
differentiable, $\Gamma$-invariant function $f$ on the upper half plane that is square-integrable
on $\Gamma \backslash \mathbb{H}$. Then $\lambda$ does not lie in the open interval
$(0, 3/16)$: either $\lambda \le 0$ or $\lambda \ge 3/16$.

## Sources

- Selberg, as recorded in Luo--Rudnick--Sarnak (1995): every eigenvalue of a congruence subgroup in the model is either `0`-side excluded or at least `3/16`; stated here as the absence of eigenvalues in `(0, 3/16)`.

Stated but not proved: `MathlibExt.NumberTheory.SelbergSpectralGap.selberg_threeSixteenths_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergSpectralGapWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SelbergSpectralGapWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#selberg-three-sixteenths-wanted).

## Selberg's bound on the spectral-gap constant

Selberg's congruence spectral-gap constant
$C_{61}$ is at most $1/4$.

## Sources

- Selberg's theorem `λ₁(Γ) ≥ 3/16`, catalogue upper row `C₆₁ ≤ 1/4`.

Stated but not proved: `MathlibExt.NumberTheory.SelbergSpectralGap.selbergUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergSpectralGapWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SelbergSpectralGapWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#selberg-upper-bound-wanted).

## Kim–Sarnak eigenvalue bound

Let $\Gamma$ be a congruence subgroup of
$\mathrm{SL}(2, \mathbb{Z})$ and let $\lambda$ be a real eigenvalue of the hyperbolic Laplacian
$\Delta$ for $\Gamma$, that is, $\Delta f = \lambda f$ for some nonzero, twice continuously
differentiable, $\Gamma$-invariant function $f$ on the upper half plane that is square-integrable
on $\Gamma \backslash \mathbb{H}$. Then $\lambda$ does not lie in the open interval
$(0, 975/4096)$: either $\lambda \le 0$ or $\lambda \ge 975/4096$.

## Sources

- Kim--Sarnak (2003), as recorded in Kim--Ramakrishnan (2003): no eigenvalue of a congruence subgroup lies in `(0, 975/4096)`.

Stated but not proved: `MathlibExt.NumberTheory.SelbergSpectralGap.kimSarnak975_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergSpectralGapWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SelbergSpectralGapWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#kim-sarnak975-wanted).

## Kim–Sarnak bound on the spectral-gap constant

Selberg's congruence spectral-gap constant
$C_{61}$ is at most $7/64$.

## Sources

- Kim--Sarnak bound `λ₁(Γ) ≥ 975/4096 = 1/4 - (7/64)^2`, catalogue best upper row `C₆₁ ≤ 7/64`.

Stated but not proved: `MathlibExt.NumberTheory.SelbergSpectralGap.kimSarnakUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/NumberTheory/SelbergSpectralGapWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SelbergSpectralGapWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html#kim-sarnak-upper-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Selberg's eigenvalue conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/selberg-s-eigenvalue-conjecture)
