---
declaration: section
origin: cited
lean: MetaMathlibExt.nonzeroDigitProd, MetaMathlibExt.IsProdigious, MetaMathlibExt.exists_positive_crt_solution_nonzero_digit_product_one
statement: formalized
proof: formalized
---

# Prodigious numbers

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/prodigious-numbers/index.html).

## Product of the nonzero digits

For natural numbers $b$ and $n$, this is the product of the
nonzero digits of $n$ in base $b$; it equals $1$ when $n = 0$. In the degenerate bases, the digits
of $n > 0$ are the single digit $n$ when $b = 0$, and $n$ copies of $1$ when $b = 1$.

Formalized by `MetaMathlibExt.nonzeroDigitProd`, a definition declared in [MathlibExt/NumberTheory/ProdigiousNumber.lean, line 18](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ProdigiousNumber.lean#L18). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/prodigious-numbers/index.html#nonzero-digit-prod).

## Prodigious numbers

For natural numbers $b$ and $n$, the number $n$ is $b$-prodigious when
$b \ge 2$, $n > 0$, and $n$ is divisible by the product of the nonzero digits of $n$ in base $b$.

Formalized by `MetaMathlibExt.IsProdigious`, a definition declared in [MathlibExt/NumberTheory/ProdigiousNumber.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ProdigiousNumber.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/prodigious-numbers/index.html#is-prodigious).

## Chinese remainder solutions with nonzero-digit product one

Let $b \ge 3$ and $w \ge 1$
be integers, and for $v = 1, \dots, w$ let $m_v$ be a positive integer and $r_v$ an integer.
Suppose the system of congruences $x \equiv r_v \pmod{m_v}$, $v = 1, \dots, w$, has an integer
solution, and $r_v = 0$ whenever $\gcd(m_v, b) \ne 1$. Then the system has a positive integer
solution $c$ with $p_b(c) = 1$, where $p_b(c)$ is the product of the nonzero base-$b$ digits
of $c$.

## Sources

- Michael Gohn, Joshua Harrington, Sophia Lebiere, Hani Samamah, Kyla Shappell, and Tony W. H. Wong, "Arithmetic Progressions of b-Prodigious Numbers," Journal of Integer Sequences 25 (2022), Article 22.8.7, Lemma `lem:crt`, lines 178-180, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Wong/wong42.tex>.

Formalized by `MetaMathlibExt.exists_positive_crt_solution_nonzero_digit_product_one`, a theorem declared in [MathlibExt/NumberTheory/Digits/ProdigiousCrtSolution.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Digits/ProdigiousCrtSolution.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/prodigious-numbers/index.html#exists-positive-crt-solution-nonzero-dig).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prodigious numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/prodigious-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/prodigious-numbers)
