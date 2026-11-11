---
declaration: section
origin: cited
lean: MetaMathlibExt.tangentNumber_two_adic_divisibility_mod_six, MetaMathlibExt.weightedAffinePowerSum
statement: formalized
proof: formalized
---

# Bernoulli, Euler and Genocchi numbers: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/index.html).

Combinatorial formulas for Bernoulli, Euler, tangent and Genocchi numbers (Garabedian's formulas, median Euler and Genocchi numbers, Euler–Seidel matrices, Carlitz q-Bernoulli polynomials), their divisibility, and sums of powers via Faulhaber coefficients.

## Tangent numbers: 2-adic divisibility and a congruence mod 6

Let $T \colon \mathbb{N} \to
\mathbb{Z}$ satisfy $T(0) = 0$ and, for every $m \in \mathbb{N}$,

$$T(m+1) = [m = 0] - \sum_{k=0}^{m} \binom{m}{k} T(k)\, T(m-k),$$

where $[m = 0]$ is $1$ if $m = 0$ and $0$ otherwise. Then for every $n \ge 1$, $2^n$ divides
$T(2n+1)$ and $T(2n+1)/2^n \equiv (-1)^n 4^{n-1} \pmod 6$.

These conditions determine $T$: its values are the coefficients of the exponential generating
function of $\tanh x$, the signed tangent numbers (unsigned, OEIS A009006). The source defines
the tangent numbers through $1 + \tanh x$, which agrees with this recurrence at odd indices.

## Sources

- Kwang-Wu Chen, "An Interesting Lemma for Regular C-fractions," Journal of Integer Sequences 6 (2003), Article 03.4.8, Theorem, equation, lines 362–369 (tangent numbers defined at lines 351–360), https://cs.uwaterloo.ca/journals/JIS/VOL6/Chen/chen53.tex

Formalized by `MetaMathlibExt.tangentNumber_two_adic_divisibility_mod_six`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TangentNumberDivisibility.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/TangentNumberDivisibility.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/index.html#tangent-number-two-adic-divisibility-mod).

## Weighted affine power sum

Let $R$ be a ring, $a, b$ integers, $u \in R$ and $n, p$
natural numbers. The weighted affine power sum is

$$S_p(a, b; u, n + 1) = \sum_{k=0}^{n} u^k (ak + b)^p,$$

computed in $R$ with $a$, $b$ and $k$ mapped into $R$.

Unlike later generating-function identities in the source, this finite definition does not
require $u$ to be nonzero.

Formalized by `MetaMathlibExt.weightedAffinePowerSum`, a definition declared in [MathlibExt/Combinatorics/Enumerative/WeightedAffinePowerSum.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/WeightedAffinePowerSum.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/index.html#weighted-affine-power-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli, Euler and Genocchi numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi)
