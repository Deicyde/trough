---
declaration: section
origin: cited
lean: MetaMathlibExt.dejean_repetition_threshold, MetaMathlibExt.abelianCubeFree, MetaMathlibExt.kurosaki_phi_pow_power_free
statement: formalized
---

# Repetitions in words: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/index.html).

Squares, overlaps, cubes and fractional powers in words: square-free and overlap-free words, abelian and k-abelian repetitions, power-free morphisms, Crochemore's test and Dejean's repetition threshold.

## Dejean's theorem on repetition thresholds

For a natural number $n$ and a real number
$r$, call an infinite word $w = w_0 w_1 w_2 \cdots$ over the alphabet $\{0, \dots, n-1\}$
*$r^+$-free* if for all natural numbers $s$, $\ell$ and $p$ with $0 < p \le \ell$ such that
$w_{s+i+p} = w_{s+i}$ for every natural number $i$ with $i + p < \ell$, we have $\ell / p \le r$;
that is, no factor of $w$ has exponent strictly greater than $r$. Let $\mathrm{RT}(n)$, the
repetition threshold, be the infimum of the set of real numbers $r > 1$ for which there is an
infinite $r^+$-free word over $\{0, \dots, n-1\}$. Then $\mathrm{RT}(2) = 2$,
$\mathrm{RT}(3) = 7/4$, $\mathrm{RT}(4) = 7/5$, and $\mathrm{RT}(n) = n/(n-1)$ for every
$n \ge 5$.

This is a proved result (Dejean's conjecture of 1972): the last cases were proved in 2011 by
Currie and Rampersad and, independently, by Rao.

Paper: James D. Currie, Lucas Mol, and Narad Rampersad, "The Number of Threshold
Words on n Letters Grows Exponentially for Every n ≥ 27", Journal of Integer
Sequences 23 (2020), Article 20.3.1.

## Sources

- Period/exponent and `r`/`r⁺`-free definitions, lines 93--99; repetition-threshold definition and exact values, lines 100--113. Original definition/conjecture: Françoise Dejean, "Sur un théorème de Thue", Journal of Combinatorial Theory, Series A 13(1) (1972), 90--99, DOI 10.1016/0097-3165(72)90011-8. Final cases confirmed in 2011 by James D. Currie and Narad Rampersad, "A proof of Dejean's conjecture", Mathematics of Computation 80 (2011), 1063--1070, arXiv:0905.1129, and independently by Michaël Rao, "Last cases of Dejean's conjecture", Theoretical Computer Science 412(27) (2011), 3010--3018, DOI 10.1016/j.tcs.2010.06.020. Lean representation: `Fin n` harmlessly relabels the source `n`-letter alphabet `A_n`; the universal period clause expresses absence of factors with exponent strictly greater than `r`, i.e. `r⁺`-freeness; `RT` is the real-valued `sInf` over `r > 1` admitting such an infinite word.
- <https://cs.uwaterloo.ca/journals/JIS/VOL23/Mol/mol2.tex>.

Stated but not proved: `MetaMathlibExt.dejean_repetition_threshold` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DejeanRepetitionThresholdWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Words/DejeanRepetitionThresholdWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/index.html#dejean-repetition-threshold).

## Exponential lower bound for ternary abelian-cube-free words

An abelian cube is a word
$xyz$ with $x$, $y$, $z$ nonempty such that each letter occurs equally often in $x$, $y$ and $z$.
Let $a_n$ be the number of words of length $n$ over $\{0, 1, 2\}$ that contain no abelian cube
as a factor. Then $2^{n/24} = O(a_n)$ as $n \to \infty$: there is a constant $C$ such that
$2^{n/24} \le C a_n$ for all sufficiently large $n$.

## Sources

- Ali Aberkane and James D. Currie, *The Number of Ternary Words Avoiding Abelian Cubes Grows Exponentially*, Journal of Integer Sequences 7 (2004), Article 04.2.7, <https://cs.uwaterloo.ca/journals/JIS/VOL7/Currie/currie18.tex>, Second Main Theorem, lines 558-561.

Formalized by `MetaMathlibExt.abelianCubeFree`, a theorem declared in [MathlibExt/Combinatorics/Words/TernaryAbelianCubeFreeLowerBound.lean, line 2229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/TernaryAbelianCubeFreeLowerBound.lean#L2229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/index.html#abelian-cube-free).

## Kurosaki's words are $(7/4)^+$-power-free

On the alphabet $\{1, 2, 3\}$, let $\sigma$ be the
permutation that swaps $1$ and $2$ and fixes $3$, let $\rho$ be the permutation that swaps $2$ and
$3$ and fixes $1$, and for a finite word $w$ let $\varphi(w) = \sigma(w)\,w\,\rho(w)$, where
$\sigma(w)$ and $\rho(w)$ apply the permutation to each letter of $w$. Call $p \ge 1$ a period of
a finite word $u = u_0 u_1 \cdots$ when $u_i = u_{i+p}$ for every $i$ with $i + p < |u|$. For every
$n \ge 1$, every factor $u$ of the word $\varphi^n(2)$ and every period $p$ of $u$ satisfy
$4|u| \le 7p$; that is, every factor of $\varphi^n(2)$ has exponent at most $7/4$.

## Sources

- Serina Camungol and Narad Rampersad, "Concerning Kurosaki's Squarefree Word," Journal of Integer Sequences 16 (2013), Article 13.9.4, Theorem, lines 184–188, with the σ/ρ/φ definitions at lines 116–124, https://cs.uwaterloo.ca/journals/JIS/VOL16/Camungol/ramper4.tex

Formalized by `MetaMathlibExt.kurosaki_phi_pow_power_free`, a theorem declared in [MathlibExt/Combinatorics/Words/KurosakiPowerFree.lean, line 1165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Words/KurosakiPowerFree.lean#L1165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/index.html#kurosaki-phi-pow-power-free).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Repetitions in words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words)
