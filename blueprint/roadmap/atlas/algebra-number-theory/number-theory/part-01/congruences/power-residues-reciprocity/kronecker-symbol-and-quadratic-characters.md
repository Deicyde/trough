---
declaration: section
origin: cited
lean: MetaMathlibExt.IsFundamentalDiscriminant, MetaMathlibExt.kroneckerAtTwo, MetaMathlibExt.kroneckerAtPrime, MetaMathlibExt.kroneckerSym, MetaMathlibExt.kroneckerSym_prime, MetaMathlibExt.kroneckerSym_eq_jacobiSym_of_prime_ne_two, MetaMathlibExt.quadraticDirichletCharacter, MetaMathlibExt.jacobiSym_natAbs_eq_kroneckerSym_of_prime_ne_two_of_one_mod_four_pos
statement: formalized
proof: formalized
---

# Kronecker symbol and quadratic characters

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html).

## Fundamental discriminant

An integer $D$ is a fundamental discriminant if either $D$ is
squarefree and $D \equiv 1 \pmod 4$, or $D = 4m$ for some squarefree integer $m$ with
$m \equiv 2 \pmod 4$ or $m \equiv 3 \pmod 4$.

With this definition $D = 1$ is a fundamental discriminant and $D = 0$ is not.

Formalized by `MetaMathlibExt.IsFundamentalDiscriminant`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#is-fundamental-discriminant).

## Kronecker symbol at two

For an integer $D$, the Kronecker symbol of $D$ at $2$ is $0$
if $D$ is even, $1$ if $D \equiv \pm 1 \pmod 8$, and $-1$ if $D \equiv \pm 3 \pmod 8$.

Formalized by `MetaMathlibExt.kroneckerAtTwo`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#kronecker-at-two).

## Kronecker symbol at a prime

For an integer $D$ and a natural number $p$, the Kronecker
symbol of $D$ at $p$ is the Kronecker symbol of $D$ at two if $p = 2$, the Legendre symbol
$\left(\frac{D}{p}\right)$ if $p$ is an odd prime, and $0$ if $p$ is not prime.

Formalized by `MetaMathlibExt.kroneckerAtPrime`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#kronecker-at-prime).

## Kronecker symbol

For an integer $D$ and a natural number $n$, the Kronecker symbol
$\left(\frac{D}{n}\right)$ is defined as follows. If $n = 0$, it is $1$ when $D = \pm 1$ and $0$
otherwise. If $n \ge 1$ and $n = p_1 p_2 \cdots p_k$ is the factorization of $n$ into primes,
listed with multiplicity, it is the product of the Kronecker symbols of $D$ at the primes
$p_1, \ldots, p_k$ (the empty product $1$ when $n = 1$).

Formalized by `MetaMathlibExt.kroneckerSym`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#kronecker-sym).

## Kronecker symbol with a prime denominator

For every integer $D$ and every prime $p$,
the Kronecker symbol $\left(\frac{D}{p}\right)$ equals the Kronecker symbol of $D$ at the
prime $p$.

Formalized by `MetaMathlibExt.kroneckerSym_prime`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/Quadratic.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#kronecker-sym-prime).

## Kronecker and Jacobi symbols agree at odd primes

For every integer $D$ and every prime
$p \ne 2$, the Kronecker symbol $\left(\frac{D}{p}\right)$ equals the Jacobi symbol
$\left(\frac{D}{p}\right)$.

Formalized by `MetaMathlibExt.kroneckerSym_eq_jacobiSym_of_prime_ne_two`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticCharacterAux.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticCharacterAux.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#kronecker-sym-eq-jacobi-sym-of-prime-ne).

## Quadratic Dirichlet character of a fundamental discriminant

Let $D$ be a fundamental
discriminant. Then there is a unique integer-valued Dirichlet character $\chi$ modulo $|D|$ such
that $\chi(n \bmod |D|) = \left(\frac{D}{n}\right)$ for every natural number $n$, where
$\left(\frac{D}{n}\right)$ is the Kronecker symbol.

## Sources

- Joshua Males, Andreas Mono, Larry Rolen, and Ian Wagner, *Central L-values of newforms and local polynomials*, arXiv:2306.15519v5, subsection "L-functions and L-values", line 455. Exact source sentence: "One may also consider L-functions associated to a Dirichlet character chi_D = (D / dot), namely ...". This is the existence and uniqueness of the integer-valued Dirichlet character of level `Int.natAbs D` evaluating as the positive-denominator Kronecker symbol `kroneckerSym D` at every natural `n`, assuming `IsFundamentalDiscriminant D`. No primitivity or conductor claim belongs to this item.

Formalized by `MetaMathlibExt.quadraticDirichletCharacter`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticDirichletCharacter.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticDirichletCharacter.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#quadratic-dirichlet-character).

## Quadratic reciprocity for the Kronecker symbol, positive $D \equiv 1 \pmod 4$

Let $D$ be a
positive integer with $D \equiv 1 \pmod 4$ and let $p$ be an odd prime. Then the Jacobi symbol
$\left(\frac{p}{|D|}\right)$ equals the Kronecker symbol $\left(\frac{D}{p}\right)$.

