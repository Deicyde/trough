---
declaration: section
origin: cited
lean: MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.PlanarPoint, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.cyclicNext, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.tourLength, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.shortestTourLength, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.normalizedTourLength, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.IsIIDWithLaw, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.IIDRealization, MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.HasBHHLimit
statement: formalized
---

# Beardwood–Halton–Hammersley theorem

33 results, 26 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html).

## Points of the Euclidean plane

A planar point is a point of the Euclidean plane
$\mathbb{R}^2$: a pair $(x, y)$ of real numbers, with the Euclidean norm
$\lVert (x, y) \rVert = \sqrt{x^2 + y^2}$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.PlanarPoint`, an abbreviation declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#planar-point).

## Cyclic successor

For a natural number $n$ and an index $i$ with $0 \le i < n$, the cyclic
successor of $i$ is $(i + 1) \bmod n$; in particular the successor of $n - 1$ is $0$. For $n = 0$
there are no indices.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.cyclicNext`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#cyclic-next).

## Length of a closed tour

For points $x_0, \dots, x_{n-1}$ in the Euclidean plane and a
permutation $\sigma$ of $\{0, \dots, n-1\}$, the tour length is
$\sum_{i=0}^{n-1} \lVert x_{\sigma(i)} - x_{\sigma(i+1 \bmod n)} \rVert$, the length of the closed
tour that visits $x_{\sigma(0)}, \dots, x_{\sigma(n-1)}$ in this order and returns to its start.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.tourLength`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#tour-length).

## Shortest tour length

For points $x_0, \dots, x_{n-1}$ in the Euclidean plane, $L_n$ is
the minimum, over all permutations $\sigma$ of $\{0, \dots, n-1\}$, of the length of the closed
tour that visits $x_{\sigma(0)}, \dots, x_{\sigma(n-1)}$ in this order and returns to its start.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.shortestTourLength`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#shortest-tour-length).

## Normalized tour length

Let $\Omega$ be a set and let
$X_0, X_1, X_2, \dots \colon \Omega \to \mathbb{R}^2$ be functions. For an outcome
$\omega \in \Omega$ and $n \ge 1$, the normalized tour length is $L_n(\omega)/\sqrt{n}$, where
$L_n(\omega)$ is the length of a shortest closed tour through $X_0(\omega), \dots, X_{n-1}(\omega)$.
For $n = 0$ it is defined to be $0$.

The value at $n = 0$ does not affect limits as $n \to \infty$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.normalizedTourLength`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#normalized-tour-length).

## I.i.d. points with a given law

Let $\Omega$ be a measurable space with a measure
$\mathbb{P}$, let $X_0, X_1, X_2, \dots \colon \Omega \to \mathbb{R}^2$ be functions and let $\nu$
be a measure on the Borel sets of the plane. The $X_i$ are i.i.d. with law $\nu$ when
$\mathbb{P}$ and $\nu$ are probability measures, every $X_i$ is measurable, the $X_i$ are mutually
independent under $\mathbb{P}$, and the distribution of each $X_i$ under $\mathbb{P}$ is $\nu$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.IsIIDWithLaw`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#is-iidwith-law).

## I.i.d. realization

For a measure $\nu$ on the plane, an i.i.d. realization with law $\nu$
consists of a measurable space $\Omega$ with a measure $\mathbb{P}$, together with a sequence
$X_0, X_1, X_2, \dots \colon \Omega \to \mathbb{R}^2$ of points that is i.i.d. with common law
$\nu$ under $\mathbb{P}$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.IIDRealization`, a structure declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#iidrealization).

## Almost-sure BHH limit

Let $\Omega$ be a measurable space with a measure $\mu$, let
$X_0, X_1, X_2, \dots \colon \Omega \to \mathbb{R}^2$ be functions into the plane, and let $\beta$
be a real number. The sequence has BHH limit $\beta$ when, for $\mu$-almost every
$\omega \in \Omega$, the normalized tour length $L_n(\omega)/\sqrt{n}$ tends to $\beta$ as
$n \to \infty$, where $L_n(\omega)$ is the length of a shortest closed tour through
$X_0(\omega), \dots, X_{n-1}(\omega)$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.HasBHHLimit`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#has-bhhlimit).

## BHH constant of a law

For a measure $\nu$ on the plane and a real number $\beta$, $\beta$
is a BHH constant for $\nu$ when an i.i.d. realization with law $\nu$ exists and every i.i.d.
realization with law $\nu$ has almost-sure BHH limit $\beta$: almost surely,
$L_n/\sqrt{n} \to \beta$, where $L_n$ is the length of a shortest closed tour through the first
$n$ points.

Requiring a realization to exist keeps the condition from holding vacuously.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.IsBHHConstantFor`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#is-bhhconstant-for).

## BHH limit values of a sampling law

For a measure $\mu$ on the plane, the BHH limit values
of $\mu$ form the set of real numbers $\beta$ that are BHH limits for $\mu$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhhLimitValues`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh-limit-values).

