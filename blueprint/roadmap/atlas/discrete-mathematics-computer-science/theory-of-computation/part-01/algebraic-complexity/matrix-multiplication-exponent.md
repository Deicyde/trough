---
declaration: section
origin: cited
lean: Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.RankOneTrilinearTerm, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.RankOneTrilinearTerm.eval, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasTrilinearRankAtMost, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasTrilinearRankAtMost.mono, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasTrilinearRankAtMost_card, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearRank, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearRank_spec, Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearRank_le
statement: formalized
---

# Matrix multiplication exponent

85 results, 52 proved and 33 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html).

## Rank-one trilinear term

For a type $F$ with multiplication and types $A$, $B$, $C$, a
rank-one trilinear term is a triple of functions $u : A \to F$, $v : B \to F$, $w : C \to F$ (its
left, middle and right factors), representing one rank-one summand $u \otimes v \otimes w$ of a
trilinear tensor decomposition.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.RankOneTrilinearTerm`, a structure declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rank-one-trilinear-term).

## Value of a rank-one trilinear term

For a rank-one trilinear term over a semigroup $F$
with factors $u : A \to F$, $v : B \to F$ and $w : C \to F$, its value at $a \in A$, $b \in B$,
$c \in C$ is the product $u(a)\,v(b)\,w(c)$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.RankOneTrilinearTerm.eval`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#eval).

## Trilinear rank at most $r$

Let $F$ be a semiring and $A$, $B$, $C$ types. An array
$T : A \to B \to C \to F$ has trilinear rank at most $r$ when there are $s \le r$ and functions
$u_i : A \to F$, $v_i : B \to F$, $w_i : C \to F$ for $i = 1, \dots, s$ such that
$T(a, b, c) = \sum_{i=1}^{s} u_i(a)\,v_i(b)\,w_i(c)$ for all $a \in A$, $b \in B$, $c \in C$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasTrilinearRankAtMost`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-trilinear-rank-at-most).

## Monotonicity of trilinear rank bounds

Let $F$ be a semiring and $T : A \to B \to C \to F$
an array. If $T$ has trilinear rank at most $r$ and $r \le s$, then $T$ has trilinear rank at
most $s$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasTrilinearRankAtMost.mono`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#mono).

## Trivial upper bound on trilinear rank

Let $F$ be a semiring and $A$, $B$, $C$ finite
types. Every array $T : A \to B \to C \to F$ has trilinear rank at most
$|A| \cdot |B| \cdot |C|$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasTrilinearRankAtMost_card`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-trilinear-rank-at-most-card).

## Trilinear rank

Let $F$ be a semiring and let $A$, $B$, $C$ be finite types. The trilinear
rank of a coefficient array $T : A \to B \to C \to F$ is the least $r \in \mathbb{N}$ for which
there are $s \le r$ functions $u_i : A \to F$, $v_i : B \to F$, $w_i : C \to F$ with
$T(a, b, c) = \sum_{i=1}^{s} u_i(a)\,v_i(b)\,w_i(c)$ for all $a \in A$, $b \in B$, $c \in C$.

Such an $r$ exists because $|A| \cdot |B| \cdot |C|$ coordinate terms always suffice.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearRank`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#trilinear-rank).

## The trilinear rank is attained

Let $F$ be a semiring, let $A$, $B$, $C$ be finite types,
let $T : A \to B \to C \to F$ be a coefficient array, and let $R(T)$ be its trilinear rank. Then
there are $s \le R(T)$ functions $u_i : A \to F$, $v_i : B \to F$, $w_i : C \to F$ with
$T(a, b, c) = \sum_{i=1}^{s} u_i(a)\,v_i(b)\,w_i(c)$ for all $a \in A$, $b \in B$, $c \in C$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearRank_spec`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#trilinear-rank-spec).

## Decompositions bound the trilinear rank

Let $F$ be a semiring, let $A$, $B$, $C$ be finite
types, and let $T : A \to B \to C \to F$ be a coefficient array. If there are $s \le r$ functions
$u_i : A \to F$, $v_i : B \to F$, $w_i : C \to F$ with
$T(a, b, c) = \sum_{i=1}^{s} u_i(a)\,v_i(b)\,w_i(c)$ for all $a \in A$, $b \in B$, $c \in C$,
then the trilinear rank of $T$ is at most $r$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearRank_le`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#trilinear-rank-le).

## Rank bounds via the trilinear rank

