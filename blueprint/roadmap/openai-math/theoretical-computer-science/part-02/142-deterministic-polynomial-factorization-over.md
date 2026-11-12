---
declaration: section
origin: cited
---

# 142. Deterministic polynomial factorization over prime fields

1 manuscript, with no Lean, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives a uniform deterministic algorithm that completely factors every nonzero dense degree-*n* polynomial over a prime field 𝔽$_{p}$, including multiplicities, in bit complexity polynomial in $(n+1)\log p$. The prime is supplied in binary. No randomness, integer-factorization or primitive-root oracle, or GRH assumption is required.

## Deterministic Polynomial Factorization over Prime Fields

We give a uniform deterministic polynomial-time algorithm for complete factorization over prime fields. For a prime *p* in binary and a nonzero polynomial $f\in\mathbf F_p[x]$ given by its dense coefficient list, the algorithm computes the irreducible factors and their multiplicities using a number of bit operations polynomial in $(\deg f+1)\log p$. The proof uses the uniform Hecke zero-free theorem from the companion paper *Primitive roots for every admissible integer base*.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/Deterministic-Polynomial-Factorization-over-Prime-Fields.pdf).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
