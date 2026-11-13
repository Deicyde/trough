---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry33Zeta3integral.ramanujan_part1_ch9_entry33_zeta3integral_general, MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry33Zeta3integral.ramanujan_part1_ch9_entry33_zeta3integral
statement: formalized
proof: formalized
---

# Integrals of cosⁿx sin nx

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-cos-x-sin-nx/index.html).

## Ramanujan's integrals of $\cos^n x \sin nx$ for every $n \ge 0$

Let $n$ be a natural
number and let $H_n = \sum_{k=1}^{n} 1/k$ be the $n$-th harmonic number. Then
$x \cos^n x \sin(nx)$ and $\cos^n x \sin(nx)$ are integrable on $[0, \pi/2]$,
$\int_0^{\pi/2} x \cos^n x \sin(nx)\,dx = \frac{\pi}{2^{n+2}} H_n$ and
$\int_0^{\pi/2} \cos^n x \sin(nx)\,dx = \frac{1}{2^{n+1}} \sum_{k=1}^{n} \frac{2^k}{k}$.

This is Entry 33 without the hypothesis $n > 0$: at $n = 0$ both sides of each identity are $0$.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry33Zeta3integral.ramanujan_part1_ch9_entry33_zeta3integral_general`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry33Zeta3integral.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry33Zeta3integral.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-cos-x-sin-nx/index.html#ramanujan-part1-ch9-entry33-zeta3integra).

## Ramanujan's integrals of $\cos^n x \sin nx$ (Entry 33)

Let $n$ be a positive integer and
let $H_n = \sum_{k=1}^{n} 1/k$ be the $n$-th harmonic number. Then $x \cos^n x \sin(nx)$ and
$\cos^n x \sin(nx)$ are integrable on $[0, \pi/2]$,
$\int_0^{\pi/2} x \cos^n x \sin(nx)\,dx = \frac{\pi}{2^{n+2}} H_n$ and
$\int_0^{\pi/2} \cos^n x \sin(nx)\,dx = \frac{1}{2^{n+1}} \sum_{k=1}^{n} \frac{2^k}{k}$.

## Sources

- Bruce C. Berndt, Ramanujan's Notebooks, Part I, Chapter 9.

Formalized by `MathlibExt.Analysis.Ramanujan.Part1Ch9.Entry33Zeta3integral.ramanujan_part1_ch9_entry33_zeta3integral`, a theorem declared in [MathlibExt/Analysis/Ramanujan/Part1Ch9Entry33Zeta3integral.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Ramanujan/Part1Ch9Entry33Zeta3integral.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-cos-x-sin-nx/index.html#ramanujan-part1-ch9-entry33-zeta3integra-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integrals of cosⁿx sin nx](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/integration/integrals-of-cos-x-sin-nx/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/integration/integrals-of-cos-x-sin-nx)
