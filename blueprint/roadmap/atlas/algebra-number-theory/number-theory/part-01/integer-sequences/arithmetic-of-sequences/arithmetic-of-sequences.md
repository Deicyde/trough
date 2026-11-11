---
declaration: section
origin: cited
lean: MetaMathlibExt.multipleCountingJacobsthalSequence, MetaMathlibExt.oddLichtenberg, MetaMathlibExt.generalized_euclid_sequence_contains_every_prime
statement: formalized
proof: formalized
---

# Arithmetic properties of sequences: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/index.html).

Dold, Newton and realizable sequences, Sylvester, Euclid and Göbel sequences, gcd and divisibility sequences, OEIS-specific sequences.

## Multiple-counting Jacobsthal sequence

For natural numbers $x$, $\rho$ and $n$, the
multiple-counting Jacobsthal sequence $J_{x,\rho}(n)$ is the number of multiples of $\rho$ strictly
between $x^n$ and $x^{n+1}$, that is, the number of natural numbers $k$ with $x^n < k < x^{n+1}$
and $\rho \mid k$.

The source studies $2 \le x$ and $2 \le \rho$; the count itself is useful without those
restrictions.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL19/Cilasun/cila5.tex>.

Formalized by `MetaMathlibExt.multipleCountingJacobsthalSequence`, a definition declared in [MathlibExt/NumberTheory/MultipleCountingJacobsthalSequence.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/MultipleCountingJacobsthalSequence.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/index.html#multiple-counting-jacobsthal-sequence).

## Odd Lichtenberg numbers

The odd Lichtenberg numbers form the sequence $(a_n)_{n \ge 0}$
of natural numbers defined by $a_0 = 1$ and $a_{n+1} = 4 a_n + 1$, so the sequence begins
$1, 5, 21, 85, \dots$; these are the positive terms of OEIS A002450.

Equivalently, it is the self-generating sequence with seed $1$ and generating function
$k \mapsto 4k + 1$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL25/Hinz/hinz5.tex>.

Formalized by `MetaMathlibExt.oddLichtenberg`, a definition declared in [MathlibExt/NumberTheory/OddLichtenbergNumbers.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/OddLichtenbergNumbers.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/index.html#odd-lichtenberg).

## Some generalized Euclid sequence contains every prime

Let $P$ be a finite set of primes
and let $k$ be the number of elements of $P$. Then there is an injective sequence
$a_0, a_1, a_2, \dots$ of primes such that $a_0, \dots, a_{k-1}$ are exactly the elements of $P$,
every prime occurs in the sequence, and for every $n \ge k$ there is a set
$I \subseteq \{0, \dots, n-1\}$ such that $a_n$ divides

$$\prod_{i \in I} a_i + \prod_{i \in \{0, \dots, n-1\} \setminus I} a_i.$$

This is an existence claim over all choices of $I$ and of the prime divisor, unlike the open
Euclid–Mullin conjecture about one specific sequence. For distinct primes $p_1, \dots, p_r$ and
any $J \subseteq \{1, \dots, r\}$, the number
$\prod_{i \in J} p_i + \prod_{i \in \{1, \dots, r\} \setminus J} p_i$ is coprime to
$p_1 \cdots p_r$, so a prime divisor of it is always new.

Proof: Booker's residue-set route, with an elementary squarefree count in place of Rogers'
density bound and Jacobi-sum character-sum bounds in place of the Hasse and Weil bounds.

## Sources

- Andrew R. Booker, "A Variant of the Euclid-Mullin Sequence Containing Every Prime," Journal of Integer Sequences 19 (2016), Article 16.6.4, Theorem, lines 132–136, https://cs.uwaterloo.ca/journals/JIS/VOL19/Booker/book3.tex

Formalized by `MetaMathlibExt.generalized_euclid_sequence_contains_every_prime`, a theorem declared in [MathlibExt/NumberTheory/Sequences/GeneralizedEuclidSequence.lean, line 2576](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Sequences/GeneralizedEuclidSequence.lean#L2576). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/index.html#generalized-euclid-sequence-contains-eve).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic properties of sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences)
