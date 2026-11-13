---
declaration: section
origin: cited
lean: MetaMathlibExt.isoperimetric_inequality, MathlibExt.Geometry.Euclidean.JungWanted.jung, MetaMathlibExt.kirchberger, MathlibExt.Geometry.Convex.RadoCenterpointWanted.rado_centerpoint, MathlibExt.Geometry.Convex.TverbergWanted.tverberg, MathlibExt.Geometry.ScottishBook68Wanted.ulamFlatSectionsConvex
statement: formalized
---

# Convex geometry: its own results

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html).

Convex sets and convex bodies in Euclidean space: Helly-type and Radon-type theorems, partitions, sections, valuations and linear optimization over polyhedra.

## Isoperimetric inequality

Let $g$ be a continuous, $1$-periodic, Lipschitz map from
$\mathbb{R}$ to the Euclidean plane $\mathbb{R}^2$ that is injective on $[0, 1)$, so that its
image $C = g(\mathbb{R})$ is a simple closed curve, and suppose $C$ has finite
one-dimensional Hausdorff measure. Let $U \subseteq \mathbb{R}^2$ be a bounded, connected open
set whose boundary is $C$. Let $L$ be the one-dimensional Hausdorff measure of $C$ (its
length) and $A$ the Lebesgue measure of $U$ (its area). Then $4 \pi A \le L^2$, and
$4 \pi A = L^2$ if and only if $C$ is a circle, that is, $C = \{x : \lVert x - c \rVert = r\}$
for some point $c \in \mathbb{R}^2$ and some real $r > 0$.

## Sources

- https://en.wikipedia.org/wiki/Isoperimetric_inequality.

Stated but not proved: `MetaMathlibExt.isoperimetric_inequality` is written with `theorem_wanted` in [WantedExt/Analysis/Geometry/IsoperimetricInequalityWanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Geometry/IsoperimetricInequalityWanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html#isoperimetric-inequality).

## Jung's theorem

Let $n \ge 1$ and let $s$ be a bounded subset of the Euclidean space
$\mathbb{R}^n$ with diameter $\operatorname{diam} s$. Then there is a point $c \in \mathbb{R}^n$
such that $s$ is contained in the closed ball with center $c$ and radius
$\sqrt{n / (2(n + 1))} \cdot \operatorname{diam} s$.

## Sources

- H. Jung, Über die kleinste Kugel, die eine räumliche Figur einschließt, J. Reine Angew. Math. 123 (1901) 241–257 original theorem; D. Gale sharp Euclidean formulation; standard modern reference M. Berger, Geometry I & II.

Formalized by `MathlibExt.Geometry.Euclidean.JungWanted.jung`, a theorem declared in [MathlibExt/Geometry/Euclidean/Jung.lean, line 772](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/Jung.lean#L772). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html#jung).

## Kirchberger's theorem

Let $A$ and $B$ be finite sets of points in $\mathbb{R}^d$. Then $A$
and $B$ are strictly separated by a hyperplane, that is, there are a nonzero vector
$w \in \mathbb{R}^d$ and a real number $\beta$ with $\langle w, a \rangle < \beta$ for all $a \in A$
and $\beta < \langle w, c \rangle$ for all $c \in B$, if and only if for every set
$C \subseteq A \cup B$ of at most $d + 2$ points, the sets $A \cap C$ and $B \cap C$ are strictly
separated by a hyperplane in the same sense.

Proof: The reverse implication applies Helly's theorem to tagged strict half-spaces in one higher
dimension, following the route of Rademacher and Schoenberg (1950) from Kirchberger (1903).

## Sources

- https://en.wikipedia.org/wiki/Kirchberger%27s_theorem.
- Paul Kirchberger, "Über Tchebychefsche Annäherungsmethoden," Mathematische Annalen 57 (1903), 509–540, DOI 10.1007/BF01445182, https://doi.org/10.1007/BF01445182.

Formalized by `MetaMathlibExt.kirchberger`, a theorem declared in [MathlibExt/Geometry/Convex/Kirchberger.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Kirchberger.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html#kirchberger).

## Rado's centerpoint theorem

Let $n \ge 1$ and let $p_1, \dots, p_n$ be points of
$\mathbb{R}^d$, not necessarily distinct. Then some point $x$ in the convex hull of
$\{p_1, \dots, p_n\}$ has at least $n/(d+1)$ of the points in every closed halfspace containing
it: for all $v \in \mathbb{R}^d$ and $t \in \mathbb{R}$ with $\langle v, x \rangle \le t$, the
number of indices $i$ with $\langle v, p_i \rangle \le t$ is at least $n/(d+1)$.

## Sources

- R. Rado, J. London Math. Soc. s1-21 (1946), 291-300, DOI 10.1112/jlms/s1-21.4.291.

Formalized by `MathlibExt.Geometry.Convex.RadoCenterpointWanted.rado_centerpoint`, a theorem declared in [MathlibExt/Geometry/Convex/RadoCenterpoint.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/RadoCenterpoint.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html#rado-centerpoint).

## Tverberg's theorem

Let $d, r$ be natural numbers with $r \ge 1$ and let $N = (d+1)(r-1)+1$.
For any points $p_1, \dots, p_N$ of $\mathbb{R}^d$, not necessarily distinct, there are pairwise
disjoint sets $P_1, \dots, P_r \subseteq \{1, \dots, N\}$ whose union is $\{1, \dots, N\}$ and a
point $x \in \mathbb{R}^d$ that lies in the convex hull of $\{p_i : i \in P_j\}$ for every $j$.

## Sources

- H. Tverberg, J. London Math. Soc. s1-41 (1966), 123-128, DOI 10.1112/jlms/s1-41.1.123.

Formalized by `MathlibExt.Geometry.Convex.TverbergWanted.tverberg`, a theorem declared in [MathlibExt/Geometry/Convex/Tverberg.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/Tverberg.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html#tverberg).

## Ulam's flat-sections problem in dimension three

Let $K \subseteq \mathbb{R}^3$ be a compact
set homeomorphic to the closed unit ball. Suppose that for every nonzero continuous linear
functional $F : \mathbb{R}^3 \to \mathbb{R}$ and every real $c$ such that the plane
$\{x : F(x) = c\}$ meets the interior of $K$, the intersection of this plane with the boundary
(frontier) of $K$ is homeomorphic to the unit circle. Then $K$ is convex.

Only planes meeting the interior of $K$ are constrained: a supporting plane can meet the
boundary in a single point, as the plane $\{x : x_1 = 1\}$ does for the closed unit ball, so
requiring a circle for every plane would make the hypothesis impossible. Allowing empty or
one-point sections for the other planes would still exclude convex bodies such as the cube,
whose face planes meet its boundary in a square.

## Sources

- S. Ulam, Problem 68 of the Scottish Book, asking to prove that a manifold whose every hyperplane section of its boundary is a sphere is convex. Montejano gave a complete solution, settling the problem affirmatively: L. Montejano, "About a problem of Ulam concerning flat sections of manifolds", Comment. Math. Helv. 65 (1990), 462–473; see also Montejano, "Three old problems from the Polish school of mathematics", Bol. Soc. Mat. Mex. (3) 30 (2024).

Stated but not proved: `MathlibExt.Geometry.ScottishBook68Wanted.ulamFlatSectionsConvex` is written with `theorem_wanted` in [WantedExt/Geometry/ScottishBook68Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ScottishBook68Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html#ulam-flat-sections-convex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convex geometry](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/convex-geometry)
