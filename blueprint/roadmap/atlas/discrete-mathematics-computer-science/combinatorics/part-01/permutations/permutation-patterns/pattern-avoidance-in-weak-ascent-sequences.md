---
declaration: section
origin: cited
lean: MetaMathlibExt.wordWeakAscents, MetaMathlibExt.IsWeakAscentSeq, MetaMathlibExt.ContainsPattern, MetaMathlibExt.lengthThreePatterns, MetaMathlibExt.ascentAvoiders, MetaMathlibExt.weakAscentAvoiders, MetaMathlibExt.isWeakAscentSeq_example, MetaMathlibExt.containsPattern_example
statement: formalized
---

# Pattern avoidance in weak ascent sequences

34 results, 17 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html).

## Number of weak ascents of a word

For a word $a_1 a_2 \cdots a_m$ of natural numbers,
$\mathrm{wasc}(a_1 \cdots a_m)$ is the number of weak ascents, that is, of positions $j$ with
$1 \le j < m$ and $a_j \le a_{j+1}$; in particular the empty word and every word of length one
have no weak ascents.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1 (definition of `wasc`).

Formalized by `MetaMathlibExt.wordWeakAscents`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#word-weak-ascents).

## Weak ascent sequence

A word $a_1 a_2 \cdots a_n$ over $\mathbb{N}$ is a weak ascent
sequence if either $n = 0$, or $a_1 = 0$ and $a_i \le 1 + \operatorname{wasc}(a_1 \cdots a_{i-1})$
for every $2 \le i \le n$, where $\operatorname{wasc}(u)$ is the number of weak ascents of $u$,
that is, of positions $j$ with $u_j \le u_{j+1}$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.IsWeakAscentSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#is-weak-ascent-seq).

## Pattern containment in words

A word $w$ over $\mathbb{N}$ contains a pattern $p$ (another
word over $\mathbb{N}$) if $w$ has a subsequence $s$, not necessarily contiguous, of the same
length as $p$ that is order-isomorphic to $p$: for all positions $i$ and $j$, $s_i < s_j$ if and
only if $p_i < p_j$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.ContainsPattern`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#contains-pattern).

## The thirteen patterns of length three

The set of patterns of length three consists of
the thirteen words $000$, $001$, $010$, $011$, $012$, $021$, $100$, $101$, $102$, $110$, $120$,
$201$ and $210$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.lengthThreePatterns`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#length-three-patterns).

## Ascent sequences avoiding a set of patterns

For a finite set $P$ of patterns (words over
$\mathbb{N}$) and $n \in \mathbb{N}$, $A_n(P)$ is the set of ascent sequences of length $n$ that
contain no pattern of $P$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.ascentAvoiders`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#ascent-avoiders).

## Weak ascent sequences avoiding a set of patterns

For a finite set $P$ of patterns
(words over $\mathbb{N}$) and a natural number $n$, $\mathrm{WA}_n(P)$ is the set of weak ascent
sequences of length $n$ that contain none of the patterns in $P$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.weakAscentAvoiders`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-avoiders).

## The weak ascent sequence $00203413$

The word $00203413$ has five weak ascents and is a
weak ascent sequence.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.isWeakAscentSeq_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#is-weak-ascent-seq-example).

## The word $00203413$ contains $011$

The word $00203413$ contains the pattern $011$.

For example, its subsequence $033$ is order-isomorphic to $011$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.containsPattern_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#contains-pattern-example).

## Number of patterns of length three

The set of patterns of length three,
$\{000, 001, 010, 011, 012, 021, 100, 101, 102, 110, 120, 201, 210\}$, has exactly $13$ elements.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 1.

Formalized by `MetaMathlibExt.card_lengthThreePatterns`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#card-length-three-patterns).

## Number of Wilf classes of ascent sequences avoiding four length-3 patterns

For a set $P$
of patterns, let $A_n(P)$ be the set of ascent sequences of length $n$ avoiding every pattern in
$P$. As $P$ ranges over the $4$-element subsets of the thirteen patterns of length three, the
counting sequences $n \mapsto |A_n(P)|$ take exactly $74$ distinct values. Equivalently, there are
$74$ A-Wilf-equivalence classes of such quadruples, where $P$ and $Q$ are A-Wilf equivalent when
$|A_n(P)| = |A_n(Q)|$ for every $n \ge 0$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 1.

