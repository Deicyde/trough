---
declaration: section
origin: cited
lean: Cslib.Complexity.Algebraic.MatrixArithmeticCircuit, Cslib.Complexity.Algebraic.matrixInput, Cslib.Complexity.Algebraic.IsMatrixMultiplication, Cslib.Complexity.Algebraic.outerMatrixCircuit, Cslib.Complexity.Algebraic.outerMatrixCircuit_correct, Cslib.Complexity.Algebraic.outerMatrixCircuit_size, Cslib.Complexity.Algebraic.IsMatrixMultiplication.output_is_node, Cslib.Complexity.Algebraic.IsMatrixMultiplication.output_cost_le
statement: formalized
proof: formalized
---

# Arithmetic circuits for matrix multiplication

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html).

## Matrix arithmetic circuit

For a type $F$ of scalars and $m, r, n \in \mathbb{N}$, a matrix
arithmetic circuit is an arithmetic circuit over $F$ whose inputs are indexed by the entries
$(i, k)$ of an $m \times r$ matrix together with the entries $(k, j)$ of an $r \times n$ matrix,
and whose outputs are indexed by the entries $(i, j)$ of an $m \times n$ matrix.

Formalized by `Cslib.Complexity.Algebraic.MatrixArithmeticCircuit`, an abbreviation declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#matrix-arithmetic-circuit).

## Matrix input assignment

For matrices $A \in F^{m \times r}$ and $B \in F^{r \times n}$,
the input assignment of $(A, B)$ is the function on the entry positions $(i, k)$ of an
$m \times r$ matrix together with the entry positions $(k, j)$ of an $r \times n$ matrix that
sends $(i, k)$ to $A_{ik}$ and $(k, j)$ to $B_{kj}$. It supplies the inputs of a matrix
arithmetic circuit.

Formalized by `Cslib.Complexity.Algebraic.matrixInput`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#matrix-input).

## Circuits that compute the matrix product

A circuit $c$ over a field $F$ whose inputs are
the entries of an $m \times r$ matrix and an $r \times n$ matrix computes matrix multiplication
when, for all matrices $A \in F^{m \times r}$ and $B \in F^{r \times n}$ and all $i < m$, $j < n$,
its output at $(i, j)$ on the entries of $A$ and $B$ equals $(AB)_{ij}$.

Correctness is required on actual values in $F$, not as an identity of formal polynomials.

Formalized by `Cslib.Complexity.Algebraic.IsMatrixMultiplication`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#is-matrix-multiplication).

## Outer-product matrix circuit

For a type $F$ of scalars and $m, n \in \mathbb{N}$, the
outer-product matrix circuit is the matrix arithmetic circuit for an $m \times 1$ matrix times a
$1 \times n$ matrix with exactly $mn$ gates: for $i < m$ and $j < n$, the gate for $(i, j)$
multiplies the input at entry $(i, 0)$ of the first matrix by the input at entry $(0, j)$ of
the second, and the output at $(i, j)$ is that gate.

Formalized by `Cslib.Complexity.Algebraic.outerMatrixCircuit`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#outer-matrix-circuit).

## The outer-product matrix circuit computes the matrix product

For every field $F$ and all
$m, n \in \mathbb{N}$, the outer-product matrix circuit over $F$ computes the product of an
$m \times 1$ matrix and a $1 \times n$ matrix.

Formalized by `Cslib.Complexity.Algebraic.outerMatrixCircuit_correct`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#outer-matrix-circuit-correct).

## Size of the outer-product matrix circuit

For every type $F$ of scalars and all
$m, n \in \mathbb{N}$, the outer-product matrix circuit over $F$ has exactly $mn$ gates.

Formalized by `Cslib.Complexity.Algebraic.outerMatrixCircuit_size`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#outer-matrix-circuit-size).

## Outputs of a matrix multiplication circuit are gates

Let $F$ be a field and let $c$ be
a circuit over $F$ that computes the product of an $m \times r$ matrix and an $r \times n$ matrix,
where $r \ge 1$. Then for all $i < m$ and $j < n$, the output of $c$ at $(i, j)$ is one of its
gates, not a constant or an input.

Formalized by `Cslib.Complexity.Algebraic.IsMatrixMultiplication.output_is_node`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#output-is-node).

