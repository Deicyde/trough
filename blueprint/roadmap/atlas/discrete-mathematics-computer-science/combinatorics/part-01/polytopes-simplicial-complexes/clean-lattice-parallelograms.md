---
declaration: section
origin: cited
lean: MetaMathlibExt.latticePoints, MetaMathlibExt.latticeParallelogram, MetaMathlibExt.stdCleanParallelogram, MetaMathlibExt.unimodularMap, MetaMathlibExt.UnimodularlyEquivalent, MetaMathlibExt.unimodularlyEquivalent_refl, MetaMathlibExt.IsCleanParallelogram, MetaMathlibExt.stdColumn
statement: formalized
---

# Clean lattice parallelograms

31 results, 14 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html).

## The integer lattice in the plane

The lattice points of $\mathbb{R}^2$ are the points
$(a, b)$ with $a, b \in \mathbb{Z}$; they form the image of $\mathbb{Z}^2$ in $\mathbb{R}^2$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 1.

Formalized by `MetaMathlibExt.latticePoints`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#lattice-points).

## Parallelogram spanned by two vectors

For $u, v \in \mathbb{R}^2$, the parallelogram
spanned by $u$ and $v$ is the set $\{s u + t v : 0 \le s \le 1,\ 0 \le t \le 1\}$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 1.1.

Formalized by `MetaMathlibExt.latticeParallelogram`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#lattice-parallelogram).

## The parallelogram $P_{a,n}$

For natural numbers $a$ and $n$, the set
$P_{a,n} \subseteq \mathbb{R}^2$ is the closed parallelogram spanned by $(1, 0)$ and $(a, n)$,
that is, the set of points $s (1, 0) + t (a, n)$ with $0 \le s \le 1$ and $0 \le t \le 1$. For
$n \ge 1$ it is the parallelogram with vertices $(0, 0)$, $(1, 0)$, $(a, n)$ and $(a + 1, n)$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 2.

Formalized by `MetaMathlibExt.stdCleanParallelogram`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#std-clean-parallelogram).

## Integer affine maps of the plane

For a $2 \times 2$ integer matrix $M$ with entries
$m_{ij}$ and an integer vector $u = (u_1, u_2) \in \mathbb{Z}^2$, the map
$T_{M,u} : \mathbb{R}^2 \to \mathbb{R}^2$ is
$T_{M,u}(x, y) = (m_{11} x + m_{12} y + u_1, m_{21} x + m_{22} y + u_2)$, that is,
$p \mapsto M p + u$. It is an affine unimodular map when $\det M = \pm 1$; the definition itself
puts no condition on $\det M$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 1.1.

Formalized by `MetaMathlibExt.unimodularMap`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#unimodular-map).

## Unimodularly equivalent sets

Two sets $P, Q \subseteq \mathbb{R}^2$ are unimodularly
equivalent when some affine unimodular map sends $P$ onto $Q$: there are a $2 \times 2$ integer
matrix $M$ with $\det M = 1$ or $\det M = -1$ and an integer vector $u \in \mathbb{Z}^2$ such that
$\{M x + u : x \in P\} = Q$.

In the paper's notation, where $T$ is the map and $P_1$ and $P_2$ are the two sets, the displayed
condition $T(P_1) = T(P_2)$ is a typo for $T(P_1) = P_2$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 1.1.

Formalized by `MetaMathlibExt.UnimodularlyEquivalent`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#unimodularly-equivalent).

## Unimodular equivalence is reflexive

Every subset $P$ of $\mathbb{R}^2$ is unimodularly
equivalent to itself (take the identity matrix and the zero translation).

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 1.1.

Formalized by `MetaMathlibExt.unimodularlyEquivalent_refl`, a theorem declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#unimodularly-equivalent-refl).

## Clean lattice parallelogram

For points $u, v \in \mathbb{R}^2$, the parallelogram
spanned by $u$ and $v$ is clean when $u$ and $v$ are lattice points and the lattice points on the
boundary of the parallelogram are exactly $0$, $u$, $v$ and $u + v$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 2 (definition after Reznick).

