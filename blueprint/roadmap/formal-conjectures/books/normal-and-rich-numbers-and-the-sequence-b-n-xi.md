---
declaration: theorem
origin: cited
lean: BugeaudNormalAndRich.isNormalInBase_iff_isEquidistributedModuloOne, BugeaudNormalAndRich.isRichInBase_iff_dense
statement: formalized
---

# Normal and rich numbers and the sequence $(b^n \xi)$ modulo one

> Let $b \ge 2$ be an integer. A real number $\xi$ is normal in base $b$ if and only if the
> sequence $(b^n \xi)_{n \ge 0}$ is uniformly distributed modulo one. This was proved by Wall
> [Wal49]; see also [Bug12, Theorem 4.14] and [EvdPSW03, p. 127].
>
> A real number $\xi$ is rich (or disjunctive) in base $b$ if every finite block of digits occurs in
> its base-$b$ expansion. By the same argument, $\xi$ is rich in base $b$ if and only if the
> sequence $(b^n \xi)_{n \ge 0}$ is dense modulo one [Bug12, Section 4.4].
>
> The two easy implications, normal implies rich and uniformly distributed implies dense, are
> `NormalNumber.IsNormalInBase.isRichInBase` and `IsEquidistributedModuloOne.dense_range`.
>
> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Cambridge Tracts in Mathematics 193. Cambridge University Press, 2012. Chapter 4.
>   - [Wal49] Wall, Donald Dines. "Normal numbers." Ph.D. thesis, University of California,
>     Berkeley, 1949.
>   - [EvdPSW03] Everest, Graham, Alf van der Poorten, Igor Shparlinski, and Thomas Ward.
>     "Recurrence sequences." Mathematical Surveys and Monographs 104. American Mathematical
>     Society, Providence, RI, 2003.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `BugeaudNormalAndRich.isNormalInBase_iff_isEquidistributedModuloOne`

Solved: stated here; a Lean proof is at [https://github.com/rwst/formal-conjectures/blob/a522a5352dd28df0b5ef08c213c368b5f6a5df6e/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean#L459](https://github.com/rwst/formal-conjectures/blob/a522a5352dd28df0b5ef08c213c368b5f6a5df6e/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean#L459).

> A real number $\xi$ is normal in base $b$ if and only if $(b^n \xi)_{n \ge 0}$ is uniformly
> distributed modulo $1$ [Wal49], [Bug12, Theorem 4.14].

```lean
theorem isNormalInBase_iff_isEquidistributedModuloOne (b : ℕ) (hb : 2 ≤ b) (ξ : ℝ) :
    IsNormalInBase b ξ ↔ IsEquidistributedModuloOne fun n => (b : ℝ) ^ n * ξ
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean#L55).

## `BugeaudNormalAndRich.isRichInBase_iff_dense`

Textbook result, stated without proof. A Lean proof is at [https://github.com/rwst/formal-conjectures/blob/a522a5352dd28df0b5ef08c213c368b5f6a5df6e/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean#L466](https://github.com/rwst/formal-conjectures/blob/a522a5352dd28df0b5ef08c213c368b5f6a5df6e/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean#L466).

> A real number $\xi$ is rich in base $b$ if and only if $(b^n \xi)_{n \ge 0}$ is dense
> modulo $1$ [Bug12, Section 4.4].

```lean
theorem isRichInBase_iff_dense (b : ℕ) (hb : 2 ≤ b) (ξ : ℝ) :
    IsRichInBase b ξ ↔ Dense (Set.range fun n => (↑((b : ℝ) ^ n * ξ) : AddCircle (1 : ℝ)))
```

Category `textbook`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean)
