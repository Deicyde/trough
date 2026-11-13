---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.IsTriangleFree, MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.triangleCount, MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.polynomialTriangleRemoval, MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.polynomialTriangleRemoval_holds
statement: formalized
---

# Polynomial triangle removal in vector spaces

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces/index.html).

## Triangle-free subsets of $\mathbb{F}_2^n$

A set $A \subseteq \mathbb{F}_2^n$ is
triangle-free if there are no $x, y \in A$ with $x + y \in A$ (the case $x = y$ is allowed).

Formalized by `MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.IsTriangleFree`, a definition declared in [WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces/index.html#is-triangle-free).

## Number of triangles in a subset of $\mathbb{F}_2^n$

For $A \subseteq \mathbb{F}_2^n$,
the triangle count of $A$ is the number of ordered pairs $(x, y) \in A \times A$ with
$x + y \in A$. Divided by $4^n$, it is the probability that $x, y, x + y \in A$ for independent
uniform $x, y \in \mathbb{F}_2^n$.

Formalized by `MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.triangleCount`, a definition declared in [WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces/index.html#triangle-count).

## Polynomial triangle removal in $\mathbb{F}_2^n$

This is the statement that there are
real constants $c > 0$ and $C > 0$ such that for every $n$, every $A \subseteq \mathbb{F}_2^n$
and every real $\varepsilon$ with $0 < \varepsilon \le 1$: if every triangle-free $B \subseteq A$
misses at least $\varepsilon 2^n$ elements of $A$, then the triangle count of $A$ is at least
$c \varepsilon^C 4^n$, that is, $\Pr_{x,y}[x, y, x + y \in A] \ge c \varepsilon^C$ for
independent uniform $x, y \in \mathbb{F}_2^n$.

This is Green's question as posed by O'Donnell (Problem 14); the answer is yes.

Formalized by `MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.polynomialTriangleRemoval`, a definition declared in [WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces/index.html#polynomial-triangle-removal).

## Polynomial triangle removal holds in $\mathbb{F}_2^n$

There are real constants $c > 0$
and $C > 0$ such that for every natural number $n$, every finite set $A \subseteq \mathbb{F}_2^n$
and every real number $\varepsilon$ with $0 < \varepsilon \le 1$ the following holds: if every
triangle-free $B \subseteq A$ misses at least $\varepsilon 2^n$ elements of $A$, then the
triangle count of $A$ is at least $c \varepsilon^C 4^n$. Here a set $B \subseteq \mathbb{F}_2^n$
is triangle-free when there are no $x, y \in B$ with $x + y \in B$ (the case $x = y$ is allowed),
and the triangle count of $A$ is the number of ordered pairs $(x, y) \in A \times A$ with
$x + y \in A$, so that it divided by $4^n$ is the probability that $x, y, x + y \in A$ for
independent uniform $x, y \in \mathbb{F}_2^n$.

This answers O'Donnell's Problem 14 in the affirmative. Fox and Lovász proved it with the
essentially tight exponent $C = 1 + 1/(5/3 - \log_2 3) \approx 13.239$.

## Sources

- R. O'Donnell, Open Problems in Analysis of Boolean Functions (2012), arXiv:1204.6447, Problem 14 (Triangle Removal in 𝔽₂ⁿ); resolution: J. Fox and L. M. Lovász, A tight bound for Green's arithmetic triangle removal lemma in vector spaces, Adv. Math. 321 (2017), 287-297, arXiv:1606.01230, Theorem 1: for 0 < ε < 1 and δ = (ε/3)^{C_p}, if X, Y, Z ⊆ 𝔽_pⁿ span fewer than δ N² triangles (N = pⁿ) then removing εN elements of X ∪ Y ∪ Z kills all triangles; C₂ = 1 + 1/(5/3 - log₂ 3) ≈ 13.239 (applied with X = Y = Z = A and p = 2; the case ε = 1 follows from ε < 1), https://arxiv.org/abs/1606.01230.

Stated but not proved: `MathlibExt.Combinatorics.TriangleRemovalVectorSpaceAMR127Problem0013Wanted.polynomialTriangleRemoval_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/TriangleRemovalVectorSpaceAMR127Problem0013Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces/index.html#polynomial-triangle-removal-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polynomial triangle removal in vector spaces](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/progressions-dense-sets/polynomial-triangle-removal-in-vector-spaces)