Let $F$ be a semiring and $A$, $B$, $C$ finite types.
For every array $T : A \to B \to C \to F$ and every natural number $r$, $T$ has trilinear rank at
most $r$ if and only if the trilinear rank of $T$ (the least length of a decomposition of $T$
into rank-one arrays) is at most $r$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasTrilinearRankAtMost_iff`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-trilinear-rank-at-most-iff).

## Trilinear tensors

For a field $F$ and types $A$, $B$, $C$, write $F^X$ for the
$F$-vector space of functions $X \to F$. The space of trilinear tensors over $F$ indexed by
$A$, $B$, $C$ is the tensor product $(F^A \otimes_F F^B) \otimes_F F^C$ over $F$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.TrilinearTensor`, an abbreviation declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#trilinear-tensor).

## Coefficient array of a trilinear tensor

Let $F$ be a field, let $A$ and $C$ be finite
types, let $B$ be a type, and write $F^X$ for the space of functions $X \to F$. The coefficient
map is the $F$-linear isomorphism from $(F^A \otimes_F F^B) \otimes_F F^C$ to the space
of arrays $A \to B \to C \to F$ that sends each pure tensor $(u \otimes v) \otimes w$ to the
array $(a, b, c) \mapsto u(a)\,v(b)\,w(c)$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearTensorCoefficients`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#trilinear-tensor-coefficients).

## Coefficients of a pure tensor

Let $F$ be a field, let $A$ and $C$ be finite types and
let $B$ be a type. For $u : A \to F$, $v : B \to F$, $w : C \to F$ and $a \in A$, $b \in B$,
$c \in C$, the coefficient array of the pure tensor $(u \otimes v) \otimes w$ takes the value
$u(a)\,v(b)\,w(c)$ at $(a, b, c)$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.trilinearTensorCoefficients_tmul`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#trilinear-tensor-coefficients-tmul).

## The pure tensor of a rank-one term

Let $F$ be a field and $A$, $B$, $C$ types. A
rank-one trilinear term with factors $u : A \to F$, $v : B \to F$ and $w : C \to F$ determines
the pure tensor $(u \otimes v) \otimes w$ in the trilinear tensor space over $F$ indexed by
$A$, $B$, $C$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.RankOneTrilinearTerm.tensor`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#tensor).

## Tensor rank at most $r$

Let $F$ be a field and $A$, $B$, $C$ types. An element $T$ of
$(F^A \otimes_F F^B) \otimes_F F^C$ has tensor rank at most $r$ when there are $s \le r$ and
functions $u_i : A \to F$, $v_i : B \to F$, $w_i : C \to F$ for $i = 1, \dots, s$ such that
$T = \sum_{i=1}^{s} (u_i \otimes v_i) \otimes w_i$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasTensorRankAtMost`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-tensor-rank-at-most).

## Tensor rank bounds agree with coefficient rank bounds

Let $F$ be a field and $A$, $B$,
$C$ types with $A$ and $C$ finite, and let $T$ be an element of $(F^A \otimes_F F^B) \otimes_F F^C$.
For every natural number $r$, $T$ has tensor rank at most $r$ if and only if its coefficient
array $A \to B \to C \to F$, obtained by the canonical linear equivalence, has trilinear rank at
most $r$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasTensorRankAtMost_iff`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-tensor-rank-at-most-iff).

## Tensor rank

Let $F$ be a field and let $A$, $B$, $C$ be finite types. The tensor rank of
a trilinear tensor $T$ over $F$ indexed by $A$, $B$, $C$ is the least $r \in \mathbb{N}$ such
that $T$ is a sum of at most $r$ pure tensors $(u \otimes v) \otimes w$ with $u : A \to F$,
$v : B \to F$ and $w : C \to F$.

It is defined as the trilinear rank of the coefficient array of $T$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.tensorRank`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#tensor-rank).

## The tensor rank is attained

Let $F$ be a field, let $A$, $B$, $C$ be finite types, let
$T$ be a trilinear tensor over $F$ indexed by $A$, $B$, $C$, and let $R(T)$ be its tensor rank.
Then $T$ is a sum of at most $R(T)$ pure tensors $(u \otimes v) \otimes w$ with $u : A \to F$,
$v : B \to F$ and $w : C \to F$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.tensorRank_spec`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#tensor-rank-spec).

## Decompositions bound the tensor rank

Let $F$ be a field, let $A$, $B$, $C$ be finite
types, and let $T$ be a trilinear tensor over $F$ indexed by $A$, $B$, $C$. If $T$ is a sum of at
most $r$ pure tensors $(u \otimes v) \otimes w$ with $u : A \to F$, $v : B \to F$ and
$w : C \to F$, then the tensor rank of $T$ is at most $r$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.tensorRank_le`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#tensor-rank-le).

