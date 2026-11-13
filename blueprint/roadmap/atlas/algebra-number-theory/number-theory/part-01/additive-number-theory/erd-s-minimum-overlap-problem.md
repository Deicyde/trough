---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.Overlap, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.MaxOverlap, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.M, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.Overlap_le_MaxOverlap, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.MaxOverlap_attained, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.balancedPartition_nonempty, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.M_attained, MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.M_le_MaxOverlap
statement: formalized
---

# Erdős minimum overlap problem

56 results, 39 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html).

## Overlap count of two finite sets of integers

For finite sets $A, B \subseteq \mathbb{Z}$
and an integer $k$, the overlap of $A$ and $B$ at $k$ is the number of pairs
$(a, b) \in A \times B$ with $a - b = k$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.Overlap`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#overlap).

## Maximum overlap

For finite sets $A, B \subseteq \mathbb{Z}$, the maximum overlap of $A$
and $B$ is the natural number obtained as the supremum over all integers $k$ of
$\#\{(a, b) \in A \times B : a - b = k\}$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.MaxOverlap`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#max-overlap).

## Erdős minimum overlap function

For a natural number $n$, $M(n)$ is the least value of
the maximum overlap of $A$ and $B$, the supremum over $k \in \mathbb{Z}$ of
$\#\{(a, b) \in A \times B : a - b = k\}$, taken over all pairs of disjoint finite sets
$A, B \subseteq \mathbb{Z}$ with $A \cup B = \{1, \dots, 2n\}$ and $|A| = |B|$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.M`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#m).

## Overlaps are bounded by the maximum overlap

For finite sets $A, B \subseteq \mathbb{Z}$
and every integer $k$, the overlap $\#\{(a, b) \in A \times B : a - b = k\}$ is at most the
maximum overlap of $A$ and $B$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.Overlap_le_MaxOverlap`, a theorem declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#overlap-le-max-overlap).

## The maximum overlap is attained

For finite sets $A, B \subseteq \mathbb{Z}$ there is an
integer $k$ such that the maximum overlap of $A$ and $B$, the supremum over $j \in \mathbb{Z}$
of $\#\{(a, b) \in A \times B : a - b = j\}$, equals
$\#\{(a, b) \in A \times B : a - b = k\}$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.MaxOverlap_attained`, a theorem declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#max-overlap-attained).

## Balanced partitions of $\{1, \dots, 2n\}$ exist

For every natural number $n$, the set of
maximum overlaps of $A$ and $B$, taken over all pairs of disjoint finite sets of integers $A$ and
$B$ with $A \cup B = \{1, \dots, 2n\}$ and $|A| = |B|$, is nonempty.

For example, $A = \{1, \dots, n\}$ and $B = \{n + 1, \dots, 2n\}$ is such a pair.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.balancedPartition_nonempty`, a theorem declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#balanced-partition-nonempty).

## The minimum overlap is attained

For every natural number $n$ there are disjoint finite
sets $A, B \subseteq \mathbb{Z}$ with $A \cup B = \{1, \dots, 2n\}$ and $|A| = |B|$ such that
the minimum overlap $M(n)$ equals the maximum overlap of $A$ and $B$, the supremum over
$k \in \mathbb{Z}$ of $\#\{(a, b) \in A \times B : a - b = k\}$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.M_attained`, a theorem declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#m-attained).

## The minimum overlap bounds every balanced partition

Let $n$ be a natural number and let
$A, B \subseteq \mathbb{Z}$ be disjoint finite sets with $A \cup B = \{1, \dots, 2n\}$ and
$|A| = |B|$. Then the minimum overlap $M(n)$ is at most the maximum overlap of $A$ and $B$,
the supremum over $k \in \mathbb{Z}$ of $\#\{(a, b) \in A \times B : a - b = k\}$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.M_le_MaxOverlap`, a theorem declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#m-le-max-overlap).

## Normalized minimum overlap

