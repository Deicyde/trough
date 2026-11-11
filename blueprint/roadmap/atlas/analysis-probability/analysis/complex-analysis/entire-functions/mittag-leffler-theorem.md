---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.MittagLefflerWanted.principalPart, MathlibExt.Analysis.Complex.MittagLefflerWanted.principalPart_analyticAt, MathlibExt.Analysis.Complex.MittagLefflerWanted.principalPart_meromorphicAt, MathlibExt.Analysis.Complex.MittagLefflerWanted.mittag_leffler_of_isDiscrete, MathlibExt.Analysis.Complex.MittagLefflerWanted.mittag_leffler
statement: formalized
proof: formalized
---

# Mittag-Leffler theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html).

## Principal part with finitely many coefficients

For a point $s \in \mathbb{C}$ and a finitely
supported sequence $c = (c_k)_{k \in \mathbb{N}}$ of complex coefficients, the principal part at
$s$ with coefficients $c$ is the function $\mathbb{C} \to \mathbb{C}$ given by
$z \mapsto \sum_k c_k (z - s)^{-(k+1)}$, the sum running over the finitely many $k$ with
$c_k \neq 0$.

At $z = s$ every term is taken to be $0$ (the convention $0^{-n} = 0$), so the function has value
$0$ there.

Formalized by `MathlibExt.Analysis.Complex.MittagLefflerWanted.principalPart`, a definition declared in [MathlibExt/Analysis/Complex/MittagLeffler.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/MittagLeffler.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html#principal-part).

## The principal part is analytic away from its pole

For every $s \in \mathbb{C}$ and every
finitely supported sequence $c$ of complex coefficients, the principal part at $s$ with
coefficients $c$ is analytic at every point $z \neq s$.

Formalized by `MathlibExt.Analysis.Complex.MittagLefflerWanted.principalPart_analyticAt`, a theorem declared in [MathlibExt/Analysis/Complex/MittagLeffler.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/MittagLeffler.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html#principal-part-analytic-at).

## The principal part is meromorphic

For every $s \in \mathbb{C}$ and every finitely
supported sequence $c$ of complex coefficients, the principal part at $s$ with coefficients $c$ is
meromorphic at every point of $\mathbb{C}$.

Formalized by `MathlibExt.Analysis.Complex.MittagLefflerWanted.principalPart_meromorphicAt`, a theorem declared in [MathlibExt/Analysis/Complex/MittagLeffler.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/MittagLeffler.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html#principal-part-meromorphic-at).

## Mittag-Leffler theorem, discrete-subspace form

Let $S \subseteq \mathbb{C}$ be a closed set
that is discrete in the subspace topology, and for each $s \in S$ let $c_s$ be a finitely supported
sequence of complex coefficients. Then there is a function $f : \mathbb{C} \to \mathbb{C}$ that is
holomorphic on $\mathbb{C} \setminus S$, meromorphic on all of $\mathbb{C}$, and such that for every
$s \in S$ the difference between $f$ and the principal part at $s$ with coefficients $c_s$ is
analytic at $s$.

Formalized by `MathlibExt.Analysis.Complex.MittagLefflerWanted.mittag_leffler_of_isDiscrete`, a theorem declared in [MathlibExt/Analysis/Complex/MittagLeffler.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/MittagLeffler.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html#mittag-leffler-of-is-discrete).

## Mittag-Leffler theorem

Let $S \subseteq \mathbb{C}$ be a closed set such that every $z \in S$
has a radius $\varepsilon > 0$ for which the punctured disk $\{w : 0 < |w - z| < \varepsilon\}$
contains no point of $S$, and for each $s \in S$ let $c_s$ be a finitely supported sequence of
complex coefficients. Then there is a function $f : \mathbb{C} \to \mathbb{C}$ that is holomorphic
on $\mathbb{C} \setminus S$, meromorphic on all of $\mathbb{C}$, and such that for every $s \in S$
the difference between $f$ and the principal part at $s$ with coefficients $c_s$ is analytic at
$s$.

## Sources

- Mittag-Leffler theorem, G. Mittag-Leffler, Acta Math. 4 (1884); see Rudin; Lean is closed discrete S with punctured-ball isolation, prescribed finite principal parts via Finsupp, global meromorphic existence holomorphic on Sᶜ.

Formalized by `MathlibExt.Analysis.Complex.MittagLefflerWanted.mittag_leffler`, a theorem declared in [MathlibExt/Analysis/Complex/MittagLeffler.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/MittagLeffler.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html#mittag-leffler).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mittag-Leffler theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/entire-functions/mittag-leffler-theorem)
