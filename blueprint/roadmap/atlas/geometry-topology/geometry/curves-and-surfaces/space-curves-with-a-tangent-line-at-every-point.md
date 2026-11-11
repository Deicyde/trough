---
declaration: section
origin: cited
lean: MathlibExt.Geometry.ScottishBook117Wanted.HasTangentLineAt, MathlibExt.Geometry.ScottishBook117Wanted.ScottishBookProblem117Claim, MathlibExt.Geometry.ScottishBook117Wanted.frechet117_refuted
statement: formalized
---

# Space curves with a tangent line at every point

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/space-curves-with-a-tangent-line-at-every-point/index.html).

## Tangent line to a closed space curve

A `1`-periodic continuous injective-on-`[0, 1)` curve `γ : ℝ → ℝ³`
has an (oriented) tangent line at `t` if there is a unit direction `v` such
that every nearby secant vector `γ s - γ t` is arbitrarily close, relative
to its length, to the line spanned by `v`.

Formalized by `MathlibExt.Geometry.ScottishBook117Wanted.HasTangentLineAt`, a definition declared in [WantedExt/Geometry/ScottishBook117Wanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ScottishBook117Wanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/space-curves-with-a-tangent-line-at-every-point/index.html#has-tangent-line-at).

## The claim of Fréchet's Problem 117

The claim of Fréchet's Problem 117 from the Scottish
Book is the statement that for every $1$-periodic continuous map
$\gamma : \mathbb{R} \to \mathbb{R}^3$ that is injective on $[0, 1)$ and has a tangent line at
every $t \in \mathbb{R}$, there is a $1$-periodic continuous map
$p : \mathbb{R} \to \mathbb{R}^3$ that is injective on $[0, 1)$, has the same image as $\gamma$,
and is differentiable at every $t \in \mathbb{R}$ with $p'(t) \ne 0$.

Formalized by `MathlibExt.Geometry.ScottishBook117Wanted.ScottishBookProblem117Claim`, a definition declared in [WantedExt/Geometry/ScottishBook117Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ScottishBook117Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/space-curves-with-a-tangent-line-at-every-point/index.html#scottish-book-problem117-claim).

## Fréchet's Problem 117 has a negative answer

There is a $1$-periodic continuous
map $\gamma : \mathbb{R} \to \mathbb{R}^3$, injective on $[0, 1)$, that has a tangent
line at every parameter $t$, such that no $1$-periodic continuous map
$p : \mathbb{R} \to \mathbb{R}^3$ that is injective on $[0, 1)$ and has the same image
as $\gamma$ is differentiable at every $t$ with $p'(t) \neq 0$.

Here $\gamma$ has a tangent line at $t$ when there is a unit vector $v$ such that for
every $\varepsilon > 0$ there is $\delta > 0$ with
$\|w - \langle w, v \rangle v\| \le \varepsilon \|w\|$, where $w = \gamma(s) - \gamma(t)$,
whenever $0 < |s - t| < \delta$.

## Sources

- M. Fréchet, Problem 117 of the Scottish Book; in general, no, by A. J. Ward, Fundamenta Mathematicae 28 (1937), cited in the typescript addendum Ad 117. Ward also gives a representation whose derivatives exist and are not all zero except on a null set of parameter values whose points have Carathéodory measure zero.

Stated but not proved: `MathlibExt.Geometry.ScottishBook117Wanted.frechet117_refuted` is written with `theorem_wanted` in [WantedExt/Geometry/ScottishBook117Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/ScottishBook117Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/space-curves-with-a-tangent-line-at-every-point/index.html#frechet117-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Space curves with a tangent line at every point](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/space-curves-with-a-tangent-line-at-every-point/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/curves-and-surfaces/space-curves-with-a-tangent-line-at-every-point)
