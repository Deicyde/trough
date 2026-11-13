---
declaration: section
origin: cited
lean: MathlibExt.Probability.KLS.outerMinkowskiBoundary, MathlibExt.Probability.KLS.cheegerCoefficient, MathlibExt.Probability.KLS.inverseCheegerConstant, MathlibExt.Probability.KLS.IsHalfspace, MathlibExt.Probability.KLS.halfspaceCheegerCoefficient, MathlibExt.Probability.KLS.inverseHalfspaceCheegerConstant, MathlibExt.Probability.KLS.dimensionalKlsConstant, MathlibExt.Probability.KLS.klsConstant
statement: formalized
---

# Kannan–Lovász–Simonovits conjecture

35 results, 22 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html).

## Outer Minkowski boundary measure

Let $\mu$ be a measure on a pseudometric space $E$ and
let $A \subseteq E$. For $\varepsilon > 0$ let
$A_\varepsilon = \{x \in E : \inf_{a \in A} d(x, a) \le \varepsilon\}$ be the closed
$\varepsilon$-neighbourhood of $A$, with $\inf \emptyset = \infty$. The outer Minkowski boundary
measure of $A$ with respect to $\mu$ is

$$\mu^+(A) = \liminf_{\varepsilon \to 0^+} \frac{\mu(A_\varepsilon) - \mu(A)}{\varepsilon},$$

where the difference and the quotient are computed in $[0, \infty]$, with $\infty - \infty = 0$.

Formalized by `MathlibExt.Probability.KLS.outerMinkowskiBoundary`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#outer-minkowski-boundary).

## Cheeger coefficient

For a measure $\mu$ on a pseudometric space $E$ equipped with a
σ-algebra, the Cheeger coefficient of $\mu$ is the infimum in $[0, \infty]$ of
$\mu^+(A) / \min(\mu(A), 1 - \mu(A))$ over all measurable sets $A \subseteq E$ with
$0 < \mu(A) < 1$, where
$\mu^+(A) = \liminf_{\varepsilon \to 0^+} (\mu(A_\varepsilon) - \mu(A)) / \varepsilon$ is the
outer Minkowski boundary measure of $A$ and $A_\varepsilon$ is the closed
$\varepsilon$-neighbourhood of $A$. The infimum of the empty family is $\infty$; the measure
$\mu$ is not required to be a probability measure.

Formalized by `MathlibExt.Probability.KLS.cheegerCoefficient`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#cheeger-coefficient).

## Inverse Cheeger constant

For a measure $\mu$ on a pseudometric space $E$ equipped with a
σ-algebra, the inverse Cheeger constant of $\mu$ is $1 / h(\mu) \in [0, \infty]$, where $h(\mu)$
is the Cheeger coefficient of $\mu$, with the conventions $1 / 0 = \infty$ and
$1 / \infty = 0$.

Formalized by `MathlibExt.Probability.KLS.inverseCheegerConstant`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#inverse-cheeger-constant).

## Half-spaces

A set $A \subseteq \mathbb{R}^n$ is a half-space if there are a nonzero
vector $v \in \mathbb{R}^n$ and a real number $a$ such that
$A = \{x \in \mathbb{R}^n : \langle v, x \rangle \le a\}$.

Formalized by `MathlibExt.Probability.KLS.IsHalfspace`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#is-halfspace).

## Half-space Cheeger coefficient

For a measure $\mu$ on $\mathbb{R}^n$ with the Euclidean
metric, the half-space Cheeger coefficient of $\mu$ is the infimum in $[0, \infty]$ of
$\mu^+(H) / \min(\mu(H), 1 - \mu(H))$ over all closed half-spaces
$H = \{x : \langle v, x \rangle \le a\}$ with $v \ne 0$ and $a \in \mathbb{R}$ such that
$0 < \mu(H) < 1$, where $\mu^+(H)$ is the outer Minkowski boundary measure of $H$. The infimum
of the empty family is $\infty$.

Formalized by `MathlibExt.Probability.KLS.halfspaceCheegerCoefficient`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#halfspace-cheeger-coefficient).

## Inverse half-space Cheeger constant

