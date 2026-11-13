---
declaration: section
origin: cited
lean: NumberField.Modulus.infinite_finitePart, NumberField.Modulus.infinite_infinitePart, NumberField.Modulus.finiteSupported, NumberField.Modulus.finiteExponent, NumberField.Modulus.coprimeFractionalIdeals, NumberField.Modulus.rayElements, NumberField.Modulus.CongruentOneAtFinitePart, NumberField.Modulus.PositiveAtInfinitePart
statement: formalized
proof: formalized
---

# Ray class groups

97 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html).

## Finite part of the modulus of a real place

For a real place $v$ of a number field $K$,
let $\mathfrak m_v$ be the modulus of $K$ with finite part the unit ideal $\mathcal O_K$ and
infinite part $\{v\}$. The finite part of $\mathfrak m_v$ is the unit ideal $\mathcal O_K$.

Formalized by `NumberField.Modulus.infinite_finitePart`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/Modulus.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Modulus.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#infinite-finite-part).

## Infinite part of the modulus of a real place

For a real place $v$ of a number field $K$,
let $\mathfrak m_v$ be the modulus of $K$ with finite part the unit ideal $\mathcal O_K$ and
infinite part $\{v\}$. The infinite part of $\mathfrak m_v$ is the singleton $\{v\}$.

Formalized by `NumberField.Modulus.infinite_infinitePart`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/Modulus.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Modulus.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#infinite-infinite-part).

## Primes dividing a modulus

Let $\mathfrak m$ be a modulus of a number field $K$, with finite
part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$. A nonzero prime ideal $\mathfrak p$ of
$\mathcal O_K$ lies in the finite support of $\mathfrak m$ when
$\mathfrak m_0 \subseteq \mathfrak p$, that is, when $\mathfrak p$ divides $\mathfrak m_0$.

Formalized by `NumberField.Modulus.finiteSupported`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-supported).

## Exponent of a modulus at a prime

Let $\mathfrak m$ be a modulus of a number field $K$, with
finite part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$. For a nonzero prime ideal
$\mathfrak p$ of $\mathcal O_K$, the finite exponent of $\mathfrak m$ at $\mathfrak p$ is the
integer $v_{\mathfrak p}(\mathfrak m_0)$, the exponent of $\mathfrak p$ in the prime factorization
of $\mathfrak m_0$.

Formalized by `NumberField.Modulus.finiteExponent`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-exponent).

## Fractional ideals coprime to a modulus

Let $\mathfrak m$ be a modulus of a number field
$K$, with finite part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$. For an invertible
fractional ideal $I$ of $\mathcal O_K$ and a nonzero prime ideal $\mathfrak p$, write
$v_{\mathfrak p}(I)$ for the exponent of $\mathfrak p$ in the factorization of $I$. The fractional
ideals coprime to $\mathfrak m$ form the subgroup of the group of invertible fractional ideals of
$\mathcal O_K$ consisting of those $I$ with $v_{\mathfrak p}(I) = 0$ for every nonzero prime ideal
$\mathfrak p$ of $\mathcal O_K$ containing $\mathfrak m_0$.

Formalized by `NumberField.Modulus.coprimeFractionalIdeals`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#coprime-fractional-ideals).

## Elements coprime to a modulus

Let $\mathfrak m$ be a modulus of a number field $K$, with
finite part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$. The elements coprime to
$\mathfrak m$ form the subgroup of $K^\times$ consisting of those $x$ whose principal fractional
ideal $(x)$ is coprime to $\mathfrak m$, that is, has exponent $0$ at every nonzero prime ideal
$\mathfrak p$ of $\mathcal O_K$ containing $\mathfrak m_0$.

Formalized by `NumberField.Modulus.rayElements`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-elements).

## Multiplicative congruence to one at the finite part

Let $\mathfrak m$ be a modulus of a
number field $K$, with finite part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$. For a
nonzero prime ideal $\mathfrak p$ of $\mathcal O_K$, write $v_{\mathfrak p}(I)$ for the exponent of
$\mathfrak p$ in the factorization of a nonzero fractional ideal $I$ of $\mathcal O_K$, and for
$y \in K$ write $v_{\mathfrak p}(y) = v_{\mathfrak p}((y))$ (with $v_{\mathfrak p}(0) = 0$). An
element $x \in K^\times$ is congruent to $1$ at the finite part of $\mathfrak m$ when, for every
nonzero prime ideal $\mathfrak p$ of $\mathcal O_K$ containing $\mathfrak m_0$, either $x = 1$ or
$v_{\mathfrak p}(\mathfrak m_0) \le v_{\mathfrak p}(x - 1)$.

Formalized by `NumberField.Modulus.CongruentOneAtFinitePart`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#congruent-one-at-finite-part).

## Positivity at the infinite part of a modulus

Let $\mathfrak m$ be a modulus of a number
field $K$, with infinite part the finite set $\mathfrak m_\infty$ of real places of $K$. An element
$x \in K^\times$ is positive at the infinite part of $\mathfrak m$ when $\sigma_w(x) > 0$ for every
real place $w \in \mathfrak m_\infty$, where $\sigma_w \colon K \to \mathbb R$ is the real
embedding corresponding to $w$.

Formalized by `NumberField.Modulus.PositiveAtInfinitePart`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#positive-at-infinite-part).

## Elements congruent to one modulo a modulus

Let $\mathfrak m$ be a modulus of a number field
$K$, with finite part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$ and infinite part the
finite set $\mathfrak m_\infty$ of real places of $K$. For a nonzero prime ideal $\mathfrak p$ of
$\mathcal O_K$, write $v_{\mathfrak p}(I)$ for the exponent of $\mathfrak p$ in the factorization
of a nonzero fractional ideal $I$ of $\mathcal O_K$, and for $y \in K$ write
$v_{\mathfrak p}(y) = v_{\mathfrak p}((y))$ (with $v_{\mathfrak p}(0) = 0$); for a real place $w$
write $\sigma_w \colon K \to \mathbb R$ for the corresponding real embedding. An element
$x \in K^\times$ is congruent to $1$ modulo $\mathfrak m$ when, for every nonzero prime ideal
$\mathfrak p$ of $\mathcal O_K$ containing $\mathfrak m_0$, $v_{\mathfrak p}(x) = 0$ and either
$x = 1$ or $v_{\mathfrak p}(\mathfrak m_0) \le v_{\mathfrak p}(x - 1)$, and $\sigma_w(x) > 0$ for
every real place $w \in \mathfrak m_\infty$.

Formalized by `NumberField.Modulus.IsRayElementOne`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#is-ray-element-one).

## Generators of the ray group

Let $\mathfrak m$ be a modulus of a number field $K$. The ray
generators of $\mathfrak m$ are the fractional ideals coprime to $\mathfrak m$ of the form $(x)$,
the principal fractional ideal of an element $x \in K^\times$ that is congruent to $1$ modulo
$\mathfrak m$.

Formalized by `NumberField.Modulus.rayGenerators`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-generators).

## The ray group of a modulus

Let $\mathfrak m$ be a modulus of a number field $K$. The ray
group of $\mathfrak m$ is the subgroup of the group of fractional ideals coprime to $\mathfrak m$
generated by the principal ideals $(x)$ of the elements $x \in K^\times$ congruent to $1$ modulo
$\mathfrak m$.

Formalized by `NumberField.Modulus.rayGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayGroup.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-group).

## Lower bound for the exponent of a sum

Let $K$ be a number field and $\mathfrak p$ a nonzero
prime ideal of $\mathcal O_K$. For $x \in K$ write $c_{\mathfrak p}(x)$ for the exponent of
$\mathfrak p$ in the principal fractional ideal $x \mathcal O_K$, with the convention
$c_{\mathfrak p}(0) = 0$. If $x, y \in K$ satisfy $x + y \neq 0$ and $n \in \mathbb Z$ satisfies
$n \le c_{\mathfrak p}(x)$ and $n \le c_{\mathfrak p}(y)$, then $n \le c_{\mathfrak p}(x + y)$.

Only $x + y \neq 0$ is assumed: $x$ or $y$ may be zero.

Formalized by `NumberField.Modulus.count_spanSingleton_add_ge_of_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#count-span-singleton-add-ge-of-ne-zero).

## Ray elements have order zero at the primes dividing the modulus

Let $m$ be a
modulus of a number field $K$ and let $x \in K^\times$ be a ray element of $m$. Then for
every finite prime $\mathfrak p$ of $K$ dividing the finite part of $m$, the exponent of
$\mathfrak p$ in the principal fractional ideal $x \mathcal O_K$ is $0$.

Formalized by `NumberField.Modulus.rayElement_count_spanSingleton_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-element-count-span-singleton-eq-zero).

## Ray elements have valuation one at the primes dividing the modulus

Let $m$ be a
modulus of a number field $K$ and let $x \in K^\times$ be a ray element of $m$. Then for
every finite prime $\mathfrak p$ of $K$ dividing the finite part of $m$, the multiplicative
$\mathfrak p$-adic valuation of $x$ equals $1$.

## Sources

- N406 §21.3, the supported-finite-place fact; compare [`valuation_eq_one_of_spanSingleton_coprime'`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L1206-L1248) and `hx_coprime`.

