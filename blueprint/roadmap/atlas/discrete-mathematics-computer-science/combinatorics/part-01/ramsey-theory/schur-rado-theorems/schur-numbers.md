---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SchurNumbersWanted.schurForces, MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber, MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_two, MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_three, MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_four, MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_five, MathlibExt.Combinatorics.SchurNumbersWanted.le_schurNumber_six, MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_six_le
statement: formalized
---

# Schur numbers

8 results, 2 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html).

## Schur forcing property

For natural numbers $k$ and $N$, we say that $N$ forces a
monochromatic Schur triple in $k$ colours when every colouring $c$ of the natural numbers with $k$
colours has $x, y, z \in \{1, \dots, N\}$ with $x + y = z$ and $c(x) = c(y) = c(z)$.

Solutions with $x = y$ count, so this property gives the Schur numbers, not the weak Schur
numbers.

Formalized by `MathlibExt.Combinatorics.SchurNumbersWanted.schurForces`, a definition declared in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-forces).

## Schur number

For $k \ge 1$, the Schur number $S(k)$ is $N_0 - 1$, where $N_0$ is the
least natural number $N$ that forces a monochromatic Schur triple in $k$ colours: every colouring
$c$ of the natural numbers with $k$ colours has $x, y, z \in \{1, \dots, N\}$ with $x + y = z$ and
$c(x) = c(y) = c(z)$. For $k = 0$, $S(0) = 0$.

Such an $N_0$ exists by Schur's theorem, and $S(k)$ is the largest $N$ such that
$\{1, \dots, N\}$ splits into $k$ sum-free parts, some possibly empty (OEIS A045652); the
numbers $N_0 = S(k) + 1$ form OEIS A030126.

Formalized by `MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber`, a definition declared in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-number).

## The second Schur number

The Schur number $S(2)$ equals $4$.

## Sources

- exhaustive check; OEIS A045652; listed in leansolving/SqueezeBench `SqueezeBench/Problems/Schur/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-number-two).

## The third Schur number

The Schur number $S(3)$ equals $13$.

## Sources

- exhaustive check; OEIS A045652; listed in SqueezeBench `SqueezeBench/Problems/Schur/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-number-three).

## The fourth Schur number

The Schur number $S(4)$ equals $44$.

## Sources

- S. W. Golomb and L. D. Baumert, *Backtrack programming*, J. ACM 12 (1965), 516–524; OEIS A045652; listed in SqueezeBench `SqueezeBench/Problems/Schur/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_four` is written with `theorem_wanted` in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-number-four).

## The fifth Schur number

The Schur number $S(5)$ equals $160$.

## Sources

- M. J. H. Heule, *Schur Number Five*, Proc. AAAI 2018, 6598–6606 (arXiv:1711.08076), a DRAT-verified SAT proof; OEIS A045652; listed in SqueezeBench `SqueezeBench/Problems/Schur/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-number-five).

## Lower bound for the sixth Schur number

The Schur number $S(6)$ is at least $536$.

## Sources

- H. Fredricksen and M. M. Sweet, *Symmetric sum-free partitions and lower bounds for Schur numbers*, Electron. J. Combin. 7 (2000), R32; listed in SqueezeBench `SqueezeBench/Problems/Schur/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SchurNumbersWanted.le_schurNumber_six` is written with `theorem_wanted` in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#le-schur-number-six).

## Upper bound for the sixth Schur number

The Schur number $S(6)$ is at most $1836$.

## Sources

- the multicolour Ramsey bound `R₆(3) ≤ 1838` (S. P. Radziszowski, *Small Ramsey Numbers*, Electron. J. Combin. Dynamic Survey DS1) together with `S(k) ≤ R_k(3) - 2`; the range `536 ≤ S(6) ≤ 1836` is stated in S. Eliahou and D. F. Revuelta, *The Schur degree of additive sets*, arXiv:2006.01502; listed in SqueezeBench `SqueezeBench/Problems/Schur/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SchurNumbersWanted.schurNumber_six_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/SchurNumbersWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/SchurNumbersWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html#schur-number-six-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Schur numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/schur-numbers)
