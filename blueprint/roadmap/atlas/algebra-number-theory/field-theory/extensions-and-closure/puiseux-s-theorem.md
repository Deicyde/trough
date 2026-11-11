---
declaration: section
origin: cited
lean: HahnSeries.isAlgClosed_rat, MetaMathlibExt.puiseux_theorem
statement: formalized
proof: formalized
---

# Puiseux's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/puiseux-s-theorem/index.html).

## Hahn Series

## Algebraic closedness of rational Hahn series

Let $K$ be an algebraically closed field of
characteristic zero. Then the field of Hahn series over $K$ with exponents in $\mathbb{Q}$ (formal
sums $\sum_r a_r t^r$ with $a_r \in K$ whose support $\{r \in \mathbb{Q} : a_r \neq 0\}$ is
well-ordered) is algebraically closed.

Formalized by `HahnSeries.isAlgClosed_rat`, a theorem declared in [MathlibExt/FieldTheory/PuiseuxTheorem.lean, line 997](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/PuiseuxTheorem.lean#L997). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/puiseux-s-theorem/index.html#is-alg-closed-rat).

## Puiseux's theorem

Let $K$ be an algebraically closed field of characteristic zero, let
$K((t))$ be the field of formal Laurent series over $K$, and let $K((t^{\mathbb{Q}}))$ be the field
of Hahn series over $K$ with exponents in $\mathbb{Q}$ (formal sums $\sum_r a_r t^r$ with
$a_r \in K$ whose support $\{r \in \mathbb{Q} : a_r \neq 0\}$ is well-ordered). Then:
(i) $K((t^{\mathbb{Q}}))$ is algebraically closed;
(ii) there are an injective ring homomorphism $\iota : K((t)) \to K((t^{\mathbb{Q}}))$, a subfield
$P$ of $K((t^{\mathbb{Q}}))$ containing $\iota(K((t)))$, and a ring isomorphism $e$ from $P$ onto
the algebraic closure $\overline{K((t))}$ of $K((t))$, such that $P$ consists exactly of the
series $y$ for which there is an integer $n > 0$ with every exponent in the support of $y$ of the
form $m/n$ with $m \in \mathbb{Z}$ (the Puiseux series), and $e(\iota(y))$ is the image of $y$
under the canonical embedding $K((t)) \to \overline{K((t))}$ for every $y \in K((t))$;
(iii) $K((t))$ is isomorphic as a ring to the field of fractions of the power series ring
$K[[t]]$.

Proof: Newton polygon plus Hensel lifting, first in the rational Hahn field and
then with the ramification bounded inside a power-series level.

## Sources

- https://en.wikipedia.org/wiki/Puiseux_series

Formalized by `MetaMathlibExt.puiseux_theorem`, a theorem declared in [MathlibExt/FieldTheory/PuiseuxTheorem.lean, line 2040](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/PuiseuxTheorem.lean#L2040). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/puiseux-s-theorem/index.html#puiseux-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Puiseux's theorem](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/puiseux-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/FieldTheory/extensions-and-closure/puiseux-s-theorem)
