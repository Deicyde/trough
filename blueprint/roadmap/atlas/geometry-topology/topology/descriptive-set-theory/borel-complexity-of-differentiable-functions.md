---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook52Wanted.HasDerivativeAtEveryPoint, MathlibExt.Topology.ScottishBook52Wanted.everywhere_differentiable_class_not_borel
statement: formalized
---

# Borel complexity of differentiable functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/borel-complexity-of-differentiable-functions/index.html).

## Functions differentiable at every point of $(0, 1)$

A continuous function
$f \colon (0, 1) \to \mathbb{R}$ has a derivative at every point if for every $x \in (0, 1)$ the
function $\tilde f \colon \mathbb{R} \to \mathbb{R}$ equal to $f$ on $(0, 1)$ and to $0$ outside
$(0, 1)$ is differentiable at $x$. Since $\tilde f$ agrees with $f$ near every point of $(0, 1)$,
this depends only on $f$: it says that $f$ is differentiable at every point of $(0, 1)$.

Formalized by `MathlibExt.Topology.ScottishBook52Wanted.HasDerivativeAtEveryPoint`, a definition declared in [WantedExt/Topology/ScottishBook52Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook52Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/borel-complexity-of-differentiable-functions/index.html#has-derivative-at-every-point).

## Everywhere differentiable functions do not form a Borel set

In the space $C((0, 1))$ of
continuous real functions on the open interval $(0, 1)$, with the compact-open topology (uniform
convergence on compact subsets), the set of functions that have a derivative at every point of
$(0, 1)$ is not a Borel set.

This is Banach's Problem 52 of the Scottish Book. The typescript also records that this class is
not an $F_\sigma$ set, that it is coanalytic, and that the problem was solved by Mazurkiewicz.

## Sources

- S. Banach, Problem 52 of the Scottish Book; solved by Mazurkiewicz, as recorded in typescript Ad 52; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook52Wanted.everywhere_differentiable_class_not_borel` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook52Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook52Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/borel-complexity-of-differentiable-functions/index.html#everywhere-differentiable-class-not-bore).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Borel complexity of differentiable functions](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/borel-complexity-of-differentiable-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/descriptive-set-theory/borel-complexity-of-differentiable-functions)
