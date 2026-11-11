---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry3.ramanujan_part1_ch2_entry3_general, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry3.ramanujan_part1_ch2_entry3, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry3InfiniteEvaluation.ramanujan_part1_ch2_entry3_infinite_evaluation, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7.ramanujan_part1_ch2_entry7, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Corollary.ramanujan_part1_ch2_entry7_corollary, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example1.ramanujan_part1_ch2_entry7_example1, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example1Boundary.ramanujan_part1_ch2_entry7_example1_boundary, MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example2.ramanujan_part1_ch2_entry7_example2
statement: formalized
proof: formalized
---

# Arctangent sums and series

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html).

## Ramanujan's arctangent identity for $\sum_{k=1}^{2n+1} \arctan(1/(n+k))$, $n \ge 0$

For every natural number $n$,

$$\sum_{k=1}^{2n+1} \arctan \frac{1}{n+k} = \frac{\pi}{4} +
\sum_{k=1}^{n} \arctan \frac{10k}{(3k^2 + 2)(9k^2 - 1)}.$$

This is Ramanujan's Entry 3 of Chapter 2 without the hypothesis $n \ge 1$; at $n = 0$ both sides
are $\pi/4$.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry3.ramanujan_part1_ch2_entry3_general`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry3.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry3.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry3-general).

## Ramanujan's arctangent identity for $\sum_{k=1}^{2n+1} \arctan(1/(n+k))$

For every
positive integer $n$,

$$\sum_{k=1}^{2n+1} \arctan \frac{1}{n+k} = \frac{\pi}{4} +
\sum_{k=1}^{n} \arctan \frac{10k}{(3k^2 + 2)(9k^2 - 1)}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 3, formula (3.1), printed p. 27 / PDF p. 37.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry3.ramanujan_part1_ch2_entry3`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry3.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry3.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry3).

## Ramanujan's arctangent series for $\log 3 - \pi/4$

The series

$$\sum_{k=1}^{\infty} \arctan \frac{10k}{(3k^2 + 2)(9k^2 - 1)}$$

converges, and its sum is $\log 3 - \pi/4$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, consequence following Entry 3, printed p. 28 / PDF p. 38.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry3InfiniteEvaluation.ramanujan_part1_ch2_entry3_infinite_evaluation`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry3-infinite-eval).

## Ramanujan's finite arctangent sum (Entry 7)

For every real number $n > 0$ and every
natural number $r$,

$$\sum_{k=0}^{r-1} \arctan \frac{2}{(n + 2k + 1)^2} = \arctan \frac{2r}{n^2 + 2nr + 1}.$$

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, formula (7.2), printed pp. 35-36 / PDF pp. 45-46.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7.ramanujan_part1_ch2_entry7`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7).

## Ramanujan's infinite arctangent series (corollary to Entry 7)

For every real number
$n > 0$, the series

$$\sum_{k=0}^{\infty} \arctan \frac{2}{(n + 2k + 1)^2}$$

converges absolutely and its sum is $\arctan(1/n)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, corollary to Entry 7, formula (7.3), printed p. 36 / PDF p. 46.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Corollary.ramanujan_part1_ch2_entry7_corollary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Corollary.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Corollary.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-corollary).

## Arctangent series over consecutive shifts (Entry 7, Example 1)

Let $n > 0$ be a real
number with $n \ne (\sqrt{5} - 1)/2$. Then the series

$$\sum_{k=0}^{\infty} \arctan \frac{2}{(n + k + 1)^2}$$

