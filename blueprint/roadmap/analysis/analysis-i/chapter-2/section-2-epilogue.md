# Chapter 2 epilogue: Isomorphism with the Mathlib natural numbers

> In this (technical) epilogue, we show that the "Chapter 2" natural numbers `Chapter2.Nat` are
> isomorphic in various senses to the standard natural numbers `ℕ`.
>
> After this epilogue, `Chapter2.Nat` will be deprecated, and we will instead use the standard
> natural numbers `ℕ` throughout.  In particular, one should use the full Mathlib API for `ℕ` for
> all subsequent chapters, in lieu of the `Chapter2.Nat` API.
>
> Filling the sorries here requires both the `Chapter2.Nat` API and the Mathlib API for the standard
> natural numbers `ℕ`.  As such, they are excellent exercises to prepare you for the aforementioned
> transition.
>
> In second half of this section we also give a fully axiomatic treatment of the natural numbers
> via the Peano axioms. The treatment in the preceding three sections was only partially axiomatic,
> because we used a specific construction `Chapter2.Nat` of the natural numbers that was an inductive
> type, and used that inductive type to construct a recursor.  Here, we give some exercises to show
> how one can accomplish the same tasks directly from the Peano axioms, without knowing the specific
> implementation of the natural numbers.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_2_epilogue.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_epilogue.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has no labelled items. It also has 22 declarations with no label, counted here but not shown.

## Depends on

- [Section 2.3: Multiplication](section-2-3.md)

## Sources

- [Analysis/Section_2_epilogue.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_epilogue.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_2_epilogue/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_2_epilogue.html)