## Membership in the set of BHH limit values

For a measure $\nu$ on the plane and a real
number $\beta$, $\beta$ belongs to the set of BHH limit values of $\nu$ if and only if $\beta$ is a
BHH constant for $\nu$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.mem_bhhLimitValues_iff`, a theorem declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#mem-bhh-limit-values-iff).

## Unique BHH constant of a law

A measure $\nu$ on the plane has a unique BHH constant when
there is exactly one real number $\beta$ that is a BHH constant for $\nu$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.HasUniqueBHHConstantFor`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#has-unique-bhhconstant-for).

## BHH constant of a sampling law

For a measure $\mu$ on the plane, the BHH constant of $\mu$
is the infimum of the set of real numbers $\beta$ that are BHH limits for $\mu$. The infimum of a
set of reals that is empty or not bounded below is taken to be $0$.

No existence theorem is assumed: the definition does not presuppose that a BHH limit exists.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhhConstantFor`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh-constant-for).

## The BHH constant equals the unique BHH limit

Let $\mu$ be a measure on the plane and
$\beta$ a real number. If, for every real $\gamma$, $\gamma$ is a BHH limit for $\mu$ if and only
if $\gamma = \beta$, then the BHH constant of $\mu$ (the infimum of its BHH limits) equals $\beta$.

The hypothesis excludes the case with no BHH limit, where the infimum is $0$ by convention.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhhConstantFor_eq_of_unique_characterization`, a theorem declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh-constant-for-eq-of-unique-characteri).

## Unit square

The closed unit square $[0,1]^2$: the set of points of the Euclidean plane
both of whose coordinates lie in the interval $[0,1]$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.unitSquare`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#unit-square).

## Uniform law on the unit square

Lebesgue measure on the Euclidean plane restricted to the
closed unit square $[0,1]^2$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.unitSquareUniformLaw`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#unit-square-uniform-law).

## Beardwood–Halton–Hammersley constant

The Beardwood–Halton–Hammersley constant is the
BHH constant of the uniform law on the closed unit square $[0,1]^2$ (Lebesgue measure restricted
to $[0,1]^2$): the infimum of the set of real numbers $\beta$ such that i.i.d. samples with this
law exist and, for every such sample $X_1, X_2, \dots$, the length of the shortest closed tour
through $X_1, \dots, X_n$ divided by $\sqrt{n}$ tends to $\beta$ almost surely. The infimum of a
set of reals that is empty or not bounded below is taken to be $0$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.beardwoodHaltonHammersleyConstant`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#beardwood-halton-hammersley-constant).

## The notation $\beta_2$

We write $\beta_2$ for the real-valued Beardwood–Halton–Hammersley
constant of the unit square.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.β₂`, an abbreviation declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#untitled).

## Notation C₁₂ for the BHH constant

The constant $C_{12}$ is defined to be the
Beardwood–Halton–Hammersley constant $\beta_2$ for uniform points in the unit square; $C_{12}$ is
the name the source uses for it.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.C₁₂`, an abbreviation declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#c).

## Statement of the Beardwood–Halton–Hammersley theorem

The proposition that the
Beardwood–Halton–Hammersley constant $\beta_2$ is a BHH constant for the uniform law on the closed
unit square $[0,1]^2$, and that every real number $\beta$ that is a BHH constant for this law equals
$\beta_2$. Here a real number $\beta$ is a BHH constant for a law $\mu$ on the plane when a
sequence $X_0, X_1, \dots$ of independent random points with common law $\mu$ exists on some
probability space, and for every such sequence, almost surely $L_n / \sqrt{n} \to \beta$ as
$n \to \infty$, where $L_n$ is the length of the shortest closed tour through $X_0, \dots, X_{n-1}$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.unitSquareBHHTheorem`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#unit-square-bhhtheorem).

## Statement of the Beardwood–Halton–Hammersley upper bound

This is the proposition that the
Beardwood–Halton–Hammersley constant $\beta_2$ for uniform points in the unit square satisfies
$\beta_2 \le 0.92117$, the upper bound reported by Beardwood, Halton and Hammersley (1959).

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhh1959UpperBound`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh1959-upper-bound).

## Statement of Steinerberger's upper bound

The proposition that the
Beardwood–Halton–Hammersley constant $\beta_2$ satisfies
$\beta_2 \le 0.92117 - \frac{9}{16} \cdot 10^{-6}$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.steinerberger2015ImprovedUpperBound`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#steinerberger2015-improved-upper-bound).

## Statement of the Yu–Carlsson upper bound

This is the proposition that the real-valued
Beardwood–Halton–Hammersley constant $\beta_2$ of the unit square satisfies $\beta_2 < 0.90304$.

## Sources

