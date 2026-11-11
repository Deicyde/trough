---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.ArgumentPrinciple.argumentPrinciple_closedBall_general, MathlibExt.Analysis.Complex.ArgumentPrinciple.argumentPrinciple_closedBall
statement: formalized
proof: formalized
---

# Argument principle

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/argument-principle/index.html).

## Argument principle on a closed disc

Let $c \in \mathbb{C}$, $R > 0$, and let
$f : \mathbb{C} \to \mathbb{C}$ be meromorphic on the closed disc $|z - c| \le R$ with finite order
at every point of that disc (so $f$ vanishes identically near no point). Suppose the order of $f$
is zero at every point of the circle $|z - c| = R$. Then the integral of $f'/f$ over the circle
$|z - c| = R$, traversed once counterclockwise, equals $2\pi i$ times the sum of the orders of $f$
at the points of the open disc $|z - c| < R$ (zeros counted positively and poles negatively, with
multiplicity).

Formalized by `MathlibExt.Analysis.Complex.ArgumentPrinciple.argumentPrinciple_closedBall_general`, a theorem declared in [MathlibExt/Analysis/Complex/ArgumentPrinciple.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/ArgumentPrinciple.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/argument-principle/index.html#argument-principle-closed-ball-general).

## Argument principle on a closed disc, with an integrability hypothesis

Let $c \in \mathbb{C}$,
$R > 0$, and let $f : \mathbb{C} \to \mathbb{C}$ be meromorphic on the closed disc $|z - c| \le R$
with finite order at every point of that disc. Suppose the order of $f$ is zero at every point of
the circle $|z - c| = R$ and $f'/f$ is integrable on that circle. Then the integral of $f'/f$ over
the circle, traversed once counterclockwise, equals $2\pi i$ times the sum of the orders of $f$ at
the points of the open disc $|z - c| < R$ (zeros counted positively and poles negatively, with
multiplicity).

## Sources

- L. V. Ahlfors, Complex Analysis, 3rd ed., §5.2. It follows from `argumentPrinciple_closedBall_general`; the hypothesis `hint` is unused and keeps the source's shape.

Formalized by `MathlibExt.Analysis.Complex.ArgumentPrinciple.argumentPrinciple_closedBall`, a theorem declared in [MathlibExt/Analysis/Complex/ArgumentPrinciple.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/ArgumentPrinciple.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/argument-principle/index.html#argument-principle-closed-ball).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Argument principle](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/argument-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/argument-principle)
