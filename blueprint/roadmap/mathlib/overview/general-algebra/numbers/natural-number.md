# Natural number

The **natural numbers** are the numbers $0, 1, 2, 3, \dots$ used to count the
elements of finite collections and to number the positions in a sequence. Their
collection is written $\mathbb{N}$. They are where arithmetic begins: the
[integers](integer.md), the [rational numbers](rational-number.md) and the
[real numbers](real-number.md) are all constructed from them, and proof by
induction, one of the basic methods of mathematical argument, is a property of
$\mathbb{N}$. Conventions differ on whether $0$ counts as a natural number; this
article, like Mathlib, includes it, and calls $1, 2, 3, \dots$ the positive
integers.

## Definition

The natural numbers are characterized by the Peano axioms. They form a
[set](../../data-structures/sets/set.md) $\mathbb{N}$ with a distinguished element $0$ and a successor
function $S \colon \mathbb{N} \to \mathbb{N}$, thought of as $n \mapsto n + 1$, such that:

- [$0$ is not the successor of any natural number](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Nat/Basic.html#Nat.succ_ne_zero): $S(n) \neq 0$ for every $n$;
- [the successor function is injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Basic.html#Nat.succ_injective): $S(m) = S(n)$ implies $m = n$;
- induction holds: [if a set of natural numbers contains $0$, and contains $S(n)$ whenever it contains $n$, then it contains every natural number](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Nat.rec).

Any two structures satisfying these axioms are isomorphic by a unique bijection
that matches the two zeros and the two successor functions, so the axioms
determine $\mathbb{N}$ up to isomorphism. This uniqueness needs induction for
every subset of $\mathbb{N}$; with induction only for first-order formulas,
nonstandard models exist. In set theory one concrete model takes
$0$ to be the empty set and $S(n) = n \cup \{n\}$, so that each natural number is
the set of all smaller natural numbers, $n = \{0, 1, \dots, n - 1\}$.

The same principle that justifies induction also justifies definition by
recursion: given a value $a$ and a rule $g$, there is exactly one function $f$ on
$\mathbb{N}$ with [$f(0) = a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Init.html#Nat.rec_zero) and
[$f(n + 1) = g(n, f(n))$ for every $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Init.html#Nat.rec_add_one). Addition and
multiplication are defined this way, by recursion on the second argument:

$$m + 0 = m, \qquad m + S(n) = S(m + n), \qquad m \cdot 0 = 0, \qquad m \cdot S(n) = m \cdot n + m.$$

Writing $1 = S(0)$, the first two equations give $S(n) = n + 1$.

## Properties

**Arithmetic.** Under these operations the natural numbers
[form a commutative semiring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Nat.html#Nat.instCommSemiring): addition and
multiplication are associative and commutative, multiplication distributes over
addition, and $0$ and $1$ are the identity elements. No natural number other than
$0$ has an additive inverse, so the equation $m + x = n$ need not have a solution
in $\mathbb{N}$; adjoining the missing solutions produces the integers.

**Order.** The usual order is determined by addition: $m \le n$ holds exactly when
$n = m + k$ for some natural number $k$. Every sum $m + k$ is at least $m$, and
[whenever $m \le n$ there is such a $k$](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Nat/Lemmas.html#Nat.exists_eq_add_of_le).
This is [a total order](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Basic.html#Nat.instLinearOrder) in which
[$0$ is the least element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Nat.html#Nat.instOrderBot) and
[there is no largest element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Nat.html#Nat.instNoMaxOrder), since $n < n + 1$.

**Well-ordering.** Every nonempty set $A$ of natural numbers has a least element:
[the infimum of $A$ belongs to $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Lattice/Nat.html#Nat.sInf_mem) and
[lies below every element of $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/Lattice/Nat.html#Nat.sInf_le). The well-ordering principle
can stand in for induction: to prove that a property holds everywhere, one shows
that a least counterexample cannot exist.

**Division with remainder.** For natural numbers $a$ and $b$ with $b > 0$ there
are natural numbers $q$ and $r$, the quotient and the remainder, with

$$a = bq + r, \qquad 0 \le r < b.$$

Taking $q = \lfloor a / b \rfloor$ and $r = a \bmod b$, the identity
[$b \lfloor a/b \rfloor + (a \bmod b) = a$](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Nat/Div/Basic.html#Nat.div_add_mod) holds, and
[the remainder is less than $b$ when $b > 0$](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Nat.mod_lt). Repeated division
with remainder is the [Euclidean algorithm](../divisibility-in-integral-domains/euclids-algorithm.md), which computes the
[greatest common divisor](../divisibility-in-integral-domains/greatest-common-divisor.md).

**Primes.** A natural number $p \ge 2$ is [prime](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md) if its only
divisors are $1$ and $p$. [There are infinitely many primes](../../../hundred-theorems/part-01/the-infinitude-of-primes.md):
[for every $n$ there is a prime $p \ge n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Prime/Infinite.html#Nat.exists_infinite_primes).
By the [fundamental theorem of arithmetic](../../../hundred-theorems/part-04/the-fundamental-theorem-of-arithmetic.md),
every positive integer is a product of primes, and
[any two factorizations of $n$ into primes differ only in the order of the factors](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Factors.html#Nat.primeFactorsList_unique).

**Size.** The set $\mathbb{N}$ is infinite, and its
[cardinality is $\aleph_0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/SetTheory/Cardinal/Defs.html#Cardinal.mk_nat), the smallest infinite
[cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md) (see [aleph numbers](../../logic-and-computation/set-theory/cardinals/aleph-numbers.md)). A set
is countable when it can be mapped injectively into $\mathbb{N}$.

## Induction and recursion

Several variants of induction follow from the axiom. In strong induction,
[if a property holds for $n$ whenever it holds for every $m < n$, then it holds for every natural number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Init.html#Nat.strong_induction_on).
Induction can also start at any base value $m$:
[if a property holds for $m$, and passes from $n$ to $n + 1$ for every $n \ge m$, then it holds for every $n \ge m$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Init.html#Nat.le_induction).

Recursion defines most of the familiar functions and sequences of
elementary mathematics: powers by $a^0 = 1$ and $a^{n+1} = a^n \cdot a$, the
factorial by $0! = 1$ and $(n + 1)! = (n + 1) \cdot n!$, and the Fibonacci numbers
by $F_0 = 0$, $F_1 = 1$ and
[$F_{n+2} = F_n + F_{n+1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Fib/Basic.html#Nat.fib_add_two). A recurrent sequence of real
numbers, given by a first term $x_0$ and a rule $x_{n+1} = h(x_n)$, is a function on
$\mathbb{N}$ defined in the same way.

## Related concepts

- **Number systems.** The [integers](integer.md) adjoin additive inverses, the
  [rational numbers](rational-number.md) multiplicative inverses of nonzero integers, and
  the [real numbers](real-number.md) limits of Cauchy sequences of rationals.
- **Semirings.** For every semiring $R$ there is a
  [ring homomorphism from $\mathbb{N}$ to $R$ sending $n$ to $n \cdot 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Cast/Basic.html#Nat.castRingHom),
  and [any two ring homomorphisms from $\mathbb{N}$ to $R$ are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Cast/Basic.html#ext_nat).
  So $\mathbb{N}$ is the initial object among semirings: it maps to every
  semiring by exactly one homomorphism.
- **Ordinals and cardinals.** In the set-theoretic model above, the natural
  numbers are exactly the finite [ordinals](../../logic-and-computation/set-theory/ordinals/ordinal.md), and they also serve as
  the finite [cardinals](../../logic-and-computation/set-theory/cardinals/cardinal.md).

## In Mathlib

The natural numbers are [defined](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Nat) in Lean's core library as an
inductive type with two constructors, zero and successor. Lean generates the
recursion principle together with this definition, so nothing has to be
postulated as an axiom; induction is that recursion principle applied to a
family of propositions, and the other two Peano axioms are theorems. The kernel computes with natural numbers using
arbitrary-precision arithmetic. Zero is a natural number, and the
[positive natural numbers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/PNat/Notation.html#PNat) form a separate type. The operations are
total, with conventions for the cases where the textbook operation is undefined:
subtraction is truncated, so that [$m - n = 0$ exactly when $m \le n$](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Nat/Lemmas.html#Nat.sub_eq_zero_iff_le)
(for instance $3 - 5 = 0$); division rounds down, and
[division by zero gives $0$](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Nat/Div/Basic.html#Nat.div_zero), while
[the remainder of $a$ on division by zero is $a$](https://leanprover-community.github.io/mathlib4_docs/Init/Data/Nat/Div/Basic.html#Nat.mod_zero). Statements
that need genuine subtraction carry a hypothesis such as $n \le m$, or pass to the
integers. Mathlib reads a natural number as an element of any semiring through
the cast $n \mapsto n \cdot 1$, which the map above bundles as a ring
homomorphism; this is how numerals such as $2$ make sense in every ring.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Nat`](https://leanprover-community.github.io/mathlib4_docs/Init/Prelude.html#Nat)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L21)
- [Mathlib undergraduate list: Single Variable Real Analysis › Sequences of real numbers](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L286)
- [Freek Wiedijk's 100 theorems, no. 74](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/100.yaml#L374)