Formalized by `NumberField.Modulus.rayElement_valuation_eq_one`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-element-valuation-eq-one).

## Elements of valuation one at the primes dividing a modulus are ray elements

Let $K$ be a
number field, $\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$, and
$a \in K^\times$. If the multiplicative $\mathfrak p$-adic valuation of $a$ equals $1$ at every
nonzero prime ideal $\mathfrak p$ of $\mathcal O_K$ containing $\mathfrak m_0$, then $a$ is
coprime to $\mathfrak m$, that is, a ray element of $\mathfrak m$: its principal fractional ideal
$(a)$ has exponent $0$ at every such $\mathfrak p$.

## Sources

- N406 Section 21.3. This is the converse of `rayElement_valuation_eq_one`, the converse valuation criterion used to turn the controlled approximation witness into a ray element; it is a reusable bridge toward N406, not itself the full source theorem.

Formalized by `NumberField.Modulus.mem_rayElements_of_valuation_eq_one`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#mem-ray-elements-of-valuation-eq-one).

## Product of two elements congruent to one at the finite part

Let $m$ be a modulus
of a number field $K$ and let $x, y \in K^\times$ both be congruent to $1$ at the finite
part of $m$. If moreover $x$ is a ray element of $m$, then $xy$ is congruent to $1$ at the
finite part of $m$.

Formalized by `NumberField.Modulus.CongruentOneAtFinitePart.mul`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#mul).

## Inverses preserve congruence to one at the finite part

Let $K$ be a number field and
$\mathfrak m$ a modulus of $K$. If a ray element $x$ of $\mathfrak m$ is congruent to $1$ at the
finite part of $\mathfrak m$, then so is $x^{-1}$.

Formalized by `NumberField.Modulus.CongruentOneAtFinitePart.inv`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#inv).

## The finite ray-one subgroup

Let $K$ be a number field and $\mathfrak m$ a modulus of $K$
with finite part $\mathfrak m_0$. The finite ray-one subgroup of $\mathfrak m$ is the subgroup of
the group of ray elements of $\mathfrak m$ consisting of the $x$ that are congruent to $1$ at the
finite part of $\mathfrak m$: for every nonzero prime $\mathfrak p$ of $\mathcal O_K$ containing
$\mathfrak m_0$, either $x = 1$ or the exponent of $\mathfrak p$ in $(x - 1) \mathcal O_K$ is at
least the exponent of $\mathfrak p$ in $\mathfrak m_0$.

Formalized by `NumberField.Modulus.finiteRayOneElements`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-ray-one-elements).

## Coprime representation of ray elements

Let $K$ be a number field and $\mathfrak m$ a
modulus of $K$ with finite part $\mathfrak m_0$, a nonzero ideal of $\mathcal O_K$. Every ray
element $x$ of $\mathfrak m$ can be written as $x = a / b$ in $K$ with $a, b \in \mathcal O_K$
whose residue classes are units of $\mathcal O_K / \mathfrak m_0$.

Source (N406 §21.3): the
[`coprime_rep_exists`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L1553-L1747)
admissible integral numerator/denominator representation with both residues units.

Formalized by `NumberField.Modulus.exists_isUnit_mod_finitePart_div_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#exists-is-unit-mod-finite-part-div-eq).

## Equal fractions give equal residues modulo the finite part

Let $m$ be a modulus
of a number field $K$ with finite part $\mathfrak m_0$, an ideal of $\mathcal O_K$, and
write $\bar x$ for the image of $x \in \mathcal O_K$ in $\mathcal O_K / \mathfrak m_0$.
Let $a, b, c, d \in \mathcal O_K$ be such that $\bar a$, $\bar b$, $\bar c$ and $\bar d$
are units. If $a / b = c / d$ in $K$, then $\bar a \bar b^{-1} = \bar c \bar d^{-1}$ in
the unit group $(\mathcal O_K / \mathfrak m_0)^\times$.

Formalized by `NumberField.Modulus.quotientUnits_div_eq_of_div_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#quotient-units-div-eq-of-div-eq).

## Finite residue map

Let $K$ be a number field and $\mathfrak m$ a modulus of $K$ with finite
part $\mathfrak m_0$, a nonzero ideal of $\mathcal O_K$. The finite residue map of $\mathfrak m$ is
the group homomorphism from the ray elements of $\mathfrak m$ to
$(\mathcal O_K / \mathfrak m_0)^\times$ sending $x$ to $\bar a \bar b^{-1}$, where $x = a / b$ with
$a, b \in \mathcal O_K$ whose residue classes $\bar a, \bar b$ are units of
$\mathcal O_K / \mathfrak m_0$; such $a$ and $b$ exist, and the value does not depend on their
choice.

Source (N406 §21.3): the
[`finitePartMapHom`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L1812-L1864)
finite component of the quotient isomorphism.

Formalized by `NumberField.Modulus.finiteResidueMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 622](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L622). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-residue-map).

## Computing the finite residue map from a representation

Let $K$ be a number field and
$\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$. Let $x$ be a ray element of
$\mathfrak m$, and let $a, b \in \mathcal O_K$ have residue classes $\bar a, \bar b$ that are
units of $\mathcal O_K / \mathfrak m_0$ and satisfy $a / b = x$ in $K$. Then the finite residue
map of $\mathfrak m$ sends $x$ to $\bar a \bar b^{-1}$ in $(\mathcal O_K / \mathfrak m_0)^\times$.

Source (N406 §21.3): the representation-independence computation
[`coprime_rep_well_def`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L1757-L1810)
for the finite component.

Formalized by `NumberField.Modulus.finiteResidueMap_apply_of_div_eq`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-residue-map-apply-of-div-eq).

## Kernel criterion for the finite residue map

Let $K$ be a number field and $\mathfrak m$ a
modulus of $K$. A ray element $x$ of $\mathfrak m$ is sent to $1$ by the finite residue map of
$\mathfrak m$ if and only if $x$ is congruent to $1$ at the finite part of $\mathfrak m$.

Source (N406 §21.3): helper
[`finitePartMapHom_ker_iff`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L1996-L2011).

Formalized by `NumberField.Modulus.finiteResidueMap_eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 845](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L845). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-residue-map-eq-one-iff).

## Kernel of the finite residue map

Let $K$ be a number field and $\mathfrak m$ a modulus of
$K$. The kernel of the finite residue map of $\mathfrak m$ is the finite ray-one subgroup of
$\mathfrak m$.

Source (N406 §21.3): the finite kernel component used in the
[`theorem_21_8_quotient_iso`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L2600-L2647).

Formalized by `NumberField.Modulus.finiteResidueMap_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-residue-map-ker).

## Valuation criterion for the finite residue map to be trivial

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$, and $z$ a ray element of
$\mathfrak m$. Suppose that at every nonzero prime ideal $\mathfrak p$ of $\mathcal O_K$
containing $\mathfrak m_0$, the multiplicative $\mathfrak p$-adic valuation of $z - 1$ is at most
$\exp(-e_{\mathfrak p})$, where $e_{\mathfrak p}$ is the exponent of $\mathfrak p$ in
$\mathfrak m_0$; equivalently, $z = 1$ or $z - 1$ has $\mathfrak p$-adic order at least
$e_{\mathfrak p}$. Then the finite residue map of $\mathfrak m$ sends $z$ to $1$ in
$(\mathcal O_K / \mathfrak m_0)^\times$.

## Sources

- N406, Theorem 21.8, Section 21.3 (ATLAS NumberTheoryI item N406): the native-API finite-congruence step corresponding to [`finitePartMapHom_ker_iff`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L1996-L2011), used by the weak-approximation argument before residue/sign surjectivity and by [`theorem_21_8_quotient_iso`](https://github.com/facebookresearch/atlas-lean/blob/e8b31c5cb0bec89b487ce33fe525a2c0b0f8b9c6/v1/Atlas/NumberTheoryI/code/RayClassFields.lean#L2607-L2647). It is not the generalized weak-approximation theorem and not the final N406 result.

Formalized by `NumberField.Modulus.finiteResidueMap_eq_one_of_valuation_le`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean, line 870](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/FiniteCongruence.lean#L870). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#finite-residue-map-eq-one-of-valuation-l).

## Ray class group

The ray class group of a modulus $\mathfrak m$ of a number field $K$ is
the quotient of the group of nonzero fractional ideals of $K$ coprime to the finite part of
$\mathfrak m$ by the ray group of $\mathfrak m$.

Formalized by `NumberField.Modulus.RayClassGroup`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/RayClass/Group.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Group.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-group).

## Ray class map

For a modulus $\mathfrak m$ of a number field $K$, the ray class map is the
canonical quotient homomorphism from the group of nonzero fractional ideals of $K$ coprime to the
finite part of $\mathfrak m$ onto the ray class group of $\mathfrak m$, sending each such ideal to
its class modulo the ray group of $\mathfrak m$.

Formalized by `NumberField.Modulus.rayClassMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/Group.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Group.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-map).

## Sign of a unit at a real place

For a real place $w$ of a number field $K$, let
$\sigma_w \colon K \to \mathbb{R}$ be the corresponding real embedding. The sign at $w$ is the
group homomorphism from $K^\times$ to $\mathbb{Z}/2\mathbb{Z}$, written multiplicatively, that
sends $x$ to the class of $0$ (the identity) if $\sigma_w(x) > 0$ and to the class of $1$
otherwise.

