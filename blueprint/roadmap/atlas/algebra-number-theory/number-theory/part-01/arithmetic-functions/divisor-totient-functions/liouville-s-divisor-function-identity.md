---
declaration: section
origin: cited
lean: MetaMathlibExt.liouville_divisor_function_identity_general, MetaMathlibExt.liouville_divisor_function_identity
statement: formalized
proof: formalized
---

# Liouville's divisor-function identity

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/liouville-s-divisor-function-identity/index.html).

## Liouville's divisor-function identity for all natural numbers

For every natural number
$n$, writing $\tau(d)$ for the number of positive divisors of $d$,

$$\left(\sum_{d \mid n} \tau(d)\right)^2 = \sum_{d \mid n} \tau(d)^3,$$

where both sums run over the positive divisors $d$ of $n$. By convention the divisor set of $0$
is empty here, so for $n = 0$ both sides are $0$.

Formalized by `MetaMathlibExt.liouville_divisor_function_identity_general`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/LiouvilleDivisorIdentity.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/LiouvilleDivisorIdentity.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/liouville-s-divisor-function-identity/index.html#liouville-divisor-function-identity-gene).

## Liouville's divisor-function identity

For every positive integer $n$, writing $\tau(d)$
for the number of positive divisors of $d$,

$$\left(\sum_{d \mid n} \tau(d)\right)^2 = \sum_{d \mid n} \tau(d)^3,$$

where both sums run over the positive divisors $d$ of $n$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, “Translations and Extensions of the Nicomachean Identity,” Journal of Integer Sequences 27 (2024), lines 317–322, <https://cs.uwaterloo.ca/journals/JIS/VOL27/Kim/kim8.tex>. Here `d.divisors.card` is the source's divisor-count function. It follows from `liouville_divisor_function_identity_general`; the hypothesis `hn` is unused and keeps the source's shape (at `n = 0` both sides are `0`, since `Nat.divisors 0 = ∅`).

Formalized by `MetaMathlibExt.liouville_divisor_function_identity`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/LiouvilleDivisorIdentity.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/LiouvilleDivisorIdentity.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/liouville-s-divisor-function-identity/index.html#liouville-divisor-function-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Liouville's divisor-function identity](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/liouville-s-divisor-function-identity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/liouville-s-divisor-function-identity)
