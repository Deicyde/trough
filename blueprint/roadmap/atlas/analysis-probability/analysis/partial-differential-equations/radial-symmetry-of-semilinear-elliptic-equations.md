---
declaration: section
origin: cited
lean: MathlibExt.Analysis.RadialSymmetryWanted.Analysis.PDE.SolvesSemilinearPoisson, MathlibExt.Analysis.RadialSymmetryWanted.Analysis.PDE.semilinear_poisson_radial_symmetry
statement: formalized
---

# Radial symmetry of semilinear elliptic equations

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/radial-symmetry-of-semilinear-elliptic-equations/index.html).

## Semilinear Poisson problem on the unit ball

Let $n$ be a natural number, let
$f : \mathbb{R} \to \mathbb{R}$, and let $u : \mathbb{R}^n \to \mathbb{R}$ be a function on
Euclidean space. Then $u$ solves the semilinear Poisson problem for $f$ if
$-\Delta u(x) = f(u(x))$ for every $x$ in the open unit ball and $u(x) = 0$ for every $x$ on the
unit sphere.

The definition imposes no differentiability on $u$; regularity is assumed separately where it is
needed.

Formalized by `MathlibExt.Analysis.RadialSymmetryWanted.Analysis.PDE.SolvesSemilinearPoisson`, a definition declared in [WantedExt/Analysis/RadialSymmetryWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RadialSymmetryWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/radial-symmetry-of-semilinear-elliptic-equations/index.html#solves-semilinear-poisson).

## Radial symmetry of positive solutions of the semilinear Poisson problem

Let $n \ge 1$,
let $f : \mathbb{R} \to \mathbb{R}$ be Lipschitz, and let $u : \mathbb{R}^n \to \mathbb{R}$ be a
function on Euclidean space that is $C^2$ on the closed unit ball $\overline{B}$. Suppose that $u$
solves the semilinear Poisson problem for $f$, that is, $-\Delta u = f(u)$ on the open unit ball
$B$ and $u = 0$ on the unit sphere, and that $u > 0$ on $B$. Then there is a function
$v : \mathbb{R} \to [0, \infty)$ that is strictly decreasing on $[0, 1]$ and satisfies
$u(x) = v(\|x\|)$ for every $x \in \overline{B}$.

## Sources

- B. Gidas, W. M. Ni, and L. Nirenberg, Symmetry and related properties via the maximum principle, Comm. Math. Phys. 68 (1979), 209-243. Also stated as Theorem 2 (Radial symmetry) in L. C. Evans, Partial Differential Equations, Section 9 on nonvariational techniques. Problem `semilinear_poisson_radial_symmetry` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RadialSymmetryWanted.Analysis.PDE.semilinear_poisson_radial_symmetry` is written with `theorem_wanted` in [WantedExt/Analysis/RadialSymmetryWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RadialSymmetryWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/radial-symmetry-of-semilinear-elliptic-equations/index.html#semilinear-poisson-radial-symmetry).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Radial symmetry of semilinear elliptic equations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/radial-symmetry-of-semilinear-elliptic-equations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/partial-differential-equations/radial-symmetry-of-semilinear-elliptic-equations)
