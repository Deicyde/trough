---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.H, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.P, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.H.hessian, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.Ŀ, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.IsMConvex, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.M, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.IsStable, MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.S
statement: formalized
---

# Lorentzian polynomials

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html).

## Homogeneous polynomials of degree $d$

For natural numbers $n$ and $d$, $H^d_n$ denotes
the space of homogeneous polynomials of degree $d$ in $\mathbb{R}[w_1, \dots, w_n]$, including the
zero polynomial.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.H`, a definition declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#h).

## Homogeneous polynomials with positive coefficients

$P^d_n$ is the set of homogeneous
polynomials $f$ of degree $d$ in $\mathbb{R}[w_1, \dots, w_n]$ such that the coefficient in $f$ of
every monomial of degree $d$ is strictly positive.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.P`, an abbreviation declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#p).

## Hessian of a quadratic form

For a homogeneous polynomial $f$ of degree $2$ in
$\mathbb{R}[w_1, \dots, w_n]$, its Hessian is the real $n \times n$ matrix $\mathcal{H}_f$ of second
partial derivatives of $f$: the diagonal entry $(i, i)$ is twice the coefficient of $w_i^2$ in $f$,
and for $i \ne j$ the entry $(i, j)$ is the coefficient of $w_i w_j$ in $f$.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.H.hessian`, a definition declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#hessian).

## Strictly Lorentzian polynomials

For natural numbers $n$ and $d$, the set $\mathring{L}^d_n$
of strictly Lorentzian polynomials of degree $d$ in $\mathbb{R}[w_1, \dots, w_n]$ is defined by
recursion on $d$. Let $P^d_n$ be the set of homogeneous polynomials of degree $d$ in which every
monomial of degree $d$ has a strictly positive coefficient, and let $\partial_i$ be the partial
derivative with respect to $w_i$. Then $\mathring{L}^0_n = P^0_n$ and $\mathring{L}^1_n = P^1_n$;
$\mathring{L}^2_n$ is the set of $f \in P^2_n$ whose Hessian matrix
$(\partial_i \partial_j f)_{i,j}$ is invertible and has exactly one positive eigenvalue, counted
with multiplicity; and for $d \ge 3$, $\mathring{L}^d_n$ is the set of $f \in P^d_n$ such that
$\partial_i f \in \mathring{L}^{d-1}_n$ for every $i$.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.Ŀ`, a definition declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#untitled).

## M-convex sets

A subset $J \subseteq \mathbb{N}^n$ is M-convex if for all
$\alpha, \beta \in J$ and every index $i$ with $\alpha_i > \beta_i$ there is an index $j$ with
$\alpha_j < \beta_j$ and $\alpha - e_i + e_j \in J$, where $e_1, \dots, e_n$ are the standard unit
vectors of $\mathbb{N}^n$.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.IsMConvex`, a definition declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#is-mconvex).

## Homogeneous polynomials with M-convex support

$M^d_n$ is the set of homogeneous
polynomials $f$ of degree $d$ in $\mathbb{R}[w_1, \dots, w_n]$ whose coefficients are all
nonnegative and whose support, the set of exponent vectors $\alpha \in \mathbb{N}^n$ of the
monomials with nonzero coefficient in $f$, is M-convex.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.M`, an abbreviation declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#m).

## Stable polynomials

A polynomial $f \in \mathbb{R}[w_1, \dots, w_n]$ is stable if either
$f$ is the zero polynomial or $f(z_1, \dots, z_n) \ne 0$ for all $z_1, \dots, z_n$ in the open upper
half plane $\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im} z > 0\}$.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.IsStable`, a definition declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#is-stable).

## Stable homogeneous polynomials with nonnegative coefficients

$S^d_n$ is the set of
homogeneous polynomials $f$ of degree $d$ in $\mathbb{R}[w_1, \dots, w_n]$ whose coefficients are
all nonnegative and that are stable: either $f$ is the zero polynomial or $f$ has no zero in
$\mathbb{H}^n$, where $\mathbb{H}$ is the open upper half plane in $\mathbb{C}$.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.S`, an abbreviation declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#s).

## The set of Lorentzian polynomials

For natural numbers $n$ and $d$, the set $L^d_n$ of
Lorentzian polynomials is a set of homogeneous polynomials of degree $d$ in
$\mathbb{R}[w_1, \dots, w_n]$, defined by recursion on $d$. For $d \le 2$, $L^d_n = S^d_n$, the set
of homogeneous stable polynomials of degree $d$ with nonnegative coefficients. For $d \ge 3$,
$L^d_n$ is the set of $f \in M^d_n$ (the homogeneous polynomials of degree $d$ with nonnegative
coefficients and M-convex support) such that $\partial_i f \in L^{d-1}_n$ for every
$i \in \{1, \dots, n\}$, where $\partial_i$ is the partial derivative with respect to $w_i$.

Formalized by `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.L`, a definition declared in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#l).

## Lorentzian polynomials as the closure of strictly Lorentzian polynomials

For all natural
numbers $n \ge 1$ and $d$, the closure of the set $\mathring{L}^d_n$ of strictly Lorentzian
polynomials of degree $d$ in $n$ variables, taken in the space $H^d_n$ of homogeneous polynomials
of degree $d$ in $\mathbb{R}[w_1, \dots, w_n]$ with the Euclidean topology on coefficients, is the
set $L^d_n$ of Lorentzian polynomials of degree $d$ in $n$ variables.

The paper (Theorem 2.25) allows $n = 0$, but the statement fails for $n = 0$ and $d = 2$: the
$0 \times 0$ Hessian of a polynomial cannot have a positive eigenvalue, so $\mathring{L}^2_0$ is
empty, while $L^2_0 = S^2_0$ contains the zero polynomial, which is homogeneous of degree $2$.

## Sources

- P. Brändén and J. Huh, `Lorentzian polynomials`, Annals of Math, 192 (3) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_lorentzian_polynomials` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.LorentzianPolynomialsWanted.LorentzianPolynomials.theorem_2_25` is written with `theorem_wanted` in [WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/LorentzianPolynomialsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html#theorem-2-25).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lorentzian polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/matroid-theory/lorentzian-polynomials)
