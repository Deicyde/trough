---
declaration: section
origin: cited
lean: MeasureTheory.Martingale.submartingale_comp_convex, MeasureTheory.Submartingale.comp_convex_of_monotoneOn, MeasureTheory.Martingale.supermartingale_comp_concave
statement: formalized
proof: formalized
---

# Convex functions of martingales

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/convex-functions-of-martingales/index.html).

## Convex functions of martingales are submartingales

Let $\mu$ be a probability measure,
let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration, and let $(X_n)_{n \in \mathbb{N}}$ be a
real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$. Let
$\varphi : \mathbb{R} \to \mathbb{R}$ be convex, and suppose $\varphi(X_n)$ is integrable for every
$n$. Then $(\varphi(X_n))_{n \in \mathbb{N}}$ is a submartingale with respect to $(\mathcal{F}_n)$
and $\mu$.

## Sources

- Lecture 26/27, martingale observations.

Formalized by `MeasureTheory.Martingale.submartingale_comp_convex`, a theorem declared in [MathlibExt/Probability/ConvexSubmartingale.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ConvexSubmartingale.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/convex-functions-of-martingales/index.html#submartingale-comp-convex).

## Convex nondecreasing functions preserve submartingales

Let $\mu$ be a probability measure,
let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration, and let $(X_n)_{n \in \mathbb{N}}$ be a
real-valued submartingale with respect to $(\mathcal{F}_n)$ and $\mu$. Let
$\varphi : \mathbb{R} \to \mathbb{R}$ be convex and nondecreasing, and suppose $\varphi(X_n)$ is
integrable for every $n$. Then $(\varphi(X_n))_{n \in \mathbb{N}}$ is a submartingale with respect
to $(\mathcal{F}_n)$ and $\mu$.

Monotonicity is needed: a convex function of a submartingale need not be a submartingale. For
example, take $\varphi(x) = (x - 4)^2$ and a submartingale with $X_i = 2$ and $X_j = 3$ almost
surely for some $i < j$; then $\varphi(X_i) = 4 > 1 = \varphi(X_j)$.

Formalized by `MeasureTheory.Submartingale.comp_convex_of_monotoneOn`, a theorem declared in [MathlibExt/Probability/ConvexSubmartingale.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ConvexSubmartingale.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/convex-functions-of-martingales/index.html#comp-convex-of-monotone-on).

## Concave functions of martingales are supermartingales

Let $\mu$ be a probability measure,
let $(\mathcal{F}_n)_{n \in \mathbb{N}}$ be a filtration, and let $(X_n)_{n \in \mathbb{N}}$ be a
real-valued martingale with respect to $(\mathcal{F}_n)$ and $\mu$. Let
$\varphi : \mathbb{R} \to \mathbb{R}$ be concave, and suppose $\varphi(X_n)$ is integrable for
every $n$. Then $(\varphi(X_n))_{n \in \mathbb{N}}$ is a supermartingale with respect to
$(\mathcal{F}_n)$ and $\mu$.

Formalized by `MeasureTheory.Martingale.supermartingale_comp_concave`, a theorem declared in [MathlibExt/Probability/ConvexSubmartingale.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/ConvexSubmartingale.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/convex-functions-of-martingales/index.html#supermartingale-comp-concave).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convex functions of martingales](https://deicyde.github.io/atlas-lean/roadmap/Probability/martingales/convex-functions-of-martingales/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/martingales/convex-functions-of-martingales)
