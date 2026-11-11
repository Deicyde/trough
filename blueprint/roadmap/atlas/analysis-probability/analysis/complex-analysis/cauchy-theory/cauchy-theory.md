---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.FiniteZerosInDiscOfHolomorphicWanted.finite_zeros_in_ball_of_not_identically_zero, MathlibExt.Analysis.Complex.SupOnTangentCirclesLogConvexWanted.sq_sSup_norm_circle_one_le_mul, MathlibExt.Analysis.Complex.CasoratiWeierstrass.casoratiWeierstrass, MathlibExt.Analysis.Complex.IsolatedSingularityWanted.isolatedSingularity_trichotomy, MathlibExt.Analysis.Complex.LaurentSeriesWanted.laurentExpansion, MetaMathlibExt.looman_menchoff, MathlibExt.Analysis.Complex.ResidueTheoremWanted.residueTheorem_closedBall, MetaMathlibExt.schwarz_reflection
statement: formalized
---

# Complex integration, residues and singularities: its own results

8 results, 3 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html).

Contour integrals, Cauchy's theorem, residues, argument principle, Rouché, Laurent series, isolated singularities (Casorati–Weierstrass, great Picard), Schwarz reflection, Looman–Menchoff, normal families and local properties of holomorphic functions on discs and annuli.

## A holomorphic function not identically zero has finitely many zeros in a disc

Let
$P \in \mathbb{C}$ and $r > 0$, write $D(P,r)$ for the open disc and $\overline{D}(P,r)$ for the
closed disc of center $P$ and radius $r$, and let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic
on some open set containing $\overline{D}(P,r)$. If $f$ does not vanish identically on $D(P,r)$,
then $f$ has only finitely many zeros in $D(P,r)$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functions of a complex variable; General properties of functions of one complex variable), problem `ma_proofbench_l1_26`.

Stated but not proved: `MathlibExt.Analysis.Complex.FiniteZerosInDiscOfHolomorphicWanted.finite_zeros_in_ball_of_not_identically_zero` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/FiniteZerosInDiscOfHolomorphicWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/FiniteZerosInDiscOfHolomorphicWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#finite-zeros-in-ball-of-not-identically).

## A three-circles inequality for circles tangent at the origin

Let
$f:\mathbb{C}\to\mathbb{C}$ be an entire function and, for $r>0$, let
\[
A(r)=\sup\{\lvert f(z)\rvert:\lvert z-r\rvert=r\}.
\]
Then
\[
A(1)^{2}\le A(2)\,A\!\left(\frac{2}{3}\right).
\]

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Functions of a complex variable; Geometric function theory), problem `ma_proofbench_l2_99`.

Stated but not proved: `MathlibExt.Analysis.Complex.SupOnTangentCirclesLogConvexWanted.sq_sSup_norm_circle_one_le_mul` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/SupOnTangentCirclesLogConvexWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/SupOnTangentCirclesLogConvexWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#sq-s-sup-norm-circle-one-le-mul).

## Casorati–Weierstrass theorem

Let $c \in \mathbb{C}$, $r > 0$, and let
$f : \mathbb{C} \to \mathbb{C}$ be holomorphic on the punctured disc $0 < |z - c| < r$ and not
meromorphic at $c$ (that is, $c$ is neither a removable singularity nor a pole of $f$). Then the
image of the punctured disc $0 < |z - c| < r$ under $f$ is dense in $\mathbb{C}$.

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., isolated singularities.

