---
declaration: section
origin: cited
lean: MetaMathlibExt.moebiusAlgebraMul, MetaMathlibExt.flagFVector, MetaMathlibExt.flagHVector, MetaMathlibExt.IsHyperplaneArrangement
statement: formalized
proof: formalized
---

# Möbius algebras and flag vectors

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors/index.html).

## The Möbius algebra

## Möbius algebra product

Let $L$ be a lattice with meet $\wedge$ and let $R$ be a
commutative semiring. The Möbius algebra $A(L, R)$ is the set of functions $f \colon L \to R$ with
$f(s) \neq 0$ for only finitely many $s \in L$. The product of $f, g \in A(L, R)$ is the function
$f \cdot g \in A(L, R)$ given by

$$(f \cdot g)(u) = \sum_{s \wedge t = u} f(s)\, g(t) \qquad (u \in L),$$

the sum taken over all pairs $(s, t) \in L \times L$ with $f(s) \neq 0$, $g(t) \neq 0$ and
$s \wedge t = u$. Equivalently, identifying each $s \in L$ with the function that is $1$ at $s$
and $0$ elsewhere, it is the bilinear extension of $s \cdot t = s \wedge t$.

Formalized by `MetaMathlibExt.moebiusAlgebraMul`, a definition declared in [MathlibExt/Combinatorics/Poset/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Poset/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors/index.html#moebius-algebra-mul).

## Flag $f$-vector

Let $P$ be a finite partially ordered set with a grade function
$\rho \colon P \to \mathbb{Z}_{\ge 0}$, that is, $\rho(s) < \rho(t)$ whenever $s < t$,
$\rho(t) = \rho(s) + 1$ whenever $t$ covers $s$ (that is, $s < t$ and no $u \in P$ satisfies
$s < u < t$), and $\rho(t) = 0$ whenever $t$ is minimal. For a finite set
$S \subseteq \mathbb{Z}_{\ge 0}$, let $P_S = \{t \in P : \rho(t) \in S\}$. The flag $f$-vector of
$P$ is the function $\alpha_P$ on finite sets $S \subseteq \mathbb{Z}_{\ge 0}$ such that
$\alpha_P(S)$ is the number of maximal chains in $P_S$, that is, of subsets $C \subseteq P_S$ any
two elements of which are comparable and such that every element of $P_S \setminus C$ is
incomparable with some element of $C$. In particular $\alpha_P(\emptyset) = 1$, the empty chain
being the only maximal chain in the empty poset.

Formalized by `MetaMathlibExt.flagFVector`, a definition declared in [MathlibExt/Combinatorics/Poset/Basic.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Poset/Basic.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors/index.html#flag-fvector).

## Flag $h$-vector

Let $P$ be a finite partially ordered set with a grade function
$\rho \colon P \to \mathbb{Z}_{\ge 0}$, that is, $\rho(s) < \rho(t)$ whenever $s < t$,
$\rho(t) = \rho(s) + 1$ whenever $t$ covers $s$, and $\rho(t) = 0$ whenever $t$ is minimal. Let
$\alpha_P$ be the flag $f$-vector of $P$ with respect to $\rho$: for a finite set
$T \subseteq \mathbb{Z}_{\ge 0}$, $\alpha_P(T)$ is the number of maximal chains in the subposet
$\{t \in P : \rho(t) \in T\}$. The flag $h$-vector of $P$ is the integer-valued function $\beta_P$
on finite sets $S \subseteq \mathbb{Z}_{\ge 0}$ given by

$$\beta_P(S) = \sum_{T \subseteq S} (-1)^{|S \setminus T|} \alpha_P(T),$$

where the sum runs over all subsets $T$ of $S$ and $|S \setminus T|$ is the number of elements of
$S \setminus T$. In particular, $\beta_P(\emptyset) = \alpha_P(\emptyset) = 1$.

Formalized by `MetaMathlibExt.flagHVector`, a definition declared in [MathlibExt/Combinatorics/Poset/Basic.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Poset/Basic.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors/index.html#flag-hvector).

## Hyperplane arrangement

Let $K$ be a field, let $V$ be a finite-dimensional vector space
over $K$, and let $E$ be an affine subspace of $V$, possibly empty. The dimension of a nonempty
affine subspace $v + W$, with $v \in V$ and $W$ a linear subspace of $V$, is $\dim W$. An affine
hyperplane of $E$ is a nonempty affine subspace $H$ of $V$ with $H \subseteq E$ and
$\dim H + 1 = \dim E$. A set $\mathcal{A}$ of affine subspaces of $V$ is a hyperplane arrangement
in $E$ if $\mathcal{A}$ is finite and every element of $\mathcal{A}$ is an affine hyperplane of $E$.

For $n \in \mathbb{Z}_{\ge 0}$, $V = K^n$ and $E = V$, the affine hyperplanes of $E$ are the sets
$\{v \in K^n : \alpha_1 v_1 + \cdots + \alpha_n v_n = a\}$
with $(\alpha_1, \ldots, \alpha_n) \in K^n$ nonzero and $a \in K$. The empty set is a hyperplane
arrangement in every $E$, and it is the only one when $E$ is empty or $\dim E = 0$.

Formalized by `MetaMathlibExt.IsHyperplaneArrangement`, a definition declared in [MathlibExt/Combinatorics/Poset/Basic.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Poset/Basic.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors/index.html#is-hyperplane-arrangement).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Möbius algebras and flag vectors](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/partially-ordered-sets/m-bius-algebras-and-flag-vectors)
