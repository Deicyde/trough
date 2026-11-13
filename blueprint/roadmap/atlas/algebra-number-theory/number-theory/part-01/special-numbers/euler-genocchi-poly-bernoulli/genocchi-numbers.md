---
declaration: section
origin: cited
lean: MetaMathlibExt.genocchiPowerSeries, MetaMathlibExt.genocchiNumber, MetaMathlibExt.genocchiPowerSeries_eq, MetaMathlibExt.genocchiNumber_eq, MetaMathlibExt.genocchiNumber_eq_bernoulli, MetaMathlibExt.genocchiNumberViaBernoulli_eq_genocchiNumber, MathlibExt.NumberTheory.GenocchiExplicitWanted.diffPowEval, MathlibExt.NumberTheory.GenocchiExplicitWanted.zerroU
statement: formalized
---

# Genocchi numbers

14 results, 9 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html).

## Generating function of the Genocchi numbers

The Genocchi power series is the formal power
series $\frac{2x}{e^x + 1} = 2x \cdot (e^x + 1)^{-1}$ in $\mathbb{Q}[[x]]$, where
$e^x = \sum_{n \ge 0} x^n / n!$ is the exponential power series and $(e^x + 1)^{-1}$ is the inverse
of $e^x + 1$ among formal power series. It is the exponential generating function of the Genocchi
numbers $G_n$, that is, $\frac{2x}{e^x + 1} = \sum_{n \ge 0} G_n \frac{x^n}{n!}$.

This retains the standard convention $\frac{2x}{e^x + 1}$ stated by Chen and used independently by
Kida; the sign-changed variant consumes only even-index terms, where the conventions agree.

## Sources

- Chen, JIS VOL6 (`chen50.tex`, lines 296-300): https://cs.uwaterloo.ca/journals/JIS/VOL6/Chen/chen50.html
- Kida, JIS VOL16: https://cs.uwaterloo.ca/journals/JIS/VOL16/Kida/kida2.html

Formalized by `MetaMathlibExt.genocchiPowerSeries`, a definition declared in [MathlibExt/NumberTheory/GenocchiNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GenocchiNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-power-series).

## Genocchi numbers

For a natural number $n$, the Genocchi number $G_n \in \mathbb{Q}$ is
$n!$ times the coefficient of $x^n$ in the Genocchi power series
$\frac{2x}{e^x + 1} \in \mathbb{Q}[[x]]$, so that
$\frac{2x}{e^x + 1} = \sum_{n \ge 0} G_n \frac{x^n}{n!}$.

## Sources

- Chen, JIS VOL6 (`chen50.tex`, lines 296-300): https://cs.uwaterloo.ca/journals/JIS/VOL6/Chen/chen50.html
- Kida, JIS VOL16: https://cs.uwaterloo.ca/journals/JIS/VOL16/Kida/kida2.html

Formalized by `MetaMathlibExt.genocchiNumber`, a definition declared in [MathlibExt/NumberTheory/GenocchiNumber.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GenocchiNumber.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-number).

## The Genocchi power series is $2x/(e^x + 1)$

The Genocchi power series equals
$2x \cdot (e^x + 1)^{-1}$ in $\mathbb{Q}[[x]]$, where $e^x = \sum_{n \ge 0} x^n / n!$ is the
exponential power series and $(e^x + 1)^{-1}$ is the inverse of $e^x + 1$ among formal power
series.

Formalized by `MetaMathlibExt.genocchiPowerSeries_eq`, a theorem declared in [MathlibExt/NumberTheory/GenocchiNumber.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GenocchiNumber.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-power-series-eq).

## Genocchi numbers from their generating function

For every natural number $n$, the
Genocchi number $G_n$ equals $n!$ times the coefficient of $x^n$ in the Genocchi power series
$\frac{2x}{e^x + 1} \in \mathbb{Q}[[x]]$.

Formalized by `MetaMathlibExt.genocchiNumber_eq`, a theorem declared in [MathlibExt/NumberTheory/GenocchiNumber.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GenocchiNumber.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-number-eq).

## Genocchi numbers in terms of Bernoulli numbers

For every natural number $n$, the Genocchi
number $G_n$, defined by $\frac{2x}{e^x + 1} = \sum_{m \ge 0} G_m \frac{x^m}{m!}$, satisfies
$G_n = 2(1 - 2^n) B_n$, where $B_n$ is the $n$-th Bernoulli number with the convention
$B_1 = -\tfrac{1}{2}$.

Formalized by `MetaMathlibExt.genocchiNumber_eq_bernoulli`, a theorem declared in [MathlibExt/NumberTheory/GenocchiBernoulli.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GenocchiBernoulli.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-number-eq-bernoulli).

## The two definitions of the Genocchi numbers agree

For every natural number $n$, the
rational number $2(1 - 2^n) B_n$, where $B_n$ is the $n$-th Bernoulli number with the convention
$B_1 = -\tfrac{1}{2}$, equals the Genocchi number $G_n$ defined by the exponential generating
function $\frac{2x}{e^x + 1} = \sum_{m \ge 0} G_m \frac{x^m}{m!}$.

Formalized by `MetaMathlibExt.genocchiNumberViaBernoulli_eq_genocchiNumber`, a theorem declared in [MathlibExt/NumberTheory/GenocchiBernoulli.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GenocchiBernoulli.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-number-via-bernoulli-eq-genocch).

