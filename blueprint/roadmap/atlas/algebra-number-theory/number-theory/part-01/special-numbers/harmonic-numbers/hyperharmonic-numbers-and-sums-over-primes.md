---
declaration: section
origin: cited
lean: MetaMathlibExt.hyperharmonic, MetaMathlibExt.hyperharmonic_succ, MetaMathlibExt.hyperharmonic_one, MetaMathlibExt.hyperharmonic_two_two, MetaMathlibExt.hyperharmonic_isEquivalent, MetaMathlibExt.sum_isEquivalent_of_isEquivalent, MetaMathlibExt.nth_kPrimeFactors_isEquivalent, MetaMathlibExt.sum_pow_mul_log_pow_isEquivalent
statement: formalized
---

# Hyperharmonic numbers and sums over primes

41 results, 25 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html).

## Hyperharmonic numbers

The hyperharmonic numbers $h_n^{(r)} \in \mathbb{Q}$ of order $r$
and index $n$, for natural numbers $r$ and $n$, are defined by recursion on $r$:
$h_n^{(0)} = 1/n$ for $n \ge 1$, $h_0^{(0)} = 0$, and

$$h_n^{(r+1)} = \sum_{k=1}^{n} h_k^{(r)}.$$

Thus $h_0^{(r)} = 0$ for every order $r$, and $h_n^{(1)} = 1 + 1/2 + \dots + 1/n$ is the $n$-th
harmonic number $H_n$. This is the definition of Conway and Guy.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 1 (hyperharmonic numbers `h_n^{(r)}`, after Mező).

Formalized by `MetaMathlibExt.hyperharmonic`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#hyperharmonic).

## Recursion for the hyperharmonic numbers

For all natural numbers $r$ and $n$, the
hyperharmonic numbers $h_m^{(s)}$ (of order $s$ and index $m$) satisfy

$$h_n^{(r+1)} = \sum_{k=1}^{n} h_k^{(r)}.$$

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 1 (hyperharmonic numbers `h_n^{(r)}`, after Mező).

Formalized by `MetaMathlibExt.hyperharmonic_succ`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#hyperharmonic-succ).

## Hyperharmonic numbers of order one are the harmonic numbers

For every natural number $n$,
the hyperharmonic number $h_n^{(1)}$ of order $1$ and index $n$ equals the $n$-th harmonic number
$H_n = \sum_{k=1}^{n} 1/k$ (in particular $h_0^{(1)} = H_0 = 0$).

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 1 (hyperharmonic numbers `h_n^{(r)}`, after Mező).

Formalized by `MetaMathlibExt.hyperharmonic_one`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#hyperharmonic-one).

## The hyperharmonic number $h_2^{(2)}$

The hyperharmonic number of order $2$ and index $2$
is $h_2^{(2)} = 5/2$.

Indeed $h_2^{(2)} = h_1^{(1)} + h_2^{(1)} = H_1 + H_2 = 1 + 3/2$, where $H_n$ is the $n$-th
harmonic number.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 1 (hyperharmonic numbers `h_n^{(r)}`, after Mező).

Formalized by `MetaMathlibExt.hyperharmonic_two_two`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#hyperharmonic-two-two).

## Asymptotic of the hyperharmonic numbers (Mező)

For every natural number $r \ge 1$, the
hyperharmonic numbers $h_n^{(r)}$ of order $r$ are asymptotically equivalent, as $n \to \infty$,
to $n^{r-1} \log n / (r-1)!$, where $\log$ is the natural logarithm:

$$h_n^{(r)} \sim \frac{n^{r-1} \log n}{(r-1)!} \qquad (n \to \infty).$$

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 1 (`jis-2024-24.4.1-lem-1`).

Stated but not proved: `MetaMathlibExt.hyperharmonic_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#hyperharmonic-is-equivalent).

## Jakimczuk's lemma on sums of asymptotically equivalent terms

Let $(a_i)_{i \ge 0}$ and
$(b_i)_{i \ge 0}$ be real sequences with $a_i > 0$ and $b_i > 0$ for every $i \ge 1$. If
$a_i \sim b_i$ as $i \to \infty$ and $\sum_{i=1}^{n} b_i \to +\infty$ as $n \to \infty$, then

$$\sum_{i=1}^{n} a_i \sim \sum_{i=1}^{n} b_i \qquad (n \to \infty).$$

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 7 (`jis-2024-24.4.1-lem-7`).

Stated but not proved: `MetaMathlibExt.sum_isEquivalent_of_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-is-equivalent-of-is-equivalent).

## Asymptotics of the $n$-th number with $k$ prime factors

Let $k \ge 1$. For $n \ge 1$ let
$p_{n,k}$ be the $n$-th squarefree natural number with exactly $k$ distinct prime factors, and let
$q_{n,k}$ be the $n$-th natural number with exactly $k$ prime factors counted with multiplicity
(that is, $\Omega(q_{n,k}) = k$). Then, as $n \to \infty$,
$p_{n,k} \sim q_{n,k} \sim (k-1)!\, n \log n / (\log \log n)^{k-1}$ and
$p_{n,k} (\log \log p_{n,k})^{k-1} \sim q_{n,k} (\log \log q_{n,k})^{k-1} \sim (k-1)!\, n \log n$.
Moreover the $n$-th prime $p_n$ satisfies $p_n \sim n \log n$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 8 (`jis-2024-24.4.1-lem-8`).

