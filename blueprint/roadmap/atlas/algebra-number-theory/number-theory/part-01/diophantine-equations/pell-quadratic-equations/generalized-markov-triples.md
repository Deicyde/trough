---
declaration: section
origin: cited
lean: MetaMathlibExt.IsGenMarkovTriple, MetaMathlibExt.isGenMarkovTriple_one_one_one, MetaMathlibExt.isGenMarkovTriple_zero_one_one_two, MetaMathlibExt.IsGenMarkovNumber, MetaMathlibExt.HasUniqueMaxGenMarkovTriple, MetaMathlibExt.HasUniqueMaxGenMarkovTriple.isGenMarkovNumber, MetaMathlibExt.genMarkovCongruenceCount, MetaMathlibExt.genMarkovCongruenceCount_zero_five
statement: formalized
---

# Generalized Markov triples

85 results, 40 proved and 45 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html).

## Generalized Markov triple

For a natural number $k$, a $k$-generalized Markov triple
is a triple $(a, b, c)$ of positive integers satisfying the $k$-generalized Markov equation
$\mathrm{GME}(k)$:

$$a^2 + b^2 + c^2 + k(bc + ca + ab) = (3 + 3k)abc.$$

For $k = 0$ these are the classical Markov triples.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 1.2.

Formalized by `MetaMathlibExt.IsGenMarkovTriple`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-triple).

## $(1, 1, 1)$ is a generalized Markov triple

For every natural number $k$, the triple
$(1, 1, 1)$ is a $k$-generalized Markov triple.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 1.2.

Formalized by `MetaMathlibExt.isGenMarkovTriple_one_one_one`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-triple-one-one-one).

## The Markov triple $(1, 1, 2)$

The triple $(1, 1, 2)$ is a $0$-generalized Markov
triple, that is, a classical Markov triple: $1^2 + 1^2 + 2^2 = 3 \cdot 1 \cdot 1 \cdot 2$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 1.1.

Formalized by `MetaMathlibExt.isGenMarkovTriple_zero_one_one_two`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-triple-zero-one-one-two).

## Generalized Markov number

Let $k$ be a natural number. A natural number $b$ is a
$k$-generalized Markov number when there are natural numbers $a$ and $c$ such that
$(a, b, c)$ is a $k$-generalized Markov triple.

Since the $k$-generalized Markov equation is symmetric in its three variables, this is the same
as $b$ being an entry, in any position, of some $k$-generalized Markov triple.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 1.2.

Formalized by `MetaMathlibExt.IsGenMarkovNumber`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-number).

## Unique maximal generalized Markov triple

Let $k$ and $b$ be natural numbers. The number
$b$ is the maximum of a unique $k$-generalized Markov triple up to order if there is a
$k$-generalized Markov triple $(a, b, c)$ with $a \le b$ and $c \le b$, and every
$k$-generalized Markov triple $(a', b, c')$ with $a' \le b$ and $c' \le b$ satisfies
$(a', c') = (a, c)$ or $(a', c') = (c, a)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Conjecture 1.8.

Formalized by `MetaMathlibExt.HasUniqueMaxGenMarkovTriple`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#has-unique-max-gen-markov-triple).

## A unique maximum is a generalized Markov number

Let $k$ and $b$ be natural numbers.
If $b$ is the maximum of a unique $k$-generalized Markov triple up to order, then $b$ is a
$k$-generalized Markov number.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Conjecture 1.8.

Formalized by `MetaMathlibExt.HasUniqueMaxGenMarkovTriple.isGenMarkovNumber`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-number-2).

## Number of solutions of $x^2 + kx + 1 \equiv 0 \pmod b$

For natural numbers $k$ and
$b$, this is the number of integers $x$ with $0 \le x < b$ such that $b$ divides
$x^2 + kx + 1$. For $b = 0$ it is $0$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.5.

Formalized by `MetaMathlibExt.genMarkovCongruenceCount`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-congruence-count).

## The congruence $x^2 + 1 \equiv 0 \pmod 5$ has two solutions

Exactly two integers $x$
with $0 \le x < 5$ satisfy $x^2 + 1 \equiv 0 \pmod 5$.

They are $x = 2$ and $x = 3$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.2.

Formalized by `MetaMathlibExt.genMarkovCongruenceCount_zero_five`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-congruence-count-zero-five).

## Uniqueness criterion via the congruence $x^2 + kx + 1 \equiv 0 \pmod{b}$

Let $k$ be a
natural number and let $b$ be a $k$-generalized Markov number with $b \ne 1$ and $b \ne k + 2$.
If the congruence $x^2 + kx + 1 \equiv 0 \pmod{b}$ has at most two solutions $x$ with
$0 \le x < b$, then $b$ is the maximum of a unique $k$-generalized Markov triple up to order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.5.

Stated but not proved: `MetaMathlibExt.hasUniqueMaxGenMarkovTriple_of_congruenceCount_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#has-unique-max-gen-markov-triple-of-cong).

## Generalized Markov numbers $p$ and $2p$ are unique maxima

Let $k$ be a natural number
and $p$ a prime. If $b$ is a $k$-generalized Markov number with $b = p$ or $b = 2p$, then $b$ is
the maximum of a unique $k$-generalized Markov triple up to order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.6.

Stated but not proved: `MetaMathlibExt.hasUniqueMaxGenMarkovTriple_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#has-unique-max-gen-markov-triple-prime).

## Uniqueness for prime powers $p^m$ and $2p^m$ under conditions on $k$

Let $k$ and $m$ be
natural numbers with $m \ge 2$ and let $p$ be a prime. Suppose that $k = 2$; or that $k \ge 4$ is
even and $p^2$ divides neither $k/2 + 1$ nor $k/2 - 1$; or that $k$ is odd and $p^2$ divides
neither $k + 2$ nor $k - 2$ in $\mathbb{Z}$. If $b$ is a $k$-generalized Markov number with
$b = p^m$ or $b = 2p^m$, then $b$ is the maximum of a unique $k$-generalized Markov triple up to
order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.7.

Stated but not proved: `MetaMathlibExt.hasUniqueMaxGenMarkovTriple_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#has-unique-max-gen-markov-triple-prime-p).

## Uniqueness for odd prime powers $p^m$ and $2p^m$ with $p \nmid k^2 - 4$

Let $k$ and $m$
be natural numbers with $m \ge 2$, and let $p$ be an odd prime that does not divide $k^2 - 4$ in
$\mathbb{Z}$. If $b$ is a $k$-generalized Markov number with $b = p^m$ or $b = 2p^m$, then $b$ is
the maximum of a unique $k$-generalized Markov triple up to order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 4.10.

Stated but not proved: `MetaMathlibExt.hasUniqueMaxGenMarkovTriple_odd_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#has-unique-max-gen-markov-triple-odd-pri).

