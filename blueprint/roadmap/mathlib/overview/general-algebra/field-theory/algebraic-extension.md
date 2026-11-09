# Algebraic extension

An **algebraic extension** is a [field](field.md) extension $L/K$ in which every element of $L$ is a root of some nonzero [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) with coefficients in $K$. Algebraic extensions are the setting of most of classical field theory: finite extensions, splitting fields and Galois extensions are all algebraic, and every algebraic extension of a field embeds into its [algebraic closure](existence-of-algebraic-closure-of-a-field.md), which is thus the largest algebraic extension up to isomorphism. The opposite behaviour, an element satisfying no nonzero polynomial relation over $K$, is called transcendence.

## Definition

Let $K$ be a field and $L$ an extension field of $K$. An element $\alpha \in L$ is [algebraic over $K$](../../../undergraduate/ring-theory/field-theory/algebraic-elements.md) if it is a [root of a nonzero polynomial with coefficients in $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#IsAlgebraic), and [transcendental](../../../undergraduate/ring-theory/field-theory/transcendental-elements.md) otherwise. The extension $L/K$ is algebraic when [every element of $L$ is algebraic over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#Algebra.IsAlgebraic).

Since $K$ is a field, a nonzero polynomial can be divided by its leading coefficient, so an element is algebraic exactly when it is a root of a monic polynomial over $K$, that is, when it is integral over $K$. Hence [an extension of a field is algebraic if and only if it is integral](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Integral.html#Algebra.isAlgebraic_iff_isIntegral). For an algebraic element $\alpha$, the monic polynomial of least degree with root $\alpha$ is its [minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md).

## Examples

- The extension $\mathbb{Q}(\sqrt 2)/\mathbb{Q}$ is algebraic: it has dimension $2$ over $\mathbb{Q}$, and finite extensions are algebraic (see below). Directly, $a + b\sqrt 2$ is a root of $x^2 - 2ax + a^2 - 2b^2$.
- The extension $\mathbb{C}/\mathbb{R}$ is algebraic, since $a + bi$ is a root of the real polynomial $x^2 - 2ax + a^2 + b^2$.
- The complex numbers that are algebraic over $\mathbb{Q}$ form a field, and it is algebraic over $\mathbb{Q}$ of infinite degree: it contains $\sqrt[n]{2}$, whose minimal polynomial $x^n - 2$ has degree $n$, for every $n \ge 1$. So an algebraic extension need not be finite.
- The [real numbers](../numbers/real-number.md) are not algebraic over the [rational numbers](../numbers/rational-number.md). An algebraic extension of a countable field is countable (see the cardinality bound below), while $\mathbb{R}$ is [uncountable](../../../hundred-theorems/part-01/the-non-denumerability-of-the-continuum.md).
- The field $K(x)$ of rational functions in one variable is not algebraic over $K$: no nonzero polynomial over $K$ vanishes at $x$.

## Properties

- **Finite extensions are algebraic.** If $L$ is finite-dimensional over $K$, then [$L/K$ is algebraic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Integral.html#Algebra.IsAlgebraic.of_finite). If $[L : K] = n$ and $\alpha \in L$, the $n + 1$ elements $1, \alpha, \dots, \alpha^n$ are linearly dependent over $K$, and a dependence relation is a nonzero polynomial vanishing at $\alpha$. The examples above show that the converse fails.
- **Generated extensions.** For a subset $S$ of $L$, the field $K(S)$ is [algebraic over $K$ if and only if every element of $S$ is algebraic over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AlgebraicClosure.html#IntermediateField.isAlgebraic_adjoin_iff_isAlgebraic). In particular $K(\alpha)/K$ is algebraic whenever $\alpha$ is, and it is then [finite-dimensional](../../linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md) of degree equal to the degree of the minimal polynomial of $\alpha$.
- **Towers.** Let $K \subseteq M \subseteq L$ be fields. If $L/K$ is algebraic, then [$L/M$ is algebraic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Basic.html#Algebra.IsAlgebraic.tower_top) and [$M/K$ is algebraic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Basic.html#Algebra.IsAlgebraic.tower_bot). Conversely, if $L/M$ and $M/K$ are both algebraic, then [$L/K$ is algebraic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Integral.html#Algebra.IsAlgebraic.trans): an element of $L$ satisfies a polynomial with finitely many coefficients in $M$, these generate a finite extension of $K$, and adjoining the element gives a larger finite extension of $K$, which is algebraic.
- **Relative algebraic closure.** For any extension $L/K$, the elements of $L$ algebraic over $K$ form an intermediate field, the relative algebraic closure of $K$ in $L$: [an element of $L$ lies in it exactly when it is algebraic over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AlgebraicClosure.html#mem_algebraicClosure_iff), and this field [is algebraic over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AlgebraicClosure.html#algebraicClosure.isAlgebraic). It is the largest intermediate field algebraic over $K$.
- **Composita.** The field generated by any family of intermediate fields of $L/K$, each algebraic over $K$, [is again algebraic over $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IntermediateField/Adjoin/Basic.html#IntermediateField.isAlgebraic_iSup).
- **Cardinality.** An algebraic extension $L$ of $K$ has [at most $\max(|K|, \aleph_0)$ elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Cardinality.html#Algebra.IsAlgebraic.cardinalMk_le_max), because each element is one of the finitely many roots of one of the polynomials over $K$.
- **Endomorphisms.** If $L/K$ is algebraic, then [every homomorphism of $K$-algebras from $L$ to itself is bijective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Basic.html#Algebra.IsAlgebraic.algHom_bijective). Such a map is injective, like every homomorphism of fields, and it sends each root in $L$ of a nonzero polynomial over $K$ to a root of the same polynomial; so it permutes the finite set of roots of the polynomial of each element, and in particular hits that element.

## Related concepts

A field $k$ is [algebraically closed](algebraically-closed-field.md) exactly when it has no proper algebraic extensions: if $k$ is algebraically closed and $K/k$ is any extension, [the only intermediate field algebraic over $k$ is $k$ itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IntermediateField.eq_bot_of_isAlgClosed_of_isAlgebraic). An algebraic closure of $K$ is an algebraic extension that is algebraically closed, and [Mathlib's algebraic closure of a field is algebraic over it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/AlgebraicClosure.html#AlgebraicClosure.isAlgebraic). The [splitting field](splitting-field.md) of a polynomial is a finite, hence algebraic, extension. Galois theory concerns algebraic extensions that are also normal and separable.

## In Mathlib

Mathlib defines algebraicity for an arbitrary algebra $A$ over a commutative ring $R$, not only for field extensions: $A$ is algebraic over $R$ when each of its elements is a root of a nonzero polynomial with coefficients in $R$. It is a property attached to the pair, recorded as a type class so that it can be found automatically, and a field extension $L/K$ is treated as $L$ viewed as an algebra over $K$. Over a ring that is not a field, algebraic and integral differ, and some results need extra hypotheses: the transitivity theorem asks the middle ring to have no zero divisors, and the cardinality bound and the result on endomorphisms are stated for an integral domain acting without torsion on a larger integral domain (for endomorphisms, a field), which covers every field extension. One consequence of the definition is that no algebra over the zero ring is algebraic, since the zero ring has no nonzero polynomials.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Field](field.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)
- [Algebraic elements](../../../undergraduate/ring-theory/field-theory/algebraic-elements.md)

## Sources

- [Mathlib documentation: `Algebra.IsAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Algebraic/Defs.html#Algebra.IsAlgebraic)
- [Source of `Algebra.IsAlgebraic` in Mathlib/RingTheory/Algebraic/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Algebraic/Defs.lean#L66)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L130)
- [Mathlib undergraduate list: Ring Theory › Field Theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L184)