## Matrix coordinates

The index set of an $m \times n$ matrix: pairs $(i, j)$ of a row index
$i \in \{0, \dots, m-1\}$ and a column index $j \in \{0, \dots, n-1\}$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.MatrixCoordinate`, an abbreviation declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-coordinate).

## Matrix multiplication tensor

For a field $F$ and natural numbers $m$, $n$, $p$, the matrix
multiplication tensor is the array over $F$ indexed by triples $((i, j), (j', k), (k', i'))$ of an
$m \times n$, an $n \times p$ and a $p \times m$ matrix coordinate, whose entry is $1$ if $j = j'$,
$k = k'$ and $i' = i$, and $0$ otherwise.

These are the coefficients of $\sum_{i, j, k} e_{(i,j)} \otimes e_{(j,k)} \otimes e_{(k,i)}$, the
tensor of multiplying an $m \times n$ matrix by an $n \times p$ matrix.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationTensor`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-tensor).

## Square matrix multiplication tensor

For a field $F$ and a natural number $n$, the square
matrix multiplication tensor over $F$ is the matrix multiplication tensor for multiplying an
$n \times n$ matrix by an $n \times n$ matrix. Its value at a triple of matrix coordinates
$((i, j), (j', k), (k', i'))$ is $1$ when $j = j'$, $k = k'$ and $i = i'$, and $0$ otherwise.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.squareMatrixMultiplicationTensor`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#square-matrix-multiplication-tensor).

## Matrix multiplication structure tensor

For a field $F$ and natural numbers $m, n, p$, the
structure tensor of multiplying an $m \times n$ matrix by an $n \times p$ matrix over $F$ is
the element $\sum_{i < m} \sum_{j < n} \sum_{k < p} e_{(i,j)} \otimes e_{(j,k)} \otimes e_{(k,i)}$
of the trilinear tensor space
$F^{[m] \times [n]} \otimes F^{[n] \times [p]} \otimes F^{[p] \times [m]}$, where
$[m] = \{0, \dots, m - 1\}$ and $e_x$ is the standard basis vector at the matrix coordinate $x$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationStructureTensor`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-structure-tensor).

## Coefficients of the matrix multiplication structure tensor

Let $F$ be a field, let
$m, n, p$ be natural numbers, and write $e_x$ for the standard basis vector with index $x$. The
coordinates of the structure tensor
$\sum_{i < m,\, j < n,\, k < p} e_{(i,j)} \otimes e_{(j,k)} \otimes e_{(k,i)}$ in
$F^{m \times n} \otimes F^{n \times p} \otimes F^{p \times m}$ are the matrix multiplication
coefficients: the coordinate at $((i, j), (j', k), (k', i'))$ is $1$ if $j = j'$, $k = k'$ and
$i = i'$, and $0$ otherwise.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationStructureTensor_coefficients`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-structure-tensor-c).

## Square matrix multiplication rank

For a field $F$ and a natural number $n$, the square
matrix multiplication rank of $F$ at $n$ is the tensor rank of the structure tensor of
multiplying two $n \times n$ matrices over $F$: the least number of pure tensors whose sum is that
structure tensor.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.squareMatrixMultiplicationRank`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#square-matrix-multiplication-rank).

## Square matrix multiplication rank equals the coefficient tensor rank

For every field $F$
and natural number $n$, the square matrix multiplication rank of $F$ at $n$ equals the trilinear
rank of the square $n \times n$ matrix multiplication tensor over $F$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.squareMatrixMultiplicationRank_eq`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#square-matrix-multiplication-rank-eq).

## Matrix multiplication tensor contraction

Let $F$ be a field, let $m, n, p$ be natural
numbers, let $A \in F^{m \times n}$ and $B \in F^{n \times p}$, and let $i < m$ and $k < p$. Write
$T$ for the matrix multiplication tensor over $F$ for $m, n, p$ and, for a natural number $q$,
$[q] = \{0, \dots, q - 1\}$. The contraction of $T$ against $A$ and $B$ at output coordinate
$(i, k)$ is

$$\sum_{a \in [m] \times [n]} \sum_{b \in [n] \times [p]} T(a, b, (k, i)) \, A_a \, B_b,$$

where $A_a$ and $B_b$ are the entries of $A$ and $B$ at the matrix coordinates $a$ and $b$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationTensorContraction`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-tensor-contraction).

## Contracting the matrix multiplication tensor gives the matrix product

For a field $F$,
matrices $A \in F^{m \times n}$ and $B \in F^{n \times p}$, and indices $i < m$ and $k < p$, the
contraction of the matrix multiplication tensor against $A$ and $B$ at output coordinate
$(i, k)$ equals the entry $(AB)_{ik}$ of the matrix product.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationTensorContraction_eq_mul`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-tensor-contraction-2).

## Matrix multiplication rank exponent

A real number $w$ is a matrix multiplication rank
exponent over a field $F$ when $w \ge 0$ and there are a real $C > 0$ and a natural number
$N_0 \ge 1$ such that for every $n \ge N_0$ the $n \times n$ matrix multiplication coefficient
tensor over $F$ is a sum of at most $C n^w$ rank-one trilinear terms.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasMatrixMultiplicationRankExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-matrix-multiplication-rank-exponent).

## Rank exponents via the minimum tensor rank

Let $F$ be a field and $w$ a real number. Then
$w$ is a matrix multiplication rank exponent over $F$ if and only if $w \ge 0$ and there are a real
$C > 0$ and a natural number $N_0 \ge 1$ such that for every $n \ge N_0$ the tensor rank of the
$n \times n$ matrix multiplication structure tensor over $F$ is at most $C n^w$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasMatrixMultiplicationRankExponent_iff`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-matrix-multiplication-rank-exponent-2).

## Monotonicity of matrix multiplication rank exponents

Let $F$ be a field and let
$w \le w'$ be real numbers. If $w$ is a matrix multiplication rank exponent for $F$, then so
is $w'$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasMatrixMultiplicationRankExponent.mono`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#mono-2).

## Matrix multiplication exponent

The matrix multiplication exponent $\omega(F)$ of a field
$F$ is the infimum, taken in $[0, \infty]$, of the real numbers $w$ that are matrix multiplication
rank exponents over $F$; it is $\infty$ when there is no such $w$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-exponent).

