---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry20Piseries1.ramanujan_part1_ch9_entry20_piseries1, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry21Piseries2.ramanujan_part1_ch9_entry21_piseries2, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.chapter9Chi3Term_eq_entry21, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.chapter9Chi3AtOne_eq_entry21, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.chapter9Entry23FactorialTerm_eq_entry20, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.ramanujan_part1_ch9_entry22_chudnovsky, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry23Ramanujanpi2.ramanujan_part1_ch9_entry23_ramanujanpi2, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry32Lambertdivisor.ramanujan_part1_ch9_entry32_lambertdivisor
statement: formalized
proof: formalized
---

# Power series in sin x and tan x

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html).

## A series in even powers of $\sin x$ involving $\zeta(3)$

Let $x$ be a real number with
$|x| \le \pi/2$, let $M(x) = \frac{x^2}{2} \log|2\sin x|$ for $x \ne 0$ and $M(0) = 0$, and let
$\zeta(3) = \sum_{k=1}^{\infty} k^{-3}$. Then $|2\sin x| > 0$ if $x \ne 0$, the series
$\sum_{k=1}^{\infty} k^{-3}$,
$A(x) = \sum_{k=0}^{\infty} \frac{2^{2k} (k!)^2 \sin^{2k+2} x}{(2k+1)! \, (2k+2)^2}$,
$B(x) = \sum_{k=1}^{\infty} \frac{\sin 2kx}{k^2}$ and
$E(x) = \sum_{k=1}^{\infty} \frac{\cos 2kx}{k^3}$ are all summable, and
$A(x) = M(x) + \frac{x}{2} B(x) + \frac{1}{4} E(x) - \frac{\zeta(3)}{4}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry20Piseries1.ramanujan_part1_ch9_entry20_piseries1`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry20Piseries1.lean, line 2204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry20Piseries1.lean#L2204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#ramanujan-part1-ch9-entry20-piseries1).

## A series in even powers of $\tan x$ with odd harmonic numbers

Let $x$ be a real number
with $|x| \le \pi/4$. Let $h_k = \sum_{j=0}^{k-1} \frac{1}{2j+1}$, let
$N(x) = \frac{x^2}{2} \log|\tan x|$ for $x \ne 0$ and $N(0) = 0$, and let
$\lambda(3) = \sum_{j=0}^{\infty} (2j+1)^{-3}$. Then the series $\sum_{j=0}^{\infty} (2j+1)^{-3}$,
$A(x) = \sum_{k=1}^{\infty} (-1)^{k-1} \frac{h_k \tan^{2k} x}{(2k)^2}$,
$B(x) = \sum_{j=0}^{\infty} \frac{\sin((4j+2)x)}{(2j+1)^2}$ and
$E(x) = \sum_{j=0}^{\infty} \frac{\cos((4j+2)x)}{(2j+1)^3}$ are all summable, and
$A(x) = N(x) + x B(x) + \frac{1}{2} E(x) - \frac{1}{2} \lambda(3)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry21Piseries2.ramanujan_part1_ch9_entry21_piseries2`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry21Piseries2.lean, line 2323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry21Piseries2.lean#L2323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#ramanujan-part1-ch9-entry21-piseries2).

## Odd reciprocal cubes in Entries 21 and 22

The sequence $j \mapsto 1/(2j+1)^3$
($j = 0, 1, 2, \dots$) used in the statement of Entry 22 of Chapter 9 of Ramanujan's notebooks
is, by definition, the same sequence as the one used in Entry 21.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.chapter9Chi3Term_eq_entry21`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#chapter9-chi3-term-eq-entry21).

## The sum of the odd reciprocal cubes in Entries 21 and 22

The constant
$\sum_{j \ge 0} 1/(2j+1)^3$ used in the statement of Entry 22 of Chapter 9 of Ramanujan's
notebooks is, by definition, the same constant as the one used in Entry 21.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.chapter9Chi3AtOne_eq_entry21`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#chapter9-chi3-at-one-eq-entry21).

## The factorial sine series term in Entries 20 and 22