For a natural number $N$, the normalized minimum overlap is
the real number $M(N) / N$, where $M(N)$ is the Erdős minimum overlap function; for $N = 0$
the quotient is $0$ by the convention $x / 0 = 0$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.MinOverlapQuotient`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#min-overlap-quotient).

## Universal asymptotic lower bound for discrete overlaps

A real number $c$ is a
universal asymptotic lower bound when for every $\varepsilon > 0$ there is a positive integer
$N_0$ such that for every $N \ge N_0$ and all disjoint finite sets $A, B \subseteq \mathbb{Z}$
with $A \cup B = \{1, \dots, 2N\}$ and $|A| = |B|$, some integer $x$ satisfies
$(c - \varepsilon) N \le \#\{(a, b) \in A \times B : a - b = x\}$.

The positive size threshold $N_0$ is chosen before the size $N$ and the partition.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.DiscreteUniversalLowerBound`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#discrete-universal-lower-bound).

## Continuous support interval

The support interval of the continuous minimum-overlap
problem is the closed interval $[-1, 1]$ of real numbers.

Functions in the continuous model are extended by zero outside this interval.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousSupportInterval`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-support-interval).

## Translation interval of the continuous overlap model

The translation interval of the
continuous minimum-overlap model is the closed interval $[-2, 2] \subseteq \mathbb{R}$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousTranslationInterval`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-translation-interval).

## Continuous overlap integrand

For functions $f, g : \mathbb{R} \to \mathbb{R}$ and real
numbers $x$ and $t$, the overlap integrand is $f(t)\,g(x + t)$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousOverlapIntegrand`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-overlap-integrand).

## Continuous overlap

For functions $f, g : \mathbb{R} \to \mathbb{R}$ and a translation
$x \in \mathbb{R}$, the overlap of $f$ and $g$ at $x$ is $\int_{-1}^{1} f(t)\,g(x + t)\,dt$, the
integral of the overlap integrand over the support interval $[-1, 1]$.

The integral is the Lebesgue (Bochner) integral, which is $0$ when the integrand is not
integrable.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousOverlap`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-overlap).

## Continuous overlap values

For functions $f, g : \mathbb{R} \to \mathbb{R}$, the set of
overlap values of $f$ and $g$ is the image of the translation interval $[-2, 2]$ under the overlap
$x \mapsto \int_{-1}^{1} f(t)\,g(x + t)\,dt$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousOverlapValues`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-overlap-values).

## Admissible pairs for the continuous minimum-overlap problem

A pair of functions
$f, g : \mathbb{R} \to \mathbb{R}$ is admissible when $f$ and $g$ are almost everywhere measurable
with respect to Lebesgue measure, take values in $[0, 1]$ at every point, vanish at every point
outside the support interval $[-1, 1]$, satisfy $f(t) + g(t) = 1$ for every $t \in [-1, 1]$, and
satisfy $\int_{\mathbb{R}} f(t)\,dt = 1$.

Since measurability is only required almost everywhere, Lebesgue-null modifications of Borel
functions are included. Integrability and the bounds on the overlap follow from these conditions.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.ContinuousAdmissible`, a structure declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-admissible).

## Continuous pair score

For functions $f, g : \mathbb{R} \to \mathbb{R}$, the pair score of
$f$ and $g$ is the supremum of the overlap values $\int_{-1}^{1} f(t)\,g(x + t)\,dt$ over the
translations $x \in [-2, 2]$.

As with every supremum of real numbers here, it is $0$ when the set is not bounded above; for
admissible pairs the overlap values lie in $[0, 1]$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousPairScore`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-pair-score).

## Universal lower bound in the continuous overlap model

Call a pair of functions
$f, g : \mathbb{R} \to \mathbb{R}$ admissible when $f$ and $g$ are almost everywhere measurable,
take values in $[0, 1]$, vanish outside $[-1, 1]$, satisfy $f + g = 1$ on $[-1, 1]$, and
$\int_{\mathbb{R}} f = 1$, and let the pair score $S(f, g)$ be the supremum over $x \in [-2, 2]$
of $\int_{-1}^{1} f(t)\, g(x + t)\, dt$. A real number $c$ is a universal lower bound when
$c \le S(f, g)$ for every admissible pair $(f, g)$.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.ContinuousUniversalLowerBound`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-universal-lower-bound).

## The continuous Erdős minimum-overlap constant

For an admissible pair $(f, g)$ let
$S(f, g)$ be its pair score, the supremum over $x \in [-2, 2]$ of
$\int_{-1}^{1} f(t)\,g(x + t)\,dt$. The continuous minimum-overlap constant $C_{1b}$ is the
supremum of the set of real numbers $c$ such that $c \le S(f, g)$ for every admissible pair
$(f, g)$.