## Rank exponents bound the matrix multiplication exponent

If a real number $w$ is a matrix
multiplication rank exponent over a field $F$, then the matrix multiplication exponent
$\omega(F)$ of $F$ satisfies $\omega(F) \le w$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationExponent_le_of_admissible`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-exponent-le-of-adm).

## Lower bounds for the matrix multiplication exponent

Let $F$ be a field and let $W$ be an
element of $[0, \infty]$. If $W \le w$ for every real number $w$ that is a matrix multiplication
rank exponent over $F$, then $W$ is at most the matrix multiplication exponent $\omega(F)$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.le_matrixMultiplicationExponent`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#le-matrix-multiplication-exponent).

## Direct rank bound for the matrix multiplication tensor

For every field $F$ and natural
numbers $m, n, p$, the coefficient tensor of multiplying an $m \times n$ matrix by an $n \times p$
matrix over $F$ is a sum of at most $mnp$ rank-one trilinear terms.

The decomposition is the direct algorithm, with one term for each triple $(i, j, k)$ with
$i < m$, $j < n$ and $k < p$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationTensor_rank_le_product`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-tensor-rank-le-pro).

## Direct decomposition of the structure tensor

Let $F$ be a field, let $m, n, p$ be
natural numbers, and write $e_x$ for the standard basis vector with index $x$. The matrix
multiplication structure tensor
$\sum_{i < m,\, j < n,\, k < p} e_{(i,j)} \otimes e_{(j,k)} \otimes e_{(k,i)}$ in
$F^{m \times n} \otimes F^{n \times p} \otimes F^{p \times m}$ is a sum of at most $mnp$ pure
tensors $u \otimes v \otimes w$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationStructureTensor_rank_le_product`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-structure-tensor-r).

## Strassen's rank bound for $2 \times 2$ matrix multiplication

For every field $F$, the
square $2 \times 2$ matrix multiplication tensor over $F$ is a sum of at most $7$ rank-one
trilinear terms.

The seven terms are Strassen's, and the decomposition holds in every characteristic.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.squareMatrixMultiplicationTensor_rank_le_seven`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 407](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L407). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#square-matrix-multiplication-tensor-rank).

## Strassen's decomposition of the structure tensor

