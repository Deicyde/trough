---
declaration: section
origin: cited
lean: MathlibExt.InformationTheory.ShannonSourceCodingWanted.IsPrefixFree, MathlibExt.InformationTheory.ShannonSourceCodingWanted.shannon_source_coding_lower_bound, MathlibExt.InformationTheory.ShannonSourceCodingWanted.shannon_source_coding_upper_bound
statement: formalized
proof: formalized
---

# Shannon's source coding theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/shannon-s-source-coding-theorem/index.html).

## Prefix-free code (Shannon source coding)

A code $c$ assigning to each element of $\alpha$
a finite word over $\beta$ is prefix-free when, for all distinct $a_1, a_2 \in \alpha$, the word
$c(a_1)$ is not a prefix of the word $c(a_2)$. This is the general notion of a prefix-free code.

Formalized by `MathlibExt.InformationTheory.ShannonSourceCodingWanted.IsPrefixFree`, an abbreviation declared in [MathlibExt/InformationTheory/ShannonSourceCoding.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ShannonSourceCoding.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/shannon-s-source-coding-theorem/index.html#is-prefix-free).

## Shannon source coding lower bound

Let $\alpha$ and $\beta$ be finite types with
$q = |\beta| \ge 2$, and let $p : \alpha \to \mathbb{R}$ satisfy $p(a) > 0$ for every $a \in \alpha$
and $\sum_{a \in \alpha} p(a) = 1$. Let $c$ assign to each $a \in \alpha$ a finite word $c(a)$ over
$\beta$, of length $|c(a)|$, such that $c$ is injective and its set of codewords is uniquely
decodable: any two finite lists of codewords with the same concatenation are equal. Then the
expected length $\sum_{a \in \alpha} p(a)\,|c(a)|$ is at least the base-$q$ entropy
$-\left(\sum_{a \in \alpha} p(a) \log p(a)\right) / \log q$, where $\log$ is the natural logarithm.

## Sources

- C. E. Shannon, Bell Syst. Tech. J. 27 (1948), 379-423 and 623-656, DOI 10.1002/j.1538-7305.1948.tb01338.x.

Formalized by `MathlibExt.InformationTheory.ShannonSourceCodingWanted.shannon_source_coding_lower_bound`, a theorem declared in [MathlibExt/InformationTheory/ShannonSourceCoding.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ShannonSourceCoding.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/shannon-s-source-coding-theorem/index.html#shannon-source-coding-lower-bound).

## Shannon source coding upper bound

Let $\alpha$ and $\beta$ be finite types with
$q = |\beta| \ge 2$, and let $p : \alpha \to \mathbb{R}$ satisfy $p(a) > 0$ for every $a \in \alpha$
and $\sum_{a \in \alpha} p(a) = 1$. Then there is a prefix-free code $c$ assigning to each
$a \in \alpha$ a finite word $c(a)$ over $\beta$, of length $|c(a)|$, whose expected length
$\sum_{a \in \alpha} p(a)\,|c(a)|$ is strictly less than
$-\left(\sum_{a \in \alpha} p(a) \log p(a)\right) / \log q + 1$, where $\log$ is the natural
logarithm.

## Sources

- C. E. Shannon, Bell Syst. Tech. J. 27 (1948), 379-423 and 623-656, DOI 10.1002/j.1538-7305.1948.tb01338.x.

Formalized by `MathlibExt.InformationTheory.ShannonSourceCodingWanted.shannon_source_coding_upper_bound`, a theorem declared in [MathlibExt/InformationTheory/ShannonSourceCoding.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/InformationTheory/ShannonSourceCoding.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/shannon-s-source-coding-theorem/index.html#shannon-source-coding-upper-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Shannon's source coding theorem](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/shannon-s-source-coding-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/InformationTheory/source-coding/shannon-s-source-coding-theorem)