## Sources

- Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousMinimumOverlapConstant`, a definition declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-minimum-overlap-constant).

## Notation $C_{1b}$

We write $C_{1b}$ for the continuous Erdős minimum-overlap constant.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.C₁ᵦ`, an abbreviation declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#c).

## The continuous minimum-overlap constant is at most $1/2$

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 1/2$.

The bound is witnessed by the admissible pair $f = g$ with value $1/2$ on $[-1, 1]$ and $0$
elsewhere.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousMinimumOverlapConstant_le_half`, a theorem declared in [MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ErdosMinimumOverlapConstant.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-minimum-overlap-constant-le-h).

## The proposition that $M(N)/N$ tends to $C_{1b}$

For a natural number $N$ let $M(N)$ be
the Erdős minimum overlap function: the least, over all pairs of disjoint finite sets
$A, B \subseteq \mathbb{Z}$ with $A \cup B = \{1, \dots, 2N\}$ and $|A| = |B|$, of the largest
number of pairs $(a, b) \in A \times B$ with a given difference $a - b$. This is the proposition
that $M(N)/N$ tends to the continuous Erdős minimum-overlap constant $C_{1b}$ as $N \to \infty$.

## Sources

- Haugland 2016; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousDiscreteEquivalence`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-discrete-equivalence).

## The proposition that $C_{1b}$ is the largest asymptotic overlap constant

Call a real
number $c$ a universal asymptotic lower bound when for every $\varepsilon > 0$ there is a
positive integer $N_0$ such that for every $N \ge N_0$ and all disjoint finite sets
$A, B \subseteq \mathbb{Z}$ with $A \cup B = \{1, \dots, 2N\}$ and $|A| = |B|$, some integer $x$
satisfies $(c - \varepsilon) N \le \#\{(a, b) \in A \times B : a - b = x\}$. This is the
proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ is a universal asymptotic
lower bound and that every universal asymptotic lower bound $c$ satisfies $c \le C_{1b}$.

## Sources

- Haugland 2016; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousDiscreteAsymptoticCharacterization`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-discrete-asymptotic-character).

## Erdős's upper bound $1/2$ for the minimum-overlap constant (statement)

The statement that
the continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 1/2$.

## Sources

- Erdős 1955; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_E1955_half`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-e1955-half).

## Erdős's unpublished upper bound $4/9$ for the minimum-overlap constant (statement)

The
statement that the continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 4/9$.

## Sources

- Erdős, unpublished; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_Erdos_unpublished_fourNinths`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-erdos-unpublished-four-ninth).

## Statement of the Motzkin–Ralston–Selfridge upper bound $5/12$ for the minimum-overlap constant

**Statement of the Motzkin–Ralston–Selfridge upper bound $5/12$ for the minimum-overlap
constant.** The proposition that the continuous Erdős minimum-overlap constant $C_{1b}$
satisfies $C_{1b} \le 5/12$.

## Sources

- Motzkin--Ralston--Selfridge 1956; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_MRS1956_fiveTwelfths`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-mrs1956-five-twelfths).

## Statement of the Motzkin–Ralston–Selfridge upper bound $0.4$ for the minimum-overlap constant

**Statement of the Motzkin–Ralston–Selfridge upper bound $0.4$ for the minimum-overlap
constant.** The proposition that the continuous Erdős minimum-overlap constant $C_{1b}$
satisfies $C_{1b} \le 0.4$.

## Sources

- Motzkin--Ralston--Selfridge 1956; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_MRS1956_pointFour`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-mrs1956-point-four).

## Statement of Haugland's unpublished 1993 upper bound for the minimum-overlap constant

The proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ satisfies
$C_{1b} \le 0.385694$.

## Sources

- Haugland, unpublished 1993; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_Haugland_unpublished_1993`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-haugland-unpublished-1993).

## Statement of Haugland's 1996 upper bound for the minimum-overlap constant

The
proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ satisfies
$C_{1b} \le 0.382002$.

## Sources

- Haugland 1996; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_H1996`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-h1996).

## Statement of Haugland's 2016 upper bound for the minimum-overlap constant

The
proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ satisfies
$C_{1b} \le 0.380926$.

## Sources

- Haugland 2016; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_H2016`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-h2016).

