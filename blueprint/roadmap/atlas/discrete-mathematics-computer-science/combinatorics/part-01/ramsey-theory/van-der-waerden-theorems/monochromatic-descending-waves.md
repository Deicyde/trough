---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.IsDescendingWave, MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.ForcesMonochromaticWave, MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberQuadratic, MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberCubicOrder, MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberQuadratic_refuted, MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberCubicOrder_holds
statement: formalized
---

# Monochromatic descending waves

6 results, 4 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html).

## Descending wave

A $k$-term descending wave is a sequence $x_0, x_1, \dots, x_{k-1}$ of
natural numbers with $x_0 < x_1 < \dots < x_{k-1}$ and $x_{j-1} + x_{j+1} \le 2 x_j$ for every
$j$ with $0 < j < k - 1$.

Formalized by `MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.IsDescendingWave`, a definition declared in [WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html#is-descending-wave).

## Forcing a monochromatic descending wave

For natural numbers $k$ and $n$, the statement
that for every colouring of the natural numbers with two colours there is a monochromatic $k$-term
descending wave all of whose terms lie in $\{1, \dots, n\}$. Equivalently, every colouring of
$\{1, \dots, n\}$ with two colours has a monochromatic $k$-term descending wave, so the statement
says $f(k) \le n$, where $f(k)$ is the least $n$ with this property.

Formalized by `MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.ForcesMonochromaticWave`, a definition declared in [WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html#forces-monochromatic-wave).

## Erdős Problem 781, the exact-value question

For natural numbers $k$ and $n$, say that $n$
forces a $k$-term wave if every colouring of $\{1, \dots, n\}$ with two colours has a monochromatic
$k$-term descending wave. The statement that for every natural number $k \ge 1$ the number
$k^2 - k + 1$ forces a $k$-term wave and the number $k^2 - k$ does not; that is,
$f(k) = k^2 - k + 1$ for every $k \ge 1$, where $f(k)$ is the least $n$ that forces a $k$-term
wave.

Formalized by `MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberQuadratic`, a definition declared in [WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html#wave-number-quadratic).

## Erdős Problem 781, cubic order of the wave number

For natural numbers $k$ and $n$, say
that $n$ forces a $k$-term wave if every colouring of $\{1, \dots, n\}$ with two colours has a
monochromatic $k$-term descending wave. The statement that there are real numbers $c > 0$ and $C$
such that for all sufficiently large $k$, every natural number $n$ that forces a $k$-term wave
satisfies $n \ge c k^3$, and the natural number $\lfloor \max(C k^3, 0) \rfloor$ forces a $k$-term
wave. Writing $f(k)$ for the least $n$ that forces a $k$-term wave, this says $f(k) \asymp k^3$.

Formalized by `MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberCubicOrder`, a definition declared in [WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html#wave-number-cubic-order).

## Erdős Problem 781 is false

For natural numbers $k$ and $n$, say that $n$ forces a $k$-term
wave if every colouring of $\{1, \dots, n\}$ with two colours has a monochromatic $k$-term
descending wave. It is not the case that for every natural number $k \ge 1$ the number
$k^2 - k + 1$ forces a $k$-term wave and the number $k^2 - k$ does not. Writing $f(k)$ for the
least $n$ that forces a $k$-term wave, this says that $f(k) \ne k^2 - k + 1$ for some $k \ge 1$.

Alon and Spencer proved $f(k) \ge c k^3$ for some $c > 0$, so $f(k) > k^2 - k + 1$ for all large
$k$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #781, https://www.erdosproblems.com/781 (status DISPROVED); resolution: N. Alon and J. Spencer, Ascending waves, J. Combin. Theory Ser. A 52 (1989), 275-287; T. C. Brown, P. Erdős and A. R. Freedman, Quasi-progressions and descending waves, J. Combin. Theory Ser. A 53 (1990), 81-95, Alon-Spencer Theorem 1.1: c_1 k³ ≤ f(k) ≤ c_2 k³ for all k ≥ 1, the upper bound being Brown, Erdős and Freedman's f(k) ≤ k³/3 - 4k/3 + 3; Brown, Erdős and Freedman also proved k² - k + 1 ≤ f(k) and asked whether it is the exact value, and Alon and Spencer: 'Here we show that this is false', https://web.math.princeton.edu/~nalon/PDFS/Publications1/Ascending%20waves.pdf.

Stated but not proved: `MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberQuadratic_refuted` is written with `theorem_wanted` in [WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html#wave-number-quadratic-refuted).

## Alon–Spencer: the descending-wave number has cubic order

For natural numbers $k$ and $n$, say
that $n$ forces a $k$-term wave if every colouring of $\{1, \dots, n\}$ with two colours has a
monochromatic $k$-term descending wave. There are real numbers $c > 0$ and $C$ such that for all
sufficiently large $k$, every natural number $n$ that forces a $k$-term wave satisfies
$n \ge c k^3$, and the natural number $\lfloor \max(C k^3, 0) \rfloor$ forces a $k$-term wave.
Writing $f(k)$ for the least $n$ that forces a $k$-term wave, this says $f(k) \asymp k^3$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #781, https://www.erdosproblems.com/781 (status DISPROVED); resolution: N. Alon and J. Spencer, Ascending waves, J. Combin. Theory Ser. A 52 (1989), 275-287; T. C. Brown, P. Erdős and A. R. Freedman, Quasi-progressions and descending waves, J. Combin. Theory Ser. A 53 (1990), 81-95, Alon-Spencer Theorem 1.1: c_1 k³ ≤ f(k) ≤ c_2 k³ for all k ≥ 1, the upper bound being Brown, Erdős and Freedman's f(k) ≤ k³/3 - 4k/3 + 3; Brown, Erdős and Freedman also proved k² - k + 1 ≤ f(k) and asked whether it is the exact value, and Alon and Spencer: 'Here we show that this is false', https://web.math.princeton.edu/~nalon/PDFS/Publications1/Ascending%20waves.pdf.

Stated but not proved: `MathlibExt.Combinatorics.DescendingWaveColoringErdosProblem781Wanted.waveNumberCubicOrder_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/DescendingWaveColoringErdosProblem781Wanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html#wave-number-cubic-order-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic descending waves](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-descending-waves)