Formalized by `NumberField.Modulus.signAtRealPlace`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#sign-at-real-place).

## Trivial sign at a real place means positivity

Let $w$ be a real place of a number field
$K$ with real embedding $\sigma_w \colon K \to \mathbb{R}$. For every $x \in K^\times$, the sign of
$x$ at $w$, an element of $\mathbb{Z}/2\mathbb{Z}$ written multiplicatively, is the identity if
and only if $\sigma_w(x) > 0$.

Formalized by `NumberField.Modulus.signAtRealPlace_apply_eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#sign-at-real-place-apply-eq-one-iff).

## Infinite sign map of a modulus

Let $m$ be a modulus of a number field $K$ and let
$m_\infty$ be its finite set of real places. The infinite sign map of $m$ is the group
homomorphism from the ray elements of $m$ to the group of functions
$m_\infty \to \mathbb{Z}/2\mathbb{Z}$, with $\mathbb{Z}/2\mathbb{Z}$ written multiplicatively and
the pointwise product, that sends $x$ to the function whose value at $w \in m_\infty$ is the
sign of $x$ at the real place $w$.

Formalized by `NumberField.Modulus.infiniteSignMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#infinite-sign-map).

## Coordinates of the infinite sign map

Let $m$ be a modulus of a number field $K$ with
finite set of real places $m_\infty$. For every ray element $x$ of $m$ and every $w \in m_\infty$,
the value at $w$ of the infinite sign map of $m$ applied to $x$ is the sign of $x$ at the real
place $w$.

Formalized by `NumberField.Modulus.infiniteSignMap_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#infinite-sign-map-apply).

## Trivial infinite sign means positivity at the modulus

Let $m$ be a modulus of a number
field $K$ with finite set of real places $m_\infty$, and for a real place $w$ let $\sigma_w$ be
the corresponding real embedding of $K$. For every ray element $x$ of $m$, the infinite sign map
of $m$ sends $x$ to the identity if and only if $x$ is positive at the infinite part of $m$,
that is, $\sigma_w(x) > 0$ for every $w \in m_\infty$.

Formalized by `NumberField.Modulus.infiniteSignMap_eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#infinite-sign-map-eq-one-iff).

## Ray elements positive at the infinite part

Let $m$ be a modulus of a number field $K$
with finite set of real places $m_\infty$, and for a real place $w$ let $\sigma_w$ be the real
embedding of $K$ at $w$. The positive ray elements of $m$ form the subgroup of the ray elements
of $m$ defined as the kernel of the infinite sign map of $m$; equivalently, they are the ray
elements $x$ with $\sigma_w(x) > 0$ for every $w \in m_\infty$.

Formalized by `NumberField.Modulus.positiveRayElements`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#positive-ray-elements).

## Membership in the positive ray elements

Let $m$ be a modulus of a number field $K$ with
finite set of real places $m_\infty$, and for a real place $w$ let $\sigma_w$ be the real embedding
of $K$ at $w$. A ray element $x$ of $m$ is a positive ray element of $m$ if and only if $x$ is
positive at the infinite part of $m$, that is, $\sigma_w(x) > 0$ for every $w \in m_\infty$.

Formalized by `NumberField.Modulus.mem_positiveRayElements_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InfiniteSign.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#mem-positive-ray-elements-iff).

## Weak approximation with a finite target and prescribed signs

Let $K$ be a number field
and $\mathfrak m$ a modulus of $K$, with finite part $\mathfrak m_0$ (a nonzero ideal of
$\mathcal O_K$) and infinite part $\mathfrak m_\infty$ (a finite set of real places of $K$). For
a nonzero prime $\mathfrak p$ of $\mathcal O_K$ write $v_{\mathfrak p}$ for the
$\mathfrak p$-adic valuation on $K$ (with $v_{\mathfrak p}(0) = \infty$) and $e_{\mathfrak p}$
for the exponent of $\mathfrak p$ in $\mathfrak m_0$; for a real place $w$ write
$\sigma_w : K \to \mathbb R$ for its real embedding. Let $P$ be any set of places in
$\mathfrak m_\infty$, and let $a \in K$ be nonzero with $v_{\mathfrak p}(a) = 0$ for every
nonzero prime $\mathfrak p$ dividing $\mathfrak m_0$. Then there is a nonzero $x \in K$ such
that $v_{\mathfrak p}(x) = 0$ and $v_{\mathfrak p}(x - a) \ge e_{\mathfrak p}$ for every nonzero
prime $\mathfrak p$ dividing $\mathfrak m_0$, and such that for every $w \in \mathfrak m_\infty$,
$\sigma_w(x) > 0$ if $w \in P$ and $\sigma_w(x) < 0$ if $w \notin P$.

## Sources

- mapping toward ATLAS N406, Theorem 21.8, Section 21.3 (`weak_approx_coprime_sign_finitePart`, lines 2255--2568): the finite target `a` is lifted at source lines 2267--2275 with supported valuation-one hypothesis at 2277--2292; the finite/infinite index family below is at 2314--2385; modulus-dependent tolerances at 2388--2404; nonzero witness at 2406--2412; valuation preservation at 2414--2451; sign control at 2458--2477; and the strict absolute-value-to-discrete-valuation residue comparison at 2480--2568.

Formalized by `NumberField.Modulus.exists_ne_zero_with_target_and_sign`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/WeakApproximation.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/WeakApproximation.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#exists-ne-zero-with-target-and-sign).

## Weak approximation with prescribed signs at a modulus

Let $K$ be a number field and
$\mathfrak m$ a modulus of $K$, with finite part $\mathfrak m_0$ (a nonzero ideal of
$\mathcal O_K$) and infinite part $\mathfrak m_\infty$ (a finite set of real places of $K$); for
a real place $w$ write $\sigma_w : K \to \mathbb R$ for its real embedding. For every set $P$ of
places in $\mathfrak m_\infty$ there is a nonzero $x \in K$ whose $\mathfrak p$-adic valuation
is $0$ for every nonzero prime $\mathfrak p$ of $\mathcal O_K$ dividing $\mathfrak m_0$, and such
that for every $w \in \mathfrak m_\infty$, $\sigma_w(x) > 0$ if $w \in P$ and $\sigma_w(x) < 0$
if $w \notin P$.

This is the special case of weak approximation with a finite target and prescribed signs in
which the target is $1$.

Formalized by `NumberField.Modulus.exists_ne_zero_with_valuation_one_and_sign`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/WeakApproximation.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/WeakApproximation.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#exists-ne-zero-with-valuation-one-and-si).

## Residue-sign target

Let $m$ be a modulus of a number field $K$, with finite part the
nonzero ideal $\mathfrak{m}_0$ of the ring of integers $\mathcal{O}_K$ and infinite part the
finite set $S$ of real places of $K$. Let $G$ denote $\mathbb{Z}/2\mathbb{Z}$ written
multiplicatively, let $G^S$ denote the group of functions from $S$ to $G$ (one sign for each place
in $S$), and let $(\mathcal{O}_K/\mathfrak{m}_0)^\times$ denote the unit group of the quotient ring
$\mathcal{O}_K/\mathfrak{m}_0$. The residue-sign target of $m$ is the product group
$G^S \times (\mathcal{O}_K/\mathfrak{m}_0)^\times$.

Formalized by `NumberField.Modulus.ResidueSignTarget`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-target).

## Residue-sign map

Let $m$ be a modulus of a number field $K$. The residue-sign map of $m$
is the group homomorphism from the ray elements of $m$ to the residue-sign target of $m$ that
sends a ray element $x$ to the pair formed by the image of $x$ under the infinite sign map of $m$
and the image of $x$ under the finite residue map of $m$.

Formalized by `NumberField.Modulus.residueSignMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-map).

## Components of the residue-sign map

Let $m$ be a modulus of a number field $K$. For every
ray element $x$ of $m$, the image of $x$ under the residue-sign map of $m$ is the pair whose first
component is the image of $x$ under the infinite sign map of $m$ and whose second component is the
image of $x$ under the finite residue map of $m$.

Formalized by `NumberField.Modulus.residueSignMap_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-map-apply).

## Ray-one subgroup

Let $m$ be a modulus of a number field $K$. The ray-one subgroup of $m$ is
the subgroup of the ray elements of $m$ consisting of the ray elements $x$ that lie in the finite
ray-one subgroup of $m$ (those congruent to $1$ at the finite part of $m$) and in the subgroup of
ray elements positive at every real place in the infinite part of $m$.

Formalized by `NumberField.Modulus.rayOneElements`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-one-elements).

## Membership in the ray-one subgroup

Let $m$ be a modulus of a number field $K$. A ray
element $x$ of $m$ lies in the ray-one subgroup of $m$ if and only if $x$ is congruent to $1$ at
the finite part of $m$ and $x$ is positive at every real place in the infinite part of $m$.

Formalized by `NumberField.Modulus.mem_rayOneElements_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#mem-ray-one-elements-iff).

## Surjectivity of the residue-sign map

