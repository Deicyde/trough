---
declaration: section
origin: cited
lean: MetaMathlibExt.ramanujanK, MetaMathlibExt.ramanujanK_zero, MetaMathlibExt.ramanujanK_eta_quotients, MetaMathlibExt.ramanujanK_div_sub_div_sq, MetaMathlibExt.ramanujanK_sq_relation, MetaMathlibExt.ramanujan_theta_level_ten
statement: formalized
---

# Ramanujan's function k

6 results, 2 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html).

## Ramanujan's function $k(q)$

For a complex number $q$, Ramanujan's function is

$$
k(q) = \frac{q\,(q;q^{10})_\infty (q^2;q^{10})_\infty (q^8;q^{10})_\infty (q^9;q^{10})_\infty}
{(q^3;q^{10})_\infty (q^4;q^{10})_\infty (q^6;q^{10})_\infty (q^7;q^{10})_\infty},
$$

where $(a;x)_\infty$ is the raw infinite q-Pochhammer product $\prod_{n \ge 0} (1 - a x^n)$
(equal to $1$ by convention when this product does not converge unconditionally), and a
quotient by $0$ is read as $0$.

For $|q| < 1$ this is the product representation of $k(q) = r(q)\,r(q^2)^2$, where $r$ is the
Rogers–Ramanujan continued fraction.

## Sources

- Russelle Guadalupe, *New Proofs of Certain Theta Function Identities via Ramanujan's Function*, INTEGERS 26 (2026), Article A41, Section 1 (product representation of `k(q)`).

Formalized by `MetaMathlibExt.ramanujanK`, a definition declared in [WantedExt/NumberTheory/RamanujanKFunctionWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanKFunctionWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html#ramanujan-k).

## Ramanujan's function $k$ vanishes at $0$

Ramanujan's function satisfies $k(0) = 0$.

## Sources

- Russelle Guadalupe, *New Proofs of Certain Theta Function Identities via Ramanujan's Function*, INTEGERS 26 (2026), Article A41, Section 1 (product representation of `k(q)`).

Formalized by `MetaMathlibExt.ramanujanK_zero`, a theorem declared in [WantedExt/NumberTheory/RamanujanKFunctionWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanKFunctionWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html#ramanujan-k-zero).

## Eta-quotient expressions for Ramanujan's function $k$

Let $q$ be a complex number with
$0 < |q| < 1$, write $f_m = (q^m;q^m)_\infty = \prod_{n \ge 1} (1 - q^{mn})$ for $m \ge 1$, and let
$k = k(q)$ be the value of Ramanujan's function. Then

$$
\frac{f_2 f_5^5}{q f_1 f_{10}^5} = \frac{1}{k} - k, \qquad
\frac{f_2^4 f_5^2}{q f_1^2 f_{10}^4} = \frac{1}{k} + 1 - k, \qquad
\frac{f_1^3 f_5}{q f_2 f_{10}^3} = \frac{1}{k} - 4 - k.
$$

## Sources

- Russelle Guadalupe, *New Proofs of Certain Theta Function Identities via Ramanujan's Function*, INTEGERS 26 (2026), Article A41, Lemma 2, Equations (5)-(7).

Stated but not proved: `MetaMathlibExt.ramanujanK_eta_quotients` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanKFunctionWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanKFunctionWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html#ramanujan-k-eta-quotients).

## Ramanujan's function $k$ at $q$ and $q^2$ as an eta quotient

For every complex number
$q$ with $0 < |q| < 1$, Ramanujan's function $k$ satisfies

$$
\frac{k(q)}{k(q^2)} - \frac{k(q^2)}{k(q)} =
\frac{(q;q)_\infty (q^5;q^5)_\infty^3}{q\,(q^{10};q^{10})_\infty^4},
$$

where $(a;x)_\infty = \prod_{n \ge 0} (1 - a x^n)$ is the infinite q-Pochhammer product.

## Sources

- Russelle Guadalupe, *New Proofs of Certain Theta Function Identities via Ramanujan's Function*, INTEGERS 26 (2026), Article A41, Lemma 3.

Stated but not proved: `MetaMathlibExt.ramanujanK_div_sub_div_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanKFunctionWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanKFunctionWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html#ramanujan-k-div-sub-div-sq).

## Modular equation of degree 2 for Ramanujan's function $k$

For every complex number $q$
with $|q| < 1$, the values $X = k(q)$ and $Y = k(q^2)$ of Ramanujan's function satisfy
$X^2 - Y + 2XY + X^2 Y + Y^2 = 0$.

## Sources

- Russelle Guadalupe, *New Proofs of Certain Theta Function Identities via Ramanujan's Function*, INTEGERS 26 (2026), Article A41, Theorem 4.

Stated but not proved: `MetaMathlibExt.ramanujanK_sq_relation` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanKFunctionWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanKFunctionWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html#ramanujan-k-sq-relation).

## Ramanujan's level-10 theta function identities

For complex $x$ with $|x| < 1$, let
$\varphi(x) = \sum_{n \in \mathbb{Z}} x^{n^2}$, $\psi(x) = \sum_{n \ge 0} x^{n(n+1)/2}$ and
$f(-x) = \prod_{n \ge 1} (1 - x^n)$, so that $f(x) = \prod_{n \ge 1} (1 - (-x)^n)$. Then for
every complex number $q$ with $|q| < 1$,

$$
\frac{\varphi(q)^5}{\varphi(q^5)} + \frac{\varphi(-q^2)^5}{\varphi(-q^{10})} +
2\,\frac{f(q)^5}{f(q^5)} = 4\,\frac{\psi(q)^5}{\psi(q^5)}
$$

and

$$
\varphi(q)^2 \varphi(q^5)^2 - \varphi(-q)^2 \varphi(-q^5)^2 - 16 q^3 \psi(q^2)^2 \psi(q^{10})^2 =
8 q\, f(-q^2)^2 f(-q^{10})^2.
$$

## Sources

- Russelle Guadalupe, *New Proofs of Certain Theta Function Identities via Ramanujan's Function*, INTEGERS 26 (2026), Article A41, Theorem 1, Equations (3) and (4).

Stated but not proved: `MetaMathlibExt.ramanujan_theta_level_ten` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamanujanKFunctionWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RamanujanKFunctionWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html#ramanujan-theta-level-ten).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ramanujan's function k](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/ramanujan-s-function-k)
