---
declaration: section
origin: cited
lean: MetaMathlibExt.lcm_product_identity
statement: formalized
proof: formalized
---

# Arithmetic functions: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/index.html).

Divisor sums, totients, Möbius and multiplicative functions, their mean values and extremal orders, and integers classified by them.

## The LCM product identity

For every natural number $n$, the product of
$p^{\lfloor n/(p-1) \rfloor}$ over the primes $p \le n + 1$ equals the least common multiple of all
products $i_1 i_2 \cdots i_n$ of $n$ positive integers with $i_1 + \cdots + i_n \le 2n$.

Since $\lfloor n/(p-1) \rfloor = 0$ for $p > n + 1$, the left side is the product of
$p^{\lfloor n/(p-1) \rfloor}$ over all primes $p$.

## Sources

- Abdelmalek Bedhouche and Bakir Farhi, "On Some Products Taken over Prime Numbers," Journal of Integer Sequences 26 (2023), Article 23.1.5, Corollary, lines 335–340, https://cs.uwaterloo.ca/journals/JIS/VOL26/Farhi/farhi32.tex

Formalized by `MetaMathlibExt.lcm_product_identity`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LcmProductIdentity.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LcmProductIdentity.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/index.html#lcm-product-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions)