Let $m$ be a modulus of a number field $K$. Every
element of the residue-sign target of $m$ is the image of some ray element of $m$ under the
residue-sign map of $m$.

Formalized by `NumberField.Modulus.residueSignMap_surjective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-map-surjective).

## Kernel of the residue-sign map

Let $m$ be a modulus of a number field $K$. The kernel of
the residue-sign map of $m$ is the ray-one subgroup of $m$.

Formalized by `NumberField.Modulus.residueSignMap_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-map-ker).

## Kernel criterion for the residue-sign map

Let $m$ be a modulus of a number field $K$. A
ray element $x$ of $m$ is sent to $1$ by the residue-sign map of $m$ if and only if $x$ is a ray
element congruent to $1$ modulo $m$: $x$ is a ray element of $m$, $x$ is congruent to $1$ at the
finite part of $m$, and $x$ is positive at every real place in the infinite part of $m$.

Formalized by `NumberField.Modulus.residueSignMap_eq_one_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-map-eq-one-iff).

## The residue-sign isomorphism

Let $m$ be a modulus of a number field $K$. The residue-sign
isomorphism of $m$ is the group isomorphism from the quotient of the ray elements of $m$ by the
ray-one subgroup of $m$ onto the residue-sign target of $m$ induced by the residue-sign map, which
is surjective with kernel the ray-one subgroup; it sends the class of a ray element $x$ to the
image of $x$ under the residue-sign map.

Formalized by `NumberField.Modulus.rayElementsQuotientEquivResidueSign`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-elements-quotient-equiv-residue-sign).

## The residue-sign isomorphism on classes

Let $m$ be a modulus of a number field $K$. For
every ray element $x$ of $m$, the residue-sign isomorphism of $m$ sends the class of $x$ in the
quotient of the ray elements of $m$ by the ray-one subgroup to the image of $x$ under the
residue-sign map of $m$.

Formalized by `NumberField.Modulus.rayElementsQuotientEquivResidueSign_mk`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ResidueSign.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-elements-quotient-equiv-residue-sign-2).

## Embedding of integral units into field units

Let $K$ be a field and $\mathcal{O}_K$ its
ring of integers, the integral closure of $\mathbb{Z}$ in $K$. This is the group homomorphism
$\mathcal{O}_K^\times \to K^\times$ induced by the inclusion $\mathcal{O}_K \subseteq K$: it sends
a unit of $\mathcal{O}_K$ to the same element regarded as a unit of $K$.

## Sources

- ATLAS `okUnitsToKUnits`.

Formalized by `NumberField.Modulus.integralUnitsToFieldUnits`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-field-units).

## Integral units embed injectively into field units

Let $K$ be a field and $\mathcal{O}_K$
its ring of integers, the integral closure of $\mathbb{Z}$ in $K$. The group homomorphism
$\mathcal{O}_K^\times \to K^\times$ induced by the inclusion $\mathcal{O}_K \subseteq K$ is
injective.

Formalized by `NumberField.Modulus.integralUnitsToFieldUnits_injective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-field-units-injective).

## Integral units as ray elements

Let $K$ be a number field with ring of integers
$\mathcal{O}_K$, let $\mathfrak{m}$ be a modulus of $K$, and let
$K_{\mathfrak{m}} \subseteq K^\times$ be the group of ray elements for $\mathfrak{m}$. Every unit
of $\mathcal{O}_K$ has $\mathfrak{p}$-adic valuation $0$ at every prime $\mathfrak{p}$ of
$\mathcal{O}_K$, so it lies in $K_{\mathfrak{m}}$. This is the group homomorphism
$\mathcal{O}_K^\times \to K_{\mathfrak{m}}$ sending a unit $u$ to its image in $K^\times$.

## Sources

- ATLAS `okUnitsToUnitsCoprime`; ATLAS `valuation_algebraMap_unit_eq_one` is discharged inline in the definition.

Formalized by `NumberField.Modulus.integralUnitsToRayElements`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-elements).

## Ray-element image of an integral unit as a field unit

Let $K$ be a number field with
ring of integers $\mathcal{O}_K$, let $\mathfrak{m}$ be a modulus of $K$, and let
$u \in \mathcal{O}_K^\times$. The image of $u$ in the group of ray elements for $\mathfrak{m}$,
regarded as an element of $K^\times$, equals the image of $u$ under the embedding
$\mathcal{O}_K^\times \to K^\times$.

Formalized by `NumberField.Modulus.integralUnitsToRayElements_coe`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-elements-coe).

## Integral units embed injectively into the ray elements

Let $K$ be a number field with
ring of integers $\mathcal{O}_K$ and let $\mathfrak{m}$ be a modulus of $K$. The homomorphism
from $\mathcal{O}_K^\times$ to the group of ray elements for $\mathfrak{m}$ that sends a unit to
its image in $K^\times$ is injective.

Formalized by `NumberField.Modulus.integralUnitsToRayElements_injective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-elements-injective).

## Ray-one integral units

Let $K$ be a number field with ring of integers $\mathcal{O}_K$,
let $\mathfrak{m}$ be a modulus of $K$ with finite part $\mathfrak{m}_0$, and send each unit of
$\mathcal{O}_K$ to its image in the group of ray elements for $\mathfrak{m}$. For a nonzero prime
$\mathfrak{p}$ of $\mathcal{O}_K$, write $v_{\mathfrak{p}}$ for the $\mathfrak{p}$-adic valuation
of nonzero elements and nonzero ideals. The ray-one integral units for $\mathfrak{m}$ form the
subgroup of $\mathcal{O}_K^\times$ of those units $u$ whose image lies in the ray-one subgroup,
that is: for every prime $\mathfrak{p}$ dividing $\mathfrak{m}_0$, either $u = 1$ or
$v_{\mathfrak{p}}(u - 1) \ge v_{\mathfrak{p}}(\mathfrak{m}_0)$, and $u$ is positive under the
real embedding of every real place in the infinite part of $\mathfrak{m}$.

## Sources

- ATLAS `UnitsInCongruenceSubgroup`.

Formalized by `NumberField.Modulus.integralRayOneUnits`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-ray-one-units).

## Membership in the ray-one integral units

Let $\mathfrak m$ be a modulus of a number field
$K$ with finite part $\mathfrak m_0$ and set of real places $\mathfrak m_\infty$, and for a nonzero
prime $\mathfrak p$ of the ring of integers $\mathcal O_K$ write $v_{\mathfrak p}$ for the exponent
of $\mathfrak p$ in a fractional ideal of $K$, applied to an element through its principal
fractional ideal. A unit $u$ of $\mathcal O_K$ lies in the subgroup of ray-one integral units if
and only if $u$, viewed as an element of $K^\times$, is a ray element congruent to $1$ modulo
$\mathfrak m$: its principal fractional ideal is coprime to $\mathfrak m_0$, for every nonzero
prime $\mathfrak p$ dividing $\mathfrak m_0$ either $u = 1$ or
$v_{\mathfrak p}(u - 1) \ge v_{\mathfrak p}(\mathfrak m_0)$, and $u$ is positive under the real
embedding of every place in $\mathfrak m_\infty$.

Formalized by `NumberField.Modulus.mem_integralRayOneUnits_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#mem-integral-ray-one-units-iff).

## Inclusion of the ray-one integral units

Let $K$ be a number field with ring of integers
$\mathcal{O}_K$ and let $\mathfrak{m}$ be a modulus of $K$. The inclusion of the ray-one integral
units for $\mathfrak{m}$ is the group homomorphism from the subgroup of ray-one integral units for
$\mathfrak{m}$ to $\mathcal{O}_K^\times$ that sends each such unit to itself.

## Sources

- ATLAS `exactSeq_map1`.

Formalized by `NumberField.Modulus.integralRayOneUnitsInclusion`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-ray-one-units-inclusion).

## Map from integral units to the ray quotient

Let $\mathfrak m$ be a modulus of a number
field $K$, let $K_{\mathfrak m} \le K^\times$ be the group of ray elements (elements whose principal
fractional ideal is coprime to the finite part of $\mathfrak m$) and let
$K_{\mathfrak m,1} \le K_{\mathfrak m}$ be the ray-one subgroup. This is the group homomorphism
$\mathcal O_K^\times \to K_{\mathfrak m}/K_{\mathfrak m,1}$ sending a unit $u$ of the ring of
integers $\mathcal O_K$ to the coset of $u$, viewed as an element of $K_{\mathfrak m}$.

## Sources

- ATLAS `exactSeq_map2`.

Formalized by `NumberField.Modulus.integralUnitsToRayQuotient`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-quotient).

## Value of the ray-quotient map on integral units

Let $\mathfrak m$ be a modulus of a
number field $K$, let $K_{\mathfrak m} \le K^\times$ be the group of ray elements (elements whose
principal fractional ideal is coprime to the finite part of $\mathfrak m$) and let
$K_{\mathfrak m,1} \le K_{\mathfrak m}$ be the ray-one subgroup. For every unit $u$ of the ring of
integers $\mathcal O_K$, the map $\mathcal O_K^\times \to K_{\mathfrak m}/K_{\mathfrak m,1}$ sends
$u$ to the coset of $u$, viewed as an element of $K_{\mathfrak m}$.

