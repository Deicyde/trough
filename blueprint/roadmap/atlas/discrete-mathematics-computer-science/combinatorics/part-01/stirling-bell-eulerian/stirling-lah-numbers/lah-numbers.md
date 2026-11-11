---
declaration: section
origin: cited
lean: MetaMathlibExt.unsignedLahNumber, MetaMathlibExt.signedLahNumber
statement: formalized
proof: formalized
---

# Lah numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lah-numbers/index.html).

## Unsigned Lah number

For natural numbers $n$ and $k$, the unsigned Lah number $L(n, k)$
is $\binom{n-1}{k-1} \frac{n!}{k!}$ when $1 \le k \le n$, $L(0, 0) = 1$, and $L(n, k) = 0$
otherwise.

$L(n, k)$ counts the partitions of an $n$-element set into $k$ nonempty linearly ordered blocks.

## Sources

- closed formula from Maxie D. Schmidt, *Jacobi-Type Continued Fractions for the Ordinary Generating Functions of Generalized Factorial Functions*, Journal of Integer Sequences 20 (2017): https://cs.uwaterloo.ca/journals/JIS/VOL20/Schmidt/schmidt14.tex.

Formalized by `MetaMathlibExt.unsignedLahNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LahNumber.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/LahNumber.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lah-numbers/index.html#unsigned-lah-number).

## Signed Lah number

For natural numbers $n$ and $k$, the signed Lah number is the integer
$(-1)^{n-k} L(n, k)$ when $k \le n$, where $L(n, k)$ is the unsigned Lah number, and $0$ when
$k > n$.

## Sources

- sign convention from Toufik Mansour, Matthias Schork, and Mark Shattuck, *The Generalized Stirling and Bell Numbers Revisited*, Journal of Integer Sequences 15 (2012): https://cs.uwaterloo.ca/journals/JIS/VOL15/Schork/schork2.tex.

Formalized by `MetaMathlibExt.signedLahNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/LahNumber.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/LahNumber.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lah-numbers/index.html#signed-lah-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lah numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lah-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/lah-numbers)
