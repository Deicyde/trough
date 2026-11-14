# Sphere packing in dimensions 8 and 24 (Math Inc)

The blueprint of Sphere packing in dimensions 8 and 24 (Math Inc), read at commit [1e98fb49](https://github.com/math-inc/Sphere-Packing-Lean/tree/1e98fb493088948ca7bbf47d7faed49cc5b39fc4) (2026-03-02): one article for each of its 159 nodes whose Lean declarations it names and marks formalized, or in Mathlib. Its other 7 nodes have no article, and a section of only those is left out: the map records what the project contains, not what it plans. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

This repository is a fork of thefundamentaltheor3m/Sphere-Packing-Lean, whose chapter is [Sphere packing in dimension 8](../sphere-packing/README.md). At commit 1e98fb49 of this repository and commit efe3bbbc of the original, the fork was one commit ahead of the original, the commit that adds the dimension 8 and 24 formalizations, and 78 commits behind.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

This blueprint consists of an adaptation of Maryna Viazovska's Fields Medal-winning paper proving that no packing of unit balls in Euclidean space $\mathbb{R}^8$ has density greater than that of the $E_8$-lattice packing, together with a blueprint for the analogous optimality result in dimension $24$ (the Leech lattice).

This formalisation project was kickstarted at EPFL by Maryna Viazovska and Sidharth Hariharan in March 2024 (see the original [Sphere-Packing-Lean](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean) repository). The present repository builds on that project: using the existing blueprint and codebase, the autoformalization agent Gauss completed the dimension $8$ development, and then formalized dimension $24$ optimality and periodic uniqueness, updating the blueprint along the way.

- [Sphere packings](sphere-packings/README.md)
- [Density of packings](density-of-packings/README.md)
- [The $E_8$ lattice](the-e-8-lattice/README.md)
- [Facts from Fourier analysis](facts-from-fourier-analysis/README.md)
- [Cohn-Elkies linear programming bounds](cohn-elkies-linear-programming-bounds/README.md)
- [Modular forms](modular-forms/README.md)
- [Fourier eigenfunctions with double zeroes at lattice points](fourier-eigenfunctions-with-double-zeroes-at-lat/README.md)
- [Proof of Theorem g](proof-of-theorem-g/README.md)
- [Sphere packing in dimension $24$](sphere-packing-in-dimension-24/README.md)
