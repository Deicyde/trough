---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry16Tan.ramanujan_part1_ch9_entry16_tan, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry16Tanseries.chapter9Entry16DifferenceTerm, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry16Tanseries.ramanujan_part1_ch9_entry16_tanseries, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry19Catalangf.ramanujan_part1_ch9_entry19_catalangf, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry31Ramanujansum.ramanujan_part1_ch9_entry31_ramanujansum
statement: formalized
proof: formalized
---

# Central binomial series in trigonometric arguments

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html).

## The central binomial series in $\sin x$ and $x \log|2\sin x|$

Let $x$ be a real number
with $|x| \le \pi/2$, and let $L(x) = x \log|2\sin x|$ for $x \ne 0$ and $L(0) = 0$. Then
$|2\sin x| > 0$ if $x \ne 0$, the series
$S(x) = \sum_{k=0}^{\infty} \binom{2k}{k} \frac{\sin^{2k+1} x}{2^{2k} (2k+1)^2}$ and
$F(x) = \sum_{k=1}^{\infty} \frac{\sin 2kx}{k^2}$ are both summable, and
$S(x) = L(x) + \frac{1}{2} F(x)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry16Tan.ramanujan_part1_ch9_entry16_tan`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry16Tan.lean, line 1888](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry16Tan.lean#L1888). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html#ramanujan-part1-ch9-entry16-tan).

## Terms of the cosine-minus-sine central binomial series

For a real number $x$ and a
natural number $k$, the $k$-th term is
$\binom{2k}{k} \frac{\cos^{2k+1} x - \sin^{2k+1} x}{2^{2k} (2k+1)^2}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9, Entry 16.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry16Tanseries.chapter9Entry16DifferenceTerm`, a definition declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry16Tanseries.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry16Tanseries.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html#chapter9-entry16-difference-term).

## The central binomial series in $\cos x$ minus that in $\sin x$

Let $x$ be a real number
with $0 \le x \le \pi/4$, and for real $y$ let
$S(y) = \sum_{k=0}^{\infty} \binom{2k}{k} \frac{\sin^{2k+1} y}{2^{2k} (2k+1)^2}$. Then
$2\cos x > 0$, the series
$D(x) = \sum_{k=0}^{\infty} \binom{2k}{k} \frac{\cos^{2k+1} x - \sin^{2k+1} x}
{2^{2k} (2k+1)^2}$ and the series defining $S(2x)$ are both summable, and
$D(x) = \frac{\pi}{2} \log(2\cos x) - \frac{1}{2} S(2x)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry16Tanseries.ramanujan_part1_ch9_entry16_tanseries`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry16Tanseries.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry16Tanseries.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html#ramanujan-part1-ch9-entry16-tanseries).

## The central binomial series in $\cos x$ plus that in $\sin x$

Let $x$ be a real number
with $0 \le x \le \pi/4$. Then $2\cos x > 0$, the series
$C(x) = \sum_{k=0}^{\infty} \binom{2k}{k} \frac{\cos^{2k+1} x + \sin^{2k+1} x}
{2^{2k} (2k+1)^2}$ and $T(x) = \sum_{k=0}^{\infty} (-1)^k \frac{\tan^{2k+1} x}{(2k+1)^2}$ are
both summable, and $C(x) = \frac{\pi}{2} \log(2\cos x) + T(x)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry19Catalangf.ramanujan_part1_ch9_entry19_catalangf`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry19Catalangf.lean, line 1602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry19Catalangf.lean#L1602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html#ramanujan-part1-ch9-entry19-catalangf).

## Ramanujan's central-binomial sine series identity (Entry 31)

For real $y$ let
$\psi(y) = \sum_{k \ge 0} \binom{2k}{k} \sin^{2k+1}(\pi y) / \bigl(2^{2k} (2k+1)^2\bigr)$. If
$0 \le x \le 1/4$, then the series defining $\psi(1/2 - x)$, $\psi(2x)$ and $\psi(x)$ converge
absolutely, $2 \cos(\pi x) > 0$, and
$\psi(1/2 - x) + \tfrac12 \psi(2x) - \psi(x) = \tfrac{\pi}{2} \log(2 \cos(\pi x))$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry31Ramanujansum.ramanujan_part1_ch9_entry31_ramanujansum`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry31Ramanujansum.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry31Ramanujansum.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html#ramanujan-part1-ch9-entry31-ramanujansum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Central binomial series in trigonometric arguments](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/central-binomial-series-in-trigonometric-argumen)
