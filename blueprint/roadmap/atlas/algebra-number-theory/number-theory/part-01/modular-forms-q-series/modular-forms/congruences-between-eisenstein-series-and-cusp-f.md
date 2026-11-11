---
declaration: section
origin: cited
lean: MetaMathlibExt.eisenstein_congr_sum_delta_pow_mul_eisenstein, MetaMathlibExt.sigma_congr_sum_tau_conv_sigma, MetaMathlibExt.eisenstein_congr_delta_mul_eisenstein_dim_one, MetaMathlibExt.eisenstein_congr_delta_mul_eisenstein_dim_two, MetaMathlibExt.eisenstein_congr_delta_mul_eisenstein_dim_three
statement: formalized
---

# Congruences between Eisenstein series and cusp forms

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html).

## Lu's congruence for the Eisenstein series $G_k$

Let $k \ge 12$ be even with $k \ne 14$.
For $w, n \in \mathbb{N}$ let $\sigma_{-1}(n)$ be $1$ if $n = 0$ and $0$ otherwise; for $w \ge 1$
let $\sigma_{w-1}(0) = -B_w/(2w)$, where $B_w$ is the $w$-th Bernoulli number, and
$\sigma_{w-1}(n) = \sum_{d \mid n} d^{w-1}$ for $n \ge 1$. In $\mathbb{Q}[[q]]$ let
$G_w = \sum_{n \ge 0} \sigma_{w-1}(n) q^n$, let $E_w = G_w/\sigma_{w-1}(0)$ for even $w$, and let
$\Delta = q \prod_{j \ge 1} (1 - q^j)^{24}$; for $i, n \in \mathbb{N}$ write $b_i(n)$ for the
coefficient of $q^n$ in $\Delta^i E_{k-12i}$. Let $N_w = 1$ for $w \le 2$, let $N_w$ be the
absolute value of the numerator of $\sigma_{w-1}(0)$ for $w \ge 3$, and let $N'_k$ be the largest
divisor of $N_k$ that is coprime to $N_{k-12i}$ for every $1 \le i \le \lfloor k/12 \rfloor$. For
rationals $x, y$ and a positive integer $N$, $x \equiv y \pmod{N}$ means that $(x - y)/N$ has
denominator coprime to $N$. Let $m = \lfloor k/12 \rfloor - 1$ if
$k \equiv 2 \pmod{12}$ and $m = \lfloor k/12 \rfloor$ otherwise, let $C$ be the $m \times m$ matrix
$(b_i(j))_{1 \le i, j \le m}$, and let
$(\gamma_1, \dots, \gamma_m) = (\sigma_{k-1}(1), \dots, \sigma_{k-1}(m))\, C^{-1}$. Then
$\sigma_{k-1}(n) \equiv \sum_{i=1}^m \gamma_i b_i(n) \pmod{N'_k}$ for every $n \ge 0$, that is,
$G_k \equiv \sum_{i=1}^m \gamma_i \Delta^i E_{k-12i} \pmod{N'_k}$ coefficientwise.

## Sources

- Qing Lu, *Explicit Congruences for Modular Forms of Higher Weights*, Journal of Integer Sequences 29 (2026), Article 26.5.1, Theorem 1 (`jis-2026-26.5.1-thm-1`).

Stated but not proved: `MetaMathlibExt.eisenstein_congr_sum_delta_pow_mul_eisenstein` is written with `theorem_wanted` in [WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html#eisenstein-congr-sum-delta-pow-mul-eisen).

## Lu's congruence for the divisor sums $\sigma_{k-1}(n)$

Let $k \ge 12$ be even with
$k \ne 14$. For $w, n \in \mathbb{N}$ let $\sigma_{-1}(n)$ be $1$ if $n = 0$ and $0$ otherwise;
for $w \ge 1$ let $\sigma_{w-1}(0) = -B_w/(2w)$, where $B_w$ is the $w$-th Bernoulli number, and
$\sigma_{w-1}(n) = \sum_{d \mid n} d^{w-1}$ for $n \ge 1$. In $\mathbb{Q}[[q]]$ let
$G_w = \sum_{n \ge 0} \sigma_{w-1}(n) q^n$ and $\Delta = q \prod_{j \ge 1} (1 - q^j)^{24}$, and
for $i, n \in \mathbb{N}$ let $c_i(n)$ be the coefficient of $q^n$ in $\Delta^i G_{k-12i}$, that
is, the additive convolution $(\tau^{*i} * \sigma_{k-12i-1})(n)$, where $\tau(n)$ is the
coefficient of $q^n$ in $\Delta$. Let $N_w = 1$ for $w \le 2$, let $N_w$ be the absolute value of
the numerator of $\sigma_{w-1}(0)$ for $w \ge 3$, and let $N'_k$ be the largest divisor of $N_k$
that is coprime to $N_{k-12i}$ for every $1 \le i \le \lfloor k/12 \rfloor$. For rationals $x, y$
and a positive integer $N$, $x \equiv y \pmod{N}$ means that $(x - y)/N$ has denominator coprime
to $N$. Let $m = \lfloor k/12 \rfloor - 1$ if $k \equiv 2 \pmod{12}$ and
$m = \lfloor k/12 \rfloor$ otherwise, let $C$ be the $m \times m$ matrix
$\bigl(c_i(j)/\sigma_{k-12i-1}(0)\bigr)_{1 \le i, j \le m}$, and let
$(\gamma_1, \dots, \gamma_m) = (\sigma_{k-1}(1), \dots, \sigma_{k-1}(m))\, C^{-1}$. Then for every
$n \ge 1$, $\sigma_{k-1}(n) \equiv
\sum_{i=1}^m \bigl(\gamma_i/\sigma_{k-12i-1}(0)\bigr)\, c_i(n) \pmod{N'_k}$.

## Sources

- Qing Lu, *Explicit Congruences for Modular Forms of Higher Weights*, Journal of Integer Sequences 29 (2026), Article 26.5.1, Corollary 3 (`jis-2026-26.5.1-cor-3`).

Stated but not proved: `MetaMathlibExt.sigma_congr_sum_tau_conv_sigma` is written with `theorem_wanted` in [WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html#sigma-congr-sum-tau-conv-sigma).

## Lu's one-term congruence for $G_k$

Let $k \in \{12, 16, 18, 20, 22, 26\}$.
For $w, n \in \mathbb{N}$ let $\sigma_{-1}(n)$ be $1$ if $n = 0$ and $0$ otherwise; for $w \ge 1$
let $\sigma_{w-1}(0) = -B_w/(2w)$, where $B_w$ is the $w$-th Bernoulli number, and
$\sigma_{w-1}(n) = \sum_{d \mid n} d^{w-1}$ for $n \ge 1$. In $\mathbb{Q}[[q]]$ let
$G_w = \sum_{n \ge 0} \sigma_{w-1}(n) q^n$, let $E_w = G_w/\sigma_{w-1}(0)$ for even $w$, and let
$\Delta = q \prod_{j \ge 1} (1 - q^j)^{24}$; for $i, n \in \mathbb{N}$ write $b_i(n)$ for the
coefficient of $q^n$ in $\Delta^i E_{k-12i}$. Let $N_w = 1$ for $w \le 2$, let $N_w$ be the
absolute value of the numerator of $\sigma_{w-1}(0)$ for $w \ge 3$, and let $N'_k$ be the largest
divisor of $N_k$ that is coprime to $N_{k-12i}$ for every $1 \le i \le \lfloor k/12 \rfloor$. For
rationals $x, y$ and a positive integer $N$, $x \equiv y \pmod{N}$ means that $(x - y)/N$ has
denominator coprime to $N$. Then
$\sigma_{k-1}(n) \equiv b_1(n) \pmod{N'_k}$ for every $n \ge 0$, that is,
$G_k \equiv \Delta E_{k-12} \pmod{N'_k}$ coefficientwise; in particular the congruence holds for
every $n \ge 1$.

## Sources

- Qing Lu, *Explicit Congruences for Modular Forms of Higher Weights*, Journal of Integer Sequences 29 (2026), Article 26.5.1, Corollary 5 (`jis-2026-26.5.1-cor-5`).

Stated but not proved: `MetaMathlibExt.eisenstein_congr_delta_mul_eisenstein_dim_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html#eisenstein-congr-delta-mul-eisenstein-di).

## Lu's two-term congruence for $G_k$

Let $k \in \{24, 28, 30, 32, 34, 38\}$.
For $w, n \in \mathbb{N}$ let $\sigma_{-1}(n)$ be $1$ if $n = 0$ and $0$ otherwise; for $w \ge 1$
let $\sigma_{w-1}(0) = -B_w/(2w)$, where $B_w$ is the $w$-th Bernoulli number, and
$\sigma_{w-1}(n) = \sum_{d \mid n} d^{w-1}$ for $n \ge 1$. In $\mathbb{Q}[[q]]$ let
$G_w = \sum_{n \ge 0} \sigma_{w-1}(n) q^n$, let $E_w = G_w/\sigma_{w-1}(0)$ for even $w$, and let
$\Delta = q \prod_{j \ge 1} (1 - q^j)^{24}$; for $i, n \in \mathbb{N}$ write $b_i(n)$ for the
coefficient of $q^n$ in $\Delta^i E_{k-12i}$. Let $N_w = 1$ for $w \le 2$, let $N_w$ be the
absolute value of the numerator of $\sigma_{w-1}(0)$ for $w \ge 3$, and let $N'_k$ be the largest
divisor of $N_k$ that is coprime to $N_{k-12i}$ for every $1 \le i \le \lfloor k/12 \rfloor$. For
rationals $x, y$ and a positive integer $N$, $x \equiv y \pmod{N}$ means that $(x - y)/N$ has
denominator coprime to $N$. Let
$\gamma_2 = 2^{k-1} + 25 - 1/\sigma_{k-13}(0)$. Then
$\sigma_{k-1}(n) \equiv b_1(n) + \gamma_2 b_2(n) \pmod{N'_k}$ for every $n \ge 0$, that is,
$G_k \equiv \Delta E_{k-12} + \gamma_2 \Delta^2 E_{k-24} \pmod{N'_k}$ coefficientwise; in
particular the congruence holds for every $n \ge 1$.

## Sources

- Qing Lu, *Explicit Congruences for Modular Forms of Higher Weights*, Journal of Integer Sequences 29 (2026), Article 26.5.1, Corollary 6 (`jis-2026-26.5.1-cor-6`).

Stated but not proved: `MetaMathlibExt.eisenstein_congr_delta_mul_eisenstein_dim_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html#eisenstein-congr-delta-mul-eisenstein-di-2).

## Lu's three-term congruence for $G_k$

Let $k \in \{36, 40, 42, 44, 46, 50\}$.
For $w, n \in \mathbb{N}$ let $\sigma_{-1}(n)$ be $1$ if $n = 0$ and $0$ otherwise; for $w \ge 1$
let $\sigma_{w-1}(0) = -B_w/(2w)$, where $B_w$ is the $w$-th Bernoulli number, and
$\sigma_{w-1}(n) = \sum_{d \mid n} d^{w-1}$ for $n \ge 1$. In $\mathbb{Q}[[q]]$ let
$G_w = \sum_{n \ge 0} \sigma_{w-1}(n) q^n$, let $E_w = G_w/\sigma_{w-1}(0)$ for even $w$, and let
$\Delta = q \prod_{j \ge 1} (1 - q^j)^{24}$; for $i, n \in \mathbb{N}$ write $b_i(n)$ for the
coefficient of $q^n$ in $\Delta^i E_{k-12i}$. Let $N_w = 1$ for $w \le 2$, let $N_w$ be the
absolute value of the numerator of $\sigma_{w-1}(0)$ for $w \ge 3$, and let $N'_k$ be the largest
divisor of $N_k$ that is coprime to $N_{k-12i}$ for every $1 \le i \le \lfloor k/12 \rfloor$. For
rationals $x, y$ and a positive integer $N$, $x \equiv y \pmod{N}$ means that $(x - y)/N$ has
denominator coprime to $N$. Let
$\gamma_2 = 2^{k-1} + 25 - 1/\sigma_{k-13}(0)$ and
$\gamma_3 = 3^{k-1} + 48 \cdot 2^{k-1} + 949 - (2^{k-13} + 25)/\sigma_{k-13}(0) -
(2^{k-1} + 25)/\sigma_{k-25}(0) + 1/\bigl(\sigma_{k-13}(0)\,\sigma_{k-25}(0)\bigr)$. Then
$\sigma_{k-1}(n) \equiv b_1(n) + \gamma_2 b_2(n) + \gamma_3 b_3(n) \pmod{N'_k}$ for every
$n \ge 0$, that is,
$G_k \equiv \Delta E_{k-12} + \gamma_2 \Delta^2 E_{k-24} + \gamma_3 \Delta^3 E_{k-36}
\pmod{N'_k}$ coefficientwise; in particular the congruence holds for every $n \ge 1$.

## Sources

- Qing Lu, *Explicit Congruences for Modular Forms of Higher Weights*, Journal of Integer Sequences 29 (2026), Article 26.5.1, Corollary 7 (`jis-2026-26.5.1-cor-7`).

Stated but not proved: `MetaMathlibExt.eisenstein_congr_delta_mul_eisenstein_dim_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/EisensteinRamanujanCongruenceWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html#eisenstein-congr-delta-mul-eisenstein-di-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Congruences between Eisenstein series and cusp forms](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/modular-forms/congruences-between-eisenstein-series-and-cusp-f)
