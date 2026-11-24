# Carleson's theorem

[fpvandoorn/carleson](https://github.com/fpvandoorn/carleson) says in its README:

> A formalized proof of a generalized Carleson's theorem in the [Lean interactive theorem prover](https://lean-lang.org/).

Its blueprint, by Lars Becker, María Inés de Frutos-Fernández, Leo Diedering, Floris van Doorn, Sébastien Gouëzel, Asgar Jamneshan, Evgenia Karunus, Edward van de Meent, Pietro Monticone, Jasper Mulder-Sohn, Jim Portegies, Joris Roos, Michael Rothgang, Rajula Srivastava, James Sundstrom, Jeremy Tan and Christoph Thiele, read at commit [f7487cc9](https://github.com/fpvandoorn/carleson/tree/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78) (2026-11-17): one article for each of its 179 nodes whose Lean declarations it names and marks formalized, or in Mathlib. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

This paper is the blueprint underlying the Lean formalization of the proof of Carleson's classical result ([Carleson 1966](https://doi.org/10.1007/BF02392815)) asserting almost everywhere convergence of Fourier series of continuous functions. We break up the proof into two steps, a reduction of the classical result to a new theorem that appears in the sibling communication (Becker et al. 2025) and a proof of this new theorem, which is also detailed as blueprint in this paper. An early version of this blueprint was used to initiate the Lean formalization. During the formalization, many contributors elaborated the blueprint with minor corrections, modifications and extensions. The final version is presented here as a guide through the accompanying Lean code.

- [Introduction](introduction/README.md)
- [Proof of Metric Space Carleson, overview](proof-of-metric-space-carleson-overview/README.md)
- [Proof of Metric Space Carleson](proof-of-metric-space-carleson/README.md)
- [Proof of Finitary Carleson](proof-of-finitary-carleson/README.md)
- [Proof of discrete Carleson](proof-of-discrete-carleson/README.md)
- [Proof of the Antichain Operator Proposition](proof-of-the-antichain-operator-proposition/README.md)
- [Proof of the Forest Operator Proposition](proof-of-the-forest-operator-proposition/README.md)
- [Proof of the Hölder cancellative condition](proof-of-the-holder-cancellative-condition/README.md)
- [Proof of Vitali covering and Hardy–Littlewood](proof-of-vitali-covering-and-hardy-littlewood/README.md)
- [Two-sided Metric Space Carleson](two-sided-metric-space-carleson/README.md)
- [Proof of The Classical Carleson Theorem](proof-of-the-classical-carleson-theorem/README.md)
