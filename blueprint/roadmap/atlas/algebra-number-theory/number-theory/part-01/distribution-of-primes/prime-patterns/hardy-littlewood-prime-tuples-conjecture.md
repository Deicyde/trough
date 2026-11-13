---
declaration: section
origin: cited
lean: MetaMathlibExt.hardyLittlewoodResidueCount, MetaMathlibExt.IsHardyLittlewoodAdmissible, MetaMathlibExt.hardyLittlewoodPrimeTupleCount, MetaMathlibExt.hardyLittlewoodEulerFactor, MetaMathlibExt.hardyLittlewoodSingularSeries, MetaMathlibExt.IsAdmissibleFinset, MetaMathlibExt.hardyLittlewoodResidueCount_ne_iff, MetaMathlibExt.isHardyLittlewoodAdmissible_iff_isAdmissibleFinset
statement: formalized
---

# Hardy–Littlewood prime tuples conjecture

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html).

## Number of residue classes met by an integer tuple

For an $m$-tuple
$b = (b_1, \dots, b_m)$ of integers and a natural number $p$, $v_p(b)$ is the number of distinct
values among the remainders $b_1 \bmod p, \dots, b_m \bmod p$, that is, the number of residue
classes modulo $p$ that contain an entry of $b$.

Formalized by `MetaMathlibExt.hardyLittlewoodResidueCount`, a definition declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#hardy-littlewood-residue-count).

## Hardy–Littlewood admissible tuples

An $m$-tuple $b$ of integers is admissible when
$v_p(b) \ne p$ for every prime $p$, where $v_p(b)$ is the number of residue classes modulo $p$
that contain an entry of $b$.

Formalized by `MetaMathlibExt.IsHardyLittlewoodAdmissible`, a definition declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#is-hardy-littlewood-admissible).

## The prime-tuple counting function

For an $m$-tuple $b = (b_1, \dots, b_m)$ of
integers and a natural number $x$, $P(x; b)$ is the number of integers $n$ with $1 \le n \le x$
such that each of $n + b_1, \dots, n + b_m$ is a (positive) prime number.

Formalized by `MetaMathlibExt.hardyLittlewoodPrimeTupleCount`, a definition declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#hardy-littlewood-prime-tuple-count).

## Euler factors of the Hardy–Littlewood singular series

For an $m$-tuple $b$ of
integers and a natural number $p$, the Euler factor of $b$ at $p$ is the real number

$$\left(\frac{p}{p-1}\right)^{m-1} \frac{p - v_p(b)}{p - 1},$$

where $v_p(b)$ is the number of residue classes modulo $p$ that contain an entry of $b$, the
exponent $m - 1$ is truncated at $0$ (so it is $0$ when $m = 0$), and division by $0$ gives $0$.

Formalized by `MetaMathlibExt.hardyLittlewoodEulerFactor`, a definition declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#hardy-littlewood-euler-factor).

## The Hardy–Littlewood singular series

For an $m$-tuple $b$ of integers, the singular
series $\mathfrak{S}(b)$ is the product over all primes $p$ of the Euler factors

$$\left(\frac{p}{p-1}\right)^{m-1} \frac{p - v_p(b)}{p - 1},$$

where $v_p(b)$ is the number of residue classes modulo $p$ that contain an entry of $b$ and the
exponent $m - 1$ is truncated at $0$. The product is the limit in $\mathbb{R}$ of the products
over finite sets $S$ of primes, with the sets $S$ directed by inclusion; this limit may be $0$
(for instance when some Euler factor is $0$), and $\mathfrak{S}(b)$ is $1$ when the limit does
not exist.

Formalized by `MetaMathlibExt.hardyLittlewoodSingularSeries`, a definition declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#hardy-littlewood-singular-series).

## Admissible finite sets of integers

A finite set $H$ of integers is admissible if
for every prime $p$ there is a residue class $r$ modulo $p$ that contains no element of $H$.

A tuple of integers is called Hardy–Littlewood admissible when, for every prime $p$, its entries
meet fewer than $p$ residue classes modulo $p$; this holds exactly when its set of entries is
admissible.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 1.

Formalized by `MetaMathlibExt.IsAdmissibleFinset`, a definition declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#is-admissible-finset).

## Missing a residue class modulo a prime

Let $b = (b_1, \dots, b_m)$ be an $m$-tuple of
integers, let $p$ be a prime, and let $v_p(b)$ be the number of residue classes modulo $p$ that
contain an entry of $b$. Then $v_p(b) \ne p$ if and only if there is a residue class $r$ modulo
$p$ with $b_i \not\equiv r \pmod p$ for every $i$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 1.

Formalized by `MetaMathlibExt.hardyLittlewoodResidueCount_ne_iff`, a theorem declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#hardy-littlewood-residue-count-ne-iff).

## Hardy–Littlewood admissibility via the set of entries

A tuple of integers is
Hardy–Littlewood admissible exactly when its set of entries is admissible.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 1.

Formalized by `MetaMathlibExt.isHardyLittlewoodAdmissible_iff_isAdmissibleFinset`, a theorem declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#is-hardy-littlewood-admissible-iff-is-ad).

## The empty set is admissible

The empty set of integers is admissible: for every prime
$p$, some residue class modulo $p$ contains none of its elements.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 1.

Formalized by `MetaMathlibExt.isAdmissibleFinset_empty`, a theorem declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#is-admissible-finset-empty).

## The set $\{0\}$ is admissible

The one-element set $\{0\}$ of integers is admissible:
for every prime $p$ it misses the residue class of $1$ modulo $p$.

## Sources

- Carol Wu, *On Smooth Gaps between Primes Using the Maynard-Tao Sieve*, INTEGERS 25 (2025), Article A44, Definition 1.

Formalized by `MetaMathlibExt.isAdmissibleFinset_singleton_zero`, a theorem declared in [MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/HardyLittlewoodPrimeTuple.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#is-admissible-finset-singleton-zero).

## Hardy–Littlewood prime-tuple conjecture

Let $m \ge 1$ and let $b = (b_1, \dots, b_m)$ be
an admissible $m$-tuple of pairwise distinct integers. Then the singular series $\mathfrak{S}(b)$
is nonzero, and the prime-tuple count $P(x; b)$, the number of integers $n$ with $1 \le n \le x$
such that $n + b_1, \dots, n + b_m$ are all prime, satisfies

$$P(x; b) \sim \mathfrak{S}(b) \int_2^x \frac{du}{(\log u)^m}$$

as the natural number $x$ tends to infinity.

## Sources

- Hùng Việt Chu, Nathan McNew, Steven J. Miller, Victor Xu, and Sean Zhang, *When Sets Can and Cannot Have Sum-Dominant Subsets*, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Miller/miller8.tex>.

Stated but not proved: `MetaMathlibExt.hardyLittlewoodPrimeTupleConjecture` is written with `theorem_wanted` in [WantedExt/NumberTheory/HardyLittlewoodPrimeTupleWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HardyLittlewoodPrimeTupleWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html#hardy-littlewood-prime-tuple-conjecture).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hardy–Littlewood prime tuples conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-patterns/hardy-littlewood-prime-tuples-conjecture)