Formalized by `MetaMathlibExt.IsCleanParallelogram`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#is-clean-parallelogram).

## Interior lattice points of $P_{a,n}$ on a vertical line

For natural numbers $a$ and $n$,
let $P_{a,n}$ be the parallelogram spanned by $(1, 0)$ and $(a, n)$, with vertices $(0, 0)$,
$(1, 0)$, $(a, n)$, $(a + 1, n)$. For an integer $k$, the set $S_k$ is the set of integers $y$
such that $(k, y)$ lies in the interior of $P_{a,n}$, that is, the $y$-coordinates of the lattice
points in the interior of $P_{a,n}$ on the line $x = k$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 2.

Formalized by `MetaMathlibExt.stdColumn`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#std-column).

## Point reflection between the two triangles of a parallelogram

Let $u$ and $v$ be
linearly independent vectors in $\mathbb{R}^2$ and let $P$ be the parallelogram they span. The map
$p \mapsto u + v - p$ is a bijection from the set of points of the triangle
$\operatorname{conv}\{0, u, v\}$ that lie in the interior of $P$ onto the set of points of the
triangle $\operatorname{conv}\{u, v, u + v\}$ that lie in the interior of $P$.

The map sends $s u + t v$ to $(1 - s) u + (1 - t) v$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 1.

Stated but not proved: `MetaMathlibExt.antidiagonal_triangle_bijOn` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#antidiagonal-triangle-bij-on).

## Unimodular equivalences between the parallelograms $P_{b,n}$

For natural numbers $b$
and $n$ let $P_{b,n}$ be the parallelogram spanned by $(1, 0)$ and $(b, n)$, with vertices
$(0, 0)$, $(1, 0)$, $(b, n)$, $(b + 1, n)$. Let $n$, $a$ and $a'$ be natural numbers with $n > 1$,
$1 \le a < n$, $\gcd(a, n) = 1$, $1 \le a' < n$ and $a a' \equiv 1 \pmod{n}$. Then $P_{a,n}$ is
unimodularly equivalent to each of $P_{n-a,n}$, $P_{a',n}$ and $P_{n-a',n}$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 2.

Stated but not proved: `MetaMathlibExt.stdCleanParallelogram_unimodularlyEquivalent` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#std-clean-parallelogram-unimodularly-equ).

## Clean parallelograms are unimodularly equivalent to standard ones

Let $u$ and $v$ be
lattice points spanning a clean lattice parallelogram $P$ whose area is an integer $n \ge 2$. Then
there is an integer $a$ with $1 \le a < n$ and $\gcd(a, n) = 1$ such that $P$ is unimodularly
equivalent to the standard clean parallelogram $P_{a,n}$.

For area $1$ (the unit square) there is no such $a$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Theorem 3.

Stated but not proved: `MetaMathlibExt.cleanParallelogram_unimodularlyEquivalent_std` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#clean-parallelogram-unimodularly-equival).

## Interior lattice points of a standard clean parallelogram

Let $1 \le a < n$ with
$\gcd(a, n) = 1$, let $P_{a,n} = \{s (1, 0) + t (a, n) : 0 \le s \le 1,\ 0 \le t \le 1\}$, and
write $\langle x \rangle = x - \lfloor x \rfloor$ for the fractional part of a real number $x$.
The lattice points in the interior of $P_{a,n}$ are exactly the points
$\langle k(n - a)/n \rangle \, (1, 0) + (k/n) \, (a, n)$ for $k = 1, \dots, n - 1$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 3.

Stated but not proved: `MetaMathlibExt.interior_stdCleanParallelogram_latticePoints` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#interior-std-clean-parallelogram-lattice).

## The point reflection symmetry of $P_{a,n}$

