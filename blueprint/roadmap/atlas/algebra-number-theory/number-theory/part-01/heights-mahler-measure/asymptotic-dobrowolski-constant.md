---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.AsymptoticDobrowolski.dobrowolskiScale, MathlibExt.NumberTheory.AsymptoticDobrowolski.dobrowolskiScale_pos, MathlibExt.NumberTheory.AsymptoticDobrowolski.IsAsymptoticDobrowolskiCoefficient, MathlibExt.NumberTheory.AsymptoticDobrowolski.asymptoticDobrowolskiConstant, MathlibExt.NumberTheory.AsymptoticDobrowolski.coe_le_asymptoticDobrowolskiConstant, MathlibExt.NumberTheory.AsymptoticDobrowolski.zero_isAsymptoticDobrowolskiCoefficient, MathlibExt.NumberTheory.AsymptoticDobrowolski.asymptoticDobrowolskiConstant_le_iff, MathlibExt.NumberTheory.AsymptoticDobrowolski.isAsymptoticDobrowolskiCoefficient_iff
statement: formalized
---

# Asymptotic Dobrowolski constant

16 results, 11 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html).

## Dobrowolski scale

For a natural number $d$, the Dobrowolski scale is

$$\left(\frac{\log \log d}{\log d}\right)^3,$$

with natural logarithms and the conventions $\log 0 = 0$ and $x / 0 = 0$, so that it is $0$ for
$d \le 1$.

It is used only for degrees $d \ge 3$ in the definition of asymptotic Dobrowolski coefficients.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.dobrowolskiScale`, a definition declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#dobrowolski-scale).

## Positivity of the Dobrowolski scale

For every natural number $d \ge 3$, the Dobrowolski
scale $\left(\frac{\log \log d}{\log d}\right)^3$ is strictly positive.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.dobrowolskiScale_pos`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#dobrowolski-scale-pos).

## Asymptotic Dobrowolski coefficients

A real number $c$ is an asymptotic Dobrowolski
coefficient if for every $\varepsilon > 0$ there is a natural number $D \ge 3$ such that every
nonzero algebraic number $\alpha \in \mathbb{C}$ that is not a root of unity and whose minimal
polynomial over $\mathbb{Q}$ has degree $d \ge D$ satisfies

$$1 + (c - \varepsilon) \left(\frac{\log \log d}{\log d}\right)^3 \le M(\alpha),$$

where $M(\alpha)$ is the Mahler measure of $\alpha$.

The degree threshold $D$ may depend on $\varepsilon$ but is uniform over all such $\alpha$.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.IsAsymptoticDobrowolskiCoefficient`, a definition declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#is-asymptotic-dobrowolski-coefficient).

## Asymptotic Dobrowolski constant

The asymptotic Dobrowolski constant is the supremum, in
the extended real numbers $[-\infty, +\infty]$, of the set of all real asymptotic Dobrowolski
coefficients.

The supremum would be $-\infty$ if there were no coefficient and is $+\infty$ if the coefficients
are unbounded above; neither attainment nor a finite upper bound is assumed.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.asymptoticDobrowolskiConstant`, a definition declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#asymptotic-dobrowolski-constant).

## Coefficients are bounded by the asymptotic Dobrowolski constant

Every real asymptotic
Dobrowolski coefficient $c$ satisfies $c \le$ the asymptotic Dobrowolski constant, as extended
real numbers.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.coe_le_asymptoticDobrowolskiConstant`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#coe-le-asymptotic-dobrowolski-constant).

## Zero is an asymptotic Dobrowolski coefficient

The real number $0$ is an asymptotic
Dobrowolski coefficient: for every real $\varepsilon > 0$ there is a natural number $D \ge 3$
such that every nonzero algebraic number $\alpha \in \mathbb{C}$ that is not a root of unity and
whose minimal polynomial over $\mathbb{Q}$ has degree $d \ge D$ satisfies
$1 - \varepsilon \left(\frac{\log \log d}{\log d}\right)^3 \le M(\alpha)$, where $M(\alpha)$ is the
Mahler measure of the primitive integer minimal polynomial of $\alpha$ with positive leading
coefficient.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.zero_isAsymptoticDobrowolskiCoefficient`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#zero-is-asymptotic-dobrowolski-coefficie).

## Upper bounds for the asymptotic Dobrowolski constant

For every extended real number $b$,
the asymptotic Dobrowolski constant is at most $b$ if and only if every real asymptotic
Dobrowolski coefficient $c$ satisfies $c \le b$.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.asymptoticDobrowolskiConstant_le_iff`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#asymptotic-dobrowolski-constant-le-iff).

## Coefficients are exactly the reals below the constant

A real number $c$ is an asymptotic
Dobrowolski coefficient if and only if $c$ is at most the asymptotic Dobrowolski constant, as
extended real numbers.

The $\varepsilon$ in the definition makes the set of coefficients closed, so a finite constant is
itself a coefficient; this also covers the case where the coefficients are unbounded above.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.isAsymptoticDobrowolskiCoefficient_iff`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#is-asymptotic-dobrowolski-coefficient-if).

