---
declaration: section
origin: cited
lean: Cslib.Kolmogorov.pad, Cslib.Kolmogorov.card_lt_two_pow, Cslib.Kolmogorov.stringsOfLength, Cslib.Kolmogorov.card_compressible_lt, Cslib.Kolmogorov.exists_incompressible, Cslib.Kolmogorov.not_computable_K
statement: formalized
proof: formalized
---

# Incompressible strings, and Kolmogorov complexity is not computable

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html).

## Padding a string to a given length

For a natural number $n$ and a binary string $p$, the
padding of $p$ to length $n$ is the string $0^k 1 p$ with $k = \max(n - 1 - |p|, 0)$; when
$|p| < n$ it has length $n$.

Formalized by `Cslib.Kolmogorov.pad`, a definition declared in [CSLibExt/Computability/Kolmogorov/Incompressible.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Incompressible.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html#pad).

## Few strings have small complexity

Fewer than `2 ^ m` strings have complexity below `m`.
Padding their shortest descriptions to length `m` maps them injectively to strings of length `m`
other than `0ᵐ`.

Formalized by `Cslib.Kolmogorov.card_lt_two_pow`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Incompressible.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Incompressible.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html#card-lt-two-pow).

## Binary strings of a given length

For a natural number $n$, the finite set of all binary
strings of length $n$.

Formalized by `Cslib.Kolmogorov.stringsOfLength`, a definition declared in [CSLibExt/Computability/Kolmogorov/Incompressible.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Incompressible.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html#strings-of-length).

## Most strings are incompressible

For all natural numbers $n$ and $c$, fewer than
$2^{n-c}$ binary strings of length $n$ have Kolmogorov complexity less than $n - c$, where
$n - c$ is read as $0$ when $c > n$.

Hence at least $2^n - 2^{n-c} + 1$ strings of length $n$ have complexity at least $n - c$.

Formalized by `Cslib.Kolmogorov.card_compressible_lt`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Incompressible.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Incompressible.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html#card-compressible-lt).

## Incompressible strings exist at every length

Some string of length `n` has complexity at
least `n`.

Formalized by `Cslib.Kolmogorov.exists_incompressible`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Incompressible.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Incompressible.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html#exists-incompressible).

## Kolmogorov complexity is not computable

The function sending each binary string $x$
to its Kolmogorov complexity $K(x)$ is not computable: no partial recursive function, acting on
binary strings through their encodings as natural numbers, halts on every binary string $x$ with
output $K(x)$.

The proof is a form of Berry's paradox.

Formalized by `Cslib.Kolmogorov.not_computable_K`, a theorem declared in [CSLibExt/Computability/Kolmogorov/Incompressible.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Computability/Kolmogorov/Incompressible.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html#not-computable-k).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Incompressible strings, and Kolmogorov complexity is not computable](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/kolmogorov-complexity/incompressible-strings-and-kolmogorov-complexity)
