---
declaration: section
origin: cited
lean: MetaMathlibExt.gaussianInt_exists_prime_norm_between, MetaMathlibExt.eisenstein_exists_prime_norm_between, MetaMathlibExt.nat_schatunowsky, MetaMathlibExt.nat_iwata_finite, MetaMathlibExt.gaussianInt_schatunowsky_max_norm_five_add_five_i, MetaMathlibExt.quadPrimeNorm, MetaMathlibExt.quadPrimeNorm_zero, MetaMathlibExt.quadPrimorialNorm
statement: formalized
---

# Schatunowsky-type theorems

21 results, 6 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html).

## Bertrand's postulate for Gaussian integers

Let $N(a + bi) = a^2 + b^2$ be the norm on the
Gaussian integers $\mathbb{Z}[i]$. For every prime element $\pi$ of $\mathbb{Z}[i]$ with
$N(\pi) \ne 2$ (that is, $\pi$ is not an associate of $1 + i$) there is a prime element $\rho$
of $\mathbb{Z}[i]$ with $N(\pi) < N(\rho) \le 2N(\pi)$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Lemma 2.

Stated but not proved: `MetaMathlibExt.gaussianInt_exists_prime_norm_between` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#gaussian-int-exists-prime-norm-between).

## Bertrand's postulate for Eisenstein integers

Let $\mathcal{O}$ be the ring of integers of
the cyclotomic field $\mathbb{Q}(\zeta_3)$, and let $N$ be the field norm from $\mathbb{Q}(\zeta_3)$
to $\mathbb{Q}$. For every prime element $\pi$ of $\mathcal{O}$ there is a prime element $\rho$ of
$\mathcal{O}$ with $N(\pi) < N(\rho) \le 2N(\pi)$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Lemma 3.

Stated but not proved: `MetaMathlibExt.eisenstein_exists_prime_norm_between` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#eisenstein-exists-prime-norm-between).

## Schatunowsky's theorem

The natural numbers $a \ge 2$ such that every natural number $b$
with $1 < b < a$ and $\gcd(a, b) = 1$ is prime are exactly $2, 3, 4, 6, 8, 12, 18, 24$ and $30$.

The numbers $a = 0$ and $a = 1$, for which no such $b$ exists, are excluded.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Theorem 1, quoting Schatunowsky.

Stated but not proved: `MetaMathlibExt.nat_schatunowsky` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#nat-schatunowsky).

## Iwata's generalization of Schatunowsky's theorem

For every natural number $\ell$, there
are only finitely many natural numbers $a$ such that every natural number $b$ with $1 < b < a$
and $\gcd(a, b) = 1$ satisfies $\Omega(b) \le \ell$, where $\Omega(b)$ is the number of prime
factors of $b$ counted with multiplicity.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Theorem 2, quoting Iwata. `ℓ = 0` is included (trivially finite).

Stated but not proved: `MetaMathlibExt.nat_iwata_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#nat-iwata-finite).

## Dalezman's Schatunowsky theorem for the Gaussian integers

Let $N(a + bi) = a^2 + b^2$ be
the norm on the Gaussian integers $\mathbb{Z}[i]$, and let $S$ be the set of
$\alpha \in \mathbb{Z}[i]$ such that every $\beta \in \mathbb{Z}[i]$ coprime to $\alpha$ with
$1 < N(\beta) < N(\alpha)$ is a Gaussian prime. Then $5 + 5i \in S$, every element of $S$ has
norm at most $50$, and every element of $S$ of norm $50$ is an associate of $5 + 5i$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Theorem 3, quoting Dalezman.

Stated but not proved: `MetaMathlibExt.gaussianInt_schatunowsky_max_norm_five_add_five_i` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#gaussian-int-schatunowsky-max-norm-five).

## Norm of the $n$-th prime

Let $K$ be a number field with ring of integers $\mathcal{O}_K$.
For $n \ge 1$, $N(\pi_n)$ is the $n$-th smallest natural number that is the absolute norm of some
nonzero prime ideal of $\mathcal{O}_K$, each such norm counted once however many prime ideals
have it; and $N(\pi_0) = 1$.

For an imaginary quadratic field $K = \mathbb{Q}(\sqrt{m})$ of class number one the prime ideals
above distinct rational primes $p$ have distinct norms $p$ or $p^2$, so $N(\pi_n)$ is the norm of
the $n$-th prime $\pi_n$ of the paper's norm-ordered set $P_m^+$ (Definition 1), and
$N(\pi_0) = 1$ matches its convention $\pi_0 = 1$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Definition 1 and Section 4 (`N(π_n)`).

Formalized by `MetaMathlibExt.quadPrimeNorm`, a definition declared in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-prime-norm).

## The zeroth prime norm is one

For every number field $K$, the zeroth prime norm
$N(\pi_0)$ of $K$ equals $1$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Definition 1 (convention `π_0 = 1`).

Formalized by `MetaMathlibExt.quadPrimeNorm_zero`, a theorem declared in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-prime-norm-zero).

## Norm of the $n$-th primorial

Let $K$ be a number field with ring of integers
$\mathcal{O}_K$, and let $n$ be a natural number. The primorial norm $N(\pi_n\#)$ is the product of
the absolute norms of the nonzero prime ideals of $\mathcal{O}_K$ whose norm is at most $N(\pi_n)$,
where $N(\pi_n)$ is the $n$-th smallest norm of a nonzero prime ideal of $\mathcal{O}_K$ for
$n \ge 1$ and $N(\pi_0) = 1$.

There are finitely many such prime ideals. For an imaginary quadratic field of class number one,
$N(\pi_n\#)$ is the norm of the paper's quadratic primorial $\pi_n\#$ (Definition 2).

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Definition 2 (`π_n#`).

