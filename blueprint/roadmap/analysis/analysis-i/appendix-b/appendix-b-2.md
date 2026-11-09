---
declaration: theorem
origin: cited
lean: AppendixB.NNRealDecimal.toNNReal_conv, AppendixB.NNRealDecimal.not_inj, AppendixB.RealDecimal.not_inj_one, AppendixB.TerminatingDecimal
statement: formalized
---

# Appendix B.2: The decimal representation of real numbers

> An implementation of the decimal representation of Mathlib's real numbers `ℝ`.
>
> This is separate from the way decimal numerals are already represented in Mathlib.  We also represent the integer part of the natural numbers just by `ℕ`, avoiding using the decimal representation from the
> previous section, although we still retain the `AppendixB.Digit` class.

*Quoted from [Analysis/Appendix_B_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 5 declarations: 1 proved here, 3 stated without proof (3 of them exercises) and 1 definition. It also has 9 declarations with no label, counted here but not shown.

## Exercise B.2.1

`AppendixB.NNRealDecimal.toNNReal_conv` (theorem, [line 31](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean#L31)). An exercise, stated without proof.

> Exercise B.2.1

```lean
theorem NNRealDecimal.toNNReal_conv (d:NNRealDecimal) :
  Summable fun i ↦ (d.fracPart i) * (10:NNReal) ^ (-i-1:ℝ)
```

## Proposition B.2.2

`AppendixB.NNRealDecimal.not_inj` (theorem, [line 88](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean#L88)). Proved here.

> Proposition B.2.2

```lean
theorem NNRealDecimal.not_inj : (1:NNReal) = (mk 1 fun _ ↦ 0) ∧ (1:NNReal) = (mk 0 fun _ ↦ 9)
```

## Exercise B.2.2

`AppendixB.RealDecimal.not_inj_one` (theorem, [line 126](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean#L126)). An exercise, stated without proof.

> Exercise B.2.2

```lean
theorem RealDecimal.not_inj_one (d: RealDecimal) : (d:ℝ) = 1 ↔ (d = pos (mk 1 fun _ ↦ 0) ∨ d = pos (mk 0 fun _ ↦ 9))
```

## Exercise B.2.3

`AppendixB.TerminatingDecimal` (abbrev, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean#L130)). A definition.

> Exercise B.2.3

```lean
abbrev TerminatingDecimal (x:ℝ) : Prop
```

## Exercise B.2.4

An `example` ([line 137](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean#L137)). An exercise, stated without proof.

> Exercise B.2.4.  This is Corollary 8.3.4, but the intent is to rewrite the proof using the decimal system.

```lean
example : Uncountable ℝ
```

## Depends on

- [Appendix B.1: The decimal representation of natural numbers](appendix-b-1.md)

## Sources

- [Analysis/Appendix_B_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_B_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_B_2.html)