Formalized by `NumberField.Modulus.integralUnitsToRayQuotient_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-quotient-apply).

## Residue-sign map on integral units

Let $\mathfrak m$ be a modulus of a number field $K$
with finite part $\mathfrak m_0$ and set of real places $\mathfrak m_\infty$, let
$K_{\mathfrak m} \le K^\times$ be the group of ray elements and let
$K_{\mathfrak m,1} \le K_{\mathfrak m}$ be the ray-one subgroup. The residue-sign map on integral
units is the group homomorphism from $\mathcal O_K^\times$ to
$(\mathbb Z/2\mathbb Z)^{\mathfrak m_\infty} \times (\mathcal O_K/\mathfrak m_0)^\times$, with
$\mathbb Z/2\mathbb Z$ written multiplicatively, obtained by composing the map
$\mathcal O_K^\times \to K_{\mathfrak m}/K_{\mathfrak m,1}$ sending a unit to its coset with the
isomorphism from $K_{\mathfrak m}/K_{\mathfrak m,1}$ onto this group induced by the residue-sign
homomorphism on $K_{\mathfrak m}$.

Formalized by `NumberField.Modulus.integralUnitsToResidueSign`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-residue-sign).

## Value of the residue-sign map on integral units

Let $\mathfrak m$ be a modulus of a
number field $K$ and let $K_{\mathfrak m} \le K^\times$ be the group of ray elements. For every unit
$u$ of the ring of integers $\mathcal O_K$, the residue-sign map on integral units sends $u$ to the
image of $u$, viewed as an element of $K_{\mathfrak m}$, under the residue-sign homomorphism on
$K_{\mathfrak m}$.

Formalized by `NumberField.Modulus.integralUnitsToResidueSign_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-residue-sign-apply).

## Kernel of the ray-quotient map on integral units

Let $\mathfrak m$ be a modulus of a
number field $K$, let $K_{\mathfrak m} \le K^\times$ be the group of ray elements and
$K_{\mathfrak m,1} \le K_{\mathfrak m}$ the ray-one subgroup. The kernel of the homomorphism
$\mathcal O_K^\times \to K_{\mathfrak m}/K_{\mathfrak m,1}$ sending a unit of the ring of integers
$\mathcal O_K$ to its coset is the subgroup of ray-one integral units, the units of $\mathcal O_K$
that lie in $K_{\mathfrak m,1}$.

Formalized by `NumberField.Modulus.integralUnitsToRayQuotient_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-quotient-ker).

## Kernel of the residue-sign map on integral units

Let $\mathfrak m$ be a modulus of a
number field $K$. The kernel of the residue-sign map on the unit group $\mathcal O_K^\times$ of the
ring of integers is the subgroup of ray-one integral units, the units of $\mathcal O_K$ whose image
in the group of ray elements modulo $\mathfrak m$ lies in its ray-one subgroup.

Formalized by `NumberField.Modulus.integralUnitsToResidueSign_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-residue-sign-ker).

## The inclusion of the ray-one integral units is injective

Let $K$ be a number field
with ring of integers $\mathcal{O}_K$ and let $\mathfrak{m}$ be a modulus of $K$. The inclusion
homomorphism from the subgroup of ray-one integral units for $\mathfrak{m}$ into the unit group
$\mathcal{O}_K^\times$ is injective.

Formalized by `NumberField.Modulus.integralRayOneUnitsInclusion_injective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-ray-one-units-inclusion-injecti).

## Exactness of the ray sequence at the integral units

Let $K$ be a number field with ring
of integers $\mathcal{O}_K$ and let $\mathfrak{m}$ be a modulus of $K$. Write $K_{\mathfrak{m}}$
for the group of ray elements for $\mathfrak{m}$, $K_{\mathfrak{m},1}$ for its ray-one subgroup,
and $U_{\mathfrak{m},1} \subseteq \mathcal{O}_K^\times$ for the subgroup of ray-one integral units.
Consider the sequence

$$U_{\mathfrak{m},1} \to \mathcal{O}_K^\times \to K_{\mathfrak{m}}/K_{\mathfrak{m},1}$$

whose first map is the inclusion and whose second map sends a unit to the class of its image in
$K_{\mathfrak{m}}$. For every $u \in \mathcal{O}_K^\times$, the class of $u$ is the identity if
and only if $u$ lies in the image of the first map; that is, the sequence is exact at
$\mathcal{O}_K^\times$.

## Sources

- ATLAS `exactSeq_exact_at_units`.

Formalized by `NumberField.Modulus.integralUnits_mulExact_quotient`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-mul-exact-quotient).

## Exactness at the integral units, residue-sign form

Let $K$ be a number field with ring
of integers $\mathcal{O}_K$ and let $\mathfrak{m}$ be a modulus of $K$ with finite part
$\mathfrak{m}_0$. Let $T_{\mathfrak{m}}$ be the residue-sign target of $\mathfrak{m}$: the product
of a copy of $\mathbb{Z}/2\mathbb{Z}$, written multiplicatively, for each real place in the
infinite part of $\mathfrak{m}$, with $(\mathcal{O}_K/\mathfrak{m}_0)^\times$. Let
$\rho \colon \mathcal{O}_K^\times \to T_{\mathfrak{m}}$ send a unit to the class of its image in
the quotient of the group of ray elements for $\mathfrak{m}$ by its ray-one subgroup, followed by
the canonical isomorphism of that quotient with $T_{\mathfrak{m}}$ induced by the residue-sign
map. Then for every $u \in \mathcal{O}_K^\times$, $\rho(u) = 1$ if and only if $u$ is in the image
of the inclusion of the ray-one integral units for $\mathfrak{m}$ into $\mathcal{O}_K^\times$.

Formalized by `NumberField.Modulus.integralUnits_mulExact_residueSign`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/IntegralUnits.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-mul-exact-residue-sign).

## Principal ray ideal map

Let $\mathfrak m$ be a modulus of a number field $K$ with ring of
integers $\mathcal O_K$. The principal ray ideal map is the group homomorphism from the group of
ray elements for $\mathfrak m$ (the $x \in K^\times$ whose principal ideal is coprime to
$\mathfrak m$) to the group of fractional ideals coprime to $\mathfrak m$ that sends $x$ to the
principal fractional ideal $x\mathcal O_K$.

Formalized by `NumberField.Modulus.principalRayIdealMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#principal-ray-ideal-map).

## Value of the principal ray ideal map

Let $\mathfrak m$ be a modulus of a number field
$K$ with ring of integers $\mathcal O_K$. For every ray element $x \in K^\times$ for
$\mathfrak m$, the image of $x$ under the principal ray ideal map, viewed as an invertible
fractional ideal of $K$, is the principal fractional ideal $x\mathcal O_K$.

Formalized by `NumberField.Modulus.principalRayIdealMap_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#principal-ray-ideal-map-apply).

## Principal ideals agree exactly up to an integral unit

Let $K$ be a number field with ring
of integers $\mathcal O_K$. For all $x, y \in K^\times$, the principal fractional ideals
$x\mathcal O_K$ and $y\mathcal O_K$ are equal if and only if $x = uy$ for some unit
$u \in \mathcal O_K^\times$.

Formalized by `NumberField.Modulus.toPrincipalIdeal_eq_iff_exists_integralUnit_mul`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#to-principal-ideal-eq-iff-exists-integra).

## The ray group is the image of the ray-one elements

Let $\mathfrak m$ be a modulus of a
number field $K$. The ray group of $\mathfrak m$ equals the image under the principal ray ideal
map of the subgroup of ray-one elements, that is, of the ray elements for $\mathfrak m$ that are
congruent to $1$ modulo the finite part of $\mathfrak m$ and positive at every real place in
its infinite part.

Formalized by `NumberField.Modulus.rayGroup_eq_map_rayOneElements`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/PrincipalIdeal.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-group-eq-map-ray-one-elements).

## Ray-element class map

For a modulus $\mathfrak m$ of a number field $K$, the ray-element
class map is the group homomorphism from the group of ray elements of $\mathfrak m$ to the ray
class group $\mathrm{Cl}_{\mathfrak m}$ that sends $x$ to the ray class of its principal
fractional ideal $(x)$, which is coprime to $\mathfrak m$; that is, the principal-ideal map
followed by the projection onto the ray class group.

## Sources

- ATLAS `exactSeq_map3`, before the quotient lift.

Formalized by `NumberField.Modulus.rayElementClassMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-element-class-map).

## Value of the ray-element class map

Let $\mathfrak m$ be a modulus of a number field $K$
and let $\mathrm{Cl}_{\mathfrak m}$ be its ray class group. For every ray element $x$ of
$\mathfrak m$, the ray-element class map sends $x$ to the ray class in $\mathrm{Cl}_{\mathfrak m}$
of the principal fractional ideal $(x)$, viewed as a fractional ideal coprime to $\mathfrak m$.

Formalized by `NumberField.Modulus.rayElementClassMap_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-element-class-map-apply).

## Ray-one elements have trivial ray class

Let $\mathfrak m$ be a modulus of a number field
$K$. Every ray-one element of $\mathfrak m$ lies in the kernel of the ray-element class map; that
is, its principal fractional ideal has trivial class in the ray class group
$\mathrm{Cl}_{\mathfrak m}$.

Formalized by `NumberField.Modulus.rayOneElements_le_rayElementClassMap_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-one-elements-le-ray-element-class-ma).