## Bound on the number of generalized Markov triples with a given maximum

Let $k$ be a
natural number such that either $k \ge 4$ is even and $k/2 + 1$ and $k/2 - 1$ are squarefree,
or $k$ is odd and the integers $k + 2$ and $k - 2$ are squarefree. Let $b$ be a $k$-generalized
Markov number that is not divisible by $4$, and suppose that the number $n$ of odd primes
dividing $b$ is at least $1$; equivalently, $b = p_1^{a_1} \cdots p_n^{a_n}$ or
$b = 2 p_1^{a_1} \cdots p_n^{a_n}$ for distinct odd primes $p_1, \dots, p_n$ with $n \ge 1$.
Then there are at most $2^{n-1}$ pairs of natural numbers $(a, c)$ with $a \le c \le b$ such
that $(a, b, c)$ is a $k$-generalized Markov triple; that is, $b$ is the maximum of at most
$2^{n-1}$ such triples up to order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 4.20.

Stated but not proved: `MetaMathlibExt.card_maxGenMarkovTriples_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#card-max-gen-markov-triples-le).

## Generalized Markov triples are pairwise coprime

If $(a, b, c)$ is a $k$-generalized
Markov triple, then $\gcd(a, b) = \gcd(b, c) = \gcd(a, c) = 1$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 2.3 (citing Gyoda and Matsushita, Corollary 8).

Stated but not proved: `MetaMathlibExt.IsGenMarkovTriple.pairwise_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#pairwise-coprime).

## The generalized Markov equation and the generalized second Markov equation

Let
$k \in \mathbb{N}$ and let $a, b, c$ be rational numbers. Put $x = (3 + 3k)a - k$,
$y = (3 + 3k)b - k$ and $z = (3 + 3k)c - k$. Then
$a^2 + b^2 + c^2 + k(bc + ca + ab) = (3 + 3k)abc$ if and only if
$x^2 + y^2 + z^2 + (k^2 + 2k)(x + y + z) + 2k^3 + 3k^2 = xyz$. The first equation is the
$k$-generalized Markov equation $\mathrm{GME}(k)$ and the second the $k$-generalized second
Markov equation $\mathrm{GSME}(k)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 2.4.

Stated but not proved: `MetaMathlibExt.genMarkov_iff_genSecondMarkov` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-iff-gen-second-markov).

## Vieta jumping for the second generalized Markov equation

Let $k$ be a natural number
and let $a, b, c$ be integers with

$$a^2 + b^2 + c^2 + (k^2 + 2k)(a + b + c) + 2k^3 + 3k^2 = abc.$$

Then the triples $(a, ab - c - k^2 - 2k, b)$ and $(b, bc - a - k^2 - 2k, c)$ satisfy the same
equation.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 2.6.

Stated but not proved: `MetaMathlibExt.genSecondMarkov_vieta` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-second-markov-vieta).

## Trace identities in $\mathrm{SL}(2, \mathbb{Z})$

For all $A, B \in \mathrm{SL}(2,
\mathbb{Z})$ we have $\operatorname{tr} A = \operatorname{tr} A^{-1}$,
$\operatorname{tr}(AB) = \operatorname{tr} A \cdot \operatorname{tr} B -
\operatorname{tr}(AB^{-1})$, and $A^2 = (\operatorname{tr} A) A - I$, where $I$ is the
identity matrix.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 3.6 (citing Aigner, Lemma 4.2).

Stated but not proved: `MetaMathlibExt.specialLinearGroup_two_trace_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#special-linear-group-two-trace-identitie).

## At most two solutions of $x^2 + kx + 1 \equiv 0$ modulo a prime

For every prime $p$
and every $k \in \mathbb{N}$, at most two integers $x$ with $0 \le x < p$ satisfy
$x^2 + kx + 1 \equiv 0 \pmod p$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.9.

Stated but not proved: `MetaMathlibExt.genMarkovCongruenceCount_prime_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-congruence-count-prime-le-two).

## At most two solutions of $x^2 + kx + 1 \equiv 0$ modulo an odd prime power

Let $p$
be an odd prime, let $m \ge 2$ and let $k \in \mathbb{N}$ with $k^2 - 4 \not\equiv 0 \pmod p$.
Then at most two integers $x$ with $0 \le x < p^m$ satisfy
$x^2 + kx + 1 \equiv 0 \pmod{p^m}$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.11.

Stated but not proved: `MetaMathlibExt.genMarkovCongruenceCount_prime_pow_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-congruence-count-prime-pow-le).

## An even generalized Markov number forces $k$ to be even

Let $k$ be a natural number. If
some $k$-generalized Markov number $b$ is even, then $k$ is even.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.13.

Stated but not proved: `MetaMathlibExt.even_of_even_genMarkovNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#even-of-even-gen-markov-number).

## Generalized Markov numbers divisible by $4$

Let $k$ be a natural number. If some
$k$-generalized Markov number is divisible by $4$, then $k \equiv 2 \pmod{4}$.

## Sources

- Only the first claim of Proposition 4.14 is stated; its "in particular" parity consequence is omitted because its displayed fraction is garbled in the record.
- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 4.14.

Stated but not proved: `MetaMathlibExt.mod_four_eq_two_of_four_dvd_genMarkovNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#mod-four-eq-two-of-four-dvd-gen-markov-n).

## Large odd primes do not divide $k^2 - 4$

Let $p$ be an odd prime and $k$ a natural
number. If either $k \ge 4$ is even and $p > k/2 + 1$, or $k$ is odd and $p > k + 2$, then $p$
does not divide $k^2 - 4$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 4.15.

Stated but not proved: `MetaMathlibExt.not_dvd_sq_sub_four_of_large_prime` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#not-dvd-sq-sub-four-of-large-prime).

## Discriminant condition for prime-power generalized Markov numbers

Let $p$ be an odd
prime and $m \ge 2$, and suppose that some $k$-generalized Markov number $b$ equals $p^m$ or
$2p^m$. Suppose moreover that either $k \ge 4$ is even and $p^2$ divides neither $k/2 + 1$ nor
$k/2 - 1$, or $k$ is odd and $p^2$ divides neither $k + 2$ nor $k - 2$. Then $p$ does not
divide $k^2 - 4$.

As printed (without the Markov-number hypothesis) Proposition 4.16 is false: $k = 4$, $p = 3$
satisfy the divisibility conditions ($9 \nmid 3$, $9 \nmid 1$) but $3 \mid 12$; the paper's
proof assumes $b = p^m$ is a $k$-generalized Markov number and uses $m \ge 2$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 4.16 and its proof.

Stated but not proved: `MetaMathlibExt.not_dvd_sq_sub_four_of_genMarkovNumber_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#not-dvd-sq-sub-four-of-gen-markov-number).

