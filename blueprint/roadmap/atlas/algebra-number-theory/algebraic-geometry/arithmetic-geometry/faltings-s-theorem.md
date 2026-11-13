---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Place, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.finite_setOf_place_notMem, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Adele, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Adele.principal, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Adele.principal_apply, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.instAlgebraAdele_algebraMap, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.integralAdele, MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.genus
statement: formalized
---

# Faltings's theorem

10 results, 3 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html).

## Place

Let $F$ be a field and $K$ a field with $F$ a $K$-algebra. A place of $F/K$ is a
valuation ring of $F$ containing $K$ and different from $F$: a $K$-subalgebra $\mathcal{O}$ of
$F$ with $\mathcal{O} \neq F$ such that $z \in \mathcal{O}$ or $z^{-1} \in \mathcal{O}$ for
every $z \in F$. See [Stichtenoth, Definition 1.1.4 and 1.1.8].

Stichtenoth calls the maximal ideal of $\mathcal{O}$ the place, which determines $\mathcal{O}$,
and also requires $\mathcal{O} \neq K$; that condition is omitted since it is automatic.

Formalized by `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Place`, a structure declared in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#place).

## Finitely many poles

Let $F$ be a function field over a field $K$, that is, a finite
extension of the rational function field $K(t)$. For every $x \in F$, there are only finitely
many places $P$ of $F/K$ whose valuation ring $\mathcal{O}_P$ does not contain $x$, that is,
$x$ has only finitely many poles. See [Stichtenoth, Corollary 1.3.4].

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.finite_setOf_place_notMem` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#finite-set-of-place-not-mem).

## Adele ring

Let $F$ be a field and $K$ a field with $F$ a $K$-algebra. The adele ring
$\mathcal{A}_F$ of $F/K$ is the restricted product of copies of $F$ indexed by the places $P$
of $F/K$, with respect to their valuation rings $\mathcal{O}_P$ and the cofinite filter: its
elements are the families $\alpha = (\alpha_P)_P$ with $\alpha_P \in F$ for every place $P$
and $\alpha_P \in \mathcal{O}_P$ for all but finitely many $P$. See [Stichtenoth, Definition
1.5.2].

Formalized by `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Adele`, an abbreviation declared in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#adele).

## Principal adele map

Let $F$ be a function field over a field $K$, that is, a finite
extension of the rational function field $K(t)$. The principal adele map is a ring homomorphism
from $F$ to the adele ring $\mathcal{A}_F$ of $F/K$. It is meant to be the diagonal embedding
sending $x \in F$ to the adele whose coordinate at every place $P$ of $F/K$ is $x$, which is
well defined since $x$ has only finitely many poles; this coordinate formula is stated
separately.

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Adele.principal` is written with `def_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#principal).

## Coordinates of a principal adele

Let $F$ be a function field over a field $K$, that is,
a finite extension of the rational function field $K(t)$. For every $x \in F$ and every place
$P$ of $F/K$, the coordinate at $P$ of the principal adele of $x$ is $x$.

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.Adele.principal_apply` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#principal-apply).

## The adele algebra map is the principal embedding

Let $F$ be a function field over a
field $K$, that is, a finite extension of the rational function field $K(t)$. The algebra map
$F \to \mathcal{A}_F$ of the $F$-algebra structure on the adele ring $\mathcal{A}_F$ equals the
principal adele map $F \to \mathcal{A}_F$.

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.instAlgebraAdele_algebraMap` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#inst-algebra-adele-algebra-map).

## Integral adeles

Let $F$ be a field and $K$ a field with $F$ a $K$-algebra. The integral
adeles $\mathcal{A}_F(0)$ form the $K$-subspace of the adele ring $\mathcal{A}_F$ of $F/K$
consisting of the adeles $\alpha = (\alpha_P)_P$ whose coordinate $\alpha_P$ lies in the
valuation ring $\mathcal{O}_P$ of $P$ for every place $P$ of $F/K$. See [Stichtenoth,
Definition 1.5.3].

Formalized by `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.integralAdele`, a definition declared in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#integral-adele).

## Genus of a function field

For a function field $F$ over a field $K$, that is, a finite
extension of the rational function field $K(t)$, the genus of $F/K$ is a natural number $g$,
specified by the separately stated formula $g = \dim_K \mathcal{A}_F / (\mathcal{A}_F(0) + F)$,
where $\mathcal{A}_F$ is the adele ring and $\mathcal{A}_F(0)$ the integral adeles.
See [Stichtenoth, Corollary 1.5.5].

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.genus` is written with `def_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#genus).

## Genus as the dimension of the adele class space

Let $F$ be a function field over a
field $K$, that is, a finite extension of the rational function field $K(t)$. The genus $g$ of
$F/K$ equals the dimension over $K$ of the quotient
$\mathcal{A}_F / (\mathcal{A}_F(0) + F)$, where $\mathcal{A}_F$ is the adele ring,
$\mathcal{A}_F(0)$ the integral adeles, and $F$ is embedded in $\mathcal{A}_F$ by the algebra
map of the $F$-algebra structure on the adeles (stated separately to be the principal
embedding). See [Stichtenoth, Corollary 1.5.5].

The dimension is the finite rank, taken to be $0$ if the quotient is infinite-dimensional.

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.genus_eq` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#genus-eq).

## Faltings' theorem (Mordell conjecture)

Let $K$ be a number field and $F$ a function
field over $K$, that is, a finite extension of the rational function field $K(t)$. If the genus
of $F/K$ is at least $2$, then $F/K$ has only finitely many places of degree one, that is,
places $P$ whose residue field (the quotient of the valuation ring of $P$ by its maximal ideal)
has dimension $1$ over $K$.

## Sources

-. Problem `faltings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.FaltingsWanted.AlgebraicGeometry.Faltings.faltings` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/FaltingsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/FaltingsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html#faltings).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Faltings's theorem](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/arithmetic-geometry/faltings-s-theorem)