Let $a$ and $n$ be natural numbers with
$1 \le a < n$ and $\gcd(a, n) = 1$, let $P_{a,n} \subseteq \mathbb{R}^2$ be the parallelogram
with vertices $(0, 0)$, $(1, 0)$, $(a, n)$, $(a + 1, n)$, and let
$S : \mathbb{R}^2 \to \mathbb{R}^2$ be $S(x, y) = (a + 1 - x, n - y)$. Then $S(P_{a,n}) = P_{a,n}$,
and $S$ is an isometry of $\mathbb{R}^2$ for the maximum distance
$d((x, y), (x', y')) = \max(|x - x'|, |y - y'|)$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 4.

Stated but not proved: `MetaMathlibExt.stdCleanParallelogram_symmetry` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#std-clean-parallelogram-symmetry).

## Lowest and highest interior lattice points of $P_{a,n}$ on each vertical line

Let $a$
and $n$ be natural numbers with $1 \le a < n$ and $\gcd(a, n) = 1$, let $P_{a,n}$ be the
parallelogram with vertices $(0, 0)$, $(1, 0)$, $(a, n)$, $(a + 1, n)$, and for an integer $k$
let $S_k$ be the set of integers $y$ such that $(k, y)$ lies in the interior of $P_{a,n}$. If
$a = 1$, the least element of $S_1$ is $1$ and the greatest is $n - 1$. If $a > 1$, then: for
every integer $k$ with $2 \le k \le a - 1$, the least element of $S_k$ is
$\lceil (k - 1) n / a \rceil$ and the greatest is $\lfloor k n / a \rfloor$; the least element of
$S_1$ is $1$ and the greatest is $\lfloor n / a \rfloor$; and the least element of $S_a$ is
$\lceil (a - 1) n / a \rceil$ and the greatest is $n - 1$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 5.

Stated but not proved: `MetaMathlibExt.stdColumn_least_greatest` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#std-column-least-greatest).

## Lowest and highest interior lattice points of $P_{a,n}$ on paired vertical lines

Let $a$
and $n$ be natural numbers with $1 \le a < n$ and $\gcd(a, n) = 1$, let $P_{a,n}$ be the
parallelogram with vertices $(0, 0)$, $(1, 0)$, $(a, n)$, $(a + 1, n)$, and for an integer $k$
let $S_k$ be the set of integers $y$ such that $(k, y)$ lies in the interior of $P_{a,n}$. Let
$k, l \ge 1$ be natural numbers with $k + l = a + 1$, and suppose that $y_L$ is the least element
of $S_k$ and $y_H$ is the greatest element of $S_l$. Then $y_L + y_H = n$, and $(l, y_H)$ lies on
the boundary of the convex hull of the points of $\mathbb{Z}^2$ in the interior of $P_{a,n}$ if
and only if $(k, y_L)$ does.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 6.

Stated but not proved: `MetaMathlibExt.stdColumn_low_add_high` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#std-column-low-add-high).

## Number of steps of Euclid's algorithm

For natural numbers $u$ and $v$, the number of
division steps of Euclid's algorithm on $(u, v)$ is $0$ if $v = 0$, and otherwise one more than
the number of division steps on $(v, u \bmod v)$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 5.3 (division steps of the Euclidean algorithm).

Formalized by `MetaMathlibExt.euclidSteps`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#euclid-steps).

## Euclid's algorithm on small inputs

Euclid's algorithm takes exactly one division step
on $(2, 1)$, two division steps on $(3, 2)$ and five division steps on $(13, 8)$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 5.3.

Formalized by `MetaMathlibExt.euclidSteps_small_values`, a theorem declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#euclid-steps-small-values).

## Lamé's theorem (1844)

Let $F_0 = 0$, $F_1 = 1$, $F_{k+2} = F_{k+1} + F_k$ be the
Fibonacci numbers, and let $N \ge 1$. Let $u > v > 0$ be natural numbers on which Euclid's
algorithm takes exactly $N$ division steps, and suppose that $u \le u'$ whenever $u' > v' > 0$
are natural numbers on which it takes exactly $N$ division steps. Then $u = F_{N+2}$ and
$v = F_{N+1}$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Theorem 7.

