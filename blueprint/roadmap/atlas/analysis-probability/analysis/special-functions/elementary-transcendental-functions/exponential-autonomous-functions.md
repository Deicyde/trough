---
declaration: section
origin: cited
lean: MetaMathlibExt.completeBellPolynomial, MetaMathlibExt.completeExponentialAutonomousFunction
statement: formalized
proof: formalized
---

# Exponential autonomous functions

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-autonomous-functions/index.html).

## Complete Bell polynomials

For a sequence $x = (x_0, x_1, x_2, \dots)$ of complex numbers,
the complete Bell polynomials $B_n(x)$ are defined by $B_0(x) = 1$ and, for every $m \ge 0$,
$B_{m+1}(x) = \sum_{i=0}^{m} \binom{m}{i} B_{m-i}(x) \, x_i$.

Writing $x_i = y_{i+1}$, this is the usual recurrence for $B_{m+1}(y_1, \dots, y_{m+1})$.

Formalized by `MetaMathlibExt.completeBellPolynomial`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/CompleteExponentialAutonomousFunction.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CompleteExponentialAutonomousFunction.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-autonomous-functions/index.html#complete-bell-polynomial).

## Complete exponential autonomous functions

Let $k \ge 1$, $a \in \mathbb{C}$ and
$x_0, \dots, x_{k-1} \in \mathbb{C}$. The complete exponential autonomous function of order $k$
with parameter $a$ and variables $x$ is the sequence $f_0, f_1, f_2, \dots$ of complex numbers
given by $f_n = x_n$ for $n < k$, $f_k = a e^{x_0}$, and $f_n = a e^{x_0} B_{n-k}(y)$ for
$n > k$, where $B_{n-k}$ is the complete Bell polynomial and $y$ is the sequence with
$y_i = f_{i+1}$ (so only $f_1, \dots, f_{n-k}$ enter).

Formalized by `MetaMathlibExt.completeExponentialAutonomousFunction`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/CompleteExponentialAutonomousFunction.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CompleteExponentialAutonomousFunction.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-autonomous-functions/index.html#complete-exponential-autonomous-function).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Exponential autonomous functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-autonomous-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/exponential-autonomous-functions)
