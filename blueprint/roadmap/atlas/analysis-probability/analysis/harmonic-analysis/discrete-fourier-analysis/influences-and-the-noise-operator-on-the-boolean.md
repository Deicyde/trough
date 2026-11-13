---
declaration: section
origin: cited
lean: BooleanCube.flipCoord, BooleanCube.flipCoord_apply_self, BooleanCube.flipCoord_apply_of_ne, BooleanCube.flipCoord_flipCoord, BooleanCube.flipCoord_involutive, BooleanCube.flipCoord_ne_self, BooleanCube.cubeVal_not, BooleanCube.cubeVal_ne_zero
statement: formalized
proof: formalized
---

# Influences and the noise operator on the Boolean cube

55 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html).

## Coordinate flips

## Coordinate flip on the Boolean cube

For a point $x$ of the Boolean cube of dimension $n$
and a coordinate $i \in \{0, \dots, n-1\}$, the point $x^{\oplus i}$ is obtained from $x$ by
negating its $i$-th coordinate (exchanging true and false) and leaving every other coordinate
unchanged.

Formalized by `BooleanCube.flipCoord`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#flip-coord).

## A coordinate flip negates the flipped coordinate

For every point $x$ of the Boolean cube
of dimension $n$ and every coordinate $i \in \{0, \dots, n-1\}$, the $i$-th coordinate of
$x^{\oplus i}$, the point $x$ with its $i$-th coordinate flipped, is the negation $\lnot x_i$ of
$x_i$ (true and false exchanged).

Formalized by `BooleanCube.flipCoord_apply_self`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#flip-coord-apply-self).

## A coordinate flip fixes the other coordinates

For every point $x$ of the Boolean cube of
dimension $n$ and all coordinates $i, j \in \{0, \dots, n-1\}$ with $j \ne i$, the $j$-th
coordinate of $x^{\oplus i}$, the point $x$ with its $i$-th coordinate flipped, is $x_j$.

Formalized by `BooleanCube.flipCoord_apply_of_ne`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#flip-coord-apply-of-ne).

## Flipping a coordinate twice

For every point $x$ of the Boolean cube of dimension $n$ and
every coordinate $i \in \{0, \dots, n-1\}$, writing $x^{\oplus i}$ for $x$ with its $i$-th
coordinate flipped, we have $(x^{\oplus i})^{\oplus i} = x$.

Formalized by `BooleanCube.flipCoord_flipCoord`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#flip-coord-flip-coord).

## Flipping a coordinate is an involution

For every $n \in \mathbb{N}$ and every coordinate
$i \in \{0, \dots, n-1\}$, the map $x \mapsto x^{\oplus i}$ on the Boolean cube of dimension $n$,
which flips the $i$-th coordinate, is an involution: applying it twice gives the identity.

Formalized by `BooleanCube.flipCoord_involutive`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#flip-coord-involutive).

## A coordinate flip moves every point

For every point $x$ of the Boolean cube of dimension
$n$ and every coordinate $i \in \{0, \dots, n-1\}$, the point $x^{\oplus i}$ obtained from $x$ by
flipping its $i$-th coordinate is different from $x$.

Formalized by `BooleanCube.flipCoord_ne_self`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#flip-coord-ne-self).

## Sign of a negated Boolean value

For every Boolean value $b$, the sign of its negation
is the negative of its sign: $\sigma(\lnot b) = -\sigma(b)$, where $\sigma(\text{true}) = 1$
and $\sigma(\text{false}) = -1$.

Formalized by `BooleanCube.cubeVal_not`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#cube-val-not).

## Coordinate signs are nonzero

For every Boolean value $b$, its sign $\sigma(b)$ (equal
to $1$ for true and $-1$ for false) is nonzero.

