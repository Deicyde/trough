---
declaration: section
origin: cited
lean: PMF.expect, PMF.expect_eq_tsum, PMF.expect_eq_sum, PMF.expect_const, PMF.expect_uniformOfFintype, PMF.expect_add, PMF.expect_sum, PMF.expect_const_mul
statement: formalized
proof: formalized
---

# Expectation under a probability mass function

23 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html).

## Expectation under a probability mass function

Let $\alpha$ be a type carrying a σ-algebra
in which singletons are measurable, let $p$ be a probability mass function on $\alpha$ and let
$f : \alpha \to \mathbb{R}$. The expectation of $f$ under $p$ is the Bochner integral
$\int f \, d\mu_p$, where $\mu_p$ is the probability measure on $\alpha$ associated to $p$.

On a finite type it equals the finite sum $\sum_{a \in \alpha} p(a) f(a)$, with each mass $p(a)$
read as a real number. As a Bochner integral it is $0$ when $f$ is not integrable; nonnegative
or natural-valued observables should use the extended nonnegative expectation, whose value in
$[0, \infty]$ can be $\infty$.

Formalized by `PMF.expect`, a definition declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect).

## Expectation as a series

Let $p$ be a probability mass function on a measurable space
$\alpha$ in which singletons are measurable, and let $f : \alpha \to \mathbb{R}$ be integrable with
respect to the probability measure associated to $p$. Then the expectation of $f$ under $p$ equals
the unordered sum $\sum_{a \in \alpha} p(a) f(a)$.

Formalized by `PMF.expect_eq_tsum`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-eq-tsum).

## Expectation on a finite type

Let $p$ be a probability mass function on a finite measurable
space $\alpha$ in which singletons are measurable, and let $f : \alpha \to \mathbb{R}$. Then the
expectation of $f$ under $p$ equals the finite sum $\sum_{a \in \alpha} p(a) f(a)$.

Formalized by `PMF.expect_eq_sum`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-eq-sum).

## Expectation of a constant on a finite type

Let $\alpha$ be a finite set with a
$\sigma$-algebra in which singletons are measurable and let $p$ be a probability mass function on
$\alpha$. For every $c \in \mathbb{R}$, the expectation of the constant function $a \mapsto c$
under $p$ is $c$.

Formalized by `PMF.expect_const`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-const).

## Expectation under the uniform distribution

Let $\alpha$ be a nonempty finite type carrying
a σ-algebra in which singletons are measurable. For every function $f : \alpha \to \mathbb{R}$,
the expectation of $f$ under the uniform distribution on $\alpha$ equals the average
$\frac{1}{|\alpha|} \sum_{a \in \alpha} f(a)$.

Formalized by `PMF.expect_uniformOfFintype`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-uniform-of-fintype).

## Additivity of expectation on a finite type

Let $\alpha$ be a finite set with a
$\sigma$-algebra in which singletons are measurable, let $p$ be a probability mass function on
$\alpha$, and write $\mathbb{E}_p[h]$ for the expectation of $h : \alpha \to \mathbb{R}$ under $p$.
For all $f, g : \alpha \to \mathbb{R}$, $\mathbb{E}_p[f + g] = \mathbb{E}_p[f] + \mathbb{E}_p[g]$.

No integrability hypothesis is needed.

Formalized by `PMF.expect_add`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-add).

## Expectation of a finite sum

Let $p$ be a probability mass function on a finite type
$\alpha$ carrying a σ-algebra in which singletons are measurable, and write $\mathbb{E}_p[g]$ for
the expectation of $g : \alpha \to \mathbb{R}$ under $p$. For every finite subset $s$ of an index
type $\iota$ and every family of functions $f_i : \alpha \to \mathbb{R}$, $i \in \iota$, we have
$\mathbb{E}_p[a \mapsto \sum_{i \in s} f_i(a)] = \sum_{i \in s} \mathbb{E}_p[f_i]$.

Formalized by `PMF.expect_sum`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-sum).

## Homogeneity of expectation on a finite type

