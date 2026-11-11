---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.PartialHadamard.signVal, MathlibExt.Combinatorics.PartialHadamard.IsPartialHadamard, MathlibExt.Combinatorics.PartialHadamard.partialHadamardCount, MathlibExt.Combinatorics.PartialHadamard.partialHadamardCount_zero_width, MathlibExt.Combinatorics.PartialHadamard.leadingTerm, MathlibExt.Combinatorics.PartialHadamard.IsLeadingAdmissible, MathlibExt.Combinatorics.PartialHadamard.leadingTermExponent, MathlibExt.Combinatorics.PartialHadamardWanted.davisCubicAdmissible_wanted
statement: formalized
---

# Partial Hadamard matrices

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html).

## Sign of a bit

The sign of a bit $b \in \{0, 1\}$ is the integer $\sigma(b)$ given by
$\sigma(0) = -1$ and $\sigma(1) = 1$.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.signVal`, a definition declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#sign-val).

## Partial Hadamard matrices

Read a bit $b \in \{0, 1\}$ as the sign $\sigma(b)$, where
$\sigma(0) = -1$ and $\sigma(1) = 1$. An $n \times t$ matrix $M$ with entries in $\{0, 1\}$ is a
partial Hadamard matrix when its rows are pairwise orthogonal as sign vectors: for all distinct
rows $i \ne i'$, $\sum_{j < t} \sigma(M_{ij}) \sigma(M_{i'j}) = 0$.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.IsPartialHadamard`, a definition declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#is-partial-hadamard).

## Number of partial Hadamard matrices

For natural numbers $n$ and $t$, $N_{n,t}$ is the
number of $n \times t$ partial Hadamard matrices, that is, of $n \times t$ matrices with entries in
$\{0, 1\}$ whose rows are pairwise orthogonal when each entry $0$ is read as the sign $-1$ and
each entry $1$ as the sign $1$.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.partialHadamardCount`, a definition declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#partial-hadamard-count).

## Width-zero partial Hadamard count

For every natural number $n$, the number $N_{n,0}$ of
$n \times 0$ partial Hadamard matrices is $1$: the orthogonality conditions are empty sums, so the
empty matrix is the only one.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.partialHadamardCount_zero_width`, a theorem declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#partial-hadamard-count-zero-width).

## De Launey–Levin leading term

For natural numbers $n$ and $t$, the de Launey–Levin leading
term is the real number $A_{n,4t} = 2^{4nt + (n-1)^2} (8\pi t)^{-n(n-1)/4}$, where the power of
$8\pi t$ is the real power function and $n - 1$ in the exponent of $2$ is truncated subtraction of
natural numbers, so that $(n-1)^2 = 0$ when $n = 0$.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.leadingTerm`, a definition declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#leading-term).

## Admissible exponents for the partial Hadamard leading term

For natural numbers $n$ and
$m$, let $N_{n,m}$ be the number of $n \times m$ partial Hadamard matrices, and for natural
numbers $n$ and $t$ let $A_{n,4t} = 2^{4nt + (n-1)^2} (8\pi t)^{-n(n-1)/4}$ be the de
Launey–Levin leading term. A real number $\alpha$ is admissible for the leading term when, for
all sequences $(n_k)$ and $(t_k)$ of natural numbers with $n_k \ge 2$ for every $k$ and
$t_k / n_k^{\alpha} \to \infty$ as $k \to \infty$, the ratio $N_{n_k, 4t_k} / A_{n_k, 4t_k}$
tends to $1$.

The catalogue constant $C_{23c}$ also allows corrected asymptotic formulas below the cubic scale;
this predicate is its precise leading-term specialization, whose exact threshold the source
records as $3$.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.IsLeadingAdmissible`, a definition declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#is-leading-admissible).

## Leading-term counting exponent for partial Hadamard matrices

For natural numbers $n$
and $m$, let $N_{n,m}$ be the number of $n \times m$ partial Hadamard matrices, and for natural
numbers $n$ and $t$ let $A_{n,4t} = 2^{4nt + (n-1)^2} (8\pi t)^{-n(n-1)/4}$ be the de
Launey–Levin leading term. Call a real number $\alpha$ admissible when
$N_{n_k, 4t_k} / A_{n_k, 4t_k} \to 1$ along all sequences $(n_k)$ and $(t_k)$ of natural numbers
with $n_k \ge 2$ for every $k$ and $t_k / n_k^{\alpha} \to \infty$. The leading-term counting
exponent is the infimum of the admissible $\alpha \ge 1$, and is $0$ if there is no such $\alpha$.

This exponent is not asserted to equal the catalogue constant $C_{23c}$, which also permits
corrected asymptotic formulas.

Formalized by `MathlibExt.Combinatorics.PartialHadamard.leadingTermExponent`, a definition declared in [MathlibExt/Combinatorics/PartialHadamard.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/PartialHadamard.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#leading-term-exponent).

## Partial Hadamard counts follow the leading term above the cubic scale

The exponent $3$ is
admissible for the partial Hadamard leading term. That is, let $N_{n,m}$ be the number of
$n \times m$ partial Hadamard matrices and let
$A_{n,4t} = 2^{4nt + (n-1)^2} (8\pi t)^{-n(n-1)/4}$ be the de Launey–Levin leading term. Then for
all sequences $(n_k)$ and $(t_k)$ of natural numbers with $n_k \ge 2$ for every $k$ and
$t_k / n_k^3 \to \infty$ as $k \to \infty$, the ratio $N_{n_k, 4t_k} / A_{n_k, 4t_k}$ tends to $1$.

## Sources

- Davis, *Counting partial Hadamard matrices in the cubic regime*, arXiv:2603.30013 (2026): the leading term is asymptotic in the regime `t / n³ → ∞`.

Stated but not proved: `MathlibExt.Combinatorics.PartialHadamardWanted.davisCubicAdmissible_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/PartialHadamardWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PartialHadamardWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#davis-cubic-admissible-wanted).

## No exponent below 3 is admissible for the partial Hadamard leading term

Let $N_{n,m}$ be
the number of $n \times m$ partial Hadamard matrices and let
$A_{n,4t} = 2^{4nt + (n-1)^2} (8\pi t)^{-n(n-1)/4}$ be the de Launey–Levin leading term. Then for
every real number $\alpha < 3$ there are sequences $(n_k)$ and $(t_k)$ of natural numbers with
$n_k \ge 2$ for every $k$ and $t_k / n_k^{\alpha} \to \infty$ as $k \to \infty$ along which the
ratio $N_{n_k, 4t_k} / A_{n_k, 4t_k}$ does not tend to $1$.

## Sources

- Davis (2026), same paper: a nonvanishing correction at `t = Θ n³` for large fixed `Θ` blocks every smaller exponent for the leading term alone.

Stated but not proved: `MathlibExt.Combinatorics.PartialHadamardWanted.davisCubicSharp_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/PartialHadamardWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/PartialHadamardWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html#davis-cubic-sharp-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial Hadamard matrices](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/designs-latin-squares/partial-hadamard-matrices)
