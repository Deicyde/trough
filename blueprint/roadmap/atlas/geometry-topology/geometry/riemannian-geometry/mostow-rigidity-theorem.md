---
declaration: section
origin: cited
lean: MathlibExt.Geometry.MostowRigidityWanted.Geometry.MostowRigidity.PO, MathlibExt.Geometry.MostowRigidityWanted.Geometry.MostowRigidity.mostow_rigidity
statement: formalized
---

# Mostow rigidity theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/mostow-rigidity-theorem/index.html).

## Projective indefinite orthogonal group

For natural numbers $p$ and $q$, let $J$ be the
diagonal $(p+q) \times (p+q)$ real matrix whose first $p$ diagonal entries are $1$ and whose last
$q$ are $-1$, and let $\mathrm{O}(p,q)$ be the group of real $(p+q) \times (p+q)$ matrices $A$
with $J A^{\mathsf{T}} J A = A J A^{\mathsf{T}} J = I$. The group $\mathrm{PO}(p,q)$ is the
quotient of $\mathrm{O}(p,q)$ by its center.

Formalized by `MathlibExt.Geometry.MostowRigidityWanted.Geometry.MostowRigidity.PO`, a definition declared in [WantedExt/Geometry/MostowRigidityWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MostowRigidityWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/mostow-rigidity-theorem/index.html#po).

## Mostow rigidity, algebraic form

Let $n \ge 3$, and let $\Gamma$ and $\Lambda$ be lattices
in the projective orthogonal group $\mathrm{PO}(n,1)$: discrete subgroups that have a fundamental
domain for their action by left multiplication and finite covolume with respect to Haar measure.
Then every group isomorphism $f : \Gamma \to \Lambda$ is a conjugation: there is
$g \in \mathrm{PO}(n,1)$ such that $f(\gamma) = g \gamma g^{-1}$ for all $\gamma \in \Gamma$.

## Sources

- https://en.wikipedia.org/wiki/Mostow_rigidity_theorem#Algebraic_form and Gopal Prasad, *Strong rigidity of ℚ-rank 1 lattices*, Invent. Math. 21 (1973), 255–286. Problem `mostow_rigidity` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.MostowRigidityWanted.Geometry.MostowRigidity.mostow_rigidity` is written with `theorem_wanted` in [WantedExt/Geometry/MostowRigidityWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/MostowRigidityWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/mostow-rigidity-theorem/index.html#mostow-rigidity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mostow rigidity theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/mostow-rigidity-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/mostow-rigidity-theorem)
