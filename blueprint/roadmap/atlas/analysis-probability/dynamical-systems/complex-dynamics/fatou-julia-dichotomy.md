---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.Tc, MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.Mandelbrot, MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.FilledJulia, MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.julia_cantor_dichotomy
statement: formalized
---

# Fatou–Julia dichotomy

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy/index.html).

## Quadratic map $T_c$

For $c \in \mathbb{C}$, $T_c \colon \mathbb{C} \to \mathbb{C}$ is the
map $T_c(z) = z^2 + c$.

Formalized by `MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.Tc`, a definition declared in [WantedExt/Analysis/FatouJuliaWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FatouJuliaWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy/index.html#tc).

## Mandelbrot set of the quadratic family

Let $T_c(z) = z^2 + c$ for $c \in \mathbb{C}$
and let $T_c^n$ be its $n$-fold iterate. The Mandelbrot set $M$ is the set of $c \in \mathbb{C}$
for which the orbit of $0$ under $T_c$ is bounded: there is a real $R$ such that
$|T_c^n(0)| \le R$ for every $n \ge 0$.

Formalized by `MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.Mandelbrot`, a definition declared in [WantedExt/Analysis/FatouJuliaWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FatouJuliaWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy/index.html#mandelbrot).

## Filled Julia set

For $c \in \mathbb{C}$, let $T_c(z) = z^2 + c$ and let $T_c^n$ be its
$n$-fold iterate. The filled Julia set $K_c$ is the set of $z \in \mathbb{C}$ whose orbit under
$T_c$ is bounded: there is a real $M$ such that $|T_c^n(z)| \le M$ for every $n \ge 0$.

Formalized by `MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.FilledJulia`, a definition declared in [WantedExt/Analysis/FatouJuliaWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FatouJuliaWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy/index.html#filled-julia).

## Fatou–Julia dichotomy for quadratic polynomials

For $c \in \mathbb{C}$, let $K_c$ be the
filled Julia set of $T_c(z) = z^2 + c$ and let $M$ be the Mandelbrot set. If $c \in M$, then $K_c$
is nonempty and connected. If $c \notin M$, then $K_c$ is homeomorphic to the Cantor space
$\{0, 1\}^{\mathbb{N}}$ of binary sequences with the product topology.

## Sources

- P. Fatou, *Sur les équations fonctionnelles*, Bull. Soc. Math. France 47 (1919), 161-271; 48 (1920), 33-94, 208-314. G. Julia, *Mémoire sur l'itération des fonctions rationnelles*, J. Math. Pures Appl. 1 (1918), 47-245. Modern statement: A. Douady and J. H. Hubbard, *Étude dynamique des polynômes complexes I, II*, Publ. Math. Orsay 84-02, 85-04. Listed as §62 (additional statement 1) in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `fatou_julia_dichotomy` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.FatouJuliaWanted.ComplexAnalysis.FatouJuliaProblem.julia_cantor_dichotomy` is written with `theorem_wanted` in [WantedExt/Analysis/FatouJuliaWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FatouJuliaWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy/index.html#julia-cantor-dichotomy).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fatou–Julia dichotomy](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/complex-dynamics/fatou-julia-dichotomy)