Stated but not proved: `MetaMathlibExt.ascent_wilf_classes_quadruples` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#ascent-wilf-classes-quadruples).

## WA-Wilf classes of pattern quadruples

Write $\mathrm{WA}_n(P)$ for the set of weak ascent
sequences of length $n$ avoiding every pattern in $P$, and call two sets of patterns $P$ and $Q$
WA-Wilf equivalent when $|\mathrm{WA}_n(P)| = |\mathrm{WA}_n(Q)|$ for every $n \ge 0$. As $P$
ranges over the $4$-element subsets of the thirteen patterns of length three, the counting
sequences $n \mapsto |\mathrm{WA}_n(P)|$ take exactly $228$ or exactly $229$ distinct values;
that is, there are $228$ or $229$ WA-Wilf equivalence classes of such quadruples.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 2.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_classes_quadruples` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-classes-quadruples).

## Weakly increasing weak ascent sequences: Catalan and Motzkin counts

Let $C_n$ denote the
Catalan numbers and $M_n$ the Motzkin numbers. For every natural number $n$, (i) the number of
weakly increasing weak ascent sequences of length $n$ is $C_n$, and (ii) the number of weakly
increasing weak ascent sequences of length $n$ that avoid the pattern $000$ is $M_n$.

At $n = 0$ both counts are $1$, from the empty sequence.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Proposition 1.

Stated but not proved: `MetaMathlibExt.weakAscent_weaklyIncreasing_card` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-weakly-increasing-card).

## Weak ascent Wilf equivalence, class 99

Write $\mathrm{WA}_n(P)$ for the set of weak
ascent sequences of length $n$ avoiding every pattern in $P$, with patterns written as words (for
example $011$). The pattern sets $\{011, 100, 102, 201\}$ and $\{011, 100, 120, 201\}$ are WA-Wilf
equivalent: for every $n \ge 0$,
$|\mathrm{WA}_n(\{011, 100, 102, 201\})| = |\mathrm{WA}_n(\{011, 100, 120, 201\})|$.

## Sources

- the extracted record drops the `w` marker on `∼`; the weak-ascent reading follows from the class number (the paper has 74 A-classes, and its class table numbered past 74 is the WA table).
- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 5.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class99` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class99).

## Weak ascent Wilf equivalence and generating function, class 93

Write $\mathrm{WA}_n(P)$
for the set of weak ascent sequences of length $n$ avoiding every pattern in $P$, with patterns
written as words (for example $011$). The pattern sets $P = \{011, 102, 120, 201\}$ and
$\{011, 102, 120, 210\}$ are WA-Wilf equivalent, that is,
$|\mathrm{WA}_n(P)| = |\mathrm{WA}_n(\{011, 102, 120, 210\})|$ for every $n \ge 0$. Moreover, the
formal power series $F(x) = \sum_{n \ge 1} |\mathrm{WA}_n(P)| \, x^n$ in $\mathbb{Z}[[x]]$
(without the $n = 0$ term) satisfies $F(x) \, (1 - 2x)(1 - x)^2 = x(2x^2 - 2x + 1)$, that is,
$F(x) = \frac{x(2x^2 - 2x + 1)}{(1 - 2x)(1 - x)^2}$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 7.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class93` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class93).

## Weak-ascent Wilf equivalence in Class 162

For every natural number $n$, the number of
weak ascent sequences of length $n$ avoiding every pattern in $\{010, 100, 101, 120\}$ equals the
number avoiding every pattern in $\{010, 100, 110, 120\}$.

That is, the two sets are WA-Wilf equivalent.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 8.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class162` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class162).

## Weak-ascent Wilf equivalence in Class 205

For every natural number $n$, the number of
weak ascent sequences of length $n$ avoiding every pattern in $\{100, 102, 120, 201\}$ equals the
number avoiding every pattern in $\{102, 110, 120, 201\}$.

That is, the two sets are WA-Wilf equivalent.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 9.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class205` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class205).

## Weak-ascent Wilf equivalence in Class 206

For every natural number $n$, the number of
weak ascent sequences of length $n$ avoiding every pattern in $\{100, 102, 120, 210\}$ equals
the number avoiding every pattern in $\{101, 102, 120, 201\}$, the number avoiding every
pattern in $\{101, 102, 120, 210\}$ and the number avoiding every pattern in
$\{102, 110, 120, 210\}$.

That is, the four sets are WA-Wilf equivalent.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 10.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class206` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class206).

