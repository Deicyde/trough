---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.GeometricWanted.banachMazur_embedding, MathlibExt.Analysis.FunctionalAnalysis.BanachStoneWanted.banachStone_real, MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.bishop_phelps, MathlibExt.Analysis.FunctionalAnalysis.DaugavetWanted.daugavet, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook122Wanted.dvoretzky_rogers_unconditional_not_absolute, MathlibExt.Analysis.FunctionalAnalysis.GrothendieckInequalityWanted.grothendieck_inequality_real, MathlibExt.Analysis.FunctionalAnalysis.MilmanPettisWanted.milman_pettis, MathlibExt.Analysis.FunctionalAnalysis.BanachSaksWanted.banach_saks
statement: formalized
---

# Geometry of Banach spaces: its own results

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html).

Convexity and smoothness of norms (uniform convexity, Kadec–Klee, Birkhoff–James), extreme points of balls, Auerbach and Schauder bases, approximation property, isometries (Banach–Stone, Mazur–Ulam), Banach–Mazur, Dvoretzky–Rogers, Grothendieck, Rademacher type, Daugavet, Bishop–Phelps.

## Banach–Mazur embedding theorem

Every separable real Banach space $E$ admits a linear
isometric embedding $e \colon E \to C([0, 1], \mathbb{R})$ into the space of continuous real
functions on $[0, 1]$ with the supremum norm, such that the range of $e$ is closed.

## Sources

- S. Banach and S. Mazur 1932 embedding theorem; Banach, Theorie des operations lineaires; Henson-Michalewski, separable Banach as universal space; Lean states separable real Banach case with `E →ₗᵢ[ℝ] C(Icc 0 1, ℝ)` and `IsClosed (range)`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.GeometricWanted.banachMazur_embedding`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Geometric.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Geometric.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#banach-mazur-embedding).

## Banach–Stone theorem for real scalars

Let $X$ and $Y$ be compact Hausdorff spaces, and let
$C(X, \mathbb{R})$ and $C(Y, \mathbb{R})$ be the real Banach spaces of continuous real functions
on them with the supremum norm. If there is a surjective linear isometry from $C(X, \mathbb{R})$
onto $C(Y, \mathbb{R})$, then $X$ and $Y$ are homeomorphic.

## Sources

- S. Banach, Theorie des operations lineaires, 1932 and M. Stone, Trans. Amer. Math. Soc. 41 (1937) 375-381; textbook Semadeni, Banach Spaces of Continuous Functions, 1971; Lean states compact Hausdorff case with Banach-space linear isometric isomorphism implies homeomorphism, real coefficient field specialization.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachStoneWanted.banachStone_real`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BanachStone.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BanachStone.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#banach-stone-real).

## Bishop–Phelps theorem

Let $E$ be a Banach space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, with dual space $E^*$. The functionals that attain their norm on the closed unit
ball, that is, the $f \in E^*$ such that $|f(x)| = \|f\|$ for some $x \in E$ with
$\|x\| \le 1$, form a dense subset of $E^*$ in the norm topology.

## Sources

- E. Bishop and R. R. Phelps, Bull. Amer. Math. Soc. 67 (1961) 97-98 and Pacific J. Math. 1961; Bollobas quantitative version; Lean states `RCLike` Banach case as density of attaining functionals.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.bishop_phelps`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BishopPhelps.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BishopPhelps.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#bishop-phelps).

## Daugavet's theorem for compact operators

Let $C[0,1]$ be the real Banach space of continuous
functions $[0,1] \to \mathbb{R}$ with the supremum norm, and let $I$ be the identity operator on
it. Every compact bounded linear operator $T : C[0,1] \to C[0,1]$ satisfies
$\|I + T\| = 1 + \|T\|$, where the norms are operator norms.

## Sources

- I. K. Daugavet, Izv. Vyssh. Uchebn. Zaved. Matematika 1963; Kadets et al., 1980s Daugavet property; Werner, Recent progress on Daugavet property, 2001; Lean states `C(Icc 0 1, ℝ)` compact-operator specialization of the general Daugavet property `‖Id+T‖=1+‖T‖`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.DaugavetWanted.daugavet`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Daugavet.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/Daugavet.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#daugavet).

