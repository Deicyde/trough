---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook124Wanted.ScottishBookProblem124Claim, MathlibExt.Analysis.ScottishBook124Wanted.marcinkiewicz124_holds
statement: formalized
---

# Titchmarsh convolution theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/titchmarsh-convolution-theorem/index.html).

## The Volterra-form sub-conjecture of Scottish Book Problem 124

The statement that for every
continuous function $f : \mathbb{R} \to \mathbb{R}$ with $f(0) \ne 0$ and every function
$y : \mathbb{R} \to \mathbb{R}$ that is Lebesgue integrable on $[0, 1]$, if
$\int_0^x y(t) f(x - t)\,dt = 0$ for every $x \in [0, 1]$, then $y = 0$ almost everywhere on
$[0, 1]$.

The Scottish Book typescript prints the upper limit of the integral as $1$, but the entry's own
arguments show that the intended upper limit is $x$ (Volterra form); with upper limit $1$ the
claim is false, since $f \equiv 1$ and $y(t) = t - 1/2$ give a nonzero solution. The typescript
does not specify a function class for $y$; integrability on $[0, 1]$ is motivated by the $L^2$
context of the entry.

Formalized by `MathlibExt.Analysis.ScottishBook124Wanted.ScottishBookProblem124Claim`, a definition declared in [WantedExt/Analysis/ScottishBook124Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook124Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/titchmarsh-convolution-theorem/index.html#scottish-book-problem124-claim).

## The Volterra-form sub-conjecture of Scottish Book Problem 124 holds

For every continuous
function $f : \mathbb{R} \to \mathbb{R}$ with $f(0) \ne 0$ and every function
$y : \mathbb{R} \to \mathbb{R}$ that is Lebesgue integrable on $[0, 1]$, if
$\int_0^x y(t) f(x - t)\,dt = 0$ for every $x \in [0, 1]$, then $y = 0$ almost everywhere on
$[0, 1]$.

## Sources

- Józef Marcinkiewicz, Problem 124 of the Scottish Book; typescript PDF p.58, printed p.55. TYPESCRIPT TYPO, CORRECTED (Phase 5): the typescript prints the equation as `∫₀¹ y(t) f(x-t) dt = 0`, but the intended upper limit is `x` (Volterra form). The literal `∫₀¹` reading is false: `f ≡ 1`, `y(t) = t - 1/2` is a nonzero solution. Only the Volterra `∫₀ˣ` reading is filed here. Positive by the local Titchmarsh convolution theorem: E. C. Titchmarsh, "The zeros of certain integral functions", Proc. London Math. Soc. s2-25 (1926), 283–302, DOI 10.1112/plms/s2-25.1.283. Sketch: Titchmarsh gives `λ, μ ≥ 0` with `λ + μ ≥ 1` such that `y = 0` a.e. on `(0, λ)` and `f = 0` a.e. on `(0, μ)`. Continuity of `f` at `0` with `f 0 ≠ 0` forces `μ = 0` (otherwise `f` would be a.e. zero on a positive-measure initial interval while being nonzero near `0`), so `λ ≥ 1` and `y = 0` a.e. on `[0, 1]`.

Stated but not proved: `MathlibExt.Analysis.ScottishBook124Wanted.marcinkiewicz124_holds` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook124Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook124Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/titchmarsh-convolution-theorem/index.html#marcinkiewicz124-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Titchmarsh convolution theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/integral-and-multiplication/titchmarsh-convolution-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/integral-and-multiplication/titchmarsh-convolution-theorem)
