---
declaration: section
origin: cited
lean: MvPolynomial.mixedDifferential, MvPolynomial.mixedDifferential_nil, MvPolynomial.mixedDifferential_cons, MvPolynomial.mixedDifferential_eq_of_perm, MvPolynomial.mixedDifferential_append, MvPolynomial.pderiv_mixedDifferential
statement: formalized
proof: formalized
---

# Mixed partial derivatives of polynomials

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html).

## Mixed differential operator

Let $R$ be a commutative ring, let $\sigma$ be an index
type, and write $\partial_s$ for the partial derivative with respect to $x_s$ on the polynomial
ring $R[x_s : s \in \sigma]$. For a finite list $(i_1, \dots, i_k)$ of indices in $\sigma$
(repetitions allowed) and a polynomial $p \in R[x_s : s \in \sigma]$, the mixed differential of
$p$ along the list is $(1 - \partial_{i_k}) \cdots (1 - \partial_{i_1})\, p$: the operator
$1 - \partial_{i_1}$ is applied first and $1 - \partial_{i_k}$ last. Along the empty list it is
$p$.

Formalized by `MvPolynomial.mixedDifferential`, a definition declared in [MathlibExt/Algebra/MvPolynomial/PDeriv.lean, line 18](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/PDeriv.lean#L18). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html#mixed-differential).

## Mixed differential along the empty list

Let $R$ be a commutative ring, let $\sigma$ be
an index type, and let $p \in R[x_s : s \in \sigma]$. The mixed differential of $p$ along the
empty list of indices is $p$ itself.

Formalized by `MvPolynomial.mixedDifferential_nil`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/PDeriv.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/PDeriv.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html#mixed-differential-nil).

## Mixed differential along a list with a given first index

Let $R$ be a commutative ring,
let $\sigma$ be an index type, let $i \in \sigma$, let $L$ be a finite list of indices in
$\sigma$, and let $p \in R[x_s : s \in \sigma]$. The mixed differential of $p$ along the list
that starts with $i$ and continues with $L$ equals the mixed differential along $L$ of
$p - \partial_i p$, where $\partial_i$ is the partial derivative with respect to $x_i$.

Formalized by `MvPolynomial.mixedDifferential_cons`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/PDeriv.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/PDeriv.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html#mixed-differential-cons).

## The mixed differential ignores the order of the indices

Let $R$ be a commutative ring,
let $\sigma$ be an index type, and let $p \in R[x_s : s \in \sigma]$. If two finite lists $L$ and
$L'$ of indices in $\sigma$ are permutations of each other, then the mixed differentials of $p$
along $L$ and along $L'$ are equal.

Formalized by `MvPolynomial.mixedDifferential_eq_of_perm`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/PDeriv.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/PDeriv.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html#mixed-differential-eq-of-perm).

## Mixed differential along a concatenated list

Let $R$ be a commutative ring, let $\sigma$
be an index type, let $p \in R[x_s : s \in \sigma]$, and let $L$ and $L'$ be finite lists of
indices in $\sigma$. The mixed differential of $p$ along the concatenation of $L$ followed by
$L'$ equals the mixed differential along $L'$ of the mixed differential of $p$ along $L$.

Formalized by `MvPolynomial.mixedDifferential_append`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/PDeriv.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/PDeriv.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html#mixed-differential-append).

## Partial derivatives commute with the mixed differential

Let $R$ be a commutative ring,
let $i \in \sigma$, let $L$ be a finite list of indices in $\sigma$, and let
$p \in R[x_s : s \in \sigma]$. Writing $\partial_i$ for the partial derivative with respect to
$x_i$, the partial derivative $\partial_i$ of the mixed differential of $p$ along $L$ equals the
mixed differential along $L$ of $\partial_i p$.

Formalized by `MvPolynomial.pderiv_mixedDifferential`, a theorem declared in [MathlibExt/Algebra/MvPolynomial/PDeriv.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/MvPolynomial/PDeriv.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html#pderiv-mixed-differential).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mixed partial derivatives of polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/polynomials/mixed-partial-derivatives-of-polynomials)
