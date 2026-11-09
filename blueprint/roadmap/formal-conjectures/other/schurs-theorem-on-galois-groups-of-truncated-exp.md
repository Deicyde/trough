---
declaration: theorem
origin: cited
lean: SchurTruncatedExponential.schur_truncatedExp_galoisGroup_equiv
statement: formalized
---

# Schur's theorem on Galois groups of truncated exponential polynomials

> *Reference:* (https://math.stackexchange.com/questions/2814220)
>
> *Reference* (https://mathoverflow.net/questions/477077)

*Quoted from [FormalConjectures/Other/SchurTruncatedExponential.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SchurTruncatedExponential.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `SchurTruncatedExponential.schur_truncatedExp_galoisGroup_equiv`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/83f95df1123bfdc7937bb7358bb65f658c30d554/Proofs/T_SchurTruncatedExponential_schur_truncatedExp_galoisGroup_equiv.lean#L2204](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/83f95df1123bfdc7937bb7358bb65f658c30d554/Proofs/T_SchurTruncatedExponential_schur_truncatedExp_galoisGroup_equiv.lean#L2204).

> **Schur's Theorem (1924):**
> Let `f_n(x) = ∑_{j=0}^n x^j/j!` be the `n`-th truncated
> exponential polynomial over `ℚ`. Then for `n ≥ 2`:
>
> - If `n ≡ 0 (mod 4)`, the Galois group of `f_n` is isomorphic to the alternating group `A_n`
> - If `n ≢ 0 (mod 4)`, the Galois group of `f_n` is isomorphic to the symmetric group `S_n`

```lean
theorem schur_truncatedExp_galoisGroup_equiv (n : ℕ) (hn : n ≥ 2) :
  letI f := truncatedExp n
  if n % 4 = 0 then
    -- Galois group is alternating group A_n
    Nonempty (f.Gal ≃* alternatingGroup (Fin n))
  else
    -- Galois group is symmetric group S_n
    Nonempty (f.Gal ≃* Equiv.Perm (Fin n))
```

Category `research solved`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Other/SchurTruncatedExponential.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SchurTruncatedExponential.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Other/SchurTruncatedExponential.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Other/SchurTruncatedExponential.lean)
- [https://math.stackexchange.com/questions/2814220](https://math.stackexchange.com/questions/2814220)
