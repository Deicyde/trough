---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SchurZassenhausWanted.schur_zassenhaus_conjugate_complements
statement: formalized
proof: formalized
---

# Group extensions and cohomology: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/index.html).

Extensions and complements (Schur–Zassenhaus), splitting of extensions, homology and first cohomology of groups, cohomological dimension, and integrability of groups as derived subgroups.

## Schur–Zassenhaus theorem: conjugacy of complements

Let $G$ be a finite group and $N$ a normal
subgroup of $G$ whose order is coprime to its index, and suppose $N$ is solvable. If $K_1$ and
$K_2$ are complements of $N$ in $G$, then there is an element $g \in N$ with $g K_1 g^{-1} = K_2$.

## Sources

- I. Schur (1904); H. Zassenhaus, Lehrbuch der Gruppentheorie (1937); Isaacs, Finite Group Theory; standard solvability hypothesis for conjugacy.

Formalized by `MathlibExt.GroupTheory.SchurZassenhausWanted.schur_zassenhaus_conjugate_complements`, a theorem declared in [MathlibExt/GroupTheory/SchurZassenhaus.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SchurZassenhaus.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/index.html#schur-zassenhaus-conjugate-complements).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Group extensions and cohomology](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/extensions-and-cohomology/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/extensions-and-cohomology)
