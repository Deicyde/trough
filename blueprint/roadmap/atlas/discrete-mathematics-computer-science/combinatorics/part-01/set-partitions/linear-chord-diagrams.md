---
declaration: section
origin: cited
lean: MetaMathlibExt.mean_short_chords_in_linear_k_chord_diagrams, MetaMathlibExt.noncrossingLinearKChordDiagram_shortChords_asymptoticallyNormal, MetaMathlibExt.IsLinearChordDiagram, MetaMathlibExt.IsShortChordVertex, MetaMathlibExt.IsBubble, MetaMathlibExt.bubbleCount, MetaMathlibExt.bubbleCount_one_one, MetaMathlibExt.bubbleCount_two_one
statement: formalized
---

# Linear chord diagrams

15 results, 8 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html).

## Mean number of short chords in linear $k$-chord diagrams

Let $k \ge 1$ and $n \ge 0$ be
integers. A linear $k$-chord diagram of length $kn$ is a set of $n$ subsets of
$\{0, 1, \dots, kn - 1\}$, each with $k$ elements, whose union is $\{0, 1, \dots, kn - 1\}$; it
is therefore a partition of this set into $n$ blocks of size $k$, its chords. A chord is short
when it consists of $k$ consecutive integers $\{i, i + 1, \dots, i + k - 1\}$. The number of
short chords, averaged over all linear $k$-chord diagrams of length $kn$, equals

$$
\frac{n\,(kn - k + 1)}{\binom{kn}{k}},
$$

where for $n = 0$ the denominator $\binom{0}{k}$ is $0$ and the quotient is read as $0$, which
is the mean over the single empty diagram.

For $n \ge 1$ there are $kn - k + 1$ sets of $k$ consecutive integers in $\{0, \dots, kn - 1\}$.
This is the mean theorem, distinct from the same paper's asymptotic Poisson distribution of
short chords.

## Sources

- Donovan Young, "Linear k-Chord Diagrams," Journal of Integer Sequences 23 (2020), Article 20.9.1, Theorem, lines 208–214, https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.tex