## Strict form of asymptotic Dobrowolski coefficients

A real number $c$ is an asymptotic
Dobrowolski coefficient if and only if for every $\varepsilon > 0$ there is a natural number
$D \ge 3$ such that every nonzero algebraic number $\alpha \in \mathbb{C}$ that is not a root of
unity and whose minimal polynomial over $\mathbb{Q}$ has degree $d \ge D$ satisfies

$$1 + (c - \varepsilon) \left(\frac{\log \log d}{\log d}\right)^3 < M(\alpha),$$

where $M(\alpha)$ is the Mahler measure of $\alpha$.

So the strict bounds are equivalent to the non-strict bounds in the definition.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.isAsymptoticDobrowolskiCoefficient_iff_strict`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#is-asymptotic-dobrowolski-coefficient-if-2).

## The asymptotic Dobrowolski constant is nonnegative

The asymptotic Dobrowolski constant
is at least $0$.

The bound comes from the coefficient $0$, which is an asymptotic Dobrowolski coefficient because
every Mahler measure is at least $1$.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.asymptoticDobrowolskiConstant_nonneg`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#asymptotic-dobrowolski-constant-nonneg).

## Trivial upper bound for the asymptotic Dobrowolski constant

The asymptotic Dobrowolski
constant is at most $+\infty$.

This is only the trivial bound in the extended reals, not a finite estimate.

Formalized by `MathlibExt.NumberTheory.AsymptoticDobrowolski.asymptoticDobrowolskiConstant_le_top`, a theorem declared in [MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Height/AsymptoticDobrowolski.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#asymptotic-dobrowolski-constant-le-top).

## Dobrowolski's lower bound for the asymptotic Dobrowolski constant

The asymptotic
Dobrowolski constant is at least $1$, as an extended real number.

## Sources

- Dobrowolski (1979), as reported by Voutier, coefficient `1`.

Stated but not proved: `MathlibExt.NumberTheory.AsymptoticDobrowolski.dobrowolski_one_le_asymptoticConstant` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#dobrowolski-one-le-asymptotic-constant).

## Cantor–Straus lower bound for the asymptotic Dobrowolski constant

The asymptotic
Dobrowolski constant is at least $2$, as an extended real number.

## Sources

- Cantor--Straus (1982), as reported by Voutier, coefficient `2`.

Stated but not proved: `MathlibExt.NumberTheory.AsymptoticDobrowolski.cantorStraus_two_le_asymptoticConstant` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#cantor-straus-two-le-asymptotic-constant).

## Louboutin's lower bound for the asymptotic Dobrowolski constant

The asymptotic
Dobrowolski constant is at least $9/4$, as an extended real number.

## Sources

- Louboutin (1983), as reported by Voutier, coefficient `9/4`.

Stated but not proved: `MathlibExt.NumberTheory.AsymptoticDobrowolski.louboutin_nine_fourths_le_asymptoticConstant` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#louboutin-nine-fourths-le-asymptotic-con).

## Blanksby–Montgomery lower bound for the Mahler measure

Let $\alpha$ be a nonzero complex
number that is algebraic over $\mathbb{Q}$ and is not a root of unity, and let $d$ be the degree
of its minimal polynomial over $\mathbb{Q}$. If $d \ge 2$, then the algebraic Mahler measure
$M(\alpha)$ satisfies $M(\alpha) > 1 + \frac{1}{52\, d \log(6d)}$, with $\log$ the natural
logarithm.

## Sources

- Blanksby--Montgomery, the strict degree-dependent bound quoted by Voutier.

Stated but not proved: `MathlibExt.NumberTheory.AsymptoticDobrowolski.blanksbyMontgomery_degreeBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#blanksby-montgomery-degree-bound).

## Stewart's lower bound for the Mahler measure

Let $\alpha$ be a nonzero complex number
that is algebraic over $\mathbb{Q}$ and is not a root of unity, and let $d$ be the degree of its
minimal polynomial over $\mathbb{Q}$. If $d \ge 2$, then the algebraic Mahler measure $M(\alpha)$
satisfies $M(\alpha) > 1 + \frac{1}{10000\, d \log d}$, with $\log$ the natural logarithm.

## Sources

- Stewart (1978), the strict degree-dependent bound quoted by Voutier.

Stated but not proved: `MathlibExt.NumberTheory.AsymptoticDobrowolski.stewart_degreeBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Height/AsymptoticDobrowolskiWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html#stewart-degree-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic Dobrowolski constant](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/heights-mahler-measure/asymptotic-dobrowolski-constant)