Let $F$ be a field and write $e_x$ for
the standard basis vector with index $x$. The $2 \times 2$ matrix multiplication structure tensor
$\sum_{i, j, k < 2} e_{(i,j)} \otimes e_{(j,k)} \otimes e_{(k,i)}$ in
$F^{2 \times 2} \otimes F^{2 \times 2} \otimes F^{2 \times 2}$ is a sum of at most $7$ pure
tensors $u \otimes v \otimes w$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationStructureTensor_rank_le_seven`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-structure-tensor-r-2).

## Direct rank bound for the square matrix multiplication tensor

For every field $F$ and
natural number $n$, the square $n \times n$ matrix multiplication tensor over $F$ is a sum of at
most $n^3$ rank-one trilinear terms.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.squareMatrixMultiplicationTensor_rank_le_cube`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#square-matrix-multiplication-tensor-rank-2).

## Exponent three for matrix multiplication rank

For every field $F$, the number $3$ is a
matrix multiplication rank exponent over $F$.

It is witnessed by the direct decomposition of the $n \times n$ matrix multiplication tensor into
$n^3$ rank-one terms.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasMatrixMultiplicationRankExponent_three`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-matrix-multiplication-rank-exponent-3).

## The matrix multiplication exponent is at most three

For every field $F$, the matrix
multiplication exponent $\omega(F)$ of $F$ satisfies $\omega(F) \le 3$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationExponent_le_three`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-exponent-le-three).

## The matrix multiplication exponent is finite

For every field $F$, the matrix
multiplication exponent of $F$, an element of $[0, \infty]$, is not $\infty$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationExponent_ne_top`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-exponent-ne-top).

## Exponents above the matrix multiplication exponent admit rank bounds

Let $F$ be a field,
let $\omega(F)$ be its matrix multiplication exponent and let $w > 0$ be real. If
$\omega(F) < w$, then there are $C > 0$ and $N_0 \ge 1$ such that for every $n \ge N_0$ the
$n \times n$ matrix multiplication tensor over $F$ has rank at most $C n^w$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.hasMatrixMultiplicationRankExponent_of_inf_lt`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-matrix-multiplication-rank-exponent-4).

## Upper bounds on the matrix multiplication exponent

Let $F$ be a field, let $\omega(F)$
be its matrix multiplication exponent and let $w \ge 0$ be real. Then $\omega(F) \le w$ if and
only if for every real $\varepsilon > 0$ there are $C > 0$ and $N_0 \ge 1$ such that for every
$n \ge N_0$ the $n \times n$ matrix multiplication tensor over $F$ has rank at most
$C n^{w + \varepsilon}$.

The right-hand side bounds the rank by $C n^{w + \varepsilon}$ for each $\varepsilon > 0$;
it is not an $O(n^w)$ rank bound.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationExponent_le_iff`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-exponent-le-iff).

## Rank bounds just above the matrix multiplication exponent

Let $F$ be a field and let
$\omega(F)$ be its matrix multiplication exponent, a finite real number. For every real
$\varepsilon > 0$ there are $C > 0$ and $N_0 \ge 1$ such that for every $n \ge N_0$ the
$n \times n$ matrix multiplication tensor over $F$ has rank at most
$C n^{\omega(F) + \varepsilon}$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.matrixMultiplicationExponent_endpoint`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#matrix-multiplication-exponent-endpoint).

## Rectangular inner dimension

For a natural number $n$ and a real aspect $k$, the
rectangular inner dimension is $\lceil n^k \rceil$, the least natural number that is at least
the real power $n^k$.

It is the inner dimension in the product of an $n \times \lceil n^k \rceil$ matrix and a
$\lceil n^k \rceil \times n$ matrix.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.rectangularInnerDimension`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-inner-dimension).

## Rectangular inner dimension at aspect zero

For every natural number $n$, including
$n = 0$, the rectangular inner dimension at dimension $n$ and aspect $0$, namely
$\lceil n^0 \rceil$, equals $1$, so aspect $0$ is the outer product of an $n \times 1$ matrix
and a $1 \times n$ matrix.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.rectangularInnerDimension_zero`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-inner-dimension-zero).

## Rectangular inner dimension at aspect one

For every natural number $n$, the rectangular
inner dimension at dimension $n$ and aspect $1$, namely $\lceil n^1 \rceil$, equals $n$, so
aspect $1$ is square matrix multiplication without rounding.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.rectangularInnerDimension_one`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-inner-dimension-one).

## Rectangular inner dimension at dimension one

For every real aspect $k$, the rectangular
inner dimension at dimension $1$ and aspect $k$, namely $\lceil 1^k \rceil$, equals $1$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.rectangularInnerDimension_one_base`, a theorem declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-inner-dimension-one-base).

## Rank exponents for rectangular matrix multiplication

