---
declaration: section
origin: cited
lean: MetaMathlibExt.dyckPeakDescents, MetaMathlibExt.dyckPeakDescents_sample
statement: formalized
proof: formalized
---

# Peak descents of Dyck paths

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/peak-descents-of-dyck-paths/index.html).

## Peak descents

Let $l$ be a finite sequence of up steps $U$ and down steps $D$. A peak
of $l$ is a position where a step $U$ is immediately followed by a step $D$. The peak descents
of $l$ form the list that has, for each peak from left to right, the length $j$ of the maximal
run of consecutive steps $D$ that starts at the $D$ of that peak, so that the peak and its
descent form the primitive block $U D^j$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2 (Dyck paths).

Formalized by `MetaMathlibExt.dyckPeakDescents`, a definition declared in [MathlibExt/Combinatorics/Enumerative/DyckPeakDescents.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DyckPeakDescents.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/peak-descents-of-dyck-paths/index.html#dyck-peak-descents).

## Peak descents of a sample Dyck path

The Dyck path $UUUUDDDUDDUUDUUDDD$, which factors
as $U\,U\,U\,(UD^3)(UD^2)\,U\,(UD)\,U\,(UD^3)$, has four peaks $UD$, and the lengths of the
maximal runs of $D$ steps starting at the $D$ of each peak are, from left to right,
$3, 2, 1, 3$.

## Sources

- Gil, Hoover, and Shearer, *Bijections Between Colored Compositions, Dyck Paths, and Polygon Partitions*, Journal of Integer Sequences 27 (2024), Article 24.5.2, Section 2.

Formalized by `MetaMathlibExt.dyckPeakDescents_sample`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/DyckPeakDescents.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/DyckPeakDescents.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/peak-descents-of-dyck-paths/index.html#dyck-peak-descents-sample).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Peak descents of Dyck paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/peak-descents-of-dyck-paths/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/dyck-paths-lattice-walks/peak-descents-of-dyck-paths)