For a measure $\mu$ on $\mathbb{R}^n$, the inverse
half-space Cheeger constant of $\mu$ is $h^{-1}$, where $h \in [0, \infty]$ is the half-space
Cheeger coefficient of $\mu$ and the inverse is taken in $[0, \infty]$, so that
$0^{-1} = \infty$ and $\infty^{-1} = 0$.

Formalized by `MathlibExt.Probability.KLS.inverseHalfspaceCheegerConstant`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#inverse-halfspace-cheeger-constant).

## Dimensional KLS constant

For $n \in \mathbb{N}$, the dimensional KLS constant in
dimension $n$ is the supremum in $[0, \infty]$ of the inverse Cheeger constants of all isotropic
log-concave probability measures on $\mathbb{R}^n$ with the Euclidean metric.

Formalized by `MathlibExt.Probability.KLS.dimensionalKlsConstant`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#dimensional-kls-constant).

## KLS constant

The KLS constant is the supremum in $[0, \infty]$ of the dimensional KLS
constants in dimension $n$, taken over all positive integers $n$.

Formalized by `MathlibExt.Probability.KLS.klsConstant`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#kls-constant).

## Smooth Poincaré bounds

Let $\mu$ be a measure on $\mathbb{R}^n$ and let
$C \in [0, \infty]$. For a differentiable $g : \mathbb{R}^n \to \mathbb{R}$ write
$\|\nabla g(x)\|$ for the Euclidean norm of the gradient of $g$ at $x$ (equivalently, the
operator norm of the derivative of $g$ at $x$). Then $C$ is a smooth Poincaré bound for $\mu$
if for every infinitely differentiable function $f : \mathbb{R}^n \to \mathbb{R}$ such that
$f$, $f^2$ and $\|\nabla f\|^2$ are $\mu$-integrable,

$$\int \Big(f(x) - \int f \, d\mu\Big)^2 \, d\mu(x) \le C \int \|\nabla f(x)\|^2 \, d\mu(x),$$

where the outer integral on the left and the integral on the right are computed in
$[0, \infty]$ with $0 \cdot \infty = 0$, and the inner integral $\int f \, d\mu$ is the usual
real integral. The measure $\mu$ need not be a probability measure.

Formalized by `MathlibExt.Probability.KLS.IsSmoothPoincareBound`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#is-smooth-poincare-bound).

## Smooth Poincaré constant

The smooth Poincaré constant of a measure $\mu$ on $\mathbb{R}^n$
is the infimum in $[0, \infty]$ of all $C \in [0, \infty]$ that are smooth Poincaré bounds for
$\mu$; it is $\infty$ when $\mu$ has no smooth Poincaré bound.

