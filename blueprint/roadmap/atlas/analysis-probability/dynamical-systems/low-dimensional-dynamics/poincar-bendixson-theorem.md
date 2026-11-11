---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.PoincareBendixsonWanted.Dynamics.Plane, MathlibExt.Dynamics.PoincareBendixsonWanted.Dynamics.poincare_bendixson
statement: formalized
---

# Poincaré–Bendixson theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/poincar-bendixson-theorem/index.html).

## The Euclidean plane

The ambient space is the plane $\mathbb{R}^2$ with its Euclidean
inner product and norm.

Formalized by `MathlibExt.Dynamics.PoincareBendixsonWanted.Dynamics.Plane`, an abbreviation declared in [WantedExt/Dynamics/PoincareBendixsonWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/PoincareBendixsonWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/poincar-bendixson-theorem/index.html#plane).

## Poincaré–Bendixson theorem

Let $F \colon \mathbb{R}^2 \to \mathbb{R}^2$ be a continuously
differentiable vector field on the Euclidean plane, and let
$\gamma \colon \mathbb{R} \to \mathbb{R}^2$ be a curve such that for every $t \ge 0$ the derivative
of $\gamma$ at $t$ within $[0, \infty)$ is $F(\gamma(t))$. Let
$\omega(\gamma) = \bigcap_{s \in \mathbb{R}} \overline{\gamma([s, \infty))}$ be the $\omega$-limit
set of $\gamma$. Then at least one of the following holds: the forward orbit
$\gamma([0, \infty))$ is unbounded; $\omega(\gamma)$ contains a point $x_0$ with $F(x_0) = 0$; or
there are a real number $T > 0$ and a curve $\beta \colon \mathbb{R} \to \mathbb{R}^2$ with
$\beta'(t) = F(\beta(t))$ and $\beta(t + T) = \beta(t)$ for every real $t$ and with
$F(\beta(0)) \ne 0$, such that $\omega(\gamma)$ equals the range of $\beta$.

## Sources

- H. Poincaré, *Mémoire sur les courbes définies par une équation différentielle*, Journal de Mathématiques 7 (1881), 8 (1882), 1 (1885), 2 (1886); I. Bendixson, *Sur les courbes définies par des équations différentielles*, Acta Mathematica 24 (1901), 1-88. Listed as §63 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). The Isabelle/HOL/AFP entry by Fabian Immler and Yong Kiam Tan (https://www.isa-afp.org/entries/Poincare_Bendixson.html) uses John Harrison's Jordan curve theorem. Problem `poincare_bendixson` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.PoincareBendixsonWanted.Dynamics.poincare_bendixson` is written with `theorem_wanted` in [WantedExt/Dynamics/PoincareBendixsonWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/PoincareBendixsonWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/poincar-bendixson-theorem/index.html#poincare-bendixson).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poincaré–Bendixson theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/poincar-bendixson-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/low-dimensional-dynamics/poincar-bendixson-theorem)
