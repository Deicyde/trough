---
declaration: section
origin: cited
lean: MvPolynomial.RegularFunction, MvPolynomial.RegularFunction.Jacobian, MvPolynomial.RegularFunction.comp, MvPolynomial.RegularFunction.id_comp, MvPolynomial.RegularFunction.comp_id, MvPolynomial.RegularFunction.comp_assoc, MvPolynomial.RegularFunction.aeval, MvPolynomial.RegularFunction.comp_aeval
statement: formalized
proof: formalized
---

# Polynomial maps between affine spaces

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html).

## Mv Polynomial

## Regular functions

For a commutative semiring $k$ and index types $\sigma$ and $\tau$, a
regular function from $k^\sigma$ to $k^\tau$ is a family $F = (F_t)_{t \in \tau}$ of polynomials
in the variables $X_s$, $s \in \sigma$, with coefficients in $k$.

The components are formal polynomials, not functions on $k^\sigma$.

Formalized by `MvPolynomial.RegularFunction`, an abbreviation declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#regular-function).

## Jacobian matrix of a regular function

The Jacobian of a regular function
$F = (F_j)_{j \in \tau}$ from $k^\sigma$ to $k^\tau$ is the $\tau \times \sigma$ matrix, with
entries in the polynomial ring $k[X_i : i \in \sigma]$, whose entry in row $j$ and column $i$ is
the formal partial derivative $\partial F_j / \partial X_i$.

Rows are indexed by the components and columns by the variables, following the usual matrix
convention, so the Jacobian multiplies column vectors indexed by $\sigma$.

Formalized by `MvPolynomial.RegularFunction.Jacobian`, a definition declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#jacobian).

## Composition of regular functions

For regular functions $G$ from $k^\tau$ to $k^\iota$
and $F$ from $k^\sigma$ to $k^\tau$, the composition $G \circ F$ is the regular function from
$k^\sigma$ to $k^\iota$ whose $i$-th component, for $i \in \iota$, is the polynomial obtained
from $G_i$ by substituting $F_t$ for the variable $X_t$ for every $t \in \tau$.

Formalized by `MvPolynomial.RegularFunction.comp`, a definition declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#comp).

## The identity is a left unit for composition

For every regular function $F$ from
$k^\sigma$ to $k^\tau$, composing the identity regular function on $k^\tau$, whose components
are the variables $X_t$ for $t \in \tau$, with $F$ gives $F$, that is,
$\mathrm{id} \circ F = F$.

Formalized by `MvPolynomial.RegularFunction.id_comp`, a lemma declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#id-comp).

## The identity is a right unit for composition

For every regular function $F$ from
$k^\sigma$ to $k^\tau$, composing $F$ with the identity regular function on $k^\sigma$, whose
components are the variables $X_s$ for $s \in \sigma$, gives $F$, that is,
$F \circ \mathrm{id} = F$.

Formalized by `MvPolynomial.RegularFunction.comp_id`, a lemma declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#comp-id).

## Associativity of composition of regular functions

For regular functions $H$ from
$k^\iota$ to $k^\kappa$, $G$ from $k^\tau$ to $k^\iota$ and $F$ from $k^\sigma$ to $k^\tau$,
we have $(H \circ G) \circ F = H \circ (G \circ F)$.

Formalized by `MvPolynomial.RegularFunction.comp_assoc`, a lemma declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#comp-assoc).

## Evaluation of a regular function at a point

Let $k$ be a commutative semiring and let
$S$ be a commutative $k$-algebra. For a regular function $F$ from $k^\sigma$ to $k^\tau$ and a
point $a \in S^\sigma$, the evaluation of $F$ at $a$ is the point $F(a) \in S^\tau$ whose $t$-th
coordinate, for $t \in \tau$, is the value of the polynomial $F_t$ at $a$, obtained by
substituting $a_s$ for $X_s$ for every $s \in \sigma$.

Formalized by `MvPolynomial.RegularFunction.aeval`, a definition declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#aeval).

## Evaluation respects composition

Let $k$ be a commutative semiring and let $S$ be a
commutative $k$-algebra. For regular functions $G$ from $k^\tau$ to $k^\iota$ and $F$ from
$k^\sigma$ to $k^\tau$ and every point $a \in S^\sigma$, write $F(a) \in S^\tau$ for the
evaluation of $F$ at $a$. Then evaluating the composition $G \circ F$ at $a$ gives $G(F(a))$,
the evaluation of $G$ at the point $F(a)$.

Formalized by `MvPolynomial.RegularFunction.comp_aeval`, a lemma declared in [MathlibExt/Algebra/MvPolynomial/RegularFunction.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/RegularFunction.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html#comp-aeval).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial maps between affine spaces](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/polynomial-maps-between-affine-spaces)