## Weak-ascent Wilf equivalence in Class 219

For every natural number $n$, the number of
weak ascent sequences of length $n$ avoiding every pattern in $\{100, 101, 102, 201\}$ equals
the number avoiding every pattern in $\{100, 110, 120, 201\}$.

That is, the two sets are WA-Wilf equivalent. They are not Wilf equivalent for ascent
sequences: the numbers of ascent sequences avoiding them first differ at length $5$, where
they are $29$ and $30$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 11.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class219` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class219).

## Fibonacci closed form of a binomial sum with powers of two

Let $F_m$ denote the
Fibonacci numbers, with $F_0 = 0$ and $F_1 = 1$. For every natural number $n \ge 4$,

$$\sum_{k=1}^{\lfloor n/3 \rfloor - 1} \left( \binom{n-k-4}{2k} 2^{n-3k-4} +
\binom{n-k-4}{2k-1} 2^{n-3k-3} \right) + 2^{n-4} = F_{2n-7}.$$

The sum is empty for $n < 6$. When $3$ divides $n$, the last index $k = n/3 - 1$ gives the
exponent $n - 3k - 4 = -1$, but there $\binom{n-k-4}{2k} = 0$, and the product
$\binom{n-k-4}{2k} 2^{n-3k-4}$ is read as $0$; the other product in that summand is $1$.

The source states this as the sum being $F_{2n-7} - 2^{n-4}$. The summand is reconstructed from
an extracted display of the source's Proposition 2(i), as the full text was not available; exact
computation confirms the identity for $4 \le n \le 500$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Proposition 3, with the sum of Proposition 2(i).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_two_pow_add_two_pow_eq_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#sum-choose-mul-two-pow-add-two-pow-eq-fi).

## Reducible pattern sets (Theorem 3)

For a set $P$ of patterns, let $A_n(P)$ and
$WA_n(P)$ be the sets of ascent sequences and of weak ascent sequences of length $n$ that
avoid every pattern in $P$. For each set $C$ of patterns and each pattern $\tau$ listed below,
with $B = C \cup \{\tau\}$, we have $A_n(B) = A_n(C)$ and $WA_n(B) = WA_n(C)$ for every
natural number $n$:

- $C = \{001\}$ and $\tau \in \{101, 102, 201\}$;
- $C = \{011\}$ and $\tau \in \{101, 110\}$;
- $C = \{012\}$ and $\tau \in \{102, 120\}$;
- $C = \{021\}$ and $\tau \in \{201, 210\}$;
- $C = \{000, 001\}$ and $\tau = 100$;
- $C = \{000, 011\}$ and $\tau \in \{100, 201, 210\}$;
- $C = \{000, 012\}$ and $\tau \in \{201, 210\}$;
- $C = \{000, 021\}$ and $\tau = 100$;
- $C = \{001, 010\}$ and $\tau \in \{021, 100, 110, 120, 210\}$;
- $C = \{001, 011\}$ and $\tau = 021$;
- $C = \{001, 012\}$ and $\tau = 021$;
- $C = \{001, 110\}$ and $\tau = 210$;
- $C = \{001, 120\}$ and $\tau = 210$;
- $C = \{010, 011\}$ and $\tau = 100$;
- $C = \{010, 012\}$ and $\tau \in \{101, 201\}$;
- $C = \{010, 021\}$ and $\tau \in \{100, 101, 102, 110, 120\}$;
- $C = \{001, 011, 012\}$, $\{001, 011, 100\}$ or $\{001, 012, 100\}$, and $\tau = 210$.

These are $36$ pairs $C \subsetneq B$. The paper writes $C \sim_r B$ and takes the result from
its reference [5].

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 3.

Stated but not proved: `MetaMathlibExt.reducible_pattern_sets` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#reducible-pattern-sets).

## Motzkin counts for weak ascent sequences in Class 86

Let $M_n$ denote the Motzkin
numbers. For every natural number $n \ge 3$, the number of weak ascent sequences of length $n$
avoiding every pattern in $\{000, 021, 101, 120\}$, the number avoiding every pattern in
$\{000, 021, 101, 102\}$ and the number avoiding every pattern in $\{000, 021, 110, 120\}$ are
each equal to $M_n + M_{n-2}$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 4.

Stated but not proved: `MetaMathlibExt.weakAscent_class86_card_eq_motzkin` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-class86-card-eq-motzkin).

## Weak-ascent Wilf equivalence in Class 61

For every natural number $n$, the number of
weak ascent sequences of length $n$ avoiding every pattern in $\{010, 011, 102, 201\}$ equals the
number avoiding every pattern in $\{010, 011, 120, 201\}$.

That is, the two sets are WA-Wilf equivalent.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 6.

Stated but not proved: `MetaMathlibExt.weakAscent_wilf_class61` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-wilf-class61).

## Generating function for weak ascent sequences avoiding 101, 102, 110 and 201

Let $a_n$
be the number of weak ascent sequences of length $n$ that avoid each of the patterns $101$,
$102$, $110$ and $201$, and let $F = \sum_{n \ge 0} a_n X^n$ in $\mathbb{Q}[[X]]$. For every
power series $S \in \mathbb{Q}[[X]]$ with $S^2 = 1 - 4X$ and constant term $1$,

$$F \cdot 2(1 - X)(1 - 4X - X^2) = (2 - 3X - X^2) S - X - X^2.$$

Such an $S$ is the power series $\sqrt{1 - 4X}$, and $1 - X$ and $1 - 4X - X^2$ are invertible,
so this is the formula
$F = \frac{(2 - 3X - X^2)\sqrt{1 - 4X} - X - X^2}{2(1 - X)(1 - 4X - X^2)}$ with the denominator
cleared.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Theorem 12.

Stated but not proved: `MetaMathlibExt.weakAscent_class211_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#weak-ascent-class211-generating-function).

