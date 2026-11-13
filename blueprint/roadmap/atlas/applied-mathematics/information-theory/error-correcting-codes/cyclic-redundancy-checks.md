---
declaration: section
origin: cited
lean: Cslib.CodingTheory.CRC.encode, Cslib.CodingTheory.CRC.encode_eq_add, Cslib.CodingTheory.CRC.dvd_encode, Cslib.CodingTheory.CRC.coeff_encode_add, Cslib.CodingTheory.CRC.dvd_encode_add_iff, Cslib.CodingTheory.CRC.not_dvd_C_mul_X_pow, Cslib.CodingTheory.CRC.IsBurstLE, Cslib.CodingTheory.CRC.isBurstLE_of_support
statement: formalized
proof: formalized
---

# Cyclic redundancy checks

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html).

## CRC encoder

Let $F$ be a field, let $g$ be a polynomial over $F$ (the generator), and let
$r$ be the degree of $g$ (with $r = 0$ when $g = 0$). The CRC encoding of a polynomial $m$ over
$F$ (the message) is $m X^r - (m X^r \bmod g)$: the message shifted up by $r$ positions, minus the
remainder of the shifted message modulo $g$.

Formalized by `Cslib.CodingTheory.CRC.encode`, a definition declared in [CSLibExt/Coding/CRC.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#encode).

## CRC encoding in characteristic 2

Let $F$ be a field of characteristic 2 (for example
$\mathbb{F}_2$), let $g$ and $m$ be polynomials over $F$, and let $r$ be the degree of $g$ (with
$r = 0$ when $g = 0$). Then the CRC encoding of $m$ with generator $g$ equals
$m X^r + (m X^r \bmod g)$: the encoder appends the remainder to the shifted message.

Formalized by `Cslib.CodingTheory.CRC.encode_eq_add`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#encode-eq-add).

## CRC codewords are multiples of the generator

Let $F$ be a field. For all polynomials $g$
and $m$ over $F$, the polynomial $g$ divides the CRC encoding of $m$ with generator $g$.

Formalized by `Cslib.CodingTheory.CRC.dvd_encode`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#dvd-encode).

## CRC encoding is systematic

Let $F$ be a field and $g \ne 0$ a polynomial over $F$ of
degree $r$. For every message polynomial $m$ over $F$ and every natural number $i$, the
coefficient of $X^{i+r}$ in the CRC encoding of $m$ with generator $g$ equals the coefficient of
$X^i$ in $m$.

Formalized by `Cslib.CodingTheory.CRC.coeff_encode_add`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#coeff-encode-add).

## CRC detection criterion

Let $F$ be a field, let $g$, $m$ and $e$ be polynomials over
$F$, and let $c$ be the CRC encoding of $m$ with generator $g$. Then $g$ divides $c + e$ if and
only if $g$ divides $e$: a codeword plus an error pattern passes the check exactly when $g$
divides the error.

Formalized by `Cslib.CodingTheory.CRC.dvd_encode_add_iff`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#dvd-encode-add-iff).

## Single-symbol errors are detected

Let $F$ be a field and $g$ a polynomial over $F$ with
at least two nonzero coefficients. Then $g$ does not divide $a X^i$ for any nonzero $a \in F$ and
any natural number $i$.

The divisors of $X^i$ are the monomials $c X^j$ with $c \in F$ nonzero and $j \le i$, each of
which has only one nonzero coefficient.

Formalized by `Cslib.CodingTheory.CRC.not_dvd_C_mul_X_pow`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#not-dvd-c-mul-x-pow).

## Burst errors

Let $F$ be a field and $L$ a natural number. A polynomial $e$ over $F$ is a
burst of length at most $L$ when $e = X^i b$ for some natural number $i$ and some polynomial $b$
over $F$ with $b(0) \ne 0$ and $\deg b < L$. Then the nonzero coefficients of $e$ lie in
positions $i, \dots, i + L - 1$, the first one nonzero.

Formalized by `Cslib.CodingTheory.CRC.IsBurstLE`, a definition declared in [CSLibExt/Coding/CRC.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#is-burst-le).

## Errors confined to a window are bursts

Let $F$ be a field, let $e \ne 0$ be a polynomial
over $F$, and let $i$ and $L$ be natural numbers. If every $j$ for which the coefficient of $X^j$
in $e$ is nonzero satisfies $i \le j < i + L$, then $e$ is a burst of length at most $L$.

Formalized by `Cslib.CodingTheory.CRC.isBurstLE_of_support`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#is-burst-le-of-support).

## Short bursts are detected

Let $F$ be a field, let $g$ be a polynomial over $F$ that is
not divisible by $X$, and let $L$ be a natural number with $L \le \deg g$. If a polynomial $e$
over $F$ is a burst of length at most $L$, then $g$ does not divide $e$.

Write $e = X^i b$ with $b(0) \ne 0$ and $\deg b < L$. Since $X \nmid g$, $g$ is coprime to
$X^i$, so $g \mid X^i b$ would force $g \mid b$, impossible for a nonzero $b$ of smaller degree.

Formalized by `Cslib.CodingTheory.CRC.not_dvd_of_isBurstLE`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#not-dvd-of-is-burst-le).

## CRC error-detection guarantee

Let $F$ be a field, let $g$ be a polynomial over $F$ with
at least two nonzero coefficients that is not divisible by $X$, let $m$ be a polynomial over $F$,
and let $c$ be the CRC encoding of $m$ with generator $g$. Then $g$ does not divide $c + aX^i$ for
any nonzero $a \in F$ and any natural number $i$, and $g$ does not divide $c + e$ for any
polynomial $e$ over $F$ that is a burst of length at most $\deg g$. That is, the check detects
every single-symbol error and every burst of length at most $\deg g$ in every codeword.

Given $X \nmid g$, having at least two terms is the same as $\deg g \ge 1$, and a single-symbol
error is a burst of length 1.

Formalized by `Cslib.CodingTheory.CRC.detects`, a theorem declared in [CSLibExt/Coding/CRC.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Coding/CRC.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html#detects).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cyclic redundancy checks](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/error-correcting-codes/cyclic-redundancy-checks)