converges absolutely; its sum is $\arctan \frac{2n + 1}{n^2 + n - 1}$ when $n > (\sqrt{5} - 1)/2$,
and $\arctan \frac{2n + 1}{n^2 + n - 1} + \pi$ when $n < (\sqrt{5} - 1)/2$. Here $\arctan$ is the
principal branch, with values in $(-\pi/2, \pi/2)$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 1, formula (7.4), printed p. 36 / PDF p. 46.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example1.ramanujan_part1_ch2_entry7_example1`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example1.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example1.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example1).

## Arctangent series at the exceptional point (Entry 7, Example 1)

Let
$c = (\sqrt{5} - 1)/2$. The series

$$\sum_{k=0}^{\infty} \arctan \frac{2}{(c + k + 1)^2}$$

converges absolutely and its sum is $\pi/2$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, boundary consequence of Entry 7, Example 1, formula (7.4), printed p. 36 / PDF p. 46.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example1Boundary.ramanujan_part1_ch2_entry7_example1_boundary`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example1Boundary.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example1Boundary.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example1-boun).

## Alternating arctangent series (Entry 7, Example 2)

For every real number $n > 0$, the
series

$$\sum_{k=0}^{\infty} (-1)^k \arctan \frac{2}{(n + k + 1)^2}$$

converges absolutely and its sum is $\arctan \frac{1}{n^2 + n + 1}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 2, formula (7.5), printed p. 36 / PDF p. 46.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example2.ramanujan_part1_ch2_entry7_example2`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example2.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example2.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example2).

## Arctangent series with halved squares (Entry 7, Example 3)

For every real number
$n > 0$, the series

$$\sum_{k=0}^{\infty} \arctan \frac{1}{2(n + k + 1)^2}$$

converges absolutely and its sum is $\arctan \frac{1}{2n + 1}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 3, formula (7.6), printed p. 36 / PDF p. 46.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example3.ramanujan_part1_ch2_entry7_example3`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example3.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example3.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example3).

## Series of arctangents of 2/k² (Entry 7, Example 4)

The series

$$\sum_{k=0}^{\infty} \arctan \frac{2}{(k + 1)^2}$$

converges absolutely and its sum is $3\pi/4$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 4, printed p. 37 / PDF p. 47.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example4.ramanujan_part1_ch2_entry7_example4`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example4.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example4.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example4).

## Alternating series of arctangents of 2/k² (Entry 7, Example 5)

The series

$$\sum_{n=0}^{\infty} (-1)^n \arctan \frac{2}{(n + 1)^2}$$

converges absolutely and its sum is $\pi/4$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 5, printed p. 37 / PDF p. 47.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example5Alternating.ramanujan_part1_ch2_entry7_example5_alternating`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example5Alternating.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example5Alternating.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example5-alte).

## Series of arctangents of 1/(2k²) (Entry 7, Example 5)

The series

$$\sum_{n=0}^{\infty} \arctan \frac{1}{2(n + 1)^2}$$

converges absolutely and its sum is $\pi/4$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 5, printed p. 37 / PDF p. 47.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example5First.ramanujan_part1_ch2_entry7_example5_first`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example5First.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example5First.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example5-firs).

## Series of arctangents of 1/(1 + k√2)² (Entry 7, Example 6)

The series

$$\sum_{k=0}^{\infty} \arctan \frac{1}{\bigl(1 + \sqrt{2}\,(k + 1)\bigr)^2}$$

converges absolutely and its sum is $\pi/8$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I (Springer, 1985), Chapter 2, Entry 7, Example 6, printed p. 37 / PDF p. 47. It follows from `Entry7.ramanujan_part1_ch2_entry7` at `n = 1 + √2`, whose partial sums `arctan (2 r / (n ^ 2 + 2 n r + 1))` tend to `arctan (1 / n) = arctan (√2 - 1) = π / 8`.

Formalized by `MathlibExt.NumberTheory.Ramanujan.Part1Ch2.Entry7Example6.ramanujan_part1_ch2_entry7_example6`, a theorem declared in [MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example6.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Ramanujan/Part1Ch2Entry7Example6.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html#ramanujan-part1-ch2-entry7-example6).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arctangent sums and series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/trigonometric-and-harmonic-series/arctangent-sums-and-series)