Formalized by `BooleanCube.cubeVal_ne_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#cube-val-ne-zero).

## Coordinate signs have absolute value one

For every Boolean value $b$, its sign $\sigma(b)$,
which is $1$ for true and $-1$ for false, satisfies $|\sigma(b)| = 1$.

Formalized by `BooleanCube.abs_cubeVal`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#abs-cube-val).

## Flipping a coordinate in a Fourier character

Let $S \subseteq \{0, \dots, n-1\}$, let
$x$ be a point of the Boolean cube in $n$ coordinates, let $i < n$, and write $x^{\oplus i}$ for
$x$ with coordinate $i$ flipped. Then the Fourier character $\chi_S$ satisfies
$\chi_S(x^{\oplus i}) = -\chi_S(x)$ if $i \in S$, and $\chi_S(x^{\oplus i}) = \chi_S(x)$ if
$i \notin S$.

Formalized by `BooleanCube.cubeChi_flipCoord`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#cube-chi-flip-coord).

## Flipping a coordinate preserves sums over the cube

Let $M$ be an additive commutative
monoid, $n \in \mathbb{N}$, $f$ a function from the Boolean cube of dimension $n$ to $M$, and
$i \in \{0, \dots, n-1\}$. For a point $x$ of the cube write $x^{\oplus i}$ for the point $x$ with
its $i$-th coordinate flipped. Then $\sum_x f(x^{\oplus i}) = \sum_x f(x)$, both sums ranging over
all points $x$ of the cube.

Formalized by `BooleanCube.sum_comp_flipCoord`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#sum-comp-flip-coord).

## Averages are invariant under flipping a coordinate

Let $M$ be an additive commutative
monoid that is a module over the nonnegative rationals, let $f$ be a function from the Boolean
cube in $n$ coordinates to $M$, and let $i < n$. Writing $x^{\oplus i}$ for $x$ with coordinate
$i$ flipped, the uniform average of $f(x^{\oplus i})$ over all points $x$ of the cube equals the
uniform average of $f(x)$.

Formalized by `BooleanCube.expect_comp_flipCoord`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#expect-comp-flip-coord).

## Uniform average over the Boolean cube as a sum

For every $n \in \mathbb{N}$ and every
function $f : \{-1, 1\}^n \to \mathbb{R}$, the uniform average of $f$ over the Boolean cube
$\{-1, 1\}^n$ is $\mathbb{E}_x f(x) = \frac{1}{2^n} \sum_{x \in \{-1, 1\}^n} f(x)$.

Formalized by `BooleanCube.expect_eq_sum_div_two_pow`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#expect-eq-sum-div-two-pow).

## Fourier coefficients as averages

For every real-valued function $f$ on the Boolean cube
in $n$ coordinates and every set $S$ of the $n$ coordinates, the Fourier coefficient $\hat f(S)$
is the average of $f(x) \chi_S(x)$ over all points $x$ of the cube,
$\hat f(S) = \mathbb{E}_x [f(x) \chi_S(x)]$, where $\chi_S$ is the Fourier character of $S$.

Formalized by `BooleanCube.boolFourierCoeff_eq_expect`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-eq-expect).

## Fourier coefficients as sums over the cube

For every real-valued function $f$ on the
Boolean cube in $n$ coordinates and every set $S$ of the $n$ coordinates, the Fourier coefficient
of $f$ at $S$ is $\hat f(S) = \frac{1}{2^n} \sum_x f(x) \chi_S(x)$, where the sum runs over all
points $x$ of the cube and $\chi_S$ is the Fourier character of $S$.

Formalized by `BooleanCube.boolFourierCoeff_eq_sum_div_two_pow`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-eq-sum-div-two-pow).

## Average over the Boolean cube as the empty Fourier coefficient

For every $n \in \mathbb{N}$
and every function $f : \{-1, 1\}^n \to \mathbb{R}$, the uniform average $\mathbb{E}_x f(x)$ of $f$
over the Boolean cube $\{-1, 1\}^n$ equals the Fourier coefficient $\hat f(\emptyset)$ of $f$ at
the empty set.

Formalized by `BooleanCube.expect_eq_boolFourierCoeff_empty`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#expect-eq-bool-fourier-coeff-empty).

## Orthogonality of the Boolean cube characters

Let $n \in \mathbb{N}$, let $S$ and $T$ be
subsets of $\{0, \dots, n-1\}$, and let $\chi_S$ and $\chi_T$ be their Fourier characters. Then
$\sum_x \chi_S(x) \chi_T(x)$, the sum ranging over all points $x$ of the Boolean cube of dimension
$n$, equals $2^n$ if $S = T$ and $0$ otherwise.

Formalized by `BooleanCube.sum_cubeChi_mul_cubeChi_eq_ite`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#sum-cube-chi-mul-cube-chi-eq-ite).

## Sum of a Boolean cube character

For every $n \in \mathbb{N}$ and every subset $S$ of
$\{0, \dots, n-1\}$, the sum of the Fourier character $\chi_S$ over all points of the Boolean cube
of dimension $n$ equals $2^n$ if $S$ is empty and $0$ otherwise.

Formalized by `BooleanCube.sum_cubeChi_eq_ite`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#sum-cube-chi-eq-ite).

## Dual orthogonality of the Boolean cube characters

Let $n \in \mathbb{N}$ and let $x, y$ be
points of the Boolean cube of dimension $n$. For each subset $S$ of $\{0, \dots, n-1\}$ let
$\chi_S$ be the Fourier character of $S$. Then $\sum_S \chi_S(x) \chi_S(y)$, the sum ranging over
all subsets $S$ of $\{0, \dots, n-1\}$, equals $2^n$ if $x = y$ and $0$ otherwise.

Formalized by `BooleanCube.sum_cubeChi_apply_mul_cubeChi_apply_eq_ite`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#sum-cube-chi-apply-mul-cube-chi-apply-eq).

## Fourier inversion on the Boolean cube

Let $n \in \mathbb{N}$, let $f$ be a real-valued
function on the Boolean cube of dimension $n$, and let $x$ be a point of the cube. For each subset
$S$ of $\{0, \dots, n-1\}$ let $\hat f(S)$ be the Fourier coefficient of $f$ at $S$ and $\chi_S$
the Fourier character of $S$. Then $\sum_S \hat f(S) \chi_S(x) = f(x)$, the sum ranging over all
subsets $S$ of $\{0, \dots, n-1\}$.

Formalized by `BooleanCube.sum_boolFourierCoeff_mul_cubeChi`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#sum-bool-fourier-coeff-mul-cube-chi).

## Plancherel's identity on the Boolean cube

For every $n \in \mathbb{N}$ and all functions
$f, g : \{-1, 1\}^n \to \mathbb{R}$, the uniform average of $f g$ over the Boolean cube
$\{-1, 1\}^n$ is the sum, over all sets $S \subseteq \{0, \dots, n-1\}$, of the products of the
Fourier coefficients of $f$ and $g$ at $S$:
$\mathbb{E}_x f(x) g(x) = \sum_S \hat f(S) \hat g(S)$.

Formalized by `BooleanCube.expect_mul_eq_sum_boolFourierCoeff_mul`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#expect-mul-eq-sum-bool-fourier-coeff-mul).

## Parseval's identity on the Boolean cube

For every $n \in \mathbb{N}$ and every function
$f : \{-1, 1\}^n \to \mathbb{R}$, the uniform average of $f^2$ over the Boolean cube $\{-1, 1\}^n$
is the sum, over all sets $S \subseteq \{0, \dots, n-1\}$, of the squares of the Fourier
coefficients of $f$ at $S$: $\mathbb{E}_x f(x)^2 = \sum_S \hat f(S)^2$.

Formalized by `BooleanCube.expect_sq_eq_sum_boolFourierCoeff_sq`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#expect-sq-eq-sum-bool-fourier-coeff-sq).

## Fourier coefficients determine the function

If two real-valued functions $f$ and $g$ on
the Boolean cube in $n$ coordinates have the same Fourier coefficient $\hat f(S) = \hat g(S)$ at
every set $S$ of the $n$ coordinates, then $f = g$.

Formalized by `BooleanCube.boolFourierCoeff_injective`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-injective).

## Additivity of Fourier coefficients

For all real-valued functions $f$ and $g$ on the
Boolean cube in $n$ coordinates and every set $S$ of the $n$ coordinates, the Fourier coefficient
of $f + g$ at $S$ is the sum of the Fourier coefficients of $f$ and $g$ at $S$:
$\widehat{f + g}(S) = \hat f(S) + \hat g(S)$.

Formalized by `BooleanCube.boolFourierCoeff_add`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-add).

## Fourier coefficients of a difference

For real-valued functions $f$ and $g$ on the
Boolean cube $\{-1, 1\}^n$ and every set $S \subseteq \{0, \dots, n-1\}$, the Fourier coefficient
of $f - g$ at $S$ is $\widehat{f - g}(S) = \hat f(S) - \hat g(S)$.

Formalized by `BooleanCube.boolFourierCoeff_sub`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-sub).

## Homogeneity of Fourier coefficients

For every real $c$, every real-valued function $f$
on the Boolean cube in $n$ coordinates and every set $S$ of the $n$ coordinates, the Fourier
coefficient of $c f$ at $S$ is $c$ times the Fourier coefficient of $f$ at $S$:
$\widehat{c f}(S) = c \hat f(S)$.

Formalized by `BooleanCube.boolFourierCoeff_const_mul`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-const-mul).

## Fourier coefficients of a constant function

For every real $c$ and every set $S$ of the
$n$ coordinates, the Fourier coefficient at $S$ of the constant function $x \mapsto c$ on the
Boolean cube in $n$ coordinates is $c$ if $S = \emptyset$ and $0$ otherwise.

Formalized by `BooleanCube.boolFourierCoeff_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-const).