Stated but not proved: `MetaMathlibExt.nth_kPrimeFactors_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#nth-k-prime-factors-is-equivalent).

## Asymptotics of power-logarithm sums

For all $m, n, k \in \mathbb{N}$, as the natural
number $x$ tends to infinity,

$$\sum_{\ell=1}^{x} \ell^m (\log \ell)^n \sim \frac{x^{m+1} (\log x)^n}{m+1}$$

and

$$\sum_{\ell=1}^{x} \frac{\ell^m (\log \ell)^n}{(\log \log \ell)^k} \sim
\frac{x^{m+1} (\log x)^n}{(m+1)(\log \log x)^k}.$$

In the second sum the term $\ell = 1$, where $\log \log 1 = \log 0$ is undefined, is evaluated with
the conventions $\log 0 = 0$ and $t/0 = 0$; a single term does not affect the asymptotic.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 9 (`jis-2024-24.4.1-lem-9`).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_log_pow_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-pow-mul-log-pow-is-equivalent).

## Alternating generalized harmonic numbers

For a real number $s$ and a natural number $n$,
the alternating generalized harmonic number is
$\overline{H}_n^{(s)} = \sum_{j=1}^{n} (-1)^{j-1} / j^s$, which is $0$ for $n = 0$.

For $s = -p$ with $p$ a natural number this is $\sum_{j=1}^{n} (-1)^{j-1} j^p$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Section 1 (definition of `H̄_n^{(p)}` and `H̄_n^{(-p)}`).

Formalized by `MetaMathlibExt.alternatingGeneralizedHarmonic`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-generalized-harmonic).

## Alternating generalized harmonic numbers of index zero

For every real number $s$, the
alternating generalized harmonic number $\overline{H}_0^{(s)}$ is $0$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Section 1 (definition of `H̄_n^{(p)}`).

Formalized by `MetaMathlibExt.alternatingGeneralizedHarmonic_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-generalized-harmonic-zero).

## Signed iterated partial sums

Let $(b_n)_{n \ge 0}$ be a real sequence and fix a choice of
signs, either alternating, $\varepsilon_k = (-1)^{k-1}$, or constant, $\varepsilon_k = 1$. The
signed iterated partial sums $S^{(r)}_n$ of $b$, for orders $r \in \mathbb{N}$ and
$n \in \mathbb{N}$, are defined by $S^{(0)}_n = 0$, $S^{(1)}_n = b_n$ and, for $r \ge 1$,

$$S^{(r+1)}_n = \sum_{k=1}^{n} \varepsilon_k \, S^{(r)}_k.$$

The value $0$ at order $0$ is a convention and is not used.

With $b_n = H_n^{(p)} = \sum_{j=1}^{n} j^{-p}$, constant signs give the generalized hyperharmonic
numbers $H_n^{(p,r)}$ and alternating signs give the type I alternating ones $H_n^{(p,r,1)}$; with
$b_n = \bar H_n^{(p)} = \sum_{j=1}^{n} (-1)^{j-1} j^{-p}$, constant signs give type II,
$H_n^{(p,r,2)}$, and alternating signs give type III, $H_n^{(p,r,3)}$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Section 1 (definitions of `H_n^{(p,r)}` and `H_n^{(p,r,i)}`, `i = 1, 2, 3`).

Formalized by `MetaMathlibExt.signedIteratedPartialSum`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#signed-iterated-partial-sum).

## Order one of the signed iterated partial sums

For every real sequence
$(b_n)_{n \ge 0}$, either choice of signs and every $n \in \mathbb{N}$, the signed iterated partial
sum of $b$ of order $1$ at $n$ equals $b_n$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Section 1 (`H_n^{(p,1)} = H_n^{(p)}`, `H_n^{(p,1,1)} = H_n^{(p)}`, `H_n^{(p,1,2)} = H_n^{(p,1,3)} = H̄_n^{(p)}`).

Formalized by `MetaMathlibExt.signedIteratedPartialSum_one`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#signed-iterated-partial-sum-one).

## Recursion for the signed iterated partial sums

Let $(b_n)_{n \ge 0}$ be a real sequence,
fix a choice of signs, either $\varepsilon_k = (-1)^{k-1}$ for all $k$ or $\varepsilon_k = 1$ for
all $k$, and let $S^{(r)}_n$ denote the signed iterated partial sum of $b$ of order $r$ at $n$ for
this choice. Then for every $r \ge 1$ and every $n \in \mathbb{N}$,

$$S^{(r+1)}_n = \sum_{k=1}^{n} \varepsilon_k \, S^{(r)}_k.$$

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Section 1 (definitions of `H_n^{(p,r)}` and `H_n^{(p,r,i)}`).

Formalized by `MetaMathlibExt.signedIteratedPartialSum_succ`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#signed-iterated-partial-sum-succ).

## Alternating zeta values

For a natural number $p$, the alternating zeta value
$\bar\zeta(p)$ is defined by $\bar\zeta(1) = \log 2$, by $\bar\zeta(p) = (1 - 2^{1-p})\,\zeta(p)$
for $p \ge 2$, where $\zeta(p) = \sum_{n \ge 1} 1/n^p$, and by $\bar\zeta(0) = 0$.

For every $p \ge 1$ this is the alternating series $\bar\zeta(p) = \sum_{n \ge 1} (-1)^{n-1}/n^p$;
the value at $p = 0$ is not used.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 10 (definition of `ζ̄(s)`).

Formalized by `MetaMathlibExt.alternatingZeta`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-zeta).

## Alternating zeta value at one

The alternating zeta value at $1$ is $\bar\zeta(1) = \log 2$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 10 (definition of `ζ̄(s)`).

Formalized by `MetaMathlibExt.alternatingZeta_one`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-zeta-one).

## Li's coefficients $a(r, m, j)$

The rational numbers $a(r, m, j)$, for natural numbers
$r$, $m$, $j$, are defined by recursion on $r$. For all $m$ and $j$, $a(0, m, j) = 0$; moreover
$a(1, 0, 0) = 1$ and $a(1, m, j) = 0$ for $(m, j) \ne (0, 0)$. For $r \ge 1$ the values of
order $r + 1$ are as follows. First,

$$a(r+1, r, 0) = -\sum_{m=0}^{r-1} \frac{a(r, m, r-m-1)}{r-m}.$$

For $0 \le m \le r - 1$ and $1 \le \ell \le r - m$,

$$a(r+1,m,\ell) = \sum_{j=\ell-1}^{r-1-m} \frac{a(r,m,j)}{j+1} \binom{j+1}{j-\ell+1} B_{j-\ell+1}.$$

For $0 \le m \le r - 1$,

$$a(r+1, m, 0) = -\sum_{y=0}^{m} \sum_{j=\max(0, m-y-1)}^{r-1-y} a(r, y, j)\, D(m, j, y),$$

where

$$D(m, j, y) = \frac{1}{j+1} \sum_{\ell=\max(0, m-y-1)}^{j} \binom{j+1}{j-\ell} B_{j-\ell}
\binom{\ell+1}{m-y} (-1)^{1+\ell-m+y}.$$

