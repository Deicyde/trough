---
declaration: section
origin: cited
lean: MathlibExt.Probability.EfronStein.efron_stein_finite_iid_general, MathlibExt.Probability.EfronStein.efron_stein_finite_iid
statement: formalized
proof: formalized
---

# Efron–Stein inequality

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/efron-stein-inequality/index.html).

## Efron–Stein inequality for a finite product weight

Let $\alpha$ be a finite nonempty set,
let $p : \alpha \to \mathbb{R}$ satisfy $p(a) \ge 0$ for every $a \in \alpha$ and
$\sum_{a \in \alpha} p(a) = 1$, let $n \in \mathbb{N}$ and let $f : \alpha^n \to \mathbb{R}$. For
$x = (x_1, \dots, x_n) \in \alpha^n$ write $w(x) = \prod_{j=1}^{n} p(x_j)$, and for a coordinate
$i \in \{1, \dots, n\}$ and $a \in \alpha$ let $x^{(i,a)}$ be $x$ with its $i$-th coordinate
replaced by $a$. Let $\mu = \sum_{x \in \alpha^n} w(x) f(x)$. Then

$$
\sum_{x \in \alpha^n} w(x) \bigl(f(x) - \mu\bigr)^2 \le \frac{1}{2} \sum_{i=1}^{n}
\sum_{x \in \alpha^n} \sum_{a \in \alpha} w(x)\, p(a) \bigl(f(x) - f(x^{(i,a)})\bigr)^2.
$$

Formalized by `MathlibExt.Probability.EfronStein.efron_stein_finite_iid_general`, a theorem declared in [MathlibExt/Probability/EfronStein.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/EfronStein.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/efron-stein-inequality/index.html#efron-stein-finite-iid-general).

## Efron–Stein inequality for finite i.i.d. coordinates

Let $\alpha$ be a finite nonempty set,
let $p : \alpha \to \mathbb{R}$ satisfy $p(a) \ge 0$ for every $a \in \alpha$ and
$\sum_{a \in \alpha} p(a) = 1$, let $n \in \mathbb{N}$ and let $f : \alpha^n \to \mathbb{R}$. For
$x = (x_1, \dots, x_n) \in \alpha^n$ write $w(x) = \prod_{j=1}^{n} p(x_j)$, and for a coordinate
$i \in \{1, \dots, n\}$ and $a \in \alpha$ let $x^{(i,a)}$ be $x$ with its $i$-th coordinate
replaced by $a$. Let $\mu = \sum_{x \in \alpha^n} w(x) f(x)$. Then

$$
\sum_{x \in \alpha^n} w(x) \bigl(f(x) - \mu\bigr)^2 \le \frac{1}{2} \sum_{i=1}^{n}
\sum_{x \in \alpha^n} \sum_{a \in \alpha} w(x)\, p(a) \bigl(f(x) - f(x^{(i,a)})\bigr)^2.
$$

In words: the variance of $f$ under the product weight is at most half the expected sum of squared
differences under independent resampling of each coordinate.

## Sources

- B. Efron and C. Stein, "The Jackknife Estimate of Variance", Annals of Statistics 9 (1981), DOI 10.1214/aos/1176345462. It follows from `efron_stein_finite_iid_general`; the instance `[DecidableEq α]` is unused and keeps the source's shape.

Formalized by `MathlibExt.Probability.EfronStein.efron_stein_finite_iid`, a theorem declared in [MathlibExt/Probability/EfronStein.lean, line 628](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/EfronStein.lean#L628). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/efron-stein-inequality/index.html#efron-stein-finite-iid).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Efron–Stein inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/concentration-inequalities/efron-stein-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/concentration-inequalities/efron-stein-inequality)
