The **natural numbers** are the numbers $0, 1, 2, 3, \dots$ used to count the
elements of finite collections and to number the positions in a sequence. Their
collection is written $\mathbb{N}$. They are where arithmetic begins: the
[integers](trough:Int), the [rational numbers](trough:Rat) and the
[real numbers](trough:Real) are all constructed from them, and proof by
induction, one of the basic methods of mathematical argument, is a property of
$\mathbb{N}$. Conventions differ on whether $0$ counts as a natural number; this
article, like Mathlib, includes it, and calls $1, 2, 3, \dots$ the positive
integers.

## Definition

The natural numbers are characterized by the Peano axioms. They form a
[set](trough:Set) $\mathbb{N}$ with a distinguished element $0$ and a successor
function $S \colon \mathbb{N} \to \mathbb{N}$, thought of as $n \mapsto n + 1$, such that:

- $0$ is not the successor of any natural number: $S(n) \neq 0$ for every $n$;
- the successor function is injective: $S(m) = S(n)$ implies $m = n$;
- induction holds: if a set of natural numbers contains $0$, and contains $S(n)$ whenever it contains $n$, then it contains every natural number.

Any two structures satisfying these axioms are isomorphic by a unique bijection
that matches the two zeros and the two successor functions, so the axioms
determine $\mathbb{N}$ up to isomorphism. This uniqueness needs induction for
every subset of $\mathbb{N}$; with induction only for first-order formulas,
nonstandard models exist. In set theory one concrete model takes
$0$ to be the empty set and $S(n) = n \cup \{n\}$, so that each natural number is
the set of all smaller natural numbers, $n = \{0, 1, \dots, n - 1\}$.

The same principle that justifies induction also justifies definition by
recursion: given a value $a$ and a rule $g$, there is exactly one function $f$ on
$\mathbb{N}$ with $f(0) = a$ and
$f(n + 1) = g(n, f(n))$ for every $n$. Addition and
multiplication are defined this way, by recursion on the second argument:

$$m + 0 = m, \qquad m + S(n) = S(m + n), \qquad m \cdot 0 = 0, \qquad m \cdot S(n) = m \cdot n + m.$$

Writing $1 = S(0)$, the first two equations give $S(n) = n + 1$.

## Properties

**Arithmetic.** Under these operations the natural numbers
form a commutative semiring: addition and
multiplication are associative and commutative, multiplication distributes over
addition, and $0$ and $1$ are the identity elements. No natural number other than
$0$ has an additive inverse, so the equation $m + x = n$ need not have a solution
in $\mathbb{N}$; adjoining the missing solutions produces the integers.

**Order.** The usual order is determined by addition: $m \le n$ holds exactly when
$n = m + k$ for some natural number $k$. Every sum $m + k$ is at least $m$, and
whenever $m \le n$ there is such a $k$.
This is a total order in which
$0$ is the least element and
there is no largest element, since $n < n + 1$.

**Well-ordering.** Every nonempty set $A$ of natural numbers has a least element:
the infimum of $A$ belongs to $A$ and
lies below every element of $A$. The well-ordering principle
can stand in for induction: to prove that a property holds everywhere, one shows
that a least counterexample cannot exist.

**Division with remainder.** For natural numbers $a$ and $b$ with $b > 0$ there
are natural numbers $q$ and $r$, the quotient and the remainder, with

$$a = bq + r, \qquad 0 \le r < b.$$

Taking $q = \lfloor a / b \rfloor$ and $r = a \bmod b$, the identity
$b \lfloor a/b \rfloor + (a \bmod b) = a$ holds, and
the remainder is less than $b$ when $b > 0$. Repeated division
with remainder is the [Euclidean algorithm](trough:Nat.xgcd), which computes the
[greatest common divisor](trough:GCDMonoid.gcd).

**Primes.** A natural number $p \ge 2$ is [prime](trough:Prime) if its only
divisors are $1$ and $p$. [There are infinitely many primes](trough:Nat.exists_infinite_primes):
for every $n$ there is a prime $p \ge n$.
By the [fundamental theorem of arithmetic](trough:Nat.primeFactorsList_unique),
every positive integer is a product of primes, and
any two factorizations of $n$ into primes differ only in the order of the factors.

**Size.** The set $\mathbb{N}$ is infinite, and its
cardinality is $\aleph_0$, the smallest infinite
[cardinal](trough:Cardinal) (see [aleph numbers](trough:Cardinal.aleph)). A set
is countable when it can be mapped injectively into $\mathbb{N}$.

## Induction and recursion

Several variants of induction follow from the axiom. In strong induction,
if a property holds for $n$ whenever it holds for every $m < n$, then it holds for every natural number.
Induction can also start at any base value $m$:
if a property holds for $m$, and passes from $n$ to $n + 1$ for every $n \ge m$, then it holds for every $n \ge m$.

Recursion defines most of the familiar functions and sequences of
elementary mathematics: powers by $a^0 = 1$ and $a^{n+1} = a^n \cdot a$, the
factorial by $0! = 1$ and $(n + 1)! = (n + 1) \cdot n!$, and the Fibonacci numbers
by $F_0 = 0$, $F_1 = 1$ and
$F_{n+2} = F_n + F_{n+1}$. A recurrent sequence of real
numbers, given by a first term $x_0$ and a rule $x_{n+1} = h(x_n)$, is a function on
$\mathbb{N}$ defined in the same way.

## Related concepts

- **Number systems.** The [integers](trough:Int) adjoin additive inverses, the
  [rational numbers](trough:Rat) multiplicative inverses of nonzero integers, and
  the [real numbers](trough:Real) limits of Cauchy sequences of rationals.
- **Semirings.** For every semiring $R$ there is a
  ring homomorphism from $\mathbb{N}$ to $R$ sending $n$ to $n \cdot 1$,
  and any two ring homomorphisms from $\mathbb{N}$ to $R$ are equal.
  So $\mathbb{N}$ is the initial object among semirings: it maps to every
  semiring by exactly one homomorphism.
- **Ordinals and cardinals.** In the set-theoretic model above, the natural
  numbers are exactly the finite [ordinals](trough:Ordinal), and they also serve as
  the finite [cardinals](trough:Cardinal).

## In Mathlib

The natural numbers are defined in Lean's core library as an
inductive type with two constructors, zero and successor. Lean generates the
recursion principle together with this definition, so nothing has to be
postulated as an axiom; induction is that recursion principle applied to a
family of propositions, and the other two Peano axioms are theorems. The kernel computes with natural numbers using
arbitrary-precision arithmetic. Zero is a natural number, and the
positive natural numbers form a separate type. The operations are
total, with conventions for the cases where the textbook operation is undefined:
subtraction is truncated, so that $m - n = 0$ exactly when $m \le n$
(for instance $3 - 5 = 0$); division rounds down, and
division by zero gives $0$, while
the remainder of $a$ on division by zero is $a$. Statements
that need genuine subtraction carry a hypothesis such as $n \le m$, or pass to the
integers. Mathlib reads a natural number as an element of any semiring through
the cast $n \mapsto n \cdot 1$, which the map above bundles as a ring
homomorphism; this is how numerals such as $2$ make sense in every ring.

## Depends on

- [Set](trough:Set)