Formalized by `MathlibExt.Probability.KLS.smoothPoincareConstant`, a definition declared in [MathlibExt/Probability/Geometry/KLS.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#smooth-poincare-constant).

## The empty set has zero outer Minkowski boundary

For every measure $\mu$ on a
pseudometric space $E$, the outer Minkowski boundary measure of the empty set with respect to
$\mu$ is $0$.

Formalized by `MathlibExt.Probability.KLS.outerMinkowskiBoundary_empty`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#outer-minkowski-boundary-empty).

## Cheeger coefficient of the zero measure

On every pseudometric space $E$ equipped with a
σ-algebra, the zero measure has Cheeger coefficient $\infty$.

No set has measure strictly between $0$ and $1$ under the zero measure, so the infimum is taken
over the empty family.

Formalized by `MathlibExt.Probability.KLS.cheegerCoefficient_zero`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#cheeger-coefficient-zero).

## Inverse Cheeger constant of the zero measure

On every pseudometric space $E$ equipped
with a σ-algebra, the zero measure has inverse Cheeger constant $0$.

Formalized by `MathlibExt.Probability.KLS.inverseCheegerConstant_zero`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#inverse-cheeger-constant-zero).

## The Cheeger coefficient is at most the half-space Cheeger coefficient

For every measure
$\mu$ on $\mathbb{R}^n$ with the Euclidean metric, the Cheeger coefficient of $\mu$ is at most
its half-space Cheeger coefficient.

Formalized by `MathlibExt.Probability.KLS.cheegerCoefficient_le_halfspace`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#cheeger-coefficient-le-halfspace).

## Inverse Cheeger constant bounded by the dimensional KLS constant

For every
$n \in \mathbb{N}$ and every isotropic log-concave probability measure $\mu$ on $\mathbb{R}^n$
with the Euclidean metric, the inverse Cheeger constant of $\mu$ is at most the dimensional KLS
constant in dimension $n$.

Formalized by `MathlibExt.Probability.KLS.inverseCheegerConstant_le_dimensional`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#inverse-cheeger-constant-le-dimensional).

## Dimensional KLS constants are bounded by the KLS constant

For every positive integer
$n$, the dimensional KLS constant in dimension $n$ is at most the KLS constant.

Formalized by `MathlibExt.Probability.KLS.dimensionalKlsConstant_le_constant`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#dimensional-kls-constant-le-constant).

## Inverse Cheeger constant bounded by the KLS constant

For every positive integer $n$ and
every isotropic log-concave probability measure $\mu$ on $\mathbb{R}^n$ with the Euclidean
metric, the inverse Cheeger constant of $\mu$ is at most the KLS constant.

Formalized by `MathlibExt.Probability.KLS.inverseCheegerConstant_le_constant`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#inverse-cheeger-constant-le-constant).

## Bounding the KLS constant dimension by dimension

For every $C \in [0, \infty]$, the KLS
constant is at most $C$ if and only if, for every positive integer $n$, the dimensional KLS
constant in dimension $n$ is at most $C$.

Formalized by `MathlibExt.Probability.KLS.klsConstant_le_iff`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#kls-constant-le-iff).

## Bounding the KLS constant measure by measure

For every $C \in [0, \infty]$, the KLS
constant is at most $C$ if and only if, for every positive integer $n$ and every isotropic
log-concave probability measure $\mu$ on $\mathbb{R}^n$, the inverse Cheeger constant of $\mu$ is
at most $C$.

Formalized by `MathlibExt.Probability.KLS.klsConstant_le_iff_measures`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#kls-constant-le-iff-measures).

## Finiteness of the KLS constant

The KLS constant is finite if and only if there is a real
number $C$ such that, for every positive integer $n$ and every isotropic log-concave probability
measure $\mu$ on $\mathbb{R}^n$, the inverse Cheeger constant of $\mu$ is at most $\max(C, 0)$.

The right-hand side is the Kannan–Lovász–Simonovits (KLS) conjecture.

Formalized by `MathlibExt.Probability.KLS.klsConstant_lt_top_iff`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#kls-constant-lt-top-iff).

## Smooth Poincaré bounds are upward closed

Let $\mu$ be a measure on $\mathbb{R}^n$ and let
$C \le D$ in $[0, \infty]$. If $C$ is a smooth Poincaré bound for $\mu$, then so is $D$.

Formalized by `MathlibExt.Probability.KLS.IsSmoothPoincareBound.mono`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#mono).

## The smooth Poincaré constant is at most every smooth Poincaré bound

Let $\mu$ be a
measure on $\mathbb{R}^n$ and let $C \in [0, \infty]$. If $C$ is a smooth Poincaré bound for
$\mu$, then the smooth Poincaré constant of $\mu$ is at most $C$.

Formalized by `MathlibExt.Probability.KLS.smoothPoincareConstant_le_of_bound`, a theorem declared in [MathlibExt/Probability/Geometry/KLS.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Geometry/KLS.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#smooth-poincare-constant-le-of-bound).

## Kannan–Lovász–Simonovits bound on the KLS constant

There are a real $C > 0$ and an
integer $N \ge 3$ such that for every $n \ge N$ the dimensional KLS constant
$\psi_n \in [0, \infty]$ satisfies $\psi_n \le C \sqrt{n}$.

## Sources

- Kannan, Lovasz and Simonovits, DCG 13 (1995), 541--560; optimizationproblems `constants/20c.md`, KLS1995 row.

Stated but not proved: `MathlibExt.Probability.KLS.kannanLovaszSimonovits1995_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#kannan-lovasz-simonovits1995-bound).

## Lee–Vempala bound on the KLS constant

There are a real $C > 0$ and an integer $N \ge 3$
such that for every $n \ge N$ the dimensional KLS constant $\psi_n \in [0, \infty]$ satisfies
$\psi_n \le C n^{1/4}$.

## Sources

- Lee and Vempala, Ann. of Math. 199 (2024), 1--104; optimizationproblems `constants/20c.md`, LV2024 row.

Stated but not proved: `MathlibExt.Probability.KLS.leeVempala2024_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#lee-vempala2024-bound).

## Chen's subpolynomial bound on the KLS constant, weaker form

There are a real $C > 0$ and
an integer $N \ge 3$ such that for every $n \ge N$ the dimensional KLS constant
$\psi_n \in [0, \infty]$ satisfies $\psi_n \le \exp\bigl(C \sqrt{\log n} \, \log \log n\bigr)$.

## Sources

- Chen, GAFA 31 (2021), 34--61; optimizationproblems `constants/20c.md`. Jambulapati--Lee--Vempala v1 quotes the stronger exponent `sqrt(log n * log(log n))`.

Stated but not proved: `MathlibExt.Probability.KLS.chen2021_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#chen2021-bound).

## Klartag–Lehec polylogarithmic bound on the KLS constant

There are a real $C > 0$ and an
integer $N \ge 3$ such that for every $n \ge N$ the dimensional KLS constant
$\psi_n \in [0, \infty]$ satisfies $\psi_n \le C (\log n)^5$.

## Sources

- Klartag and Lehec, GAFA 32 (2022), 1134--1159; optimizationproblems `constants/20c.md`, KL2022 row.

Stated but not proved: `MathlibExt.Probability.KLS.klartagLehec2022_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#klartag-lehec2022-bound).

## Jambulapati–Lee–Vempala polylogarithmic bound on the KLS constant

Let
$\alpha = 1 + \bigl(1 + 7\sqrt{2} + \sqrt{53 - 4\sqrt{2}}\bigr)/8$. There are a real $C > 0$ and an
integer $N \ge 3$ such that for every $n \ge N$ the dimensional KLS constant
$\psi_n \in [0, \infty]$ satisfies $\psi_n \le C (\log n)^{\alpha}$.

The exponent is kept in exact algebraic form rather than as a rounded decimal.

## Sources

- arXiv:2208.11644v1, Theorem 22 and the preceding KLS/thin-shell comparison.

Stated but not proved: `MathlibExt.Probability.KLS.jambulapatiLeeVempala2022_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#jambulapati-lee-vempala2022-bound).

## Lehec's reported polylogarithmic bound on the KLS constant, weakened

There are a real
$C > 0$ and an integer $N \ge 3$ such that for every $n \ge N$ the dimensional KLS constant
$\psi_n \in [0, \infty]$ satisfies $\psi_n \le C (\log n)^{3.083}$.

The exponent $3.083$ lies just above Lehec's reported exponent $3.082\ldots$, which the primary
gives only to this decimal precision; $3.083$ is not claimed to be the exact exponent.

## Sources

- Klartag, arXiv:2303.14938v1, Introduction, personal-communication paragraph.

Stated but not proved: `MathlibExt.Probability.KLS.lehec_reported_bound_weaker_specialization` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#lehec-reported-bound-weaker-specializati).

## Klartag's square-root-logarithmic bound on the KLS constant

There is a real $C > 0$ such
that for every integer $n \ge 2$ the dimensional KLS constant $\psi_n \in [0, \infty]$ satisfies
$\psi_n \le C \sqrt{\log n}$.

## Sources

- Klartag, arXiv:2303.14938v1, Theorem 1.2.

Stated but not proved: `MathlibExt.Probability.KLS.klartag2023_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#klartag2023-bound).

## Inverse Cheeger constant of the standard Gaussian

For every $n \ge 1$, the standard
Gaussian measure on $\mathbb{R}^n$ has inverse Cheeger constant exactly $\sqrt{\pi/2}$.

## Sources

- optimizationproblems `constants/20c.md`, classical Gaussian row; the Gaussian isoperimetric theorem supplies the minimizing half-space claim.

Stated but not proved: `MathlibExt.Probability.KLS.stdGaussian_inverseCheeger` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#std-gaussian-inverse-cheeger).

## A lower bound for the KLS constant

The KLS constant is at least $\sqrt{\pi/2}$.

The bound comes from the standard Gaussian measure in any dimension $n \ge 1$, whose inverse Cheeger
constant is $\sqrt{\pi/2}$.

## Sources

- optimizationproblems `constants/20c.md`, classical Gaussian lower-bound row.

Stated but not proved: `MathlibExt.Probability.KLS.sqrtPiDivTwo_le_klsConstant` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#sqrt-pi-div-two-le-kls-constant).

## Lower Poincaré–Cheeger comparison with coefficient 1/π

Let $n \ge 1$ and let $\mu$ be an
isotropic log-concave probability measure on $\mathbb{R}^n$, with inverse Cheeger constant
$\psi(\mu) \in [0, \infty]$ and smooth Poincaré constant $C_P(\mu) \in [0, \infty]$. Then
$\frac{1}{\pi} \psi(\mu)^2 \le C_P(\mu)$.

## Sources

- optimizationproblems `constants/20c.md`, Poincare comparison display. Klartag arXiv:2303.14938v1 states the weaker lower coefficient `1/9`, not `1/pi`.

Stated but not proved: `MathlibExt.Probability.KLS.catalogue_poincare_lower_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#catalogue-poincare-lower-bound).

## Lower Poincaré–Cheeger comparison with coefficient 1/9

Let $n \ge 1$ and let $\mu$ be an
isotropic log-concave probability measure on $\mathbb{R}^n$, with inverse Cheeger constant
$\psi(\mu) \in [0, \infty]$ and smooth Poincaré constant $C_P(\mu) \in [0, \infty]$. Then
$\frac{1}{9} \psi(\mu)^2 \le C_P(\mu)$.

## Sources

- Klartag, arXiv:2303.14938v1, equation comparing `psi` and `C_P`. The locally Lipschitz-to-smooth approximation remains part of the requested proof.

Stated but not proved: `MathlibExt.Probability.KLS.klartag2023_poincare_lower_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#klartag2023-poincare-lower-bound).

## Cheeger's inequality for isotropic log-concave measures

Let $n \ge 1$, let $\mu$ be an
isotropic log-concave probability measure on $\mathbb{R}^n$, and let $\psi_\mu \in [0, \infty]$ be
the inverse Cheeger constant of $\mu$. Then the smooth Poincaré constant of $\mu$ is at most
$4 \psi_\mu^2$.

## Sources

- optimizationproblems `constants/20c.md`, comparison display, and Klartag, arXiv:2303.14938v1, Introduction.

Stated but not proved: `MathlibExt.Probability.KLS.poincare_cheeger_upper_bound` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#poincare-cheeger-upper-bound).

## Dimensional KLS constant versus thin-shell variance, up to a squared logarithm

Let
$\Sigma \in [0, \infty]$ be the thin-shell variance constant: the supremum, over all dimensions
$m \ge 1$ and all isotropic log-concave probability measures $\mu$ on $\mathbb{R}^m$, of
$\frac{1}{m} \int (\lVert x \rVert^2 - m)^2 \, d\mu(x)$. There is a real $C > 0$ such that for
every integer $n \ge 3$ the dimensional KLS constant $\psi_n \in [0, \infty]$ satisfies
$\psi_n^2 \le C (\log n)^2 \, \Sigma$.

## Sources

- Jambulapati--Lee--Vempala, arXiv:2208.11644v1, KLS/thin-shell comparison.

Stated but not proved: `MathlibExt.Probability.KLS.kls_le_thinShell_variance_log_squared` is written with `theorem_wanted` in [WantedExt/Probability/KLSBoundsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/KLSBoundsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html#kls-le-thin-shell-variance-log-squared).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kannan–Lovász–Simonovits conjecture](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/high-dimensional-probability/kannan-lov-sz-simonovits-conjecture)
