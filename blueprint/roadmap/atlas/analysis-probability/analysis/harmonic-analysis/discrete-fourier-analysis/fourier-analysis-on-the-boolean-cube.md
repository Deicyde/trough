---
declaration: section
origin: cited
lean: BooleanCube.BoolCube, BooleanCube.cubeVal, BooleanCube.cubeChi, BooleanCube.boolFourierCoeff, BooleanCube.MultilinearDegreeLE, BooleanCube.cubeVal_true, BooleanCube.cubeVal_false, BooleanCube.cubeVal_mul_self
statement: formalized
proof: formalized
---

# Fourier analysis on the Boolean cube

44 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html).

## Boolean cube

For $n \in \mathbb{N}$, the Boolean cube of dimension $n$ is the set of
functions $x : \{0, \dots, n-1\} \to \{\mathrm{true}, \mathrm{false}\}$. It represents
$\{-1, 1\}^n$, with true standing for $1$ and false for $-1$.

Formalized by `BooleanCube.BoolCube`, an abbreviation declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#bool-cube).

## Sign of a Boolean coordinate

The sign of a Boolean value $b$ is the real number
$\sigma(b)$ given by $\sigma(\text{true}) = 1$ and $\sigma(\text{false}) = -1$.

Formalized by `BooleanCube.cubeVal`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-val).

## Fourier character on the Boolean cube

For a set $S$ of coordinates among $n$, the Fourier
character $\chi_S$ is the real-valued function on the Boolean cube in $n$ coordinates given by
$\chi_S(x) = \prod_{i \in S} \sigma(x_i)$, where $\sigma$ is the sign of a coordinate:
$\sigma(\text{true}) = 1$ and $\sigma(\text{false}) = -1$.

Formalized by `BooleanCube.cubeChi`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-chi).

## Fourier coefficient on the Boolean cube

For $n \in \mathbb{N}$, a function
$f : \{-1, 1\}^n \to \mathbb{R}$ and a set $S \subseteq \{0, \dots, n-1\}$, the normalized Fourier
coefficient of $f$ at $S$ is
$\hat f(S) = \frac{1}{|\{-1, 1\}^n|} \sum_{x \in \{-1, 1\}^n} f(x) \chi_S(x)$, where
$\chi_S(x) = \prod_{i \in S} x_i$. That is, $\hat f(S)$ is the uniform expectation of $f \chi_S$.

Formalized by `BooleanCube.boolFourierCoeff`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#bool-fourier-coeff).

## Fourier degree at most $d$

A real-valued function $f$ on the Boolean cube of dimension
$n$ has Fourier degree at most a natural number $d$ when its Fourier coefficient $\hat f(S)$
vanishes for every set $S$ of coordinates with $|S| > d$.

This is the degree of the multilinear polynomial representing the function on the cube.

Formalized by `BooleanCube.MultilinearDegreeLE`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-degree-le).

## Sign of true

The sign $\sigma(\text{true})$ of the Boolean value true equals $1$.

Formalized by `BooleanCube.cubeVal_true`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-val-true).

## Sign of false

The sign $\sigma(\text{false})$ of the Boolean value false equals $-1$.

Formalized by `BooleanCube.cubeVal_false`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-val-false).

## Coordinate signs square to one

For every Boolean value $b$, its sign $\sigma(b)$ satisfies
$\sigma(b) \cdot \sigma(b) = 1$.

Formalized by `BooleanCube.cubeVal_mul_self`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-val-mul-self).

## The empty Fourier character is constant one

For every $n$ and every point $x$ of the
Boolean cube in $n$ coordinates, the Fourier character $\chi_\emptyset$ of the empty set of
coordinates satisfies $\chi_\emptyset(x) = 1$.

Formalized by `BooleanCube.cubeChi_empty`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-chi-empty).

## Singleton Fourier characters are coordinate signs

For every $n$, every coordinate $i$ and
every point $x$ of the Boolean cube in $n$ coordinates, the Fourier character $\chi_{\{i\}}$ of
the singleton $\{i\}$ satisfies $\chi_{\{i\}}(x) = \sigma(x_i)$, where $\sigma$ is the sign of a
coordinate: $\sigma(\text{true}) = 1$ and $\sigma(\text{false}) = -1$.

Formalized by `BooleanCube.cubeChi_singleton`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-chi-singleton).