## 2-generalized Markov triples are squares of Markov triples

If $(a, b, c)$ is a Markov
triple, that is, a $0$-generalized Markov triple, then $(a^2, b^2, c^2)$ is a $2$-generalized
Markov triple. Conversely, for every $2$-generalized Markov triple $(A, B, C)$ there is a Markov
triple $(a, b, c)$ with $A = a^2$, $B = b^2$ and $C = c^2$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 4.17 (citing Gyoda and Matsushita, Theorem 2.9).

Stated but not proved: `MetaMathlibExt.genMarkovTriple_two_iff_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-triple-two-iff-sq).

## Uniqueness criterion for classical Markov numbers

Let $b \ne 1, 2$ be a Markov number
(a $0$-generalized Markov number). If the congruence $x^2 + 1 \equiv 0 \pmod{b}$ has at most
two solutions $x$ with $0 \le x < b$, then $b$ is the maximum of a unique Markov triple up to
order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.2 (citing Aigner, Corollary 3.17).

Stated but not proved: `MetaMathlibExt.markov_hasUniqueMaxTriple_of_congruenceCount_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#markov-has-unique-max-triple-of-congruen).

## Uniqueness for Markov numbers $p^m$ and $2p^m$ with $p$ an odd prime

Let $p$ be an odd
prime and $m \ge 1$. If $b = p^m$ or $b = 2p^m$ is a Markov number (a $0$-generalized Markov
number), then $b$ is the maximum of a unique Markov triple up to order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.3 (citing Aigner, Corollary 3.20).

Stated but not proved: `MetaMathlibExt.markov_hasUniqueMaxTriple_odd_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#markov-has-unique-max-triple-odd-prime-p).

## Markov triples with a common characteristic number agree up to order

Let $m \ge 5$
and let $(m, m_2, m_3)$ and $(m, n_2, n_3)$ be Markov triples (that is, $0$-generalized Markov
triples) with $m_2, m_3, n_2, n_3 \le m$. Suppose some integer $x$ with $0 < x < m$ satisfies
$m_2 x \equiv \pm m_3 \pmod{m}$ and $n_2 x \equiv \pm n_3 \pmod{m}$, where the two signs are
chosen independently. Then $(m_2, m_3) = (n_2, n_3)$ or $(m_2, m_3) = (n_3, n_2)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 1.11 (citing Aigner, Proposition 3.15).

Stated but not proved: `MetaMathlibExt.markov_eq_of_characteristic_number_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#markov-eq-of-characteristic-number-eq).

## Vieta jumping of generalized Markov triples

For a natural number $k$, the left Vieta
jumping sends a triple $(a, b, c)$ of natural numbers to
$(a, \lfloor (a^2 + kab + b^2)/c \rfloor, b)$ and the right Vieta jumping sends it to
$(b, \lfloor (b^2 + kbc + c^2)/a \rfloor, c)$, where division by $0$ gives $0$. The left jumping
is indexed by the boolean value false and the right one by true.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.genMarkovVieta`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-vieta).

## The wide generalized Markov tree

Fix a natural number $k$. The wide $k$-generalized
Markov tree $\mathrm{WMT}(k)$ is the binary tree of triples of natural numbers with root
$(1, 1, 1)$ in which a vertex $(a, b, c)$ has left child
$(a, \lfloor (a^2 + kab + b^2)/c \rfloor, b)$ and right child
$(b, \lfloor (b^2 + kbc + c^2)/a \rfloor, c)$, the left and right Vieta jumpings. For a path $w$,
a finite sequence of left and right steps, the vertex of $\mathrm{WMT}(k)$ at $w$ is the triple
reached from the root by taking the steps of $w$ in order; the empty path gives the root.

The quotients are divisions of natural numbers, rounded down, with division by $0$ giving $0$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.wideGenMarkovTree`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-markov-tree).

## Generalized Markov tree

For a natural number $k$ and a finite sequence $w$ of left and
right steps, the vertex of the $k$-generalized Markov tree $MT(k)$ at $w$ is the vertex of the
wide $k$-generalized Markov tree $WMT(k)$ reached from its root by one left step followed by the
steps of $w$ in order. Thus $MT(k)$ is the full subtree of $WMT(k)$ rooted at the left child of
the root.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.genMarkovTree`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-tree).

## Children in the wide generalized Markov tree are Vieta jumpings

For every natural
number $k$, every path $w$ and every direction $d$ (left or right), the vertex of the wide
$k$-generalized Markov tree $\mathrm{WMT}(k)$ at the path $w$ followed by one step in direction
$d$ is the image of the vertex at $w$ under the Vieta jumping in direction $d$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.wideGenMarkovTree_append_singleton`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-markov-tree-append-singleton).

## Root of the generalized Markov tree

For every natural number $k$, the root of the
$k$-generalized Markov tree $MT(k)$, its vertex at the empty path, is $(1, k + 2, 1)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 4.

Formalized by `MetaMathlibExt.genMarkovTree_nil`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 351](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L351). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-tree-nil).

## Left child of the root of the classical Markov tree

For $k = 0$, the vertex of the
Markov tree $MT(0)$ reached from the root by one left step is $(1, 5, 2)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.genMarkovTree_zero_false`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-tree-zero-false).

## Generalized Markov triples in the wide Markov tree

Let $k$ be a natural number. Every
vertex of the wide $k$-generalized Markov tree $\mathrm{WMT}(k)$ is a $k$-generalized Markov
triple. Moreover, every $k$-generalized Markov triple $(a, b, c)$ with $a < b$ and $c < b$ is
the vertex of $\mathrm{WMT}(k)$ at exactly one path that starts with a left step, and at exactly
one path that starts with a right step.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 2.1 (citing Gyoda and Matsushita, Theorem 1).

Stated but not proved: `MetaMathlibExt.wideGenMarkovTree_isGenMarkovTriple_and_twice` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-markov-tree-is-gen-markov-tripl).

## Vertices of the generalized Markov tree

For every natural number $k$, every vertex of
the $k$-generalized Markov tree $MT(k)$ is a $k$-generalized Markov triple, and for every
$k$-generalized Markov triple $(a, b, c)$ with $a < b$ and $c < b$ there is exactly one path $w$
such that the vertex of $MT(k)$ at $w$ is $(a, b, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 2.2.

Stated but not proved: `MetaMathlibExt.genMarkovTree_isGenMarkovTriple_and_once` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-tree-is-gen-markov-triple-and).

## Vieta jumping identities for generalized Markov triples

If $(a, b, c)$ is a
$k$-generalized Markov triple, then, as integers,
$a^2 + kab + b^2 = c\,((3 + 3k)ab - c - k(a + b))$ and
$b^2 + kbc + c^2 = a\,((3 + 3k)bc - a - k(b + c))$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2 (display after Corollary 2.2).

Stated but not proved: `MetaMathlibExt.IsGenMarkovTriple.vieta_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#vieta-eq).

