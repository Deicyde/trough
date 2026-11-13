---
declaration: section
origin: cited
lean: MetaMathlibExt.frisch_alternating_reciprocal_binomial, MetaMathlibExt.klamkin_binomial_reciprocal_identity
statement: formalized
proof: formalized
---

# Sums of reciprocals of binomial coefficients

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/sums-of-reciprocals-of-binomial-coefficients/index.html).

## Frisch's alternating reciprocal-binomial identity

For natural numbers $n$, $b$ and $c$
with $0 < c \le b$, the rational numbers
$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \binom{b+k}{c}^{-1}$ and
$\frac{c}{n+c} \binom{n+b}{b-c}^{-1}$ are equal.

## Sources

- H. W. Gould and Jocelyn Quaintance, "On the Binomial Identities of Frisch and Klamkin," Journal of Integer Sequences 19 (2016), who attribute the identity to Ragnar Frisch, "Sur les semi-invariants et moments employés dans l'étude des distributions statistiques" (1926); lines 92–95 of <https://cs.uwaterloo.ca/journals/JIS/VOL19/Gould/gould8.tex>. The inverse Frisch identity, Abel's infinite variant and the Klamkin identities are not included.

Formalized by `MetaMathlibExt.frisch_alternating_reciprocal_binomial`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FrischReciprocalBinomial.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/FrischReciprocalBinomial.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/sums-of-reciprocals-of-binomial-coefficients/index.html#frisch-alternating-reciprocal-binomial).

## Klamkin's binomial reciprocal identity

For natural numbers $n$, $b$ and $x$ with
$n + b \le x$, the following equality of rational numbers holds:

$$\sum_{k=0}^{n} \frac{\binom{n}{k}}{\binom{x}{k+b}} = \frac{x+1}{(x-n+1)\binom{x-n}{b}}.$$

## Sources

- H. W. Gould and Jocelyn Quaintance, "On the Binomial Identities of Frisch and Klamkin," Journal of Integer Sequences 19 (2016), Article 16.7.7, Eq. `klam1a`, lines 105–107, <https://cs.uwaterloo.ca/journals/JIS/VOL19/Gould/gould8.tex>.

Formalized by `MetaMathlibExt.klamkin_binomial_reciprocal_identity`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/KlamkinBinomialReciprocal.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/KlamkinBinomialReciprocal.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/sums-of-reciprocals-of-binomial-coefficients/index.html#klamkin-binomial-reciprocal-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of reciprocals of binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/sums-of-reciprocals-of-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/sums-of-reciprocals-of-binomial-coefficients)