Stated but not proved: `MetaMathlibExt.lame_euclidSteps_minimal` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#lame-euclid-steps-minimal).

## Convergent vectors of a continued fraction

Let $x$ be a rational number with regular
continued fraction $[q_0; q_1, q_2, \dots]$, and let $A_j$ and $B_j$ be the numerators and
denominators of its convergents, given by $A_{-2} = 0$, $A_{-1} = 1$, $B_{-2} = 1$, $B_{-1} = 0$
and $A_j = q_j A_{j-1} + A_{j-2}$, $B_j = q_j B_{j-1} + B_{j-2}$ for $j \ge 0$. Stark's
convergent vectors of $x$ are $v_j = (B_j, A_j)$ for $j \ge -2$, so $v_{-2} = (1, 0)$,
$v_{-1} = (0, 1)$ and $v_j = v_{j-2} + q_j v_{j-1}$ for every $j \ge 0$ for which $q_j$ exists.

If the expansion terminates with $q_m$, then $v_j = v_m$ for all $j > m$; for $j < -2$ the
value is set to $v_0$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 3 (CF algorithm).

Formalized by `MetaMathlibExt.convergentVec`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec).

## Partial quotients of a rational number

Let $x$ be a rational number. The continued
fraction algorithm sets $x_0 = x$ and $q_0 = \lfloor x_0 \rfloor$ and, as long as $x_j$ is not an
integer, $x_{j+1} = 1/(x_j - q_j)$ and $q_{j+1} = \lfloor x_{j+1} \rfloor$; it stops at the first
index $m$ for which $x_m$ is an integer, so that $x = [q_0; q_1, \dots, q_m]$. For a natural
number $i$, the $i$-th partial quotient of $x$ is $q_i$ when $i \le m$ and $0$ when $i > m$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 3.

Formalized by `MetaMathlibExt.partialQuotient`, a definition declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#partial-quotient).

## Initial convergent vectors

For every rational number $x$, the convergent vectors of the
regular continued fraction of $x$ begin with $v_{-2} = (1, 0)$, $v_{-1} = (0, 1)$ and
$v_0 = (1, \lfloor x \rfloor)$, and its zeroth partial quotient is $q_0 = \lfloor x \rfloor$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 3 (CF algorithm, Step 1 and Step 2).

Formalized by `MetaMathlibExt.convergentVec_initial`, a theorem declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-initial).

## Recurrence for convergent vectors

Let $x$ be a rational number with regular continued
fraction $[q_0; q_1, q_2, \dots]$ and convergent vectors $v_{-2}, v_{-1}, v_0, \dots$, and let
$i \ge 0$. If the expansion of $x$ has a term $b$ in position $i + 2$ (it does not terminate
before $q_{i+2}$), then $q_{i+2} = b$ and $v_{i+2} = v_i + b \, v_{i+1}$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Section 3 (CF algorithm, Step 3).

Formalized by `MetaMathlibExt.convergentVec_recurrence`, a theorem declared in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-recurrence).

## The last partial quotient of $n/a$ is at least $2$

Let $a$ and $n$ be natural numbers
with $1 \le a < n$, and let $n/a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of
$n/a$, where $q_0 = \lfloor n/a \rfloor$ and $m$ is the number of partial quotients after $q_0$
produced by the continued fraction algorithm (so $m = 0$ exactly when $a$ divides $n$). Then
$q_m \ge 2$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 7.