Formalized by `MathlibExt.Analysis.Complex.CasoratiWeierstrass.casoratiWeierstrass`, a theorem declared in [MathlibExt/Analysis/Complex/CasoratiWeierstrass.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/CasoratiWeierstrass.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#casorati-weierstrass).

## Classification of isolated singularities

Let $c \in \mathbb{C}$, let $r > 0$, and let
$f : \mathbb{C} \to \mathbb{C}$ be holomorphic on the punctured disc
$\{z \in \mathbb{C} : 0 < |z - c| < r\}$. Then at least one of the following holds: there is a
function $g$ holomorphic on the disc $\{z \in \mathbb{C} : |z - c| < r\}$ that agrees with $f$ on
the punctured disc (removable singularity); or $|f(z)| \to \infty$ as $z \to c$ with $z \ne c$
(pole); or for every $r' > 0$ the image under $f$ of the punctured disc
$\{z \in \mathbb{C} : 0 < |z - c| < r'\}$ is dense in $\mathbb{C}$ (essential singularity,
Casorati–Weierstrass).

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., Ch. 4, §3.1 and §3.2 (removable singularities; zeros, poles and the Casorati-Weierstrass theorem).

Stated but not proved: `MathlibExt.Analysis.Complex.IsolatedSingularityWanted.isolatedSingularity_trichotomy` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/IsolatedSingularityWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/IsolatedSingularityWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#isolated-singularity-trichotomy).

## Laurent expansion on an annulus

Let $c \in \mathbb{C}$, let $r$ and $R$ be real numbers, and
let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic on the annulus
$A = \{z \in \mathbb{C} : r < |z - c| < R\}$. Then there are coefficients $a_n \in \mathbb{C}$
for $n \in \mathbb{Z}$ such that for every $z \in A$ the series
$\sum_{n \in \mathbb{Z}} a_n (z - c)^n$ is unconditionally summable with sum $f(z)$. Here
$0^n = 0$ for $n < 0$, which matters only at $z = c$ when $r < 0$.

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., Ch. 5, §1.3 (the Laurent series).

Stated but not proved: `MathlibExt.Analysis.Complex.LaurentSeriesWanted.laurentExpansion` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/LaurentSeriesWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/LaurentSeriesWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#laurent-expansion).

## Looman–Menchoff theorem

Let $s \subseteq \mathbb{C}$ be open and let
$f : \mathbb{C} \to \mathbb{C}$ be continuous on $s$. Write $u = \operatorname{Re} f$ and
$v = \operatorname{Im} f$ as functions of $z = x + iy$, and suppose that at every $z \in s$ the
partial derivatives $u_x(z)$, $u_y(z)$, $v_x(z)$, $v_y(z)$ exist and satisfy the Cauchy–Riemann
equations $u_x(z) = v_y(z)$ and $u_y(z) = -v_x(z)$. Then $f$ is complex differentiable on $s$.

Proof: Baire category gives a square with uniform axis-wise Lipschitz bounds on the
exceptional set. A Goursat rectangle estimate and Morera's theorem eliminate that set.

## Sources

- https://en.wikipedia.org/wiki/Looman%E2%80%93Menchoff_theorem (statement id `looman-menchoff-s1`, canonical name "Looman-Menchoff theorem").

Formalized by `MetaMathlibExt.looman_menchoff`, a theorem declared in [MathlibExt/Analysis/Complex/LoomanMenchoff.lean, line 1534](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/LoomanMenchoff.lean#L1534). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#looman-menchoff).

## Residue theorem on a disc

Let $c\in\mathbb{C}$ and $R>0$, and let $S$ be a finite set of
points of the open disc $\{z:|z-c|\lt R\}$. For each $s\in S$ let $r_s>0$ be such that the closed
disc $\{z:|z-s|\le r_s\}$ lies in $\{z:|z-c|\lt R\}$ and contains no point of $S$ other than $s$.
Let $f:\mathbb{C}\to\mathbb{C}$ be complex differentiable on $\{z:|z-c|\le R\}\setminus S$ and
integrable on the circle $|z-c|=R$ and on each circle $|z-s|=r_s$. Then, with all circles
oriented counterclockwise,

$$\oint_{|z-c|=R} f(z)\,dz=\sum_{s\in S}\oint_{|z-s|=r_s} f(z)\,dz.$$

Each integral on the right is $2\pi i$ times the residue of $f$ at $s$.

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., Ch. 4, §5.1 (the residue theorem).

Stated but not proved: `MathlibExt.Analysis.Complex.ResidueTheoremWanted.residueTheorem_closedBall` is written with `theorem_wanted` in [WantedExt/Analysis/Complex/ResidueTheoremWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Complex/ResidueTheoremWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#residue-theorem-closed-ball).

## Schwarz reflection principle

Let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic on the
open upper half-plane $\{z : \operatorname{Im} z > 0\}$, continuous on the closed upper half-plane
$\{z : \operatorname{Im} z \ge 0\}$, and real-valued on the real axis. Then there is an entire
function $g$ that agrees with $f$ on the closed upper half-plane and satisfies
$g(\bar z) = \overline{g(z)}$ for every $z \in \mathbb{C}$.

## Sources

- https://en.wikipedia.org/wiki/Schwarz_reflection_principle.

Formalized by `MetaMathlibExt.schwarz_reflection`, a theorem declared in [MathlibExt/Analysis/Complex/SchwarzReflection.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/SchwarzReflection.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html#schwarz-reflection).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complex integration, residues and singularities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory)