## Induced solution of the generalized second Markov equation

For a natural number $k$,
a triple $(a, b, c)$ of integers is an induced positive solution of the $k$-generalized second
Markov equation $\mathrm{GSME}(k)$ when $a, b, c > 0$,

$$a^2 + b^2 + c^2 + (k^2 + 2k)(a + b + c) + 2k^3 + 3k^2 = abc,$$

and $3 + 3k$ divides each of $a + k$, $b + k$ and $c + k$.

Equivalently, $(a + k)/(3 + 3k)$, $(b + k)/(3 + 3k)$ and $(c + k)/(3 + 3k)$ are integers; they
are automatically positive since $a, b, c > 0$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.IsInducedGenSecondMarkovSolution`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-induced-gen-second-markov-solution).

## The root induced solution of the generalized second Markov equation

For every natural
number $k$, the triple $(3 + 2k, 3 + 2k, 3 + 2k)$, the image of $(1, 1, 1)$ under
$x \mapsto (3 + 3k)x - k$, is an induced positive solution of the $k$-generalized second
Markov equation $\mathrm{GSME}(k)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 2.

Formalized by `MetaMathlibExt.isInducedGenSecondMarkovSolution_root`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-induced-gen-second-markov-solution-ro).

## Vieta jumping preserves induced solutions of the generalized second Markov equation

If
$(a, b, c)$ is an induced solution of the $k$-generalized second Markov equation
$\mathrm{GSME}(k)$, then so are $(a, ab - c - k^2 - 2k, b)$ and $(b, bc - a - k^2 - 2k, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 2.7.

Stated but not proved: `MetaMathlibExt.IsInducedGenSecondMarkovSolution.vieta` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#vieta).

## Vertices of the second generalized Markov tree

For a natural number $k$, let $SMT(k)$
be the tree obtained from the $k$-generalized Markov tree $MT(k)$ by replacing each vertex
$(a, b, c)$ with the integer triple $((3 + 3k)a - k, (3 + 3k)b - k, (3 + 3k)c - k)$. Every vertex
of $SMT(k)$ is an induced solution of the $k$-generalized second Markov equation, and for every
induced solution $(a, b, c)$ with $a < b$ and $c < b$ there is exactly one path $w$ such that the
vertex of $SMT(k)$ at $w$ is $(a, b, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 2.8.

Stated but not proved: `MetaMathlibExt.genSecondMarkovTree_induced_and_once` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-second-markov-tree-induced-and-once).

## The matrix $S$ of the generalized Cohn triple relation

For a natural number $k$, $S$
is the $2 \times 2$ integer matrix

$$S = \begin{pmatrix} k & 0 \\ 3k^2 + 3k & k \end{pmatrix}.$$

It is the matrix in the relation $Q = PR - S$ that defines $k$-generalized Cohn triples.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Definition 3.2.

Formalized by `MetaMathlibExt.genCohnS`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-s).

## The matrix $S$ vanishes for $k = 0$

For $k = 0$, the matrix $S$ of the generalized
Cohn triple relation is the zero $2 \times 2$ matrix, so the relation $Q = PR - S$ reduces to
the classical Cohn relation $Q = PR$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 1.3.

Formalized by `MetaMathlibExt.genCohnS_zero`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-s-zero).

## Generalized Cohn matrices

Let $k$ be a natural number. An integer $2 \times 2$ matrix
$P = (p_{ij})$ is a $k$-generalized Cohn matrix if $\det P = 1$, its entry $p_{12}$ is a
$k$-generalized Markov number, and its trace equals $(3 + 3k) p_{12} - k$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Definition 3.1.

Formalized by `MetaMathlibExt.IsGenCohnMatrix`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 470](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L470). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-cohn-matrix).

## Generalized Cohn triple

Let $k$ be a natural number and let $S$ be the integer matrix
with rows $(k, 0)$ and $(3k^2 + 3k, k)$. A triple $(P, Q, R)$ of integer $2 \times 2$ matrices is
a $k$-generalized Cohn triple associated with natural numbers $(a, b, c)$ when $P$, $Q$ and $R$
are $k$-generalized Cohn matrices, $Q = PR - S$, the $(1, 2)$-entries of $P$, $Q$ and $R$ are
$a$, $b$ and $c$ respectively, and $(a, b, c)$ is a $k$-generalized Markov triple.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Definition 3.2.

Formalized by `MetaMathlibExt.IsGenCohnTriple`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-cohn-triple).

## Generalized Cohn triples give generalized Markov triples

Let $k$ be a natural number.
If $(P, Q, R)$ is a $k$-generalized Cohn triple associated with $(a, b, c)$, then $(a, b, c)$ is
a $k$-generalized Markov triple.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Definition 3.2.

Formalized by `MetaMathlibExt.IsGenCohnTriple.isGenMarkovTriple`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-triple-2).

## The matrix $P_{1;\ell}$

For a natural number $k$ and an integer $\ell$, $P_{1;\ell}$ is
the integer $2 \times 2$ matrix with first row $(\ell, 1)$ and second row
$(-\ell^2 + 2k\ell + 3\ell - 1, -\ell + 2k + 3)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.genCohnP1`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 496](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L496). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-p1).

## The matrix $Q_{1;\ell}$

For a natural number $k$ and an integer $\ell$, $Q_{1;\ell}$ is
the $2 \times 2$ integer matrix

$$\begin{pmatrix} k + \ell + 1 & 1 \\ k^2 - \ell^2 + 3k + \ell + 1 & k - \ell + 2 \end{pmatrix}.$$

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.genCohnQ1`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-q1).

## The matrix $R_{1;\ell}$

For a natural number $k$ and an integer $\ell$, $R_{1;\ell}$ is
the $2 \times 2$ integer matrix

$$\begin{pmatrix} 2k + \ell + 2 & 1 \\ -\ell^2 - 2k\ell + 2k - \ell + 1 & -\ell + 1 \end{pmatrix}.$$

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.genCohnR1`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 510](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L510). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-r1).

## The matrices $P_{1;\ell}$, $Q_{1;\ell}$ and $R_{1;\ell}$ have determinant $1$

For every
natural number $k$ and every integer $\ell$, the $2 \times 2$ integer matrices $P_{1;\ell}$,
$Q_{1;\ell}$ and $R_{1;\ell}$ (which depend on $k$) all have determinant $1$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.genCohnPQR1_det`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 517](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L517). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-pqr1-det).

## One step of the wide generalized Cohn tree

Fix a natural number $k$ and let $S$ be the
matrix of the $k$-generalized Cohn triple relation. On triples $(P, Q, R)$ of $2 \times 2$
integer matrices, the left step (encoded by the Boolean false) sends $(P, Q, R)$ to its left
child $(P, PQ - S, Q)$, and the right step (encoded by true) sends it to its right child
$(Q, QR - S, R)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.genCohnStep`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 527](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L527). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-step).

