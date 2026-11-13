---
declaration: section
origin: cited
lean: MetaMathlibExt.erdosStraus_typeI_of_dvd_sq, MetaMathlibExt.erdosStraus_typeI_exists_dvd_sq, MetaMathlibExt.erdosStraus_typeII_exists_dvd_sq, MathlibExt.NumberTheory.ErdosStrausPrimeStructureWanted.erdos_straus_prime_restricted_representation_iff
statement: formalized
---

# Erdős–Straus conjecture

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture/index.html).

## Type I Erdős–Straus triples from divisors of a square

Let $p$ be a prime and let $x$ be a
natural number with $\lceil p/4 \rceil \le x \le \lceil p/2 \rceil$. If $d$ is a positive divisor
of $x^2$ with $d \equiv -px \pmod{4x - p}$, then there are natural numbers $y$ and $z$ with
$(4x - p)\,y = px + d$ and $(4x - p)\,d\,z = px(px + d)$ such that $x \le y \le z$ and $p \nmid y$.

Since $4x > p$, these equations say $y = (px + d)/(4x - p)$ and $z = p(x + px^2/d)/(4x - p)$.

## Sources

- Kyle Bradford, *Elementary Patterns from the Erdős-Straus Conjecture*, INTEGERS 25 (2025), Article A54, Proposition 1.

Stated but not proved: `MetaMathlibExt.erdosStraus_typeI_of_dvd_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosStrausDivisorPatternsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosStrausDivisorPatternsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture/index.html#erdos-straus-type-i-of-dvd-sq).

## Divisor criterion necessary for type I Erdős–Straus solutions

Let $p$ be a prime and let
$x \le y \le z$ be positive integers with $4/p = 1/x + 1/y + 1/z$ and $p \nmid y$. Then
$\lceil p/4 \rceil \le x \le \lceil p/2 \rceil$, and there is a positive divisor $d$ of $x^2$ with
$d \equiv -px \pmod{4x - p}$, $(4x - p)\,y = px + d$ and $(4x - p)\,d\,z = px(px + d)$.

Since $4x > p$, the last two equations say $y = (px + d)/(4x - p)$ and
$z = p(x + px^2/d)/(4x - p)$.

## Sources

- Kyle Bradford, *Elementary Patterns from the Erdős-Straus Conjecture*, INTEGERS 25 (2025), Article A54, Proposition 3.

Stated but not proved: `MetaMathlibExt.erdosStraus_typeI_exists_dvd_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosStrausDivisorPatternsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosStrausDivisorPatternsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture/index.html#erdos-straus-type-i-exists-dvd-sq).

## Divisor criterion necessary for type II Erdős–Straus solutions

Let $p$ be a prime and let
$x \le y \le z$ be positive integers with $4/p = 1/x + 1/y + 1/z$ and $p \mid y$. Then
$\lceil p/4 \rceil \le x \le \lceil p/2 \rceil$, and there is a positive divisor $d$ of $x^2$ with
$d \le x$, $d \equiv -x \pmod{4x - p}$, $(4x - p)\,y = p(x + d)$ and $(4x - p)\,d\,z = px(x + d)$.

Since $4x > p$, the last two equations say $y = p(x + d)/(4x - p)$ and
$z = p(x + x^2/d)/(4x - p)$.

## Sources

- Kyle Bradford, *Elementary Patterns from the Erdős-Straus Conjecture*, INTEGERS 25 (2025), Article A54, Proposition 4.

Stated but not proved: `MetaMathlibExt.erdosStraus_typeII_exists_dvd_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosStrausDivisorPatternsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosStrausDivisorPatternsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture/index.html#erdos-straus-type-ii-exists-dvd-sq).

## Chamberland's characterization of restricted Erdős–Straus representations

For a prime
$p$, there are positive integers $a \le b \le c$ with $p \nmid a$, $p \mid b$, $p \mid c$ and
$4/p = 1/a + 1/b + 1/c$ if and only if there are positive integers $q$, $r$, $s_1$, $s_2$ with
$q \equiv 3 \pmod 4$, both $s_1$ and $s_2$ dividing $(q + 1)/4$, and $p + 4 s_1 s_2 = qr$.

## Sources

- Marc Chamberland, "The Erdős-Straus Conjecture and the Structure of Primes", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.ErdosStrausPrimeStructureWanted.erdos_straus_prime_restricted_representation_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosStrausPrimeStructureWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosStrausPrimeStructureWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture/index.html#erdos-straus-prime-restricted-representa).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Erdős–Straus conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/diophantine-tuples-egyptian/erd-s-straus-conjecture)