The congruence condition cannot be dropped: for $D = 3$ and $p = 7$ the Jacobi symbol
$\left(\frac{7}{3}\right)$ is $1$, while the Kronecker symbol $\left(\frac{3}{7}\right)$ is
$-1$.

Formalized by `MetaMathlibExt.jacobiSym_natAbs_eq_kroneckerSym_of_prime_ne_two_of_one_mod_four_pos`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridge.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridge.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#jacobi-sym-nat-abs-eq-kronecker-sym-of-p).

## Kronecker symbol at odd primes for negative integers congruent to 1 mod 4

Let $D$ be a
negative integer with $D \equiv 1 \pmod 4$ and let $p$ be an odd prime. Then the Jacobi symbol
$\left(\frac{p}{|D|}\right)$ equals the Kronecker symbol $\left(\frac{D}{p}\right)$.

Formalized by `MetaMathlibExt.jacobiSym_natAbs_eq_kroneckerSym_of_prime_ne_two_of_one_mod_four_neg`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeNeg.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeNeg.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#jacobi-sym-nat-abs-eq-kronecker-sym-of-p-2).

## Kronecker symbol at odd primes for integers congruent to 1 mod 4

Let $D$ be an integer
with $D \equiv 1 \pmod 4$ and let $p$ be an odd prime. Then the Jacobi symbol
$\left(\frac{p}{|D|}\right)$ equals the Kronecker symbol $\left(\frac{D}{p}\right)$.

This covers $D$ of either sign. The congruence condition cannot be dropped: for $D = 3$ and
$p = 7$ the Jacobi symbol is $1$ while the Kronecker symbol is $-1$.

Formalized by `MetaMathlibExt.jacobiSym_natAbs_eq_kroneckerSym_of_prime_ne_two_of_one_mod_four`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeNeg.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeNeg.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#jacobi-sym-nat-abs-eq-kronecker-sym-of-p-3).

## Kronecker symbol at odd numbers for integers congruent to 3 mod 4

Let $\chi_4$ be the
nontrivial Dirichlet character modulo $4$, so $\chi_4(n) = 1$ for $n \equiv 1 \pmod 4$ and
$\chi_4(n) = -1$ for $n \equiv 3 \pmod 4$. Let $D$ be an integer with $D \equiv 3 \pmod 4$ and
let $p$ be an odd natural number. Then $\chi_4(p) \cdot \left(\frac{p}{|D|}\right) =
\left(\frac{D}{p}\right)$, where $\left(\frac{p}{|D|}\right)$ is the Jacobi symbol and
$\left(\frac{D}{p}\right)$ is the Kronecker symbol.

For $D > 0$ the factor $\chi_4(p)$ is the sign from quadratic reciprocity; for $D < 0$ it is
the value $\left(\frac{-1}{p}\right) = \chi_4(p)$.

Formalized by `MetaMathlibExt.chi4_mul_jacobiSym_natAbs_eq_kroneckerSym_of_odd_of_three_mod_four`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityThreeOdd.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityThreeOdd.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#chi4-mul-jacobi-sym-nat-abs-eq-kronecker).

## Jacobi symbol of $4m$ at an odd denominator

For every integer $m$ and every odd natural
number $p$, the Jacobi symbol $\left(\frac{4m}{p}\right)$ equals $\left(\frac{m}{p}\right)$.

Formalized by `MetaMathlibExt.jacobiSym_four_mul_of_odd`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeFour.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeFour.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#jacobi-sym-four-mul-of-odd).

## Jacobi symbol of $2m$ at an odd denominator

For every integer $m$ and every odd natural
number $p$, the Jacobi symbol $\left(\frac{2m}{p}\right)$ equals
$\chi_8(p) \left(\frac{m}{p}\right)$, where $\chi_8$ is the Dirichlet character modulo $8$ with
$\chi_8(n) = 1$ for $n \equiv \pm 1 \pmod 8$, $\chi_8(n) = -1$ for $n \equiv \pm 3 \pmod 8$, and
$\chi_8(n) = 0$ for even $n$.

Formalized by `MetaMathlibExt.jacobiSym_two_mul_of_odd`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeFour.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeFour.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#jacobi-sym-two-mul-of-odd).

## Kronecker–Jacobi bridge for 4m with m ≡ 3 mod 4

Even `m % 4 = 3` subcase for odd `p`: reduce `4 * m` to `m`, identify
`kroneckerSym` with `jacobiSym` at odd denominators, then apply the `D % 4 = 3`
bridge to `m` itself. Covers prime and composite odd denominators alike.

Formalized by `MetaMathlibExt.chi4_mul_jacobiSym_natAbs_eq_kroneckerSym_of_odd_of_four_mul_three_mod_four`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeFour.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/DirichletCharacter/QuadraticReciprocityBridgeFour.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html#kronecker-jacobi-bridge-for-4m-with-m-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kronecker symbol and quadratic characters](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/power-residues-reciprocity/kronecker-symbol-and-quadratic-characters)
