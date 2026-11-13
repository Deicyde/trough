---
declaration: section
origin: cited
lean: MathlibExt.Analysis.MandelbrotWanted.ComplexAnalysis.MandelbrotProblem.Tc, MathlibExt.Analysis.MandelbrotWanted.ComplexAnalysis.MandelbrotProblem.Mandelbrot, MathlibExt.Analysis.MandelbrotWanted.ComplexAnalysis.MandelbrotProblem.mandelbrot_connected, MathlibExt.Dynamics.MandelbrotBoundaryWanted.Dynamics.MandelbrotBoundary.Tc, MathlibExt.Dynamics.MandelbrotBoundaryWanted.Dynamics.MandelbrotBoundary.Mandelbrot, MathlibExt.Dynamics.MandelbrotBoundaryWanted.Dynamics.MandelbrotBoundary.mandelbrot_boundary_dimh
statement: formalized
---

# Mandelbrot set

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html).

## The quadratic family

For $c \in \mathbb{C}$, $T_c \colon \mathbb{C} \to \mathbb{C}$ is the
map $T_c(z) = z^2 + c$.

Formalized by `MathlibExt.Analysis.MandelbrotWanted.ComplexAnalysis.MandelbrotProblem.Tc`, a definition declared in [WantedExt/Analysis/MandelbrotWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MandelbrotWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html#tc).

## The Mandelbrot set

The Mandelbrot set is the set of all $c \in \mathbb{C}$ for which the
orbit of $0$ under $T_c(z) = z^2 + c$ is bounded: there is a real number $M$ with
$|T_c^n(0)| \le M$ for every $n \in \mathbb{N}$, where $T_c^n$ is the $n$-th iterate of $T_c$
and $T_c^0$ is the identity.

Formalized by `MathlibExt.Analysis.MandelbrotWanted.ComplexAnalysis.MandelbrotProblem.Mandelbrot`, a definition declared in [WantedExt/Analysis/MandelbrotWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MandelbrotWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html#mandelbrot).

## The Mandelbrot set is connected (Douady–Hubbard)

The Mandelbrot set, the set of all
$c \in \mathbb{C}$ for which the sequence $(T_c^n(0))_{n \ge 0}$ of iterates of $0$ under
$T_c(z) = z^2 + c$ is bounded, is a nonempty connected subset of $\mathbb{C}$.

## Sources

- A. Douady and J. H. Hubbard, *Étude dynamique des polynômes complexes I, II*, Publ. Math. Orsay 84-02, 85-04. Listed as §62 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `mandelbrot_connected` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.MandelbrotWanted.ComplexAnalysis.MandelbrotProblem.mandelbrot_connected` is written with `theorem_wanted` in [WantedExt/Analysis/MandelbrotWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MandelbrotWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html#mandelbrot-connected).

## Quadratic family

For each complex number $c$, the map $T_c : \mathbb{C} \to \mathbb{C}$ is
given by $T_c(z) = z^2 + c$.

Formalized by `MathlibExt.Dynamics.MandelbrotBoundaryWanted.Dynamics.MandelbrotBoundary.Tc`, a definition declared in [WantedExt/Dynamics/MandelbrotBoundaryWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/MandelbrotBoundaryWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html#tc-2).

## Mandelbrot set

The Mandelbrot set is the set $M$ of complex numbers $c$ for which the orbit
of $0$ under the quadratic map $T_c(z) = z^2 + c$ is bounded: there is a real number $R$ with
$|T_c^n(0)| \le R$ for every $n \in \mathbb{N}$, where $T_c^n$ is the $n$-th iterate of $T_c$ and
$T_c^0$ is the identity.

Formalized by `MathlibExt.Dynamics.MandelbrotBoundaryWanted.Dynamics.MandelbrotBoundary.Mandelbrot`, a definition declared in [WantedExt/Dynamics/MandelbrotBoundaryWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/MandelbrotBoundaryWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html#mandelbrot-2).

## Hausdorff dimension of the Mandelbrot boundary (Shishikura)

The boundary of the
Mandelbrot set $M \subseteq \mathbb{C}$ has Hausdorff dimension $2$.

## Sources

- M. Shishikura, The Hausdorff dimension of the boundary of the Mandelbrot set and Julia sets, Ann. of Math. 147 (1998). Listed as §260 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Knill, §260. Problem `mandelbrot_boundary_dimh` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.MandelbrotBoundaryWanted.Dynamics.MandelbrotBoundary.mandelbrot_boundary_dimh` is written with `theorem_wanted` in [WantedExt/Dynamics/MandelbrotBoundaryWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/MandelbrotBoundaryWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html#mandelbrot-boundary-dimh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mandelbrot set](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/mandelbrot-set/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/complex-dynamics/mandelbrot-set)