Formalized by `MetaMathlibExt.quadPrimorialNorm`, a definition declared in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-primorial-norm).

## The zeroth primorial norm is one

For every number field $K$ with ring of integers
$\mathcal{O}_K$, the primorial norm $N(\pi_0\#)$ of $K$ equals $1$: no nonzero prime ideal of
$\mathcal{O}_K$ has norm at most $1$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Definition 2 (`π_0# = 1`).

Formalized by `MetaMathlibExt.quadPrimorialNorm_zero`, a theorem declared in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-primorial-norm-zero).

## Schatunowsky set of a number field

Let $K$ be a number field with ring of integers
$\mathcal{O}_K$ and let $\ell$ be a natural number. For $\alpha \in \mathcal{O}_K$ write $N(\alpha)$
for the absolute norm of the principal ideal $(\alpha)$ and $\Omega(\alpha)$ for the number of
prime ideal factors of $(\alpha)$ counted with multiplicity. The Schatunowsky set $Q_\ell(K)$ is
the set of $\alpha \in \mathcal{O}_K$ with $N(\alpha) > 1$ such that every $\beta \in \mathcal{O}_K$
coprime to $\alpha$ (that is, $(\alpha) + (\beta) = \mathcal{O}_K$) with $1 < N(\beta) < N(\alpha)$
satisfies $\Omega(\beta) \le \ell$.

The set is closed under multiplication by units. For $K = \mathbb{Q}(\sqrt{m})$ imaginary quadratic
of class number one it is the paper's set $Q_{m,\ell}$ (Equation (4)).

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Section 5, Equation (4).

Formalized by `MetaMathlibExt.quadSchatunowskySet`, a definition declared in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-schatunowsky-set).

## One is not in the Schatunowsky set

For every number field $K$ and every natural number
$\ell$, the element $1$ of the ring of integers $\mathcal{O}_K$ does not lie in the Schatunowsky
set $Q_\ell(K)$, because the ideal it generates has norm $1$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Section 5, Equation (4).

Formalized by `MetaMathlibExt.one_not_mem_quadSchatunowskySet`, a theorem declared in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#one-not-mem-quad-schatunowsky-set).

## Unit groups of imaginary quadratic fields

Let $K$ be an imaginary quadratic field with
discriminant $d_K$. The unit group of its ring of integers $\mathcal{O}_K$ is cyclic, of order
$4$ if $d_K = -4$, of order $6$ if $d_K = -3$, and of order $2$ otherwise.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Proposition 2.

Stated but not proved: `MetaMathlibExt.imagQuadratic_units_isCyclic_card` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#imag-quadratic-units-is-cyclic-card).

## Ratios of consecutive prime ideal norms in an imaginary quadratic field tend to $1$