## Fourier coefficients of a character

For all sets $S$ and $T$ of the $n$ coordinates, the
Fourier coefficient at $S$ of the Fourier character $\chi_T$ on the Boolean cube in $n$
coordinates, $\chi_T(x) = \prod_{i \in T} \sigma(x_i)$ with $\sigma(\text{true}) = 1$ and
$\sigma(\text{false}) = -1$, is $1$ if $T = S$ and $0$ otherwise.

Formalized by `BooleanCube.boolFourierCoeff_cubeChi`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-cube-chi).

## Uniqueness of the Fourier expansion

For real numbers $a_T$ indexed by the sets
$T \subseteq \{0, \dots, n-1\}$, let $g(x) = \sum_T a_T \chi_T(x)$ on the Boolean cube
$\{-1, 1\}^n$, where $\chi_T$ is the Fourier character of $T$. Then for every set
$S \subseteq \{0, \dots, n-1\}$ the Fourier coefficient of $g$ at $S$ is $\hat g(S) = a_S$.

Formalized by `BooleanCube.boolFourierCoeff_sum_mul_cubeChi`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-sum-mul-cube-chi).

## Flipping a coordinate negates the Fourier coefficients of the sets containing it

Let $f$
be a real-valued function on the Boolean cube in $n$ coordinates, let $i$ be a coordinate, and
let $g(x) = f(x^{\oplus i})$, where $x^{\oplus i}$ is the point $x$ with its $i$-th coordinate
flipped. Write $\hat f(S)$ and $\hat g(S)$ for the Fourier coefficients of $f$ and $g$ at a set
$S$ of the $n$ coordinates. Then for every such $S$, $\hat g(S) = -\hat f(S)$ if $i \in S$ and
$\hat g(S) = \hat f(S)$ if $i \notin S$.

