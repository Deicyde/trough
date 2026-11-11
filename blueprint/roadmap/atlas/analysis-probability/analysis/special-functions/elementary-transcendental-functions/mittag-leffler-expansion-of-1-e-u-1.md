---
declaration: section
origin: cited
lean: MetaMathlibExt.one_div_exp_sub_one_eq_tsum, MetaMathlibExt.oneDivExpSubOneLaurentRemainder, MetaMathlibExt.differentiable_oneDivExpSubOneLaurentRemainder, MetaMathlibExt.oneDivExpSubOneLaurentRemainder_abs_le, MetaMathlibExt.abs_deriv_oneDivExpSubOneLaurentRemainder_le, MetaMathlibExt.abs_one_div_exp_sub_one_sub_laurent_le
statement: formalized
proof: formalized
---

# Mittag-Leffler expansion of 1/(e^u − 1)

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html).

## Mittag-Leffler expansion of $1/(e^u - 1)$

For every real number $u \neq 0$,

$$
\frac{1}{e^u - 1} = \frac{1}{u} - \frac{1}{2} + \sum_{m=1}^{\infty} \frac{2u}{u^2 + 4\pi^2 m^2}.
$$

Formalized by `MetaMathlibExt.one_div_exp_sub_one_eq_tsum`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html#one-div-exp-sub-one-eq-tsum).

## Remainder of the Laurent expansion of $1/(e^v - 1)$

For a natural number $N$, the
function $R_N : \mathbb{R} \to \mathbb{R}$ is defined by $R_N(0) = 0$ and, for $v \neq 0$,

$$
R_N(v) = \frac{1}{e^v - 1} - \frac{1}{v} + \frac{1}{2} -
  \sum_{n=0}^{N-1} \frac{B_{2n+2}}{(2n+2)!} v^{2n+1},
$$

where $B_k$ are the Bernoulli numbers. This is the remainder after truncating the Laurent
expansion of $1/(e^v - 1)$ at $0$ after its first $N$ terms of positive odd degree.

Formalized by `MetaMathlibExt.oneDivExpSubOneLaurentRemainder`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean, line 552](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean#L552). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html#one-div-exp-sub-one-laurent-remainder).

## The Laurent remainder of $1/(e^v - 1)$ is differentiable

For every natural number $N$,
the function $R_N : \mathbb{R} \to \mathbb{R}$ given by $R_N(0) = 0$ and, for $v \neq 0$,

$$
R_N(v) = \frac{1}{e^v - 1} - \frac{1}{v} + \frac{1}{2} -
  \sum_{n=0}^{N-1} \frac{B_{2n+2}}{(2n+2)!} v^{2n+1},
$$

where $B_k$ are the Bernoulli numbers, is differentiable at every point of $\mathbb{R}$.

Formalized by `MetaMathlibExt.differentiable_oneDivExpSubOneLaurentRemainder`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean, line 568](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean#L568). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html#differentiable-one-div-exp-sub-one-laure).

## Bound on the Laurent remainder of $1/(e^v - 1)$

For a natural number $N$, let
$R_N : \mathbb{R} \to \mathbb{R}$ be given by $R_N(0) = 0$ and, for $v \neq 0$,

$$
R_N(v) = \frac{1}{e^v - 1} - \frac{1}{v} + \frac{1}{2} -
  \sum_{n=0}^{N-1} \frac{B_{2n+2}}{(2n+2)!} v^{2n+1},
$$

where $B_k$ are the Bernoulli numbers. Then for every real number $v$,

$$
|R_N(v)| \le 2(2N + 3) \left( \sum_{m=0}^{\infty} \frac{1}{(2\pi(m + 1))^{2N+2}} \right) |v|^{2N+1}.
$$

Formalized by `MetaMathlibExt.oneDivExpSubOneLaurentRemainder_abs_le`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html#one-div-exp-sub-one-laurent-remainder-ab).

## Bound on the derivative of the Laurent remainder of $1/(e^v - 1)$

For a natural
number $N$, let $R_N : \mathbb{R} \to \mathbb{R}$ be given by $R_N(0) = 0$ and, for $v \neq 0$,

$$
R_N(v) = \frac{1}{e^v - 1} - \frac{1}{v} + \frac{1}{2} -
  \sum_{n=0}^{N-1} \frac{B_{2n+2}}{(2n+2)!} v^{2n+1},
$$

where $B_k$ are the Bernoulli numbers. Then for every real number $v$, the derivative of $R_N$
satisfies

$$
|R_N'(v)| \le 2(2N + 3) \left( \sum_{m=0}^{\infty} \frac{1}{(2\pi(m + 1))^{2N+2}} \right) |v|^{2N}.
$$

Formalized by `MetaMathlibExt.abs_deriv_oneDivExpSubOneLaurentRemainder_le`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html#abs-deriv-one-div-exp-sub-one-laurent-re).

## Global remainder bound for the Laurent expansion of $1/(e^v - 1)$

For every natural
number $N$ there is a constant $C \ge 0$ such that for every real number $v \neq 0$,

$$
\left| \frac{1}{e^v - 1} - \frac{1}{v} + \frac{1}{2} -
  \sum_{n=0}^{N-1} \frac{B_{2n+2}}{(2n+2)!} v^{2n+1} \right| \le C |v|^{2N+1},
$$

where $B_k$ are the Bernoulli numbers.

Formalized by `MetaMathlibExt.abs_one_div_exp_sub_one_sub_laurent_le`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean, line 599](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/ExpSubOneMittagLeffler.lean#L599). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html#abs-one-div-exp-sub-one-sub-laurent-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mittag-Leffler expansion of 1/(e^u − 1)](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/mittag-leffler-expansion-of-1-e-u-1)