- [YC2023], strict computer-aided upper bound.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.yuCarlsson2023StrictUpperBound`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#yu-carlsson2023-strict-upper-bound).

## Statement of the Beardwood–Halton–Hammersley lower bound

This is the proposition that the
Beardwood–Halton–Hammersley constant $\beta_2$ for uniform points in the unit square satisfies
$\beta_2 \ge 5/8 = 0.625$, the lower bound reported by Beardwood, Halton and Hammersley (1959).

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhh1959LowerBound`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh1959-lower-bound).

## Statement of the corrected Steinerberger lower bound

The proposition that the
Beardwood–Halton–Hammersley constant $\beta_2$ satisfies
$\frac{5}{8} + \frac{19}{10368} \le \beta_2$.

The bound is the exact rational $\frac{5}{8} + \frac{19}{10368}$, not a decimal approximation of it.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.steinerberger2015CorrectedSymbolicLowerBound`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#steinerberger2015-corrected-symbolic-low).

## Statement of the Gaudio–Jaillet lower bound

The proposition that the
Beardwood–Halton–Hammersley constant $\beta_2$ of the unit square is at least $0.6277$, that is,
$0.6277 \le \beta_2$.

Formalized by `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.gaudioJaillet2020LowerBound`, a definition declared in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#gaudio-jaillet2020-lower-bound).

## Beardwood–Halton–Hammersley theorem

Let $\beta_2$ be the Beardwood–Halton–Hammersley
constant and, for points $X_0, X_1, \dots$ of the plane, let $L_n$ be the length of the shortest
closed tour through $X_0, \dots, X_{n-1}$. Then a sequence of independent random points
$X_0, X_1, \dots$, each uniformly distributed on the closed unit square $[0,1]^2$, exists on some
probability space; for every such sequence, almost surely $L_n / \sqrt{n} \to \beta_2$ as
$n \to \infty$; and $\beta_2$ is the only real number $\beta$ such that every such sequence almost
surely satisfies $L_n / \sqrt{n} \to \beta$.

## Sources

- Beardwood, Halton and Hammersley (1959), quoted in Steinerberger (2015).

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.unitSquareBHHTheorem_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#unit-square-bhhtheorem-holds).

## Beardwood–Halton–Hammersley upper bound

The Beardwood–Halton–Hammersley constant $\beta_2$
for uniform points in the unit square satisfies $\beta_2 \le 0.92117$.

## Sources

- Beardwood, Halton and Hammersley (1959), catalogue upper-bound row.

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhh1959UpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh1959-upper-bound-holds).

## Steinerberger's upper bound for the BHH constant

The Beardwood–Halton–Hammersley constant
$\beta_2$ satisfies $\beta_2 \le 0.92117 - \frac{9}{16} \cdot 10^{-6}$.

## Sources

- Steinerberger, New Bounds for the Traveling Salesman Constant (2015).

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.steinerberger2015ImprovedUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#steinerberger2015-improved-upper-bound-h).

## Yu–Carlsson upper bound on the BHH constant

The real-valued Beardwood–Halton–Hammersley
constant $\beta_2$ of the unit square satisfies $\beta_2 < 0.90304$.

## Sources

- Yu and Carlsson (2023), strict upper-bound row in the catalogue.

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.yuCarlsson2023StrictUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#yu-carlsson2023-strict-upper-bound-holds).

## Beardwood–Halton–Hammersley lower bound

The Beardwood–Halton–Hammersley constant $\beta_2$
for uniform points in the unit square satisfies $\beta_2 \ge 5/8 = 0.625$.

## Sources

- Beardwood, Halton and Hammersley (1959), catalogue lower-bound row.

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.bhh1959LowerBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#bhh1959-lower-bound-holds).

## Gaudio–Jaillet corrected lower bound for the BHH constant

The Beardwood–Halton–Hammersley
constant $\beta_2$ satisfies $\frac{5}{8} + \frac{19}{10368} \le \beta_2$.

## Sources

- Gaudio and Jaillet (2020), correction of Steinerberger's lower coefficient.

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.steinerberger2015CorrectedSymbolicLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#steinerberger2015-corrected-symbolic-low-2).

## Gaudio–Jaillet lower bound for the BHH constant

The Beardwood–Halton–Hammersley
constant $\beta_2$ of the unit square satisfies $0.6277 \le \beta_2$.

## Sources

- Gaudio and Jaillet, An improved lower bound for the Traveling Salesman constant.

Stated but not proved: `MathlibExt.Probability.BeardwoodHaltonHammersleyConstantWanted.gaudioJaillet2020LowerBound_holds` is written with `theorem_wanted` in [WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/BeardwoodHaltonHammersleyConstantWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html#gaudio-jaillet2020-lower-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Beardwood–Halton–Hammersley theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/high-dimensional-probability/beardwood-halton-hammersley-theorem)
