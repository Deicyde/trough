---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.projToSpec, MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.IsProjectiveHom, MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.IsNormalScheme, MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.kollar_lieblich_olsson_sawin
statement: formalized
---

# Topological reconstruction of varieties

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties/index.html).

## Structure morphism of a projective spectrum

Let $R$ be a commutative ring and $A$ a
commutative $R$-algebra graded by $R$-submodules $\mathcal{A}_0, \mathcal{A}_1, \dots$. The
structure morphism $\operatorname{Proj} \mathcal{A} \to \operatorname{Spec} R$ is the canonical
morphism $\operatorname{Proj} \mathcal{A} \to \operatorname{Spec} \mathcal{A}_0$ followed by the
morphism $\operatorname{Spec} \mathcal{A}_0 \to \operatorname{Spec} R$ induced by the algebra map
$R \to \mathcal{A}_0$.

For a polynomial ring over $R$ graded by total degree, this is the structure morphism of
projective space over $R$.

Formalized by `MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.projToSpec`, a definition declared in [WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties/index.html#proj-to-spec).

## Projective morphism to an affine scheme

Let $R$ be a commutative ring and $X$ a scheme.
A morphism $f : X \to \operatorname{Spec} R$ is projective if there are $n \in \mathbb{N}$ and a
closed immersion $i$ of $X$ into $\operatorname{Proj} R[x_1, \dots, x_n]$, the polynomial ring
graded by total degree, such that $f$ is $i$ followed by the structure morphism
$\operatorname{Proj} R[x_1, \dots, x_n] \to \operatorname{Spec} R$.

Formalized by `MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.IsProjectiveHom`, a definition declared in [WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties/index.html#is-projective-hom).

## Normal scheme

A scheme $X$ is normal if for every point $x \in X$ the local ring
$\mathcal{O}_{X,x}$ is an integrally closed domain.

Formalized by `MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.IsNormalScheme`, a definition declared in [WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties/index.html#is-normal-scheme).

## Kollár–Lieblich–Olsson–Sawin topological reconstruction theorem

Let $K$ and $L$ be
fields of characteristic zero, and let $X$ and $Y$ be irreducible normal schemes with projective
morphisms $f : X \to \operatorname{Spec} K$ and $g : Y \to \operatorname{Spec} L$. Suppose that
the Krull dimension of the underlying topological space of $X$ is at least $4$; or it is at least
$3$ and $K$ and $L$ are essentially of finite type over $\mathbb{Q}$; or it is at least $2$ and
$K$ and $L$ are uncountable. Then for every homeomorphism $h : X \to Y$ there is an isomorphism
of schemes $X \cong Y$ whose underlying map is $h$.

## Sources

- János Kollár, Max Lieblich, Martin Olsson, and Will Sawin. The Zariski topology, linear systems, and algebraic varieties. Problem `kollar_lieblich_olsson_sawin` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.AlgebraicGeometry.TopologicalReconstructionWanted.AlgebraicGeometry.TopologicalReconstruction.kollar_lieblich_olsson_sawin` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/AlgebraicGeometry/TopologicalReconstructionWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties/index.html#kollar-lieblich-olsson-sawin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Topological reconstruction of varieties](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/topological-reconstruction-of-varieties)
