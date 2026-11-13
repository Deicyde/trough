---
declaration: section
origin: cited
lean: MetaMathlibExt.HasDistinctMultiplesInInterval, MetaMathlibExt.distinctMultiplesIntervalLength, MetaMathlibExt.HasDistinctMultiplesInInterval.mono, MetaMathlibExt.exists_hasDistinctMultiplesInInterval, MetaMathlibExt.hasDistinctMultiplesInInterval_distinctMultiplesIntervalLength, MetaMathlibExt.distinctMultiplesIntervalLength_le_iff, MetaMathlibExt.distinctMultiplesIntervalLength_one, MetaMathlibExt.distinctMultiplesIntervalLength_mul_le
statement: formalized
---

# Distinct multiples in an interval

13 results, 9 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html).

## Distinct multiples of $1, \dots, n$ in an interval

For natural numbers $n$, $m$ and $L$,
the interval $(m, m + L]$ contains distinct multiples of $1, \dots, n$ when there are pairwise
distinct natural numbers $a_1, \dots, a_n$ with $m < a_i \le m + L$ and $i \mid a_i$ for every
$1 \le i \le n$.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`, after Erdős and Pomerance).

Formalized by `MetaMathlibExt.HasDistinctMultiplesInInterval`, a definition declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#has-distinct-multiples-in-interval).

## Least interval length containing distinct multiples

For natural numbers $n$ and $m$,
$f(n, m)$ is the least natural number $L$ such that the interval $(m, m + L]$ contains distinct
multiples of $1, \dots, n$.

Such an $L$ always exists, so the least one is well defined.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`, after Erdős and Pomerance).

Formalized by `MetaMathlibExt.distinctMultiplesIntervalLength`, a definition declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#distinct-multiples-interval-length).

## Lengthening the interval preserves distinct multiples

For natural numbers $n$, $m$, $L$
and $L'$ with $L \le L'$, if the interval $(m, m + L]$ contains distinct multiples of
$1, \dots, n$, then so does the interval $(m, m + L']$.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`).

Formalized by `MetaMathlibExt.HasDistinctMultiplesInInterval.mono`, a theorem declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#mono).

## Some interval contains distinct multiples

For all natural numbers $n$ and $m$ there is a
natural number $L$ such that the interval $(m, m + L]$ contains distinct multiples of
$1, \dots, n$.

For example, $L = n(m + 1)$ works, with $a_i = i(m + 1)$ for $1 \le i \le n$.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`).

Formalized by `MetaMathlibExt.exists_hasDistinctMultiplesInInterval`, a theorem declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#exists-has-distinct-multiples-in-interva).

## The least interval length is admissible

For natural numbers $n$ and $m$, let $f(n, m)$
be the least natural number $L$ such that the interval $(m, m + L]$ contains distinct multiples
of $1, \dots, n$. Then the interval $(m, m + f(n, m)]$ contains distinct multiples of
$1, \dots, n$.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`).

Formalized by `MetaMathlibExt.hasDistinctMultiplesInInterval_distinctMultiplesIntervalLength`, a theorem declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#has-distinct-multiples-in-interval-disti).

## Characterization of the least interval length

For natural numbers $n$ and $m$, let
$f(n, m)$ be the least natural number $K$ such that the interval $(m, m + K]$ contains distinct
multiples of $1, \dots, n$. Then for every natural number $L$, $f(n, m) \le L$ if and only if
the interval $(m, m + L]$ contains distinct multiples of $1, \dots, n$.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`).

Formalized by `MetaMathlibExt.distinctMultiplesIntervalLength_le_iff`, a theorem declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#distinct-multiples-interval-length-le-if).

## The least interval length for $n = 1$

For natural numbers $n$ and $m$, let $f(n, m)$ be
the least natural number $L$ such that the interval $(m, m + L]$ contains distinct multiples of
$1, \dots, n$. Then $f(1, m) = 1$ for every natural number $m$: the interval $(m, m + 1]$
contains the multiple $m + 1$ of $1$, and the empty interval $(m, m]$ contains nothing.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Section 1 (definition of `f(n, m)`).

Formalized by `MetaMathlibExt.distinctMultiplesIntervalLength_one`, a theorem declared in [MathlibExt/NumberTheory/DistinctMultiplesInterval.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DistinctMultiplesInterval.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#distinct-multiples-interval-length-one).

## An inequality between diagonal and shifted interval lengths

For natural numbers $n$ and
$m$, let $f(n, m)$ be the least natural number $L$ such that the interval $(m, m + L]$ contains
distinct multiples of $1, \dots, n$. Then for all positive integers $k$ and $n$,
$kn + f(kn, kn) \le k^2 n + f(n, k^2 n)$.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Lemma 2.

Stated but not proved: `MetaMathlibExt.distinctMultiplesIntervalLength_mul_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/DistinctMultiplesIntervalWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DistinctMultiplesIntervalWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#distinct-multiples-interval-length-mul-l).