Formalized by `BooleanCube.boolFourierCoeff_comp_flipCoord`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-comp-flip-coord).

## Influence of a coordinate

For a real-valued function $f$ on the Boolean cube
$\{-1, 1\}^n$ and a coordinate $i \in \{0, \dots, n-1\}$, the influence of $i$ on $f$ is
$\mathrm{Inf}_i[f] = \mathbb{E}_x\big[\big((f(x) - f(x^{\oplus i})) / 2\big)^2\big]$, where the
expectation is over $x$ uniform on the cube and $x^{\oplus i}$ is $x$ with its $i$-th coordinate
flipped.

Formalized by `BooleanCube.boolInfluence`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-influence).

## Total influence on the Boolean cube

For a function $f$ from the Boolean cube
$\{-1, 1\}^n$ to $\mathbb{R}$, the total influence of $f$ is the sum of the influences of its $n$
coordinates, $\mathrm{I}[f] = \sum_{i=0}^{n-1} \mathrm{Inf}_i[f]$, where
$\mathrm{Inf}_i[f] = \mathbb{E}_x \left[\left(\frac{f(x) - f(x^{\oplus i})}{2}\right)^2\right]$,
$x^{\oplus i}$ is $x$ with its $i$-th coordinate flipped and $\mathbb{E}_x$ is the uniform average
over the points $x$ of the cube.

