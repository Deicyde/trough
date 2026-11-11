---
declaration: section
origin: cited
lean: CovariantDerivative.leviCivitaConnection_vectorSpace_apply, MathlibExt.Geometry.MetricCompatibilityShared.IsMetricCompatible, MathlibExt.Geometry.KoszulFormulaWanted.Geometry.KoszulFormula.koszul_formula, MathlibExt.Geometry.LeviCivitaWanted.Geometry.LeviCivita.SameOnSmooth, MathlibExt.Geometry.LeviCivitaWanted.Geometry.LeviCivita.levi_civita_exists_unique
statement: formalized
---

# Levi-Civita connection

5 results, 3 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html).

## The Levi-Civita connection of a vector space is the Fréchet derivative

Let $F$ be a
finite-dimensional real inner product space with its standard Riemannian metric, let $V$ be a
vector field on $F$ and $x \in F$, and suppose $V$ is differentiable at $x$ as a section of the
tangent bundle. Then for every tangent vector $v \in T_xF$, the covariant derivative $\nabla_v V$
of $V$ at $x$ for the Levi-Civita connection $\nabla$ equals $DV(x)(v)$, the Fréchet derivative
of $V$ at $x$ applied to $v$.

Formalized by `CovariantDerivative.leviCivitaConnection_vectorSpace_apply`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/LeviCivitaVectorSpace.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/LeviCivitaVectorSpace.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html#levi-civita-connection-vector-space-appl).

## Metric-compatible covariant derivative

Let $M$ be a smooth manifold (possibly with
corners) modelled on a finite-dimensional real normed space, with a smooth Riemannian metric
$\langle \cdot, \cdot \rangle$ on its tangent bundle. A covariant derivative $\nabla$ on the
tangent bundle is compatible with the metric if for all smooth vector fields $Y, Z$ on $M$,
every point $x \in M$ and every tangent vector $v \in T_x M$,

$$
v \langle Y, Z \rangle = \langle \nabla_v Y, Z(x) \rangle + \langle Y(x), \nabla_v Z \rangle,
$$

where $v \langle Y, Z \rangle$ is the derivative at $x$ in the direction $v$ of the function
$y \mapsto \langle Y(y), Z(y) \rangle$.

Formalized by `MathlibExt.Geometry.MetricCompatibilityShared.IsMetricCompatible`, a definition declared in [WantedExt/Geometry/MetricCompatibilityShared.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MetricCompatibilityShared.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html#is-metric-compatible).

## Koszul formula

Let $M$ be a smooth manifold, modelled with corners on a finite-dimensional
real normed space, whose tangent bundle carries a smooth Riemannian metric $\langle \cdot, \cdot
\rangle$, and let $\nabla$ be a smooth covariant derivative on the tangent bundle of $M$ that is
torsion-free and compatible with the metric. Then for all smooth vector fields $X$, $Y$, $Z$ on
$M$ and every point $x \in M$, evaluating every term at $x$,

$$2 \langle \nabla_X Y, Z \rangle = X \langle Y, Z \rangle + Y \langle X, Z \rangle -
Z \langle X, Y \rangle - \langle X, [Y, Z] \rangle - \langle Y, [X, Z] \rangle +
\langle Z, [X, Y] \rangle,$$

where $\nabla_X Y$ at $x$ is the covariant derivative of $Y$ in the direction $X(x)$,
$X \langle Y, Z \rangle$ at $x$ is the derivative of the function $y \mapsto \langle Y(y), Z(y)
\rangle$ in the direction $X(x)$, and $[\cdot, \cdot]$ is the Lie bracket of vector fields.

## Sources

- J.-L. Koszul (course notes, 1950s); cf. do Carmo, Riemannian Geometry. Listed as §38 additional statement in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `koszul_formula` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.KoszulFormulaWanted.Geometry.KoszulFormula.koszul_formula` is written with `theorem_wanted` in [WantedExt/Geometry/KoszulFormulaWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/KoszulFormulaWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html#koszul-formula).

## Agreement of covariant derivatives on smooth vector fields

Let $M$ be a smooth manifold,
possibly with boundary or corners, modelled on a finite-dimensional real normed space, whose
tangent bundle carries a smooth Riemannian metric. Two covariant derivatives $\nabla$ and
$\nabla'$ on the tangent bundle of $M$ agree on smooth sections when $\nabla_v Y = \nabla'_v Y$
for every smooth vector field $Y$ on $M$, every point $x \in M$ and every tangent vector $v$ at
$x$.

Covariant derivatives here act on all sections of the tangent bundle, not only smooth ones, so the
uniqueness in the Levi-Civita theorem is stated as agreement on smooth vector fields.

Formalized by `MathlibExt.Geometry.LeviCivitaWanted.Geometry.LeviCivita.SameOnSmooth`, a definition declared in [WantedExt/Geometry/LeviCivitaWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/LeviCivitaWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html#same-on-smooth).

## Fundamental theorem of Riemannian geometry (Levi-Civita)

Let $M$ be a Hausdorff smooth
manifold, possibly with boundary or corners, modelled on a finite-dimensional real normed space,
whose tangent bundle carries a smooth Riemannian metric. Then there is a smooth covariant
derivative $\nabla$ on the tangent bundle of $M$ that is torsion-free and compatible with the
metric, and every smooth, torsion-free, metric-compatible covariant derivative $\nabla'$ on the
tangent bundle of $M$ agrees with $\nabla$ on smooth vector fields: $\nabla'_v Y = \nabla_v Y$ for
every smooth vector field $Y$ on $M$, every point $x \in M$ and every tangent vector $v$ at $x$.

## Sources

- T. Levi-Civita, Nozione di parallelismo in una varietà qualunque, Rend. Circ. Mat. Palermo 42 (1917). Listed as §38 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `levi_civita_exists_unique` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.LeviCivitaWanted.Geometry.LeviCivita.levi_civita_exists_unique` is written with `theorem_wanted` in [WantedExt/Geometry/LeviCivitaWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/LeviCivitaWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html#levi-civita-exists-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Levi-Civita connection](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/levi-civita-connection/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/levi-civita-connection)