Let $F$ be a field and let $k, w$ be
real. Then $w$ is a rank exponent for rectangular matrix multiplication over $F$ at aspect $k$
when $k \ge 0$, $w \ge 0$, and for every $\varepsilon > 0$ there are $C > 0$ and $N_0 \ge 1$
such that for every $n \ge N_0$ the tensor of multiplying an $n \times \lceil n^k \rceil$
matrix by a $\lceil n^k \rceil \times n$ matrix over $F$ has rank at most
$C n^{w + \varepsilon}$.

The coefficient $C$ and the threshold $N_0$ may depend on $\varepsilon$, but not on $n$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.HasRectangularMatrixMultiplicationRankExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#has-rectangular-matrix-multiplication-ra).

## Rectangular matrix multiplication exponent

For a field $F$ and a real number $k$, the
rectangular matrix multiplication exponent $\omega(k)$ of $F$ is the infimum in $[0, \infty]$ of
all real $w \ge 0$ with the following property: for every $\varepsilon > 0$ there are a real
$C > 0$ and a natural number $N_0 \ge 1$ such that for every $n \ge N_0$, the coefficient tensor
$\sum e_{ij} \otimes e_{jl} \otimes e_{li}$ of multiplying an $n \times \lceil n^k \rceil$ matrix
by an $\lceil n^k \rceil \times n$ matrix over $F$ is a sum of at most $C n^{w + \varepsilon}$
rank-one trilinear terms. If $k < 0$, no $w$ qualifies and $\omega(k) = \infty$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.rectangularMatrixMultiplicationExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-matrix-multiplication-expone).

## Dual matrix multiplication exponent

For a field $F$, the dual matrix multiplication
exponent of $F$ is the supremum, taken in the extended nonnegative reals $[0, \infty]$, of the
set of real aspects $k \ge 0$ for which the rectangular matrix multiplication exponent of $F$ at
aspect $k$ equals $2$.

Formalized by `Cslib.Complexity.Algebraic.MatrixMultiplicationExponent.dualMatrixMultiplicationExponent`, a definition declared in [CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean, line 514](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Complexity/Algebraic/MatrixMultiplicationExponent.lean#L514). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#dual-matrix-multiplication-exponent).

## Dual exponent at most one

For every field $F$, the dual matrix multiplication
exponent $\alpha(F)$ of the arithmetic-circuit model satisfies $\alpha(F) \le 1$.

## Sources

- C15b, CLLZ2025 Figure 2, the general upper bound, not a method-specific barrier.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.upperBoundOne` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#upper-bound-one).

## Coppersmith's rectangular exponent

For every field $F$, the rectangular matrix
multiplication exponent of the arithmetic-circuit model at aspect $0.172$ equals $2$: an
$n \times \lceil n^{0.172} \rceil$ matrix times an $\lceil n^{0.172} \rceil \times n$ matrix costs
$n^{2 + o(1)}$ arithmetic operations.

## Sources

- C15b/LGU2018 Section 1.1, Coppersmith's 1982 exponent equality.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.coppersmith1982Exponent` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#coppersmith1982-exponent).

## Coppersmith's 1997 bound on the dual exponent

For every field $F$, the dual matrix
multiplication exponent $\alpha(F)$ of the arithmetic-circuit model satisfies
$\alpha(F) > 0.29462$.

## Sources

- C15b/LG2012 abstract, the previous Coppersmith 1997 record is strict.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.coppersmith1997StrictLower` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#coppersmith1997-strict-lower).

## Le Gall's 2012 bound on the dual exponent

For every field $F$, the dual matrix
multiplication exponent $\alpha(F)$ of the arithmetic-circuit model satisfies
$\alpha(F) > 0.30298$.

## Sources

- C15b/LG2012 abstract, Le Gall's 2012 improvement is strict.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.leGall2012StrictLower` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#le-gall2012-strict-lower).

## Le Gall–Urrutia bound on the dual exponent

For every field $F$, the dual matrix
multiplication exponent $\alpha(F)$ of the arithmetic-circuit model satisfies
$\alpha(F) \ge 0.31389$.

## Sources

- C15b/LGU2018 Section 1.2, the fourth-power lower bound is weak.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.leGallUrrutia2018Lower` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#le-gall-urrutia2018-lower).

## Williams–Xu–Xu–Zhou bound on the dual exponent

For every field $F$, the dual matrix
multiplication exponent $\alpha(F)$ of the arithmetic-circuit model satisfies
$\alpha(F) > 0.321334$.

## Sources

- C15b/WXXZ2024 introduction, the best displayed lower bound is strict.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.williamsXuXuZhou2024StrictLower` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#williams-xu-xu-zhou2024-strict-lower).

## Naive bound for rectangular matrix multiplication

For every field $F$ and every real
$k \ge 0$, the rectangular matrix multiplication exponent of the arithmetic-circuit model at
aspect $k$ is at most $2 + k$.

## Sources

- CLLZ rectangular naive upper bound; a general finite circuit construction is missing.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.rectangularNaiveUpper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-naive-upper).