## Paths of generalized Cohn steps

Fix a natural number $k$ and let $S$ be the integer
$2 \times 2$ matrix with rows $(k, 0)$ and $(3k^2 + 3k, k)$. For a triple $T$ of integer
$2 \times 2$ matrices and a path $w$, a finite sequence of left and right moves, this is the
triple obtained from $T$ by applying the moves of $w$ in order, where a left move sends
$(P, Q, R)$ to $(P, PQ - S, Q)$ and a right move sends $(P, Q, R)$ to $(Q, QR - S, R)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.10.

Formalized by `MetaMathlibExt.genCohnPath`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 537](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L537). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-path).

## The wide generalized Cohn tree

Fix a natural number $k$ and an integer $\ell$, and let
$S = \begin{pmatrix} k & 0 \\ 3k^2 + 3k & k \end{pmatrix}$. The wide $k$-generalized Cohn tree
$\mathrm{WGCT}(k, \ell)$ is the binary tree of triples of $2 \times 2$ integer matrices whose
root is $(P_{1;\ell}, Q_{1;\ell}, R_{1;\ell})$, where

$$P_{1;\ell}=\begin{pmatrix}\ell & 1\\ -\ell^2+2k\ell+3\ell-1 & -\ell+2k+3\end{pmatrix},$$



$$Q_{1;\ell}=\begin{pmatrix}k+\ell+1 & 1\\ k^2-\ell^2+3k+\ell+1 & k-\ell+2\end{pmatrix},$$



$$R_{1;\ell}=\begin{pmatrix}2k+\ell+2 & 1\\ -\ell^2-2k\ell+2k-\ell+1 & -\ell+1\end{pmatrix},$$

and in which a vertex $(P, Q, R)$ has left child $(P, PQ - S, Q)$ and right child
$(Q, QR - S, R)$. For a path $w$, a finite sequence of left and right steps, the vertex of
$\mathrm{WGCT}(k, \ell)$ at $w$ is the triple reached from the root by taking the steps of $w$ in
order; the empty path gives the root.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.wideGenCohnTree`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-cohn-tree).

## The $k$-generalized Cohn tree

For $k \in \mathbb{N}$ and $\ell \in \mathbb{Z}$, the
$k$-generalized Cohn tree $\mathrm{GCT}(k, \ell)$ is the full subtree of the wide
$k$-generalized Cohn tree $\mathrm{WGCT}(k, \ell)$ rooted at the left child of its root. For a
finite sequence $w$ of left and right moves, this is the vertex of $\mathrm{GCT}(k, \ell)$
reached from its root along $w$, that is, the vertex of $\mathrm{WGCT}(k, \ell)$ reached from
the root of $\mathrm{WGCT}(k, \ell)$ by one left move followed by the moves of $w$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.genCohnTree`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 557](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L557). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-tree).

## Children in the wide generalized Cohn tree

Let $k$ be a natural number, $\ell$ an
integer, and $S$ the integer matrix with rows $(k, 0)$ and $(3k^2 + 3k, k)$. For every path $w$
in the wide $k$-generalized Cohn tree $\mathrm{WGCT}(k, \ell)$, if $(P, Q, R)$ is the vertex at
$w$, then the vertex at $w$ followed by a left step is $(P, PQ - S, Q)$ and the vertex at $w$
followed by a right step is $(Q, QR - S, R)$; that is, each child is obtained from its parent by
one generalized Cohn step.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.1.

Formalized by `MetaMathlibExt.wideGenCohnTree_append_singleton`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-cohn-tree-append-singleton).

## Cohn steps reach every classical Cohn triple whose middle entry is largest

Call a
$0$-generalized Cohn triple a Cohn triple; for $k = 0$ the matrix $S$ of the generalized Cohn
relation is zero, so the relation reads $Q = PR$. Call $(P, Q, R) \mapsto (P, PQ, Q)$ the left
step and $(P, Q, R) \mapsto (Q, QR, R)$ the right step. First, if $(P, Q, R)$ is a Cohn triple
associated with $(a, b, c)$ and $a \le b$, $c \le b$, then $(P, Q, R)$ is obtained by applying
finitely many left and right steps to some Cohn triple associated with $(1, 1, 1)$. Second, if
$(P, Q, R)$ is a Cohn triple associated with $(a, b, c)$, then the $(1, 2)$-entries of the left
step $(P, PQ, Q)$ are $(a, \lfloor (a^2 + b^2)/c \rfloor, b)$ and those of the right step
$(Q, QR, R)$ are $(b, \lfloor (b^2 + c^2)/a \rfloor, c)$: on $(1, 2)$-entries the steps are the
left and right Vieta jumpings of the Markov triple $(a, b, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.9 (citing Aigner, Theorem 4.7).

Stated but not proved: `MetaMathlibExt.cohnTriple_reachable` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 577](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L577). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#cohn-triple-reachable).

## Cohn steps reach every generalized Cohn triple whose middle entry is largest

Let
$k \in \mathbb{N}$ and let $S$ be the integer matrix with rows $(k, 0)$ and $(3k^2 + 3k, k)$.
Call $(P, Q, R) \mapsto (P, PQ - S, Q)$ the left step and $(P, Q, R) \mapsto (Q, QR - S, R)$ the
right step. First, if $(P, Q, R)$ is a $k$-generalized Cohn triple associated with $(a, b, c)$
and $a \le b$, $c \le b$, then $(P, Q, R)$ is obtained by applying finitely many left and
right steps to some $k$-generalized Cohn triple associated with $(1, 1, 1)$. Second, if
$(P, Q, R)$ is a $k$-generalized Cohn triple associated with $(a, b, c)$, then the
$(1, 2)$-entries of the left step $(P, PQ - S, Q)$ are
$(a, \lfloor (a^2 + kab + b^2)/c \rfloor, b)$ and those of the right step $(Q, QR - S, R)$ are
$(b, \lfloor (b^2 + kbc + c^2)/a \rfloor, c)$: on $(1, 2)$-entries the steps are the left and
right Vieta jumpings of $(a, b, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 1.10.

Stated but not proved: `MetaMathlibExt.genCohnTriple_reachable` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 592](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L592). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-triple-reachable).

## Generalized Cohn triples associated with $(1, 1, 1)$