Stated but not proved: `MetaMathlibExt.partialQuotient_last_ge_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#partial-quotient-last-ge-two).

## Lattice points of the parallelogram of two consecutive convergent vectors

Let
$1 \le a < n$ be integers, let $n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction
of $n / a$, where $m$ is the least index at which it terminates, and let $v_i$ be its convergent
vectors. For every integer $i$ with $-2 \le i < m$, the lattice points of the parallelogram
spanned by $v_i$ and $v_{i+1}$ are exactly $0$, $v_i$, $v_{i+1}$ and $v_i + v_{i+1}$, and every
point of $\mathbb{Z}^2$ equals $s v_i + t v_{i+1}$ for some integers $s$ and $t$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Theorem 4.

Stated but not proved: `MetaMathlibExt.convergentVec_parallelogram_latticePoints` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-parallelogram-lattice-poi).

## Distances of the convergent vectors to the line $y = (n / a) x$

Let $1 \le a < n$ be
coprime integers, let $n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of
$n / a$, where $m$ is the least index at which it terminates, and let $v_j = (B_j, A_j)$ be its
convergent vectors. For $p = (x, y) \in \mathbb{R}^2$ let $d(p) = |n x - a y| / \sqrt{n^2 + a^2}$
be the distance from $p$ to the line $y = (n / a) x$. Then: if $m \ge 1$, then
$d(v_0) < n / (2 \sqrt{n^2 + a^2})$ and $d(v_{m-1}) > 0$; for every natural number $i$ with
$i + 1 < m$ we have $d(v_{i+1}) < d(v_i)$, so the distances strictly decrease along
$v_0, v_1, \dots, v_{m-1}$; and for every $i$ with $1 \le i \le m - 1$, every lattice point
$(\beta, \alpha)$ with $0 < \beta < a$, $0 < \alpha < n$, $\beta \le B_i$ and
$(\beta, \alpha) \ne v_{i-1}, v_i$ satisfies $d(\beta, \alpha) > d(v_{i-1})$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Theorem 5.

Stated but not proved: `MetaMathlibExt.convergentVec_dist_strictAnti` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-dist-strict-anti).

## Convergent vectors in the quarters of $P_{a,n}$

Let $1 \le a < n$ be coprime integers,
let $n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of $n / a$, where $m$ is
the least index at which it terminates, and let $v_i$ be its convergent vectors. The lines
$y = (n / a)(x - 1/2)$ and $y = n / 2$ cut the parallelogram $P_{a,n}$ with vertices $(0, 0)$,
$(1, 0)$, $(a, n)$, $(a + 1, n)$ into four closed parallelograms: $P_1$ (lower left), spanned by
$(1/2, 0)$ and $(a/2, n/2)$, and its translates $P_2 = P_1 + (1/2, 0)$ (lower right),
$P_3 = P_1 + ((a + 1)/2, n/2)$ (upper right) and $P_4 = P_1 + (a/2, n/2)$ (upper left). Let
$S(p) = (a + 1, n) - p$. Then for every $i$ with $0 \le i < m$: if $i$ is even, then
$v_i \in P_1$ and $S(v_i) \in P_3$; if $i$ is odd, then $v_i + (1, 0) \in P_2$ and
$S(v_i + (1, 0)) \in P_4$.

These points form the sets $V_1$ and $V_2$ of the paper.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 8.

Stated but not proved: `MetaMathlibExt.convergentVec_mem_quarters` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-mem-quarters).

## Lattice points of the triangle with vertices $0$, $v_{i-2}$, $v_i$

Let $1 \le a < n$ be
integers, let $n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of $n / a$, where
$m$ is the least index at which it terminates, and let $v_j$ be its convergent vectors. For every
integer $i$ with $0 \le i \le m$, let $T_i$ be the closed triangle with vertices $0$, $v_{i-2}$
and $v_i$. Then the segment $[v_{i-2}, v_i]$ contains exactly $q_i + 1$ lattice points, the
interior of $T_i$ contains no lattice point, and every lattice point of $T_i$ other than its
vertices lies on the segment $[v_{i-2}, v_i]$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 9.

Stated but not proved: `MetaMathlibExt.convergentVec_triangle_latticePoints` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-triangle-lattice-points).

## A determinant of three convergent vectors

Let $1 \le a < n$ be integers, let
$n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of $n / a$, where $m$ is the
least index at which it terminates, and let $v_j = (B_j, A_j)$ be its convergent vectors. Then
for every natural number $i$ with $i + 2 \le m$, the determinant of the $3 \times 3$ matrix with
rows $(1, B_{i-2}, A_{i-2})$, $(1, B_i, A_i)$ and $(1, B_{i+2}, A_{i+2})$ equals
$(-1)^{i+1} q_i q_{i+1} q_{i+2}$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 10.

Stated but not proved: `MetaMathlibExt.convergentVec_det_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#convergent-vec-det-three).