All other values $a(r+1, m, \ell)$ are $0$. Here $B_n$ are the Bernoulli numbers with
$B_1 = 1/2$, that is, the numbers determined by $\sum_{j=0}^{k} \binom{k+1}{j} B_j = k + 1$ for
all $k \ge 0$.

Li writes $D(r, m, j, y)$; the value does not depend on $r$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 3 (quoting Li, *Euler sums of generalized hyperharmonic numbers*).

Formalized by `MetaMathlibExt.liCoeffA`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-a).

## The coefficient $a(1, 0, 0)$

The coefficient $a(1, 0, 0)$ of Li's Lemma 3 equals $1$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 3.

Formalized by `MetaMathlibExt.liCoeffA_one_zero_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-a-one-zero-zero).

## The coefficient $a(2, 1, 0)$

The coefficient $a(2, 1, 0)$ of Li's Lemma 3 equals $-1$.

By the recursion, $a(2, 1, 0) = -a(1, 0, 0) = -1$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 3.

Formalized by `MetaMathlibExt.liCoeffA_two_one_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-a-two-one-zero).

## Li's coefficients $c(m, j)$

For natural numbers $m$ and $j$, the rational number
$c(m, j)$ is $\frac{1}{m+1} \binom{m+1}{m+1-j} B_{m+1-j}$ when $j \le m + 1$ and $0$ otherwise,
where $B_i$ denotes the Bernoulli numbers with the convention $B_1 = +\frac{1}{2}$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffC`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-c).

## Li's coefficient $c(0, 0)$

Li's coefficient $c(0, 0)$ equals $\frac{1}{2}$ (this is the
Bernoulli number $B_1$ in the convention $B_1 = +\frac{1}{2}$).

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffC_zero_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-c-zero-zero).

## Li's coefficients $d(m, j)$

For natural numbers $m$ and $j$, the rational number
$d(m, j)$ is $\frac{1}{m+1} \sum_{k} \binom{m+1}{m-k} B_{m-k} \binom{1+k}{j} (-1)^{1+k-j}$, the sum
running over the natural numbers $k$ with $\max(j - 1, 0) \le k \le m$ (so $d(m, j) = 0$ when
$j > m + 1$), where $B_i$ denotes the Bernoulli numbers with the convention $B_1 = +\frac{1}{2}$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffD`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-d).

## Li's coefficient $d(0, 1)$

Li's coefficient $d(0, 1)$ equals $1$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffD_zero_one`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-d-zero-one).

## Li's coefficients $c_1(m, j)$

For natural numbers $m$ and $j$, the rational number
$c_1(m, j)$ is
$\frac{1}{2(m+1)} \sum_{k=0}^{m-j} \binom{m+1}{k} B_k 2^k \binom{m+1-k}{j} (-1)^{m-k-j}$ when
$j \le m$ and $0$ otherwise, where $B_i$ denotes the Bernoulli numbers with the convention
$B_1 = +\frac{1}{2}$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffC1`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-c1).

## Li's coefficient $c_1(0, 0)$

Li's coefficient $c_1(0, 0)$ equals $\frac{1}{2}$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffC1_zero_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-c1-zero-zero).

## Li's coefficients $d_1(m, j)$

For natural numbers $m$ and $j$,
$d_1(m, j) = \sum_{k=j}^{m} \binom{k}{j} (-1)^{k-j} c_1(m, k)$, where $c_1$ denotes Li's
coefficients $c_1(m, k)$; in particular $d_1(m, j) = 0$ when $j > m$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffD1`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-d1).

## Li's coefficient $d_1(0, 0)$

Li's coefficient $d_1(0, 0)$ equals $\frac{1}{2}$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 4.

Formalized by `MetaMathlibExt.liCoeffD1_zero_zero`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-d1-zero-zero).

## Li's coefficients $b_1(r, m, j, k)$

These rational numbers, indexed by natural numbers
$r, m, j, k$, are defined by recursion on $r$ from Li's coefficients $c$, $d$, $c_1$ and $d_1$.
All values $b_1(0, m, j, k)$ are $0$, $b_1(1, 0, 0, 2) = 1$, and all other values
$b_1(1, m, j, k)$ are $0$. For $s \ge 1$ let $G = \lfloor (s-1)/2 \rfloor$ and
$b(m, j, k) = b_1(s, m, j, k)$; then $b_1(s+1, m, j, k)$ is $0$ except in the following cases.

