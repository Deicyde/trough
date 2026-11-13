---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.StrongMasonWanted.Combinatorics.StrongMason.independentSetCount, MathlibExt.Combinatorics.StrongMasonWanted.Combinatorics.StrongMason.strong_mason_conjecture
statement: formalized
---

# Mason's conjectures on independent sets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/mason-s-conjectures-on-independent-sets/index.html).

## Number of independent sets of a given size

For a finite matroid $M$ and a natural
number $k$, this is the number of independent sets of $M$ with exactly $k$ elements.

Formalized by `MathlibExt.Combinatorics.StrongMasonWanted.Combinatorics.StrongMason.independentSetCount`, a definition declared in [WantedExt/Combinatorics/StrongMasonWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StrongMasonWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/mason-s-conjectures-on-independent-sets/index.html#independent-set-count).

## The strong Mason conjecture

Let $M$ be a finite matroid whose ground set has $n$
elements, and for each $j$ let $I_j$ be the number of independent sets of $M$ with $j$ elements.
Then for every natural number $k$ with $0 < k < n$,

$$I_{k-1} \, I_{k+1} \, (k+1) \, (n-k+1) \le I_k^2 \, k \, (n-k).$$

Equivalently, the sequence $I_k / \binom{n}{k}$ is log-concave for $0 \le k \le n$.

## Sources

- P. Branden and J. Huh, 'Lorentzian polynomials', Ann. of Math. 192 (2020), 821-891, Theorem 4.14, https://doi.org/10.4007/annals.2020.192.3.4; independently N. Anari, K. Liu, S. Oveis Gharan, and C. Vinzant, 'Log-concave polynomials III: Mason's ultra-log-concavity conjecture for independent sets of matroids', https://arxiv.org/abs/1811.01600. Problem `strong_mason_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.StrongMasonWanted.Combinatorics.StrongMason.strong_mason_conjecture` is written with `theorem_wanted` in [WantedExt/Combinatorics/StrongMasonWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/StrongMasonWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/mason-s-conjectures-on-independent-sets/index.html#strong-mason-conjecture).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mason's conjectures on independent sets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/matroid-theory/mason-s-conjectures-on-independent-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/matroid-theory/mason-s-conjectures-on-independent-sets)