Formalized by `BooleanCube.boolTotalInfluence`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-total-influence).

## Variance on the Boolean cube

For a function $f : \{-1, 1\}^n \to \mathbb{R}$ on the
Boolean cube, its variance under the uniform distribution is
$\mathrm{Var}[f] = \mathbb{E}_x\big[(f(x) - \mathbb{E}_y[f(y)])^2\big]$, where $\mathbb{E}_x$
denotes the uniform average over the $2^n$ points $x$ of the cube.

Formalized by `BooleanCube.boolVariance`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-variance).

## Influences are nonnegative

For every real-valued function $f$ on the Boolean cube
$\{-1, 1\}^n$ and every coordinate $i \in \{0, \dots, n-1\}$, the influence $\mathrm{Inf}_i[f]$ of
coordinate $i$ on $f$ satisfies $\mathrm{Inf}_i[f] \ge 0$.

Formalized by `BooleanCube.boolInfluence_nonneg`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-influence-nonneg).

## Total influence is nonnegative

For every function $f$ from the Boolean cube
$\{-1, 1\}^n$ to $\mathbb{R}$, the total influence of $f$ is nonnegative.

Formalized by `BooleanCube.boolTotalInfluence_nonneg`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-total-influence-nonneg).

## Variance on the Boolean cube is nonnegative

For every function
$f : \{-1, 1\}^n \to \mathbb{R}$ on the Boolean cube, the variance of $f$ under the uniform
distribution is at least $0$.

Formalized by `BooleanCube.boolVariance_nonneg`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-variance-nonneg).

## Constant functions have zero influence

For every real number $c$ and every coordinate
$i \in \{0, \dots, n-1\}$, the influence of coordinate $i$ on the constant function with value $c$
on the Boolean cube $\{-1, 1\}^n$ is $0$.

Formalized by `BooleanCube.boolInfluence_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-influence-const).

## Constant functions have zero total influence

For every real number $c$, the constant
function with value $c$ on the Boolean cube $\{-1, 1\}^n$ has total influence $0$.

Formalized by `BooleanCube.boolTotalInfluence_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-total-influence-const).

## Constant functions have zero variance

For every real number $c$, the constant function
with value $c$ on the Boolean cube $\{-1, 1\}^n$ has variance $0$ under the uniform
distribution.

