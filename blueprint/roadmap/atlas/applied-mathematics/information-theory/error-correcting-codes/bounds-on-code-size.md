---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Coding.SingletonBound.singleton_bound, Hamming.ball, Hamming.card_ball, Hamming.card_ball_fin, MathlibExt.Combinatorics.Coding.HammingSpherePacking.hamming_sphere_packing_bound
statement: formalized
proof: formalized
---

# Bounds on code size

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html).

## Singleton bound

Let $\alpha$ be a nonempty finite alphabet with $q$ letters, and let $n$
and $d$ be natural numbers with $1 \le d \le n$. If $C$ is a set of words of length $n$ over
$\alpha$ in which any two distinct words are at Hamming distance at least $d$, then $C$ has at
most $q^{n - d + 1}$ elements.

The proof punctures the code to its first $n - d + 1$ coordinates: two codewords agreeing on all
retained coordinates can differ in at most the $d - 1$ deleted coordinates, contradicting the
minimum-distance hypothesis, so puncturing is injective on the code and the bound follows by
counting the punctured words.

## Sources

- R. C. Singleton, "Maximum distance q-nary codes", IEEE Transactions on Information Theory 10(2) (1964), 116–118, DOI 10.1109/TIT.1964.1053661.

Formalized by `MathlibExt.Combinatorics.Coding.SingletonBound.singleton_bound`, a theorem declared in [MathlibExt/Combinatorics/Coding/SingletonBound.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/SingletonBound.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html#singleton-bound).

## Closed Hamming ball

For finite types $\iota$ and $F$, a word $x : \iota \to F$ and a
natural number $e$, the closed Hamming ball of radius $e$ about $x$ is the finite set of all words
$y : \iota \to F$ whose Hamming distance from $x$ is at most $e$.

Formalized by `Hamming.ball`, a definition declared in [MathlibExt/InformationTheory/HammingBall.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/HammingBall.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html#ball).

## Size of a Hamming ball

For finite types $\iota$ and $F$, every word $x : \iota \to F$ and
every natural number $e$, the closed Hamming ball of radius $e$ about $x$ has
$\sum_{k=0}^{e} \binom{|\iota|}{k} (|F| - 1)^k$ elements.

Formalized by `Hamming.card_ball`, a theorem declared in [MathlibExt/InformationTheory/HammingBall.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/HammingBall.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html#card-ball).

## Size of a Hamming ball of fixed-length words

Let $n \ge 1$ and let $F$ be a finite
alphabet with $q \ge 2$ letters. For every word $x \in F^n$ and every natural number $e$, the
closed Hamming ball of radius $e$ about $x$ has $\sum_{k=0}^{e} \binom{n}{k} (q - 1)^k$ elements.

Formalized by `Hamming.card_ball_fin`, a theorem declared in [MathlibExt/InformationTheory/HammingBall.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/HammingBall.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html#card-ball-fin).

## Hamming bound

Let $\alpha$ be a finite alphabet with $q \ge 2$ letters, and let $n$ and
$t$ be natural numbers. If $C$ is a set of words of length $n$ over $\alpha$ in which any two
distinct words are at Hamming distance at least $2t + 1$, then

$$|C| \sum_{i=0}^{t} \binom{n}{i} (q - 1)^i \le q^n.$$

The proof packs disjoint radius-$t$ Hamming balls around the codewords into the ambient space:
the distance hypothesis forces the balls apart (any overlap would give a triangle-inequality
contradiction), and each ball contains exactly $\sum_{i=0}^{t} \binom{n}{i} (q - 1)^i$ words.

This is the $q$-ary generalization of Hamming's binary sphere-packing bound. The original paper
assumes binary words and derives the $2^n$ form; the same disjoint-ball counting argument gives
the formula stated here for an arbitrary finite alphabet.

Binary source: R. W. Hamming, "Error Detecting and Error Correcting Codes",
Bell System Technical Journal 29 (1950), 147–160,
DOI 10.1002/j.1538-7305.1950.tb00463.x.

Formalized by `MathlibExt.Combinatorics.Coding.HammingSpherePacking.hamming_sphere_packing_bound`, a theorem declared in [MathlibExt/Combinatorics/Coding/HammingSpherePacking.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Coding/HammingSpherePacking.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html#hamming-sphere-packing-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounds on code size](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/error-correcting-codes/bounds-on-code-size)