Let $k$ be a natural number.
For an integer $\ell$, let $P_{1;\ell}$ be the integer matrix with rows $(\ell, 1)$ and
$(-\ell^2 + 2k\ell + 3\ell - 1, -\ell + 2k + 3)$, let $Q_{1;\ell}$ be the one with rows
$(k + \ell + 1, 1)$ and $(k^2 - \ell^2 + 3k + \ell + 1, k - \ell + 2)$, and let $R_{1;\ell}$ be
the one with rows $(2k + \ell + 2, 1)$ and $(-\ell^2 - 2k\ell + 2k - \ell + 1, -\ell + 1)$.
Then for every integer $\ell$, $(P_{1;\ell}, Q_{1;\ell}, R_{1;\ell})$ is a $k$-generalized Cohn
triple associated with $(1, 1, 1)$. Conversely, if $(P, Q, R)$ is a $k$-generalized Cohn triple
associated with $(1, 1, 1)$, then there is an integer $\ell$ with $P = P_{1;\ell}$,
$Q = Q_{1;\ell}$ and $R = R_{1;\ell}$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 3.4.

Stated but not proved: `MetaMathlibExt.isGenCohnTriple_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 606](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L606). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-cohn-triple-one-iff).

## Children of a generalized Cohn triple

Let $k$ be a natural number, let $S$ be the integer
matrix with rows $(k, 0)$ and $(3k^2 + 3k, k)$, and let $(P, Q, R)$ be a $k$-generalized Cohn
triple associated with $(a, b, c)$. Then $(P, PQ - S, Q)$ is a $k$-generalized Cohn triple
associated with $(a, \lfloor (a^2 + kab + b^2)/c \rfloor, b)$, and $(Q, QR - S, R)$ is a
$k$-generalized Cohn triple associated with $(b, \lfloor (b^2 + kbc + c^2)/a \rfloor, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 3.5.

Stated but not proved: `MetaMathlibExt.IsGenCohnTriple.step` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 617](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L617). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#step).

## A product identity for generalized Cohn matrices

Let $k$ be a natural number, let $M$
be a $k$-generalized Cohn matrix, and let $E$ be the $2 \times 2$ integer matrix whose only
nonzero entry is $3 + 3k$, in row $2$ and column $1$. Then $MEM = (\operatorname{tr} M + k)M + E$
and $M^{-1} E M^{-1} = -(\operatorname{tr} M^{-1} + k)M^{-1} + E$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 3.7.

Stated but not proved: `MetaMathlibExt.IsGenCohnMatrix.mul_E_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#mul-e-mul).

## Vertices of the wide generalized Cohn tree are generalized Cohn triples

Let $k$ be a
natural number. For every integer $\ell$ and every path $w$, the vertex of the wide
$k$-generalized Cohn tree $\mathrm{WGCT}(k, \ell)$ at $w$ is a $k$-generalized Cohn triple
associated with the vertex of the wide $k$-generalized Markov tree $\mathrm{WMT}(k)$ at $w$.
Moreover, every $k$-generalized Markov triple $(a, b, c)$ with $a \le b$ and $c \le b$ has an
associated $k$-generalized Cohn triple.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 3.9.

Stated but not proved: `MetaMathlibExt.wideGenCohnTree_isGenCohnTriple` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 642](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L642). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-cohn-tree-is-gen-cohn-triple).

## Generalized Cohn triples with largest middle entry lie in wide generalized Cohn trees

Let $k$ be a natural number and let $(P, Q, R)$ be a $k$-generalized Cohn triple associated with
$(a, b, c)$, where $a \le b$ and $c \le b$. Then there are an integer $\ell$ and a path $w$ such
that $(P, Q, R)$ is the vertex of the wide $k$-generalized Cohn tree $\mathrm{WGCT}(k, \ell)$
reached along $w$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 3.10.

Stated but not proved: `MetaMathlibExt.IsGenCohnTriple.mem_wideGenCohnTree` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#mem-wide-gen-cohn-tree).

## Parent triples of a generalized Cohn triple

Let $k$ be a natural number and let $S$ be
the integer matrix with rows $(k, 0)$ and $(3k^2 + 3k, k)$. Let $(P, Q, R)$ be a $k$-generalized
Cohn triple associated with $(a, b, c)$, and let $b' = \lfloor (a^2 + kac + c^2)/b \rfloor$. Then
$(P, R, P^{-1}(R + S))$ is a $k$-generalized Cohn triple associated with $(a, c, b')$, and
$((P + S)R^{-1}, P, R)$ is a $k$-generalized Cohn triple associated with $(b', a, c)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 3.11.

Stated but not proved: `MetaMathlibExt.IsGenCohnTriple.parent` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 663](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L663). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#parent).

## Distinct paths give distinct middle matrices in the wide generalized Cohn tree

For
every natural number $k$ and every integer $\ell$, if the vertices $(P, Q, R)$ and $(P', Q', R')$
of the wide $k$-generalized Cohn tree $\mathrm{WGCT}(k, \ell)$ at paths $w$ and $w'$ (finite
sequences of left and right steps) satisfy $Q = Q'$, then $w = w'$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Theorem 3.13.

Stated but not proved: `MetaMathlibExt.wideGenCohnTree_snd_injective` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#wide-gen-cohn-tree-snd-injective).

## Vertices of the generalized Cohn tree are Cohn triples over the Markov tree

For every
natural number $k$, every integer $\ell$ and every path $w$ (a finite sequence of left and
right steps), the vertex $(P, Q, R)$ of the $k$-generalized Cohn tree $\mathrm{GCT}(k, \ell)$
at $w$ is a $k$-generalized Cohn triple associated with the vertex $(a, b, c)$ of the
$k$-generalized Markov tree $\mathrm{MT}(k)$ at the same path $w$.

The source phrases this as the canonical graph isomorphism
$\mathrm{GCT}(k, \ell) \to \mathrm{MT}(k)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 3.15.

Stated but not proved: `MetaMathlibExt.genCohnTree_isGenCohnTriple` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-tree-is-gen-cohn-triple).

## Middle matrices of the generalized Cohn tree are distinct

For every natural number $k$
and every integer $\ell$, vertices of the $k$-generalized Cohn tree $\mathrm{GCT}(k, \ell)$ at
different paths have different middle matrices.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 3.16.

Stated but not proved: `MetaMathlibExt.genCohnTree_snd_injective` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 689](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L689). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-tree-snd-injective).

## Cohn triples sit at a unique vertex of a Cohn tree

Let $(P, Q, R)$ be a
$k$-generalized Cohn triple associated with $(a, b, c)$, where $b > \max\{a, c\}$. Then there is
exactly one pair $(\ell, w)$ of an integer $\ell$ and a path $w$ (a finite sequence of left and
right moves) such that $(P, Q, R)$ is the vertex of the $k$-generalized Cohn tree
$\mathrm{GCT}(k, \ell)$ reached along $w$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 3.17.