## Iterated forward differences of a power on $\mathbb{Q}$

For a rational number $x$ and
natural numbers $k$ and $n$, $\Delta^k x^n$ denotes the value at $x$ of the $k$-th iterate of the
forward difference operator applied to the function $y \mapsto y^n$ on $\mathbb{Q}$, where the
forward difference of $f \colon \mathbb{Q} \to \mathbb{Q}$ is the function
$y \mapsto f(y + 1) - f(y)$.

Formalized by `MathlibExt.NumberTheory.GenocchiExplicitWanted.diffPowEval`, a definition declared in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#diff-pow-eval).

## The Zerroukhat–Khaldi sum $U(m, k)$

For natural numbers $m$ and $k$, define the rational
number

$$U(m, k) = \sum_{j=0}^{m} (-1)^{k+j+m} \frac{(k+j-1)!}{2^{k+j-1}} S(m, j),$$

where $S(m, j)$ is the Stirling number of the second kind and, in the term with $k = j = 0$,
$k + j - 1$ is read as $0$, so that this term is $(-1)^m S(m, 0)$.

Formalized by `MathlibExt.NumberTheory.GenocchiExplicitWanted.zerroU`, a definition declared in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#zerro-u).

## The Zerroukhat–Khaldi sum $H_{n,m}$

For natural numbers $n$ and $m$, define the rational
number

$$H_{n,m} = (-1)^n \, n \sum_{k=1}^{n-m} U(m+1, k) \, S(n-m, k),$$

where $U(m+1, k)$ is the Zerroukhat–Khaldi sum $U$, $S(n-m, k)$ is the Stirling number of the
second kind, and $n - m$ is truncated at $0$, so that $H_{n,m} = 0$ when $m \ge n$.

Formalized by `MathlibExt.NumberTheory.GenocchiExplicitWanted.zerroH`, a definition declared in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#zerro-h).

## Explicit formula for Genocchi numbers via Stirling numbers

Let $n$ and $r$ be positive
integers with $n \ge r + 1$, let $G_n$ be the $n$-th Genocchi number and let $S(a, b)$ denote
the Stirling numbers of the second kind. For $k \ge 1$ write
$c_k = \sum_{j=0}^{r} (-1)^{k+j+r} \frac{(k+j-1)!}{2^{k+j-1}} S(r, j)$. Then
$G_n = (-1)^n \, n \sum_{k=1}^{n-r} c_k \, S(n-r, k)$.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.GenocchiExplicitWanted.genocchiNumber_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#genocchi-number-eq-sum).

## Bernoulli numbers via forward differences at $0$

Let $n$ and $r$ be positive integers
with $n \ge r + 1$, let $B_n$ be the $n$-th Bernoulli number, let $S(a, b)$ denote the Stirling
numbers of the second kind and let $\Delta^k 0^m$ be the $k$-th forward difference of
$y \mapsto y^m$ at $0$. For $k \ge 1$ write
$d_k = \sum_{j=0}^{r} (-1)^{k+j+r+1} \, 2^{r-j} \, \frac{(k+j-1)!}{k!} \, S(r, j)$. Then
$(-1)^n B_n = \frac{n}{2^n - 1} \sum_{k=1}^{n-r} d_k \, \frac{\Delta^k 0^{n-r}}{2^{k+r}}$.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.GenocchiExplicitWanted.neg_one_pow_mul_bernoulli_eq_sum_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#neg-one-pow-mul-bernoulli-eq-sum-zero).

## Bernoulli numbers via forward differences at $1$

Let $n$ and $r$ be positive integers
with $n \ge r + 1$, let $B_n$ be the $n$-th Bernoulli number, let $S(a, b)$ denote the Stirling
numbers of the second kind and let $\Delta^k 1^m$ be the $k$-th forward difference of
$y \mapsto y^m$ at $1$. For $k \ge 0$ write
$e_k = \sum_{j=0}^{r} (-1)^{k+j+r} \, 2^{r-j} \, \frac{(k+j)!}{k!} \, S(r, j)$. Then
$(-1)^n B_n = \frac{n}{2^n - 1} \sum_{k=0}^{n-1-r} e_k \, \frac{\Delta^k 1^{n-1-r}}{2^{k+1+r}}$.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.GenocchiExplicitWanted.neg_one_pow_mul_bernoulli_eq_sum_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#neg-one-pow-mul-bernoulli-eq-sum-one).

## Recurrence for the Zerroukhat–Khaldi sums $U$

Let $U(m, k)$ be the Zerroukhat–Khaldi
sum. For all natural numbers $r$ and $k$ with $k \ge 1$,
$U(r+1, k) = U(r, k+1) + k \, U(r, k)$.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.GenocchiExplicitWanted.zerroU_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#zerro-u-succ).

## A step identity for the Zerroukhat–Khaldi sums $H_{n,m}$

Let $H_{n,m}$ denote the
Zerroukhat–Khaldi sum. For all natural numbers $n$ and $r$ with $r \ge 1$ and $n \ge r + 1$,
$H_{n,r} = H_{n,r-1}$.

## Sources

- Schehrazade Zerroukhat and Laala Khaldi, "A Note on Explicit Formulas for Bernoulli and Genocchi Numbers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.GenocchiExplicitWanted.zerroH_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GenocchiExplicitWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GenocchiExplicitWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html#zerro-h-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Genocchi numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/genocchi-numbers)