Formalized by `MetaMathlibExt.mean_short_chords_in_linear_k_chord_diagrams`, a theorem declared in [MathlibExt/Probability/MeanShortChords.lean, line 459](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/MeanShortChords.lean#L459). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#mean-short-chords-in-linear-k-chord-diag).

## Asymptotic normality of short chords in non-crossing chord diagrams

The short-chord count in a uniformly chosen non-crossing linear `k`-chord diagram is
asymptotically normal with the stated mean and variance.

## Sources

- Donovan Young, "Linear k-Chord Diagrams", Journal of Integer Sequences 23 (2020), Article 20.9.1, Theorem lines 1014-1024 (§6.1), <https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.tex>.

Stated but not proved: `MetaMathlibExt.noncrossingLinearKChordDiagram_shortChords_asymptoticallyNormal` is written with `theorem_wanted` in [WantedExt/Analysis/Asymptotics/NoncrossingChordDiagramNormalLimitWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Asymptotics/NoncrossingChordDiagramNormalLimitWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#asymptotic-normality-of-short-chords-in).

## Linear chord diagrams

A linear chord diagram on the $2n$ vertices $0, \dots, 2n-1$, laid
out on a line, is encoded by a map $\sigma$ from $\{0, \dots, 2n-1\}$ to itself that is a
fixed-point-free involution: $\sigma(i) \ne i$ and $\sigma(\sigma(i)) = i$ for every vertex $i$.
Vertex $i$ is joined by a chord to $\sigma(i)$.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Section 1 (linear chord diagrams on `2n` vertices).

Formalized by `MetaMathlibExt.IsLinearChordDiagram`, a definition declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#is-linear-chord-diagram).

## Endpoints of short chords

Let $\sigma$ be a map from $\{0, \dots, 2n-1\}$ to itself (for a
linear chord diagram, vertex $i$ is joined by a chord to $\sigma(i)$). A vertex $i$ is an
endpoint of a short chord of $\sigma$ when $\sigma(i) = i - 1$ or $\sigma(i) = i + 1$, that is,
when $i$ is joined to an adjacent vertex.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Abstract and Section 1 (short chords).

Formalized by `MetaMathlibExt.IsShortChordVertex`, a definition declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#is-short-chord-vertex).

## Bubbles

Let $\sigma$ be a map from $\{0, \dots, 2n-1\}$ to itself (for a linear chord
diagram, vertex $i$ is joined by a chord to $\sigma(i)$). For natural numbers $a$ and $p$, the
vertices $a, a+1, \dots, a+p-1$ form a bubble of size $p$ in $\sigma$ when $p \ge 1$,
$a + p \le 2n$, none of these vertices is an endpoint of a short chord of $\sigma$, the vertex
$a - 1$ is an endpoint of a short chord unless $a = 0$, and the vertex $a + p$ is an endpoint
of a short chord unless $a + p = 2n$.

So a bubble is a maximal run of consecutive vertices containing no endpoint of a short chord.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Section 1 (definition of bubbles and their size).

Formalized by `MetaMathlibExt.IsBubble`, a definition declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#is-bubble).

## Bubble counts

For natural numbers $n$ and $p$, $B_{n,p}$ is the total number of bubbles of
size $p$ in all linear chord diagrams on $2n$ vertices: the sum, over all linear chord diagrams
$\sigma$ on the vertices $0, \dots, 2n-1$, of the number of vertices $a$ such that the vertices
$a, a+1, \dots, a+p-1$ form a bubble of size $p$ in $\sigma$. In particular $B_{n,0} = 0$.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Section 1 (definition of `B_{n,p}`, Table 1).

Formalized by `MetaMathlibExt.bubbleCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#bubble-count).

## No bubbles of size one on two vertices

$B_{1,1} = 0$: the linear chord diagrams on $2$
vertices have no bubble of size $1$. The only such diagram is a single short chord.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Table 1 (row `n = 1`).

Formalized by `MetaMathlibExt.bubbleCount_one_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#bubble-count-one-one).

## Bubbles of size one on four vertices

$B_{2,1} = 2$: the linear chord diagrams on $4$
vertices have $2$ bubbles of size $1$ in total.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Table 1 (row `n = 2`).

Formalized by `MetaMathlibExt.bubbleCount_two_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#bubble-count-two-one).

## Bubbles of size four on four vertices

$B_{2,4} = 1$: the linear chord diagrams on $4$
vertices have exactly one bubble of size $4$ in total. It consists of all four vertices of the
crossing diagram (chords $\{0, 2\}$ and $\{1, 3\}$), which has no short chord.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Table 1 (row `n = 2`).

Formalized by `MetaMathlibExt.bubbleCount_two_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#bubble-count-two-four).

## Total number of bubbles in linear chord diagrams

For every natural number $n \ge 2$,
let $B_{n,p}$ be the total number of bubbles of size $p$ over all linear chord diagrams on $2n$
vertices. Then

$$\sum_{p=1}^{2n} B_{n,p} = \frac{(2n-2)!\,(4n-5)}{2^{n-1}\,(n-1)!}.$$

The hypothesis $n \ge 2$ is needed: for $n = 1$ the left side is $0$ and the right side is $-1$.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Lemma 3 (`jis-2024-24.4.2-lem-3`).

Stated but not proved: `MetaMathlibExt.sum_bubbleCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#sum-bubble-count).

## First moment of bubble sizes in linear chord diagrams

For every natural number
$n \ge 2$, let $B_{n,p}$ be the total number of bubbles of size $p$ over all linear chord diagrams
on $2n$ vertices. Then

$$\sum_{p=1}^{2n} p\,B_{n,p} = \frac{(2n-1)!}{2^{n-2}\,(n-2)!}.$$

The hypothesis $n \ge 2$ is added because the right side involves $(n-2)!$.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Lemma 4 (`jis-2024-24.4.2-lem-4`).

Stated but not proved: `MetaMathlibExt.sum_mul_bubbleCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#sum-mul-bubble-count).

## Mean bubble size

Let $B_{n,p}$ be the total number of bubbles of size $p$ in all linear
chord diagrams on $2n$ vertices. For every integer $n \ge 2$, the mean bubble size satisfies

$$\frac{\sum_{p=1}^{2n} p\,B_{n,p}}{\sum_{p=1}^{2n} B_{n,p}} = \frac{2(2n-1)(n-1)}{4n-5}.$$

The hypothesis $n \ge 2$ is added: for $n = 1$ there are no bubbles.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Theorem 5 (`jis-2024-24.4.2-thm-5`).

Stated but not proved: `MetaMathlibExt.mean_bubble_size` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#mean-bubble-size).

## Formal contour-integral formula for bubble counts

Let $G(s, w, y)$ be the power series
in $\mathbb{Q}[[s, w, y]]$ given by

$$G = \left(1 - \frac{y^2}{1 - sy + y^2}\right)^{-2} \left(\frac{1}{1 - wsy + w^2y^2} - 1\right),$$

and write $[s^a w^p y^m]\,G$ for its coefficient of $s^a w^p y^m$. For integers $n, p \ge 0$ let
$B_{n,p}$ be the total number of bubbles of size $p$ in all linear chord diagrams on $2n$
vertices. Then for all integers $n, p \ge 0$ (including $n = 0$)

$$\sum_{k \ge 0} \frac{(2k)!}{2^k\, k!}\, [s^{2k} w^p y^{2n}]\,G = B_{n,p} \quad\text{and}\quad
\sum_{k \ge 0} \frac{(2k)!}{2^k\, k!}\, [s^{2k} w^p y^{2n+1}]\,G = 0.$$

Each sum has only finitely many nonzero terms, since every power of $s$ in $G$ comes with at
least the same power of $y$. This is the termwise reading of the paper's formal contour
integral: integrating $x^{-1} e^{x^2/2} G(t/x, w, y)$ over $x$ and then replacing $t^{2k}$ by
$\int_0^\infty t^{2k} e^{-t}\,dt = (2k)!$ turns $s^{2k}$ into $(2k)!/(2^k k!)$. The literal
integrals diverge.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Theorem 1 (`jis-2024-24.4.2-thm-1`).

Stated but not proved: `MetaMathlibExt.bubbleCount_formal_contour_integral` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#bubble-count-formal-contour-integral).

## Closed form of the bubble generating function

In $\mathbb{Q}[[t, w, y]]$ let
$D = 1 - w(1 - wy)$ and let $I(t, w, y)$ be the power series

$$I = \frac{(1-w)^2 (1-wy)^2}{(1+w^2y)\,D^2}
\exp\!\left(\frac{y}{2}\left(\frac{tw}{1+w^2y}\right)^2\right) +
\left(\frac{(2 - w(y+2)(1 + y(1 - w(2-wy))))\,wy}{D^2} + \frac{(1-wy)\,t^2 w y^3}{D}\right)
\exp\!\left(\frac{t^2 y}{2}\right),$$

and write $[t^m w^p y^n]\,I$ for its coefficient of $t^m w^p y^n$. For integers $n, p \ge 0$ let
$B_{n,p}$ be the total number of bubbles of size $p$ in all linear chord diagrams on $2n$
vertices. Then for all integers $n \ge 1$ and $p \ge 0$

$$\sum_{m \ge 0} m!\, [t^m w^p y^n]\,I = B_{n,p}.$$

The sum has only finitely many nonzero terms, since $t$ occurs in $I$ only as $t^2$ times a
factor $y$. Replacing $t^m$ by $m! = \int_0^\infty t^m e^{-t}\,dt$ reads the formula as a formal
Laplace transform in $t$, as in the paper's proofs of Lemmas 3 and 4, so that the left side is
the coefficient of $y^n w^p$ of the paper's $B(y, w) = \sum_{n,p} B_{n,p} y^n w^p$. The case
$n = 0$ is excluded: the printed formula has constant term $1$ while $B_{0,0} = 0$ (the paper's
residue computation in its contour variable $x$ omits the residue $-1$ at $x = 0$; Theorem 1
gives constant term $0$).

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Corollary 2 (`jis-2024-24.4.2-cor-2`).

Stated but not proved: `MetaMathlibExt.bubbleCount_formal_laplace_closed_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#bubble-count-formal-laplace-closed-form).

## Limiting density of bubble sizes in linear chord diagrams

Let $B_{n,p}$ be the total
number of bubbles of size $p$ over all linear chord diagrams on $2n$ vertices. Let $x$ be a real
number with $0 < x \le 2$, and let $(p_n)_{n \ge 0}$ be natural numbers with $p_0 = 0$,
$p_n \le 2n - 2$ for every $n \ge 1$, and $p_n / (n - 1) \to x$ as $n \to \infty$. Then

$$\frac{(n-1)\,B_{n,p_n}}{\sum_{p=1}^{2n-2} B_{n,p}} \to \frac{e\,(6-x)}{2\,(4e-2)}\,e^{-x/2}$$

as $n \to \infty$. The sum in the denominator leaves out the bubble sizes $2n - 1$ and $2n$; a
bubble of size $2n$ is a whole diagram without short chords.

The paper writes $B_{n,x(n-1)}$; since $x(n-1)$ need not be an integer, the limit is read along
integer sizes $p_n$ with $p_n/(n-1) \to x$, the scaling the paper's proof uses.

## Sources

- Donovan Young, *Counting Bubbles in Linear Chord Diagrams*, Journal of Integer Sequences 27 (2024), Article 24.4.2, Theorem 6 (`jis-2024-24.4.2-thm-6`).

Stated but not proved: `MetaMathlibExt.tendsto_bubbleCount_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearChordBubblesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html#tendsto-bubble-count-density).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear chord diagrams](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/linear-chord-diagrams/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/set-partitions/linear-chord-diagrams)