## Fourier characters square to one

For every $n$, every set $S$ of the $n$ coordinates and
every point $x$ of the Boolean cube in $n$ coordinates, the Fourier character $\chi_S$ satisfies
$\chi_S(x) \cdot \chi_S(x) = 1$.

Formalized by `BooleanCube.cubeChi_mul_self`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-chi-mul-self).

## The empty Fourier coefficient is the mean

For every $n \in \mathbb{N}$ and every function
$f : \{-1, 1\}^n \to \mathbb{R}$, the normalized Fourier coefficient of $f$ at the empty set is the
uniform mean of $f$: $\hat f(\emptyset) = \frac{1}{|\{-1, 1\}^n|} \sum_{x \in \{-1, 1\}^n} f(x)$.

Formalized by `BooleanCube.boolFourierCoeff_empty`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#bool-fourier-coeff-empty).

## Fourier coefficients of the zero function

For every $n \in \mathbb{N}$ and every
$S \subseteq \{0, \dots, n-1\}$, the normalized Fourier coefficient at $S$ of the identically zero
function on $\{-1, 1\}^n$ is $0$.

Formalized by `BooleanCube.boolFourierCoeff_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#bool-fourier-coeff-zero).

## A character's own Fourier coefficient

For every $n \in \mathbb{N}$ and every
$S \subseteq \{0, \dots, n-1\}$, the normalized Fourier coefficient at $S$ of the character
$\chi_S(x) = \prod_{i \in S} x_i$ on $\{-1, 1\}^n$ equals $1$, that is,
$\widehat{\chi_S}(S) = 1$.

Formalized by `BooleanCube.boolFourierCoeff_cubeChi_self`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#bool-fourier-coeff-cube-chi-self).

## Empty Fourier coefficient of a constant function

For every $n \in \mathbb{N}$ and every
real $c$, the normalized Fourier coefficient at the empty set of the constant function
$x \mapsto c$ on the Boolean cube $\{-1, 1\}^n$ equals $c$. This includes dimension $n = 0$.

Formalized by `BooleanCube.boolFourierCoeff_const_empty`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#bool-fourier-coeff-const-empty).

## The zero function satisfies every Fourier degree bound

For all natural numbers $n$ and
$d$, the zero function on the Boolean cube of dimension $n$ has Fourier degree at most $d$.

Formalized by `BooleanCube.multilinearDegreeLE_zero`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-degree-le-zero).

## Fourier degree bounds are monotone

Let $f$ be a real-valued function on the Boolean
cube of dimension $n$, and let $d \le e$ be natural numbers. If $f$ has Fourier degree at most
$d$, then $f$ has Fourier degree at most $e$.

Formalized by `BooleanCube.MultilinearDegreeLE.mono`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#mono).

## Fourier degree is at most the dimension

Let $f$ be a real-valued function on the
Boolean cube of dimension $n$, and let $d \ge n$ be a natural number. Then $f$ has Fourier
degree at most $d$.

Formalized by `BooleanCube.multilinearDegreeLE_of_dimension_le`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-degree-le-of-dimension-le).

## Lagrange basis polynomial of a cube point

Let $x$ be a point of the Boolean cube in $n$
coordinates, indexed by $i \in \{0, \dots, n-1\}$. Its cube basis polynomial is the real
polynomial $\prod_{i=0}^{n-1} \ell_i$ in the variables $X_0, \dots, X_{n-1}$, where $\ell_i = X_i$
if $x_i$ is true and $\ell_i = 1 - X_i$ if $x_i$ is false. Reading true as $1$ and false as $0$,
it is the Lagrange basis polynomial of $x$ on the grid $\{0,1\}^n$.

Formalized by `BooleanCube.cubeBasis`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#cube-basis).

## Multilinear extension

Let $f$ be a Boolean-valued function on the Boolean cube of
dimension $n$, and read each coordinate and each value as $1$ for true and $0$ for false. The real
multilinear extension of $f$ is the polynomial in $\mathbb{R}[X_0, \dots, X_{n-1}]$

$$\sum_{x \in \{0,1\}^n} f(x) \prod_{i < n} \bigl(x_i X_i + (1 - x_i)(1 - X_i)\bigr).$$

For each cube point $x$ the product is its Lagrange basis polynomial: it evaluates to $1$ at $x$
and to $0$ at every other point of $\{0,1\}^n$. Hence the extension agrees with $f$ on
$\{0,1\}^n$, and it is the unique polynomial of degree at most one in each variable that does.

Formalized by `BooleanCube.multilinearExtension`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-extension).

## Lagrange basis polynomials on the cube are point indicators

Let $x$ and $y$ be points
of the Boolean cube of dimension $n$, and identify $y$ with the point of
$\{0,1\}^n \subseteq \mathbb{R}^n$ whose $i$-th coordinate is $1$ when $y_i$ is true and $0$
when it is false. Then the cube basis polynomial of $x$ evaluated at $y$ equals $1$ if $x = y$
and $0$ otherwise.

Formalized by `BooleanCube.eval_cubeBasis`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#eval-cube-basis).

## The multilinear extension agrees with its function on the cube

Let $f$ be a Boolean
function on the Boolean cube of dimension $n$, and let $y$ be a point of the cube, identified
with the point of $\{0,1\}^n \subseteq \mathbb{R}^n$ whose $i$-th coordinate is $1$ when $y_i$
is true and $0$ when it is false. Then the real multilinear extension of $f$ evaluated at $y$
equals $1$ if $f(y)$ is true and $0$ if $f(y)$ is false.

Formalized by `BooleanCube.eval_multilinearExtension`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#eval-multilinear-extension).

## Multilinear extension of a constant function

For every natural number $n$ and every
Boolean value $b$, the real multilinear extension of the constant function $b$ on the Boolean
cube of dimension $n$ is the constant polynomial $1$ if $b$ is true and the constant
polynomial $0$ if $b$ is false.

Formalized by `BooleanCube.multilinearExtension_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-extension-const).

