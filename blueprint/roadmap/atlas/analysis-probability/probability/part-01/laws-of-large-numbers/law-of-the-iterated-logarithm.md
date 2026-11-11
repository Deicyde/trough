---
declaration: section
origin: cited
lean: MathlibExt.Probability.LawIteratedLogarithmWanted.law_of_the_iterated_logarithm_of_memLp, MathlibExt.Probability.LawIteratedLogarithmWanted.law_of_the_iterated_logarithm
statement: formalized
proof: formalized
---

# Law of the iterated logarithm

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/law-of-the-iterated-logarithm/index.html).

## Law of the iterated logarithm, square-integrable form

Let $X_0, X_1, \dots$ be independent,
identically distributed, measurable real random variables on a probability space with
$\mathbb{E}[X_0^2] < \infty$, $\mathbb{E}[X_0] = 0$ and $\operatorname{Var}(X_0) = 1$, and let
$S_n = X_0 + \dots + X_{n-1}$. Then almost surely
$\limsup_{n \to \infty} S_n / \sqrt{2 n \log \log n} = 1$ and
$\liminf_{n \to \infty} S_n / \sqrt{2 n \log \log n} = -1$.

Integrability of $X_0$ is not assumed separately, since it follows from square integrability on a
probability space.

Formalized by `MathlibExt.Probability.LawIteratedLogarithmWanted.law_of_the_iterated_logarithm_of_memLp`, a theorem declared in [MathlibExt/Probability/LawIteratedLogarithm.lean, line 3235](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LawIteratedLogarithm.lean#L3235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/law-of-the-iterated-logarithm/index.html#law-of-the-iterated-logarithm-of-mem-lp).

## Law of the iterated logarithm

Let $X_0, X_1, \dots$ be independent, identically distributed,
measurable real random variables on a probability space such that $X_0$ is integrable,
$\mathbb{E}[X_0^2] < \infty$, $\mathbb{E}[X_0] = 0$ and $\operatorname{Var}(X_0) = 1$, and let
$S_n = X_0 + \dots + X_{n-1}$. Then almost surely
$\limsup_{n \to \infty} S_n / \sqrt{2 n \log \log n} = 1$ and
$\liminf_{n \to \infty} S_n / \sqrt{2 n \log \log n} = -1$.

Proof: Hartman–Wintner truncation and exponential maximal bounds give the upper half; a CLT block
argument and the second Borel–Cantelli lemma give the lower half.

## Sources

- A. Y. Khinchin 1924, A. N. Kolmogorov 1929, P. Hartman and A. Wintner, On the law of the iterated logarithm, Amer. J. Math. 63 (1941) 169–176; textbook in Durrett, Probability Theory and Examples, 5th ed., Foundations of Modern Probability (Hartman-Wintner LIL). Lean i.i.d. mean-zero variance-one normalized `√(2 n log log n)` form.

Formalized by `MathlibExt.Probability.LawIteratedLogarithmWanted.law_of_the_iterated_logarithm`, a theorem declared in [MathlibExt/Probability/LawIteratedLogarithm.lean, line 3346](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LawIteratedLogarithm.lean#L3346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/law-of-the-iterated-logarithm/index.html#law-of-the-iterated-logarithm).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Law of the iterated logarithm](https://deicyde.github.io/atlas-lean/roadmap/Probability/laws-of-large-numbers/law-of-the-iterated-logarithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/laws-of-large-numbers/law-of-the-iterated-logarithm)