## Lower bound for matrix multiplication circuits

Let $F$ be a field and let $c$ be a
circuit over $F$ that computes the product of an $m \times r$ matrix and an $r \times n$ matrix,
where $r \ge 1$. Then $c$ has at least $mn$ gates.

Distinct entries of the product require distinct gates, over every field.

Formalized by `Cslib.Complexity.Algebraic.IsMatrixMultiplication.output_cost_le`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/MatrixMultiplication.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#output-cost-le).

## Admissible rectangular circuit exponents

Let $F$ be a field and $k, w$ real numbers. The
exponent $w$ is admissible at aspect $k$ over $F$ when $k \ge 0$, $w \ge 0$, and for every
$\varepsilon > 0$ there are a real $C > 0$ and a natural number $N \ge 1$ such that for every
$n \ge N$ some arithmetic circuit over $F$ computes the product of an $n \times \lceil n^k \rceil$
matrix and an $\lceil n^k \rceil \times n$ matrix with at most $C n^{w + \varepsilon}$ gates.

The circuit may depend on $n$ and $\varepsilon$, and it must be correct on every pair of matrices
with entries in $F$.

Formalized by `Cslib.Complexity.Algebraic.HasRectangularCircuitExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#has-rectangular-circuit-exponent).

## Rectangular circuit exponent

For a field $F$ and a real $k$, the rectangular circuit
exponent of $F$ at aspect $k$ is the infimum in $[0, \infty]$ of the admissible rectangular circuit
exponents for $F$ at aspect $k$: the reals $w \ge 0$ such that $k \ge 0$ and, for every
$\varepsilon > 0$, there are $C > 0$ and $N \ge 1$ such that for every $n \ge N$ some arithmetic
circuit over $F$ of size at most $C n^{w + \varepsilon}$ computes the product of an
$n \times \lceil n^k \rceil$ matrix and a $\lceil n^k \rceil \times n$ matrix. The infimum of the
empty family is $\infty$; in particular the exponent is $\infty$ when $k < 0$.

Formalized by `Cslib.Complexity.Algebraic.rectangularCircuitExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#rectangular-circuit-exponent).

## Dual matrix multiplication exponent (arithmetic circuits)

For a field $F$, the dual
matrix multiplication exponent $\alpha(F) \in [0, \infty]$ of the arithmetic-circuit model is the
supremum of all real $k \ge 0$ at which the rectangular matrix multiplication exponent of the
arithmetic-circuit model over $F$ equals $2$.