## Vertices of the interior hull of a standard clean parallelogram

Let $1 \le a < n$ with
$\gcd(a, n) = 1$, let $P_{a,n} = \{s (1, 0) + t (a, n) : 0 \le s \le 1,\ 0 \le t \le 1\}$, and let
$n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of $n / a$, with $m \ge 2$.
Write $A_i / B_i$ for its $i$-th convergent, and put $v_{-1} = (0, 1)$, $v_i = (B_i, A_i)$ for
$i \ge 0$, $u_i = v_i + (1, 0)$ (so $u_{-1} = (1, 1)$) and $w = (a + 1, n)$. Then the vertices of
the convex hull of the lattice points in the interior of $P_{a,n}$ are exactly $u_{-1}$ and
$w - u_{-1}$, the points $u_i$ and $w - u_i$ for odd $i$ with $0 \le i < m$, and the points $v_i$
and $w - v_i$ for even $i$ with $0 \le i < m$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Theorem 6.

Stated but not proved: `MetaMathlibExt.extremePoints_interiorHull_stdCleanParallelogram` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#extreme-points-interior-hull-std-clean-p).

## Vertices and area of the interior hull of a standard clean parallelogram

Let
$1 \le a < n$ with $\gcd(a, n) = 1$, let
$P_{a,n} = \{s (1, 0) + t (a, n) : 0 \le s \le 1,\ 0 \le t \le 1\}$, let
$n / a = [q_0; q_1, \dots, q_m]$ be the regular continued fraction of $n / a$, and let $H$ be the
convex hull of the lattice points in the interior of $P_{a,n}$. If $H$ has positive area, then
$H$ has $2(m + 1)$ vertices when $q_0 > 1$ and $2m$ vertices otherwise (that is, when $q_0 = 1$),
and $q_0 + q_1 + \dots + q_m = \mathrm{area}(P_{a,n}) - \mathrm{area}(H)$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Lemma 11.

Stated but not proved: `MetaMathlibExt.interiorHull_stdCleanParallelogram_vertices_area` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#interior-hull-std-clean-parallelogram-ve).

## Clean interior hulls and Fibonacci numbers

Let $F_0 = 0$, $F_1 = 1$,
$F_{k+2} = F_{k+1} + F_k$ be the Fibonacci numbers. Let $1 \le a < n$ with $\gcd(a, n) = 1$, let
$P_{a,n} = \{s (1, 0) + t (a, n) : 0 \le s \le 1,\ 0 \le t \le 1\}$, and let $H$ be the convex
hull of the lattice points in the interior of $P_{a,n}$. Then the lattice points on the boundary of
$H$ are exactly the vertices of $H$ if and only if there is a natural number $k$ with $n = F_k$
and either $a = F_{k-1}$ or $a = F_{k-2}$.

## Sources

- Gabriel Khan, Mizan R. Khan, Riaz R. Khan, and Peng Zhao, *A Geometric Relationship between Continued Fractions and Clean Lattice Parallelograms*, INTEGERS 26 (2026), Article A10, Corollary 1.

Stated but not proved: `MetaMathlibExt.interiorHull_stdCleanParallelogram_clean_iff_fib` is written with `theorem_wanted` in [WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/CleanLatticeParallelogramWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html#interior-hull-std-clean-parallelogram-cl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Clean lattice parallelograms](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/polytopes-simplicial-complexes/clean-lattice-parallelograms)
