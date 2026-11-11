---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.gl2TraceRangeContainsRay, MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.quaternionRealPartRangeContainsInterval, MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.gl2TraceRangeContainsRay_refuted, MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.quaternionRealPartRangeContainsInterval_refuted, MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.wordMap, MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.psl2RealWordMapsSurjective, MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.psl2ComplexWordMapsSurjective, MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.so3WordMapsSurjective
statement: formalized
---

# Word maps on Lie groups

11 results, 6 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html).

## Mycielski's trace-range property for $\mathrm{GL}(2, \mathbb{R})$ (Kourovka 16.69(a))

For
every nontrivial element $w$ of the free group on two generators $x, y$, the set of traces
$\operatorname{tr} w(A, B)$, where $A, B$ range over $\mathrm{GL}(2, \mathbb{R})$ and $w(A, B)$ is
obtained by substituting $A$ for $x$ and $B$ for $y$, contains the interval $[-2, \infty)$.

Formalized by `MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.gl2TraceRangeContainsRay`, a definition declared in [WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#gl2-trace-range-contains-ray).

## Mycielski's real-part property for quaternion word maps (Kourovka 16.69(b))

For every
nontrivial element $w$ of the free group on two generators $x, y$, the set of real parts
$\operatorname{Re} w(p, q)$, where $p, q$ range over the nonzero real quaternions and $w(p, q)$ is
obtained by substituting $p$ for $x$ and $q$ for $y$, contains the interval $[-5/27, 1]$.

Formalized by `MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.quaternionRealPartRangeContainsInterval`, a definition declared in [WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#quaternion-real-part-range-contains-inte).

## Mycielski's trace-range question for $\mathrm{GL}(2, \mathbb{R})$ has a negative answer

There is a nontrivial element $w$ of the free group on two generators $x, y$ such that some real
number $t \ge -2$ is not the trace of $w(A, B)$ for any $A, B \in \mathrm{GL}(2, \mathbb{R})$, where
$w(A, B)$ is obtained by substituting $A$ for $x$ and $B$ for $y$.

Resolved false: the Kourovka Notebook (21st issue) answers 16.69(a), posed for `x, y ∈ GL(2, ℝ)`,
"No, it need not" (AI solution confirmed by A. Thom), citing the Nilradical note, whose Theorem 2
gives an explicit word `W ≠ 1` with `tr W(A, B) > 7/4` for all `A, B ∈ SL(2, ℝ)`. Source: E. I.
Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st
issue, arXiv:1401.0300v49 (2026), Problem 16.69 (J. Mycielski); resolution: Nilradical v1.0.0, Word
maps on PSL2: real and complex cases, result notes (21 September 2026); A. Thom, Convergent
sequences in discrete groups, Canad. Math. Bull. 56 (2013), 424-433, (a) Nilradical, Theorem 2 (an
explicit W ≠ 1 with tr W(A, B) > 7/4 for all A, B ∈ SL_2(ℝ)); (b) Thom, Corollary 1.2 (for every n
and ε > 0 a word w ≠ 1 with ‖1 - w(u, v)‖ ≤ ε for all u, v ∈ U(n)); the Kourovka Notebook (21st
issue) marks 16.69 solved (a: No, AI solution confirmed by A. Thom; b: No, Thom 2013),
https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/nilradical-kourovka-16-68-69.pdf.

Stated but not proved: `MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.gl2TraceRangeContainsRay_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#gl2-trace-range-contains-ray-refuted).

## Mycielski's real-part question for quaternion word maps has a negative answer

There is a
nontrivial element $w$ of the free group on two generators $x, y$ such that some real number $t$
with $-5/27 \le t \le 1$ is not the real part of $w(p, q)$ for any nonzero real quaternions $p, q$,
where $w(p, q)$ is obtained by substituting $p$ for $x$ and $q$ for $y$.

Resolved false: the Kourovka Notebook (21st issue) answers 16.69(b) "No, it need not", citing Thom
(2013), whose Corollary 1.2 gives, for every `n` and `ε > 0`, a word `w ≠ 1` with `‖1 - w(u, v)‖ ≤
ε` for all `u, v ∈ U(n)`. Source: E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group
Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.69 (J. Mycielski);
resolution: Nilradical v1.0.0, Word maps on PSL2: real and complex cases, result notes (21 September
2026); A. Thom, Convergent sequences in discrete groups, Canad. Math. Bull. 56 (2013), 424-433, (a)
Nilradical, Theorem 2 (an explicit W ≠ 1 with tr W(A, B) > 7/4 for all A, B ∈ SL_2(ℝ)); (b) Thom,
Corollary 1.2 (for every n and ε > 0 a word w ≠ 1 with ‖1 - w(u, v)‖ ≤ ε for all u, v ∈ U(n)); the
Kourovka Notebook (21st issue) marks 16.69 solved (a: No, AI solution confirmed by A. Thom; b: No,
Thom 2013),
https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/nilradical-kourovka-16-68-69.pdf.

Stated but not proved: `MathlibExt.GroupTheory.WordMapTraceRangeKourovka16Problem69Wanted.quaternionRealPartRangeContainsInterval_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapTraceRangeKourovka16Problem69Wanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#quaternion-real-part-range-contains-inte-2).

## Word map

For a group $G$ and an element $w$ of the free group $F_2$ on two generators
$x_0, x_1$, the word map of $w$ is the map $G \times G \to G$ sending $(x, y)$ to $w(x, y)$, the
image of $w$ under the group homomorphism $F_2 \to G$ with $x_0 \mapsto x$ and $x_1 \mapsto y$.

Formalized by `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.wordMap`, a definition declared in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#word-map).

## Surjectivity of word maps on $\mathrm{PSL}(2, \mathbb{R})$ (Kourovka 16.68(a))

The
statement, asked about by J. Mycielski, that for every nontrivial element $w$ of the free group
$F_2$ on two generators, the word map
$\mathrm{PSL}(2, \mathbb{R}) \times \mathrm{PSL}(2, \mathbb{R}) \to \mathrm{PSL}(2, \mathbb{R})$,
$(x, y) \mapsto w(x, y)$, is surjective.

Formalized by `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.psl2RealWordMapsSurjective`, a definition declared in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#psl2-real-word-maps-surjective).

## Surjectivity of word maps on $\mathrm{PSL}(2, \mathbb{C})$ (Kourovka 16.68(b))

The
statement, asked about by J. Mycielski, that for every nontrivial element $w$ of the free group
$F_2$ on two generators, the word map
$\mathrm{PSL}(2, \mathbb{C}) \times \mathrm{PSL}(2, \mathbb{C}) \to \mathrm{PSL}(2, \mathbb{C})$,
$(x, y) \mapsto w(x, y)$, is surjective.

Formalized by `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.psl2ComplexWordMapsSurjective`, a definition declared in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#psl2-complex-word-maps-surjective).

## Surjectivity of word maps on $\mathrm{SO}(3, \mathbb{R})$ (Kourovka 16.68(c))

The
statement, asked about by J. Mycielski, that for every nontrivial element $w$ of the free group
$F_2$ on two generators, the word map
$\mathrm{SO}(3, \mathbb{R}) \times \mathrm{SO}(3, \mathbb{R}) \to \mathrm{SO}(3, \mathbb{R})$,
$(x, y) \mapsto w(x, y)$, is surjective.

Formalized by `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.so3WordMapsSurjective`, a definition declared in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#so3-word-maps-surjective).

## Some nontrivial word map on $\mathrm{PSL}(2, \mathbb{R})$ is not surjective (Kourovka 16.68(a))

There is a nontrivial element $w$ of the free group $F_2$ on two generators whose word map
$\mathrm{PSL}(2, \mathbb{R}) \times \mathrm{PSL}(2, \mathbb{R}) \to \mathrm{PSL}(2, \mathbb{R})$,
$(x, y) \mapsto w(x, y)$, is not surjective. That is, Mycielski's question has a negative answer
for $\mathrm{PSL}(2, \mathbb{R})$.

Nilradical (Theorem 2) gives an explicit nontrivial word $W$ (cyclically reduced length 44) with
$\operatorname{tr} W(A, B) > 7/4$ for all $A, B \in \mathrm{SL}(2, \mathbb{R})$; a nonidentity
involution of $\mathrm{PSL}(2, \mathbb{R})$ lifts to a matrix of trace $0$, so the word map of
$W$ misses it. The Kourovka Notebook (21st issue) records the negative answer for
$\mathrm{PSL}(2, \mathbb{R})$ (AI solution confirmed by A. Thom).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.68 (J. Mycielski); resolution: Nilradical v1.0.0, Word maps on PSL2: real and complex cases, result notes (21 September 2026); A. Thom, Convergent sequences in discrete groups, Canad. Math. Bull. 56 (2013), 424-433, Nilradical, Theorem 1 (every w ≠ 1 in F_2 induces a surjective map PSL_2(K)² → PSL_2(K) for K algebraically closed of characteristic 0) and Theorem 2 (an explicit W ≠ 1 with tr W(A, B) > 7/4 for all A, B ∈ SL_2(ℝ)); Thom, Corollary 1.2 (for every n and ε > 0 a word w ≠ 1 with ‖1 - w(u, v)‖ ≤ ε for all u, v ∈ U(n)), for SO(3, ℝ); the Kourovka Notebook (21st issue) marks 16.68 solved (AI solution confirmed by A. Thom; SO(3, ℝ) from Thom 2013), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/nilradical-kourovka-16-68-69.pdf.

Stated but not proved: `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.psl2RealWordMapsSurjective_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#psl2-real-word-maps-surjective-refuted).

## Nontrivial word maps on $\mathrm{PSL}(2, \mathbb{C})$ are surjective (Kourovka 16.68(b))

For every nontrivial element $w$ of the free group $F_2$ on two generators, the word map
$\mathrm{PSL}(2, \mathbb{C}) \times \mathrm{PSL}(2, \mathbb{C}) \to \mathrm{PSL}(2, \mathbb{C})$,
$(x, y) \mapsto w(x, y)$, is surjective. That is, Mycielski's question has an affirmative answer
for $\mathrm{PSL}(2, \mathbb{C})$.

Nilradical (Theorem 1) proves that for every algebraically closed field $K$ of characteristic
zero, in particular $\mathbb{C}$, every nontrivial word $w \in F_2$ induces a surjective map
$\mathrm{PSL}(2, K)^2 \to \mathrm{PSL}(2, K)$; the Kourovka Notebook (21st issue) records the
affirmative answer for $\mathrm{PSL}(2, \mathbb{C})$ (AI solution confirmed by A. Thom).

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.68 (J. Mycielski); resolution: Nilradical v1.0.0, Word maps on PSL2: real and complex cases, result notes (21 September 2026); A. Thom, Convergent sequences in discrete groups, Canad. Math. Bull. 56 (2013), 424-433, Nilradical, Theorem 1 (every w ≠ 1 in F_2 induces a surjective map PSL_2(K)² → PSL_2(K) for K algebraically closed of characteristic 0) and Theorem 2 (an explicit W ≠ 1 with tr W(A, B) > 7/4 for all A, B ∈ SL_2(ℝ)); Thom, Corollary 1.2 (for every n and ε > 0 a word w ≠ 1 with ‖1 - w(u, v)‖ ≤ ε for all u, v ∈ U(n)), for SO(3, ℝ); the Kourovka Notebook (21st issue) marks 16.68 solved (AI solution confirmed by A. Thom; SO(3, ℝ) from Thom 2013), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/nilradical-kourovka-16-68-69.pdf.

Stated but not proved: `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.psl2ComplexWordMapsSurjective_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#psl2-complex-word-maps-surjective-holds).

## Some nontrivial word map on $\mathrm{SO}(3, \mathbb{R})$ is not surjective (Kourovka 16.68(c))

There is a nontrivial element $w$ of the free group $F_2$ on two generators whose word map
$\mathrm{SO}(3, \mathbb{R}) \times \mathrm{SO}(3, \mathbb{R}) \to \mathrm{SO}(3, \mathbb{R})$,
$(x, y) \mapsto w(x, y)$, is not surjective. That is, Mycielski's question has a negative answer
for $\mathrm{SO}(3, \mathbb{R})$.

The Kourovka Notebook (21st issue) answers 16.68 negatively for $\mathrm{SO}(3, \mathbb{R})$,
noting that this follows from Thom (2013), whose Corollary 1.2 gives, for every
$\varepsilon > 0$, a nontrivial word $w$ with $\|1 - w(u, v)\| \le \varepsilon$ for all unitary
$u, v$, in particular for all $u, v \in \mathrm{SO}(3, \mathbb{R})$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.68 (J. Mycielski); resolution: Nilradical v1.0.0, Word maps on PSL2: real and complex cases, result notes (21 September 2026); A. Thom, Convergent sequences in discrete groups, Canad. Math. Bull. 56 (2013), 424-433, Nilradical, Theorem 1 (every w ≠ 1 in F_2 induces a surjective map PSL_2(K)² → PSL_2(K) for K algebraically closed of characteristic 0) and Theorem 2 (an explicit W ≠ 1 with tr W(A, B) > 7/4 for all A, B ∈ SL_2(ℝ)); Thom, Corollary 1.2 (for every n and ε > 0 a word w ≠ 1 with ‖1 - w(u, v)‖ ≤ ε for all u, v ∈ U(n)), for SO(3, ℝ); the Kourovka Notebook (21st issue) marks 16.68 solved (AI solution confirmed by A. Thom; SO(3, ℝ) from Thom 2013), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/nilradical-kourovka-16-68-69.pdf.

Stated but not proved: `MathlibExt.GroupTheory.WordMapsSurjectivityKourovka16Problem68Wanted.so3WordMapsSurjective_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordMapsSurjectivityKourovka16Problem68Wanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html#so3-word-maps-surjective-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Word maps on Lie groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/commutators-and-engel-conditions/word-maps-on-lie-groups)