## Multilinear extension of a coordinate projection

For every coordinate $i$ of the
Boolean cube of dimension $n$, the real multilinear extension of the projection $x \mapsto x_i$
is the variable $X_i$.

Formalized by `BooleanCube.multilinearExtension_projection`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-extension-projection).

## Boolean degree

Let $f$ be a Boolean-valued function on the Boolean cube in $n$
coordinates, and read true as $1$ and false as $0$. The Boolean degree of $f$ is the total degree
of the multilinear extension of $f$: the real multilinear polynomial in $n$ variables that takes
the value $f(x)$ at every point $x \in \{0,1\}^n$.

Formalized by `BooleanCube.booleanDegree`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#boolean-degree).

## Constant functions have Boolean degree zero

For every $n \in \mathbb{N}$ and every Boolean
value $b$, the constant function $x \mapsto b$ on the Boolean cube of dimension $n$ has Boolean
degree $0$.

Formalized by `BooleanCube.booleanDegree_const`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#boolean-degree-const).

## Coordinate projections have Boolean degree one

For every $n \in \mathbb{N}$ and every
$i < n$, the coordinate projection $x \mapsto x_i$ on the Boolean cube of dimension $n$ has
Boolean degree $1$.

Formalized by `BooleanCube.booleanDegree_projection`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#boolean-degree-projection).

## All-true function

For $n \in \mathbb{N}$, the all-true function on the Boolean cube of
dimension $n$ is the Boolean AND of all coordinates: it sends $x = (x_0, \dots, x_{n-1})$ to true
exactly when $x_i$ is true for every $i < n$. In dimension $0$ it is constantly true.

Formalized by `BooleanCube.allTrueFunction`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#all-true-function).

## Multilinear extension of the AND function

For every natural number $n$, the real
multilinear extension of the AND function on the Boolean cube of dimension $n$ (true exactly
when every coordinate is true) is the monomial $\prod_{i=0}^{n-1} X_i$.

Formalized by `BooleanCube.multilinearExtension_allTrue`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-extension-all-true).

## The two-bit AND has Boolean degree two

The all-true function on the Boolean cube of
dimension $2$, $(x_0, x_1) \mapsto x_0 \wedge x_1$, has Boolean degree $2$; that is, its real
multilinear extension has total degree $2$.

Formalized by `BooleanCube.booleanDegree_allTrue_two`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#boolean-degree-all-true-two).

## Fourier degree is at most Boolean degree

