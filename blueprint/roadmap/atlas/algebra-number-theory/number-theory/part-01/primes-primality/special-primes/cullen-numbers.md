---
declaration: section
origin: cited
lean: MetaMathlibExt.sCullenNumber, MetaMathlibExt.IsSCullenNumber
statement: formalized
proof: formalized
---

# Cullen numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/cullen-numbers/index.html).

## The $s$-Cullen value

For natural numbers $s$ and $n$, the $s$-Cullen value is
$C_{n,s} = n s^n + 1$.

## Sources

- Jon Grantham and Hester Graves, *The abc Conjecture Implies That Only Finitely Many s-Cullen Numbers Are Repunits*, Journal of Integer Sequences 24 (2021), <https://cs.uwaterloo.ca/journals/JIS/VOL24/Grantham/gran4.tex>.

Formalized by `MetaMathlibExt.sCullenNumber`, a definition declared in [MathlibExt/NumberTheory/SCullenNumber.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SCullenNumber.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/cullen-numbers/index.html#s-cullen-number).

## $s$-Cullen numbers

For natural numbers $s$ and $n$, write $C_{n,s} = n s^n + 1$ for the
$s$-Cullen value. A natural number $m$ is an $s$-Cullen number when $s \ge 2$ and $m = C_{n,s}$
for some natural number $n \ge 1$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL24/Grantham/gran4.tex>.

Formalized by `MetaMathlibExt.IsSCullenNumber`, a definition declared in [MathlibExt/NumberTheory/SCullenNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SCullenNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/cullen-numbers/index.html#is-scullen-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cullen numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/primes-primality/special-primes/cullen-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/primes-primality/special-primes/cullen-numbers)
