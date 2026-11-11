---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry34Zeta3doublesum.ramanujan_part1_ch9_entry34_zeta3doublesum, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry8Arcsin.ramanujan_part1_ch9_entry8_arcsin
statement: formalized
proof: formalized
---

# Series with odd harmonic numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/series-with-odd-harmonic-numbers/index.html).

## Ramanujan's series identity with odd harmonic numbers (Entry 34)

For a natural number
$m$ let $O_m = \sum_{j=0}^{m-1} 1/(2j+1)$. Let $x$ be real with $-1/2 < x < 1$. Then
$1 + x > 0$, $|x| < 1$ and $|x/(1+x)| < 1$, the series
$\sum_{k \ge 0} \frac{1}{(2k+1)^2} \left(\frac{x}{1+x}\right)^{k+1}$ and
$\sum_{k \ge 0} \frac{(-1)^k\, 2^{2k} (k!)^2}{(2k+1)!} O_{k+1} x^{k+1}$ converge absolutely, and
their sums are equal.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry34Zeta3doublesum.ramanujan_part1_ch9_entry34_zeta3doublesum`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry34Zeta3doublesum.lean, line 1302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry34Zeta3doublesum.lean#L1302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/series-with-odd-harmonic-numbers/index.html#ramanujan-part1-ch9-entry34-zeta3doubles).

## Ramanujan's odd harmonic series identity

Let $x$ be a real number with $|x| < 1$. For
$n \ge 0$ put $h_n = 1 + \frac{1}{3} + \cdots + \frac{1}{2n+1}$, for real $y$ let
$F(y) = \sum_{n \ge 0} \frac{h_n}{2n+1} y^{2n+1}$, and let
$\operatorname{Li}_2(x) = \sum_{k \ge 1} \frac{x^k}{k^2}$. Then $1 - x > 0$, $2 - x \ne 0$ and
$|x/(2-x)| < 1$; the series defining $F(x/(2-x))$ and the series defining
$\operatorname{Li}_2(x)$ are both summable; and

$$F\left(\frac{x}{2-x}\right) = \frac{(\log(1-x))^2}{8} + \frac{\operatorname{Li}_2(x)}{2}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9, Entry 8, pp. 249–250.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry8Arcsin.ramanujan_part1_ch9_entry8_arcsin`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry8Arcsin.lean, line 721](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry8Arcsin.lean#L721). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/series-with-odd-harmonic-numbers/index.html#ramanujan-part1-ch9-entry8-arcsin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Series with odd harmonic numbers](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/series-with-odd-harmonic-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/series-with-odd-harmonic-numbers)
