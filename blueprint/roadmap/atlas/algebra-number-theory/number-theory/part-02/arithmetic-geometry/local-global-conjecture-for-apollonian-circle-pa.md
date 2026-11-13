---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.GeneralLinearGroupAction, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.DescartesMatrix, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.DescartesOrthogonalGroup, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.DescartesOrthogonalGroupAction, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.integralPrimitiveDescartesQuadruple, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₁, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₂, MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₃
statement: formalized
---

# Local-global conjecture for Apollonian circle packings

19 results, 17 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html).

## General linear group action on primitive vectors

Call $v \in \mathbb{Z}^4$ primitive
when the greatest common divisor of its four entries is $1$. For every
$X \in \mathrm{GL}_4(\mathbb{Z})$ and every primitive $v$, the vector $Xv$ is primitive, so
$\mathrm{GL}_4(\mathbb{Z})$ acts on the primitive vectors of $\mathbb{Z}^4$ by $v \mapsto Xv$.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.GeneralLinearGroupAction`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#general-linear-group-action).

## Descartes matrix

The Descartes matrix is the $4 \times 4$ integer matrix $M$ with
$M_{ii} = 1$ for every $i$ and $M_{ij} = -1$ for $i \ne j$. It is the matrix of the Descartes
form: for $v = (a, b, c, d) \in \mathbb{Z}^4$ one has
$v^{\mathsf T} M v = 2(a^2 + b^2 + c^2 + d^2) - (a + b + c + d)^2$.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.DescartesMatrix`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#descartes-matrix).

## Descartes orthogonal group

Let $M$ be the Descartes matrix. The Descartes orthogonal
group is the subgroup of $\mathrm{GL}_4(\mathbb{Z})$ consisting of the matrices $X$ with
$X^{\mathsf T} M X = M$, that is, the invertible integer matrices that preserve the Descartes
form $2(a^2 + b^2 + c^2 + d^2) - (a + b + c + d)^2$.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.DescartesOrthogonalGroup`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#descartes-orthogonal-group).

## Descartes orthogonal group action

Let $Q$ be the set of vectors
$(a, b, c, d) \in \mathbb{Z}^4$ with $(a + b + c + d)^2 = 2(a^2 + b^2 + c^2 + d^2)$ and
$\gcd(a, b, c, d) = 1$. For every matrix $X$ in the Descartes orthogonal group and every $v \in Q$,
the vector $Xv$ lies in $Q$, so the Descartes orthogonal group acts on $Q$ by $v \mapsto Xv$.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.DescartesOrthogonalGroupAction`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#descartes-orthogonal-group-action).

## Integral primitive Descartes quadruple

An integral primitive Descartes quadruple is a
vector $(a, b, c, d) \in \mathbb{Z}^4$ such that $a + b + c + d > 0$, the Descartes equation
$(a + b + c + d)^2 = 2(a^2 + b^2 + c^2 + d^2)$ holds, and $\gcd(a, b, c, d) = 1$.

## Sources

- S. Haag, C. Kertzer, J. Rickards, and K. E. Stange, `The local-global conjecture for Apollonian circle packings is false`, Annals of Math, 200 (2) 2024, Section 1.1.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.integralPrimitiveDescartesQuadruple`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#integral-primitive-descartes-quadruple).

## The Apollonian generator $S_1$

$S_1$ is the element of $\mathrm{GL}_4(\mathbb{Z})$ given
by the $4 \times 4$ integer matrix whose first row is $(-1, 2, 2, 2)$ and whose other rows are
those of the identity matrix; it is its own inverse. Acting on column vectors, it sends
$(a, b, c, d)$ to $(-a + 2b + 2c + 2d, b, c, d)$.

It is one of the four generators of the Apollonian group defined at the start of Section 3 of
Haag, Kertzer, Rickards and Stange.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₁`, an abbreviation declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#s).

## The Apollonian generator $S_2$

$S_2$ is the element of $\mathrm{GL}_4(\mathbb{Z})$ given
by the $4 \times 4$ integer matrix whose second row is $(2, -1, 2, 2)$ and whose other rows are
those of the identity matrix; it is its own inverse. Acting on column vectors, it sends
$(a, b, c, d)$ to $(a, 2a - b + 2c + 2d, c, d)$.

It is one of the four generators of the Apollonian group defined at the start of Section 3 of
Haag, Kertzer, Rickards and Stange.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₂`, an abbreviation declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#s-2).

## The Apollonian generator $S_3$

$S_3$ is the element of $\mathrm{GL}_4(\mathbb{Z})$ given
by the $4 \times 4$ integer matrix whose third row is $(2, 2, -1, 2)$ and whose other rows are
those of the identity matrix; it is its own inverse. Acting on column vectors, it sends
$(a, b, c, d)$ to $(a, b, 2a + 2b - c + 2d, d)$.

It is one of the four generators of the Apollonian group defined at the start of Section 3 of
Haag, Kertzer, Rickards and Stange.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₃`, an abbreviation declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#s-3).

## The Apollonian generator $S_4$

