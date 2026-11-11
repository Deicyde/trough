---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSignedPowTwoSum, MetaMathlibExt.isSignedPowTwoSum_one, MetaMathlibExt.isSignedPowTwoSum_iff, MetaMathlibExt.isSignedPowTwoSum_extend, MetaMathlibExt.one_add_signedPowTwoSum_iff
statement: formalized
---

# Signed binary representations

5 results, 2 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html).

## Signed power-of-two sums

For natural numbers $m$, $s$ and $t$, an integer $n$ is a signed
power-of-two sum with coefficients in $\{-1, m\}$ over the range $s \le j \le t$ if
$n = \sum_{j=s}^{t} \lambda_j 2^j$ for some integers $\lambda_j$ with every
$\lambda_j \in \{-1, m\}$.

## Sources

- Ross, *A Perfect Number Generalization and Some Euclid-Euler Type Results*, JIS 27 (2024), Article 24.7.5, Lemma 7.

Formalized by `MetaMathlibExt.IsSignedPowTwoSum`, a definition declared in [WantedExt/NumberTheory/SignedBinarySumWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SignedBinarySumWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html#is-signed-pow-two-sum).

## Example of a signed power-of-two sum

The integer $1$ can be written as
$\sum_{j=0}^{1} \lambda_j 2^j$ with every $\lambda_j \in \{-1, 3\}$, namely
$1 = 3 \cdot 2^0 + (-1) \cdot 2^1$.

## Sources

- Ross, *A Perfect Number Generalization and Some Euclid-Euler Type Results*, JIS 27 (2024), Article 24.7.5, Lemma 7.

Formalized by `MetaMathlibExt.isSignedPowTwoSum_one`, a theorem declared in [WantedExt/NumberTheory/SignedBinarySumWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SignedBinarySumWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html#is-signed-pow-two-sum-one).

## Interval and congruence characterization of signed power-of-two sums

Let $m \ge 1$ and
$s \le t$ be natural numbers and put $L = t - s + 1$. An integer $n$ can be written as
$\sum_{j=s}^{t} \lambda_j 2^j$ with every $\lambda_j \in \{-1, m\}$ if and only if
$-2^s (2^L - 1) \le n \le 2^s m (2^L - 1)$ and $n \equiv -2^s (2^L - 1) \pmod{2^s (m + 1)}$.

## Sources

- Ross, *A Perfect Number Generalization and Some Euclid-Euler Type Results*, JIS 27 (2024), Article 24.7.5, Lemma 7 (`jis-2024-24.7.5-lem-7`): for `0 ≤ s ≤ t` and `m ≥ 1`, the integers of the form `∑_{j=s}^{t} λⱼ * 2^j` with `λⱼ ∈ {-1, m}` are precisely the integers `n` in the interval `[-2^s * (2^{t-s+1} - 1), 2^s * m * (2^{t-s+1} - 1)]` satisfying `n ≡ -2^s * (2^{t-s+1} - 1) [ZMOD 2^s * (m + 1)]`.

Stated but not proved: `MetaMathlibExt.isSignedPowTwoSum_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/SignedBinarySumWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SignedBinarySumWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html#is-signed-pow-two-sum-iff).

## Extending a signed power-of-two sum to a longer range

Let $m \ge 1$, $s$, $t$ and $\alpha$
be natural numbers, let $\beta = \nu_2(m + 1)$ be the exponent of $2$ in $m + 1$, and suppose that
$s + \beta \le t + 1$ and $2^\alpha \equiv 1 \pmod{(m + 1)/2^\beta}$. If an integer $n$ can be
written as $\sum_{j=s}^{t} \lambda_j 2^j$ with every $\lambda_j \in \{-1, m\}$, then $n$ can also be
written as $\sum_{j=s}^{t+\alpha} \mu_j 2^j$ with every $\mu_j \in \{-1, m\}$.

The source's hypothesis $t \ge s + \beta - 1$ is written as $s + \beta \le t + 1$ to cover the
case $\beta = 0$.

## Sources

- Ross, *A Perfect Number Generalization and Some Euclid-Euler Type Results*, JIS 27 (2024), Article 24.7.5, Corollary 8 (`jis-2024-24.7.5-cor-8`): fix `m ≥ 1` and let `β = ν₂(m + 1)`. If `n` is a signed power-of-two sum over `[s, t]` with `t ≥ s + β - 1`, then `n` is also expressible over `[s, t + α]` whenever `2^α ≡ 1 [(m + 1) / 2^β]`.

Stated but not proved: `MetaMathlibExt.isSignedPowTwoSum_extend` is written with `theorem_wanted` in [WantedExt/NumberTheory/SignedBinarySumWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SignedBinarySumWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html#is-signed-pow-two-sum-extend).

## Integers that are one plus a signed sum of powers of two

An integer $n$ can be written as
$n = 1 + \sum_{j=1}^{k} \lambda_j 2^j$ for some $k \ge 1$ and some
$\lambda_1, \dots, \lambda_k \in \{-1, 1\}$ if and only if $n \equiv 3 \pmod 4$.

## Sources

- Ross, *A Perfect Number Generalization and Some Euclid-Euler Type Results*, JIS 27 (2024), Article 24.7.5, Lemma 12 (`jis-2024-24.7.5-lem-12`): an integer `n` can be written as `1 + ∑_{j=1}^{k} λⱼ * 2^j` for some `k ≥ 1` and coefficients `λⱼ ∈ {-1, 1}` if and only if `n ≡ 3 [ZMOD 4]`.

Stated but not proved: `MetaMathlibExt.one_add_signedPowTwoSum_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/SignedBinarySumWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/SignedBinarySumWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html#one-add-signed-pow-two-sum-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Signed binary representations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/signed-binary-representations)