## Erdős–Pomerance bounds for the diagonal interval length

For natural numbers $n$ and $m$,
let $f(n, m)$ be the least natural number $L$ such that the interval $(m, m + L]$ contains
distinct multiples of $1, \dots, n$. For every real $\varepsilon > 0$ and all sufficiently large
natural numbers $n$,

$$
\left(\frac{2}{\sqrt{e}} - \varepsilon\right) n \sqrt{\frac{\log n}{\log \log n}} < f(n, n) <
(2 + \varepsilon)\, n \sqrt{\log n}.
$$

## Sources

- the constants are read from the paper text (arXiv:2601.16972, same paper, Lemma 3), since the record's are garbled; they agree with the record's `√2e > 1.21` remark (`2/√e ≈ 1.213`).
- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Lemma 3, quoting Erdős and Pomerance.

Stated but not proved: `MetaMathlibExt.distinctMultiplesIntervalLength_diag_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/DistinctMultiplesIntervalWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DistinctMultiplesIntervalWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#distinct-multiples-interval-length-diag).

## Shifting the interval can greatly increase the least length

For natural numbers $n$ and
$m$, let $f(n, m)$ be the least natural number $L$ such that the interval $(m, m + L]$ contains
distinct multiples of $1, \dots, n$. For all sufficiently large natural numbers $n$ there is a
positive integer $m$ with

$$
f(n, m) - f(n, n) > \frac{0.36\, n \log n}{\log \log n}.
$$

Since $f(n, m)$ is periodic in $m$ with period $\operatorname{lcm}(1, \dots, n)$, this says that
$\max_{m \ge 1} f(n, m) - f(n, n) > 0.36\, n \log n / \log \log n$ for all large $n$, the form
stated in the source.

## Sources

- Wouter van Doorn, *On the Length of an Interval That Contains Distinct Multiples of the First n Positive Integers*, INTEGERS 26 (2026), Article A7, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_distinctMultiplesIntervalLength_sub_gt` is written with `theorem_wanted` in [WantedExt/NumberTheory/DistinctMultiplesIntervalWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DistinctMultiplesIntervalWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#exists-distinct-multiples-interval-lengt).

## Erdős's matching function for multiples in intervals

For a natural number $m$, $f(m)$ is
the largest natural number $r$ such that for every natural number $N$, every set
$A \subseteq \{1, \dots, N\}$ with exactly $m$ elements and every real $x \ge 1$, there are
distinct $a_1, \dots, a_r \in A$ and distinct natural numbers $b_1, \dots, b_r$ in the open
interval $(x, x + 2N)$ with $a_i \mid b_i$ for every $i$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem650Wanted.f`, a definition declared in [WantedExt/NumberTheory/ErdosProblem650Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem650Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#f).

## Statement of Erdős Problem 650

Let $f$ be Erdős's matching function for multiples in
intervals. The statement is the conjunction of four claims: for every natural number $m$,
$f(m) = \min(m, \lceil 2\sqrt{m}\,\rceil)$; it is not the case that $f(m) \le \sqrt{m}$ for every
natural number $m$; $\sqrt{m} \le f(m)$ for every natural number $m$; and $f(m^2) \le 2m$ for
every natural number $m$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem650Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem650Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem650Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#conjecture).

## Erdős Problem 650: matching integers to distinct multiples

For a natural number $m$, let
$f(m)$ be the largest natural number $r$ such that for every natural number $N$, every set
$A \subseteq \{1, \dots, N\}$ with exactly $m$ elements and every real $x \ge 1$, there are
distinct $a_1, \dots, a_r \in A$ and distinct natural numbers $b_1, \dots, b_r$ in the open
interval $(x, x + 2N)$ with $a_i \mid b_i$ for every $i$. Then $f(m) = \min(m,
\lceil 2\sqrt{m}\,\rceil)$ for every natural number $m$; it is not the case that
$f(m) \le \sqrt{m}$ for every natural number $m$; $\sqrt{m} \le f(m)$ for every natural number
$m$; and $f(m^2) \le 2m$ for every natural number $m$.

Solved by Erdős–Surányi [ErSu59], Erdős–Selfridge [Er78], [Er86c] and van Doorn–Li–Tang [VLT26].

## Sources

- [VLT26] W. van Doorn, Y. Li and Q. Tang, Optimal bounds for an Erdős problem on matching integers to distinct multiples, arXiv:2603.28636 (2026), https://arxiv.org/abs/2603.28636; W. van Doorn, Lean formalization of Erdős Problem 650 (Aristotle-assisted), https://github.com/Woett/Lean-files/blob/c100ed4a4429e987a9555ee428a1aa524a46e16d/ErdosProblem650.lean.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem650Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem650Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem650Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Distinct multiples in an interval](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/distinct-multiples-in-an-interval)
