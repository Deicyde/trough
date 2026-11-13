---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.BinaryCode, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.dim, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.rate, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.distance, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.normalisedDistance, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.distanceFrom, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.normalisedDistanceFrom, MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.IsGood
statement: formalized
---

# Locally testable codes

11 results, 10 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html).

## Binary code

A binary code of length $n$ is a linear subspace of $\mathbb{F}_2^n$,
the vector space of words of length $n$ over the two-element field $\mathbb{F}_2$.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.BinaryCode`, an abbreviation declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#binary-code).

## Dimension of a binary code

The dimension of a binary code
$C \subseteq \mathbb{F}_2^n$ is its dimension as a vector space over $\mathbb{F}_2$.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.dim`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#dim).

## Rate of a binary code

The rate of a binary code $C \subseteq \mathbb{F}_2^n$ is its
dimension over $\mathbb{F}_2$ divided by its length $n$, as a real number; it is $0$ when
$n = 0$.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.rate`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#rate).

## Minimum distance of a binary code

The distance of a binary code
$C \subseteq \mathbb{F}_2^n$ is the smallest Hamming weight (number of nonzero coordinates) of
a nonzero codeword of $C$, and is $0$ if $C = \{0\}$.

When $C \neq \{0\}$, since $C$ is linear, this is the minimum Hamming distance between two
distinct codewords.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.distance`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#distance).

## Normalised distance of a binary code

The normalised distance of a binary code
$C \subseteq \mathbb{F}_2^n$ is its distance divided by its length $n$, as a real number; it is
$0$ when $n = 0$.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.normalisedDistance`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#normalised-distance).

## Distance from a word to a binary code

For a binary code $C \subseteq \mathbb{F}_2^n$
and a word $f \in \mathbb{F}_2^n$, the distance from $f$ to $C$ is the minimum, over all
codewords $c \in C$, of the Hamming distance between $f$ and $c$, that is, the number of
coordinates in which $f$ and $c$ differ.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.distanceFrom`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#distance-from).

## Normalised distance from a word to a binary code

For a binary code
$C \subseteq \mathbb{F}_2^n$ and a word $f \in \mathbb{F}_2^n$, the normalised distance from $f$
to $C$ is the distance from $f$ to $C$ (the Hamming distance from $f$ to a closest codeword)
divided by the length $n$, as a nonnegative real number; it is $0$ when $n = 0$.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.normalisedDistanceFrom`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#normalised-distance-from).

## Good family of codes

Let $(n_i)_{i \in \mathbb{N}}$ be natural numbers and, for each $i$,
let $C_i \subseteq \mathbb{F}_2^{n_i}$ be a binary code of length $n_i$. The family $(C_i)$ is
good if $n_i \to \infty$ as $i \to \infty$ and there is a real number $\varepsilon > 0$ such
that for every $i$ both the rate and the normalised distance of $C_i$ are at least
$\varepsilon$.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.IsGood`, a definition declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#is-good).

## Subsets with at most $q$ elements

For natural numbers $n$ and $q$, this is the
collection of all subsets $S \subseteq \{0, 1, \dots, n - 1\}$ with at most $q$ elements.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.cardLE`, an abbreviation declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#card-le).

## Locally testable code

Let $C \subseteq \mathbb{F}_2^n$ be a binary code, let $q$ be a
natural number and let $\kappa \ge 0$ be a real number. A $\kappa$-local tester for $C$ with
$q$ queries consists of a probability distribution on the subsets
$S \subseteq \{0, 1, \dots, n - 1\}$ with at most $q$ elements, together with, for each such
$S$, a set $V_S \subseteq \mathbb{F}_2^S$ of allowed local views, such that:
* if $f \in C$, then $f|_S \in V_S$ for every such $S$;
* for every $f \in \mathbb{F}_2^n$, the probability that $f|_S \notin V_S$ for a random $S$ is
  at least $\kappa$ times the normalised distance from $f$ to $C$.

The code $C$ is $\kappa$-locally testable with $q$ queries exactly when such a tester exists.

## Sources

- Definition 2.3 in `Locally Testable Codes with constant rate, distance, and locality` by I. Dinur, S. Evra, R. Livne, A. Lubotzky and S. Mozes. This probability distribution formulation is also mentioned immediately after Definition 1.1 in the original paper `Good Locally Testable Codes`.

Formalized by `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.LTC`, a structure declared in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#ltc).

## Good locally testable codes of every rate below one

For every real number $\rho$ with
$0 \le \rho < 1$ there exist a natural number $q$, a real number $\kappa > 0$, lengths
$n_i \in \mathbb{N}$ and binary codes $C_i$ of length $n_i$ for $i \in \mathbb{N}$ such that the
family $(C_i)_{i \in \mathbb{N}}$ is good and, for every $i$, the code $C_i$ is $\kappa$-locally
testable with $q$ queries and has rate at least $\rho$.

The source's theorem also asserts that the codes are explicit; explicitness is not part of this statement.

## Sources

- I. Dinur, S. Evra, R. Livne, A. Lubotzky, and S. Mozes, `Good Locally Testable Codes`, Annals of Math, 203 (2) 2026. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_good_lt_codes` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.GoodLTCodesWanted.GoodLTC.theorem_1_2` is written with `theorem_wanted` in [WantedExt/Combinatorics/GoodLTCodesWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/GoodLTCodesWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html#theorem-1-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Locally testable codes](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/error-correcting-codes/locally-testable-codes)