Stated but not proved: `MetaMathlibExt.IsGenCohnTriple.existsUnique_mem_genCohnTree` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 697](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L697). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#exists-unique-mem-gen-cohn-tree).

## The Farey tree

Write a fraction $n/d$, with $n$ and $d$ natural numbers, for the pair
$(n, d)$, so that $1/0$ stands for $\infty$. The Farey tree $\mathrm{FT}$ is the infinite binary
tree of triples of fractions with root $(0/1, 1/1, 1/0)$ in which a vertex $(a/b, c/d, e/f)$
has left child $(a/b, (a+c)/(b+d), c/d)$ and right child $(c/d, (c+e)/(d+f), e/f)$. For a path
$w$, a finite sequence of left and right moves, this gives the vertex of $\mathrm{FT}$ reached
from the root by making the moves of $w$ in order.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.2.

Formalized by `MetaMathlibExt.fareyTree`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 707](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L707). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#farey-tree).

## Left child of the root of the Farey tree

The left child of the root $(0/1, 1/1, 1/0)$
of the Farey tree is $(0/1, 1/2, 1/1)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 4.

Formalized by `MetaMathlibExt.fareyTree_false`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 716](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L716). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#farey-tree-false).

## Farey triples

Write a pair $(a, b)$ of natural numbers as the fraction $a/b$, so that
$1/0$ is allowed. Three such fractions $(a/b, c/d, e/f)$ form a Farey triple if
$\gcd(a, b) = \gcd(c, d) = \gcd(e, f) = 1$ and

$$|ad - bc| = |cf - de| = |eb - fa| = 1,$$

where the differences are taken in $\mathbb{Z}$.

The paper's printed condition writes $d/e$ for $e/f$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.2.

Formalized by `MetaMathlibExt.IsFareyTriple`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 725](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L725). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-farey-triple).

## The triple $(0/1, 1/1, 1/0)$ is a Farey triple

The fractions $0/1$, $1/1$ and $1/0$,
given as the pairs of natural numbers $(0, 1)$, $(1, 1)$ and $(1, 0)$, form a Farey triple.

This triple is the root of the Farey tree.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.2.

Formalized by `MetaMathlibExt.isFareyTriple_root`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 734](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L734). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-farey-triple-root).

## Basic properties of the Farey tree

Write a fraction $a/b$, with $a$ and $b$ natural
numbers, for the pair $(a, b)$, so that $1/0$ stands for $\infty$, and compare fractions by
cross multiplication: $a/b < c/d$ means $ad < cb$. (1) If $(a/b, c/d, e/f)$ is a Farey triple,
then so are $(a/b, (a+c)/(b+d), c/d)$ and $(c/d, (c+e)/(d+f), e/f)$; and the vertex of the
Farey tree reached along every path is a Farey triple. (2) For all coprime positive natural
numbers $a$ and $b$ there is exactly one path along which the vertex of the Farey tree has
second entry $a/b$. (3) Every vertex $(a/b, c/d, e/f)$ of the Farey tree satisfies
$a/b < c/d < e/f$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 3.22 (citing Aigner, Section 3.2).

