---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.Rouche.rouche_closedBall, MathlibExt.Analysis.RoucheWanted.ComplexAnalysis.rouche_zero_count_eq
statement: formalized
---

# Rouché's theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/rouch-s-theorem/index.html).

## Rouché's theorem on a disc

Let $c \in \mathbb{C}$ and $R > 0$, and let $f$ and $g$ be analytic
at every point of the closed disc $|z - c| \le R$. If $|g(z)| < |f(z)|$ for every $z$ on the circle
$|z - c| = R$, then $f$ and $f + g$ have the same number of zeros in the open disc $|z - c| < R$,
counted with multiplicity: the divisors of $f$ and of $f + g$ on the open disc have equal sums.

## Sources

- E. Rouché, Mémoire sur la série de Lagrange, J. École Polytechnique 22 (1862), 193-224

Formalized by `MathlibExt.Analysis.Complex.Rouche.rouche_closedBall`, a theorem declared in [MathlibExt/Analysis/Complex/Rouche.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Rouche.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/rouch-s-theorem/index.html#rouche-closed-ball).

## Rouché's theorem

Let $R > 0$, let $f : \mathbb{C} \to \mathbb{C}$ be meromorphic on
$\mathbb{C}$ and in normal form (at every point $f$ is either analytic, or has a pole and takes
the value $0$ there), and let $g : \mathbb{C} \to \mathbb{C}$ be analytic on $\mathbb{C}$.
If $|g(z)| < |f(z)|$ for every $z$ with $|z| = R$, then $f + g$ and $f$ have the same number
of zeros in the closed disk $|z| \le R$, counted with multiplicity: the sum over the points of
the disk of the positive part of the order of $f + g$ equals the same sum for $f$.

## Sources

- E. Rouché, *Mémoire sur la série de Lagrange*, J. École Polytechnique 22 (1862) (Rouché's theorem). Problem `rouche` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.RoucheWanted.ComplexAnalysis.rouche_zero_count_eq` is written with `theorem_wanted` in [WantedExt/Analysis/RoucheWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/RoucheWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/rouch-s-theorem/index.html#rouche-zero-count-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rouché's theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/cauchy-theory/rouch-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/cauchy-theory/rouch-s-theorem)