Formalized by `Cslib.Complexity.Algebraic.dualCircuitExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#dual-circuit-exponent).

## Admissible exponents bound the rectangular circuit exponent

Let $F$ be a field and let
$k$ and $w$ be reals. If $w$ is an admissible rectangular circuit exponent for $F$ at aspect $k$,
then the rectangular circuit exponent of $F$ at aspect $k$ is at most $w$.

Formalized by `Cslib.Complexity.Algebraic.rectangularCircuitExponent_le_of_admissible`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#rectangular-circuit-exponent-le-of-admis).

## Lower bounds for the rectangular circuit exponent

Let $F$ be a field, $k$ a real number
and $W \in [0, \infty]$. If $W \le w$ for every real $w$ that is an admissible exponent at aspect
$k$ over $F$, then $W$ is at most the rectangular matrix multiplication exponent of the
arithmetic-circuit model over $F$ at aspect $k$.

Formalized by `Cslib.Complexity.Algebraic.le_rectangularCircuitExponent`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#le-rectangular-circuit-exponent).

## Aspects with circuit exponent two bound the dual exponent

Let $F$ be a field and $k \ge 0$
a real number. If the rectangular matrix multiplication exponent of the arithmetic-circuit model
over $F$ at aspect $k$ equals $2$, then $k \le \alpha(F)$, where $\alpha(F)$ is the dual matrix
multiplication exponent of the arithmetic-circuit model.

Formalized by `Cslib.Complexity.Algebraic.le_dualCircuitExponent`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#le-dual-circuit-exponent).

## Upper bounds for the dual circuit exponent

Let $F$ be a field and $K \in [0, \infty]$.
If $k \le K$ for every real $k \ge 0$ at which the rectangular matrix multiplication exponent of
the arithmetic-circuit model over $F$ equals $2$, then the dual matrix multiplication exponent
$\alpha(F)$ of the arithmetic-circuit model satisfies $\alpha(F) \le K$.

Formalized by `Cslib.Complexity.Algebraic.dualCircuitExponent_le`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#dual-circuit-exponent-le).

## Exponent two is admissible at aspect zero

For every field $F$, the exponent $2$ is an
admissible rectangular circuit exponent at aspect $0$ over $F$: for every $\varepsilon > 0$ there
are a real $C > 0$ and a natural number $N \ge 1$ such that for every $n \ge N$ some arithmetic
circuit over $F$ computes the product of an $n \times \lceil n^0 \rceil$ matrix and a
$\lceil n^0 \rceil \times n$ matrix, that is of an $n \times 1$ matrix and a $1 \times n$ matrix,
with at most $C n^{2 + \varepsilon}$ gates.

The outer-product circuit, with $n^2$ gates, is such a circuit.

Formalized by `Cslib.Complexity.Algebraic.hasRectangularCircuitExponent_zero_two`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#has-rectangular-circuit-exponent-zero-tw).

## The rounded inner dimension is positive

For every natural number $n \ge 1$ and every real
$k$, the rounded inner dimension $\lceil n^k \rceil$ is positive.

Formalized by `Cslib.Complexity.Algebraic.rectangularInnerDimension_pos`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#rectangular-inner-dimension-pos).

## Admissible rectangular circuit exponents are at least two

Let $F$ be a field and let $k$
and $w$ be reals. If $w$ is an admissible rectangular circuit exponent for $F$ at aspect $k$, then
$w \ge 2$.

A circuit computing the product of an $n \times \lceil n^k \rceil$ matrix and a
$\lceil n^k \rceil \times n$ matrix with $n \ge 1$ has a separate gate for each of the $n^2$ output
entries, so it has at least $n^2$ gates.

Formalized by `Cslib.Complexity.Algebraic.HasRectangularCircuitExponent.two_le`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#two-le).

## The rectangular circuit exponent is at least two

For every field $F$ and every real $k$,
the rectangular circuit exponent of $F$ at aspect $k$ is at least $2$ (it may be $\infty$).

Formalized by `Cslib.Complexity.Algebraic.two_le_rectangularCircuitExponent`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#two-le-rectangular-circuit-exponent).

## The rectangular circuit exponent at aspect zero is two

For every field $F$, the
rectangular circuit exponent of $F$ at aspect $0$ equals $2$.

The upper bound comes from the outer-product circuit, which multiplies an $n \times 1$ matrix by a
$1 \times n$ matrix with $n^2$ multiplications.

Formalized by `Cslib.Complexity.Algebraic.rectangularCircuitExponent_zero`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#rectangular-circuit-exponent-zero).

## Some aspect has rectangular circuit exponent two

For every field $F$, there is a real
$k \ge 0$ at which the rectangular matrix multiplication exponent of the arithmetic-circuit model
over $F$ equals $2$. Hence the set of such $k$, viewed in $[0, \infty]$, whose supremum is the dual
matrix multiplication exponent, is nonempty.

Formalized by `Cslib.Complexity.Algebraic.dualCircuitExponent_family_nonempty`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#dual-circuit-exponent-family-nonempty).

## Admissible circuit exponents are upward closed

Let $F$ be a field and $k, w, w'$ real
numbers with $w \le w'$. If $w$ is an admissible exponent at aspect $k$ over $F$, then so is
$w'$.

Formalized by `Cslib.Complexity.Algebraic.HasRectangularCircuitExponent.mono`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#mono).

## Exponents above the circuit exponent are admissible

Let $F$ be a field and $k, w$ real
numbers with $w > 0$. If the rectangular matrix multiplication exponent of the arithmetic-circuit
model over $F$ at aspect $k$ is less than $w$, then $w$ is an admissible exponent at aspect $k$
over $F$.

Formalized by `Cslib.Complexity.Algebraic.hasRectangularCircuitExponent_of_inf_lt`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#has-rectangular-circuit-exponent-of-inf).

## Upper bounds on the rectangular circuit exponent

Let $F$ be a field and let $k \ge 0$ and
$w \ge 0$ be reals. The rectangular circuit exponent of $F$ at aspect $k$ is at most $w$ if and
only if $w$ is an admissible rectangular circuit exponent for $F$ at aspect $k$: for every
$\varepsilon > 0$ there are $C > 0$ and $N \ge 1$ such that for every $n \ge N$ some arithmetic
circuit over $F$ of size at most $C n^{w + \varepsilon}$ computes the product of an
$n \times \lceil n^k \rceil$ matrix and a $\lceil n^k \rceil \times n$ matrix.

Formalized by `Cslib.Complexity.Algebraic.rectangularCircuitExponent_le_iff`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#rectangular-circuit-exponent-le-iff).

## A finite rectangular circuit exponent is attained

Let $F$ be a field and $k \ge 0$ a real
number. If the rectangular matrix multiplication exponent $\omega$ of the arithmetic-circuit model
over $F$ at aspect $k$ is finite, then $\omega$ is itself an admissible exponent at aspect $k$
over $F$.

Formalized by `Cslib.Complexity.Algebraic.rectangularCircuitExponent_endpoint`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#rectangular-circuit-exponent-endpoint).

## Square matrix multiplication circuit exponent

For a field $F$, the square matrix
multiplication circuit exponent of $F$ is the rectangular circuit exponent of $F$ at aspect $1$.
Since $\lceil n^1 \rceil = n$, it is the infimum in $[0, \infty]$ of the reals $w \ge 0$ such that
for every $\varepsilon > 0$ there are $C > 0$ and $N \ge 1$ such that for every $n \ge N$ some
arithmetic circuit over $F$ of size at most $C n^{w + \varepsilon}$ computes the product of two
$n \times n$ matrices, and it is $\infty$ when there is no such $w$.

Formalized by `Cslib.Complexity.Algebraic.squareMatrixMultiplicationCircuitExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#square-matrix-multiplication-circuit-exp).