## Big entry

Let $w = w_1 \cdots w_n$ be a word over $\mathbb{N}$ and $2 \le k \le n$. The
entry $w_k$ is a big entry of $w$ if it equals $1$ plus the number of weak ascents of
$w_1 \cdots w_{k-1}$, that is, of positions $j < k - 1$ with $w_j \le w_{j+1}$. In a weak ascent
sequence this is the largest value allowed at position $k$. The entry $w_k$ is referred to by its
zero-based index $i = k - 1$, so the index ranges over $1 \le i < n$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3 (definition of big entry).

Formalized by `MetaMathlibExt.IsBigEntry`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#is-big-entry).

## Big entries of $00203413$

In the word $w = 00203413$, with positions numbered from $1$,
the entries $w_3 = 2$ and $w_6 = 4$ are big entries and the entry $w_7 = 1$ is not.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3.

Formalized by `MetaMathlibExt.isBigEntry_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#is-big-entry-example).

## Position of the last descent top

For a finite sequence $w = w_1 w_2 \cdots w_m$ of
natural numbers, a descent of $w$ is an index $1 \le i < m$ with $w_i > w_{i+1}$, and $w_i$ is
its descent top. The position of the last descent top of $w$ is the largest index $i$ with
$w_i > w_{i+1}$ (positions counted from $1$), and it is $0$ if $w$ has no descent.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3 (definition of `W_{n,k}`).

Formalized by `MetaMathlibExt.lastDescentTop`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#last-descent-top).

## Examples of the last descent top

Each of the sequences $0010$, $0020$, $0021$ and
$0120$ has its last descent top at position $3$, and the sequence $012$, which has no
descent, has last descent top position $0$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3.

Formalized by `MetaMathlibExt.lastDescentTop_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#last-descent-top-example).

## The sets $U_{n,j}$

Let $W_n = WA_n(011, 100, 201, 210)$ be the set of weak ascent
sequences of length $n$ that avoid each of the patterns $011$, $100$, $201$ and $210$. For
natural numbers $n$ and $j$, $U_{n,j}$ is the set of sequences $w = w_1 w_2 \cdots w_n$ in
$W_n$ such that the last descent top of $w$ is at position $n - 1$, $w$ has a big entry, the
first $n - 2$ entries of $w$ are not all $0$, $w_{n-1} \ne n - 2$, and $w_{n-1} = w_n + j$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3.2 (definition of `U_{n,j}`).

Formalized by `MetaMathlibExt.quadrupleUSet`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#quadruple-uset).

## $U_{0,j}$ is empty

For every natural number $j$, the set $U_{0,j}$ is empty.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3.2.

