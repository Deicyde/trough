---
declaration: section
origin: cited
lean: MetaMathlibExt.riordanNumber, MetaMathlibExt.riordanNumber_eq_sum
statement: formalized
proof: formalized
---

# Riordan numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/riordan-numbers/index.html).

## Riordan numbers

For a natural number $n$, the $n$-th Riordan number is the integer

$$r_n = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} C_k,$$

where $C_k$ is the $k$-th Catalan number.

## Sources

- closed form (Kirgizov lines 436-438).

Formalized by `MetaMathlibExt.riordanNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/RiordanNumber.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RiordanNumber.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/riordan-numbers/index.html#riordan-number).

## Riordan numbers as an alternating Catalan sum

For every natural number $n$, the $n$-th
Riordan number $r_n$ equals

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} C_k,$$

where $C_k$ is the $k$-th Catalan number.

Formalized by `MetaMathlibExt.riordanNumber_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/RiordanNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/RiordanNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/riordan-numbers/index.html#riordan-number-eq-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Riordan numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/riordan-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/riordan-numbers)
