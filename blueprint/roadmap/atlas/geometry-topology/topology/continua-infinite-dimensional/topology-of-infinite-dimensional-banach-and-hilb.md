---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ScottishBook167Wanted.ScottishBookProblem167Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook167Wanted.ulam167_refuted, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook35Wanted.ProjectiveHilbertSpace, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook35Wanted.ProjectiveHilbertSpaceHomeomorphicToHilbertSpace, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook35Wanted.projective_hilbert_space_not_homeomorphic_to_hilbert_space, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook36Wanted.hilbertBallRetractsOntoSphere, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook7Wanted.ScottishBookProblem7Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook7Wanted.closedConvexSetsHomeomorphic_refuted
statement: formalized
---

# Topology of infinite-dimensional Banach and Hilbert spaces

8 results, 4 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html).

## Scottish Book Problem 167

Ulam's claim that for every infinite-dimensional real Hilbert
space $H$ with unit sphere $S = \{p \in H : \|p\| = 1\}$, every $n \in \mathbb{N}$, all
continuous functions $f_1, \dots, f_n : S \to \mathbb{R}$ and every continuous map
$T : S \to S$, there is a point $p_0 \in S$ with $f_i(T(p_0)) = f_i(p_0)$ for every $i$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook167Wanted.ScottishBookProblem167Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook167Wanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook167Wanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#scottish-book-problem167-claim).

## Negative answer to Scottish Book Problem 167

Ulam's claim in Problem 167 is false: there
are an infinite-dimensional real Hilbert space $H$ with unit sphere $S$, a number
$n \in \mathbb{N}$, continuous functions $f_1, \dots, f_n : S \to \mathbb{R}$ and a continuous map
$T : S \to S$ such that no point $p_0 \in S$ satisfies $f_i(T(p_0)) = f_i(p_0)$ for every $i$.

The claim fails already for one function.

## Sources

- S. Ulam, Problem 167 of the Scottish Book; refuted via V. Klee's homeomorphism of the Hilbert sphere onto the whole Hilbert space: composing that homeomorphism with a translation gives a continuous `T` and a continuous `f` with no point `p0` satisfying `f (T p0) = f p0`. See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook167Wanted.ulam167_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook167Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook167Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#ulam167-refuted).

## Projective Hilbert space

Let $E$ be a normed additive commutative group, in practice a
real inner product space. The projective Hilbert space of $E$ is the quotient of the unit sphere
$\{x \in E : \|x\| = 1\}$ by the relation identifying each $x$ with $-x$. Its points are the
antipodal pairs $\{x, -x\}$ of unit vectors, that is, the diameters of the unit sphere.

When $E$ is a real inner product space, it carries the quotient topology of the unit sphere.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook35Wanted.ProjectiveHilbertSpace`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook35Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook35Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#projective-hilbert-space).

## Projective Hilbert space homeomorphic to the space itself

For a real inner product
space $E$, the statement that the projective Hilbert space of $E$, the unit sphere
$\{x \in E : \|x\| = 1\}$ with each $x$ identified with $-x$ and given the quotient topology,
is homeomorphic to $E$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook35Wanted.ProjectiveHilbertSpaceHomeomorphicToHilbertSpace`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook35Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook35Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#projective-hilbert-space-homeomorphic-to).

## Projective Hilbert space is not homeomorphic to Hilbert space

Let $E$ be an
infinite-dimensional real Hilbert space. Then the projective Hilbert space of $E$, the unit
sphere $\{x \in E : \|x\| = 1\}$ with each $x$ identified with $-x$ and given the quotient
topology, is not homeomorphic to $E$.

This answers Ulam's Problem 35 of the Scottish Book in the negative. The projective space is the
standard model of the space of diameters of the unit sphere with the Hausdorff metric. Hilbert
space is contractible, hence simply connected, while projective Hilbert space is not, its
fundamental group being $\mathbb{Z}/2$ via the double covering by the unit sphere.

## Sources

- S. Ulam, Problem 35 of the Scottish Book; see the commentary of Holsztynski in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015), and the Hilbert-manifold classification by homotopy type.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook35Wanted.projective_hilbert_space_not_homeomorphic_to_hilbert_space` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook35Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook35Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#projective-hilbert-space-not-homeomorphi).

## Retraction onto the unit sphere of Hilbert space

Let $E$ be an infinite-dimensional real
Hilbert space and let $S = \{x \in E : \|x\| = 1\}$ be its unit sphere. Then there is a
continuous map $f : E \to E$ such that $f(x) \in S$ for every $x \in E$ and $f(x) = x$ for every
$x \in S$.

Restricting $f$ to the closed unit ball gives a retraction of the ball onto $S$; conversely, a
retraction $r$ of the closed unit ball onto $S$ extends to all of $E$ by
$f(x) = r(x / \max(1, \|x\|))$. In finite dimensions no such map exists, by the Brouwer
no-retraction theorem, so the infinite-dimensional hypothesis is essential.

## Sources

- S. Ulam, Problem 36 of the Scottish Book, asking whether there is a retraction of the closed unit ball of Hilbert space onto its boundary; the answer is affirmative, see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015), and the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867), which notes that the unit sphere of a Hilbert space is homeomorphic to the whole space.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook36Wanted.hilbertBallRetractsOntoSphere` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook36Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook36Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#hilbert-ball-retracts-onto-sphere).

## Scottish Book Problem 7 (Mazur–Banach)

The claim that in every real Banach space $E$,
any two closed convex subsets $A, B \subseteq E$ whose linear spans are infinite-dimensional are
homeomorphic, with the subspace topologies.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook7Wanted.ScottishBookProblem7Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook7Wanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook7Wanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#scottish-book-problem7-claim).

## Scottish Book Problem 7 fails: closed convex sets need not be homeomorphic

The Scottish Book
Problem 7 claim is false: there are a real Banach space $E$ and closed convex subsets
$A, B \subseteq E$, each with infinite-dimensional linear span, that are not homeomorphic.

For example, a compact infinite-dimensional closed convex set, such as the Hilbert cube, is not
homeomorphic to a noncompact one, such as the whole space, since compactness is a topological
invariant.

## Sources

- S. Mazur and S. Banach, Problem 7 of the Scottish Book; T. Banakh's observation as reported in the 2026 survey "90+ years of the Scottish Book" (arXiv:2603.27867). The modified classification problem was solved for Frechet spaces by Banakh-Cauty, Studia Mathematica 205 (2011) 1-11.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook7Wanted.closedConvexSetsHomeomorphic_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook7Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook7Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html#closed-convex-sets-homeomorphic-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Topology of infinite-dimensional Banach and Hilbert spaces](https://deicyde.github.io/atlas-lean/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/continua-infinite-dimensional/topology-of-infinite-dimensional-banach-and-hilb)