For real $u$ and $k \ge 0$, the
term $2^{2k} (k!)^2 \sin^{2k+2} u / \bigl((2k+1)! \, (2k+2)^2\bigr)$ used in the statement of
Entry 22 of Chapter 9 of Ramanujan's notebooks is, by definition, the same as the one used in
Entry 20.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.chapter9Entry23FactorialTerm_eq_entry20`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#chapter9-entry23-factorial-term-eq-entry).

## Entry 22 of Chapter 9 of Ramanujan's notebooks

For real $u$ and $k \ge 0$ let
$T_k(u) = \frac{2^{2k} (k!)^2 \sin^{2k+2} u}{(2k+1)! \, (2k+2)^2}$. Let $x$ be real with
$0 \le x \le \pi/4$. Then $2 \cos x > 0$, the series $\sum_{j \ge 0} \frac{1}{(2j+1)^3}$,
$\sum_{k \ge 0} \bigl(T_k(x) + T_k(\pi/2 - x)\bigr)$,
$\sum_{k \ge 0} \frac{\binom{2k}{k} \cos^{2k+1} x}{2^{2k} (2k+1)^2}$ and $\sum_{k \ge 0} T_k(2x)$
converge absolutely, and

$$
\sum_{k \ge 0} \bigl(T_k(x) + T_k(\pi/2 - x)\bigr) = -\frac{\pi^2}{8} \log(2 \cos x) +
\frac{\pi}{2} \sum_{k \ge 0} \frac{\binom{2k}{k} \cos^{2k+1} x}{2^{2k} (2k+1)^2} +
\frac{1}{4} \sum_{k \ge 0} T_k(2x) - \frac{1}{2} \sum_{j \ge 0} \frac{1}{(2j+1)^3}.
$$

Proof: Differentiate the factorial and central-binomial series termwise, reduce
the logarithmic integral by Abel's limit and dominated convergence, and finish
by the fundamental theorem of calculus. This follows Berndt's Entries 20–23 and
Lehmer's arcsine series.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9, Entry 22, pp. 270–271. The printed range `0 ≤ x ≤ π / 2` is false. This target uses `0 ≤ x ≤ π / 4`, the range supported by the source proof's substitution of `2 * x` into Entry 20; the endpoint remains an explicit proof obligation.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry22Chudnovsky.ramanujan_part1_ch9_entry22_chudnovsky`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean, line 2056](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry22Chudnovsky.lean#L2056). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#ramanujan-part1-ch9-entry22-chudnovsky).

## Entry 23 of Chapter 9 of Ramanujan's notebooks

For real $u$ and $k \ge 0$ let
$T_k(u) = \frac{2^{2k} (k!)^2 \sin^{2k+2} u}{(2k+1)! \, (2k+2)^2}$, and for $k \ge 1$ let
$O_k = 1 + \frac{1}{3} + \dots + \frac{1}{2k-1}$. Let $x$ be real with $|x| \le \pi/4$. Then the
series $\sum_{k \ge 1} \frac{(-1)^{k-1} O_k \tan^{2k} x}{(2k)^2}$, $\sum_{k \ge 0} T_k(x)$ and
$\sum_{k \ge 0} T_k(2x)$ converge absolutely, and

$$
\sum_{k \ge 1} \frac{(-1)^{k-1} O_k \tan^{2k} x}{(2k)^2} =
2 \sum_{k \ge 0} T_k(x) - \frac{1}{4} \sum_{k \ge 0} T_k(2x).
$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9, Entry 23, p. 271.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry23Ramanujanpi2.ramanujan_part1_ch9_entry23_ramanujanpi2`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry23Ramanujanpi2.lean, line 2570](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry23Ramanujanpi2.lean#L2570). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#ramanujan-part1-ch9-entry23-ramanujanpi2).

## Ramanujan's sine series in odd powers of the tangent (Entry 32)

Let $x$ be real with
$|x| \le \pi/4$. Then $\cos x > 0$, the series
$\sum_{k \ge 0} \frac{2^{2k} (k!)^2}{(2k)!\,(2k+1)^2} \sin^{2k+1}(2x)$ and
$\sum_{k \ge 0} \frac{(-1)^k \tan^{2k+1} x}{(2k+1)^2}$ converge absolutely, and the first sum
equals twice the second.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry32Lambertdivisor.ramanujan_part1_ch9_entry32_lambertdivisor`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry32Lambertdivisor.lean, line 2007](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry32Lambertdivisor.lean#L2007). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html#ramanujan-part1-ch9-entry32-lambertdivis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power series in sin x and tan x](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/power-series-in-sin-x-and-tan-x)