Let
$K$ be an imaginary quadratic field, that is, a totally complex number field of degree $2$ over
$\mathbb{Q}$, with ring of integers $\mathcal{O}_K$. For $m \ge 1$ let $r_m$ be the least natural
number $x$ such that at least $m$ nonzero prime ideals of $\mathcal{O}_K$ have absolute norm at
most $x$; this is the $m$-th smallest norm of a nonzero prime ideal, counted with multiplicity.
Let $N(\pi_m)$ be the $m$-th smallest element of the set of absolute norms of nonzero prime
ideals of $\mathcal{O}_K$. Then the real quotients satisfy $r_{m+1}/r_m \to 1$ and
$N(\pi_{m+1})/N(\pi_m) \to 1$ as $m \to \infty$.

The sequence $r_m$ is the paper's $N(\rho_m)$, where $\rho_m$ runs over all primes up to units
(Definition 1). The statement holds for every imaginary quadratic field: the norms do not need
the paper's class-number-one assumption.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Lemma 1.

Stated but not proved: `MetaMathlibExt.tendsto_quadPrimeNorm_succ_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#tendsto-quad-prime-norm-succ-div).

## Prime norm powers eventually fall below the quadratic primorial

Let $K$ be an imaginary
quadratic field. Put $N(\pi_0) = 1$ and, for $n \ge 1$, let $N(\pi_n)$ be the $n$-th smallest
number that is the norm of a nonzero prime ideal of $\mathcal{O}_K$; let $N(\pi_n\#)$ be the
product of the norms of the nonzero prime ideals of $\mathcal{O}_K$ of norm at most $N(\pi_n)$.
For every natural number $\ell$ there is $n_0$ such that $N(\pi_{n+1})^{\ell+1} < N(\pi_n\#)$
for all $n \ge n_0$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Proposition 4.

Stated but not proved: `MetaMathlibExt.exists_quadPrimeNorm_pow_lt_quadPrimorialNorm` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#exists-quad-prime-norm-pow-lt-quad-primo).

## Large elements of a Schatunowsky set lie in all small prime ideals

Let $K$ be an
imaginary quadratic field of class number $1$. For $\alpha \in \mathcal{O}_K$ let $N(\alpha)$ be
the absolute norm of the ideal $(\alpha)$. Put $N(\pi_0) = 1$ and, for $n \ge 1$, let $N(\pi_n)$
be the $n$-th smallest number that is the norm of a nonzero prime ideal of $\mathcal{O}_K$. For
a natural number $\ell$, let $Q_\ell$ be the set of $\alpha \in \mathcal{O}_K$ with
$N(\alpha) > 1$ such that every $\beta \in \mathcal{O}_K$ coprime to $\alpha$ with
$1 < N(\beta) < N(\alpha)$ has at most $\ell$ prime ideal factors, counted with multiplicity.
For natural numbers $\ell$ and $n$, if $\alpha \in Q_\ell$ and $N(\pi_n)^{\ell+1} < N(\alpha)$,
then $\alpha$ lies in every nonzero prime ideal of $\mathcal{O}_K$ of norm at most $N(\pi_n)$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Lemma 4.

Stated but not proved: `MetaMathlibExt.mem_prime_of_mem_quadSchatunowskySet` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#mem-prime-of-mem-quad-schatunowsky-set).

## Norm bound and finiteness of the Schatunowsky set

Let $K$ be an imaginary quadratic field
(a totally complex number field of degree $2$ over $\mathbb{Q}$) with class number $1$ and ring of
integers $\mathcal{O}_K$, and let $\ell$ and $n_0$ be natural numbers such that
$N(\pi_{n+1})^{\ell+1} < N(\pi_n\#)$ for every $n \ge n_0$, where $N(\pi_n)$ and $N(\pi_n\#)$ are
the prime and primorial norms of $K$. Then no $\alpha \in \mathcal{O}_K$ whose principal ideal
$(\alpha)$ has absolute norm greater than $N(\pi_{n_0})^{\ell+1}$ lies in the Schatunowsky set
$Q_\ell(K)$, and $Q_\ell(K)$ is finite.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Theorem 4.

Stated but not proved: `MetaMathlibExt.quadSchatunowskySet_norm_bound_and_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-schatunowsky-set-norm-bound-and-fin).

## Decomposition of the Schatunowsky set

