---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.chainPolynomial, MathlibExt.Combinatorics.DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.distributiveLatticeChainPolynomialRealRooted, MathlibExt.Combinatorics.DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.distributiveLatticeChainPolynomialRealRooted_refuted
statement: formalized
---

# Chain polynomials of posets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/chain-polynomials-of-posets/index.html).

## Chain polynomial

For a finite partially ordered set $P$ and each natural number $k$, let
$c_k(P)$ be the number of $k$-element chains of $P$, that is, of $k$-element subsets of $P$ any two
of whose elements are comparable; in particular $c_0(P) = 1$, counting the empty chain. The chain
polynomial of $P$ is the polynomial $C(P, t) = \sum_{k \ge 0} c_k(P)\, t^k$ with integer
coefficients.

Formalized by `MathlibExt.Combinatorics.DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.chainPolynomial`, a definition declared in [WantedExt/Combinatorics/DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/chain-polynomials-of-posets/index.html#chain-polynomial).

## Stanley's Problem 20' on chain polynomials of distributive lattices

The proposition that
for every finite distributive lattice $L$, every complex root of the chain polynomial $C(L, t)$ is
real, where $C(L, t) = \sum_{k \ge 0} c_k(L)\, t^k$ and $c_k(L)$ is the number of $k$-element
chains of $L$.

Formalized by `MathlibExt.Combinatorics.DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.distributiveLatticeChainPolynomialRealRooted`, a definition declared in [WantedExt/Combinatorics/DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/chain-polynomials-of-posets/index.html#distributive-lattice-chain-polynomial-re).

## Stanley's Problem 20' has a negative answer

It is not true that for every finite
distributive lattice $L$ every complex root of the chain polynomial $C(L, t)$ is real, where
$C(L, t) = \sum_{k \ge 0} c_k(L)\, t^k$ and $c_k(L)$ is the number of $k$-element chains of $L$.

For a finite poset $P$ let $J(P)$ be the distributive lattice of its order ideals, and for a
naturally labeled $P$ let $W(P, x) = \sum_{\sigma} x^{\operatorname{des}(\sigma)}$, the sum over
the linear extensions $\sigma$ of $P$, where $\operatorname{des}(\sigma)$ is the number of descents
of $\sigma$. For naturally labeled $P$, real-rootedness of $C(J(P), t)$ is equivalent to that of
$W(P, x)$ (Stanley's text before Problem 20', after Brenti), and Stembridge's naturally labeled
$17$-element posets $P$ have polynomials $W(P, x)$ with non-real zeros, so their lattices $J(P)$
have chain polynomials with non-real zeros.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics (1999), Problem 20' (chain polynomial of a finite distributive lattice); resolution: Stanley, Positivity Problems (1999), text before Problem 20', citing F. Brenti, Mem. Amer. Math. Soc. 413 (1989), Conj. 3; J. R. Stembridge, Counterexamples to the poset conjectures of Neggers, Stanley, and Stembridge, Trans. Amer. Math. Soc. 359 (2007), 1115-1128; restated in C. A. Athanasiadis and K. Kalampogia-Evangelinou, Chain enumeration, partition lattices and polynomials with only real roots, arXiv:2205.03796, Introduction, Stanley: "When P is natural it can be shown [19, Conj. 3] that Problem 20 is equivalent to the following" (Problem 20', with L = J(P)); Stembridge, Introduction: naturally labeled posets on 17 vertices with non-real W-zeros; Athanasiadis–Kalampogia-Evangelinou: for finite distributive lattices the question is equivalent to the naturally labeled poset conjecture of Neggers, "finally disproved by Stembridge", https://arxiv.org/abs/2205.03796.

Stated but not proved: `MathlibExt.Combinatorics.DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.distributiveLatticeChainPolynomialRealRooted_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/DistributiveLatticeChainPolynomialAMR156Problem0021Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/chain-polynomials-of-posets/index.html#distributive-lattice-chain-polynomial-re-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chain polynomials of posets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/partially-ordered-sets/chain-polynomials-of-posets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/partially-ordered-sets/chain-polynomials-of-posets)