## Circuit size and tensor rank give the same rectangular exponent

For every field $F$
and every real $k \ge 0$, the rectangular matrix multiplication exponent at aspect $k$ defined
by arithmetic-circuit size equals the one defined by tensor rank.

## Sources

- LG2012 exact bilinear-rank characterization; the operation/rank transfer is missing.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.rectangularOperationRankBridge` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#rectangular-operation-rank-bridge).

## The rectangular exponent depends only on the characteristic

If two fields $F$ and $K$
have the same characteristic, then for every real $k \ge 0$ the rectangular matrix
multiplication exponents of $F$ and $K$ in the arithmetic-circuit model at aspect $k$ are
equal.

## Sources

- LG2012 Section 1, characteristic dependence; this circuit-model transfer is missing.

Stated but not proved: `Cslib.Complexity.Algebraic.DualMatrixMultiplicationBoundsWanted.characteristicInvariance` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/DualMatrixMultiplicationBoundsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#characteristic-invariance).

## Conjecture that the square exponent is two

The proposition that for every field $F$,
the square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model equals $2$.

Since $\omega(F) \ge 2$ always holds, this says the trivial lower bound is sharp. It is a
conjecture, recorded as a proposition and not asserted.

Formalized by `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.omegaEqualsTwoConjecture`, a definition declared in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#omega-equals-two-conjecture).

## Naive bound for square matrix multiplication

For every field $F$, the square matrix
multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies $\omega(F) \le 3$.

## Sources

- C15a, trivial upper bound. The general finite naive circuit construction is not supplied upstream, so this remains a proof request.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.naiveUpperThree` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#naive-upper-three).

## Strassen's 1969 bound on the matrix multiplication exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le \log_2 7$.

## Sources

- C15a [S1969], Strassen's `log₂ 7` bound.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.strassen1969Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#strassen1969-upper).

## Pan's 1978 bound on the square exponent

For every field $F$, the square matrix
multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le \log_{70} 143640$.

## Sources

- C15a [P1978], Pan's `log₇₀ 143640` bound.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.pan1978Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#pan1978-upper).

## Bini–Capovani–Romani–Lotti bound on the square exponent

For every field $F$, the square
matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 3 \log_{12} 10$.

## Sources

- C15a [BCRL1979, B1980], the `3 log₁₂ 10` approximate-algorithm bound.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.biniCapovaniRomaniLotti1979Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#bini-capovani-romani-lotti1979-upper).

## Pan's 1979 bound on the matrix multiplication exponent

For every field $F$, the square
matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 3 \log_{436} 196$.

## Sources

- C15a [P1979], Pan's `3 log₄₃₆ 196` bound.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.pan1979Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#pan1979-upper).

## Pan's 1980 bound on the matrix multiplication exponent

For every field $F$, the square
matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le \log_{48} 47216$.

## Sources

- C15a [P1980], Pan's `log₄₈ 47216` bound.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.pan1980Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#pan1980-upper).

## Schönhage's 1981 bound on the matrix multiplication exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le \log_{110} 140600$.

## Sources

- C15a [S1981], Schönhage's `log₁₁₀ 140600` bound.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.schonhage1981Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#schonhage1981-upper).

## Pan's 1981 bound on the matrix multiplication exponent

For every field $F$, the square
matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.5161$.

## Sources

- C15a [P1981], Pan's decimal bound `2.5161`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.pan1981Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#pan1981-upper).

## Romani's 1982 bound on the matrix multiplication exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.5166$.

## Sources

- C15a [R1982], Romani's decimal bound `2.5166`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.romani1982Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#romani1982-upper).

## Coppersmith–Winograd 1982 bound on the square exponent

For every field $F$, the square
matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.495548$.

## Sources

- C15a [CW1982], Coppersmith--Winograd bound `2.495548`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.coppersmithWinograd1982Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#coppersmith-winograd1982-upper).

## Strassen's 1987 bound on the matrix multiplication exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.4785$.

## Sources

- C15a [S1987], Strassen's laser-method bound `2.4785`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.strassen1987Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#strassen1987-upper).

## Coppersmith–Winograd 1990 bound on the square exponent