If $s$ is odd: for $k = 0$ the value is $\sum_{l=m}^{G} b(l, j, 2)\, c_1(l, m)$ when
$1 \le m \le G$ and $j \le G - m$, and $\sum_{l=0}^{G-j} b(l, j, 2)\, c_1(l, 0)$ when $m = 0$ and
$j \le G$. For $k = 1$ the value is $\sum_{l=m-1}^{G-1} b(l, j, 3)\, c(l, m)$ when
$1 \le m \le G$ and $j \le G - m$, and $S_1 + S_2 + b(0, j, 3) - S_3$ when $m = 0$ and $j \le G$,
where $S_1$ is the sum of $b(m', j_1, 2)\, d_1(m', j - j_1)$ over the pairs of natural numbers
$(m', j_1)$ with $m' \le G$, $j_1 \le G - m'$, $j_1 < j$ and $j - j_1 \le m'$,
$S_2 = \sum_{m'=0}^{G-j} b(m', j, 2)\, d_1(m', 0)$, and $S_3$ is the sum of
$b(m', j_1, 3)\, d(m', j - j_1)$ over the pairs with $m' < G$, $j_1 < G - m'$, $j_1 < j$ and
$j - j_1 \le m' + 1$.

If $s$ is even: for $k = 2$ the value is $\sum_{l=m-1}^{G} b(l, j, 0)\, c(l, m)$ when
$1 \le m \le G + 1$ and $j \le G + 1 - m$, and $-T_1 + T_2 + b(0, j, 0) + T_3$ when $m = 0$ and
$j \le G + 1$, where $T_1$ is the sum of $b(m', j_1, 0)\, d(m', j - j_1)$ over the pairs of
natural numbers $(m', j_1)$ with $m' \le G$, $j_1 \le G - m'$, $j_1 < j$ and $j - j_1 \le m' + 1$,
$T_2$ is the sum of $b(m', j, 1)\, d_1(m', 0)$ over $0 \le m' \le \max(G - j, 0)$, and $T_3$ is
the sum of $b(m', j_1, 1)\, d_1(m', j - j_1)$ over the pairs with $m' \le G$, $j_1 \le G - m'$,
$j_1 < j$ and $j - j_1 \le m'$. For $k = 3$ the value is $\sum_{l=m}^{G} b(l, j, 1)\, c_1(l, m)$
when $1 \le m \le G$ and $j \le G - m$, and $\sum_{l=0}^{G-j} b(l, j, 1)\, c_1(l, 0)$ when
$m = 0$ and $j \le G$.

In particular $b_1(r, m, j, 0) = b_1(r, m, j, 1) = 0$ for odd $r$,
$b_1(r, m, j, 2) = b_1(r, m, j, 3) = 0$ for even $r$, and $b_1(r, m, j, 3) = 0$ for odd $r$ when
$m + j = \lfloor (r-1)/2 \rfloor$. In Lemma 6 the second argument of $b_1$ is the exponent of $n$
and the third is the shift of $p$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 5 (with `c, d, c₁, d₁` from Definition 4).

Formalized by `MetaMathlibExt.liCoeffB1`, a definition declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-b1).

## The coefficient $b_1(1, 0, 0, 2)$

The coefficient $b_1(1, 0, 0, 2)$ of Li's
Definition 5 equals $1$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 5.

Formalized by `MetaMathlibExt.liCoeffB1_one_zero_zero_two`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-b1-one-zero-zero-two).

## The coefficient $b_1(1, 0, 0, 3)$

The coefficient $b_1(1, 0, 0, 3)$ of Li's
Definition 5 equals $0$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Definition 5.

Formalized by `MetaMathlibExt.liCoeffB1_one_zero_zero_three`, a theorem declared in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 368](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L368). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#li-coeff-b1-one-zero-zero-three).

## Asymptotic of generalized hyperharmonic numbers

For a natural number $p$ let
$H_n^{(p)} = \sum_{i=1}^{n} 1/i^p$ be the generalized harmonic numbers, and let the generalized
hyperharmonic numbers be $H_n^{(p,1)} = H_n^{(p)}$ and $H_n^{(p,r+1)} = \sum_{k=1}^{n} H_k^{(p,r)}$.
Then for all natural numbers $p \ge 2$ and $r \ge 1$, $H_n^{(p,r)} \sim n^{r-1} \zeta(p) / (r-1)!$
as $n \to \infty$, where $\zeta(p) = \sum_{i \ge 1} 1/i^p$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 2 (`jis-2024-24.4.1-lem-2`).

Stated but not proved: `MetaMathlibExt.generalizedHyperharmonic_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#generalized-hyperharmonic-is-equivalent).

## Explicit formula for type II alternating hyperharmonic numbers

For real $s$ write
$\overline{H}_n^{(s)} = \sum_{i=1}^{n} (-1)^{i-1}/i^s$ for the alternating generalized harmonic
numbers. For a natural number $p$, the type II generalized alternating hyperharmonic numbers are
$H_n^{(p,1,2)} = \overline{H}_n^{(p)}$ and $H_n^{(p,r+1,2)} = \sum_{k=1}^{n} H_k^{(p,r,2)}$. Let
$a(r, m, j)$ be Li's rational coefficients. Then for all natural numbers $r, n, p \ge 1$,

$$
H_n^{(p,r,2)} = \sum_{m=0}^{r-1} \sum_{j=0}^{r-1-m} a(r, m, j)\, n^j\, \overline{H}_n^{(p-m)},
$$

where the index $p - m$ is a real number and may be negative.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 3 (`jis-2024-24.4.1-lem-3`).

Stated but not proved: `MetaMathlibExt.alternatingHyperharmonic_typeII_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 387](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L387). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-hyperharmonic-type-ii-eq-sum).

## Explicit formulas for type I and type III alternating hyperharmonic numbers

For real $s$
write $H_n^{(s)} = \sum_{i=1}^{n} 1/i^s$ and $\overline{H}_n^{(s)} = \sum_{i=1}^{n} (-1)^{i-1}/i^s$
for the generalized and the alternating generalized harmonic numbers. For a natural number $p$,
the type I and type III generalized alternating hyperharmonic numbers are
$H_n^{(p,1,1)} = H_n^{(p)}$, $H_n^{(p,1,3)} = \overline{H}_n^{(p)}$ and, for $i = 1, 3$,
$H_n^{(p,r+1,i)} = \sum_{k=1}^{n} (-1)^{k-1} H_k^{(p,r,i)}$. Let $b_1(r, j, m, k)$ for
$k = 0, 1, 2, 3$ be Li's rational coefficients. Then for all natural numbers $r, n, p \ge 1$,
with $g = \lfloor (r-1)/2 \rfloor$ and $\varepsilon_n = (-1)^{n-1}$,

$$
H_n^{(p,r,1)} = \sum_{m=0}^{g} \sum_{j=0}^{g-m} \bigl(b_1(r,j,m,0)\,\varepsilon_n H_n^{(p-m)} +
b_1(r,j,m,1)\,\overline{H}_n^{(p-m)} + b_1(r,j,m,2)\,H_n^{(p-m)} +
b_1(r,j,m,3)\,\varepsilon_n \overline{H}_n^{(p-m)}\bigr)\, n^j
$$

and

$$
H_n^{(p,r,3)} = \sum_{m=0}^{g} \sum_{j=0}^{g-m} \bigl(b_1(r,j,m,0)\,\varepsilon_n
\overline{H}_n^{(p-m)} + b_1(r,j,m,1)\,H_n^{(p-m)} + b_1(r,j,m,2)\,\overline{H}_n^{(p-m)} +
b_1(r,j,m,3)\,\varepsilon_n H_n^{(p-m)}\bigr)\, n^j,
$$

where the index $p - m$ is a real number and may be negative.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 6 (`jis-2024-24.4.1-lem-6`).