## Quotient-to-ray-class map

For a modulus $\mathfrak m$ of a number field $K$, the
quotient-to-ray-class map is the group homomorphism from the quotient of the group of ray
elements of $\mathfrak m$ by the subgroup of ray-one elements to the ray class group
$\mathrm{Cl}_{\mathfrak m}$ induced by the ray-element class map: the class of a ray element $x$
goes to the ray class of its principal fractional ideal $(x)$. It is well defined because
ray-one elements lie in the kernel of the ray-element class map.

## Sources

- ATLAS `exactSeq_map3`.

Formalized by `NumberField.Modulus.rayQuotientToRayClassGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-quotient-to-ray-class-group).

## Quotient-to-ray-class map on representatives

Let $\mathfrak m$ be a modulus of a number
field $K$. For every ray element $x$ of $\mathfrak m$, the quotient-to-ray-class map sends the
class of $x$ modulo the ray-one elements to the image of $x$ under the ray-element class map.

Formalized by `NumberField.Modulus.rayQuotientToRayClassGroup_mk`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-quotient-to-ray-class-group-mk).

## Integral units generate the unit ideal

Let $\mathfrak m$ be a modulus of a number field
$K$. For every unit $u \in \mathcal O_K^\times$, viewed as a ray element of $\mathfrak m$, the
principal fractional ideal $(u)$, as an element of the group of fractional ideals coprime to
$\mathfrak m$, is the identity element $\mathcal O_K$.

## Sources

- ATLAS lines 1160--1175, an input to exactness at the quotient.

Formalized by `NumberField.Modulus.principalRayIdealMap_integralUnitsToRayElements`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#principal-ray-ideal-map-integral-units-t).

## Exactness at the ray-element quotient (kernel form)

Let $\mathfrak m$ be a modulus of a
number field $K$. The kernel of the quotient-to-ray-class map, from the quotient of the ray
elements of $\mathfrak m$ by the ray-one elements to the ray class group
$\mathrm{Cl}_{\mathfrak m}$, equals the image of the map sending each unit
$u \in \mathcal O_K^\times$ to the class of $u$ in that quotient.

## Sources

- ATLAS `exactSeq_exact_at_quotient`.

Formalized by `NumberField.Modulus.rayQuotientToRayClassGroup_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-quotient-to-ray-class-group-ker).

## Exactness at the ray-element quotient

Let $\mathfrak m$ be a modulus of a number field
$K$, let $K_{\mathfrak m}$ be the group of ray elements (elements of $K^\times$ whose principal
ideal is coprime to the finite part of $\mathfrak m$), let $K_{\mathfrak m,1} \le K_{\mathfrak m}$
be the subgroup of ray-one elements, and let $\mathrm{Cl}_{\mathfrak m}$ be the ray class group
of $\mathfrak m$. In the sequence
$\mathcal O_K^\times \to K_{\mathfrak m}/K_{\mathfrak m,1} \to \mathrm{Cl}_{\mathfrak m}$,
where the first map sends a unit $u$ to the class of $u$ and the second sends the class of a ray
element $x$ to the ray class of the principal fractional ideal $(x)$, an element of
$K_{\mathfrak m}/K_{\mathfrak m,1}$ maps to the identity of $\mathrm{Cl}_{\mathfrak m}$ if and
only if it is the image of an integral unit.

## Sources

- ATLAS `exactSeq_exact_at_quotient`.

Formalized by `NumberField.Modulus.integralUnitsToRayQuotient_mulExact_rayQuotientToRayClassGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-ray-quotient-mul-exact).

## Ray class map on residues and signs

Let $\mathfrak m$ be a modulus of a number field
$K$ with finite part $\mathfrak m_0$, let $K_{\mathfrak m}$ be the group of elements of $K^\times$
whose principal ideal is coprime to $\mathfrak m_0$, and let $K_{\mathfrak m,1}$ be its subgroup
of elements congruent to $1$ modulo $\mathfrak m_0$ and positive at every real place of
$\mathfrak m$. Let $T_{\mathfrak m}$ be the residue-sign target of $\mathfrak m$ and let
$\mathrm{Cl}_{\mathfrak m}$ be the ray class group of $\mathfrak m$. Let
$\psi : K_{\mathfrak m}/K_{\mathfrak m,1} \to T_{\mathfrak m}$ be the canonical isomorphism
induced by sending $x$ to its signs at the real places of $\mathfrak m$ and its residue modulo
$\mathfrak m_0$, and let $\phi : K_{\mathfrak m}/K_{\mathfrak m,1} \to \mathrm{Cl}_{\mathfrak m}$
be the homomorphism induced by sending $x \in K_{\mathfrak m}$ to the ray class of its principal
ideal $(x)$. The residue-sign-to-ray-class map is the group homomorphism
$\phi \circ \psi^{-1} : T_{\mathfrak m} \to \mathrm{Cl}_{\mathfrak m}$.

Formalized by `NumberField.Modulus.residueSignToRayClassGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-to-ray-class-group).

## Residue-sign-to-ray-class map through the quotient isomorphism

Let $\mathfrak m$ be a
modulus of a number field $K$ with finite part $\mathfrak m_0$, let $K_{\mathfrak m}$ be the
group of elements of $K^\times$ whose principal ideal is coprime to $\mathfrak m_0$, and let
$K_{\mathfrak m,1}$ be its subgroup of elements congruent to $1$ modulo $\mathfrak m_0$ and
positive at every real place of $\mathfrak m$. Let $T_{\mathfrak m}$ be the residue-sign target
of $\mathfrak m$, let $\mathrm{Cl}_{\mathfrak m}$ be the ray class group of $\mathfrak m$, let
$\psi : K_{\mathfrak m}/K_{\mathfrak m,1} \to T_{\mathfrak m}$ be the canonical isomorphism
induced by sending $x$ to its signs at the real places of $\mathfrak m$ and its residue modulo
$\mathfrak m_0$, and let $\phi : K_{\mathfrak m}/K_{\mathfrak m,1} \to \mathrm{Cl}_{\mathfrak m}$
be the homomorphism induced by sending $x$ to the ray class of its principal ideal $(x)$. Then
for every $q \in K_{\mathfrak m}/K_{\mathfrak m,1}$, the residue-sign-to-ray-class map
$T_{\mathfrak m} \to \mathrm{Cl}_{\mathfrak m}$ sends $\psi(q)$ to $\phi(q)$.

Formalized by `NumberField.Modulus.residueSignToRayClassGroup_equiv`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-to-ray-class-group-equiv).

## Ray class map on residue-sign values

Let $\mathfrak m$ be a modulus of a number field
$K$ and let $x$ be a ray element of $\mathfrak m$, that is, $x \in K^\times$ with principal ideal
coprime to the finite part of $\mathfrak m$. Then the residue-sign-to-ray-class map sends the
residue-sign value of $x$ (its signs at the real places of $\mathfrak m$ together with its
residue modulo the finite part) to the ray class of the principal ideal $(x)$.

Formalized by `NumberField.Modulus.residueSignToRayClassGroup_residueSignMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-to-ray-class-group-residue).

## The residue-sign transport square commutes

Let $\mathfrak m$ be a modulus of a number
field $K$. The residue-sign map from the ray elements of $\mathfrak m$ to the residue-sign target,
followed by the transported residue-sign-to-ray-class map, equals the ray-element class map.

Formalized by `NumberField.Modulus.residueSignToRayClassGroup_comp_residueSignMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-to-ray-class-group-comp-res).

## Kernel of the ray class map on residue-sign values

Let $\mathfrak m$ be a modulus of a
number field $K$. The kernel of the residue-sign-to-ray-class map from the residue-sign target
of $\mathfrak m$ to the ray class group of $\mathfrak m$ equals the image of the homomorphism
$\mathcal O_K^\times \to$ (residue-sign target) that sends a unit $u$ to its residue-sign value,
namely its signs at the real places of $\mathfrak m$ together with its residue modulo the finite
part of $\mathfrak m$.

Formalized by `NumberField.Modulus.residueSignToRayClassGroup_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-to-ray-class-group-ker).

## Exactness at the residue-sign group

Let $\mathfrak m$ be a modulus of a number field
$K$ with finite part $\mathfrak m_0$ and set of real places $\mathfrak m_\infty$, let
$\mathrm{Cl}_{\mathfrak m}$ be its ray class group, and let
$R_{\mathfrak m} = \{\pm 1\}^{\mathfrak m_\infty} \times (\mathcal O_K/\mathfrak m_0)^\times$.
Consider the maps $\mathcal O_K^\times \to R_{\mathfrak m} \to \mathrm{Cl}_{\mathfrak m}$. The
first sends a unit $u$ to its signs at the places in $\mathfrak m_\infty$ together with its class
in $(\mathcal O_K/\mathfrak m_0)^\times$. The second is the quotient-to-ray-class map transported
along the canonical isomorphism from the quotient of the ray elements by the ray-one elements
onto $R_{\mathfrak m}$, so it sends the image in $R_{\mathfrak m}$ of a ray element $x$ to the
ray class of the principal fractional ideal $(x)$. An element of $R_{\mathfrak m}$ maps to the
identity of $\mathrm{Cl}_{\mathfrak m}$ if and only if it is the image of an integral unit.

Formalized by `NumberField.Modulus.integralUnitsToResidueSign_mulExact_residueSignToRayClassGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/QuotientToRayClass.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#integral-units-to-residue-sign-mul-exact).

