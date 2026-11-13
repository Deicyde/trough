---
declaration: section
origin: cited
lean: Cslib.CodingTheory.ReedSolomon.encode, Cslib.CodingTheory.ReedSolomon.encodeLin, Cslib.CodingTheory.ReedSolomon.code, Cslib.CodingTheory.ReedSolomon.card_eval_eq_zero_le, Cslib.CodingTheory.ReedSolomon.le_hammingNorm_encode, Cslib.CodingTheory.ReedSolomon.injOn_encode, Cslib.CodingTheory.ReedSolomon.finrank_code, Cslib.CodingTheory.ReedSolomon.le_minDist_code
statement: formalized
proof: formalized
---

# Reed–Solomon codes

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html).

## The code

## Reed-Solomon encoder

For a field $F$ and points $\alpha_0, \dots, \alpha_{n-1} \in F$,
the encoding of a polynomial $p \in F[X]$ is the word $(p(\alpha_0), \dots, p(\alpha_{n-1}))$
in $F^n$.

Formalized by `Cslib.CodingTheory.ReedSolomon.encode`, a definition declared in [CSLibExt/Coding/ReedSolomon.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#encode).

## Reed-Solomon encoder as a linear map

For a field $F$ and points
$\alpha_0, \dots, \alpha_{n-1} \in F$, the $F$-linear map $F[X] \to F^n$ sending a polynomial
$p$ to $(p(\alpha_0), \dots, p(\alpha_{n-1}))$.

Formalized by `Cslib.CodingTheory.ReedSolomon.encodeLin`, a definition declared in [CSLibExt/Coding/ReedSolomon.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#encode-lin).

## Reed-Solomon code

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in F$ and
let $k$ be a natural number. The Reed-Solomon code $\mathrm{RS}(\alpha, k)$ is the linear code
of length $n$ over $F$ consisting of the words $(p(\alpha_0), \dots, p(\alpha_{n-1}))$ for the
polynomials $p \in F[X]$ of degree less than $k$.

Formalized by `Cslib.CodingTheory.ReedSolomon.code`, a definition declared in [CSLibExt/Coding/ReedSolomon.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#code).

## Root count at distinct points

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1}$
be pairwise distinct elements of $F$, and let $p \in F[X]$ be a nonzero polynomial. Then the
number of indices $i < n$ with $p(\alpha_i) = 0$ is at most the degree of $p$.

Formalized by `Cslib.CodingTheory.ReedSolomon.card_eval_eq_zero_le`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#card-eval-eq-zero-le).

## Nonzero Reed-Solomon codewords are heavy

Let $F$ be a field, let $\alpha_0, \dots,
\alpha_{n-1} \in F$ be pairwise distinct and let $k \le n$. For every nonzero polynomial
$p \in F[X]$ of degree less than $k$, the encoding $(p(\alpha_0), \dots, p(\alpha_{n-1}))$ has at
least $n - k + 1$ nonzero coordinates.

Formalized by `Cslib.CodingTheory.ReedSolomon.le_hammingNorm_encode`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#le-hamming-norm-encode).

## The Reed-Solomon encoder is injective on low-degree polynomials

Let $F$ be a field, let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct and let $k \le n$. If two polynomials
$p, q \in F[X]$ of degree less than $k$ satisfy $p(\alpha_i) = q(\alpha_i)$ for every $i < n$,
then $p = q$.

Formalized by `Cslib.CodingTheory.ReedSolomon.injOn_encode`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#inj-on-encode).

## Dimension of a Reed-Solomon code

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in
F$ be pairwise distinct and let $k \le n$. The Reed-Solomon code of the points $\alpha$ with
parameter $k$ has dimension $k$ over $F$.

Formalized by `Cslib.CodingTheory.ReedSolomon.finrank_code`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#finrank-code).

## Lower bound on the minimum distance of a Reed-Solomon code

Let $F$ be a field, let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct and let $k \in \mathbb{N}$. The
Reed-Solomon code of the points $\alpha$ with parameter $k$ has minimum distance at least
$\max(n - k, 0) + 1$.

Formalized by `Cslib.CodingTheory.ReedSolomon.le_minDist_code`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#le-min-dist-code).

## A low-weight Reed-Solomon codeword

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1}
\in F$ (not necessarily distinct) and let $1 \le k \le n$. There is a nonzero polynomial
$p \in F[X]$ of degree less than $k$ whose encoding $(p(\alpha_0), \dots, p(\alpha_{n-1}))$ has at
most $n - k + 1$ nonzero coordinates.

One such polynomial is $\prod_{j < k - 1} (X - \alpha_j)$.

Formalized by `Cslib.CodingTheory.ReedSolomon.exists_codeword_hammingNorm_le`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#exists-codeword-hamming-norm-le).

## Reed-Solomon codes are MDS

Let $F$ be a field (not necessarily finite), let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct and let $1 \le k \le n$. The
Reed-Solomon code of the points $\alpha$ with parameter $k$ has minimum distance exactly
$n - k + 1$.

The lower bound counts roots; the upper bound is attained by the encoding of
$\prod_{j < k - 1} (X - \alpha_j)$.

Formalized by `Cslib.CodingTheory.ReedSolomon.minDist_code`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#min-dist-code).

## Reed-Solomon codes meet the Singleton bound

Let $F$ be a finite field, let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct and let $1 \le k \le n$. The
Reed-Solomon code $C$ of the points $\alpha$ with parameter $k$ has minimum distance
$d = n - \dim C + 1$, so the Singleton bound $d \le n - \dim C + 1$ for linear codes holds with
equality.

The upper bound is the Singleton bound for linear codes; the lower bound counts roots.

Formalized by `Cslib.CodingTheory.ReedSolomon.minDist_code_eq_singleton`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#min-dist-code-eq-singleton).

## Berlekamp-Welch key equations

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in
F$, let $k, e \in \mathbb{N}$ and let $y \in F^n$ be a received word. A pair of polynomials
$(Q, E)$ over $F$ solves the key equations for $y$ when $E$ is monic of degree $e$, $Q$ has degree
less than $e + k$, and $Q(\alpha_i) = y_i E(\alpha_i)$ for every $i < n$.

Formalized by `Cslib.CodingTheory.ReedSolomon.IsKeySolution`, a definition declared in [CSLibExt/Coding/ReedSolomon.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#is-key-solution).

## The key equations are solvable

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in
F$ and let $p \in F[X]$ have degree less than $k$. If a received word $y \in F^n$ differs from the
encoding $(p(\alpha_0), \dots, p(\alpha_{n-1}))$ in at most $e$ coordinates, then the
Berlekamp-Welch key equations for $y$ with parameters $k$ and $e$ have a solution $(Q, E)$.

A solution is the error locator polynomial, padded to degree $e$, together with $Q = pE$.

Formalized by `Cslib.CodingTheory.ReedSolomon.exists_isKeySolution`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#exists-is-key-solution).

## Every solution of the key equations reveals the message

Let $F$ be a field, let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct and let $k, e$ be natural numbers
with $2e + k \le n$. Let $p \in F[X]$ have degree less than $k$, and let $y \in F^n$ be
within Hamming distance $e$ of $(p(\alpha_0), \dots, p(\alpha_{n-1}))$. If $(Q, E)$ solves
the key equations for $y$ ($E$ is monic of degree $e$, $\deg Q < e + k$, and
$Q(\alpha_i) = y_i E(\alpha_i)$ for all $i < n$), then $Q = pE$.

The difference $Q - pE$ has degree less than $e + k$ and vanishes at the at least
$n - e \ge e + k$ error-free points.

Formalized by `Cslib.CodingTheory.ReedSolomon.eq_mul_of_isKeySolution`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#eq-mul-of-is-key-solution).

## The quotient of a key-equation solution is the message

Let $F$ be a field, let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct and let $k, e$ be natural numbers
with $2e + k \le n$. Let $p \in F[X]$ have degree less than $k$, and let $y \in F^n$ be
within Hamming distance $e$ of $(p(\alpha_0), \dots, p(\alpha_{n-1}))$. If $(Q, E)$ solves
the key equations for $y$ ($E$ is monic of degree $e$, $\deg Q < e + k$, and
$Q(\alpha_i) = y_i E(\alpha_i)$ for all $i < n$), then the quotient of $Q$ by $E$ is $p$.

Formalized by `Cslib.CodingTheory.ReedSolomon.divByMonic_eq_of_isKeySolution`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#div-by-monic-eq-of-is-key-solution).

## Solver for the key equations

For a field $F$, points $\alpha_0, \dots, \alpha_{n-1} \in F$
and parameters $k, e \in \mathbb{N}$, a solver for the Berlekamp-Welch key equations is a
procedure that takes a received word $y \in F^n$ and either returns a pair of polynomials
$(Q, E)$ over $F$ or reports failure, such that every returned pair solves the key equations for
$y$, and a pair is returned whenever the key equations for $y$ have a solution.

(The key equations are a linear system in the coefficients of $Q$ and of $E$; Gaussian
elimination is a solver.)

Formalized by `Cslib.CodingTheory.ReedSolomon.KeySolver`, a structure declared in [CSLibExt/Coding/ReedSolomon.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#key-solver).

## A key-equation solver by choice

For points $\alpha_0, \dots, \alpha_{n-1}$ in a field
$F$ and natural numbers $k$ and $e$, this is the solver for the key equations that, on a received
word $y \in F^n$, returns a pair $(Q, E)$ of polynomials solving the key equations for $y$ (that
is, $E$ is monic of degree $e$, $\deg Q < e + k$ and $Q(\alpha_i) = y_i E(\alpha_i)$ for all $i$),
picked by the axiom of choice, whenever such a pair exists, and reports failure otherwise.

Formalized by `Cslib.CodingTheory.ReedSolomon.KeySolver.ofChoice`, a definition declared in [CSLibExt/Coding/ReedSolomon.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#of-choice).

## Berlekamp-Welch decoder

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in F$,
let $k, e$ be natural numbers and let $S$ be a solver for the key equations with error budget
$e$. On a received word $y \in F^n$ the decoder runs $S$ on $y$ and reports failure if $S$
returns nothing. If $S$ returns a pair $(Q, E)$ (the solver guarantees that $E$ is monic),
let $q$ be the quotient of $Q$ by $E$; the decoder returns $q$ if $q$ has degree less than $k$
and the Hamming distance between $y$ and $(q(\alpha_0), \dots, q(\alpha_{n-1}))$ is at most
$e$, and reports failure otherwise.

Its only nontrivial step is the solver.

Formalized by `Cslib.CodingTheory.ReedSolomon.decode`, a definition declared in [CSLibExt/Coding/ReedSolomon.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#decode).

## What the decoder returns

Let $F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in F$
be pairwise distinct, let $k, e$ be natural numbers with $2e + k \le n$ (the unique-decoding
regime), and let $S$ be a solver for the key equations with error budget $e$. For every
polynomial $p \in F[X]$ and every received word $y \in F^n$, the Berlekamp-Welch decoder with
solver $S$ returns $p$ on $y$ if and only if $p$ has degree less than $k$ and the Hamming
distance between $y$ and $(p(\alpha_0), \dots, p(\alpha_{n-1}))$ is at most $e$.

Formalized by `Cslib.CodingTheory.ReedSolomon.decode_eq_some_iff`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#decode-eq-some-iff).

## The decoder fails exactly when no codeword is close

Let $F$ be a field, let
$\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct, let $k, e$ be natural numbers
with $2e + k \le n$, and let $S$ be a solver for the key equations with error budget $e$.
For every received word $y \in F^n$, the Berlekamp-Welch decoder with solver $S$ reports
failure on $y$ if and only if, for every polynomial $p \in F[X]$ of degree less than $k$, the
Hamming distance between $y$ and $(p(\alpha_0), \dots, p(\alpha_{n-1}))$ is greater than $e$.

Formalized by `Cslib.CodingTheory.ReedSolomon.decode_eq_none_iff`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#decode-eq-none-iff).

## Berlekamp-Welch corrects every error of weight at most $\lfloor (n-k)/2 \rfloor$

Let
$F$ be a field, let $\alpha_0, \dots, \alpha_{n-1} \in F$ be pairwise distinct, let $k \le n$,
put $t = \lfloor (n-k)/2 \rfloor$, and let $S$ be a solver for the key equations with error
budget $t$. For every polynomial $p \in F[X]$ of degree less than $k$ and every error word
$\varepsilon \in F^n$ with at most $t$ nonzero entries, the Berlekamp-Welch decoder with
solver $S$, run on the received word
$(p(\alpha_0) + \varepsilon_0, \dots, p(\alpha_{n-1}) + \varepsilon_{n-1})$, returns $p$.

Formalized by `Cslib.CodingTheory.ReedSolomon.decode_encode_add`, a theorem declared in [CSLibExt/Coding/ReedSolomon.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/ReedSolomon.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html#decode-encode-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reed–Solomon codes](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/error-correcting-codes/reed-solomon-codes)
