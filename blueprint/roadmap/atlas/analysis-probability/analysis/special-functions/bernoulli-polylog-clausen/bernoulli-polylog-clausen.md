---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry17Sec.ramanujan_part1_ch9_entry17_sec
statement: formalized
proof: formalized
---

# Bernoulli polynomials, polylogarithms and Clausen functions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/index.html).

Bernoulli and Euler polynomials and their generating-function identities, Berndt's φ_r and power-difference series, Clausen functions, the inverse tangent integral and dilogarithm identities; results whose content is values of ζ, Dirichlet L or β functions belong to NumberTheory.

## The inverse tangent integral at $\tan x$

Let $x$ be a real number with
$|x| \le \pi/4$, and let $P(x) = x \log|\tan x|$ for $x \ne 0$ and $P(0) = 0$. Then
$\cos x \ne 0$, the series
$T(x) = \sum_{k=0}^{\infty} (-1)^k \frac{\tan^{2k+1} x}{(2k+1)^2}$ (the inverse tangent integral
of $\tan x$) and $F(x) = \sum_{j=0}^{\infty} \frac{\sin((4j+2)x)}{(2j+1)^2}$ are both summable,
and $T(x) = P(x) + F(x)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry17Sec.ramanujan_part1_ch9_entry17_sec`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry17Sec.lean, line 1372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry17Sec.lean#L1372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/index.html#ramanujan-part1-ch9-entry17-sec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli polynomials, polylogarithms and Clausen functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/bernoulli-polylog-clausen/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/bernoulli-polylog-clausen)