Formalized by `MetaMathlibExt.quadrupleUSet_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#quadruple-uset-zero).

## The sets $V_{n,j}$

Let $W_n = WA_n(011, 100, 201, 210)$ be the set of weak ascent
sequences of length $n$ that avoid each of the patterns $011$, $100$, $201$ and $210$. For
natural numbers $n$ and $j$, $V_{n,j}$ is the set of sequences $w = w_1 w_2 \cdots w_n$ in
$W_n$ such that the last descent top of $w$ is at position $n - 2$, $w_n \le n - 3$,
$w_{n-1} \ne 0$, and $w_{n-2} = w_{n-1} + j$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3.2 (definition of `V_{n,j}`).

Formalized by `MetaMathlibExt.quadrupleVSet`, a definition declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#quadruple-vset).

## $V_{n,j}$ lies in $W_n$

For all natural numbers $n$ and $j$, the set $V_{n,j}$ is
contained in $W_n = WA_n(011, 100, 201, 210)$, the set of weak ascent sequences of length $n$
that avoid each of the patterns $011$, $100$, $201$ and $210$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Section 4.3.2.

Formalized by `MetaMathlibExt.quadrupleVSet_subset`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#quadruple-vset-subset).

## Successors of big entries in $W_n$

Let $W_n$ be the set of weak ascent sequences of length
$n$ avoiding the patterns $011$, $100$, $201$ and $210$, and let $w = w_1 \cdots w_n \in W_n$. If
$2 \le k \le n - 1$ and $w_k$ is a big entry of $w$, then either $w_{k+1}$ is a big entry, or
$w_{k+1} < w_k$ and $w_j$ is a big entry for every $j$ with $k + 2 \le j \le n$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Lemma 1.

Stated but not proved: `MetaMathlibExt.isBigEntry_succ_or_descent` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#is-big-entry-succ-or-descent).

## Recurrence for $|U_{n,1}|$ and $|V_{n,1}|$ (Lemma 2)

Let $f$ be either of the
sequences $u_n = |U_{n,1}|$ and $v_n = |V_{n,1}|$. Then $f_j = 0$ for every $j \le 5$,
$f_6 = 1$, and $f_n = 5 f_{n-1} - 7 f_{n-2} + 2 f_{n-3}$ for every $n \ge 7$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Lemma 2.

Stated but not proved: `MetaMathlibExt.quadrupleUSet_quadrupleVSet_recurrence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#quadruple-uset-quadruple-vset-recurrence).

## Sum formulas for $|U_{n,1}|$ and $|V_{n,1}|$ (Proposition 2)

For every natural number
$n$ let $f(n, a) = \min(n - 3 - a, \lfloor (a - 1)/2 \rfloor)$ and

$$
S(n) = \sum_{a=2}^{n-4} \sum_{k=1}^{f(n,a)} \left( \binom{a-2}{2k} 2^{a-2k-2} +
\binom{a-2}{2k-1} 2^{a-2k-1} \right) (n - k - a - 2).
$$

Then for every $n \ge 1$

$$
|U_{n,1}| = \sum_{k=1}^{\lfloor n/3 \rfloor - 1} \left( \binom{n-k-4}{2k} 2^{n-3k-4} +
\binom{n-k-4}{2k-1} 2^{n-3k-3} \right)
$$

and

$$
|V_{n,1}| = \sum_{a=2}^{n-4} 2^{a-2} (n - a - 3) + S(n),
$$

and for every $n \ge 4$

$$
|V_{n,1}| = 2^{n-4} - n + 3 + S(n).
$$

A sum whose upper limit is below its lower limit is empty, and an exponent such as
$n - 3k - 4$ is negative only where the binomial coefficient multiplying it is $0$; such a
term is $0$. The last formula is stated only for $n \ge 4$: at $n = 3$ the expression
$2^{n-4} - n + 3$ equals $1/2$, while $\sum_{a=2}^{n-4} 2^{a-2} (n - a - 3)$ is $0$.

## Sources

- David Callan and Toufik Mansour, *Ascent Sequences and Weak Ascent Sequences Avoiding a Quadruple of Length-3 Patterns*, INTEGERS 25 (2025), Article A80, Proposition 2.

Stated but not proved: `MetaMathlibExt.quadrupleUSet_quadrupleVSet_card_formulas` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean, line 450](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AscentSequenceQuadruplePatternsWanted.lean#L450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html#quadruple-uset-quadruple-vset-card-formu).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pattern avoidance in weak ascent sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/pattern-avoidance-in-weak-ascent-sequences)
