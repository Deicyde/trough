---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook175Wanted.ScottishBookHilbertCube, MathlibExt.Topology.ScottishBook175Wanted.ScottishBookLetterT, MathlibExt.Topology.ScottishBook175Wanted.borsuk175_hilbert_cube_times_letterT
statement: formalized
---

# Hilbert cube

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/hilbert-cube/index.html).

## The Hilbert cube

The Hilbert cube $Q = [0,1]^{\mathbb{N}}$ is the product of countably
many copies of the closed unit interval $[0,1]$, with the product topology.

Formalized by `MathlibExt.Topology.ScottishBook175Wanted.ScottishBookHilbertCube`, an abbreviation declared in [WantedExt/Topology/ScottishBook175Wanted.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook175Wanted.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/hilbert-cube/index.html#scottish-book-hilbert-cube).

## The letter T

The letter-T curve is the subset

$$T = \{(0, y) : 0 \le y \le 1\} \cup \{(x, 1) : -1 \le x \le 1\}$$

of $\mathbb{R}^2$: a vertical stem with a horizontal bar on top, meeting at the branch point
$(0, 1)$.

Formalized by `MathlibExt.Topology.ScottishBook175Wanted.ScottishBookLetterT`, an abbreviation declared in [WantedExt/Topology/ScottishBook175Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook175Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/hilbert-cube/index.html#scottish-book-letter-t).

## The Hilbert cube absorbs the letter T (Borsuk's Problem 175)

Let $Q = [0,1]^{\mathbb{N}}$ be
the Hilbert cube and let $T \subset \mathbb{R}^2$ be the letter-T curve. Both parts of Borsuk's
Problem 175 from the Scottish Book have affirmative answers: (a) the product $Q \times T$ is
homeomorphic to $Q$, and (b) the product $T^{\mathbb{N}}$ of countably many copies of $T$ is
homeomorphic to $Q$.

## Sources

- K. Borsuk, Problem 175 of the Scottish Book; positively solved by R. D. Anderson, as cited in Domoradzki-Stawiska-Zarichnyi, "90+ years of the Scottish Book" (arXiv:2603.27867), and in the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook175Wanted.borsuk175_hilbert_cube_times_letterT` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook175Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ScottishBook175Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/hilbert-cube/index.html#borsuk175-hilbert-cube-times-letter-t).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hilbert cube](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/hilbert-cube/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/continua-infinite-dimensional/hilbert-cube)
