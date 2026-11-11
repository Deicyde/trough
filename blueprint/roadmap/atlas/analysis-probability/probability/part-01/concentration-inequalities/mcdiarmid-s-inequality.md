---
declaration: section
origin: cited
lean: MathlibExt.Probability.McDiarmid.mcdiarmid_one_sided_finite_iid_general, MathlibExt.Probability.McDiarmid.mcdiarmid_one_sided_finite_iid_of_sum_sq_eq_zero, MathlibExt.Probability.McDiarmid.mcdiarmid_one_sided_finite_iid
statement: formalized
proof: formalized
---

# McDiarmid's inequality

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/mcdiarmid-s-inequality/index.html).

## McDiarmid's inequality when the sensitivities are not all zero

Let $n \in \mathbb{N}$,
let $\alpha$ be a finite nonempty set with weights $p : \alpha \to \mathbb{R}$ such that
$p(a) \ge 0$ for all $a$ and $\sum_{a \in \alpha} p(a) = 1$, and give each $x \in \alpha^n$ the
product weight $P(x) = \prod_{i\lt n} p(x_i)$. Let $f : \alpha^n \to \mathbb{R}$ and let
$c_0, \dots, c_{n-1} \ge 0$ be such that $|f(x) - f(y)| \le c_i$ whenever $x, y \in \alpha^n$
agree in every coordinate other than $i$, and suppose $\sum_{i\lt n} c_i^2 > 0$. Write
$\mu = \sum_{x \in \alpha^n} P(x) f(x)$ for the mean of $f$. Then for every real $t > 0$,

$$
\sum_{x \in \alpha^n,\ f(x) - \mu \ge t} P(x) \le \exp\Big(-\frac{2t^2}{\sum_{i\lt n} c_i^2}\Big).
$$

Formalized by `MathlibExt.Probability.McDiarmid.mcdiarmid_one_sided_finite_iid_general`, a theorem declared in [MathlibExt/Probability/McDiarmid.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/McDiarmid.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/mcdiarmid-s-inequality/index.html#mcdiarmid-one-sided-finite-iid-general).

## The upper tail vanishes when every sensitivity is zero

Let $n \in \mathbb{N}$, let
$\alpha$ be a finite nonempty set with weights $p : \alpha \to \mathbb{R}$ such that
$p(a) \ge 0$ for all $a$ and $\sum_{a \in \alpha} p(a) = 1$, and give each $x \in \alpha^n$ the
product weight $P(x) = \prod_{i\lt n} p(x_i)$. Let $f : \alpha^n \to \mathbb{R}$ and let
$c_0, \dots, c_{n-1} \ge 0$ be such that $|f(x) - f(y)| \le c_i$ whenever $x, y \in \alpha^n$
agree in every coordinate other than $i$, and suppose $\sum_{i\lt n} c_i^2 = 0$. Write
$\mu = \sum_{x \in \alpha^n} P(x) f(x)$ for the mean of $f$. Then for every real $t > 0$,

$$
\sum_{x \in \alpha^n,\ f(x) - \mu \ge t} P(x) = 0.
$$

Indeed, changing one coordinate never changes $f$, so the upper tail is empty.

Formalized by `MathlibExt.Probability.McDiarmid.mcdiarmid_one_sided_finite_iid_of_sum_sq_eq_zero`, a theorem declared in [MathlibExt/Probability/McDiarmid.lean, line 389](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/McDiarmid.lean#L389). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/mcdiarmid-s-inequality/index.html#mcdiarmid-one-sided-finite-iid-of-sum-sq).

## McDiarmid's bounded-differences inequality, finite i.i.d. case

Let $n \in \mathbb{N}$, let
$\alpha$ be a finite nonempty set with weights $p : \alpha \to \mathbb{R}$ such that
$p(a) \ge 0$ for all $a$ and $\sum_{a \in \alpha} p(a) = 1$, and give each $x \in \alpha^n$ the
product weight $P(x) = \prod_{i\lt n} p(x_i)$. Let $f : \alpha^n \to \mathbb{R}$ and let
$c_0, \dots, c_{n-1} \ge 0$ be such that $|f(x) - f(y)| \le c_i$ whenever $x, y \in \alpha^n$
agree in every coordinate other than $i$. Write $\mu = \sum_{x \in \alpha^n} P(x) f(x)$ for the
mean of $f$. Then for every real $t > 0$,

$$
\sum_{x \in \alpha^n,\ f(x) - \mu \ge t} P(x) \le \exp\Big(-\frac{2t^2}{\sum_{i\lt n} c_i^2}\Big),
$$

where a quotient by $0$ is read as $0$, so the bound is $1$ when every $c_i$ is $0$.

## Sources

- C. McDiarmid, Surveys in Combinatorics 1989, 148-188, DOI 10.1017/CBO9781107359949.008. When every `c i` is `0` (including `n = 0`), the right-hand side is `Real.exp 0 = 1` by Lean's convention `x / 0 = 0`; `mcdiarmid_one_sided_finite_iid_of_sum_sq_eq_zero` gives the sharp value `prob = 0` there, and `mcdiarmid_one_sided_finite_iid_general` covers `0 < ∑ i, c i ^ 2`. The instance `[DecidableEq α]` is unused and keeps the source's shape.

Formalized by `MathlibExt.Probability.McDiarmid.mcdiarmid_one_sided_finite_iid`, a theorem declared in [MathlibExt/Probability/McDiarmid.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/McDiarmid.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/mcdiarmid-s-inequality/index.html#mcdiarmid-one-sided-finite-iid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: McDiarmid's inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/mcdiarmid-s-inequality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/concentration-inequalities/mcdiarmid-s-inequality)