## Ideal-class map on coprime fractional ideals

Let $K$ be a number field, $\mathfrak m$ a
modulus of $K$, and $I_{\mathfrak m}$ the group of nonzero fractional ideals of $\mathcal O_K$
coprime to the finite part of $\mathfrak m$. The coprime ideal-class map is the group homomorphism
$I_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K)$ that sends $I$ to its ideal class $[I]$: the
inclusion of $I_{\mathfrak m}$ into the group of nonzero fractional ideals followed by the class
map.

## Sources

- ATLAS `exactSeq_map4`, before the quotient lift.

Formalized by `NumberField.Modulus.coprimeIdealClassMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#coprime-ideal-class-map).

## Value of the ideal-class map on a coprime ideal

Let $K$ be a number field, $\mathfrak m$ a
modulus of $K$, and $I_{\mathfrak m}$ the group of nonzero fractional ideals of $\mathcal O_K$
coprime to the finite part of $\mathfrak m$. For every $I \in I_{\mathfrak m}$, the coprime
ideal-class map sends $I$ to the class $[I]$ in the class group $\mathrm{Cl}(\mathcal O_K)$ of $I$
viewed as a nonzero fractional ideal.

Formalized by `NumberField.Modulus.coprimeIdealClassMap_apply`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#coprime-ideal-class-map-apply).

## The ray group lies in the kernel of the ideal-class map

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$, $I_{\mathfrak m}$ the group of nonzero fractional ideals of
$\mathcal O_K$ coprime to the finite part of $\mathfrak m$, and $P_{\mathfrak m} \subseteq
I_{\mathfrak m}$ the ray group. Then $P_{\mathfrak m}$ is contained in the kernel of the coprime
ideal-class map $I_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K)$, $I \mapsto [I]$: every ideal in
$P_{\mathfrak m}$ has trivial class in $\mathrm{Cl}(\mathcal O_K)$.

Formalized by `NumberField.Modulus.rayGroup_le_coprimeIdealClassMap_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-group-le-coprime-ideal-class-map-ker).

## Projection from the ray class group to the class group

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$, $I_{\mathfrak m}$ the group of nonzero fractional ideals of
$\mathcal O_K$ coprime to the finite part of $\mathfrak m$, $P_{\mathfrak m}$ the ray group, and
$\mathrm{Cl}_{\mathfrak m} = I_{\mathfrak m}/P_{\mathfrak m}$ the ray class group. The projection
$\mathrm{Cl}_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K)$ is the group homomorphism induced by the
coprime ideal-class map $I_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K)$, $I \mapsto [I]$, which is
trivial on $P_{\mathfrak m}$; it sends the ray class of $I$ to $[I]$.

## Sources

- ATLAS `exactSeq_map4`.

Formalized by `NumberField.Modulus.rayClassToClassGroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group).

## Projection to the class group on ray class representatives

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$, $I_{\mathfrak m}$ the group of nonzero fractional ideals of
$\mathcal O_K$ coprime to the finite part of $\mathfrak m$, and $\mathrm{Cl}_{\mathfrak m}$ the ray
class group. For every $I \in I_{\mathfrak m}$, the projection $\mathrm{Cl}_{\mathfrak m} \to
\mathrm{Cl}(\mathcal O_K)$ sends the ray class of $I$ to $[I]$, the value of the coprime
ideal-class map at $I$.

Formalized by `NumberField.Modulus.rayClassToClassGroup_rayClassMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group-ray-class-map).

## The ideal-class map factors through the ray class group

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$, $I_{\mathfrak m}$ the group of nonzero fractional ideals of
$\mathcal O_K$ coprime to the finite part of $\mathfrak m$, $P_{\mathfrak m} \subseteq
I_{\mathfrak m}$ the ray group, and $\mathrm{Cl}_{\mathfrak m} = I_{\mathfrak m}/P_{\mathfrak m}$
the ray class group. As group homomorphisms, the quotient map $I_{\mathfrak m} \to
\mathrm{Cl}_{\mathfrak m}$ followed by the projection $\mathrm{Cl}_{\mathfrak m} \to
\mathrm{Cl}(\mathcal O_K)$ equals the coprime ideal-class map $I_{\mathfrak m} \to
\mathrm{Cl}(\mathcal O_K)$, $I \mapsto [I]$.

Formalized by `NumberField.Modulus.rayClassToClassGroup_comp_rayClassMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group-comp-ray-class).

## Projecting the image of a ray element to the class group

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$, $I_{\mathfrak m}$ the group of
nonzero fractional ideals of $\mathcal O_K$ coprime to $\mathfrak m_0$, $\mathrm{Cl}_{\mathfrak m}$
the ray class group, $K_{\mathfrak m}$ the group of $x \in K^\times$ with
$x\mathcal O_K \in I_{\mathfrak m}$, and $K_{\mathfrak m,1} \subseteq K_{\mathfrak m}$ the subgroup
of those $x$ with $x \equiv 1 \pmod{\mathfrak m_0}$ that are positive at every real place in
$\mathfrak m$. For every $x \in K_{\mathfrak m}$, sending the class of $x$ through the map
$K_{\mathfrak m}/K_{\mathfrak m,1} \to \mathrm{Cl}_{\mathfrak m}$ that takes the class of $y$ to
the ray class of $y\mathcal O_K$, and then through the projection $\mathrm{Cl}_{\mathfrak m} \to
\mathrm{Cl}(\mathcal O_K)$, gives $[x\mathcal O_K]$, the value of the coprime ideal-class map at
$x\mathcal O_K \in I_{\mathfrak m}$.

Formalized by `NumberField.Modulus.rayClassToClassGroup_rayQuotientToRayClassGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group-ray-quotient-to).

## Projecting the image of a residue-sign value to the class group

Let $K$ be a number field,
$\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$, $I_{\mathfrak m}$ the group of
nonzero fractional ideals of $\mathcal O_K$ coprime to $\mathfrak m_0$, $\mathrm{Cl}_{\mathfrak m}$
the ray class group, and $K_{\mathfrak m}$ the group of $x \in K^\times$ with
$x\mathcal O_K \in I_{\mathfrak m}$. Let $T_{\mathfrak m}$ be the product of one group of order $2$
for each real place in $\mathfrak m$ with $(\mathcal O_K/\mathfrak m_0)^\times$, let
$\rho : K_{\mathfrak m} \to T_{\mathfrak m}$ be the residue-sign map, and let
$T_{\mathfrak m} \to \mathrm{Cl}_{\mathfrak m}$ be the residue-sign-to-ray-class map. For every
$x \in K_{\mathfrak m}$, sending $\rho(x)$ through this map and then through the projection
$\mathrm{Cl}_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K)$ gives $[x\mathcal O_K]$, the value of
the coprime ideal-class map at $x\mathcal O_K \in I_{\mathfrak m}$.

Formalized by `NumberField.Modulus.rayClassToClassGroup_residueSignToRayClassGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group-residue-sign-to).

## Kernel of the projection from the ray class group to the class group

Let $K$ be a number
field, $\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$, $I_{\mathfrak m}$ the group
of nonzero fractional ideals of $\mathcal O_K$ coprime to $\mathfrak m_0$,
$\mathrm{Cl}_{\mathfrak m}$ the ray class group, $K_{\mathfrak m}$ the group of $x \in K^\times$
with $x\mathcal O_K \in I_{\mathfrak m}$, and $K_{\mathfrak m,1} \subseteq K_{\mathfrak m}$ the
subgroup of those $x$ with $x \equiv 1 \pmod{\mathfrak m_0}$ that are positive at every real place
in $\mathfrak m$. The kernel of the projection $\mathrm{Cl}_{\mathfrak m} \to
\mathrm{Cl}(\mathcal O_K)$ equals the image of the homomorphism
$K_{\mathfrak m}/K_{\mathfrak m,1} \to \mathrm{Cl}_{\mathfrak m}$ that sends the class of $x$ to
the ray class of $x\mathcal O_K$.

## Sources

- ATLAS `exactSeq_exact_at_ray_class`.

Formalized by `NumberField.Modulus.rayClassToClassGroup_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group-ker).

## Exactness at the ray class group

Let $K$ be a number field, $\mathfrak m$ a modulus of
$K$ with finite part $\mathfrak m_0$, $I_{\mathfrak m}$ the group of nonzero fractional ideals of
$\mathcal O_K$ coprime to $\mathfrak m_0$, $\mathrm{Cl}_{\mathfrak m}$ the ray class group,
$K_{\mathfrak m}$ the group of $x \in K^\times$ with $x\mathcal O_K \in I_{\mathfrak m}$, and
$K_{\mathfrak m,1} \subseteq K_{\mathfrak m}$ the subgroup of those $x$ with
$x \equiv 1 \pmod{\mathfrak m_0}$ that are positive at every real place in $\mathfrak m$. The
sequence $K_{\mathfrak m}/K_{\mathfrak m,1} \to \mathrm{Cl}_{\mathfrak m} \to
\mathrm{Cl}(\mathcal O_K)$ is exact at $\mathrm{Cl}_{\mathfrak m}$, where the first map sends the
class of $x$ to the ray class of $x\mathcal O_K$ and the second is the projection: a ray class
maps to the identity of $\mathrm{Cl}(\mathcal O_K)$ if and only if it lies in the image of the
first map.