Let $\alpha$ be a finite set with a
$\sigma$-algebra in which singletons are measurable, let $p$ be a probability mass function on
$\alpha$, and write $\mathbb{E}_p[h]$ for the expectation of $h : \alpha \to \mathbb{R}$ under $p$.
For every $c \in \mathbb{R}$ and $f : \alpha \to \mathbb{R}$, the function $a \mapsto c\,f(a)$ has
expectation $c\,\mathbb{E}_p[f]$.

Formalized by `PMF.expect_const_mul`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-const-mul).

## Expectation of a scalar multiple

Let $p$ be a probability mass function on a finite
measurable space $\alpha$ in which singletons are measurable, let $c \in \mathbb{R}$ and let
$f : \alpha \to \mathbb{R}$. The expectation under $p$ of the scalar multiple $c f$ (the function
$a \mapsto c \cdot f(a)$) equals $c$ times the expectation of $f$ under $p$.

Formalized by `PMF.expect_smul`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-smul).

## Nonnegativity of expectation

Let $p$ be a probability mass function on a finite measurable
space $\alpha$ in which singletons are measurable, and let $f : \alpha \to \mathbb{R}$ satisfy
$f(a) \ge 0$ for every $a \in \alpha$. Then the expectation of $f$ under $p$ is nonnegative.

Formalized by `PMF.expect_nonneg`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-nonneg).

## Monotonicity of expectation

Let $p$ be a probability mass function on a finite measurable
space $\alpha$ in which singletons are measurable, and let $f, g : \alpha \to \mathbb{R}$ satisfy
$f(a) \le g(a)$ for every $a \in \alpha$. Then the expectation of $f$ under $p$ is at most the
expectation of $g$ under $p$.

Formalized by `PMF.expect_le_expect`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-le-expect).

## Expectation of a finitely supported distribution

Let $p$ be a probability mass function
on a measurable space $\alpha$ in which singletons are measurable, and let $s$ be a finite subset
of $\alpha$ such that $p(a) = 0$ for every $a \notin s$. Then for every function
$f : \alpha \to \mathbb{R}$, the expectation of $f$ under $p$ equals $\sum_{a \in s} p(a) f(a)$.

No integrability hypothesis on $f$ and no finiteness assumption on $\alpha$ is needed.

Formalized by `PMF.expect_eq_sum_of_finite_support`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-eq-sum-of-finite-support).

## Change of variables for expectation

Let $p$ be a probability mass function on a finite
measurable space $\alpha$ in which singletons are measurable, let $\beta$ be a measurable space in
which singletons are measurable, and let $g : \alpha \to \beta$ and $f : \beta \to \mathbb{R}$.
Write $g_* p$ for the pushforward of $p$ along $g$, which gives each $b \in \beta$ the mass
$\sum_{a :\, g(a) = b} p(a)$. Then the expectation of $f$ under $g_* p$ equals the expectation of
$f \circ g$ under $p$.

Formalized by `PMF.expect_map`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-map).

## Expectation of an indicator

Let $p$ be a probability mass function on a finite measurable
space $\alpha$ in which singletons are measurable, and let $q$ be a property of elements of
$\alpha$. The expectation under $p$ of the function equal to $1$ where $q$ holds and $0$ elsewhere
is $\sum_{a \in \alpha,\ q(a)} p(a)$, the total mass of the elements satisfying $q$.

Formalized by `PMF.expect_indicator_decide`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-indicator-decide).

## Extended expectation

For a probability mass function $p$ on a type $\alpha$ and a function
$f : \alpha \to [0, \infty]$, the extended expectation of $f$ under $p$ is the unordered sum
$\sum_{a \in \alpha} p(a) f(a)$ in $[0, \infty]$, which always exists.

Unlike the real-valued expectation, it needs no measurability or integrability hypothesis and
takes the value $\infty$ when the expected value diverges, rather than collapsing to $0$.

Formalized by `PMF.expectENN`, a definition declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn).

## Extended expectation on a finite set

Let $p$ be a probability mass function on a finite
set $\alpha$. For every $f : \alpha \to [0, \infty]$, the extended expectation of $f$ under $p$
equals the finite sum $\sum_{a \in \alpha} p(a)\, f(a)$.

Formalized by `PMF.expectENN_eq_sum`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-eq-sum).