Stated but not proved: `MetaMathlibExt.alternatingHyperharmonic_typeI_typeIII_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-hyperharmonic-type-i-type-ii).

## Asymptotics of type I alternating hyperharmonic numbers

For real $s$ let
$H_n^{(s)} = \sum_{i=1}^{n} 1/i^s$ be the generalized harmonic numbers, and let the type I
generalized alternating hyperharmonic numbers be $H_n^{(s,1,1)} = H_n^{(s)}$ and
$H_n^{(s,r+1,1)} = \sum_{k=1}^{n} (-1)^{k-1} H_k^{(s,r,1)}$. Let $y \ge 1$ and $p \ge 2$ be natural
numbers, let $\zeta(p) = \sum_{i \ge 1} 1/i^p$ and let $\bar\zeta(p)$ be the alternating zeta
value at $p$. Then, as $n \to \infty$,
$H_n^{(1,2y+1,1)} \sim n^y \log n / (2^y\, y!)$,
$H_n^{(p,2y+1,1)} \sim n^y \zeta(p) / (2^y\, y!)$,
$H_n^{(1,2y,1)} \sim (-1)^{n-1} n^{y-1} \log n / (2^y (y-1)!)$,
$H_{2n}^{(p,2y,1)} \sim -n^{y-1} (\zeta(p) - \bar\zeta(p)) / (2\,(y-1)!)$ and
$H_{2n-1}^{(p,2y,1)} \sim n^{y-1} (\zeta(p) + \bar\zeta(p)) / (2\,(y-1)!)$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 10 (`jis-2024-24.4.1-lem-10`).

Stated but not proved: `MetaMathlibExt.alternatingHyperharmonic_typeI_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 423](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L423). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-hyperharmonic-type-i-is-equi).

## Asymptotic of type II alternating hyperharmonic numbers

For a natural number $p$ let
$\overline{H}_n^{(p)} = \sum_{i=1}^{n} (-1)^{i-1}/i^p$ be the alternating generalized harmonic
numbers, and let the type II generalized alternating hyperharmonic numbers be
$H_n^{(p,1,2)} = \overline{H}_n^{(p)}$ and $H_n^{(p,r+1,2)} = \sum_{k=1}^{n} H_k^{(p,r,2)}$. Let
$\bar\zeta(p)$ be the alternating zeta value at $p$, so that $\bar\zeta(1) = \log 2$. Then for all
natural numbers $r, p \ge 1$, $H_n^{(p,r,2)} \sim n^{r-1} \bar\zeta(p) / (r-1)!$ as $n \to \infty$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 13 (`jis-2024-24.4.1-lem-13`).

Stated but not proved: `MetaMathlibExt.alternatingHyperharmonic_typeII_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-hyperharmonic-type-ii-is-equ).

## Asymptotics of type III alternating hyperharmonic numbers

For real $s$ let
$\overline{H}_n^{(s)} = \sum_{i=1}^{n} (-1)^{i-1}/i^s$ be the alternating generalized harmonic
numbers, and let the type III generalized alternating hyperharmonic numbers be
$H_n^{(s,1,3)} = \overline{H}_n^{(s)}$ and
$H_n^{(s,r+1,3)} = \sum_{k=1}^{n} (-1)^{k-1} H_k^{(s,r,3)}$. Let $y \ge 1$ and $p \ge 1$ be natural
numbers and let $\bar\zeta(p)$ be the alternating zeta value at $p$. Then, as $n \to \infty$,
$H_n^{(p,2y+1,3)} \sim n^y \bar\zeta(p) / (2^y\, y!)$ and
$H_n^{(1,2y,3)} \sim n^{y-1} \log n / (2^y (y-1)!)$. If moreover $p \ge 2$, then, with
$\zeta(p) = \sum_{i \ge 1} 1/i^p$, as $n \to \infty$,
$H_{2n}^{(p,2y,3)} \sim n^{y-1} (\zeta(p) - \bar\zeta(p)) / (2\,(y-1)!)$ and
$H_{2n-1}^{(p,2y,3)} \sim n^{y-1} (\zeta(p) + \bar\zeta(p)) / (2\,(y-1)!)$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Lemma 16 (`jis-2024-24.4.1-lem-16`).

Stated but not proved: `MetaMathlibExt.alternatingHyperharmonic_typeIII_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#alternating-hyperharmonic-type-iii-is-eq).

## Mixed hyperharmonic product sums over squarefree numbers with $k$ prime factors

Let
$q_1 \ge 2$ and $q_2, \alpha, \beta, m, k, s, n, r_1, r_2 \ge 1$ be natural numbers. Let
$p_{\ell,k}$ be the $\ell$th ($\ell \ge 1$) squarefree number with exactly $k$ prime factors.
Write $H_\ell^{(q)} = \sum_{j=1}^{\ell} j^{-q}$ and
$\bar H_\ell^{(q)} = \sum_{j=1}^{\ell} (-1)^{j-1} j^{-q}$; let $H_\ell^{(q,1)} = H_\ell^{(q)}$ and
$H_\ell^{(q,r+1)} = \sum_{j=1}^{\ell} H_j^{(q,r)}$, and define $H_\ell^{(q,r,2)}$ by the same
recursion from $H_\ell^{(q,1,2)} = \bar H_\ell^{(q)}$. Let $h_\ell^{(t)}$ be the hyperharmonic
numbers, $h_\ell^{(0)} = 1/\ell$ and $h_\ell^{(t+1)} = \sum_{j=1}^{\ell} h_j^{(t)}$. Let
$\zeta(q) = \sum_{i \ge 1} i^{-q}$ for $q \ge 2$, and let $\bar\zeta(q_2)$ be $\log 2$ if
$q_2 = 1$ and $(1 - 2^{1-q_2}) \zeta(q_2)$ otherwise. Put
$f(\ell) = p_{\ell,k}^{\alpha} (H_\ell^{(q_1,r_1)})^m (h_\ell^{(s)})^n
(H_\ell^{(q_2,r_2,2)})^\beta$,
$E = m(r_1 - 1) + n(s - 1) + \beta(r_2 - 1)$, $A = \alpha + E + 1$,
$D = ((r_1 - 1)!)^m ((s - 1)!)^n ((r_2 - 1)!)^\beta$ and $Z = \zeta(q_1)^m \bar\zeta(q_2)^\beta$.
Then, as the natural number $x$ tends to infinity,

