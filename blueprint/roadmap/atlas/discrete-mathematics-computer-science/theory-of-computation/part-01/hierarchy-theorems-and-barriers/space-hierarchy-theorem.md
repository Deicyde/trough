---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.PSPACEL.l_ne_pspace, MetaMathlibExt.Complexity.KeyTheorems.SpaceHierarchy.space_hierarchy
statement: formalized
---

# Space hierarchy theorem

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/space-hierarchy-theorem/index.html).

## There is a PSPACE language outside L (space-hierarchy separation)

There is a decision
problem that belongs to PSPACE but not to the class $\mathsf{L}$ of decision problems decidable
in deterministic logarithmic space.

## Sources

- R. W. Stearns, J. Hartmanis, and P. M. Lewis II, "Hierarchies of memory limited computations" (1965); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PSPACEL.l_ne_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PSPACELWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/PSPACELWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/space-hierarchy-theorem/index.html#l-ne-pspace).

## Deterministic space hierarchy: quadratic versus linear space

There is a language $L$
of bitstrings that lies in $\mathrm{DSPACE}(n^2)$ but not in $\mathrm{DSPACE}(n)$, the
deterministic space classes of multi-tape Turing machines for the space bounds $n \mapsto n^2$
and $n \mapsto n$.

## Sources

- R. W. Stearns, J. Hartmanis, and P. M. Lewis II, "Hierarchies of memory limited computations", Proceedings of the Sixth Annual Symposium on Switching Circuit Theory and Logical Design (1965), 179-190.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.SpaceHierarchy.space_hierarchy` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SpaceHierarchyWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/SpaceHierarchyWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/space-hierarchy-theorem/index.html#space-hierarchy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Space hierarchy theorem](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/space-hierarchy-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/hierarchy-theorems-and-barriers/space-hierarchy-theorem)