Let $f$ be a Boolean function on the Boolean
cube of dimension $n$, and let $g$ be the real function with $g(x) = 1$ if $f(x)$ is true and
$g(x) = 0$ otherwise. Then $g$ has Fourier degree at most the Boolean degree of $f$: every
Fourier coefficient $\hat g(S)$ with $|S|$ greater than the total degree of the multilinear
extension of $f$ vanishes.

Formalized by `BooleanCube.multilinearDegreeLE_indicator`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#multilinear-degree-le-indicator).

## Fourier character on finite sets

For finite sets $S$ and $T$, the Fourier character of
$S$ at $T$ is the real number $\chi_S(T) = (-1)^{|S \cap T|}$.

This is the subset-indexed form of the Fourier character on the Boolean cube; after reindexing
the coordinates, the two agree.

Formalized by `BooleanCube.fourierChar`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#fourier-char).

## Fourier coefficient on the subsets of a finite set

Let $E$ be a finite subset of a type
$\iota$ and let $f$ be a function from finite subsets of $\iota$ to $\mathbb{R}$. For a finite
subset $S$ of $\iota$, the Fourier coefficient of $f$ at $S$ over $E$ is

$$\hat f(S) = \frac{1}{2^{|E|}} \sum_{U \subseteq E} f(U) \, (-1)^{|S \cap U|},$$

the uniform average over the subsets $U$ of $E$ of $f(U)$ times the Fourier character
$\chi_S(U) = (-1)^{|S \cap U|}$.

After reindexing, it agrees with the Fourier coefficient on the Boolean cube.

Formalized by `BooleanCube.fourierCoeff`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#fourier-coeff).

## Number of points of the Boolean cube

For every $n \in \mathbb{N}$, the Boolean cube of
dimension $n$ has exactly $2^n$ points.

Formalized by `BooleanCube.card_boolCube`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#card-bool-cube).

## Subsets of a finite set as indicator functions

For a finite set $E$, this is the
bijection from the subsets $T \subseteq E$ to the functions $b$ from $E$ to
$\{\mathrm{true}, \mathrm{false}\}$ given by $b(a) = \mathrm{false}$ if $a \in T$ and
$b(a) = \mathrm{true}$ if $a \notin T$. Its inverse sends $b$ to the set
$\{a \in E : b(a) = \mathrm{false}\}$.

Members of $T$ read false, matching the convention that identifies false with the sign $-1$
and true with the sign $+1$.

Formalized by `BooleanCube.powersetEquivIndicator`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#powerset-equiv-indicator).

## Subsets of a finite set as points of the Boolean cube

For a finite set $E$ with $n = |E|$
elements, fix a bijection $e$ from $E$ to $\{0, \dots, n-1\}$ (an enumeration of $E$, chosen
noncanonically). This is the bijection from the subsets $T \subseteq E$ to the Boolean cube of
dimension $n$ that sends $T$ to the point $x$ with $x_{e(a)} = \mathrm{false}$ if $a \in T$ and
$x_{e(a)} = \mathrm{true}$ if $a \notin T$, for every $a \in E$.

Formalized by `BooleanCube.powersetEquivBoolCube`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#powerset-equiv-bool-cube).

## Coordinates of an encoded subset

Let $E$ be a finite set with $m$ elements, listed in
the fixed order $e_0, \dots, e_{m-1}$ used to encode subsets of $E$ as points of the Boolean cube
of dimension $m$. For every subset $T \subseteq E$ and every coordinate $j < m$, the $j$-th
coordinate of the point encoding $T$ is true if $e_j \notin T$ and false if $e_j \in T$.

Formalized by `BooleanCube.powersetEquivBoolCube_apply`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#powerset-equiv-bool-cube-apply).

## Reindexing a subset as a set of coordinates

For finite sets $S \subseteq E$ with $n = |E|$,
let $e$ be the fixed bijection from $E$ to $\{0, \dots, n-1\}$ (the enumeration of $E$ used to
identify subsets of $E$ with points of the Boolean cube of dimension $n$). The reindexed set is
the image $e(S) = \{e(a) : a \in S\}$, a subset of $\{0, \dots, n-1\}$.

Formalized by `BooleanCube.reindexFinset`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#reindex-finset).

## Decoding a cube point as a subset

Let $E$ be a finite set with $m$ elements, listed in a
fixed order as $e_0, \dots, e_{m-1}$; this order identifies subsets of $E$ with points of the
Boolean cube of dimension $m$. A point $x$ of that cube decodes to the subset
$\{e_j : x_j = \mathrm{false}\}$ of $E$; this inverts the encoding of subsets of $E$ as cube
points.

