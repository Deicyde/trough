---
declaration: section
origin: cited
lean: BinaryQuadraticForm.ofCoefficients, BinaryQuadraticForm.ofCoefficients_apply, BinaryQuadraticForm.ofCoefficients_posDef, BinaryQuadraticForm.imaginaryRoot, BinaryQuadraticForm.imaginaryRoot_sq, BinaryQuadraticForm.imaginaryRoot_isIntegral, BinaryQuadraticForm.imaginaryRoot_not_mem_bot, BinaryQuadraticForm.imaginaryQuadraticField
statement: formalized
proof: formalized
---

# Binary quadratic forms

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html).

## Real quadratic form of an integer coefficient triple

For integers $a, b, c$, this is the
quadratic form on the real vector space $\mathbb{R}^2$ given by
$(x, y) \mapsto a x^2 + b x y + c y^2$.

Formalized by `BinaryQuadraticForm.ofCoefficients`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#of-coefficients).

## Evaluation of the real quadratic form of a coefficient triple

For integers $a, b, c$
and real numbers $x, y$, the real quadratic form of the triple $(a, b, c)$ takes the value
$a x^2 + b x y + c y^2$ at the point $(x, y)$.

Formalized by `BinaryQuadraticForm.ofCoefficients_apply`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#of-coefficients-apply).

## Positive definiteness for negative discriminant

Let $D$ be a positive integer and let
$a, b, c$ be integers with $a > 0$ and $b^2 - 4ac = -D$. Then the real quadratic form
$(x, y) \mapsto a x^2 + b x y + c y^2$ on $\mathbb{R}^2$ is positive definite.

Formalized by `BinaryQuadraticForm.ofCoefficients_posDef`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#of-coefficients-pos-def).

## The imaginary square root of $-D$

For a natural number $D$, the imaginary root of $D$ is
the complex number $i\sqrt{D}$, where $\sqrt{D}$ is the nonnegative real square root; it is the
square root of $-D$ with nonnegative imaginary part.

Formalized by `BinaryQuadraticForm.imaginaryRoot`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#imaginary-root).

## The imaginary root squares to $-D$

For every natural number $D$, the complex number
$i\sqrt{D}$ satisfies $(i\sqrt{D})^2 = -D$.

Formalized by `BinaryQuadraticForm.imaginaryRoot_sq`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#imaginary-root-sq).

## The imaginary root is integral over $\mathbb{Q}$

For every natural number $D$, the
complex number $i\sqrt{D}$ is integral over $\mathbb{Q}$.

Formalized by `BinaryQuadraticForm.imaginaryRoot_isIntegral`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#imaginary-root-is-integral).

## The imaginary root is not rational

For every positive integer $D$, the complex number
$i\sqrt{D}$ does not lie in the subfield $\mathbb{Q}$ of $\mathbb{C}$.

Formalized by `BinaryQuadraticForm.imaginaryRoot_not_mem_bot`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#imaginary-root-not-mem-bot).

## The imaginary quadratic field $\mathbb{Q}(\sqrt{-D})$

For a natural number $D$, this is
the subfield $\mathbb{Q}(i\sqrt{D})$ of $\mathbb{C}$ generated over $\mathbb{Q}$ by the imaginary
root $i\sqrt{D}$.

When $D = 0$ this field is $\mathbb{Q}$ itself.

Formalized by `BinaryQuadraticForm.imaginaryQuadraticField`, an abbreviation declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#imaginary-quadratic-field).

## $\mathbb{Q}(\sqrt{-D})$ is a quadratic extension

For every positive integer $D$, the
subfield $\mathbb{Q}(i\sqrt{D})$ of $\mathbb{C}$ has degree $2$ over $\mathbb{Q}$.

Formalized by `BinaryQuadraticForm.imaginaryQuadraticField_finrank`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#imaginary-quadratic-field-finrank).

## The form generator is an algebraic integer

Let $D$ be a natural number and let $a, b, c$
be integers with $b^2 - 4ac = -D$. Then the element $(b + i\sqrt{D})/2$ of the field
$\mathbb{Q}(i\sqrt{D}) \subseteq \mathbb{C}$ is integral over $\mathbb{Z}$.

Formalized by `BinaryQuadraticForm.formGenerator_isIntegral`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#form-generator-is-integral).

## Ideal of a binary quadratic form

Let $D$ be a natural number, let
$K = \mathbb{Q}(i\sqrt{D}) \subseteq \mathbb{C}$ and let $\mathcal{O}_K$ be its ring of
integers. For integers $a, b, c$, the ideal of the triple $(a, b, c)$ is the fractional ideal
of $\mathcal{O}_K$ in $K$ generated by $a$ and $(b + i\sqrt{D})/2$.

When $b^2 - 4ac = -D$, the second generator is an algebraic integer.

Formalized by `BinaryQuadraticForm.formIdeal`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#form-ideal).

## The ideal of a form is nonzero

Let $D$ be a natural number and let $a, b, c$ be integers
with $a \ne 0$. Then the fractional ideal of the ring of integers of
$\mathbb{Q}(i\sqrt{D}) \subseteq \mathbb{C}$ generated by $a$ and $(b + i\sqrt{D})/2$ is nonzero.

Formalized by `BinaryQuadraticForm.formIdeal_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#form-ideal-ne-zero).

## Ideal class of a binary quadratic form

Let $D$ be a natural number, let
$K = \mathbb{Q}(i\sqrt{D}) \subseteq \mathbb{C}$ and let $\mathcal{O}_K$ be its ring of
integers. For integers $a, b, c$ with $a \ne 0$, the ideal class of the triple $(a, b, c)$ is
the class, in the class group of $\mathcal{O}_K$, of the nonzero fractional ideal of
$\mathcal{O}_K$ in $K$ generated by $a$ and $(b + i\sqrt{D})/2$.

Formalized by `BinaryQuadraticForm.classOfForm`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/IdealClass.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#class-of-form).

## Gauss-reduced binary quadratic forms

The integral binary quadratic form
$a x^2 + b x y + c y^2$ is Gauss reduced when $a > 0$, its discriminant $b^2 - 4ac$ is negative,
$|b| \le a \le c$, and $b \ge 0$ whenever $|b| = a$ or $a = c$.

For example, $x^2 - x y + y^2$ is positive definite and satisfies $|b| \le a \le c$, but it is not
reduced, because $|b| = a$ and $b < 0$.

## Sources

- Mortenson, *A Kronecker-type identity*, Bull. LMS 49 (2017), arXiv:1702.01627v2, Section 2, line 259.

Formalized by `BinaryQuadraticForm.IsGaussReduced`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/Reduced.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/Reduced.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html#is-gauss-reduced).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary quadratic forms](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/binary-quadratic-forms)