For every field $F$, the square
matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.375477$.

## Sources

- C15a [CW1990], Coppersmith--Winograd bound `2.375477`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.coppersmithWinograd1990Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#coppersmith-winograd1990-upper).

## Cohn–Kleinberg–Szegedy–Umans bound on the square exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.41$.

## Sources

- C15a [CKSU2005], group-theoretic bound `2.41`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.cohnKleinbergSzegedyUmans2005Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#cohn-kleinberg-szegedy-umans2005-upper).

## Stothers–Davie bound on the matrix multiplication exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.373689703$.

## Sources

- C15a [S2010, DS2013], bound `2.373689703`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.stothersDavie2013Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#stothers-davie2013-upper).

## Vassilevska Williams's 2012 bound on the matrix multiplication exponent

For every
field $F$, the square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model
satisfies $\omega(F) \le 2.372873$.

## Sources

- C15a [V2012, V2014], Vassilevska Williams bound `2.372873`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.vassilevskaWilliams2012Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#vassilevska-williams2012-upper).

## Zhdanovich's 2012 bound on the matrix multiplication exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.373$.

## Sources

- C15a [Z2012], Zhdanovich bound `2.373`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.zhdanovich2012Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#zhdanovich2012-upper).

## Le Gall's 2014 bound on the square exponent

For every field $F$, the square matrix
multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.3728639$.

## Sources

- C15a [LG2014], Le Gall bound `2.3728639`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.leGall2014Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#le-gall2014-upper).

## Alman–Vassilevska Williams 2020 bound on the square exponent

For every field $F$, the
square matrix multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.3728596$.

## Sources

- C15a [AV2020], Alman--Vassilevska Williams bound `2.3728596`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.almanVassilevskaWilliams2020Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#alman-vassilevska-williams2020-upper).

## Duan–Wu–Zhou bound on the square exponent

For every field $F$, the square matrix
multiplication exponent $\omega(F)$ of the arithmetic-circuit model satisfies
$\omega(F) \le 2.371866$.

## Sources

- C15a [DWZ2022], Duan--Wu--Zhou bound `2.371866`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.duanWuZhou2022Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#duan-wu-zhou2022-upper).

## Vassilevska Williams–Xu–Xu–Zhou upper bound for matrix multiplication

For every field
$F$, the square matrix multiplication exponent of $F$ in the arithmetic-circuit model is at
most $2.371552$.

## Sources

- C15a [VXXZ2023], bound `2.371552`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.vassilevskaWilliamsXuXuZhou2023Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#vassilevska-williams-xu-xu-zhou2023-uppe).

## Alman–Duan–Vassilevska Williams–Xu–Xu–Zhou upper bound for matrix multiplication

For
every field $F$, the square matrix multiplication exponent of $F$ in the arithmetic-circuit
model is at most $2.371339$.

## Sources

- C15a [ADVXXZ2024], bound `2.371339`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.almanDuanVassilevskaWilliamsXuXuZhou2024Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#alman-duan-vassilevska-williams-xu-xu-zh).

## Dupont–Eisenberger et al. upper bound for matrix multiplication

For every field $F$,
the square matrix multiplication exponent of $F$ in the arithmetic-circuit model is at most
$2.371177$.

## Sources

- C15a [DEKMRSZAWB2026], best catalogue bound `2.371177`.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.dupontEisenbergerEtAl2026Upper` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#dupont-eisenberger-et-al2026-upper).

## Circuit size and tensor rank give the same square exponent

For every field $F$, the
square matrix multiplication exponent of $F$ defined by arithmetic-circuit size equals the
matrix multiplication exponent of $F$ defined by tensor rank.

## Sources

- C15a additional comments and [B2013]: the arithmetic-operation exponent agrees with the tensor-rank exponent. This bridge is not proved.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.squareOperationRankBridge` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#square-operation-rank-bridge).

## The square exponent depends only on the characteristic

If two fields $F$ and $K$ have
the same characteristic, then the square matrix multiplication exponents of $F$ and $K$ in the
arithmetic-circuit model are equal.

## Sources

- C15a additional comments and [S1981]: the exponent depends only on the field characteristic. This circuit-model transfer is not proved.

Stated but not proved: `Cslib.Complexity.Algebraic.SquareMatrixMultiplicationBoundsWanted.characteristicInvariance` is written with `theorem_wanted` in [WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/Algebraic/SquareMatrixMultiplicationBoundsWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html#characteristic-invariance-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Matrix multiplication exponent](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/algebraic-complexity/matrix-multiplication-exponent)
