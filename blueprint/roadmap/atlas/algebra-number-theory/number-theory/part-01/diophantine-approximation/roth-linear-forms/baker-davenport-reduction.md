---
declaration: section
origin: cited
lean: MetaMathlibExt.nearestInteger_reduction_core, MetaMathlibExt.bakerDavenport_reduction_absolute_general, MetaMathlibExt.bakerDavenport_reduction_absolute, MetaMathlibExt.bakerDavenport_reduction_oneSided_general, MetaMathlibExt.bakerDavenport_reduction_oneSided
statement: formalized
proof: formalized
---

# Baker–Davenport reduction

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html).

## Nearest-integer estimate in the Baker–Davenport reduction

For a real number $x$ write
$\lVert x \rVert = |x - \operatorname{round}(x)|$ for the distance from $x$ to a nearest integer.
Let $q$, $M$, $u$ be natural numbers with $u \le M$, let $v$ be an integer, and let $\kappa$ and
$\mu$ be real numbers. If $\varepsilon = \lVert \mu q \rVert - M \lVert \kappa q \rVert$, then
$\varepsilon \le q \, |u\kappa - v + \mu|$.

## Sources

- Nearest-integer Baker–Davenport reduction core: a named reusable arithmetic prerequisite stage extracted from Lemma (lines 285--292) of Eric F. Bravo, Carlos A. Gómez, and Florian Luca, "Product of Consecutive Tribonacci Numbers With Only One Distinct Digit", Journal of Integer Sequences 22 (2019), Article 19.6.3. <https://cs.uwaterloo.ca/journals/JIS/VOL22/Gomez/gomez3.tex>. Scope: the printed lemma defines nearest-integer distance by `‖x‖ = |x - round x|` and `ε := ‖μq‖ - M‖κq‖`; this stage records the reverse-triangle inequality used by the reduction argument. It does not claim to formalize the full lemma. The source's irrationality, continued-fraction, `q > 6M`, and logarithmic hypotheses belong to the later wrapper and are deliberately omitted from this arithmetic stage, as are the source's `0 < q` and `0 < ε`, which the inequality does not need. The explicit `heq` equality hypothesis is necessary: a prior default-valued epsilon binder did not assert the definition and made the statement false.

Formalized by `MetaMathlibExt.nearestInteger_reduction_core`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportNearestIntegerCore.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportNearestIntegerCore.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html#nearest-integer-reduction-core).

## Baker–Davenport reduction for an arbitrary denominator, absolute-value form

For a real
number $x$ write $\lVert x \rVert = |x - \operatorname{round}(x)|$ for the distance from $x$ to a
nearest integer. Let $M$ and $q$ be natural numbers with $q > 0$, and let $\kappa$, $\mu$, $A$, $B$
be real numbers with $A > 0$ and $B > 1$. Put
$\varepsilon = \lVert \mu q \rVert - M \lVert \kappa q \rVert$ and suppose that $\varepsilon > 0$.
Then there are no natural numbers $r$, $s$, $w$ with $r \le M$,
$w \ge \log(Aq/\varepsilon) / \log B$ and $|r\kappa - s + \mu| < A B^{-w}$.

Formalized by `MetaMathlibExt.bakerDavenport_reduction_absolute_general`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportAbsolute.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportAbsolute.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html#baker-davenport-reduction-absolute-gener).

## Baker–Davenport reduction lemma, absolute-value form

For a real number $x$ write
$\lVert x \rVert = |x - \operatorname{round}(x)|$ for the distance from $x$ to a nearest integer.
Let $M$ be a positive integer and $\kappa$ an irrational real number, and let $q$ be the
denominator of the $j$-th convergent of the continued fraction of $\kappa$ for some natural number
$j$, with $q > 6M$. Let $A$, $B$, $\mu$ be real numbers with $A > 0$ and $B > 1$. Put
$\varepsilon = \lVert \mu q \rVert - M \lVert \kappa q \rVert$ and suppose that $\varepsilon > 0$.
Then there are no positive integers $r$, $s$, $w$ with $r \le M$,
$w \ge \log(Aq/\varepsilon) / \log B$ and $0 < |r\kappa - s + \mu| < A B^{-w}$.

Of the hypothesis $q > 6M$ only $q > 0$ is used. The hypotheses that $M > 0$, that $\kappa$ is
irrational and that $q$ is a convergent denominator, and the positivity of $r$, $s$, $w$ and of
$|r\kappa - s + \mu|$, are not needed: the statement follows from the version for an arbitrary
positive denominator.

## Sources

- Eric F. Bravo, Carlos A. Gomez, and Florian Luca, "Product of Consecutive Tribonacci Numbers With Only One Distinct Digit," Journal of Integer Sequences 22 (2019), Article 19.6.3, Lemma `bd`, lines 285–292. Source URL <https://cs.uwaterloo.ca/journals/JIS/VOL22/Gomez/gomez3.tex>.

Formalized by `MetaMathlibExt.bakerDavenport_reduction_absolute`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportAbsolute.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportAbsolute.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html#baker-davenport-reduction-absolute).

## Baker–Davenport reduction for an arbitrary denominator, one-sided form

For a real number
$x$ write $\lVert x \rVert = |x - \operatorname{round}(x)|$ for the distance from $x$ to a nearest
integer. Let $N$ and $q$ be natural numbers with $q > 0$, and let $\gamma$, $\mu$, $A$, $B$ be real
numbers with $A > 0$ and $B > 1$. Put $\xi = \lVert \mu q \rVert - N \lVert \gamma q \rVert$ and
suppose that $\xi > 0$. Then there are no natural numbers $u$, $v$, $w$ with $u \le N$,
$w \ge \log(Aq/\xi) / \log B$ and $0 < u\gamma - v + \mu < A B^{-w}$.

Formalized by `MetaMathlibExt.bakerDavenport_reduction_oneSided_general`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportOneSided.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportOneSided.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html#baker-davenport-reduction-one-sided-gene).

## Baker–Davenport reduction lemma, one-sided form

For a real number $x$ write
$\lVert x \rVert = |x - \operatorname{round}(x)|$ for the distance from $x$ to a nearest integer.
Let $N$ be a positive integer and $\gamma$ an irrational real number, and let $q$ be the
denominator of the $j$-th convergent of the continued fraction of $\gamma$ for some natural number
$j$, with $q > 6N$. Let $A$, $B$, $\mu$ be real numbers with $A > 0$ and $B > 1$. Put
$\xi = \lVert \mu q \rVert - N \lVert \gamma q \rVert$ and suppose that $\xi > 0$. Then there are
no positive integers $u$, $v$, $w$ with $u \le N$, $w \ge \log(Aq/\xi) / \log B$ and
$0 < u\gamma - v + \mu < A B^{-w}$.

Of the hypothesis $q > 6N$ only $q > 0$ is used. The hypotheses that $N > 0$, that $\gamma$ is
irrational and that $q$ is a convergent denominator, and the positivity of $u$, $v$ and $w$, are
not needed: the statement follows from the version for an arbitrary positive denominator.

## Sources

- Bilizimbéyé Edjeou, Amadou Tall, and Mohamed Ben Fraj Ben Maaouia, "Powers of Two as Sums of Three Lucas Numbers," Journal of Integer Sequences 23 (2020), Article 20.8.8, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Edjeou/edj4.tex>, Lemma, lines 200–211.

Formalized by `MetaMathlibExt.bakerDavenport_reduction_oneSided`, a theorem declared in [MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportOneSided.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DiophantineApproximation/BakerDavenportOneSided.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html#baker-davenport-reduction-one-sided).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Baker–Davenport reduction](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/baker-davenport-reduction)