## The square circuit exponent is the aspect-one rectangular exponent

For every field $F$,
the square matrix multiplication circuit exponent of $F$ equals the rectangular circuit exponent
of $F$ at aspect $1$.

Formalized by `Cslib.Complexity.Algebraic.squareMatrixMultiplicationCircuitExponent_def`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#square-matrix-multiplication-circuit-exp-2).

## The square circuit exponent is at least two

For every field $F$, the square matrix
multiplication circuit exponent of $F$ is at least $2$.

This trivial bound holds because a circuit computing the product of two $n \times n$ matrices has
a separate gate for each of the $n^2$ output entries.

Formalized by `Cslib.Complexity.Algebraic.two_le_squareMatrixMultiplicationCircuitExponent`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#two-le-square-matrix-multiplication-circ).

## Upper bounds on the square matrix multiplication circuit exponent

Let $F$ be a field with
square matrix multiplication circuit exponent $\omega(F) \in [0, \infty]$, and let $w \ge 0$ be
real. Then $\omega(F) \le w$ if and only if $F$ has rectangular circuit exponent $w$ at aspect
$1$: for every $\varepsilon > 0$ there are a real $C > 0$ and a natural number $N \ge 1$ such
that for every $n \ge N$ some arithmetic circuit over $F$ with at most $C n^{w + \varepsilon}$
gates computes the product of every pair of $n \times n$ matrices over $F$.

Formalized by `Cslib.Complexity.Algebraic.squareMatrixMultiplicationCircuitExponent_le_iff`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#square-matrix-multiplication-circuit-exp-3).

## The square matrix multiplication circuit exponent is attained

Let $F$ be a field whose
square matrix multiplication circuit exponent $\omega(F)$ is finite. Then $F$ has rectangular
circuit exponent $\omega(F)$ at aspect $1$: for every $\varepsilon > 0$ there are a real $C > 0$
and a natural number $N \ge 1$ such that for every $n \ge N$ some arithmetic circuit over $F$ with
at most $C n^{\omega(F) + \varepsilon}$ gates computes the product of every pair of $n \times n$
matrices over $F$.

Formalized by `Cslib.Complexity.Algebraic.squareMatrixMultiplicationCircuitExponent_endpoint`, a theorem declared in [CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/Algebraic/RectangularCircuitExponent.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html#square-matrix-multiplication-circuit-exp-4).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic circuits for matrix multiplication](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/algebraic-complexity/arithmetic-circuits-for-matrix-multiplication)
