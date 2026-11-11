---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimeCounting.BrunTitchmarshUniformWanted.brun_titchmarsh_uniform, MathlibExt.NumberTheory.PrimeCounting.moebiusSq_div_totient_sum_gt_log, MathlibExt.NumberTheory.PrimeCounting.squarefreeTotientWeightedLower, MathlibExt.NumberTheory.PrimeCounting.BrunTitchmarshWanted.brun_titchmarsh
statement: formalized
proof: formalized
---

# Brun–Titchmarsh theorem

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem/index.html).

## Uniform Brun–Titchmarsh bound

Write $\pi(X; k, \ell)$ for the number of primes $p \le X$
with $p \equiv \ell \pmod{k}$, and $\varphi$ for Euler's totient function. For every real $\beta$
with $0 < \beta < 1$ there is a real constant $\xi_1 > 0$ such that for all natural numbers $X$,
$k$ and $\ell$ with $X \ge 2$, $k \ge 1$ and $k \le X^{\beta}$,

$$
\pi(X; k, \ell) < \frac{\xi_1 X}{\varphi(k) \log(X/k)}.
$$

No coprimality of $k$ and $\ell$ is assumed.

The proof applies Selberg's $\Lambda^2$ upper-bound sieve to the arithmetic progression, with
optimized weights and a harmonic lower bound for the diagonal sum.

## Sources

- Jean-Marie De Koninck and Imre Kátai, "Some Remarks on a Paper of L. Toth," Journal of Integer Sequences 13 (2010), <https://cs.uwaterloo.ca/journals/JIS/VOL13/DeKoninck/dekoninck7.tex>, Lemma, lines 424–429. The source cites E. C. Titchmarsh, "A divisor problem," Rend. Palermo 54 (1930), 414–429 and 57 (1933), 478–479. The bound `2 ≤ X` makes the source's implicit analytic lower range explicit, and the source prints no coprimality hypothesis.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.BrunTitchmarshUniformWanted.brun_titchmarsh_uniform`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/BrunTitchmarshUniform.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunTitchmarshUniform.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem/index.html#brun-titchmarsh-uniform).

## Lower bound for the squarefree totient sum

For every natural number $z \ge 6$,
$\log(z + 1) + 107/100 < \sum_{r=1}^{z} \mu(r)^2 / \varphi(r)$, where $\mu$ is the Möbius
function and $\varphi$ is Euler's totient function.

## Sources

- Montgomery–Vaughan, *The large sieve* (1973), Lemmas 4–7 and equation (4.3), lines 462–657. The bound here uses `log (z + 1)`, which is slightly stronger than the paper's `log z`.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.moebiusSq_div_totient_sum_gt_log`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/SquarefreeTotient.lean, line 1027](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/SquarefreeTotient.lean#L1027). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem/index.html#moebius-sq-div-totient-sum-gt-log).

## Weighted lower bound for the squarefree totient sum

For every natural number $z \ge 100$,
$\log z + 36/100 < \sum_{q=1}^{z} (1 + q/z)^{-1} \, \mu(q)^2 / \varphi(q)$, where $\mu$ is the
Möbius function and $\varphi$ is Euler's totient function.

## Sources

- Montgomery–Vaughan, *The large sieve* (1973), Lemma 8, lines 658–714. The proof uses Abel summation, `moebiusSq_div_totient_sum_gt_log`, and the paper's explicit correction from the terms `q ≤ 5`.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.squarefreeTotientWeightedLower`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/SquarefreeTotientWeighted.lean, line 419](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/SquarefreeTotientWeighted.lean#L419). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem/index.html#squarefree-totient-weighted-lower).

## Brun–Titchmarsh inequality

Let $X$, $q$ and $a$ be natural numbers such that $a$ and $q$
are coprime and $1 \le q < X$. Write $\pi(X; q, a)$ for the number of primes $p \le X$ with
$p \equiv a \pmod{q}$, and $\varphi$ for Euler's totient function. Then

$$
\pi(X; q, a) \le \frac{2X}{\varphi(q) \log(X/q)}.
$$

The proof uses an elementary Eratosthenes sieve when $X \le 20000q$. For larger $X$ it combines
the weighted arithmetic large sieve with explicit lower bounds for the squarefree-totient sum and
the choice $z = \lfloor \sqrt{2N/3} \rfloor$, where $N = \lfloor X/q \rfloor + 1$.

## Sources

- H. Iwaniec and E. Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, 2004, Theorem 6.6; quoted as equation (1) in Y. Wang and X. Zhang, arXiv:2608.19262v1.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.BrunTitchmarshWanted.brun_titchmarsh`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/BrunTitchmarsh.lean, line 1450](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunTitchmarsh.lean#L1450). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem/index.html#brun-titchmarsh).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brun–Titchmarsh theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/brun-titchmarsh-theorem)
