---
declaration: section
origin: cited
lean: MathlibExt.Analysis.RieszBrothersWanted.Analysis.riesz_brothers_theorem, MathlibExt.Analysis.Complex.FatouRadialWanted.fatou_radial_limit
statement: formalized
---

# Spaces of analytic functions: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/index.html).

Hardy, Bergman, Dirichlet and Fock spaces and their reproducing kernels, H^∞, boundary behaviour (Fatou, F. and M. Riesz), cyclicity and polynomial density.

## F. and M. Riesz theorem

Let $\mu$ be a complex Borel measure on the circle
$\mathbb{T} = \mathbb{R}/\mathbb{Z}$. If $\int_{\mathbb{T}} e^{2\pi i n z} \, d\mu(z) = 0$ for
every integer $n \ge 1$, then $\mu$ is absolutely continuous with respect to the Haar probability
measure on $\mathbb{T}$.

## Sources

- W. Rudin, Real and Complex Analysis; N. K. Nikolski, Operators, Functions, and Systems: An Easy Reading, Volume I: Hardy, Hankel, and Toeplitz. Problem `riesz_brothers_theorem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RieszBrothersWanted.Analysis.riesz_brothers_theorem` is written with `theorem_wanted` in [WantedExt/Analysis/RieszBrothersWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RieszBrothersWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/index.html#riesz-brothers-theorem).

## Fatou's theorem on radial limits

Let $f : \mathbb{C} \to \mathbb{C}$ be holomorphic and
bounded on the open unit disc $|z| < 1$. Then for Lebesgue-almost every $\theta \in [0, 2\pi]$ the
radial limit $\lim_{r \to 1^-} f(r e^{i\theta})$ exists in $\mathbb{C}$.

## Sources

- Fatou radial limit theorem for H∞, P. Fatou, Acta Math. 30 (1906); see Rudin, Real and Complex Analysis, Bounded Analytic Functions; Lean is bounded holomorphic on ball 0 1 with a.e. radial limit via volume.restrict Icc 0 (2π) and 𝓝[<] 1.

Formalized by `MathlibExt.Analysis.Complex.FatouRadialWanted.fatou_radial_limit`, a theorem declared in [MathlibExt/Analysis/Complex/FatouRadial.lean, line 1033](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/FatouRadial.lean#L1033). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/index.html#fatou-radial-limit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spaces of analytic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/analytic-function-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/analytic-function-spaces)
