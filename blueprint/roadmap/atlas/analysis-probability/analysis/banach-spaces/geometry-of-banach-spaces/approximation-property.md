---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.HasApproximationProperty, MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.hasApproximationProperty_of_finiteDimensional, MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.hasApproximationProperty_of_schauderBasis, MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.HasApproximationProperty.of_continuousLinearEquiv, MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.HasApproximationProperty.of_complemented, MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.hasApproximationProperty_of_hilbertBasis, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook153Wanted.ScottishBookProblem153Claim, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook153Wanted.mazur153_refuted
statement: formalized
---

# Approximation property

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html).

## Approximation property

A normed space has the **approximation property** if, on every compact
set, the identity operator is a uniform limit of finite-rank continuous
linear operators.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.HasApproximationProperty`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#has-approximation-property).

## Finite-dimensional spaces have the approximation property

Finite-dimensional spaces have the approximation property: the identity
operator is itself finite-rank.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.hasApproximationProperty_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#has-approximation-property-of-finite-dim).

## Banach spaces with a Schauder basis have the approximation property

A Banach space with a Schauder basis has the approximation property.
The partial-sum projections are finite-rank, converge pointwise to the
identity, and are uniformly bounded by the Banach–Steinhaus theorem
(`SchauderBasis.exists_norm_proj_le`); pointwise convergence plus uniform
boundedness gives uniform convergence on compact sets via a finite
`ε`-net argument.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.hasApproximationProperty_of_schauderBasis`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#has-approximation-property-of-schauder-b).

## Approximation property is invariant under linear isomorphism

The approximation property is preserved under continuous linear
equivalence: conjugate a finite-rank approximant by the equivalence.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.HasApproximationProperty.of_continuousLinearEquiv`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#of-continuous-linear-equiv).

## Approximation property passes to complemented subspaces

The approximation property passes to complemented subspaces: if `P` is a
continuous projection onto the submodule `F`, restrict a finite-rank
approximant on the ambient space via `P`. The key point is that `P` fixes
every point of `F`, so `P (S x) - x = P (S x - x)` for `x ∈ F`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.HasApproximationProperty.of_complemented`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#of-complemented).

## Separable Hilbert spaces have the approximation property

A Hilbert space with a Hilbert basis indexed by `ℕ` has the approximation
property, via the associated Schauder basis
(`HilbertBasis.toSchauderBasis`).

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ApproximationProperty.hasApproximationProperty_of_hilbertBasis`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/ApproximationProperty.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#has-approximation-property-of-hilbert-ba).

## Mazur's Problem 153

The claim of Mazur's Problem 153 from the Scottish Book, in its
original form: for every continuous function $f \colon [0,1]^2 \to \mathbb{R}$ and every real
$\varepsilon > 0$ there are a natural number $n$, points
$a_1, \dots, a_n, b_1, \dots, b_n \in [0,1]$ and real numbers $c_1, \dots, c_n$ such that

$$\Bigl| f(x, y) - \sum_{k=1}^n c_k \, f(a_k, y) \, f(x, b_k) \Bigr| \le \varepsilon$$

for all $x, y \in [0,1]$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook153Wanted.ScottishBookProblem153Claim`, a definition declared in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook153Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook153Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#scottish-book-problem153-claim).

## Negative answer to Mazur's Problem 153

There are a continuous function
$f \colon [0,1]^2 \to \mathbb{R}$ and a real number $\varepsilon > 0$ such that for every natural
number $n$, all points $a_1, \dots, a_n, b_1, \dots, b_n \in [0,1]$ and all real numbers
$c_1, \dots, c_n$ there are $x, y \in [0,1]$ with

$$\Bigl| f(x, y) - \sum_{k=1}^n c_k \, f(a_k, y) \, f(x, b_k) \Bigr| > \varepsilon.$$

That is, the approximation scheme of Mazur's Problem 153 fails.

## Sources

- S. Mazur, Problem 153 of the Scottish Book; refuted via P. Enflo's counterexample to the approximation problem in Banach spaces, Acta Math. 130 (1973), 309–317, DOI 10.1007/BF02392270; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015). This is the original bivariate-function form of the problem, distinct from its consequence for the approximation property.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook153Wanted.mazur153_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook153Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FunctionalAnalysis/ScottishBook153Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html#mazur153-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximation property](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/approximation-property)
