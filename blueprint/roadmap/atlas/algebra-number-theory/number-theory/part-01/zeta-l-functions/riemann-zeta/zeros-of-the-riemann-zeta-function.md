---
declaration: section
origin: cited
lean: MetaMathlibExt.zetaZeroCount, MetaMathlibExt.bellotti_wong_zero_count_bound, MetaMathlibExt.bellotti_wong_zero_count_bound_small, MetaMathlibExt.platt_trudgian_rh_to_height
statement: formalized
---

# Zeros of the Riemann zeta function

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function/index.html).

## Zero-counting function of the Riemann zeta function

For a real number $T$, $N(T)$ is
the number of zeros $\rho = \beta + i\gamma$ of the Riemann zeta function with $0 < \beta < 1$
and $0 < \gamma \le T$, each counted with its multiplicity as a zero.

Formalized by `MetaMathlibExt.zetaZeroCount`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/BellottiWongZeroCountWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BellottiWongZeroCountWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function/index.html#zeta-zero-count).

## First Bellotti–Wong bound on the zero-counting function

For every real number
$T \ge e$, the number $N(T)$ of zeros $\rho = \beta + i\gamma$ of the Riemann zeta function with
$0 < \beta < 1$ and $0 < \gamma \le T$, counted with multiplicity, satisfies

$$
N(T) \le \frac{T}{2\pi} \log \frac{T}{2\pi e} + 0.10076 \log T + 0.24460 \log \log T + 8.08344.
$$

This bound is sharper than the second Bellotti–Wong bound for $T$ above about $e^{447.981}$.

Stated but not proved: `MetaMathlibExt.bellotti_wong_zero_count_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/BellottiWongZeroCountWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BellottiWongZeroCountWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function/index.html#bellotti-wong-zero-count-bound).

## Second Bellotti–Wong bound on the zero-counting function

For every real number
$T \ge e$, the number $N(T)$ of zeros $\rho = \beta + i\gamma$ of the Riemann zeta function with
$0 < \beta < 1$ and $0 < \gamma \le T$, counted with multiplicity, satisfies

$$
N(T) \le \frac{T}{2\pi} \log \frac{T}{2\pi e} + 0.11200 \log T + 0.12567 \log \log T + 3.77417.
$$

This bound is sharper than the first Bellotti–Wong bound for $T$ below about $e^{447.981}$.

Stated but not proved: `MetaMathlibExt.bellotti_wong_zero_count_bound_small` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/BellottiWongZeroCountWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BellottiWongZeroCountWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function/index.html#bellotti-wong-zero-count-bound-small).

## Platt–Trudgian verification of the Riemann hypothesis to height $3 \cdot 10^{12}$

Every
zero $\rho$ of the Riemann zeta function with $0 < \operatorname{Im} \rho \le 3000175332800$
satisfies $\operatorname{Re} \rho = 1/2$.

Stated but not proved: `MetaMathlibExt.platt_trudgian_rh_to_height` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/PlattTrudgianRiemannHypothesisWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/PlattTrudgianRiemannHypothesisWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function/index.html#platt-trudgian-rh-to-height).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zeros of the Riemann zeta function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/zeros-of-the-riemann-zeta-function)