$$\sum_{\ell=1}^{x} f(\ell) \sim
\frac{((k-1)!)^\alpha Z x^A (\log x)^{\alpha+n}}{A D (\log\log x)^{\alpha(k-1)}}$$

and

$$\sum_{1 \le \ell \le x,\ p_{\ell,k} \le x} f(\ell) \sim
\frac{Z x^A (\log\log x)^{(E+1)(k-1)}}{A D ((k-1)!)^{E+1}
(\log x)^{m(r_1-1)+n(s-2)+\beta(r_2-1)+1}}.$$

The exponent of $\log x$ in the second formula is an integer, which is negative for some
parameters with $s = 1$.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Theorem 15 (`jis-2024-24.4.1-thm-15`).

Stated but not proved: `MetaMathlibExt.sum_squarefreeKPrime_pow_mul_hyperharmonic_products_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-squarefree-kprime-pow-mul-hyperharmo).

## Prime-weighted power sums of type I alternating hyperharmonic numbers

Let
$\alpha, m, y \ge 1$ and $q \ge 2$ be integers. Let $p_\ell$ be the $\ell$-th prime ($p_1 = 2$),
let $H_n^{(s,r,1)}$ be the signed iterated partial sum of order $r$, with alternating signs, of the
generalized harmonic numbers $H_n^{(s)} = \sum_{j=1}^{n} j^{-s}$, let
$\zeta(q) = \sum_{n \ge 1} n^{-q}$, and let $\bar\zeta$ be the alternating zeta function. For a
real sequence $f$ write

$$S_x(f) = \sum_{\ell=1}^{x} p_\ell^\alpha f(\ell)^m, \qquad
T_x(f) = \sum_{\substack{1 \le \ell \le x \\ p_\ell \le x}} p_\ell^\alpha f(\ell)^m,$$

put $E = my + 1$, $F = m(y-1) + 1$, $A = \alpha + E$ and $B = \alpha + F$, and let
$f_1(\ell) = H_\ell^{(1,2y+1,1)}$, $f_2(\ell) = H_\ell^{(q,2y+1,1)}$,
$f_3(\ell) = (-1)^{\ell-1} H_\ell^{(1,2y,1)}$, $f_4(\ell) = H_{2\ell-1}^{(1,2y,1)}$,
$f_5(\ell) = -H_{2\ell}^{(1,2y,1)}$, $f_6(\ell) = H_{2\ell-1}^{(q,2y,1)}$ and
$f_7(\ell) = -H_{2\ell}^{(q,2y,1)}$. Then, as the natural number $x$ tends to infinity,

$$S_x(f_1) \sim \frac{x^A (\log x)^{\alpha+m}}{(2^y y!)^m A}, \qquad
T_x(f_1) \sim \frac{x^A}{(2^y y!)^m A (\log x)^{m(y-1)+1}},$$



$$S_x(f_2) \sim \frac{\zeta(q)^m x^A (\log x)^\alpha}{(2^y y!)^m A}, \qquad
T_x(f_2) \sim \frac{\zeta(q)^m x^A}{(2^y y!)^m A (\log x)^E},$$



$$S_x(f_3) \sim \frac{x^B (\log x)^{\alpha+m}}{(2^y (y-1)!)^m B}, \qquad
T_x(f_3) \sim \frac{x^B}{(2^y (y-1)!)^m B (\log x)^{m(y-2)+1}},$$

for $i = 4, 5$

$$S_x(f_i) \sim \frac{x^B (\log x)^{\alpha+m}}{(2 (y-1)!)^m B}, \qquad
T_x(f_i) \sim \frac{x^B}{(2 (y-1)!)^m B (\log x)^{m(y-2)+1}},$$

and

$$S_x(f_6) \sim \frac{(\zeta(q) + \bar\zeta(q))^m x^B (\log x)^\alpha}{(2 (y-1)!)^m B}, \qquad
T_x(f_6) \sim \frac{(\zeta(q) + \bar\zeta(q))^m x^B}{(2 (y-1)!)^m B (\log x)^F},$$



$$S_x(f_7) \sim \frac{(\zeta(q) - \bar\zeta(q))^m x^B (\log x)^\alpha}{(2 (y-1)!)^m B}, \qquad
T_x(f_7) \sim \frac{(\zeta(q) - \bar\zeta(q))^m x^B}{(2 (y-1)!)^m B (\log x)^F}.$$

The exponent $m(y-2)+1$ of $\log x$ may be negative; the power is then an integer power.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Theorem 11 (`jis-2024-24.4.1-thm-11`).

Stated but not proved: `MetaMathlibExt.sum_primes_pow_mul_alternatingHyperharmonic_typeI_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-primes-pow-mul-alternating-hyperharm).

## Type I alternating hyperharmonic power sums weighted by squarefree $k$-prime numbers

Let
$\alpha, m, k, y \ge 1$ and $q \ge 2$ be integers. Let $p_{\ell,k}$ be the $\ell$-th squarefree
number with exactly $k$ prime factors, let $H_n^{(s,r,1)}$ be the signed iterated partial sum of
order $r$, with alternating signs, of the generalized harmonic numbers
$H_n^{(s)} = \sum_{j=1}^{n} j^{-s}$, let $\zeta(q) = \sum_{n \ge 1} n^{-q}$, and let $\bar\zeta$ be
the alternating zeta function. For a real sequence $f$ write

$$S_x(f) = \sum_{\ell=1}^{x} p_{\ell,k}^\alpha f(\ell)^m, \qquad
T_x(f) = \sum_{\substack{1 \le \ell \le x \\ p_{\ell,k} \le x}} p_{\ell,k}^\alpha f(\ell)^m,$$

put $K = (k-1)!$, $E = my + 1$, $F = m(y-1) + 1$, $A = \alpha + E$ and $B = \alpha + F$, and let
$f_1(\ell) = H_\ell^{(1,2y+1,1)}$, $f_2(\ell) = H_\ell^{(q,2y+1,1)}$,
$f_3(\ell) = (-1)^{\ell-1} H_\ell^{(1,2y,1)}$, $f_4(\ell) = H_{2\ell-1}^{(1,2y,1)}$,
$f_5(\ell) = -H_{2\ell}^{(1,2y,1)}$, $f_6(\ell) = H_{2\ell-1}^{(q,2y,1)}$ and
$f_7(\ell) = -H_{2\ell}^{(q,2y,1)}$. Then, as the natural number $x$ tends to infinity,

