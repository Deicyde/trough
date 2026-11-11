---
declaration: section
origin: cited
lean: MetaMathlibExt.landsberg_schaar, MetaMathlibExt.congruentPairQuadraticSum_eq_sub_dedekindSum
statement: formalized
---

# Exponential and character sums: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/index.html).

Gauss sums, Weyl and Vinogradov sums, incomplete exponential sums, Burgess bounds, Dirichlet polynomials, trigonometric and cotangent sums.

## Landsberg–Schaar relation

For all positive integers $p$ and $q$,

$$
\frac{1}{\sqrt{p}} \sum_{n=0}^{p-1} \exp\left(\frac{2 \pi i n^2 q}{p}\right) =
\frac{e^{\pi i / 4}}{\sqrt{2q}} \sum_{n=0}^{2q-1} \exp\left(-\frac{\pi i n^2 p}{2q}\right).
$$

## Sources

- https://en.wikipedia.org/wiki/Landsberg%E2%80%93Schaar_relation.

Formalized by `MetaMathlibExt.landsberg_schaar`, a theorem declared in [MathlibExt/NumberTheory/LandsbergSchaar.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LandsbergSchaar.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/index.html#landsberg-schaar).

## Mittou's evaluation of a quadratic sum over congruent pairs

Let $p$ be a prime and $l$ a
positive integer with $\gcd(p, l) = 1$. Let $F(p, l)$ be the sum of
$\left(\frac{a}{p} - \frac{1}{2}\right)\left(\frac{b}{p} - \frac{1}{2}\right)$ over all pairs of
integers $a, b$ with $1 \le a, b \le p - 1$ and $b \equiv a l \pmod{p}$, and let

$$s(p, l) = \frac{1}{4l} \sum_{a=1}^{l-1} \cot\left(\frac{\pi a}{l}\right)
\cot\left(\frac{\pi a p}{l}\right)$$

be the Dedekind sum. Then

$$F(p, l) = \frac{p^2 - 3lp + l^2 + 1}{12 l p} - s(p, l).$$

Domain extension: the paper assumes $p \ge 3$; the identity also holds for $p = 2$ (then $l$ is
odd and both sides vanish), so that hypothesis is dropped. The paper's remark that $s(p, l)$
depends only on $p \bmod l$ is not restated.

## Sources

- Brahim Mittou, *Explicit Evaluation of a Quadratic Sum Over Congruent Pairs Modulo a Prime*, INTEGERS 25 (2025), Article A85, Theorem 1.

Stated but not proved: `MetaMathlibExt.congruentPairQuadraticSum_eq_sub_dedekindSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/CongruentPairQuadraticSumWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CongruentPairQuadraticSumWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/index.html#congruent-pair-quadratic-sum-eq-sub-dede).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential and character sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/exponential-sums)
