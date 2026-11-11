---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Function.SimpleFuncUniformApprox.eapprox_sub_lt_of_le, MathlibExt.MeasureTheory.Function.SimpleFuncUniformApprox.exists_monotone_tendsto
statement: formalized
proof: formalized
---

# Approximation by simple functions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/approximation-by-simple-functions/index.html).

## The standard simple approximations converge uniformly where the function is bounded

Let $\alpha$ be a measurable space and $f : \alpha \to [0, \infty]$ a measurable function. Let
$r_0, r_1, \ldots$ be the fixed enumeration of $\mathbb{Q}$ by natural-number codes ($r_k = 0$ when
$k$ codes no rational), put $q_k = \max(r_k, 0)$, and let
$\varphi_n(a) = \max(\{0\} \cup \{q_k : k < n,\ q_k \le f(a)\})$ be the $n$-th standard simple
approximation of $f$. Then for every $B \in [0, \infty)$ and every $\varepsilon \in (0, \infty]$
there is $N \in \mathbb{N}$ such that $f(a) - \varphi_n(a) < \varepsilon$ for all $n \ge N$ and
all $a \in \alpha$ with $f(a) \le B$, where subtraction in $[0, \infty]$ is truncated at $0$.

Formalized by `MathlibExt.MeasureTheory.Function.SimpleFuncUniformApprox.eapprox_sub_lt_of_le`, a theorem declared in [MathlibExt/MeasureTheory/Function/SimpleFuncUniformApprox.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/SimpleFuncUniformApprox.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/approximation-by-simple-functions/index.html#eapprox-sub-lt-of-le).

## Approximation of nonnegative measurable functions by simple functions

Let $\alpha$ be a
measurable space and $f : \alpha \to [0, \infty]$ a measurable function. There is a sequence of
simple functions $\varphi_n : \alpha \to [0, \infty]$ ($n \in \mathbb{N}$) such that:
(a) $\varphi_0 \le \varphi_1 \le \cdots \le f$ pointwise; (b) $\varphi_n(a) \to f(a)$ for every
$a \in \alpha$; and (c) for every $B \in [0, \infty)$ and every $\varepsilon \in (0, \infty]$ there
is $N \in \mathbb{N}$ such that $f(a) - \varphi_n(a) < \varepsilon$ for all $n \ge N$ and all
$a \in \alpha$ with $f(a) \le B$, where the subtraction in $[0, \infty]$ is truncated at $0$.

Formalized by `MathlibExt.MeasureTheory.Function.SimpleFuncUniformApprox.exists_monotone_tendsto`, a theorem declared in [MathlibExt/MeasureTheory/Function/SimpleFuncUniformApprox.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Function/SimpleFuncUniformApprox.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/approximation-by-simple-functions/index.html#exists-monotone-tendsto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximation by simple functions](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/integration/approximation-by-simple-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/MeasureTheory/integration/approximation-by-simple-functions)