## Extended expectation of a constant

Let $p$ be a probability mass function on a set
$\alpha$. For every $c \in [0, \infty]$, the extended expectation of the constant function
$a \mapsto c$ under $p$ is $c$.

The set $\alpha$ need not be finite.

Formalized by `PMF.expectENN_const`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-const).

## Extended expectation under the uniform distribution

Let $\alpha$ be a nonempty finite type
and $f : \alpha \to [0, \infty]$. The extended expectation of $f$ under the uniform distribution on
$\alpha$ equals $|\alpha|^{-1} \sum_{a \in \alpha} f(a)$, computed in $[0, \infty]$.

Formalized by `PMF.expectENN_uniformOfFintype`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-uniform-of-fintype).

## Additivity of extended expectation

Let $p$ be a probability mass function on a set
$\alpha$, and write $\overline{\mathbb{E}}_p[h]$ for the extended expectation of
$h : \alpha \to [0, \infty]$ under $p$. For all $f, g : \alpha \to [0, \infty]$,
$\overline{\mathbb{E}}_p[f + g] = \overline{\mathbb{E}}_p[f] + \overline{\mathbb{E}}_p[g]$.

No finiteness or integrability hypothesis is needed: sums of terms in $[0, \infty]$ always
converge.

Formalized by `PMF.expectENN_add`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-add).

## Extended expectation of a finite sum

Let $p$ be a probability mass function on a set
$\alpha$, and write $\overline{\mathbb{E}}_p[h]$ for the extended expectation of
$h : \alpha \to [0, \infty]$ under $p$. For every index set $\iota$, finite subset
$s \subseteq \iota$ and family of functions $f_i : \alpha \to [0, \infty]$ ($i \in \iota$),
$\overline{\mathbb{E}}_p\bigl[a \mapsto \sum_{i \in s} f_i(a)\bigr] =
\sum_{i \in s} \overline{\mathbb{E}}_p[f_i]$.

The set $\alpha$ need not be finite.

Formalized by `PMF.expectENN_sum`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-sum).

## Extended expectation under a finitely supported distribution

Let $p$ be a probability
mass function on a set $\alpha$, and let $s \subseteq \alpha$ be a finite set with $p(a) = 0$ for
every $a \notin s$. For every $f : \alpha \to [0, \infty]$, the extended expectation of $f$
under $p$ equals $\sum_{a \in s} p(a)\, f(a)$.

The set $\alpha$ itself need not be finite.

Formalized by `PMF.expectENN_eq_sum_of_finite_support`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-eq-sum-of-finite-support).

## Change of variables for extended expectation

Let $p$ be a probability mass function on a
set $\alpha$, let $g : \alpha \to \beta$ be a map to a set $\beta$, and let $g_* p$ be the
pushforward of $p$ along $g$, the probability mass function $b \mapsto \sum_{a : g(a) = b} p(a)$.
For every $f : \beta \to [0, \infty]$, the extended expectation of $f$ under $g_* p$ equals the
extended expectation of $f \circ g$ under $p$.

No finiteness or measurability hypothesis is needed: both sides are sums of terms in
$[0, \infty]$, whose order of summation can be interchanged freely.

Formalized by `PMF.expectENN_map`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-map).

## Extended and real expectations agree on natural-valued functions

Let $\alpha$ be a finite
set with a $\sigma$-algebra in which singletons are measurable, let $p$ be a probability mass
function on $\alpha$, and let $g : \alpha \to \mathbb{N}$. Let $x \in [0, \infty]$ be the
extended expectation of $g$, viewed as a function to $[0, \infty]$, under $p$, and send $x$ to
$\mathbb{R}$ by the map that is the identity on $[0, \infty)$ and sends $\infty$ to $0$. The
result is the expectation of $g$, viewed as a real-valued function, under $p$.

Formalized by `PMF.expectENN_natCast_toReal`, a theorem declared in [MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ProbabilityMassFunction/Expectation.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html#expect-enn-nat-cast-to-real).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Expectation under a probability mass function](https://deicyde.github.io/atlas-lean/roadmap/Probability/distributions/expectation-under-a-probability-mass-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/distributions/expectation-under-a-probability-mass-function)
