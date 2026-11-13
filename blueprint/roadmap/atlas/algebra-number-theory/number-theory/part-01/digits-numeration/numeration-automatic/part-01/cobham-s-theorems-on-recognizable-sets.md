---
declaration: section
origin: cited
lean: MetaMathlibExt.baseWordValue, MetaMathlibExt.IsCanonicalBaseWord, MetaMathlibExt.IsBaseRecognizable, MetaMathlibExt.baseDigits, MetaMathlibExt.BasesMultiplicativelyIndependent, MetaMathlibExt.IsUltimatelyPeriodicSet, MetaMathlibExt.cobham_base_dependence, MetaMathlibExt.isUltimatelyPeriodicSet_iff_isUltimatelyPeriodic
statement: formalized
proof: formalized
---

# Cobham's theorems on recognizable sets

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html).

## Value of a base-k digit word

The value of a word $w = d_1 d_2 \cdots d_m$ of base-$k$
digits $d_i \in \{0, \dots, k - 1\}$, read with the most significant digit first, is
$\sum_{i=1}^{m} d_i k^{m-i}$. The empty word has value $0$.

Formalized by `MetaMathlibExt.baseWordValue`, a definition declared in [MathlibExt/NumberTheory/BaseRecognizable.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BaseRecognizable.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#base-word-value).

## Canonical base-k words

A word of base-$k$ digits is canonical when it is empty or its
first (most significant) digit is nonzero.

Formalized by `MetaMathlibExt.IsCanonicalBaseWord`, a definition declared in [MathlibExt/NumberTheory/BaseRecognizable.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BaseRecognizable.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#is-canonical-base-word).

## Sets recognizable in base k

For a natural number $k$, a set $S$ of natural numbers is
recognizable in base $k$ when $k \ge 2$ and some deterministic finite automaton with a nonempty
finite set of states, reading words of base-$k$ digits from the most significant digit, accepts a
word $w = d_1 d_2 \cdots d_m$ exactly when $w$ is canonical (empty, or with $d_1 \neq 0$) and its
value $\sum_{i=1}^{m} d_i k^{m-i}$ lies in $S$.

Formalized by `MetaMathlibExt.IsBaseRecognizable`, a definition declared in [MathlibExt/NumberTheory/BaseRecognizable.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BaseRecognizable.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#is-base-recognizable).

## Base-k expansion

For a natural number $k \ge 2$ and a natural number $n$, the base-$k$
expansion of $n$ is the word $d_1 d_2 \cdots d_m$ of base-$k$ digits, most significant digit
first, with $n = \sum_{i=1}^{m} d_i k^{m-i}$ and $d_1 \neq 0$; for $n = 0$ it is the empty word.

Formalized by `MetaMathlibExt.baseDigits`, a definition declared in [MathlibExt/NumberTheory/BaseRecognizable.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BaseRecognizable.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#base-digits).

## Multiplicatively independent bases

Two natural numbers $k$ and $l$ are multiplicatively
independent when $k^m \ne l^n$ for all positive natural numbers $m$ and $n$.

Formalized by `MetaMathlibExt.BasesMultiplicativelyIndependent`, a definition declared in [MathlibExt/NumberTheory/CobhamBaseDependence.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamBaseDependence.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#bases-multiplicatively-independent).

## Ultimately periodic sets of natural numbers

A set $S$ of natural numbers is ultimately
periodic when there are natural numbers $N$ and $p > 0$ such that, for every $n \ge N$,
$n \in S$ if and only if $n + p \in S$.

Formalized by `MetaMathlibExt.IsUltimatelyPeriodicSet`, a definition declared in [MathlibExt/NumberTheory/CobhamBaseDependence.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamBaseDependence.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#is-ultimately-periodic-set).

## Cobham's theorem

Let $k$ and $l$ be multiplicatively independent natural numbers with
$l \ge 2$, and let $S$ be a set of natural numbers that is recognizable in base $k$ and is not
ultimately periodic. Then $S$ is not recognizable in base $l$.

## Sources

- proved via T. J. P. Krebs, *A more reasonable proof of Cobham's theorem*, arXiv:1801.06704, Section 3.
- T. Kärki, A. Lacroix, and M. Rigo, *On the Recognizability of Self-Generating Sets*, especially the remark invoking Cobham's theorem: <https://cs.uwaterloo.ca/journals/JIS/VOL13/Rigo/rigo6.tex>.

Formalized by `MetaMathlibExt.cobham_base_dependence`, a theorem declared in [MathlibExt/NumberTheory/CobhamBaseDependence.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamBaseDependence.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#cobham-base-dependence).

## Ultimately periodic sets and their characteristic sequences

A set $S$ of natural
numbers is ultimately periodic if and only if its characteristic sequence $n \mapsto (n \in S)$,
a sequence of truth values, is ultimately periodic.

Formalized by `MetaMathlibExt.isUltimatelyPeriodicSet_iff_isUltimatelyPeriodic`, a theorem declared in [MathlibExt/NumberTheory/CobhamBaseDependence.lean, line 676](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamBaseDependence.lean#L676). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#is-ultimately-periodic-set-iff-is-ultima).

## Cobham's theorem for characteristic sequences

Let $k$ and $l$ be multiplicatively
independent natural numbers with $l \ge 2$, and let $S$ be a set of natural numbers that is
recognizable in base $k$ and whose characteristic sequence $n \mapsto (n \in S)$, a sequence of
truth values, is not ultimately periodic. Then $S$ is not recognizable in base $l$.

Formalized by `MetaMathlibExt.cobham_base_dependence_isUltimatelyPeriodic`, a theorem declared in [MathlibExt/NumberTheory/CobhamBaseDependence.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamBaseDependence.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#cobham-base-dependence-is-ultimately-per).

## Cobham's gap theorem without a separate base hypothesis

Let $k$ be a natural number and
let $x_0 < x_1 < x_2 < \cdots$ be a strictly increasing sequence of natural numbers whose set of
values is recognizable in base $k$. Then either the limit superior, as $i \to \infty$, of the
ratios $x_{i+1} / x_i$ computed in the extended nonnegative reals $[0, \infty]$ (where a ratio
with denominator $0$ is $\infty$) is greater than $1$, or there is a natural number $C$ with
$x_{i+1} - x_i \le C$ for every $i$.

Recognizability in base $k$ already requires $k \ge 2$, so no separate hypothesis on $k$ is
needed.

Formalized by `MetaMathlibExt.cobham_gap_theorem_general`, a theorem declared in [MathlibExt/NumberTheory/CobhamGapTheorem.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamGapTheorem.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#cobham-gap-theorem-general).

## Cobham's gap theorem

Let $k \ge 2$ be a natural number and let $x_0 < x_1 < x_2 < \cdots$
be a strictly increasing sequence of natural numbers whose set of values is recognizable in base
$k$. Then either the limit superior, as $i \to \infty$, of the ratios $x_{i+1} / x_i$ computed in
the extended nonnegative reals $[0, \infty]$ (so an unbounded limit superior is $\infty$, and a
ratio with denominator $0$ is $\infty$) is greater than $1$, or there is a natural number $C$ with
$x_{i+1} - x_i \le C$ for every $i$.

## Sources

- Kärki–Lacroix–Rigo gap theorem, lines 979–995 of <https://cs.uwaterloo.ca/journals/JIS/VOL13/Rigo/rigo6.tex>.

Formalized by `MetaMathlibExt.cobham_gap_theorem`, a theorem declared in [MathlibExt/NumberTheory/CobhamGapTheorem.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CobhamGapTheorem.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html#cobham-gap-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cobham's theorems on recognizable sets](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/cobham-s-theorems-on-recognizable-sets)