## AlphaEvolve upper bound for the minimum-overlap constant (statement)

The statement that
the continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.380924$.

## Sources

- Georgiev--Gómez-Serrano--Tao--Wagner 2025; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_GGSWT2025_AlphaEvolve`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-ggswt2025-alpha-evolve).

## TTT-Discover 2026 upper bound statement for the minimum overlap constant

This is the
proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ is at most $0.380876$.

## Sources

- Yuksekgonul et al. 2026 (TTT-Discover); Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_YKLBMWKCZGS2026_TTTDiscover`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-yklbmwkczgs2026-tttdiscover).

## Together AI 2026 upper bound statement for the minimum overlap constant

This is the
proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ is at most $0.380871$.

## Sources

- Together AI 2026; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_T2026_TogetherAI`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-t2026-together-ai).

## SimpleTES 2026 upper bound statement for the minimum overlap constant

This is the
proposition that the continuous Erdős minimum-overlap constant $C_{1b}$ is at most $0.380868$.

## Sources

- Ye et al. 2026 (SimpleTES); Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_YLTLYSTYLLGDHZSWZSHMELCZX2026_SimpleTES`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-yltlystyllgdhzswzshmelczx202).

## The proposition $1/4 \le C_{1b}$

This is the proposition that the continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $1/4 \le C_{1b}$.

## Sources

- Erdős 1955; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_E1955_quarter`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-e1955-quarter).

## Scherk's lower bound for the minimum-overlap constant (statement)

The statement that the
continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $1 - 1/\sqrt{2} \le C_{1b}$.

## Sources

- Scherk, unpublished 1955; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_Scherk_unpublished_1955`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-scherk-unpublished-1955).

## The proposition $(4 - \sqrt{6})/5 \le C_{1b}$

This is the proposition that the continuous
Erdős minimum-overlap constant $C_{1b}$ satisfies $(4 - \sqrt{6})/5 \le C_{1b}$.

## Sources

- Swierczkowski 1958; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_S1958`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-s1958).

## The proposition $\sqrt{4 - \sqrt{15}} \le C_{1b}$

This is the proposition that the
continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $\sqrt{4 - \sqrt{15}} \le C_{1b}$.

## Sources

- Moser 1959; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_M1959`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-m1959).

## White's lower bound for the minimum-overlap constant (statement)

The statement that the
continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $0.379005 \le C_{1b}$, where
$0.379005$ is the exact rational number $379005/1000000$.

## Sources

- White 2022; Optimization Problems, Constant 1b.

Formalized by `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_W2022`, a definition declared in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-w2022).

## The normalized minimum overlap tends to $C_{1b}$

For a natural number $N$ let $M(N)$ be
the Erdős minimum overlap function: the least, over all pairs of disjoint finite sets
$A, B \subseteq \mathbb{Z}$ with $A \cup B = \{1, \dots, 2N\}$ and $|A| = |B|$, of the largest
number of pairs $(a, b) \in A \times B$ with a given difference $a - b$. Then $M(N)/N$ tends to
the continuous Erdős minimum-overlap constant $C_{1b}$ as $N \to \infty$.

## Sources

- Haugland 2016 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousDiscreteEquivalence_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-discrete-equivalence-holds).

## The continuous constant $C_{1b}$ is the largest asymptotic overlap constant

Call a real
number $c$ a universal asymptotic lower bound when for every $\varepsilon > 0$ there is a
positive integer $N_0$ such that for every $N \ge N_0$ and all disjoint finite sets
$A, B \subseteq \mathbb{Z}$ with $A \cup B = \{1, \dots, 2N\}$ and $|A| = |B|$, some integer $x$
satisfies $(c - \varepsilon) N \le \#\{(a, b) \in A \times B : a - b = x\}$. Then the continuous
Erdős minimum-overlap constant $C_{1b}$ is a universal asymptotic lower bound, and every
universal asymptotic lower bound $c$ satisfies $c \le C_{1b}$.

## Sources

- Haugland 2016 and the uniform partition clause of Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.continuousDiscreteAsymptoticCharacterization_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#continuous-discrete-asymptotic-character-2).

