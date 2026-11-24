# Polynomial Freiman-Ruzsa

[teorth/pfr](https://github.com/teorth/pfr) says in its README:

> The original purpose of this repository is to hold a Lean4 formalization of [the proof of the Polynomial Freiman-Ruzsa (PFR) conjecture](https://arxiv.org/abs/2311.05762) of Katalin Marton (see also [this blog post](https://terrytao.wordpress.com/2023/11/13/on-a-conjecture-of-marton)).

Its blueprint, read at commit [1899ce8e](https://github.com/teorth/pfr/tree/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4) (2026-11-23): one article for each of its 213 nodes whose Lean declarations it names and marks formalized, or in Mathlib. Its other 6 nodes have no article, and a section of only those is left out: the map records what the project contains, not what it plans. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

- [Applications of Jensen's inequality](applications-of-jensens-inequality/README.md)
- [Shannon entropy inequalities](shannon-entropy-inequalities/README.md)
- [Entropic Ruzsa calculus](entropic-ruzsa-calculus/README.md)
- [The 100% version of PFR](the-100-version-of-pfr/README.md)
- [The Fibring lemma](the-fibring-lemma/README.md)
- [Entropy version of PFR](entropy-version-of-pfr/README.md)
- [Proof of PFR](proof-of-pfr/README.md)
- [Improving the exponents](improving-the-exponents/README.md)
- [Homomorphism version of PFR](homomorphism-version-of-pfr/README.md)
- [Approximate homomorphism version of PFR](approximate-homomorphism-version-of-pfr/README.md)
- [Weak PFR over the integers](weak-pfr-over-the-integers/README.md)
- [The $m$-torsion case](the-m-torsion-case/README.md)
- [Further improvement to exponent](further-improvement-to-exponent/README.md)