$S_4$ is the element of $\mathrm{GL}_4(\mathbb{Z})$ given
by the $4 \times 4$ integer matrix whose fourth row is $(2, 2, 2, -1)$ and whose other rows are
those of the identity matrix; it is its own inverse. Acting on column vectors, it sends
$(a, b, c, d)$ to $(a, b, c, 2a + 2b + 2c - d)$.

It is one of the four generators of the Apollonian group defined at the start of Section 3 of
Haag, Kertzer, Rickards and Stange.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.S₄`, an abbreviation declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#s-4).

## Apollonian group

The Apollonian group is the subgroup of $\mathrm{GL}_4(\mathbb{Z})$
generated by the four matrices $S_1, S_2, S_3, S_4$, where $S_i$ agrees with the $4 \times 4$
identity matrix except in row $i$, which has entry $-1$ in column $i$ and entry $2$ in each of
the other three columns.

## Sources

- S. Haag, C. Kertzer, J. Rickards, and K. E. Stange, `The local-global conjecture for Apollonian circle packings is false`, Annals of Math, 200 (2) 2024, start of Section 3.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.ApollonianGroup`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#apollonian-group).

## The transformation group

The transformation group is the subgroup of
$\mathrm{GL}_4(\mathbb{Z})$ generated by the Apollonian group together with all $4 \times 4$
permutation matrices.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.TransformationGroup`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#transformation-group).

## The transformation group preserves integral primitive Descartes quadruples

For every $g$ in the transformation group, $g$ maps the set of integral primitive Descartes
quadruples into itself: if $v \in \mathbb{Z}^4$ is an integral primitive Descartes quadruple,
then so is $g v$.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.transformationGroup_smul_integralPrimitiveDescartesQuadruple`, a theorem declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#transformation-group-smul-integral-primi).

## Action of the transformation group on integral primitive Descartes quadruples

Each
element $g$ of the transformation group sends an integral primitive Descartes quadruple $v$ to
$g v$, by matrix–vector multiplication: this is the restriction of the action of the
transformation group on $\mathbb{Z}^4$ to the set of integral primitive Descartes quadruples,
which is closed under the action.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.TransformationGroupAction`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#transformation-group-action).

## Primitive Apollonian circle packing

A primitive Apollonian circle packing is an orbit of
the transformation group acting on the set of integral primitive Descartes quadruples.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.PrimitiveApollonianCirclePacking`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#primitive-apollonian-circle-packing).

## Curvature set

Let $A$ be a primitive Apollonian circle packing, viewed as an orbit of
integral primitive Descartes quadruples. The curvature set of $A$ is the set of all integers
that occur as an entry of some quadruple in $A$.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.curvatureSet`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#curvature-set).

## A packing with no square curvatures

Let $\mathcal{A}$ be the primitive Apollonian circle
packing generated by the integral primitive Descartes quadruple $(-3, 5, 8, 8)$. For every
integer $n$, $n^2$ does not belong to the curvature set of $\mathcal{A}$.

## Sources

- S. Haag, C. Kertzer, J. Rickards, and K. E. Stange, `The local-global conjecture for Apollonian circle packings is false`, Annals of Math, 200 (2) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_local_global_apollonian_circle_packings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.theorem_1_6` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#theorem-1-6).

## Missing curvature set

Let $A$ be a primitive Apollonian circle packing. The missing
curvature set of $A$ is the set of positive integers $n$ that do not lie in the curvature set
of $A$ but are congruent modulo $24$ to some element of the curvature set of $A$.

## Sources

- S. Haag, C. Kertzer, J. Rickards, and K. E. Stange, `The local-global conjecture for Apollonian circle packings is false`, Annals of Math, 200 (2) 2024, start of Section 1.2.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.missingCurvatureSet`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#missing-curvature-set).

## Number of missing curvatures

For a primitive Apollonian circle packing $A$ and a real
number $N$, the number of missing curvatures of $A$ up to $N$ is the number of elements $n$ of
the missing curvature set of $A$ with $n \le N$, regarded as a real number.

Formalized by `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.missingCurvatures`, a definition declared in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#missing-curvatures).

## Infinitely many packings with many missing curvatures

For a primitive Apollonian circle
packing $\mathcal{A}$ and a real number $N$, let $M_{\mathcal{A}}(N)$ be the number of missing
curvatures of $\mathcal{A}$ up to $N$. There are infinitely many primitive Apollonian circle
packings $\mathcal{A}$ such that $\sqrt{N} = O(M_{\mathcal{A}}(N))$ as $N$ tends to infinity.
In other words, for these packings the number of missing curvatures up to $N$ is
$\Omega(\sqrt{N})$.

## Sources

- S. Haag, C. Kertzer, J. Rickards, and K. E. Stange, `The local-global conjecture for Apollonian circle packings is false`, Annals of Math, 200 (2) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_local_global_apollonian_circle_packings` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.LocalGlobalApollonianCirclePackingsWanted.LocalGlobalApollonianCirclePackings.theorem_1_3` is written with `theorem_wanted` in [WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/LocalGlobalApollonianCirclePackingsWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html#theorem-1-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local-global conjecture for Apollonian circle packings](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-geometry/local-global-conjecture-for-apollonian-circle-pa)