Stated but not proved: `MetaMathlibExt.fareyTree_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#farey-tree-properties).

## Fraction labels of generalized Cohn matrices

Let $k$ be a natural number and $\ell$ an
integer, and write a pair $(a, b)$ of natural numbers as the fraction $a/b$. An integer
$2 \times 2$ matrix $C$ is labeled by the fraction $q$, written $C = C_q(k, \ell)$, if there is a
path $w$ from the root such that, for one of the three positions (first, second or third), $C$
is the entry in that position of the vertex of the generalized Cohn tree $\mathrm{GCT}(k, \ell)$
at $w$ and $q$ is the entry in that position of the vertex of the Farey tree at $w$.

The paper labels only second entries; here first and third entries carry the labels of the vertex
where they were created, which gives $C_{0/1}$ and $C_{1/0}$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.2.

Formalized by `MetaMathlibExt.IsGenCohnLabel`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 761](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L761). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-cohn-label).

## The middle matrix of the root of $\mathrm{GCT}(k, \ell)$ has label $1/1$

For every
natural number $k$ and every integer $\ell$, the second entry of the root vertex of the
generalized Cohn tree $\mathrm{GCT}(k, \ell)$ is labeled by the fraction $1/1$, that is, it is
$C_{1/1}(k, \ell)$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 3.2.

Formalized by `MetaMathlibExt.isGenCohnLabel_one`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 770](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L770). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-cohn-label-one).

## The Cohn labeling is injective and increasing

Fix a natural number $k$ and an integer
$\ell$. Write fractions $a/b$, with $a$ and $b$ natural numbers, as pairs $(a, b)$, compared by
cross multiplication ($a/b < c/d$ means $ad < cb$), and write $C = C_q(k, \ell)$ when the
matrix $C$ carries the fraction label $q$ in the $k$-generalized Cohn tree $\mathrm{GCT}(k, \ell)$.
For an integer $2 \times 2$ matrix $M = (m_{ij})$ let $I_M = m_{11}/m_{12} \in \mathbb{Q}$.
(1) If $C = C_q(k, \ell)$ and $C = C_{q'}(k, \ell)$, then $q = q'$. (2) If $C = C_q(k, \ell)$,
$C' = C_{q'}(k, \ell)$ and $q < q'$, then $I_C < I_{C'}$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 3.23.

Stated but not proved: `MetaMathlibExt.genCohnLabel_injective_index_strictMono` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 780](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L780). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-label-injective-index-strict-mo).

## Fraction labeling of generalized Markov numbers

Let $k$ be a natural number. Write a
fraction $n/d$ as the pair $(n, d)$ of natural numbers, with $1/0$ standing for $\infty$. Let
$FT$ be the Farey tree and $MT(k)$ the $k$-generalized Markov tree, with vertices of both
indexed by finite paths of left and right steps from the root. A natural number $m$ carries the
label $q$, written $m = m_q$, when there are a path $w$ and a position $i \in \{1, 2, 3\}$ such
that the $i$-th entry of the vertex of $FT$ at $w$ is $q$ and the $i$-th entry of the vertex of
$MT(k)$ at $w$ is $m$.

On fractions in $[0, 1]$ this gives $m_{0/1} = 1$, $m_{1/1} = k + 2$ and, for $t \in (0, 1)$,
the number $m_t$ of Gyoda and Maruyama.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 4.

Formalized by `MetaMathlibExt.IsGenMarkovLabel`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 791](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L791). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-label).

## The fraction $1/1$ labels $k + 2$

For every natural number $k$, the number $k + 2$
carries the label $1/1$ in the fraction labeling of $k$-generalized Markov numbers, that is,
$m_{1/1} = k + 2$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Section 4.

Formalized by `MetaMathlibExt.isGenMarkovLabel_one`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 800](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L800). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-label-one).

## Unique maximal triple via the fraction labeling

Let $k$ be a natural number and $b$
a $k$-generalized Markov number. Then $b$ is the maximum of a unique $k$-generalized Markov
triple up to order if and only if there is exactly one pair $(n, d)$ of natural numbers with
$n \le d$ such that $b$ is a label of the fraction $n/d$ in the fraction labeling of
$k$-generalized Markov numbers.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Proposition 4.1.

Stated but not proved: `MetaMathlibExt.hasUniqueMaxGenMarkovTriple_iff_existsUnique_label` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 809](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L809). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#has-unique-max-gen-markov-triple-iff-exi).

## Uniqueness of maximal triples and injectivity of the fraction labeling

For every
natural number $k$, the following are equivalent: every $k$-generalized Markov number is the
maximum of a unique $k$-generalized Markov triple up to order (Conjecture 1.8 for $k$); and the
fraction labeling of $k$-generalized Markov numbers is injective on $[0, 1]$, that is, whenever
$(n, d)$ and $(n', d')$ are pairs of natural numbers with $n \le d$ and $n' \le d'$ and a number
$m$ is a label of both $n/d$ and $n'/d'$, then $(n, d) = (n', d')$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 4.2.

Stated but not proved: `MetaMathlibExt.genMarkovUniqueness_iff_label_injective` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 819](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L819). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-uniqueness-iff-label-injectiv).

## Characteristic number

For natural numbers $m_r$, $m_t$, $m_s$, a natural number $x$ is
a characteristic number of $(m_r, m_t, m_s)$ when $0 < x < m_t/2$ and
$m_r x \equiv \pm m_s \pmod{m_t}$, that is, $m_t$ divides $m_r x - m_s$ or $m_r x + m_s$ in
$\mathbb{Z}$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Definition 4.3.

Formalized by `MetaMathlibExt.IsGenMarkovCharNumber`, a definition declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 829](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L829). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-char-number).

## Characteristic number of $(1, 5, 2)$

The number $2$ is a characteristic number of
$(m_r, m_t, m_s) = (1, 5, 2)$: indeed $0 < 2 < 5/2$ and $1 \cdot 2 \equiv 2 \pmod 5$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Definition 4.3.

Formalized by `MetaMathlibExt.isGenMarkovCharNumber_one_five_two`, a theorem declared in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 836](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#is-gen-markov-char-number-one-five-two).

## Positive corner entry of the generalized Cohn tree for $\ell = -k$

Let $k$ be a natural
number and $w$ a path, and suppose that the middle fraction $n/d$ of the vertex of the Farey
tree at $w$ satisfies $0 < n < d$. Then the $(1,1)$-entry of the middle matrix of the vertex of
the $k$-generalized Cohn tree $\mathrm{GCT}(k, -k)$ at $w$ is positive.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.4.

Stated but not proved: `MetaMathlibExt.genCohnTree_neg_snd_entry_pos` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 844](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-tree-neg-snd-entry-pos).

## Shape of the generalized Cohn matrices for $\ell = -k$

Let $k$ be a natural number and
$w$ a path, and suppose that the middle fraction $n/d$ of the vertex of the Farey tree at $w$
satisfies $0 < n < d$. Let $(a, b, c)$ be the vertex of the $k$-generalized Markov tree
$\mathrm{MT}(k)$ at $w$, and let $C$ be the middle matrix of the vertex of the $k$-generalized
Cohn tree $\mathrm{GCT}(k, -k)$ at $w$. Then there is a natural number $u$ that is a
characteristic number of $(a, b, c)$ such that $C_{11} = u$, $C_{12} = b$ and
$C_{22} = (3 + 3k)b - u - k$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.5.

Stated but not proved: `MetaMathlibExt.genCohnTree_neg_snd_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 854](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L854). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-cohn-tree-neg-snd-eq).

## The characteristic number solves $m_r x \equiv m_s \pmod{m_t}$

Let $k \in \mathbb{N}$,
let $w$ be a finite sequence of left and right moves, let $(r, t, s)$ be the vertex of the
Farey tree at $w$, and let $(m_r, m_t, m_s)$ be the vertex of the $k$-generalized Markov tree
$\mathrm{MT}(k)$ at $w$. Write $t = n/d$. If $0 < n < d$ and $u$ is a characteristic number
of $(m_r, m_t, m_s)$, then $m_t$ divides $m_r u - m_s$ in $\mathbb{Z}$, that is,
$m_r u \equiv m_s \pmod{m_t}$.

Of the two congruences $m_r x \equiv \pm m_s \pmod{m_t}$ allowed in the definition of a
characteristic number, the one with the plus sign holds.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Corollary 4.6.

Stated but not proved: `MetaMathlibExt.genMarkovCharNumber_dvd_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 867](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L867). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-char-number-dvd-sub).

## The characteristic number solves $x^2 + kx + 1 \equiv 0 \pmod{m_t}$

Let
$k \in \mathbb{N}$, let $w$ be a finite sequence of left and right moves, let $(r, t, s)$ be
the vertex of the Farey tree at $w$, and let $(m_r, m_t, m_s)$ be the vertex of the
$k$-generalized Markov tree $\mathrm{MT}(k)$ at $w$. Write $t = n/d$. If $0 < n < d$ and $u$
is a characteristic number of $(m_r, m_t, m_s)$, then $m_t$ divides $u^2 + ku + 1$, that is,
$u^2 + ku + 1 \equiv 0 \pmod{m_t}$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.7.

Stated but not proved: `MetaMathlibExt.genMarkovCharNumber_sq_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 878](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L878). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-char-number-sq-add).

## The characteristic number is less than $m_t/2 - k$

Let $k \in \mathbb{N}$, let $w$ be a
finite sequence of left and right moves, let $(r, t, s)$ be the vertex of the Farey tree at $w$,
and let $(m_r, m_t, m_s)$ be the vertex of the $k$-generalized Markov tree $\mathrm{MT}(k)$ at
$w$. Write $t = n/d$. If $0 < n < d$ and $u$ is a characteristic number of $(m_r, m_t, m_s)$,
then $2(u + k) < m_t$, that is, $u + k < m_t/2$.

## Sources

- Y. Gyoda and S. Maruyama, *Uniqueness Theorem of Generalized Markov Numbers That Are Prime Powers*, INTEGERS 26 (2026), Article A91, Lemma 4.8.

Stated but not proved: `MetaMathlibExt.genMarkovCharNumber_add_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean, line 888](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeneralizedMarkovUniquenessWanted.lean#L888). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html#gen-markov-char-number-add-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Markov triples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/generalized-markov-triples)
