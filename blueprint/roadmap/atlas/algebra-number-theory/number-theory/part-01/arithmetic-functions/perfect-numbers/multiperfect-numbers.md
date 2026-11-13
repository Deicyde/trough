---
declaration: section
origin: cited
lean: Nat.IsKPerfect, Nat.IsKPerfect.pos_k, Nat.isKPerfect_two_iff, MetaMathlibExt.pillai_equations_two_pow_three_pow, MetaMathlibExt.steuerwald_three_perfect_exponents
statement: formalized
proof: formalized
---

# Multiperfect numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html).

## $k$-perfect numbers

For natural numbers $k$ and $n$, the number $n$ is $k$-perfect when
$n > 0$ and $\sigma(n) = kn$, where $\sigma(n)$ is the sum of the positive divisors of $n$.

Formalized by `Nat.IsKPerfect`, a definition declared in [MathlibExt/NumberTheory/KPerfect.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KPerfect.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html#is-kperfect).

## The parameter of a $k$-perfect number is positive

For natural numbers $k$ and $n$, if $n$
is $k$-perfect, then $k > 0$.

Formalized by `Nat.IsKPerfect.pos_k`, a theorem declared in [MathlibExt/NumberTheory/KPerfect.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KPerfect.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html#pos-k).

## Perfect numbers are the $2$-perfect numbers

A natural number $n$ is $2$-perfect if and
only if it is perfect, that is, $n > 0$ and the sum of the proper divisors of $n$ equals $n$.

Formalized by `Nat.isKPerfect_two_iff`, a theorem declared in [MathlibExt/NumberTheory/KPerfect.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KPerfect.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html#is-kperfect-two-iff).

## Two Pillai equations in powers of two and three

For natural numbers $a$ and $b$, the
integer equation $2^a - 3^b = -1$ holds if and only if $(a, b) = (1, 1)$ or $(a, b) = (3, 2)$.
For natural numbers $a$, $b$ and $c$, the integer equation $2^a - 3^b = 2^c - 1$ holds if and
only if $(a, b, c) = (2, 1, 1)$, or $(a, b, c) = (4, 2, 3)$, or $b = 0$ and $c = a$.

## Sources

- Paulo J. Almeida and Gabriel Cardoso, *An Extension of the Euclid–Euler Theorem to Certain α-Perfect Numbers*, Journal of Integer Sequences 25 (2022), Article 22.8.4, Lemma `pillai`, lines 176–184, <https://cs.uwaterloo.ca/journals/JIS/VOL25/Almeida/almeida9.tex>.

Formalized by `MetaMathlibExt.pillai_equations_two_pow_three_pow`, a theorem declared in [MathlibExt/NumberTheory/SteuerwaldThreePerfect.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SteuerwaldThreePerfect.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html#pillai-equations-two-pow-three-pow).

## Steuerwald's theorem on 3-perfect numbers

Let $N$, $a$, $b$ and $m$ be natural numbers
with $N = 2^a 3^b m$, $a \ge 1$, $b \ge 1$, and $m$ coprime to $6$. If $\sigma(N) = 3N$, where
$\sigma(N)$ is the sum of the divisors of $N$, then either $a = 1$ and $b \ne 1$, or $a \ne 1$
and $b = 1$.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL25/Almeida/almeida9.tex, lines 210-219.

Formalized by `MetaMathlibExt.steuerwald_three_perfect_exponents`, a theorem declared in [MathlibExt/NumberTheory/SteuerwaldThreePerfect.lean, line 1436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SteuerwaldThreePerfect.lean#L1436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html#steuerwald-three-perfect-exponents).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiperfect numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/perfect-numbers/multiperfect-numbers)