Formalized by `BooleanCube.decodeBoolCube`, a definition declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#decode-bool-cube).

## Decoding inverts encoding

Let $E$ be a finite set with $m$ elements, listed in a fixed
order as $e_0, \dots, e_{m-1}$. Encode a subset $T \subseteq E$ as the point $x_T$ of the Boolean
cube of dimension $m$ whose $j$-th coordinate is false exactly when $e_j \in T$, and decode a
point $x$ as the subset $\{e_j : x_j = \mathrm{false}\}$. Then for every subset $T \subseteq E$,
decoding $x_T$ gives back $T$.

Formalized by `BooleanCube.decode_encode`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 495](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L495). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#decode-encode).

## Subset characters agree with cube characters

Let $E$ be a finite set with $m$ elements,
listed in a fixed order as $e_0, \dots, e_{m-1}$, and encode a subset $T \subseteq E$ as the point
$x_T$ of the Boolean cube of dimension $m$ whose $j$-th coordinate is false exactly when
$e_j \in T$. For all subsets $S, T \subseteq E$,

$$(-1)^{|S \cap T|} = \chi_{S'}(x_T),$$

where the left side is the Fourier character of $S$ at $T$, $S' = \{j : e_j \in S\}$ is $S$
reindexed as a set of coordinates, and $\chi_{S'}$ is the Fourier character on the cube.

Formalized by `BooleanCube.fourierChar_eq_cubeChi`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 525](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L525). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#fourier-char-eq-cube-chi).

## Subset Fourier coefficients agree with cube Fourier coefficients

Let $E$ be a finite
subset of a type $\iota$ with $m$ elements, listed in a fixed order as $e_0, \dots, e_{m-1}$, and
decode a point $x$ of the Boolean cube of dimension $m$ as the subset
$D(x) = \{e_j : x_j = \mathrm{false}\}$ of $E$. Let $f$ be a function from finite subsets of
$\iota$ to $\mathbb{R}$ and let $S \subseteq E$. Then the Fourier coefficient
$\hat f(S) = 2^{-m} \sum_{U \subseteq E} f(U) (-1)^{|S \cap U|}$ of $f$ at $S$ over $E$ equals
the Fourier coefficient on the cube of the function $x \mapsto f(D(x))$ at the set of
coordinates $S' = \{j : e_j \in S\}$.

Formalized by `BooleanCube.fourierCoeff_eq_boolFourierCoeff`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 566](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#fourier-coeff-eq-bool-fourier-coeff).

## Fourier inversion on the subsets of a finite set

Let $E$ be a finite subset of a type
$\iota$ and let $f$ be a function from finite subsets of $\iota$ to $\mathbb{R}$. For every
subset $T \subseteq E$,

$$f(T) = \sum_{S \subseteq E} \hat f(S) \, (-1)^{|S \cap T|},$$

where $\hat f(S) = 2^{-|E|} \sum_{U \subseteq E} f(U) (-1)^{|S \cap U|}$ is the Fourier
coefficient of $f$ at $S$ over $E$ and $(-1)^{|S \cap T|}$ is the Fourier character of $S$ at
$T$.

Formalized by `BooleanCube.fourier_inversion`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#fourier-inversion).

## Plancherel identity on the subsets of a finite set

Let $E$ be a finite subset of a type
$\iota$ and let $f$ be a function from finite subsets of $\iota$ to $\mathbb{R}$. Then

$$\frac{1}{2^{|E|}} \sum_{T \subseteq E} f(T)^2 = \sum_{S \subseteq E} \hat f(S)^2,$$

where $\hat f(S) = 2^{-|E|} \sum_{U \subseteq E} f(U) (-1)^{|S \cap U|}$ is the Fourier
coefficient of $f$ at $S$ over $E$: the mean square of $f$ over the subsets of $E$ equals the
sum of the squared Fourier coefficients.

Formalized by `BooleanCube.fourier_plancherel`, a theorem declared in [MathlibExt/Analysis/Fourier/BooleanCube.lean, line 849](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/BooleanCube.lean#L849). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html#fourier-plancherel).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fourier analysis on the Boolean cube](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/fourier-analysis-on-the-boolean-cube)