$$S_x(f_1) \sim \frac{K^\alpha x^A (\log x)^{\alpha+m}}{(2^y y!)^m A (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_1) \sim
\frac{x^A (\log \log x)^{E(k-1)}}{(2^y y!)^m K^E A (\log x)^{m(y-1)+1}},$$



$$S_x(f_2) \sim
\frac{K^\alpha \zeta(q)^m x^A (\log x)^\alpha}{(2^y y!)^m A (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_2) \sim
\frac{\zeta(q)^m x^A (\log \log x)^{E(k-1)}}{(2^y y!)^m K^E A (\log x)^E},$$



$$S_x(f_3) \sim
\frac{K^\alpha x^B (\log x)^{\alpha+m}}{(2^y (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_3) \sim
\frac{x^B (\log \log x)^{F(k-1)}}{(2^y (y-1)!)^m K^F B (\log x)^{m(y-2)+1}},$$

for $i = 4, 5$

$$S_x(f_i) \sim
\frac{K^\alpha x^B (\log x)^{\alpha+m}}{(2 (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_i) \sim
\frac{x^B (\log \log x)^{F(k-1)}}{(2 (y-1)!)^m K^F B (\log x)^{m(y-2)+1}},$$

and

$$S_x(f_6) \sim \frac{K^\alpha (\zeta(q) + \bar\zeta(q))^m x^B (\log x)^\alpha}
{(2 (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_6) \sim \frac{(\zeta(q) + \bar\zeta(q))^m x^B (\log \log x)^{F(k-1)}}
{(2 (y-1)!)^m K^F B (\log x)^F},$$



$$S_x(f_7) \sim \frac{K^\alpha (\zeta(q) - \bar\zeta(q))^m x^B (\log x)^\alpha}
{(2 (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_7) \sim \frac{(\zeta(q) - \bar\zeta(q))^m x^B (\log \log x)^{F(k-1)}}
{(2 (y-1)!)^m K^F B (\log x)^F}.$$

The exponent $m(y-2)+1$ of $\log x$ may be negative; the power is then an integer power.

The paper prints the second sum of its seventh item,
$\sum p_{\ell,k}^\alpha (-H_{2\ell}^{(1,2y,1)})^m$, over $p_{\ell,k} \le x$ but gives it the
asymptotic of a sum over $\ell \le x$, and the version over $p_{\ell,k} \le x$ is its eighth item;
it is read here as $S_x(f_5)$, a sum over $\ell \le x$, as in Theorem 11.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Theorem 12 (`jis-2024-24.4.1-thm-12`).

Stated but not proved: `MetaMathlibExt.sum_squarefreeKPrime_pow_mul_alternatingHyperharmonic_typeI_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 605](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L605). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-squarefree-kprime-pow-mul-alternatin).

## Prime- and squarefree-weighted power sums of type II alternating hyperharmonic numbers

Let $\alpha, m, q, k, r \ge 1$ be integers. Let $p_\ell$ be the $\ell$-th prime ($p_1 = 2$) and
$p_{\ell,k}$ the $\ell$-th squarefree number with exactly $k$ prime factors. Let
$H_n^{(q,r,2)}$ be the signed iterated partial sum of order $r$, with constant signs, of the
alternating generalized harmonic numbers $\bar H_n^{(q)} = \sum_{j=1}^{n} (-1)^{j-1} j^{-q}$, and
let $\bar\zeta$ be the alternating zeta function ($\bar\zeta(1) = \log 2$). Put
$E = m(r-1) + 1$ and $A = \alpha + E$. Then, as the natural number $x$ tends to infinity,

$$\sum_{\ell=1}^{x} p_\ell^\alpha \bigl(H_\ell^{(q,r,2)}\bigr)^m \sim
\frac{\bar\zeta(q)^m x^A (\log x)^\alpha}{((r-1)!)^m A},$$



$$\sum_{\substack{1 \le \ell \le x \\ p_\ell \le x}} p_\ell^\alpha \bigl(H_\ell^{(q,r,2)}\bigr)^m
\sim \frac{\bar\zeta(q)^m x^A}{((r-1)!)^m A (\log x)^E},$$



$$\sum_{\ell=1}^{x} p_{\ell,k}^\alpha \bigl(H_\ell^{(q,r,2)}\bigr)^m \sim
\frac{((k-1)!)^\alpha \bar\zeta(q)^m x^A (\log x)^\alpha}
{((r-1)!)^m A (\log \log x)^{\alpha(k-1)}},$$



$$\sum_{\substack{1 \le \ell \le x \\ p_{\ell,k} \le x}} p_{\ell,k}^\alpha
\bigl(H_\ell^{(q,r,2)}\bigr)^m \sim
\frac{\bar\zeta(q)^m x^A (\log \log x)^{E(k-1)}}{((r-1)!)^m ((k-1)!)^E A (\log x)^E}.$$

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Theorem 14 (`jis-2024-24.4.1-thm-14`).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_alternatingHyperharmonic_typeII_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 706](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L706). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-pow-mul-alternating-hyperharmonic-ty).

## Prime-weighted power sums of type III alternating hyperharmonic numbers

Let
$\alpha, m, p, y \ge 1$ and $q \ge 2$ be integers. Let $p_\ell$ be the $\ell$-th prime
($p_1 = 2$), let $H_n^{(s,r,3)}$ be the signed iterated partial sum of order $r$, with alternating
signs, of the alternating generalized harmonic numbers
$\bar H_n^{(s)} = \sum_{j=1}^{n} (-1)^{j-1} j^{-s}$, let $\zeta(q) = \sum_{n \ge 1} n^{-q}$, and
let $\bar\zeta$ be the alternating zeta function ($\bar\zeta(1) = \log 2$). For a real sequence
$f$ write

$$S_x(f) = \sum_{\ell=1}^{x} p_\ell^\alpha f(\ell)^m, \qquad
T_x(f) = \sum_{\substack{1 \le \ell \le x \\ p_\ell \le x}} p_\ell^\alpha f(\ell)^m,$$

put $E = my + 1$, $F = m(y-1) + 1$, $A = \alpha + E$ and $B = \alpha + F$, and let
$f_1(\ell) = H_\ell^{(p,2y+1,3)}$, $f_2(\ell) = H_\ell^{(1,2y,3)}$,
$f_3(\ell) = H_{2\ell-1}^{(q,2y,3)}$ and $f_4(\ell) = H_{2\ell}^{(q,2y,3)}$. Then, as the natural
number $x$ tends to infinity,

$$S_x(f_1) \sim \frac{\bar\zeta(p)^m x^A (\log x)^\alpha}{(2^y y!)^m A}, \qquad
T_x(f_1) \sim \frac{\bar\zeta(p)^m x^A}{(2^y y!)^m A (\log x)^E},$$



$$S_x(f_2) \sim \frac{x^B (\log x)^{\alpha+m}}{(2^y (y-1)!)^m B}, \qquad
T_x(f_2) \sim \frac{x^B}{(2^y (y-1)!)^m B (\log x)^{m(y-2)+1}},$$



$$S_x(f_3) \sim \frac{(\zeta(q) + \bar\zeta(q))^m x^B (\log x)^\alpha}{(2 (y-1)!)^m B}, \qquad
T_x(f_3) \sim \frac{(\zeta(q) + \bar\zeta(q))^m x^B}{(2 (y-1)!)^m B (\log x)^F},$$



$$S_x(f_4) \sim \frac{(\zeta(q) - \bar\zeta(q))^m x^B (\log x)^\alpha}{(2 (y-1)!)^m B}, \qquad
T_x(f_4) \sim \frac{(\zeta(q) - \bar\zeta(q))^m x^B}{(2 (y-1)!)^m B (\log x)^F}.$$

The exponent $m(y-2)+1$ of $\log x$ may be negative; the power is then an integer power.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Theorem 17 (`jis-2024-24.4.1-thm-17`).

Stated but not proved: `MetaMathlibExt.sum_primes_pow_mul_alternatingHyperharmonic_typeIII_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 747](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L747). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-primes-pow-mul-alternating-hyperharm-2).

## Type III alternating hyperharmonic power sums weighted by squarefree $k$-prime numbers

Let $\alpha, m, k, p, y \ge 1$ and $q \ge 2$ be integers. Let $p_{\ell,k}$ be the $\ell$-th
squarefree number with exactly $k$ prime factors, let $H_n^{(s,r,3)}$ be the signed iterated
partial sum of order $r$, with alternating signs, of the alternating generalized harmonic numbers
$\bar H_n^{(s)} = \sum_{j=1}^{n} (-1)^{j-1} j^{-s}$, let $\zeta(q) = \sum_{n \ge 1} n^{-q}$, and
let $\bar\zeta$ be the alternating zeta function ($\bar\zeta(1) = \log 2$). For a real sequence
$f$ write

$$S_x(f) = \sum_{\ell=1}^{x} p_{\ell,k}^\alpha f(\ell)^m, \qquad
T_x(f) = \sum_{\substack{1 \le \ell \le x \\ p_{\ell,k} \le x}} p_{\ell,k}^\alpha f(\ell)^m,$$

put $K = (k-1)!$, $E = my + 1$, $F = m(y-1) + 1$, $A = \alpha + E$ and $B = \alpha + F$, and let
$f_1(\ell) = H_\ell^{(p,2y+1,3)}$, $f_2(\ell) = H_\ell^{(1,2y,3)}$,
$f_3(\ell) = H_{2\ell-1}^{(q,2y,3)}$ and $f_4(\ell) = H_{2\ell}^{(q,2y,3)}$. Then, as the natural
number $x$ tends to infinity,

$$S_x(f_1) \sim
\frac{K^\alpha \bar\zeta(p)^m x^A (\log x)^\alpha}{(2^y y!)^m A (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_1) \sim
\frac{\bar\zeta(p)^m x^A (\log \log x)^{E(k-1)}}{(2^y y!)^m K^E A (\log x)^E},$$



$$S_x(f_2) \sim
\frac{K^\alpha x^B (\log x)^{\alpha+m}}{(2^y (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_2) \sim
\frac{x^B (\log \log x)^{F(k-1)}}{(2^y (y-1)!)^m K^F B (\log x)^{m(y-2)+1}},$$



$$S_x(f_3) \sim \frac{K^\alpha (\zeta(q) + \bar\zeta(q))^m x^B (\log x)^\alpha}
{(2 (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_3) \sim \frac{(\zeta(q) + \bar\zeta(q))^m x^B (\log \log x)^{F(k-1)}}
{(2 (y-1)!)^m K^F B (\log x)^F},$$



$$S_x(f_4) \sim \frac{K^\alpha (\zeta(q) - \bar\zeta(q))^m x^B (\log x)^\alpha}
{(2 (y-1)!)^m B (\log \log x)^{\alpha(k-1)}},
\qquad T_x(f_4) \sim \frac{(\zeta(q) - \bar\zeta(q))^m x^B (\log \log x)^{F(k-1)}}
{(2 (y-1)!)^m K^F B (\log x)^F}.$$

The exponent $m(y-2)+1$ of $\log x$ may be negative; the power is then an integer power.

The paper prints the first two items with the type I numbers $H_\ell^{(p,2y+1,1)}$, but their
asymptotics carry $\bar\zeta(p)$, the section treats type III, and the proof sums
$H_\ell^{(p,2y+1,3)}$; they are read here with type III.

## Sources

- Rusen Li, *Sums over Primes II*, Journal of Integer Sequences 27 (2024), Article 24.4.1, Theorem 18 (`jis-2024-24.4.1-thm-18`).

Stated but not proved: `MetaMathlibExt.sum_squarefreeKPrime_pow_mul_alternatingHyperharmonic_typeIII_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean, line 804](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HyperharmonicPrimeSumsWanted.lean#L804). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html#sum-squarefree-kprime-pow-mul-alternatin-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperharmonic numbers and sums over primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/harmonic-numbers/hyperharmonic-numbers-and-sums-over-primes)