## Erdős's unpublished upper bound $4/9$ for the minimum-overlap constant

The continuous
Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 4/9$.

## Sources

- Erdős, unpublished, recorded by Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_Erdos_unpublished_fourNinths_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-erdos-unpublished-four-ninth-2).

## Motzkin–Ralston–Selfridge upper bound $5/12$ for the minimum-overlap constant

The
continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 5/12$.

## Sources

- Motzkin--Ralston--Selfridge 1956 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_MRS1956_fiveTwelfths_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-mrs1956-five-twelfths-holds).

## Motzkin–Ralston–Selfridge upper bound $0.4$ for the minimum-overlap constant

The
continuous Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.4$.

## Sources

- Motzkin--Ralston--Selfridge 1956 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_MRS1956_pointFour_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-mrs1956-point-four-holds).

## Haugland's unpublished 1993 upper bound for the minimum-overlap constant

The continuous
Erdős minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.385694$.

## Sources

- Haugland, unpublished 1993, recorded by Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_Haugland_unpublished_1993_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-haugland-unpublished-1993-ho).

## Haugland's 1996 upper bound for the minimum-overlap constant

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.382002$.

## Sources

- Haugland 1996 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_H1996_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-h1996-holds).

## Haugland's 2016 upper bound for the minimum-overlap constant

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.380926$.

## Sources

- Haugland 2016 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_H2016_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-h2016-holds).

## AlphaEvolve upper bound for the minimum-overlap constant

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.380924$.

## Sources

- Georgiev--Gómez-Serrano--Tao--Wagner 2025 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_GGSWT2025_AlphaEvolve_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-ggswt2025-alpha-evolve-holds).

## TTT-Discover 2026 upper bound for the minimum overlap constant holds

The continuous
Erdős minimum-overlap constant $C_{1b}$ is at most $0.380876$.

## Sources

- Yuksekgonul et al. 2026 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_YKLBMWKCZGS2026_TTTDiscover_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-yklbmwkczgs2026-tttdiscover-2).

## Together AI's 2026 upper bound for the minimum-overlap constant

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $C_{1b} \le 0.380871$.

## Sources

- Together AI 2026 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_T2026_TogetherAI_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-t2026-together-ai-holds).

## SimpleTES 2026 upper bound for the minimum overlap constant holds

The continuous
Erdős minimum-overlap constant $C_{1b}$ is at most $0.380868$.

## Sources

- Ye et al. 2026 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.upperBound_YLTLYSTYLLGDHZSWZSHMELCZX2026_SimpleTES_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#upper-bound-yltlystyllgdhzswzshmelczx202-2).

## Erdős's lower bound $C_{1b} \ge 1/4$

The continuous Erdős minimum-overlap constant
$C_{1b}$ satisfies $1/4 \le C_{1b}$.

## Sources

- Erdős 1955 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_E1955_quarter_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-e1955-quarter-holds).

## Scherk's lower bound for the minimum-overlap constant

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $1 - 1/\sqrt{2} \le C_{1b}$.

## Sources

- Scherk, unpublished 1955, recorded by Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_Scherk_unpublished_1955_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-scherk-unpublished-1955-hold).

## Świerczkowski's lower bound $C_{1b} \ge (4 - \sqrt{6})/5$

The continuous Erdős
minimum-overlap constant $C_{1b}$ satisfies $(4 - \sqrt{6})/5 \le C_{1b}$.

## Sources

- Swierczkowski 1958 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_S1958_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-s1958-holds).

## Moser's lower bound $C_{1b} \ge \sqrt{4 - \sqrt{15}}$

The continuous Erdős minimum-overlap
constant $C_{1b}$ satisfies $\sqrt{4 - \sqrt{15}} \le C_{1b}$.

## Sources

- Moser 1959 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_M1959_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-m1959-holds).

## White's lower bound for the minimum-overlap constant

The continuous Erdős minimum-overlap
constant $C_{1b}$ satisfies $0.379005 \le C_{1b}$.

## Sources

- White 2022 and Optimization Problems 1b.

Stated but not proved: `MathlibExt.NumberTheory.ErdosMinimumOverlapConstantWanted.lowerBound_W2022_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosMinimumOverlapConstantWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html#lower-bound-w2022-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős minimum overlap problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/erd-s-minimum-overlap-problem)
