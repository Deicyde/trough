---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ContinuousMap.KolmogorovSuperpositionWanted.kolmogorov_superposition, MathlibExt.Analysis.KolmogorovArnoldWanted.Analysis.kolmogorov_arnold
statement: formalized
---

# Kolmogorov superposition theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/kolmogorov-superposition-theorem/index.html).

## Kolmogorov superposition theorem

Let $n \ge 2$. There are continuous functions
$\psi_{q,p} : [0,1] \to \mathbb{R}$ for $0 \le q \le 2n$ and $0 \le p < n$, depending only on
$n$, such that for every continuous function $f : [0,1]^n \to \mathbb{R}$ there are continuous
functions $\varphi_q : \mathbb{R} \to \mathbb{R}$ for $0 \le q \le 2n$ with
$f(x) = \sum_{q=0}^{2n} \varphi_q\left(\sum_{p=0}^{n-1} \psi_{q,p}(x_p)\right)$ for every
$x = (x_0, \dots, x_{n-1}) \in [0,1]^n$.

## Sources

- Kolmogorov superposition theorem, A. N. Kolmogorov, Dokl. Akad. Nauk SSSR 114 (1957) 953–956, refined Arnold 1957; see Braun–Griebel, Acta Numer. 2009 review; Lean is n ≥ 2 exact cardinal Fin (2n+1) with inner ψ in C(Icc 0 1, ℝ) independent of f and outer φ in C(ℝ, ℝ), compact-source specialization [0, 1]^n as Fin n → Icc.

Formalized by `MathlibExt.Analysis.ContinuousMap.KolmogorovSuperpositionWanted.kolmogorov_superposition`, a theorem declared in [MathlibExt/Analysis/ContinuousMap/KolmogorovSuperposition.lean, line 1515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/ContinuousMap/KolmogorovSuperposition.lean#L1515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/kolmogorov-superposition-theorem/index.html#kolmogorov-superposition).

## Kolmogorov–Arnold superposition with a single outer function

Let $n \ge 1$ and let
$f : \mathbb{R}^n \to \mathbb{R}$ be continuous on the unit cube $[0, 1]^n$. Then there exist a
continuous function $g : \mathbb{R} \to \mathbb{R}$ and continuous functions
$\varphi_{k,l} : \mathbb{R} \to \mathbb{R}$ for $0 \le k \le 2n$ and $0 \le l < n$ such that for
every $x = (x_0, \dots, x_{n-1}) \in [0, 1]^n$,

$$f(x) = \sum_{k=0}^{2n} g\left(\sum_{l=0}^{n-1} \varphi_{k,l}(x_l)\right).$$

Both $g$ and the $\varphi_{k,l}$ may depend on $f$, so this is weaker than the form in which the
inner functions are universal.

## Sources

- A. N. Kolmogorov, *On the representation of continuous functions of several variables by superposition of continuous functions of one variable and addition*, Doklady Akad. Nauk SSSR 114 (1957), 953-956. V. I. Arnold, *On functions of three variables*, Doklady Akad. Nauk SSSR 114 (1957), 679-681. G. G. Lorentz, *Metric entropy, widths, and superpositions of functions*, Amer. Math. Monthly 69 (1962), 469-485 (single-outer-function refinement). Listed as §80 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `kolmogorov_arnold_superposition` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.KolmogorovArnoldWanted.Analysis.kolmogorov_arnold` is written with `theorem_wanted` in [WantedExt/Analysis/KolmogorovArnoldWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/KolmogorovArnoldWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/kolmogorov-superposition-theorem/index.html#kolmogorov-arnold).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kolmogorov superposition theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/kolmogorov-superposition-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/approximation-theory/kolmogorov-superposition-theorem)
