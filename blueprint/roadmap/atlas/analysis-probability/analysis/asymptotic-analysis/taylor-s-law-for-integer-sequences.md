---
declaration: section
origin: cited
lean: MetaMathlibExt.IsTaylorAdmissibleSequence, MetaMathlibExt.initialSegmentMean, MetaMathlibExt.initialSegmentSampleVariance, MetaMathlibExt.SatisfiesTaylorsLawAsymptotically
statement: formalized
proof: formalized
---

# Taylor's law for integer sequences

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences/index.html).

## Admissible sequences for Taylor's law

A sequence $a : \mathbb{N} \to \mathbb{N}$, indexed
from $1$ (its value at $0$ is ignored), is admissible when $a(n) > 0$ for every $n \ge 1$ and
there is $n_0 \ge 1$ such that $a(n) < a(n + 1)$ for every $n \ge n_0$.

## Sources

- Joel E. Cohen, *Variance Functions of Asymptotically Exponentially Increasing Integer Sequences Go Beyond Taylor's Law*, Journal of Integer Sequences 25 (2022), Article 22.9.3, the collection `𝒜` of infinite eventually strictly increasing sequences of natural numbers, lines 113–125, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Cohen/cohen13.tex>.

Formalized by `MetaMathlibExt.IsTaylorAdmissibleSequence`, a definition declared in [MathlibExt/Analysis/Asymptotics/TaylorAdmissibleSequence.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/TaylorAdmissibleSequence.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences/index.html#is-taylor-admissible-sequence).

## Initial-segment mean

For a sequence $a : \mathbb{N} \to \mathbb{N}$ and $n \in \mathbb{N}$,
the initial-segment mean is the real number $m(a, n) = \frac{1}{n} \sum_{j=1}^{n} a(j)$, with
the convention $1 / 0 = 0$, so that $m(a, 0) = 0$.

The source uses $m(a, n)$ only for $n \ge 2$, with indices starting at $1$.

## Sources

- Joel E. Cohen, *Variance Functions of Asymptotically Exponentially Increasing Integer Sequences Go Beyond Taylor's Law*, Journal of Integer Sequences 25 (2022), Article 22.9.3, mean/variance definitions, lines 119–124, equation `eq:mean` at line 122, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Cohen/cohen13.tex>.

Formalized by `MetaMathlibExt.initialSegmentMean`, a definition declared in [MathlibExt/Analysis/Asymptotics/TaylorInitialMean.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/TaylorInitialMean.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences/index.html#initial-segment-mean).

## Initial-segment sample variance

For a sequence $a : \mathbb{N} \to \mathbb{N}$ and
$n \in \mathbb{N}$, the unbiased initial-segment sample variance is the real number
$v(a, n) = \frac{1}{n - 1} \sum_{j=1}^{n} \left(a(j) - \frac{1}{n} \sum_{k=1}^{n} a(k)\right)^2$,
with the convention $1 / 0 = 0$; in particular $v(a, 0) = v(a, 1) = 0$.

The inner average is the initial-segment mean $m(a, n)$. The source uses $v(a, n)$ only for
$n \ge 2$, with indices starting at $1$.

## Sources

- Joel E. Cohen, *Variance Functions of Asymptotically Exponentially Increasing Integer Sequences Go Beyond Taylor's Law*, Journal of Integer Sequences 25 (2022), Article 22.9.3, mean/variance definitions, lines 119–124, equation at line 122, first equality of the equation at line 123, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Cohen/cohen13.tex>.

Formalized by `MetaMathlibExt.initialSegmentSampleVariance`, a definition declared in [MathlibExt/Analysis/Asymptotics/TaylorInitialSampleVariance.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/TaylorInitialSampleVariance.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences/index.html#initial-segment-sample-variance).

## Taylor's law, asymptotic form

A sequence $a : \mathbb{N} \to \mathbb{N}$, indexed from
$1$ (its value at $0$ is ignored), satisfies Taylor's law asymptotically when it is admissible
for Taylor's law and, writing $m(a, n)$ and $v(a, n)$ for its initial-segment mean and
initial-segment sample variance, there are real numbers $c > 0$ and $b$ such that
$v(a, n) / m(a, n)^b \to c$ as $n \to \infty$.

## Sources

- Joel E. Cohen, *Variance Functions of Asymptotically Exponentially Increasing Integer Sequences Go Beyond Taylor's Law*, Journal of Integer Sequences 25 (2022), Article 22.9.3, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Cohen/cohen13.tex>: the collection `𝒜` of admissible sequences with the mean `eq:mean` and variance `eq:varexpanded` definitions (lines 113–125), and the asymptotic power-law definition `eq:TLpower` (lines 152–156).

Formalized by `MetaMathlibExt.SatisfiesTaylorsLawAsymptotically`, a definition declared in [MathlibExt/Analysis/Asymptotics/TaylorsLaw.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Asymptotics/TaylorsLaw.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences/index.html#satisfies-taylors-law-asymptotically).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Taylor's law for integer sequences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/asymptotic-analysis/taylor-s-law-for-integer-sequences)