## Sources

- ATLAS `exactSeq_exact_at_ray_class`.

Formalized by `NumberField.Modulus.rayQuotientToRayClassGroup_mulExact_rayClassToClassGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-quotient-to-ray-class-group-mul-exac).

## Exactness at the ray class group, residue-sign form

Let $\mathfrak m$ be a modulus of a
number field $K$, with finite part the nonzero ideal $\mathfrak m_0$ of $\mathcal O_K$ and infinite
part the finite set $\mathfrak m_\infty$ of real places of $K$. Let $\varphi$ be the homomorphism
from the residue-sign group $\{\pm 1\}^{\mathfrak m_\infty} \times
(\mathcal O_K/\mathfrak m_0)^\times$ to the ray class group $\mathrm{Cl}_{\mathfrak m}(K)$ that
sends the signs at the places in $\mathfrak m_\infty$ and the residue class modulo $\mathfrak m_0$
of an element $x \in K^\times$ coprime to $\mathfrak m_0$ to the ray class of the principal ideal
$(x)$, and let $\pi \colon \mathrm{Cl}_{\mathfrak m}(K) \to \mathrm{Cl}(K)$ be the projection to
the ideal class group. Then a ray class $c$ satisfies $\pi(c) = 1$ if and only if $c$ lies in the
image of $\varphi$; that is, the sequence is exact at $\mathrm{Cl}_{\mathfrak m}(K)$.

Formalized by `NumberField.Modulus.residueSignToRayClassGroup_mulExact_rayClassToClassGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/RayClassToClassGroup.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#residue-sign-to-ray-class-group-mul-exac).

## Nonzero integral ideals coprime to the modulus are coprime fractional ideals

Let $K$
be a number field with ring of integers $\mathcal O_K$, let $\mathfrak m$ be a modulus of $K$
with finite part $\mathfrak m_0$, and let $I$ be a nonzero ideal of $\mathcal O_K$ with
$I + \mathfrak m_0 = \mathcal O_K$. Then $I$, viewed as an invertible fractional ideal of $K$,
belongs to the group of fractional ideals coprime to $\mathfrak m_0$: its exponent at every prime
dividing $\mathfrak m_0$ is $0$.

## Sources

- E5 `mk0` membership/count bridge for ATLAS lines 1431--1465.

Formalized by `NumberField.Modulus.fractionalIdealMk0_mem_coprimeFractionalIdeals`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#fractional-ideal-mk0-mem-coprime-fractio).

## Every ideal class contains a fractional ideal coprime to the modulus

Let $K$ be a
number field and $\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$. The homomorphism
from the group of fractional ideals of $K$ coprime to $\mathfrak m_0$ (those whose exponent at
every prime dividing $\mathfrak m_0$ is $0$) to the class group of $\mathcal O_K$, sending each
such fractional ideal to its ideal class, is surjective.

## Sources

- ATLAS lines 1466--1476; Lemma 21.7 at lines 958--1010 is reused via the stronger `ClassGroup.exists_mk0_eq_and_isCoprime`.

Formalized by `NumberField.Modulus.coprimeIdealClassMap_surjective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#coprime-ideal-class-map-surjective).

## The ray class group surjects onto the class group

Let $K$ be a number field and
$\mathfrak m$ a modulus of $K$. The homomorphism from the ray class group of $\mathfrak m$ to the
class group of $\mathcal O_K$, sending the ray class of a fractional ideal coprime to the finite
part of $\mathfrak m$ to its ideal class, is surjective.

## Sources

- ATLAS lines 1478--1480.

Formalized by `NumberField.Modulus.rayClassToClassGroup_surjective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-to-class-group-surjective).

## The ray class exact sequence

Let $K$ be a number field with ring of
integers $\mathcal O_K$, and let $\mathfrak m$ be a modulus of $K$ with finite part
$\mathfrak m_0$ (a nonzero ideal of $\mathcal O_K$) and infinite part $\mathfrak m_\infty$ (a
finite set of real places). Let $K_{\mathfrak m}$ be the group of $x \in K^\times$ whose
principal fractional ideal is coprime to $\mathfrak m_0$, and let
$K_{\mathfrak m,1} \subseteq K_{\mathfrak m}$ be the subgroup of those $x$ that are positive at
every real place in $\mathfrak m_\infty$ and satisfy, for every prime
$\mathfrak p \mid \mathfrak m_0$, either $x = 1$ or
$v_{\mathfrak p}(x - 1) \ge v_{\mathfrak p}(\mathfrak m_0)$, where $v_{\mathfrak p}$ of an
element of $K^\times$ or of a nonzero ideal is the exponent of $\mathfrak p$ in its fractional
ideal. Let $U_{\mathfrak m,1}$ be the group
of units of $\mathcal O_K$ lying in $K_{\mathfrak m,1}$, let $\mathrm{Cl}_{\mathfrak m}$ be the
ray class group (fractional ideals coprime to $\mathfrak m_0$ modulo the subgroup generated by
the principal ideals $(x)$ with $x \in K_{\mathfrak m,1}$), and let $\mathrm{Cl}(\mathcal O_K)$
be the class group. Then the sequence

$$
1 \to U_{\mathfrak m,1} \to \mathcal O_K^\times \to K_{\mathfrak m}/K_{\mathfrak m,1}
\to \mathrm{Cl}_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K) \to 1
$$

is exact, where the maps are the inclusion, the map sending a unit to its class modulo
$K_{\mathfrak m,1}$, the map sending the class of $x$ to the ray class of $(x)$, and the map
sending the ray class of a fractional ideal to its ideal class.

## Sources

- ATLAS lines 1012--1480; this theorem aggregates the separately source-backed map, exactness and surjectivity declarations and is not a direct declaration port.

Formalized by `NumberField.Modulus.rayClass_six_term_exact`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-six-term-exact).

## The ray class exact sequence, sign and residue form

Let $K$ be a number field with ring of
integers $\mathcal O_K$, and let $\mathfrak m$ be a modulus of $K$ with finite part
$\mathfrak m_0$ (a nonzero ideal of $\mathcal O_K$) and infinite part $\mathfrak m_\infty$ (a
finite set of real places). Let $K_{\mathfrak m}$ be the group of $x \in K^\times$ whose
principal fractional ideal is coprime to $\mathfrak m_0$, and let
$K_{\mathfrak m,1} \subseteq K_{\mathfrak m}$ be the subgroup of those $x$ that are positive at
every real place in $\mathfrak m_\infty$ and satisfy, for every prime
$\mathfrak p \mid \mathfrak m_0$, either $x = 1$ or
$v_{\mathfrak p}(x - 1) \ge v_{\mathfrak p}(\mathfrak m_0)$, where $v_{\mathfrak p}$ of an
element of $K^\times$ or of a nonzero ideal is the exponent of $\mathfrak p$ in its fractional
ideal. Let $U_{\mathfrak m,1}$ be the group
of units of $\mathcal O_K$ lying in $K_{\mathfrak m,1}$, let $\mathrm{Cl}_{\mathfrak m}$ be the
ray class group (fractional ideals coprime to $\mathfrak m_0$ modulo the subgroup generated by
the principal ideals $(x)$ with $x \in K_{\mathfrak m,1}$), and let $\mathrm{Cl}(\mathcal O_K)$
be the class group. For
$x \in K_{\mathfrak m}$, let $\rho(x) \in \{\pm 1\}^{\mathfrak m_\infty} \times
(\mathcal O_K/\mathfrak m_0)^\times$ record the sign of $x$ at each real place in
$\mathfrak m_\infty$ and the residue class of $x$ modulo $\mathfrak m_0$ (the class of $a b^{-1}$
when $x = a/b$ with $a, b \in \mathcal O_K$ prime to $\mathfrak m_0$); $\rho$ is surjective with
kernel $K_{\mathfrak m,1}$. Then the sequence

$$
1 \to U_{\mathfrak m,1} \to \mathcal O_K^\times \to
\{\pm 1\}^{\mathfrak m_\infty} \times (\mathcal O_K/\mathfrak m_0)^\times
\to \mathrm{Cl}_{\mathfrak m} \to \mathrm{Cl}(\mathcal O_K) \to 1
$$

is exact, where the maps are the inclusion, the restriction of $\rho$ to units, the map sending
$\rho(x)$ to the ray class of $(x)$, and the map sending the ray class of a fractional ideal to
its ideal class.

## Sources

- ATLAS lines 1012--1480, aggregated from the separately source-backed map, exactness and surjectivity declarations (not a direct declaration port), and transported through the quotient equivalence backed by lines 2607--2647.

Formalized by `NumberField.Modulus.rayClass_residueSign_six_term_exact`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ExactSequence.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html#ray-class-residue-sign-six-term-exact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ray class groups](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-groups)
