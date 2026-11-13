---
declaration: section
origin: cited
lean: Finset.exists_add_eq_of_image_sub_eq_self
statement: formalized
proof: formalized
---

# Additive bases: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/index.html).

Sets whose h-fold sums cover the integers or a group: asymptotic, exact and restricted bases, Schnirelmann density, Rohrbach's theorem, representation counts and convolutions, sums of cubes covering vector spaces, knight-move bases of the plane, and sumsets of infinite sets of positive or zero density.

## Rohrbach's symmetric basis theorem

Let $A$ be a finite set of natural numbers and $a$ a
natural number with $\{a - x : x \in A\} = A$, where $a - x$ denotes truncated subtraction
($a - x = 0$ when $x > a$). If every natural number $m \le a$ is a sum $x + y$ of two elements
$x, y \in A$, then every natural number $m \le 2a$ is such a sum.

The symmetry condition forces every element of $A$ to be at most $a$, so it says exactly that $A$
is invariant under $x \mapsto a - x$.

This is Rohrbach's theorem on symmetric restricted additive bases.

## Sources

- Jukka Kohonen, "A Meet-in-the-Middle Algorithm for Finding Extremal Restricted Additive 2-Bases", Journal of Integer Sequences 17 (2014), Article 14.6.8, theorem `theorem:symmrest`, lines 274–288, with notation and basis definitions at lines 226–248, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Kohonen2/kohonen5.tex>.

Formalized by `Finset.exists_add_eq_of_image_sub_eq_self`, a theorem declared in [MathlibExt/Combinatorics/Additive/SymmetricBasis.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Additive/SymmetricBasis.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/index.html#exists-add-eq-of-image-sub-eq-self).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Additive bases](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/additive-bases/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/additive-bases)