Let $K$ be an imaginary quadratic field (a totally
complex number field of degree $2$ over $\mathbb{Q}$) with class number $1$ and ring of integers
$\mathcal{O}_K$, and let $\ell$ and $n_0$ be natural numbers such that
$N(\pi_{n+1})^{\ell+1} < N(\pi_n\#)$ for every $n \ge n_0$, where $N(\pi_n)$ and $N(\pi_n\#)$ are
the prime and primorial norms of $K$. Write $N(\alpha)$ for the absolute norm of the principal
ideal $(\alpha)$. Then the Schatunowsky set $Q_\ell(K)$ is the union, over $1 \le n \le n_0$, of
the sets of $\alpha \in \mathcal{O}_K$ with
$N(\pi_{n-1})^{\ell+1} < N(\alpha) \le N(\pi_n)^{\ell+1}$ that lie in every nonzero prime ideal
of $\mathcal{O}_K$ of norm at most $N(\pi_{n-1})$.

Since $K$ has class number $1$, lying in all these prime ideals means being divisible by the
paper's primorial $\pi_{n-1}\#$. The element of largest norm in $Q_\ell(K)$ need not be divisible
by $\pi_{n_0-1}\#$ unless $n_0$ is the least admissible value: for the Gaussian integers with
$\ell = 1$, both $n_0 = 3$ and $n_0 = 4$ are admissible, but the element of largest norm,
$5(1+i) = \pi_2\#$, is not divisible by $\pi_3\# = 15(1+i)$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Theorem 5.

Stated but not proved: `MetaMathlibExt.quadSchatunowskySet_eq_iUnion` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#quad-schatunowsky-set-eq-i-union).

## Explicit primorial thresholds for the Gaussian integers

Let $K$ be a number field of
discriminant $-4$ (so $K \cong \mathbb{Q}(i)$). Put $N(\pi_0) = 1$ and, for $n \ge 1$, let
$N(\pi_n)$ be the $n$-th smallest number that is the norm of a nonzero prime ideal of
$\mathcal{O}_K$; let $N(\pi_n\#)$ be the product of the norms of the nonzero prime ideals of
$\mathcal{O}_K$ of norm at most $N(\pi_n)$. For each pair $(\ell, n_\ell)$ among $(1, 3)$,
$(2, 4)$, $(3, 5)$, $(4, 5)$, $(5, 6)$, $(6, 7)$, $(7, 7)$ and every $n \ge n_\ell$,
$N(\pi_{n+1})^{\ell+1} < N(\pi_n\#)$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Proposition 5.

Stated but not proved: `MetaMathlibExt.gaussian_quadPrimeNorm_pow_lt_quadPrimorialNorm` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#gaussian-quad-prime-norm-pow-lt-quad-pri).

## Explicit primorial thresholds for the Eisenstein integers

Let $K$ be a number field of
discriminant $-3$ (so $K \cong \mathbb{Q}(\sqrt{-3})$). Put $N(\pi_0) = 1$ and, for $n \ge 1$, let
$N(\pi_n)$ be the $n$-th smallest number that is the norm of a nonzero prime ideal of
$\mathcal{O}_K$; let $N(\pi_n\#)$ be the product of the norms of the nonzero prime ideals of
$\mathcal{O}_K$ of norm at most $N(\pi_n)$. For each pair $(\ell, n_\ell)$ among $(1, 3)$,
$(2, 4)$, $(3, 5)$, $(4, 5)$, $(5, 6)$, $(6, 7)$, $(7, 8)$ and every $n \ge n_\ell$,
$N(\pi_{n+1})^{\ell+1} < N(\pi_n\#)$.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Proposition 6.

Stated but not proved: `MetaMathlibExt.eisenstein_quadPrimeNorm_pow_lt_quadPrimorialNorm` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#eisenstein-quad-prime-norm-pow-lt-quad-p).

## The first three Schatunowsky sets of the Gaussian integers

Let $K$ be a number field
of discriminant $-4$ (so $K \cong \mathbb{Q}(i)$). For $\alpha \in \mathcal{O}_K$ let $N(\alpha)$
be the absolute norm of the ideal $(\alpha)$, and let $Q_\ell$ be the set of
$\alpha \in \mathcal{O}_K$ with $N(\alpha) > 1$ such that every $\beta \in \mathcal{O}_K$ coprime
to $\alpha$ with $1 < N(\beta) < N(\alpha)$ has at most $\ell$ prime ideal factors, counted with
multiplicity. Below, $\gamma$ ranges over $\mathcal{O}_K$ and $\pi$ over the elements of norm $2$.
Then $Q_1$ consists of the $\alpha$ with $1 < N(\alpha) \le 4$, the products $\gamma\pi$ with
$3 \le N(\gamma) \le 12$, and the associates of $5\pi$. The set $Q_2$ consists of the $\alpha$
with $1 < N(\alpha) \le 8$, the $\gamma\pi$ with $5 \le N(\gamma) \le 62$, the $5\gamma\pi$ with
$3 \le N(\gamma) \le 14$, and the $15\gamma\pi$ with $2 \le N(\gamma) \le 4$. The set $Q_3$
consists of the $\alpha$ with $1 < N(\alpha) \le 16$, the $\gamma\pi$ with
$9 \le N(\gamma) \le 312$, the $5\gamma\pi$ with $13 \le N(\gamma) \le 131$, the $15\gamma\pi$
with $15 \le N(\gamma) \le 63$, and the associates of $195\pi$. Moreover, the elements of largest
norm are unique up to units: for $(c, \ell) = (5, 1), (30, 2), (195, 3)$ there is a $\pi$ of
norm $2$ with $c\pi \in Q_\ell$ such that every $\alpha \in Q_\ell$ has $N(\alpha) \le N(c\pi)$,
with $\alpha$ an associate of $c\pi$ in case of equality.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Corollary 1.

Stated but not proved: `MetaMathlibExt.gaussian_quadSchatunowskySet_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#gaussian-quad-schatunowsky-set-eq).

## The first three Schatunowsky sets of the Eisenstein integers

Let $K$ be a number
field of discriminant $-3$ (so $K \cong \mathbb{Q}(\sqrt{-3})$). For $\alpha \in \mathcal{O}_K$ let
$N(\alpha)$ be the absolute norm of the ideal $(\alpha)$, and let $Q_\ell$ be the set of
$\alpha \in \mathcal{O}_K$ with $N(\alpha) > 1$ such that every $\beta \in \mathcal{O}_K$ coprime
to $\alpha$ with $1 < N(\beta) < N(\alpha)$ has at most $\ell$ prime ideal factors, counted with
multiplicity. Below, $\gamma$ ranges over $\mathcal{O}_K$ and $\pi$ over the elements of norm $3$.
Then $Q_1$ consists of the $\alpha$ with $1 < N(\alpha) \le 9$, the products $\gamma\pi$ with
$4 \le N(\gamma) \le 5$, and the products $2\gamma\pi$ with $2 \le N(\gamma) \le 4$. The set
$Q_2$ consists of the $\alpha$ with $1 < N(\alpha) \le 27$, the $\gamma\pi$ with
$10 \le N(\gamma) \le 21$, the $2\gamma\pi$ with $6 \le N(\gamma) \le 28$, and the $14\gamma\pi$
with $1 \le N(\gamma) \le 3$. The set $Q_3$ consists of the $\alpha$ with
$1 < N(\alpha) \le 81$, the $\gamma\pi$ with $28 \le N(\gamma) \le 85$, the $2\gamma\pi$ with
$22 \le N(\gamma) \le 200$, the $14\gamma\pi$ with $5 \le N(\gamma) \le 48$, and the associates
of $182\pi$. Moreover, the elements of largest norm are unique up to units: there is a $\pi$ of
norm $3$ with $4\pi \in Q_1$ such that every $\alpha \in Q_1$ has $N(\alpha) \le N(4\pi)$, with
$\alpha$ an associate of $4\pi$ in case of equality; $42 \in Q_2$, and every $\alpha \in Q_2$ has
$N(\alpha) \le N(42)$, with $\alpha$ an associate of $42$ in case of equality; and there is a
$\pi$ of norm $3$ with $182\pi \in Q_3$ such that every $\alpha \in Q_3$ has
$N(\alpha) \le N(182\pi)$, with $\alpha$ an associate of $182\pi$ in case of equality.

## Sources

- Hirofumi Nakai, Ken Sasaki and Konoka Yoshida, *Schatunowsky-type Theorems for Imaginary Quadratic Integer Rings of Class Number One*, INTEGERS 26 (2026), Article A110, Corollary 2.

Stated but not proved: `MetaMathlibExt.eisenstein_quadSchatunowskySet_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SchatunowskyImaginaryQuadraticWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html#eisenstein-quad-schatunowsky-set-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schatunowsky-type theorems](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/schatunowsky-type-theorems)
