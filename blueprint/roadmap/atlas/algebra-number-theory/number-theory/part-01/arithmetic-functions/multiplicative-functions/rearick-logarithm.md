---
declaration: section
origin: cited
lean: MetaMathlibExt.rearickLog, MetaMathlibExt.rearickLog_eq_pmul_log_mul_dirichletInverse, MetaMathlibExt.rearick_log_eq_zero_iff_isMultiplicative
statement: formalized
proof: formalized
---

# Rearick logarithm

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/rearick-logarithm/index.html).

## Rearick logarithm

Let $f$ be a real-valued arithmetic function with $f(1) > 0$, and let
$f^{-1}$ be its Dirichlet inverse. The Rearick logarithm of $f$ is the arithmetic function $L(f)$
with $L(f)(0) = 0$, $L(f)(1) = \log f(1)$, and
$L(f)(n) = \sum_{d \mid n} f(d) \, f^{-1}(n/d) \log d$ for $n > 1$.

Formalized by `MetaMathlibExt.rearickLog`, a definition declared in [MathlibExt/NumberTheory/RearickLogarithm.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RearickLogarithm.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/rearick-logarithm/index.html#rearick-log).

## The Rearick logarithm as a Dirichlet convolution

Let $f$ be a real-valued arithmetic
function with $f(1) = 1$, and let $f^{-1}$ be its Dirichlet inverse. Then the Rearick logarithm
of $f$ is the Dirichlet convolution of the pointwise product $n \mapsto f(n) \log n$ with
$f^{-1}$.

Formalized by `MetaMathlibExt.rearickLog_eq_pmul_log_mul_dirichletInverse`, a theorem declared in [MathlibExt/NumberTheory/RearickLogarithm.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RearickLogarithm.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/rearick-logarithm/index.html#rearick-log-eq-pmul-log-mul-dirichlet-in).

## Rearick's characterization of multiplicative functions

Let $f$ be a real-valued arithmetic
function with $f(1) > 0$, and let $L(f)$ be its Rearick logarithm. Then $f$ is multiplicative
(that is, $f(1) = 1$ and $f(mn) = f(m) f(n)$ whenever $m$ and $n$ are coprime) if and only if
$L(f)(m) = 0$ for every natural number $m$ that is not a prime power, including $m = 0$ and
$m = 1$.

## Sources

- Rearick logarithm support characterization of multiplicative arithmetic functions, after Huilan Li and Trueman MacHenry, arXiv:1009.1892v1, <https://arxiv.org/abs/1009.1892>, lines 444-450 (Rearick logarithm definition) and 706-708 (Rearick Theorem 4). Real-valued domain closure with `f 1 > 0` after Pong, arXiv:1504.03263v2, <https://arxiv.org/abs/1504.03263>, lines 174-195; positivity also supplies the nonzero premise for the Dirichlet inverse.

Formalized by `MetaMathlibExt.rearick_log_eq_zero_iff_isMultiplicative`, a theorem declared in [MathlibExt/NumberTheory/RearickLogarithm.lean, line 574](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/RearickLogarithm.lean#L574). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/rearick-logarithm/index.html#rearick-log-eq-zero-iff-is-multiplicativ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rearick logarithm](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/rearick-logarithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/rearick-logarithm)
