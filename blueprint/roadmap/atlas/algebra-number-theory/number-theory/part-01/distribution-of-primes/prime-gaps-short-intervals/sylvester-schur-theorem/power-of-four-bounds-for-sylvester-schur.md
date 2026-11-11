---
declaration: section
origin: cited
lean: Nat.SylvesterSchur.central_erdos_layers_two_mul_add_two_lt_four_pow, Nat.SylvesterSchur.erdos_layers_le_four_pow, Nat.SylvesterSchur.erdos_layers_le_four_pow_three_layers
statement: formalized
proof: formalized
---

# Power-of-four bounds for Sylvester-Schur

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/power-of-four-bounds-for-sylvester-schur/index.html).

## Central Erdős layer estimate

Let $n \ge 512$ be a natural number and $N = 2n + 2$. For a
natural number $x$ write $x\#$ for the primorial of $x$, the product of all primes $p \le x$, and
let $L = \lfloor \log_2 N \rfloor$. Then
$n \cdot \lfloor N/3 \rfloor\# \cdot \prod_{m=2}^{L} \lfloor N^{1/m} \rfloor\# < 4^n$.

Formalized by `Nat.SylvesterSchur.central_erdos_layers_two_mul_add_two_lt_four_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosPowerBounds.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ErdosPowerBounds.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/power-of-four-bounds-for-sylvester-schur/index.html#central-erdos-layers-two-mul-add-two-lt).

## Power-of-four bound for the Erdős layer product

Let $N$ and $r$ be natural numbers. For
a natural number $x$ write $x\#$ for the primorial of $x$, the product of all primes $p \le x$.
Let $L = \lfloor \log_2 N \rfloor$, with $L = 0$ when $N = 0$, and let $P = 1$ if $L = 0$ and
$P = r\# \cdot \prod_{m=2}^{L} \lfloor N^{1/m} \rfloor\#$ if $L \ge 1$. Then
$P \le 4^{r + \lfloor \sqrt{N} \rfloor L}$.

This is a coarse bound, weaker than the full Erdős estimate, but much sharper than replacing the
first layer by $\lfloor N/3 \rfloor$ when $N$ is several multiples of $r$.

Formalized by `Nat.SylvesterSchur.erdos_layers_le_four_pow`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosPowerBounds.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ErdosPowerBounds.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/power-of-four-bounds-for-sylvester-schur/index.html#erdos-layers-le-four-pow).

## Three-layer power-of-four bound for the Erdős layer product

Let $N$ and $r$ be natural
numbers. For a natural number $x$ write $x\#$ for the primorial of $x$, the product of all primes
$p \le x$. Let $L = \lfloor \log_2 N \rfloor$, with $L = 0$ when $N = 0$, and let $P = 1$ if
$L = 0$ and $P = r\# \cdot \prod_{m=2}^{L} \lfloor N^{1/m} \rfloor\#$ if $L \ge 1$. Then
$P \le 4^{r + \lfloor \sqrt{N} \rfloor + \lfloor N^{1/3} \rfloor L}$.

The first layer contributes $r$, the second $\lfloor \sqrt{N} \rfloor$, and all remaining layers
are controlled by the cube root of $N$. This is the reusable form of the estimate used in
Erdős's case split.

Formalized by `Nat.SylvesterSchur.erdos_layers_le_four_pow_three_layers`, a theorem declared in [MathlibExt/NumberTheory/SylvesterSchur/ErdosPowerBounds.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/SylvesterSchur/ErdosPowerBounds.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/power-of-four-bounds-for-sylvester-schur/index.html#erdos-layers-le-four-pow-three-layers).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Power-of-four bounds for Sylvester-Schur](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/power-of-four-bounds-for-sylvester-schur/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/sylvester-schur-theorem/power-of-four-bounds-for-sylvester-schur)
