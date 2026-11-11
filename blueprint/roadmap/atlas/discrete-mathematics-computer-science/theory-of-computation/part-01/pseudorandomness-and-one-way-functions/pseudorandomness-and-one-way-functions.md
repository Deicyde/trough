---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.NisanWigderson.nisan_wigderson, MetaMathlibExt.Complexity.KeyTheorems.OWFImpliesPNeNP.owf_implies_p_ne_np
statement: formalized
---

# Pseudorandomness and one-way functions: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/index.html).

Complexity-theoretic foundations of cryptography and derandomization: one-way functions, hardcore predicates (Goldreich–Levin), hardness amplification (Yao's XOR lemma), hardness-versus-randomness generators (Nisan–Wigderson), and Impagliazzo's five worlds.

## Nisan-Wigderson: exponential hardness in E derandomizes BPP

Suppose there are a decision
problem $f$ in E and a natural number $c > 0$ such that, for every $n$, every well-formed flat
Boolean circuit $C$ on $n$ inputs without mod gates that computes $f$ on all bitstrings of length
$n$ (for every bitstring $x$ of length $n$, the value of its last gate on input $x$ is $f(x)$)
satisfies $|C|^c \ge 2^n$, where $|C|$ is its number of gates; that is, $C$ has at least $2^{n/c}$
gates. Then BPP equals P.

## Sources

- N. Nisan and A. Wigderson, "Hardness vs randomness", Journal of Computer and System Sciences 49 (1994), 149-167 (FOCS 1988).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.NisanWigderson.nisan_wigderson` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/NisanWigdersonWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/NisanWigdersonWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/index.html#nisan-wigderson).

## One-way functions imply P ≠ NP

If some family $f$, assigning to each natural number $n$
and each $n$-bit string $x$ a bitstring $f_n(x)$, is a one-way function family, then
$\mathrm{P} \neq \mathrm{NP}$.

## Sources

- O. Goldreich, Foundations of Cryptography, Vol. 1, Cambridge University Press, 2001, Section 2.2 (one-way functions imply P ≠ NP); R. Impagliazzo, "A personal view of average-case complexity", Proceedings of the Tenth Annual Structure in Complexities Theory Conference (1995), 134-147 (five worlds).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.OWFImpliesPNeNP.owf_implies_p_ne_np` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/OWFImpliesPNeNPWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Complexity/KeyTheorems/OWFImpliesPNeNPWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/index.html#owf-implies-p-ne-np).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pseudorandomness and one-way functions](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/TheoryOfComputation/pseudorandomness-and-one-way-functions)
