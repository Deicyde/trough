# Sphere packing in dimension 8

The blueprint of Sphere packing in dimension 8, read at commit [efe3bbbc](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/tree/efe3bbbc1ece548f4672a772b94d8f621c10fdda) (2026-11-11): one article for each of its 94 nodes whose Lean declarations it names and marks formalized, or in Mathlib. Its other 45 nodes have no article, and a section of only those is left out: the map records what the project contains, not what it plans. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

The repository math-inc/Sphere-Packing-Lean is a fork of this one that completes the formalization in dimensions 8 and 24, and has its own chapter, [Sphere packing in dimensions 8 and 24 (Math Inc)](../sphere-packing-math-inc/README.md). At commit efe3bbbc of this repository and commit 1e98fb49 of the fork, the fork was one commit ahead of this repository and 78 commits behind.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

This blueprint consists of an adaptation of Maryna Viazovska's Fields Medal-winning paper proving that no packing of unit balls in Euclidean space $\mathbb{R}^8$ has density greater than that of the $E_8$-lattice packing.

You can view the contents of the current version of this page in PDF form [here](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/blueprint.pdf).

This formalisation project was kickstarted at EPFL by Maryna Viazovska and Sidharth Hariharan, and the contents of this blueprint were originally written by Maryna Viazovska on the suggestion of Kevin Buzzard. It is being updated and restructured by those involved in the formalisation effort. We express our sincere gratitude to Jeremy Avigad, Kevin Buzzard, David Loeffler, Pietro Monticone, David Renshaw, Utensil Song, the Mathlib maintainers, the Institute for Computer-Aided Reasoning in Mathematics, and everyone in the Lean Community for their invaluable contributions and support.

- [Sphere packings](sphere-packings/README.md)
- [Density of packings](density-of-packings/README.md)
- [The $E_8$ lattice](the-e-8-lattice/README.md)
- [Facts from Fourier analysis](facts-from-fourier-analysis/README.md)
- [Cohn-Elkies linear programming bounds](cohn-elkies-linear-programming-bounds/README.md)
- [Modular forms](modular-forms/README.md)
- [Fourier eigenfunctions with double zeroes at lattice points](fourier-eigenfunctions-with-double-zeroes-at-lat/README.md)
- [Proof of Theorem g](proof-of-theorem-g/README.md)