## Dvoretzky–Rogers theorem

Every infinite-dimensional real Banach space $E$ contains a series
that converges unconditionally but not absolutely: there is a sequence $(x_n)_{n \ge 0}$ in $E$
such that the rearranged series $\sum_n x_{\sigma(n)}$ converges for every permutation $\sigma$
of $\mathbb{N}$, while $\sum_n \lVert x_n \rVert$ diverges.

## Sources

- S. Mazur and W. Orlicz, Problem 122 of the Scottish Book; A. Dvoretzky and C. A. Rogers, "Absolute and unconditional convergence in normed linear spaces", Proc. Natl. Acad. Sci. USA 36 (1950), 192-197.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook122Wanted.dvoretzky_rogers_unconditional_not_absolute` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook122Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook122Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#dvoretzky-rogers-unconditional-not-absol).

## Grothendieck's inequality (real case)

There is a constant $K > 0$ such that for all
$m, n \in \mathbb{N}$, every real $m \times n$ matrix $A = (a_{ij})$, every real Hilbert space $H$
and all vectors $x_1, \dots, x_m, y_1, \dots, y_n \in H$ of norm at most $1$, there are signs
$\varepsilon_1, \dots, \varepsilon_m, \delta_1, \dots, \delta_n \in \{1, -1\}$ such that
$\bigl|\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} \langle x_i, y_j \rangle\bigr| \le
K \bigl|\sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} \varepsilon_i \delta_j\bigr|$.

## Sources

- A. Grothendieck, Resume de la theorie metrique des produits tensoriels topologiques, Bol. Soc. Mat. Sao Paulo 8 (1953) 1-79, inequality; Pisier, Grothendieck's theorem past and present, 2012; Lean states real finite-matrix scalarized form with `Fin`-indexed unit vectors and `±1` signs, existential universal constant `K`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.GrothendieckInequalityWanted.grothendieck_inequality_real`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/GrothendieckInequality.lean, line 935](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/GrothendieckInequality.lean#L935). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#grothendieck-inequality-real).

## Milman–Pettis theorem

Let $E$ be a uniformly convex Banach space over $\mathbb{K} = \mathbb{R}$
or $\mathbb{C}$, and let $E^*$ be the space of continuous linear functionals on $E$. Then every
continuous linear functional $\Phi$ on $E^*$ is evaluation at a point: there is $x \in E$ with
$\Phi(f) = f(x)$ for every $f \in E^*$.

## Sources

- D. Milman, C. R. (Doklady) Acad. Sci. URSS 18 (1938) and B. Pettis, Duke Math. J. 1939, Milman-Pettis theorem that uniformly convex Banach spaces are reflexive; Clarkson uniform convexity 1936; Lean states `RCLike` uniformly convex complete case via double-dual evaluation surjectivity.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.MilmanPettisWanted.milman_pettis`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/MilmanPettis.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/MilmanPettis.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#milman-pettis).

## Banach–Saks theorem for uniformly convex spaces

Let $E$ be a uniformly convex real Banach
space and let $(x_n)_{n \in \mathbb{N}}$ be a bounded sequence in $E$. Then there are a strictly
increasing map $\varphi : \mathbb{N} \to \mathbb{N}$ and a point $y \in E$ such that the Cesàro
means $\frac{1}{n} \sum_{i=0}^{n-1} x_{\varphi(i)}$ converge to $y$ in norm as $n \to \infty$.

## Sources

- S. Banach and S. Saks, Studia Math. 2 (1930) 51-57; uniformly convex form and property due to Kakutani, 1939; textbook Diestel, Sequences and Series in Banach Spaces; Lean gives uniformly convex real Banach specialization with explicit `StrictMono φ` and norm-convergent Cesàro means.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachSaksWanted.banach_saks`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/BanachSaks.lean, line 585](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/BanachSaks.lean#L585). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html#banach-saks).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geometry of Banach spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces)
