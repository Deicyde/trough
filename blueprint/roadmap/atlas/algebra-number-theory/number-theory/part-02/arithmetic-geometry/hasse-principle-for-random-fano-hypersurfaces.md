---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.𝔸, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.height, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.HasSolutionsIn, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.𝕍, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.heightLE, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.𝕍Loc, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.ρLoc, MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.ρ
statement: formalized
---

# Hasse principle for random Fano hypersurfaces

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html).

## Adele ring of the rationals

$\mathbb{A}_\mathbb{Q}$, also written $\mathbb{A}$, is the
adele ring of $\mathbb{Q}$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.𝔸`, an abbreviation declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#untitled).

## Height of a rational polynomial

Let $f$ be a multivariate polynomial with rational
coefficients. Multiply the coefficients of $f$ by the least common multiple of their denominators
and divide the resulting integers by their greatest common divisor; this gives the primitive
integer coefficient vector $(a_m)_m$ of $f$, indexed by the monomials $m$ in the support of $f$.
The height of $f$ is the Euclidean norm $\sqrt{\sum_m a_m^2}$ of this vector. The zero polynomial
has height $0$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.height`, a definition declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#height).

## Unimodular solutions of a polynomial

Let $R$ and $S$ be commutative semirings with $S$ an
$R$-algebra, and let $f$ be a multivariate polynomial over $R$ in variables indexed by a type
$\sigma$. Then $f$ has a solution in $S$ if there is a vector $x \in S^\sigma$ whose components
generate the unit ideal of $S$ and such that $f(x) = 0$, where $f$ is evaluated at $x$ through
the algebra map $R \to S$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.HasSolutionsIn`, a definition declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#has-solutions-in).

## Parameter space of hypersurfaces

$\mathbb{V}_{d,n}$ is the projectivization of the
$\mathbb{Q}$-vector space of homogeneous polynomials of degree $d$ in $n + 1$ variables with
rational coefficients; its points are the degree-$d$ hypersurfaces in $\mathbb{P}^n$ defined over
$\mathbb{Q}$. Since this space has dimension $N_{d,n} = \binom{n+d}{d}$, the number of degree-$d$
monomials in $n + 1$ variables, $\mathbb{V}_{d,n}$ is a copy of
$\mathbb{P}^{N_{d,n} - 1}(\mathbb{Q})$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.𝕍`, an abbreviation declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#untitled-2).

## Hypersurfaces of bounded height

For a real number $A$, $\mathbb{V}_{d,n}(A)$ is the set of
degree-$d$ hypersurfaces $V \in \mathbb{V}_{d,n}$ in $\mathbb{P}^n$ whose height is at most $A$,
where the height of $V$ is the height of the chosen nonzero homogeneous polynomial of degree $d$
that represents $V$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.heightLE`, a definition declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#height-le).

## Everywhere locally soluble hypersurfaces

$\mathbb{V}^{\mathrm{loc}}_{d,n}$ is the set of
degree-$d$ hypersurfaces $V \in \mathbb{V}_{d,n}$ in $\mathbb{P}^n$ that are everywhere locally
soluble, that is, with $V(\mathbb{A}_\mathbb{Q}) \ne \emptyset$: the chosen homogeneous polynomial
representing $V$ has a solution in the adele ring $\mathbb{A}_\mathbb{Q}$, namely a zero given by
$n + 1$ adeles that generate the unit ideal of $\mathbb{A}_\mathbb{Q}$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.𝕍Loc`, a definition declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#loc).

## Local density of everywhere locally soluble hypersurfaces

For natural numbers $d$ and
$n$ and a real number $A$, let $\mathbb{V}_{d,n}(A)$ be the set of degree-$d$ hypersurfaces in
$\mathbb{P}^n$ of height at most $A$, and let $\mathbb{V}^{\mathrm{loc}}_{d,n}$ be the set of
everywhere locally soluble ones. The local density $\rho^{\mathrm{loc}}_{d,n}$ is the limit, as
$A \to \infty$, of the number of elements of
$\mathbb{V}^{\mathrm{loc}}_{d,n} \cap \mathbb{V}_{d,n}(A)$ divided by the number of elements of
$\mathbb{V}_{d,n}(A)$, a quotient taken to be $0$ when $\mathbb{V}_{d,n}(A)$ is empty; when this
limit does not exist, $\rho^{\mathrm{loc}}_{d,n}$ is an unspecified real number.

By a theorem of Poonen–Voloch [17, Th. 3.6], this limit exists (and is positive) when
$d \ge 2$, $n \ge 2$ and $(d, n) \ne (2, 2)$, and equals a product of local densities over all
places of $\mathbb{Q}$.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.ρLoc`, a definition declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#loc-2).

## Proportion of soluble hypersurfaces of bounded height

For a real number $A$,
$\rho_{d,n}(A)$ is the proportion of hypersurfaces in $\mathbb{V}_{d,n}(A)$, the degree-$d$
hypersurfaces in $\mathbb{P}^n$ of height at most $A$, that have a rational point: it is the
number of $V \in \mathbb{V}_{d,n}(A)$ with $V(\mathbb{Q}) \ne \emptyset$ divided by the number of
elements of $\mathbb{V}_{d,n}(A)$, taken to be $0$ when $\mathbb{V}_{d,n}(A)$ is empty. Here
$V(\mathbb{Q}) \ne \emptyset$ means that the chosen homogeneous polynomial representing $V$ has a
nonzero rational zero.

Formalized by `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.ρ`, a definition declared in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#untitled-3).

## Density of soluble Fano hypersurfaces

Let $d$ and $n$ be natural numbers with $d \ge 2$,
$n \ge d$ and $(d, n) \ne (3, 3)$. Then the proportion $\rho_{d,n}(A)$ of degree-$d$
hypersurfaces in $\mathbb{P}^n$ of height at most $A$ that have a rational point tends to the
local density $\rho^{\mathrm{loc}}_{d,n}$ as the real number $A$ tends to $\infty$.

## Sources

- T. Browning, P. L. Boudec, and W. Sawin, `The Hasse principle for random Fano hypersurfaces`, Annals of Math, 197 (3) 2023. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_hasse_principle_random_fano` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.HassePrincipleRandomFanoWanted.HassePrincipleRandomFano.theorem_1_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/HassePrincipleRandomFanoWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hasse principle for random Fano hypersurfaces](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-geometry/hasse-principle-for-random-fano-hypersurfaces)
