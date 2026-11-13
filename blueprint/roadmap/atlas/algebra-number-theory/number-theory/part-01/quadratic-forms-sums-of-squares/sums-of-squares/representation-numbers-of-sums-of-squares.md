---
declaration: section
origin: cited
lean: SumSquares.solutions, SumSquares.representationNumber, SumSquares.solutions_finite, SumSquares.representationNumber_eq_toFinset_card, SumSquares.zero_mem_solutions, SumSquares.solutions_zero_zero, SumSquares.solutions_zero_succ, SumSquares.solutions_one_zero
statement: formalized
proof: formalized
---

# Representation numbers of sums of squares

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html).

## Integer solutions of a sum of squares

For natural numbers $k$ and $n$, the solution set
is the set of all integer vectors $x = (x_1, \dots, x_k) \in \mathbb{Z}^k$ with
$x_1^2 + \cdots + x_k^2 = n$.

Formalized by `SumSquares.solutions`, a definition declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#solutions).

## Representation numbers of sums of squares

For natural numbers $k$ and $n$, the
representation number $r_k(n)$ is the number of elements of the solution set, that is, the
number of integer vectors $(x_1, \dots, x_k) \in \mathbb{Z}^k$ with $x_1^2 + \cdots + x_k^2 = n$.
Representations that differ in the order or the signs of the entries are counted separately.

Formalized by `SumSquares.representationNumber`, a definition declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#representation-number).

## Finitely many representations as a sum of squares

For all natural numbers $k$ and $n$,
there are only finitely many integer vectors $(x_1, \dots, x_k) \in \mathbb{Z}^k$ with
$x_1^2 + \cdots + x_k^2 = n$.

Formalized by `SumSquares.solutions_finite`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#solutions-finite).

## The representation number counts a finite set

For all natural numbers $k$ and $n$, the
representation number $r_k(n)$ equals the number of elements of the finite solution set of
integer vectors $(x_1, \dots, x_k) \in \mathbb{Z}^k$ with $x_1^2 + \cdots + x_k^2 = n$.

Formalized by `SumSquares.representationNumber_eq_toFinset_card`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#representation-number-eq-to-finset-card).

## The zero vector represents zero as a sum of squares

For every $k \in \mathbb{N}$, the
zero vector of $\mathbb{Z}^k$ has squared norm $0$, that is, it lies in the set of integer
vectors $x \in \mathbb{Z}^k$ with $x_1^2 + \cdots + x_k^2 = 0$.

Formalized by `SumSquares.zero_mem_solutions`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#zero-mem-solutions).

## Solution set of the empty sum at zero

The set of vectors $x \in \mathbb{Z}^0$
whose sum of squares (an empty sum) equals $0$ is all of $\mathbb{Z}^0$.

Formalized by `SumSquares.solutions_zero_zero`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#solutions-zero-zero).

## Zero squares never sum to a positive integer

For every natural number $n \ge 1$, no
vector $x \in \mathbb{Z}^0$ has sum of squares equal to $n$; that is, the solution set is empty.

Formalized by `SumSquares.solutions_zero_succ`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#solutions-zero-succ).

## Solution set of one square equal to zero

The set of vectors $x \in \mathbb{Z}^1$
with $x_1^2 = 0$ consists of the zero vector alone.

Formalized by `SumSquares.solutions_one_zero`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#solutions-one-zero).

## Zero as a sum of zero squares

The representation number $r_0(0)$, the number of integer
vectors $x \in \mathbb{Z}^0$ whose sum of squares (an empty sum) equals $0$, is $1$.

Formalized by `SumSquares.representationNumber_zero_zero`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#representation-number-zero-zero).

## Positive integers have no representation as a sum of zero squares

For every natural
number $n \ge 1$, the representation number $r_0(n)$, the number of integer vectors
$x \in \mathbb{Z}^0$ whose sum of squares (an empty sum) equals $n$, is $0$.

Formalized by `SumSquares.representationNumber_zero_succ`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#representation-number-zero-succ).

## Zero as a sum of one square

The representation number $r_1(0)$, the number of integer
vectors $x \in \mathbb{Z}^1$ with $x_1^2 = 0$, equals $1$.

Formalized by `SumSquares.representationNumber_one_zero`, a theorem declared in [MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SumSquares/RepresentationCount.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html#representation-number-one-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representation numbers of sums of squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representation-numbers-of-sums-of-squares)