Formalized by `BooleanCube.boolVariance_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-variance-const).

## Influence of a Boolean function as a flip probability

Let $f$ be a real-valued function
on the Boolean cube $\{-1, 1\}^n$ that takes only the values $1$ and $-1$, and let
$i \in \{0, \dots, n-1\}$. Then the influence of coordinate $i$ on $f$ equals the probability,
for $x$ uniform on the cube, that $f(x^{\oplus i}) \ne f(x)$, where $x^{\oplus i}$ is $x$ with
its $i$-th coordinate flipped.

Formalized by `BooleanCube.boolInfluence_eq_expect_ite_ne`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-influence-eq-expect-ite-ne).

## Fourier formula for influence

For every real-valued function $f$ on the Boolean cube
$\{-1, 1\}^n$ and every coordinate $i \in \{0, \dots, n-1\}$, the influence of coordinate $i$ on
$f$ is $\mathrm{Inf}_i[f] = \sum_{S \ni i} \hat f(S)^2$, where $\hat f(S)$ is the Fourier
coefficient of $f$ at $S$ and the sum runs over the sets $S \subseteq \{0, \dots, n-1\}$ that
contain $i$.

Formalized by `BooleanCube.boolInfluence_eq_sum_sq`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 360](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L360). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-influence-eq-sum-sq).

## Variance in terms of Fourier coefficients

For every function
$f : \{-1, 1\}^n \to \mathbb{R}$ on the Boolean cube, the variance of $f$ under the uniform
distribution equals $\sum_{S \neq \emptyset} \hat f(S)^2$, where the sum runs over the nonempty
sets $S \subseteq \{0, \dots, n-1\}$ and $\hat f(S)$ is the Fourier coefficient of $f$ at $S$.

Formalized by `BooleanCube.boolVariance_eq_sum_sq`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-variance-eq-sum-sq).

## Variance as mean square minus squared mean

For every function
$f : \{-1, 1\}^n \to \mathbb{R}$ on the Boolean cube, the variance of $f$ under the uniform
distribution equals $\mathbb{E}_x[f(x)^2] - (\mathbb{E}_x[f(x)])^2$, where $\mathbb{E}_x$
denotes the uniform average over the $2^n$ points $x$ of the cube.

Formalized by `BooleanCube.boolVariance_eq_expect_sq_sub_sq`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-variance-eq-expect-sq-sub-sq).

## Total influence in Fourier form

For every function $f$ from the Boolean cube
$\{-1, 1\}^n$ to $\mathbb{R}$, the total influence of $f$ is

$$\mathrm{I}[f] = \sum_{S \subseteq \{0, \dots, n-1\}} |S| \, \hat f(S)^2,$$

where $\hat f(S)$ is the Fourier coefficient of $f$ at $S$.

Formalized by `BooleanCube.boolTotalInfluence_eq_sum_card_mul_sq`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 392](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L392). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-total-influence-eq-sum-card-mul-sq).

## Poincaré inequality on the Boolean cube

For every function
$f : \{-1, 1\}^n \to \mathbb{R}$ on the Boolean cube, the variance of $f$ under the uniform
distribution is at most the total influence of $f$: $\mathrm{Var}[f] \le I[f]$.

Formalized by `BooleanCube.boolVariance_le_boolTotalInfluence`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-variance-le-bool-total-influence).

## Noise operator on the Boolean cube

For a real number $\rho$ and a function $f$ from the
Boolean cube $\{-1, 1\}^n$ to $\mathbb{R}$, the noise operator $T_\rho$ sends $f$ to the function

$$T_\rho f(x) = \sum_y \Bigl(\prod_{i < n} \frac{1 + \rho \sigma(x_i) \sigma(y_i)}{2}\Bigr) f(y),$$

where $y$ runs over all points of the cube and $\sigma$ is the sign of a coordinate:
$\sigma(\mathrm{true}) = 1$ and $\sigma(\mathrm{false}) = -1$.

For $-1 \le \rho \le 1$, $T_\rho f(x)$ is the expectation of $f(y)$ when each coordinate of $y$
independently equals the corresponding coordinate of $x$ with probability $(1 + \rho) / 2$; the
formula is used for every real $\rho$.

Formalized by `BooleanCube.boolNoiseOp`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op).

## Fourier expansion of the noise operator

For every real number $\rho$, every function $f$
from the Boolean cube $\{-1, 1\}^n$ to $\mathbb{R}$ and every point $x$ of the cube,

$$T_\rho f(x) = \sum_{S \subseteq \{0, \dots, n-1\}} \rho^{|S|} \, \hat f(S) \, \chi_S(x),$$

where $T_\rho$ is the noise operator, $\hat f(S)$ is the Fourier coefficient of $f$ at $S$,
$\chi_S$ is the Fourier character of $S$, and $\rho^0 = 1$ also when $\rho = 0$.

Formalized by `BooleanCube.boolNoiseOp_eq_sum`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-eq-sum).

## Fourier coefficients of the noise operator

For every real $\rho$, every real-valued
function $f$ on the Boolean cube in $n$ coordinates and every set $S$ of the $n$ coordinates, the
Fourier coefficient at $S$ of $T_\rho f$, the noise operator with parameter $\rho$ applied to $f$,
is $\widehat{T_\rho f}(S) = \rho^{|S|} \hat f(S)$.

Formalized by `BooleanCube.boolFourierCoeff_boolNoiseOp`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-fourier-coeff-bool-noise-op).

## The noise operator $T_1$ is the identity

For every function $f$ from the Boolean cube
$\{-1, 1\}^n$ to $\mathbb{R}$, the noise operator with $\rho = 1$ fixes $f$: $T_1 f = f$.

Formalized by `BooleanCube.boolNoiseOp_one`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-one).

## The noise operator $T_0$ takes the mean

For every function $f$ from the Boolean cube
$\{-1, 1\}^n$ to $\mathbb{R}$, the noise operator with $\rho = 0$ sends $f$ to the constant
function whose value is the mean $\mathbb{E}_x f(x) = 2^{-n} \sum_x f(x)$ of $f$ under the
uniform distribution.

Formalized by `BooleanCube.boolNoiseOp_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 451](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L451). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-zero).

