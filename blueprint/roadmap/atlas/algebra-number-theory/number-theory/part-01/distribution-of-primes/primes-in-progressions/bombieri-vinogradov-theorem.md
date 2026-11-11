---
declaration: section
origin: cited
lean: MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovResidueError, MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovMaxResidueError, MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovMaxUpToError, MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovSum, MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradov
statement: formalized
---

# Bombieri–Vinogradov theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html).

## Residue-class error of Chebyshev's function

For natural numbers $y$, $q$ and $a$, the
residue-class error is $E(y; q, a) = \left|\psi(y; q, a) - y/\varphi(q)\right|$, where
$\psi(y; q, a)$ is Chebyshev's function in the residue class of $a$ modulo $q$ and $\varphi$ is
Euler's totient function.

## Sources

- S. Baier and L. Zhao, *Bombieri-Vinogradov Type Theorem for Sparse Sets of Moduli*, arXiv:math/0602116, classical theorem display (1.1).

Formalized by `MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovResidueError`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html#bombieri-vinogradov-residue-error).

## Maximal residue-class error

For natural numbers $y$ and $q$, $E^{\ast}(y; q)$ is the
maximum of the residue-class error $E(y; q, a)$ over the natural numbers $a < q$ coprime to $q$,
and $0$ if there is no such $a$.

## Sources

- S. Baier and L. Zhao, *Bombieri-Vinogradov Type Theorem for Sparse Sets of Moduli*, arXiv:math/0602116, inner maximum of display (1.1).

Formalized by `MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovMaxResidueError`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html#bombieri-vinogradov-max-residue-error).

## Maximal residue-class error up to a level

For natural numbers $x$ and $q$,
$E^{\ast\ast}(x; q)$ is the maximum of the maximal residue-class error $E^{\ast}(y; q)$ over the
natural numbers $y \le x$.

## Sources

- S. Baier and L. Zhao, *Bombieri-Vinogradov Type Theorem for Sparse Sets of Moduli*, arXiv:math/0602116, maximum over `y ≤ x` in display (1.1).

Formalized by `MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovMaxUpToError`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html#bombieri-vinogradov-max-up-to-error).

## Bombieri–Vinogradov sum

For a natural number $x$ and a real number $A$, the
Bombieri–Vinogradov sum $S(x, A)$ is the sum of the maximal residue-class error
$E^{\ast\ast}(x; q)$ up to $x$ over the integers $q$ with $1 \le q \le x$ and
$q \le \sqrt{x} / (\log x)^{A + 5}$.

When $A > -5$ and $x \ge 3$, the condition $q \le x$ follows from the other one.

## Sources

- S. Baier and L. Zhao, *Bombieri-Vinogradov Type Theorem for Sparse Sets of Moduli*, arXiv:math/0602116, outer sum of display (1.1).

Formalized by `MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradovSum`, a definition declared in [WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html#bombieri-vinogradov-sum).

## Bombieri–Vinogradov theorem

Let $\psi(y; q, a)$ denote Chebyshev's function in the
residue class of $a$ modulo $q$, and let $\varphi$ be Euler's totient function. For a natural
number $x$ and a real number $A$, let $S(x, A)$ be the sum, over the integers $q$ with
$1 \le q \le x$ and $q \le \sqrt{x} / (\log x)^{A + 5}$, of the maximum of
$\left|\psi(y; q, a) - y/\varphi(q)\right|$ over the natural numbers $y \le x$ and $a < q$
coprime to $q$. Then for every real number $A > 0$ there are a real number $C > 0$ and a natural
number $x_0$ such that every natural number $x \ge x_0$ satisfies $S(x, A) \le C x / (\log x)^A$.

The main term $y/\varphi(q)$ depends on the inner variable $y$; it is not a
logarithmic-integral term depending on $x$.

## Sources

- S. Baier and L. Zhao, *Bombieri-Vinogradov Type Theorem for Sparse Sets of Moduli*, arXiv:math/0602116, classical theorem display (1.1), source lines 54–62.

Stated but not proved: `MetaMathlibExt.NumberTheory.PrimeCounting.bombieriVinogradov` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BombieriVinogradovWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html#bombieri-vinogradov).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bombieri–Vinogradov theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/bombieri-vinogradov-theorem)