## Semigroup property of the noise operator

For all real numbers $\rho$ and $\sigma$ and every
real-valued function $f$ on the Boolean cube $\{-1, 1\}^n$, applying the noise operator $T_\sigma$
and then $T_\rho$ to $f$ gives $T_{\rho\sigma} f$: $T_\rho(T_\sigma f) = T_{\rho\sigma} f$.

Formalized by `BooleanCube.boolNoiseOp_boolNoiseOp`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-bool-noise-op).

## The noise operator preserves the mean

For every real $\rho$ and every function
$f : \{-1, 1\}^n \to \mathbb{R}$ on the Boolean cube, the uniform average over the cube of
$T_\rho f$, the image of $f$ under the noise operator with parameter $\rho$, equals the uniform
average of $f$.

Formalized by `BooleanCube.expect_boolNoiseOp`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#expect-bool-noise-op).

## Characters are eigenfunctions of the noise operator

For every real number $\rho$ and every
set $S \subseteq \{0, \dots, n-1\}$, the noise operator $T_\rho$ maps the Fourier character $\chi_S$
on the Boolean cube $\{-1, 1\}^n$ to the function $x \mapsto \rho^{|S|} \chi_S(x)$, so $\chi_S$ is
an eigenfunction of $T_\rho$ with eigenvalue $\rho^{|S|}$.

Formalized by `BooleanCube.boolNoiseOp_cubeChi`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-cube-chi).

## The noise operator fixes constants

For every real number $\rho$ and every real number $c$,
the noise operator $T_\rho$ maps the constant function with value $c$ on the Boolean cube
$\{-1, 1\}^n$ to itself.

Formalized by `BooleanCube.boolNoiseOp_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-const).

## Positivity of the noise operator

For every real number $\rho$ with $|\rho| \le 1$, the
noise operator $T_\rho$ on the Boolean cube maps nonnegative functions to nonnegative functions:
if $f$ is a real function on the cube with $f(y) \ge 0$ for every point $y$, then
$T_\rho f(x) \ge 0$ for every point $x$ of the cube.

Formalized by `BooleanCube.boolNoiseOp_nonneg`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean, line 487](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCubeInfluence.lean#L487). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html#bool-noise-op-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Influences and the noise operator on the Boolean cube](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/influences-and-the-noise-operator-on-the-boolean)
